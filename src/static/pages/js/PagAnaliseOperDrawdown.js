
async function iniciarAnimacaoPesquisarAnaliseOperDrawdown() {
	$("#iRefreshOperDrawdown").addClass("fa-spin");
	$("#btnAnaliseOperDrawdownPesquisar").addClass("disabled");
}

async function finalizarAnimacaoPesquisarAnaliseOperDrawdown() {
	$("#iRefreshOperDrawdown").removeClass("fa-spin");
	$("#btnAnaliseOperDrawdownPesquisar").removeClass("disabled");
}

async function fCarregarConfigAnaliseOperDrawdown( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "perfil/config",
				data: { tipo: 'DRAWDOWN_DIAS', valor: '120' },
				success: function(result) {
					var resultado = result.data.Resultado;
					var mensagem  = result.data.Mensagem;
					var Config    = result.data.Dados;
					if (resultado == "NOK") {
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
						return false;
					} else if (resultado == "OK") {
					    var valor = Config.Valor;
					    valor = parseInt(valor);
					    $("#txtFiltroAnaliseOperDrawdownDias").val(valor);
						return true;
					} else {
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return false;
					}
				},
				error: function(data) {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
					return false;
				}
			});

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "perfil/config",
				data: { tipo: 'DRAWDOWN_MARGEM', valor: '20' },
				success: function(result) {
					var resultado = result.data.Resultado;
					var mensagem  = result.data.Mensagem;
					var Config    = result.data.Dados;
					if (resultado == "NOK") {
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
						return false;
					} else if (resultado == "OK") {
					     var valor = Config.Valor;
					     var tamanho = valor.toString().length;
					     if ( valor.toString().substring(tamanho-2, tamanho) == ',0' ) valor = valor.toString().replace(',0', '');
					     if ( valor.toString().substring(tamanho-2, tamanho) == '.0' ) valor = valor.toString().replace('.0', '');
					    $("#txtFiltroAnaliseOperDrawdownMargem").val(valor);
						return true;
					} else {
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return false;
					}
				},
				error: function(data) {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
					return false;
				}
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fLimparGridAnaliseOperDrawdown( urlPadrao ){
	fLimparAreaAlerta("AreaAlertaPrincAnaliseOperDrawdown");
	$("#txtFiltroAnaliseOperDrawdownDias").val("120");
	$("#txtFiltroAnaliseOperDrawdownMargem").val("20,00");
	fLimparSomenteGridAnaliseOperDrawdown( urlPadrao );
}

async function fLimparSomenteGridAnaliseOperDrawdown( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			finalizarAnimacaoPesquisarAnaliseOperDrawdown();

			$("th").addClass('text-center');

			$('#GridAnaliseOperDrawdown').dataTable().fnClearTable();
			$("#GridAnaliseOperDrawdown").dataTable({ bDestroy: true }).fnDestroy();

			$('#GridAnaliseOperDrawdown').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: true,  sWidth: "30px",  targets: 0 }, // 0-Origem
					{ bSortable: true,  sWidth: "20px",  targets: 1 }, // 1-Tipo
					{ bSortable: true,  sWidth: "30px",  targets: 2 }, // 2-Ativo
					{ bSortable: true,  sWidth: "30px",  targets: 3 }, // 3-Cotação
					{ bSortable: true,  sWidth: "30px",  targets: 4 }, // 4-Máxima
					{ bSortable: true,  sWidth: "30px",  targets: 5 }, // 5-Drawdown
					{ bSortable: true,  sWidth: "30px",  targets: 6 }, // 6-Margem
					{ bSortable: true,  sWidth: "100px", targets: 7 }, // 7-Situação
					{ bSortable: false, sWidth: "30px",  targets: 8 }  // 8-Acao
				],
			    order: [[ 6, "desc" ]], // 6-Margem
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				searchable: false,
				orderable: true,
				bAutoWidth: false,
				bPaginate: false,
				ordering: true
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fMontarGridAnaliseOperDrawdown( urlPadrao, dataSet ){
	try {

	    // Manter/Vender      -        0% : preço está na máxima do mercado.
	    // Manter             -  0% a 10% : preço está abaixo da metade do ponto de compra.
	    // Acompanhar         - 10% a 15% : indica acompanhamento do preço.
	    // Acompanhar/Comprar - 15% a 20% : preço já está perto do ponto do preço de entrada.
	    // Comprar            -       20% : ponto de compra

	    var margemDigitada    = $("#txtFiltroAnaliseOperDrawdownMargem").val();
	    var margemMetadeAbaxo = parseFloat( 0.00 );
	    var margemMetadeAcima = parseFloat( 0.00 );

	    margemDigitada = parseFloat(GetValorDecimal( margemDigitada.toString().replace('.', ',') ));

	    if ( margemDigitada    > 0.0 ) margemMetadeAbaxo = parseFloat( margemDigitada / 2 );
	    if ( margemMetadeAbaxo > 0.0 ) margemMetadeAcima = parseFloat( margemMetadeAbaxo + ( margemMetadeAbaxo / 2 ) );

		 promise = new Promise( (resolve, reject) => {

            $('#GridAnaliseOperDrawdown').DataTable( {
				processing: true,
				serverSide: false,
				iDisplayLength: 10,
				oLanguage: fTraduzirGrid(),
				data: dataSet,
				aoColumns: [
					{ bSortable: true,  sWidth: "30px",  targets: 0 }, // 0-Origem
					{ bSortable: true,  sWidth: "20px",  targets: 1, render: function ( data, type, row ) {  if ( type == "display" && row[1] == 'ACAO' ) return 'AÇÃO';  return data;  } }, //  1-Tipo
					{ bSortable: true,  sWidth: "30px",  targets: 2 }, // 2-Ativo
                    { bSortable: true,  sWidth: "30px",  targets: 3, render: function ( data, type, row ) { if ( type == "display") return 'R$ ' + fMascaraValor(row[3]); return data; } }, // 3-Cotação
                    { bSortable: true,  sWidth: "30px",  targets: 4, render: function ( data, type, row ) { if ( type == "display") return 'R$ ' + fMascaraValor(row[4]); return data; } }, // 4-Máxima
                    { bSortable: true,  sWidth: "30px",  targets: 5, render: function ( data, type, row ) { if ( type == "display") return 'R$ ' + fMascaraValor(row[5]); return data; } }, // 5-Drawdown
                    { bSortable: true,  sWidth: "30px",  targets: 6, render: function ( data, type, row ) { if ( type == "display") return fMascaraValor(row[6]) + '%';   return data; } }, // 6-Margem
                    { bSortable: true,  sWidth: "100px", targets: 7, // 7-Situacao
                        render: function ( data, type, row ) {
                            var situacao = ""
                            if ( type == "display") {
                                var atvVlrMargem  = parseFloat(row[6]); // 6-Margem
                                if ( atvVlrMargem <  margemMetadeAbaxo                                     ) situacao = 'Entre 0% e '+fMascaraValor(margemMetadeAbaxo)+'%: MANTER ou VENDER'; // VERMELHO
                                if ( atvVlrMargem >= margemMetadeAbaxo && atvVlrMargem < margemMetadeAcima ) situacao = 'Entre '+fMascaraValor(margemMetadeAbaxo)+'% e '+fMascaraValor(margemMetadeAcima)+'%: MANTER'; // LARANJA
                                if ( atvVlrMargem >= margemMetadeAcima && atvVlrMargem < margemDigitada    ) situacao = 'Entre '+fMascaraValor(margemMetadeAcima)+'% e '+fMascaraValor(margemDigitada)+'%: ACOMPANHAR'; // VERDE CLARO
                                if ( atvVlrMargem >= margemDigitada                                        ) situacao = 'Maior que '+fMascaraValor(margemDigitada)+'%: COMPRAR'; // VERDE ESCURO
                            }
                            return situacao;
                        }
                    }, // 7-Situacao
                    { bSortable: false, sWidth: "30px", targets: 8, // 8-Acao
                        render: function ( data, type, row ) {
                            var btnVis = "";
                            var btnDis = '';
							var btnCor = 'primary';
                            if ( type == "display") {
								CodAtivo  = row[2]; //  2-Ativo
								//btnDis = ' disabled';
								//btnCor = 'secondary';
								btnVis += '<a class="btn btn-sm btn-icon btn-icon-mini btn-round btn-simple btn-'+btnCor+btnDis+'"'+btnDis+' style="font-size:9px;" title="Visualizar Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseOperDrawdown( \''+urlPadrao+'\', \''+CodAtivo+'\' );">';
								btnVis += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
								btnVis += '</a>';
                            }
                            return btnVis;
                        }
                    } // 8-Acao
				],
				createdRow : function(row,data,dataIndex) {

                    $('td', row).addClass('text-center');
                    $('td', row).eq(2).addClass('font-weight-bold'); // 2-Ativo
                    $('td', row).eq(7).addClass('font-weight-bold'); // 7-Situacao

                    var atvOrigem = data[0]; // 0-Origem
                    if ( atvOrigem == 'PORTFÓLIO' ) $('td', row).eq(0).addClass('font-weight-bold text-primary'); // 0-Origem
                    if ( atvOrigem == 'RADAR'     ) $('td', row).eq(0).addClass('text-muted'); // 0-Origem

                    var atvVlrMargem  = parseFloat( data[6] ); // 6-Margem
                    if ( atvVlrMargem < margemMetadeAbaxo ) {
                        $('td', row).eq(2).css({"background-color": "#ffbcb2"}); // 2-Ativo
                        $('td', row).eq(7).css({"background-color": "#ffbcb2"}); // 7-Situacao
                    } else if ( atvVlrMargem >= margemMetadeAbaxo && atvVlrMargem < margemMetadeAcima ){
                        $('td', row).eq(2).css({"background-color": "#ffd191"}); // 2-Ativo # laranja mais forte ffc26c
                        $('td', row).eq(7).css({"background-color": "#ffd191"}); // 7-Situacao
                    } else if ( atvVlrMargem >= margemMetadeAcima && atvVlrMargem < margemDigitada ){
                        $('td', row).eq(2).css({"background-color": "#aae89c"}); // 2-Ativo
                        $('td', row).eq(7).css({"background-color": "#aae89c"}); // 7-Situacao
                    } else if ( atvVlrMargem >= margemDigitada ){
                        $('td', row).eq(2).css({"background-color": "#6bbd5b"}); // 2-Ativo
                        $('td', row).eq(7).css({"background-color": "#6bbd5b"}); // 7-Situacao
                    }

				}, // createdRow
				initComplete: function( settings, json ) {
					finalizarAnimacaoPesquisarAnaliseOperDrawdown();
				}, // initComplete
			    order: [[ 6, "desc" ]], // 6-Margem
                dom: 'frtBpi',
                buttons: [
                    {
                       extend:    'excelHtml5',
                       text:      '<i class="fa fa-file-excel-o"></i> Excel',
                       className: 'btn btn-outline-default btn-sm',
                       title: NOME_PROJETO + ' - Análise de Drawdown',
                       titleAttr: 'Excel',
                       exportOptions: { columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] },
                    },
                    {
                      extend: 'csvHtml5',
                      charset: 'UTF-8',
                      fieldSeparator: ';',
                      titleAttr: 'CSV',
                      text:      '<i class="fa fa-file-o"></i> CSV',
                      className: 'btn btn-outline-default btn-sm',
                      title: NOME_PROJETO + ' - Análise de Drawdown',
                      bom: true,
                      exportOptions: { columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] },
                    },
                    {
                      extend: 'pdfHtml5',
                      text:      '<i class="fa fa-file-pdf-o"></i> PDF',
                      className: 'btn btn-default btn-sm',
                      titleAttr: 'PDF',
                      title: NOME_PROJETO + ' - Análise de Drawdown',
                      pageSize: 'A3',
                      alignment: 'center',
                      exportOptions: { columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] },
                      footer: true,
                      customize: function (doc) {
                          doc.defaultStyle.fontSize = 12;
                          doc.styles.tableHeader.fontSize = 14;
                      }
                    },
                    {
                      extend: 'print',
                      text:      '<i class="fa fa-print"></i> Imprimir',
                      title: NOME_PROJETO + ' - Análise de Drawdown',
                      titleAttr: 'Imprimir',
                      className: 'btn btn-default btn-sm',
                      exportOptions: { columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] },
                    }
                ],
                bFilter: false,
                bInfo: false,
                bLengthChange: false,
                searchable: false,
                orderable: true,
                bAutoWidth: false,
                bPaginate: false,
                ordering: true
            });

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch (e) {
		fLimparSomenteGridAnaliseOperDrawdown( urlPadrao );
		finalizarAnimacaoPesquisarAnaliseOperDrawdown();
		if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarregarGridAnaliseOperDrawdown( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			fLimparAreaAlerta("AreaAlertaPrincAnaliseOperDrawdown");
			finalizarAnimacaoPesquisarAnaliseOperDrawdown();
			iniciarAnimacaoPesquisarAnaliseOperDrawdown();

			$('#GridAnaliseOperDrawdown').dataTable().fnClearTable();
			$("#GridAnaliseOperDrawdown").dataTable({ bDestroy: true }).fnDestroy();

			var QtdDias = $("#txtFiltroAnaliseOperDrawdownDias").val();
			var Margem = $("#txtFiltroAnaliseOperDrawdownMargem").val();

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url: urlPadrao + "Analise/drawdown",
				data: { QtdDias: QtdDias, Margem: Margem },
				success: function(result) {

					var resultado = result.data.Resultado;
					var mensagem  = result.data.Mensagem;
					var lista     = result.data.Lista;

					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fLimparSomenteGridAnaliseOperDrawdown();
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
						return;
					} else if (resultado == "FALHA") {
						fLimparSomenteGridAnaliseOperDrawdown();
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return;
					}else if (resultado == "OK") {
						fMontarGridAnaliseOperDrawdown( urlPadrao, lista );
					} else{
						fLimparSomenteGridAnaliseOperDrawdown();
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return;
					}

				},
				error: function(data) {
				    fLimparSomenteGridAnaliseOperDrawdown();
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
					return false;
				}
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch (e) {
	    fLimparSomenteGridAnaliseOperDrawdown();
		if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fAbrirModalDetalheAnaliseOperDrawdown( urlPadrao, CodAtivo ){
	try {

		 promise = new Promise( (resolve, reject) => {

            var margemDigitada = $("#txtFiltroAnaliseOperDrawdownMargem").val();
            margemDigitada = parseFloat(GetValorDecimal( margemDigitada.toString().replace('.', ',') ));

			$("#PopModalDetalheAnaliseOperDrawdownTit").html(CodAtivo + ' - Margem ' + fMascaraValor(margemDigitada) + '%');
			$('.nav-tabs a[href="#AbaDetalheOperDrawdownGrafico"]').tab('show');

			var DivGrafico = $("#DivGridModalDetalheAnaliseOperDrawdownGrafico");
			DivGrafico.html("");

			var DivDados = $("#DivGridModalDetalheAnaliseOperDrawdownDados");
			DivDados.html("");

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "Analise/griddrawdown",
				data: { CodAtivo: CodAtivo },
				success: function(result) {

					var resultado = result.data.Resultado;
					var mensagem  = result.data.Mensagem;
					var lista     = result.data.Lista;

					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						$("#PopModalDetalheAnaliseOperDrawdown").modal("hide");
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
						return;
					} else if (resultado == "FALHA") {
						$("#PopModalDetalheAnaliseOperDrawdown").modal("hide");
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return;
					} else if (resultado == "OK") {

						var content = '';

                        var iLen = lista.length;
						if ( iLen > 0 ){

						    var DataSetCotacao = [];
						    var DataSetMaxima  = [];
						    var DataSetCompra  = [];

							$.each(lista, function (index, value) {
								var valueData    = value[0]; // 0-Data
								var valueCotacao = parseFloat(value[1]); //  1-Cotacao
								var valueMaxima  = parseFloat(value[2]);  // 2-Maxima
								var valueMargem = parseFloat(value[3]);  // 3-Margem
								valueData = colcarFormacataoDataXML(valueData)
								valueData = moment(valueData).valueOf()
                                DataSetCotacao.push([valueData, valueCotacao]);
                                DataSetMaxima.push([valueData, valueMaxima]);
                                if ( valueMargem >= margemDigitada ) DataSetCompra.push([valueData, valueCotacao]);
							}); //$.each(lista, function (index, value) {

                            Highcharts.setOptions({ global: { useUTC: false }, lang: { decimalPoint: ',', thousandsSep: '.' } });
                            // Highcharts.setOptions({ global: { useUTC: false } });

                            Highcharts.setOptions({
                                lang: {
                                months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
                                shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                                weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                                loading: ['Atualizando o gráfico...aguarde'],
                                contextButtonTitle: 'Exportar gráfico',
                                decimalPoint: ',',
                                thousandsSep: '.',
                                downloadJPEG: 'Baixar imagem JPEG',
                                downloadPDF: 'Baixar arquivo PDF',
                                downloadPNG: 'Baixar imagem PNG',
                                downloadSVG: 'Baixar vetor SVG',
                                printChart: 'Imprimir gráfico',
                                rangeSelectorFrom: 'De',
                                rangeSelectorTo: 'Para',
                                rangeSelectorZoom: 'Zoom',
                                resetZoom: 'Limpar Zoom',
                                resetZoomTitle: 'Voltar Zoom para nível 1:1',
                                }
                            });

                            Highcharts.stockChart('DivGridModalDetalheAnaliseOperDrawdownGrafico', {
				                title: { text: null },
				                chart: { zoomType: null },
                                global: { useUTC: false },
                                colors: ['#7798BF', '#55BF3B', '#ff490b' ],
                                lang: {
                                    months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
                                    shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                                    weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                                    loading: ['Atualizando o gráfico...aguarde'],
                                    contextButtonTitle: 'Exportar gráfico',
                                    decimalPoint: ',',
                                    thousandsSep: '.',
                                    downloadJPEG: 'Baixar imagem JPEG',
                                    downloadPDF: 'Baixar arquivo PDF',
                                    downloadPNG: 'Baixar imagem PNG',
                                    downloadSVG: 'Baixar vetor SVG',
                                    printChart: 'Imprimir gráfico',
                                    rangeSelectorFrom: 'De',
                                    rangeSelectorTo: 'Para',
                                    rangeSelectorZoom: 'Zoom',
                                    resetZoom: 'Limpar Zoom',
                                    resetZoomTitle: 'Voltar Zoom para nível 1:1',
                                },
                                rangeSelector: { enabled: false, },
                                plotOptions: { series: { showInNavigator: false, }, },
                                navigator: { enabled: false, },
                                srcollbar: { enabled: false, },
                                tooltip: { valueDecimals: 2 },
                                xAxis: {
                                    type: 'datetime',
                                    dateTimeLabelFormats: { day: "%e. %b", month: "%b '%y", year: "%Y" },
                                    labels: { rotation: 45, formatter: function() { return moment(this.value).format("DD/MM/YYYY"); }, }
                                },
                                yAxis: {
					                labels: { formatter: function () { return 'R$ '+fMascaraValor(this.value); } },
                                    plotLines: [{value: 0,width: 2,color: 'silver'}]
                                },
                                tooltip: {
                                    split: true,
                                    valueDecimals: 2,
                                    pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>R$ {point.y}</b><br/>',
                                },
                                series: [
                                    {name: 'Cotação Atual', data: DataSetCotacao, id: 'dataseries' },
                                    {name: 'Cotação Máxima',  data: DataSetMaxima, dashStyle: 'shortdash', lineWidth: 3, step: true },
                                    {name: 'Ponto de Compra',  data: DataSetCompra, dashStyle: 'dot', lineWidth: 8, onSeries: 'dataseries', },
                                ]
                            });

                           lista.sort(function(a, b){
                             var DataA  = a[0]; // 0-Data
                             var DataB  = b[0]; // 0-Data
                             if (DataA == DataB) return 0;
                             return DataA > DataB? 1: -1;
                           });

                           lista.reverse();

							content += '<table class="table table-sm table-hover table-condensed nowrap" style="font-size: 12px;" border="0" cellspacing="0" width="100%" style="margin: 0px;">';
							content += '  <thead>';
							content += '    <tr style="font-size: 12px;" class="thead-dark font-weight-bold"> ';
							content += '      <th>Data</th>';
							content += '      <th>Cotação</th>';
							content += '      <th>Máxima</th>';
							content += '      <th>Margem</th>';
							content += '    </tr>';
							content += '  </thead>';
							content += '  <tbody>';

							$.each(lista, function (index, value) {
								var valueData    = value[0];             // 0-Data
								var valueCotacao = parseFloat(value[1]); // 1-Cotacao
								var valueMaxima = parseFloat(value[2]);  // 2-Maxima
								var valueMargem = parseFloat(value[3]);  // 3-Margem
								var textCor = "text-dark";
								if ( valueMargem >= margemDigitada ) textCor = "col-teal";
								// if ( valueCotacao > 0 ) textCor = "col-red";
								content += '    <tr class="text-center text-dark font-weight-bold" > ';
								content += '      <td style="width:auto;">'+colcarFormacataoData(valueData)+'</td>';
								content += '      <td style="width:auto;">R$ '+fMascaraValor(valueCotacao)+'</td>';
								content += '      <td style="width:auto;">R$ '+fMascaraValor(valueMaxima)+'</td>';
								content += '      <td class="'+textCor+'"  style="width:auto;">'+fMascaraValor(valueMargem)+'%</td>';
								content += '    </tr>';
							}); //$.each(lista, function (index, value) {

							content += '  </tbody>';
							content += '</table>';

						} // if ( lista.length > 0 ){
						else{
							content = 'Nenhuma informação encontrada para o Ativo...';
						}

						DivDados.html("");
						DivDados.append( content );

						$("#PopModalDetalheAnaliseOperDrawdown").modal({backdrop: "static"});
						return true;

					} else {
						$("#PopModalDetalheAnaliseOperDrawdown").modal("hide");
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return;
					}

				},
				error: function(data) {
					$("#PopModalDetalheAnaliseOperDrawdown").modal("hide");
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
					return;
				}
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch (e) {
		$("#PopModalDetalheAnaliseOperDrawdown").modal("hide");
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		return;
	}
}