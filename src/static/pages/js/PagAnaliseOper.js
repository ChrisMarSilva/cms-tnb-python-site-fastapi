
function iniciarAnimacaoPesquisarAnaliseOper() {
	$("#iRefreshOper").addClass("fa-spin");
	$("#btnAnaliseOperPesquisar").addClass("disabled");
    $("#txtFiltroAnaliseOperAtivo").attr("disabled","disabled");
    fDefinirPadraoSelect('txtFiltroAnaliseOperAtivo');
}

function finalizarAnimacaoPesquisaAnaliseOper() {
	$("#iRefreshOper").removeClass("fa-spin");
	$("#btnAnaliseOperPesquisar").removeClass("disabled");
    $("#txtFiltroAnaliseOperAtivo").removeAttr("disabled");
    fDefinirPadraoSelect('txtFiltroAnaliseOperAtivo');
}

function fLimparGridAnaliseOper( urlPadrao ){	

	fLimparAreaAlerta("AreaAlertaPrincAnaliseOper");
	
	$("#txtFiltroAnaliseOperAtivo").val("");	

	$("#DivAnaliseOperAtivo").text(       "..."     );
	$("#DivAnaliseOperTotInvest").text(   "R$ 0,00" );
	$("#DivAnaliseOperTotAtual").text(    "R$ 0,00" );
	$("#DivAnaliseOperValorizacao").text( "R$ 0,00 (0.00%)" );
	
	$("#DivAnaliseOperValorizacao").removeClass("text-success");
	$("#DivAnaliseOperValorizacao").removeClass("text-danger");

	fLimparSomenteGridAnaliseOper( urlPadrao );	
	
}

async function fLimparSomenteGridAnaliseOper( urlPadrao ){
	try {	

		 promise = new Promise( (resolve, reject) => {
	
			finalizarAnimacaoPesquisaAnaliseOper();
		
			$("th").addClass('text-center');
			
			$('#GridAnaliseOper').dataTable().fnClearTable();
			$("#GridAnaliseOper").dataTable({ bDestroy: true }).fnDestroy();

			$('#GridAnaliseOper').DataTable( {
				oLanguage: fTraduzirGrid(), 
				aoColumns: [
					{ bSortable: true, sWidth: "50px", targets:  0 }, //  0-Tipo
					{ bSortable: true, sWidth: "50px", targets:  1 }, //  1-Categoria
					{ bSortable: true, sWidth: "50px", targets:  2 }, //  2-Data
					{ bSortable: true, sWidth: "50px", targets:  3 }, //  3-Data
					{ bSortable: true, sWidth: "50px", targets:  4 }, //  4-Quant
					{ bSortable: true, sWidth: "50px", targets:  5 }, //  5-Preco Custo
					{ bSortable: true, sWidth: "50px", targets:  6 }, //  6-Preco Medio
					{ bSortable: true, sWidth: "50px", targets:  7 }, //  7-Total
					{ bSortable: true, sWidth: "50px", targets:  8 }  //  8-Valorizacao
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				searchable: false,
				orderable: false,
				bAutoWidth: false,
				bPaginate: false,
				ordering: false
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
		fCriarAlerta("AreaAlertaPrincAnaliseOper", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

async function fMontarGridAnaliseOper( urlPadrao, dataSet ){
	try { 

		 promise = new Promise( (resolve, reject) => {
	
			var TotInvest       = parseFloat(0);
			var TotAtual        = parseFloat(0);
			var TotValorizacao  = parseFloat(0);
			var PercValorizacao = parseFloat(0);
	
			var arTipo       = [];
			var arDatas      = [];
			var arPrecoCusto = [];
			var arPrecoMedio = [];
	  
			  $('#GridAnaliseOper').DataTable( {
				processing: true,
				serverSide: false,
				iDisplayLength: 10,
				oLanguage: fTraduzirGrid(), 
				data: dataSet,
				aoColumns: [
					  { bSortable: true, sWidth: "50px", targets:  0 }, //  0-Tipo
					  { bSortable: true, sWidth: "50px", targets:  1 }, //  1-Categoria
					  { bSortable: true, sWidth: "50px", targets:  2 }, //  2-Corretora
					  { bSortable: true, sWidth: "50px", targets:  3 }, //  3-Data
					  { bSortable: true, sWidth: "50px", targets:  4 }, //  4-Quant
					  { bSortable: true, sWidth: "50px", targets:  5,   //  5-Preco Custo
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[5]; //  5-Preco Custo
							  return data;
						  } 				
					  }, //  5-Preco Custo
					  { bSortable: true, sWidth: "50px", targets:  6, //  6-Preco Medio
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[6];//  6-Preco Medio 
							  return data;
						  } 				
					  }, //  6-Preco Medio
					  { bSortable: true, sWidth: "50px", targets:  7 ,//  7-Total
						  render: function ( data, type, row ) {
							  if ( type == "display")  return "R$ " + row[7];//  7-Total
							  return data;
						  } 				
					  }, //  7-Total
					  { bSortable: true, sWidth: "50px", targets:  8 ,//  8-Valorizacao
						  render: function ( data, type, row ) {
							  if ( type == "display")  if ( row[8] != "") return "R$ " + row[8];//  8-Valorizacao
							  return data;
						  } 				
					  }  //  8-Valorizacao
				],
				createdRow : function(row,data,dataIndex) {	
	  
				  $('td', row).addClass('text-center');	
				  
				  var Tipo       = data[0]; //  0-Tipo
				  var Data       = data[3];  //  3-Data
				  var PrecoCusto = parseFloat(GetValorDecimal(data[5]));   //  5-Preco Custo
				  var PrecoMedio = parseFloat(GetValorDecimal(data[6]));   //  6-Preco Medio
				  var Total      = parseFloat(GetValorDecimal(data[7]));    //  7-Total
				  var Valorizacao = 0;
	
				  arTipo[dataIndex]       = Tipo;
				  arDatas[dataIndex]      = Data;
				  arPrecoCusto[dataIndex] = PrecoCusto; 	
				  arPrecoMedio[dataIndex] = PrecoMedio;
	  
				  if ( Tipo == "Compra" || Tipo == "Compra/Troca" || Tipo == "Bonificação" ) TotInvest += Total;
				  if ( Tipo == "Venda"  || Tipo == "Venda/Troca"  || Tipo == "Projetado"   ) TotAtual  += Total;
					  
				  if ( Tipo == "Venda" || Tipo == "Venda/Troca" || Tipo == "Projetado" ){ //  0-Tipo
					  if ( data[8] != ""   ) Valorizacao = parseFloat(GetValorDecimal(data[8])); //  8-Valorizacao
					  if ( Valorizacao > 0 ) $('td', row).addClass('text-success');
					  if ( Valorizacao < 0 ) $('td', row).addClass('text-danger');
				  }
				  
				}, //createdRow
				initComplete: function( settings, json ) {
					
					finalizarAnimacaoPesquisaAnaliseOper();
					
					if ( TotInvest != 0 && TotAtual != 0 ){
					  TotValorizacao = parseFloat(TotAtual) - parseFloat(TotInvest);
					  PercValorizacao = ( TotValorizacao / TotInvest ) * 100;
					}
				
					$("#DivAnaliseOperTotInvest").text("R$ " + fMascaraValor(TotInvest) );
					$("#DivAnaliseOperTotAtual").text("R$ " + fMascaraValor(TotAtual) );
					$("#DivAnaliseOperValorizacao").text("R$ " + fMascaraValor(TotValorizacao) + " ("+ fMascaraValor(PercValorizacao) +"%)");
					
					if ( parseFloat(TotValorizacao) > 0 ) $("#DivAnaliseOperValorizacao").addClass("text-success");
					if ( parseFloat(TotValorizacao) < 0 ) $("#DivAnaliseOperValorizacao").addClass("text-danger");
	
					if ( arTipo.length > 2 ){
						fMontarGraficoAnaliseOper( urlPadrao, arTipo, arDatas, arPrecoCusto, arPrecoMedio );
					}
	
				}, //initComplete
				  order: [],			
				  dom: 'frtBpi',
				  buttons: [  
						{
						   extend:    'excelHtml5',
						   text:      '<i class="fa fa-file-excel-o"></i> Excel',
						   className: 'btn btn-outline-default btn-sm',
						   title: NOME_PROJETO + ' - Análise de Operações',
						   titleAttr: 'Excel',
						   exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ] },
						   customizeData: function (data) {
							  for (var i = 0; i < data.body.length; i++) {
								  for (var j = 0; j < data.body[i].length; j++) {
									  if (j == 4) data.body[i][j] = '\u200C' + data.body[i][j]; // Formatando a Coluna = 4-Quant
								  }
							  }
						  } 
						}, 
						{
						  extend: 'csvHtml5',
						  charset: 'UTF-8',
						  fieldSeparator: ';',
						  titleAttr: 'CSV',
						  text:      '<i class="fa fa-file-o"></i> CSV',
						  className: 'btn btn-outline-default btn-sm',
						  title: NOME_PROJETO + ' - Análise de Operações',
						  bom: true,
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ] } 
						},
						{
						  extend: 'pdfHtml5',
						  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						  className: 'btn btn-default btn-sm',
						  titleAttr: 'PDF',
						  title: NOME_PROJETO + ' - Análise de Operações', 
						  pageSize: 'A3',
						  alignment: 'center',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ] },
						  footer: true,
						  customize: function (doc) { 
							  doc.defaultStyle.fontSize = 12; 
							  doc.styles.tableHeader.fontSize = 14; 
						  }
						},
						{
						  extend: 'print',
						  text:      '<i class="fa fa-print"></i> Imprimir',
						  title: NOME_PROJETO + ' - Análise de Operações',
						  titleAttr: 'Imprimir',
						  className: 'btn btn-default btn-sm',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ] }
						}
				  ],
				  bFilter: false,
				  bInfo: false,
				  bLengthChange: false,
				  searchable: false,
				  orderable: false,
				  bAutoWidth: false,
				  bPaginate: false,
				  ordering: false
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
		  fLimparSomenteGridAnaliseOper( urlPadrao );
		if ( e.description != undefined ){
		  fCriarAlerta("AreaAlertaPrincAnaliseOper", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		}
	  }
}  

async function fCarregarGridAnaliseOper( urlPadrao ){
	try {   

		 promise = new Promise( (resolve, reject) => {
	
			finalizarAnimacaoPesquisaAnaliseOper();
			fLimparAreaAlerta("AreaAlertaPrincAnaliseOper");
			
			$('#DivGraficoOper').html('');
			$('#GridAnaliseOper').dataTable().fnClearTable();
			$("#GridAnaliseOper").dataTable({ bDestroy: true }).fnDestroy();	
			
			$("#DivAnaliseOperTotInvest").text("R$ 0,00");
			$("#DivAnaliseOperTotAtual").text("R$ 0,00");
			$("#DivAnaliseOperValorizacao").text("R$ 0,00 (0.00%)");
			$("#DivAnaliseOperValorizacao").removeClass("text-success");
			$("#DivAnaliseOperValorizacao").removeClass("text-danger");
			$("#DivAnaliseOperAtivo").text( "..." );
			
			var CodAtivo = $("#txtFiltroAnaliseOperAtivo").val().trim();	
			if( CodAtivo == ""  ){
			  fLimparGridAnaliseOper( urlPadrao );
			  fCriarAlerta("AreaAlertaPrincAnaliseOper", TP_ALERTA_AVISO, 'Selecione um Ativo!');
			  return false;
			}
  
			iniciarAnimacaoPesquisarAnaliseOper();
			
			$("#DivAnaliseOperAtivo").text( CodAtivo );
  
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url: urlPadrao + "Analise/gridOper",
				data: { CodAtivo : CodAtivo },
				success: function(result) {
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
	
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fLimparSomenteGridAnaliseOper( urlPadrao );
						fCriarAlerta("AreaAlertaPrincAnaliseOper", TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						fLimparSomenteGridAnaliseOper( urlPadrao );( urlPadrao );
						fCriarAlerta("AreaAlertaPrincAnaliseOper", TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridAnaliseOper( urlPadrao, lista );
					} else{
						fLimparSomenteGridAnaliseOper( urlPadrao );( urlPadrao );
						fCriarAlerta("AreaAlertaPrincAnaliseOper", TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					fLimparSomenteGridAnaliseOper( urlPadrao );( urlPadrao );
					fCriarAlerta("AreaAlertaPrincAnaliseOper", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
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
		  fLimparSomenteGridAnaliseOper( urlPadrao );( urlPadrao );
		if ( e.description != undefined ){
		  fCriarAlerta("AreaAlertaPrincAnaliseOper", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);   
		}
	  }
}
  
async function fMontarGraficoAnaliseOper( urlPadrao, arTipo, arDatas, arPrecoCusto, arPrecoMedio ){
	try {   

		 promise = new Promise( (resolve, reject) => {

			var DataSetPrecoCompra = []; 
			var DataSetPrecoMedio  = [];
			
			var iLen = arDatas.length;
			iIndex = -1;
			for (i = 0; i < iLen; i++) {
				if ( arTipo[i] == 'Compra' || arTipo[i] == 'Compra/Troca' || arTipo[i] == 'Projetado' ){
					iIndex += 1;
					DataSetPrecoCompra[iIndex] = [moment(colcarFormacataoDataXMLPadrao(arDatas[i])).valueOf(), arPrecoCusto[i] ];
					DataSetPrecoMedio[iIndex]  = [moment(colcarFormacataoDataXMLPadrao(arDatas[i])).valueOf(), arPrecoMedio[i] ];
				}
			}

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

			Highcharts.stockChart('DivGraficoOper', {
	
				title: {
					align: 'center',
					useHTML: true,
					text: '<h6 class="font-weight-bold text-muted">Custo/Ação x Preço Médio</h6>',
				},
	
				global: {
					useUTC: false
				},
	
				//colors: ['#2b908f', '#90ee7e', '#f45b5b', '#7798BF', '#aaeeee', '#ff0066', '#eeaaee', '#55BF3B', '#DF5353', '#7798BF', '#aaeeee'],
				colors: ['#7798BF', '#55BF3B' ],
	
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
	
				rangeSelector: {
					selected: 5,
					inputEnabled: false,
				},
	
				plotOptions: {
					series: {
						//marker: {enabled: true },
						//compare: 'percent',
						showInNavigator: true,
					}
				},
	
				tooltip: {
					valueDecimals: 2
				},
	
				xAxis: {
					type: 'datetime',
					dateTimeLabelFormats: { day: "%e. %b", month: "%b '%y", year: "%Y" },
					labels: { formatter: function() { return moment(this.value).format("DD/MM/YYYY"); }, }
				},
	
				yAxis: {
					labels: {
						//formatter: function () { return (this.value > 0 ? ' + ' : '') + this.value + '%'; }
						formatter: function () { return 'R$ ' + this.value; }
					},
					plotLines: [{value: 0,width: 2,color: 'silver'}]
				},
	
				tooltip: {
					split: true, valueDecimals: 2, 
					//pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
					pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>',
				},
	
				series: [
					{
						name: 'Custo/Ação',
						data: DataSetPrecoCompra,
						dataGrouping: { groupPixelWidth: 10 }
					}, 
					{
						name: 'Preço Médio',
						data: DataSetPrecoMedio,
						dataGrouping: {groupPixelWidth: 50, }
					}
				]
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
		if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrincAnaliseOper", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);   
	}
}
