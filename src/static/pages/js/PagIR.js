

$(document).ready(function() {
	
	//$(this).attr("title", ":: TnB - IRPF ::");
	$("#MnPrincIR").addClass("active open");
	
	fLimparAreaAlertaPrinc();
	
});

async function fAbrirModalGerarPortfolio( urlPadrao ) {
    try {

        $("#PopModalGerarPortfolio").modal({backdrop: "static", keyboard: false});
        $("#iRefreshGerarPortfolio").addClass("fa-spin");

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "principal/gerarportifolio",
			success: function(result) {

				setTimeout(function(){
				    $("#iRefreshGerarPortfolio").removeClass("fa-spin");
				    $('#PopModalGerarPortfolio').modal('hide');
				}, 500);

                fCarregarAnoDecalracao( urlPadrao );

			},
			error: function(data) {
				$("#iRefreshGerarPortfolio").removeClass("fa-spin");
				$('#PopModalGerarPortfolio').modal('hide');
				fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
				return;
			}
		});

    } catch (e) {
        $("#iRefreshGerarPortfolio").removeClass("fa-spin");
        $('#PopModalGerarPortfolio').modal('hide');
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fCarregarAnoDecalracao( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {
		
			$('#selIRPFAno').empty();
			//$('#selIRPFAno').append('<option value="" selected>Selecione...</option>');
			
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "IRPF/listaAno",
				success: function(result) {  
				
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista; 
	
					if (resultado == "NOK") {
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return false;
					} else if (resultado == "OK") {	
						 //if ( lista.length > 0 )
						$.each(lista, function (index, value) {
							$('#selIRPFAno').append('<option value="'+ value +'" selected>'+value+'</option>');
						});  
						fDefinirPadraoSelect('selIRPFAno');
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

async function fCarregarConfigApuracao( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : false,
				type    : "POST",
	            url     : urlPadrao + "apuracao/config",
				success: function(result) {  
				
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var Config    = result.data.Dados;

					if (resultado == "NOK") {
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return false;
					} else if (resultado == "OK") {	
						if ( Config.Valor == "S" ) $("#chkIRPFVlrSuperior20Mil").attr( "checked", true )
						else 					   $("#chkIRPFVlrSuperior20Mil").attr( "checked", false );
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
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
		
	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function iniciarAnimacaoPesquisar() {

	 promise = new Promise( (resolve, reject) => {

		$("#iRefresh").addClass("fa-spin");
		$("#btnIRPFPesquisar").addClass("disabled");
		$("#btnIRPFLimpar").addClass("disabled");

		resolve(true);
		// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
	})
	.then( txt => {
		//console.log('Sucesso: ' + txt);
	})
	.catch( txt => {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	});

}

async function finalizarAnimacaoPesquisa() {

	 promise = new Promise( (resolve, reject) => {

		$("#iRefresh").removeClass("fa-spin");
		$("#btnIRPFPesquisar").removeClass("disabled");
		$("#btnIRPFLimpar").removeClass("disabled");

		resolve(true);
		// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
	})
	.then( txt => {
		//console.log('Sucesso: ' + txt);
	})
	.catch( txt => {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	});
}

async function fLimparDeclaracao( urlPadrao ){

     promise = new Promise( (resolve, reject) => {

		fLimparAreaAlertaPrinc();
		finalizarAnimacaoPesquisa();
	
		$("th").addClass('text-center');
		$('#selApuracAno').val( "" );	
		$("#chkIRPFVlrSuperior20Mil").attr( "checked", false );
		
		fLimparGridRendIsentos(     urlPadrao );
		fLimparGridRendTributaveis( urlPadrao );
		fLimparGridBensEDireitos(   urlPadrao );
		fLimparGridMeses(           urlPadrao );
		fLimparGridMesesFII(        urlPadrao );

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
    })
    .then( txt => {
        //console.log('Sucesso: ' + txt);
    })
    .catch( txt => {
        //fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    });
	
}

async function fCarregarDeclaracao( urlPadrao ){

     promise = new Promise( (resolve, reject) => {

		var AnoDeclaracao = $("#selIRPFAno").val().trim();	
		var CalcVlrSuperior = "N";
		if ( $("#chkIRPFVlrSuperior20Mil").is(":checked") )
			CalcVlrSuperior = "S";
		
		fLimparAreaAlertaPrinc();
		finalizarAnimacaoPesquisa();
		
		fLimparGridRendIsentos(     urlPadrao );
		fLimparGridRendTributaveis( urlPadrao );
		fLimparGridBensEDireitos(   urlPadrao );
		fLimparGridMeses(           urlPadrao );
		fLimparGridMesesFII(        urlPadrao );
		
		if ( AnoDeclaracao != "" ){
			iniciarAnimacaoPesquisar();
			fCarregarGridRendIsentos(     urlPadrao, AnoDeclaracao                  );
			fCarregarGridRendTributaveis( urlPadrao, AnoDeclaracao                  );
			fCarregarGridBensEDireitos(   urlPadrao, AnoDeclaracao                  );
			fCarregarGridMeses(           urlPadrao, AnoDeclaracao, CalcVlrSuperior );
			fCarregarGridMesesFII(        urlPadrao, AnoDeclaracao                  );
		}	

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
    })
    .then( txt => {
        //console.log('Sucesso: ' + txt);
    })
    .catch( txt => {
        //fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    });
}

async function fLimparGridRendIsentos( urlPadrao ){
	try {	

		 promise = new Promise( (resolve, reject) => {
	
			$('#GridRendIsentos').dataTable().fnClearTable();
			$("#GridRendIsentos").dataTable({ bDestroy: true }).fnDestroy();
			
			$('#GridRendIsentos').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth: "200px", targets: 0 }, //  0-TipoRendimento
					{ bSortable: false, bOrderable: false, sWidth:  "50px", targets: 1 }, //  1-CNPJFontePagadora
					{ bSortable: false, bOrderable: false, sWidth: "200px", targets: 2 }, //  2-NomeFontePagadora
					{ bSortable: false, bOrderable: false, sWidth:  "50px", targets: 3 }, //  3-Valor
					{ visible  : false,                                     targets: 4 }, //  4-CodAtivo
					{ visible  : false,                                     targets: 5 }, //  5-TpRendIsento
					{ bSortable: false,                    sWidth: "30px",  targets: 6 }  //  6-Acao
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				bSearchable: false,
				bOrderable: false,
				bSortable: false,
				bAutoWidth: false,
				bPaginate: false,
				bOrdering: false
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

async function fMontarGridRendIsentos( urlPadrao, dataSet, AnoDeclaracao ){
  try {   
		
		 promise = new Promise( (resolve, reject) => {

			$('#GridRendIsentos').DataTable( {
				processing: true,
				serverSide: false,
					  oLanguage: fTraduzirGrid(), 
					  data: dataSet,
							  aoColumns: [
						  { bSortable: false, bOrderable: false, sWidth: "200px", targets: 0 }, //  0-TipoRendimento
						  { bSortable: false, bOrderable: false, sWidth:  "50px", targets: 1 }, //  1-CNPJFontePagadora
						  { bSortable: false, bOrderable: false, sWidth: "200px", targets: 2 }, //  2-NomeFontePagadora
						  { bSortable: false, bOrderable: false, sWidth:  "50px", targets: 3 ,  //  3-Valor
								  render: function ( data, type, row ) { 
									  if ( type == "display") return "R$ " + row[3];  //  3-Valor
									  return data;
								  } 				 
						  },  //  3-Valor	
						  { visible  : false,                                     targets: 4 }, // 4-CodAtivo
						  { visible  : false,                                     targets: 5 }, // 5-TpRendIsento
						  { bSortable: false,                    sWidth: "5px",   targets: 6,   // 6-Acao
							  render: function ( data, type, row ) {
								  var btnVis = "";
								  if ( type == "display") {
									  var CodAtivo     = row[4]; // 4-CodAtivo
									  var TpRendIsento = row[5]; // 5-TpRendIsento
									  if ( TpRendIsento != '' ){
										  btnVis += '<a class="btn btn-sm btn-primary btn-icon btn-icon-mini btn-round btn-simple" style="font-size:9px;" title="Visualizar Rendimentos Isentos e Não Tributáveis" href="javascript:void(0);" onclick="fAbrirModalDetalheRendIsentos( \''+urlPadrao+'\', \''+AnoDeclaracao+'\', \''+TpRendIsento+'\', \''+CodAtivo+'\' );">';
										  btnVis += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
										  btnVis += '</a>';
									  }
								  }
								  return btnVis;
							  } 
						  } //  6-Acao
					   ],
				createdRow : function(row,data,dataIndex) {			  
							  $('td', row).addClass('text-center'); 
				}, //createdRow
					initComplete: function( settings, json ) {
				}, //initComplete
						  dom: 'frtBpi', //Bfrtip //frtBip  //frtBpi
						  buttons: [  
								{
								   extend:    'excelHtml5',
								   text:      '<i class="fa fa-file-excel-o"></i> Excel',
								   className: 'btn btn-outline-default btn-sm',
								   title: NOME_PROJETO + ' - Rendimentos Isentos e Nao Tributaveis - ' + AnoDeclaracao,
								   titleAttr: 'Excel',
								   exportOptions: {  columns: [ 0, 1, 2, 3 ] }
								}, 
								{
								  extend: 'csvHtml5',
								  charset: 'UTF-8',
								  fieldSeparator: ';',
								  titleAttr: 'CSV',
								  text:      '<i class="fa fa-file-o"></i> CSV',
								  className: 'btn btn-outline-default btn-sm',
								  title: NOME_PROJETO + ' - Rendimentos Isentos e Nao Tributaveis - ' + AnoDeclaracao,
								  bom: true,
								  exportOptions: {  columns: [ 0, 1, 2, 3 ] } //orthogonal: 'export',
								},
								{
								  extend: 'pdfHtml5',
								  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
								  className: 'btn btn-default btn-sm',
								  titleAttr: 'PDF',
								  title: NOME_PROJETO + ' - Rendimentos Isentos e Nao Tributaveis - ' + AnoDeclaracao,
								  pageSize: 'A3',
								  alignment: 'center',
								  exportOptions: {  columns: [ 0, 1, 2, 3 ] }, //orthogonal: 'export',
								  footer: true,
								  customize: function (doc) { 
									  doc.defaultStyle.fontSize = 12; 
									  doc.styles.tableHeader.fontSize = 14; 
								  }
								},
								{
								  extend: 'print',
								  text:      '<i class="fa fa-print"></i> Imprimir',
								  title: NOME_PROJETO + ' - Rendimentos Isentos e Nao Tributaveis - ' + AnoDeclaracao,
								  titleAttr: 'Imprimir',
								  className: 'btn btn-default btn-sm',
								  exportOptions: {  columns: [ 0, 1, 2, 3 ] } //orthogonal: 'export',
								}
						  ],			
						  order: [],
						  bFilter: false,
						  bInfo: false,
						  bLengthChange: false,
						  bSearchable: false,
						  bOrderable: false,
						  bSortable: false,
						  bAutoWidth: false,
						  bPaginate: false,
						  bOrdering: false
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
        if ( e.description != undefined )
		  fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fCarregarGridRendIsentos( urlPadrao, AnoDeclaracao ){
  try {   
		
		 promise = new Promise( (resolve, reject) => {

			$('#GridRendIsentos').dataTable().fnClearTable();
			$("#GridRendIsentos").dataTable({ bDestroy: true }).fnDestroy();
	
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url : urlPadrao + "IRPF/gridIsentos",
				data: { AnoDeclaracao : AnoDeclaracao },
				success: function(result) {
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
	
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						// fLimparSomenteGrid(( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						// fLimparSomenteGrid(( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridRendIsentos( urlPadrao, lista, AnoDeclaracao );
					} else{
						// fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					// fLimparSomenteGrid(( urlPadrao );( urlPadrao );
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
      	if ( e.description != undefined )
			fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fAbrirModalDetalheRendIsentos( urlPadrao, AnoDeclaracao, TpRendIsento, CodAtivo ){
	try {  

		 promise = new Promise( (resolve, reject) => {
	
			fLimparAreaAlertaPrinc();
		
			var DivGridIRPFRendIsentos = $("#DivGridIRPFRendIsentos");
			DivGridIRPFRendIsentos.html("");
	
			if( (AnoDeclaracao=="") || (TpRendIsento=="") || (CodAtivo=="") ){
				fCriarAlertaPrinc(TP_ALERTA_AVISO, "Dados da pesquisa inválido!");
				return false;
			}	
			  
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "IRPF/gridIsentosDetalhe",
				data    : { AnoDeclaracao: AnoDeclaracao, TpRendIsento: TpRendIsento, CodAtivo: CodAtivo },
				success: function(result) {  
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
					
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						$("#PopModalDetalheIRPFRendIsentos").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						$("#PopModalDetalheIRPFRendIsentos").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					} else if (resultado == "OK") {
	
						if ( lista.length > 0 ){
							
								var ProvVlrPreco = 0.00;
								var ProvVlrTotal = 0.00;
								var content      = '';
	
								content += '<table class="table table-sm table-hover table-condensed nowrap" style="font-size: 12px;" border="0" cellspacing="0" width="100%" style="margin: 0px;">';
								content += '  <thead>';
								content += '    <tr style="font-size: 12px;" class="thead-dark font-weight-bold"> ';
								if ( TpRendIsento == 'D' || TpRendIsento == 'R' || TpRendIsento == 'F' ){
									content += '      <th>Data Ex.</th>';
									content += '      <th>Data Pagto</th>';
								}
								if ( TpRendIsento == 'B' ){
									content += '      <th>Data</th>';
								}
								content += '      <th>Código</th>';
								content += '      <th>Tipo</th>';
								content += '      <th>Quant.</th>';
								content += '      <th>Preço</th>';
								content += '      <th>Total</th>';
								content += '    </tr>';  
								content += '  </thead>';
								content += '  <tbody>';
								
								$.each(lista, function (index, value) {
	
									var ProvDataEx    = value[0]; // 0-DataEx
									var ProvDataPagto = value[1]; // 1-DataPagto
									var ProvCodAtivo  = value[2]; // 2-CodAtivo
									var ProvTipo      = value[3]; // 3-Tipo
									var ProvQuant     = value[4]; // 4-Quant
									var ProvPreco     = parseFloat( GetValorDecimal(value[5]) ); // 5-Preco
									var ProvTotal     = parseFloat( GetValorDecimal(value[6]) ); // 6-Total 
									ProvVlrPreco     += ProvPreco;
									ProvVlrTotal     += ProvTotal;
	
									content += '    <tr class="text-center text-dark" > ';
									content += '      <td style="width:auto;">'+colcarFormacataoData(ProvDataEx)+'</td>';
									if ( TpRendIsento == 'D' || TpRendIsento == 'R' || TpRendIsento == 'F' ) 
										content += '      <td style="width:auto;">'+colcarFormacataoData(ProvDataPagto)+'</td>';
									content += '      <td class="font-weight-bold" style="width:auto;">'+ProvCodAtivo+'</td>';
									content += '      <td style="width:auto;">'+ProvTipo+'</td>';
									content += '      <td style="width:auto;">'+colcarFormacataoInteiro(ProvQuant)+'</td>';
									content += '      <td style="width:auto;">R$ '+fMascaraValor(ProvPreco)+'</td>';
									content += '      <td class="font-weight-bold" style="width:auto;">R$ '+fMascaraValor(ProvTotal)+'</td>';
									content += '    </tr>'; 
	
							}); //$.each(lista, function (index, value) {
													
							content += '    <tr style="font-size: 12px;" class="text-center text-dark font-weight-bold" > ';
							content += '      <td> </td>';
							if ( TpRendIsento == 'D' || TpRendIsento == 'R' || TpRendIsento == 'F' ) 
								content += '      <td> </td>';
							content += '      <td>TOTAL</td>';
							content += '      <td> </td>';
							content += '      <td> </td>';
							content += '      <td>R$ '+fMascaraValor(ProvVlrPreco)+'</td>';
							content += '      <td>R$ '+fMascaraValor(ProvVlrTotal)+'</td>';
							content += '    </tr>'; 
													
							content += '  </tbody>';
							content += '</table>';
	
							DivGridIRPFRendIsentos.html("");
							DivGridIRPFRendIsentos.append( content );	
							
							$("#PopModalDetalheIRPFRendIsentos").modal({backdrop: "static"});
							return true;
						}// if ( lista.length > 0 ){
	
						fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Sem Dados para Exibir!'); 
						return true;
		   
					} else {
						$("#PopModalDetalheIRPFRendIsentos").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					$("#PopModalDetalheIRPFRendIsentos").modal("hide");	
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
		$("#PopModalDetalheIRPFRendIsentos").modal("hide");	
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	}  
}	

async function fLimparGridRendTributaveis( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {
	
			$('#GridRendTributavel').dataTable().fnClearTable();
			$("#GridRendTributavel").dataTable({ bDestroy: true }).fnDestroy();
			
			$('#GridRendTributavel').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth: "200px", targets: 0 }, //  0-TipoRendimento
					{ bSortable: false, bOrderable: false, sWidth:  "50px", targets: 1 }, //  1-CNPJFontePagadora
					{ bSortable: false, bOrderable: false, sWidth: "200px", targets: 2 }, //  2-NomeFontePagadora
					{ bSortable: false, bOrderable: false, sWidth:  "50px", targets: 3 }, //  3-Valor
					{ visible  : false,                                     targets: 4 }, //  4-CodAtivo
					{ visible  : false,                                     targets: 5 }, //  5-TpRendTributavel
					{ bSortable: false,                    sWidth: "30px",  targets: 6 }  //  6-Acao
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				bSearchable: false,
				bOrderable: false,
				bSortable: false,
				bAutoWidth: false,
				bPaginate: false,
				bOrdering: false
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

async function fMontarGridRendTributaveis( urlPadrao, dataSet, AnoDeclaracao ){
  try {   
		
		 promise = new Promise( (resolve, reject) => {

			$('#GridRendTributavel').DataTable( {
				processing: true,
				serverSide: false,
						  oLanguage: fTraduzirGrid(), 
						  data: dataSet,
								  aoColumns: [
									  { bSortable: false, bOrderable: false, sWidth: "200px", targets: 0 }, //  0-TipoRendimento
									  { bSortable: false, bOrderable: false, sWidth:  "50px", targets: 1 }, //  1-CNPJFontePagadora
									  { bSortable: false, bOrderable: false, sWidth: "200px", targets: 2 }, //  2-NomeFontePagadora
									  { bSortable: false, bOrderable: false, sWidth:  "50px", targets: 3 ,  //  3-Valor
										  render: function ( data, type, row ) { 
											  if ( type == "display") return "R$ " + row[3]; //  //  3-Valor
											  return data;
										  } 				 
									  },  //  3-Valor
									  { visible  : false,                                     targets: 4 }, // 4-CodAtivo
									  { visible  : false,                                     targets: 5 }, // 5-TpRendTributavel
									  { bSortable: false,                    sWidth: "5px",   targets: 6,   // 6-Acao
										  render: function ( data, type, row ) {
											  var btnVis = "";
											  if ( type == "display") {
												  var CodAtivo         = row[4]; // 4-CodAtivo
												  var TpRendTributavel = row[5]; // 5-TpRendTributavel
												  btnVis += '<a class="btn btn-sm btn-primary btn-icon btn-icon-mini btn-round btn-simple" style="font-size:9px;" title="Visualizar Rendimentos Sujeitos á Tributação Exclusiva/Definitiva" href="javascript:void(0);" onclick="fAbrirModalDetalheRendTributaveis( \''+urlPadrao+'\', \''+AnoDeclaracao+'\', \''+TpRendTributavel+'\', \''+CodAtivo+'\' );">';
												  btnVis += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
												  btnVis += '</a>';
											  }
											  return btnVis;
										  } 
									  } //  6-Acao
							  ],
								  createdRow : function(row,data,dataIndex) {			  
							  $('td', row).addClass('text-center'); 
								  }, //createdRow
								  initComplete: function( settings, json ) {
								  }, //initComplete
						  dom: 'frtBpi', //Bfrtip //frtBip  //frtBpi
						  buttons: [  
								{
								   extend:    'excelHtml5',
								   text:      '<i class="fa fa-file-excel-o"></i> Excel',
								   className: 'btn btn-outline-default btn-sm',
								   title: NOME_PROJETO + ' - Rendimentos Sujeitos a Tributacao Exclusiva ou Definitiva - ' + AnoDeclaracao,
								   titleAttr: 'Excel',
								   exportOptions: {  columns: [ 0, 1, 2, 3 ] }
								}, 
								{
								  extend: 'csvHtml5',
								  charset: 'UTF-8',
								  fieldSeparator: ';',
								  titleAttr: 'CSV',
								  text:      '<i class="fa fa-file-o"></i> CSV',
								  className: 'btn btn-outline-default btn-sm',
								   title: NOME_PROJETO + ' - Rendimentos Sujeitos a Tributacao Exclusiva ou Definitiva - ' + AnoDeclaracao,
								  bom: true,
								  exportOptions: {  columns: [ 0, 1, 2, 3 ] } //orthogonal: 'export',
								},
								{
								  extend: 'pdfHtml5',
								  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
								  className: 'btn btn-default btn-sm',
								  titleAttr: 'PDF',
								   title: NOME_PROJETO + ' - Rendimentos Sujeitos a Tributacao Exclusiva ou Definitiva - ' + AnoDeclaracao,
								  pageSize: 'A3',
								  alignment: 'center',
								  exportOptions: {  columns: [ 0, 1, 2, 3 ] }, //orthogonal: 'export',
								  footer: true,
								  customize: function (doc) { 
									  doc.defaultStyle.fontSize = 12; 
									  doc.styles.tableHeader.fontSize = 14; 
								  }
								},
								{
								  extend: 'print',
								  text:      '<i class="fa fa-print"></i> Imprimir',
								   title: NOME_PROJETO + ' - Rendimentos Sujeitos a Tributacao Exclusiva ou Definitiva - ' + AnoDeclaracao,
								  titleAttr: 'Imprimir',
								  className: 'btn btn-default btn-sm',
								  exportOptions: {  columns: [ 0, 1, 2, 3 ] } //orthogonal: 'export',
								}
						  ],		
						  order: [],
						  bFilter: false,
						  bInfo: false,
						  bLengthChange: false,
						  bSearchable: false,
						  bOrderable: false,
						  bSortable: false,
						  bAutoWidth: false,
						  bPaginate: false,
						  bOrdering: false
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
        if ( e.description != undefined )
		  fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fCarregarGridRendTributaveis( urlPadrao, AnoDeclaracao ){
  try {   

		 promise = new Promise( (resolve, reject) => {

			$('#GridRendTributavel').dataTable().fnClearTable();
			$("#GridRendTributavel").dataTable({ bDestroy: true }).fnDestroy();
	
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url : urlPadrao + "IRPF/gridTributaveis",
				data: { AnoDeclaracao : AnoDeclaracao },
				success: function(result) {
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
	
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						// fLimparSomenteGrid(( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						// fLimparSomenteGrid(( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridRendTributaveis( urlPadrao, lista, AnoDeclaracao );
					} else{
						// fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					// fLimparSomenteGrid(( urlPadrao );( urlPadrao );
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
      	if ( e.description != undefined )
			fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fAbrirModalDetalheRendTributaveis( urlPadrao, AnoDeclaracao, TpRendTributavel, CodAtivo ){
	try {  
		
		 promise = new Promise( (resolve, reject) => {

			fLimparAreaAlertaPrinc();
		
			var DivGridIRPFRendTributaveis = $("#DivGridIRPFRendTributaveis");
			DivGridIRPFRendTributaveis.html("");
	
			if( (AnoDeclaracao=="") || (TpRendTributavel=="") || (CodAtivo=="") ){
				fCriarAlertaPrinc(TP_ALERTA_AVISO, "Dados da pesquisa inválido!");
				return false;
			}	
			  
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "IRPF/gridTributaveisDetalhe",
				data    : { AnoDeclaracao: AnoDeclaracao, TpRendTributavel: TpRendTributavel, CodAtivo: CodAtivo },
				success: function(result) {  
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
					
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						$("#PopModalDetalheIRPFRendTributaveis").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						$("#PopModalDetalheIRPFRendTributaveis").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					} else if (resultado == "OK") {
	
						if ( lista.length > 0 ){
							
								var ProvVlrPreco = 0.00;
								var ProvVlrTotal = 0.00;
								var content      = '';
	
								content += '<table class="table table-sm table-hover table-condensed nowrap" style="font-size: 12px;" border="0" cellspacing="0" width="100%" style="margin: 0px;">';
								content += '  <thead>';
								content += '    <tr style="font-size: 12px;" class="thead-dark font-weight-bold"> ';
								if ( TpRendTributavel == 'J' ){
									content += '      <th>Data Ex.</th>';
									content += '      <th>Data Pagto</th>';
								}
								if ( TpRendTributavel == 'A' || TpRendTributavel == 'F' ){
									content += '      <th>Data</th>';
								}
								content += '      <th>Código</th>';
								content += '      <th>Tipo</th>';
								if ( TpRendTributavel == 'J' || TpRendTributavel == 'F' ) 
									content += '      <th>Quant.</th>';
								content += '      <th>Preço</th>';
								content += '      <th>Total</th>';
								content += '    </tr>';  
								content += '  </thead>';
								content += '  <tbody>';

								$.each(lista, function (index, value) {
	
									var ProvDataEx    = value[0]; // 0-DataEx
									var ProvDataPagto = value[1]; // 1-DataPagto
									var ProvCodAtivo  = value[2]; // 2-CodAtivo
									var ProvTipo      = value[3]; // 3-Tipo
									var ProvQuant     = value[4]; // 4-Quant
									var ProvPreco     = parseFloat( GetValorDecimal(value[5]) ); // 5-Preco
									var ProvTotal     = parseFloat( GetValorDecimal(value[6]) ); // 6-Total 
									ProvVlrPreco     += ProvPreco;
									ProvVlrTotal     += ProvTotal;
	
									content += '    <tr class="text-center text-dark" > ';
									content += '      <td style="width:auto;">'+colcarFormacataoData(ProvDataEx)+'</td>';
									if ( TpRendTributavel == 'J' ) 
										content += '      <td style="width:auto;">'+colcarFormacataoData(ProvDataPagto)+'</td>';
									content += '      <td class="font-weight-bold" style="width:auto;">'+ProvCodAtivo+'</td>';
									content += '      <td style="width:auto;">'+ProvTipo+'</td>';
									if ( TpRendTributavel == 'J' || TpRendTributavel == 'F' ) 
										content += '      <td style="width:auto;">'+colcarFormacataoInteiro(ProvQuant)+'</td>';
									content += '      <td style="width:auto;">R$ '+fMascaraValor(ProvPreco)+'</td>';
									content += '      <td class="font-weight-bold" style="width:auto;">R$ '+fMascaraValor(ProvTotal)+'</td>';
									content += '    </tr>'; 
	
							}); //$.each(lista, function (index, value) {
													
							content += '    <tr style="font-size: 12px;" class="text-center text-dark font-weight-bold" > ';
							content += '      <td> </td>';
							if ( TpRendTributavel == 'J' ) 
								content += '      <td> </td>';
							content += '      <td>TOTAL</td>';
							content += '      <td> </td>';
							if ( TpRendTributavel == 'J' || TpRendTributavel == 'F' ) 
								content += '      <td> </td>';
							content += '      <td>R$ '+fMascaraValor(ProvVlrPreco)+'</td>';
							content += '      <td>R$ '+fMascaraValor(ProvVlrTotal)+'</td>';
							content += '    </tr>'; 
													
							content += '  </tbody>';
							content += '</table>';
	
							DivGridIRPFRendTributaveis.html("");
							DivGridIRPFRendTributaveis.append( content );	
							
							$("#PopModalDetalheIRPFRendTributaveis").modal({backdrop: "static"});
							return true;
						}// if ( lista.length > 0 ){
	
						fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Sem Dados para Exibir!'); 
						return true;
		   
					} else {
						$("#PopModalDetalheIRPFRendTributaveis").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					$("#PopModalDetalheIRPFRendTributaveis").modal("hide");	
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
		$("#PopModalDetalheIRPFRendTributaveis").modal("hide");	
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	}  
}	

async function fLimparGridBensEDireitos( urlPadrao ){
	try {	
		
		 promise = new Promise( (resolve, reject) => {

			$('#GridBensDireitos').dataTable().fnClearTable();
			$("#GridBensDireitos").dataTable({ bDestroy: true }).fnDestroy();
			
			$('#GridBensDireitos').DataTable( {
				oLanguage: fTraduzirGrid(), 
				aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth:  "50px", targets: 0 }, //  0-Codigo
					{ bSortable: false, bOrderable: false, sWidth:  "50px", targets: 1 }, //  1-CNPJ
					{ bSortable: false, bOrderable: false, sWidth: "600px", targets: 2 }, //  2-Dicriminação
					{ bSortable: false, bOrderable: false, sWidth:  "50px", targets: 3 }, //  3-ValorAnterior
					{ bSortable: false, bOrderable: false, sWidth:  "50px", targets: 4 }, //  4-ValorAtual
					{ visible  : false,                                     targets: 5 }, //  5-CodAtivo
					{ visible  : false,                                     targets: 6 }, //  6-TpBensDireitos
					{ bSortable: false,                    sWidth: "30px",  targets: 7 }  //  7-Acao
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				bSearchable: false,
				bOrderable: false,
				bSortable: false,
				bAutoWidth: false,
				bPaginate: false,
				bOrdering: false
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

async function fMontarGridBensEDireitos( urlPadrao, dataSet, AnoDeclaracao ){
  try {   

		 promise = new Promise( (resolve, reject) => {

			$('#GridBensDireitos').DataTable( {
				processing: true,
				serverSide: false,
						  oLanguage: fTraduzirGrid(), 
						  data: dataSet,
				aoColumns: [
								  { bSortable: false, bOrderable: false, sWidth:  "50px", targets: 0 }, //  0-Codigo
								  { bSortable: false, bOrderable: false, sWidth:  "50px", targets: 1 }, //  1-CNPJ
								  { bSortable: false, bOrderable: false, sWidth: "600px", targets: 2 }, //  2-Dicriminação
								  { bSortable: false, bOrderable: false, sWidth:  "50px", targets: 3 ,  //  3-ValorAnterior
									  render: function ( data, type, row ) { 
										  if ( type == "display") return "R$ " + row[3]; //  3-ValorAnterior
										  return data;
									  } 				 
								  },  //  3-ValorAnterior
								  { bSortable: false, bOrderable: false, sWidth:  "50px", targets: 4,  //  4-ValorAtual
									  render: function ( data, type, row ) { 
										  if ( type == "display") return "R$ " + row[4]; //  4-ValorAtual
										  return data;
									  } 				 
								  },  //  4-ValorAtual
								  { visible  : false,                                     targets: 5 }, // 5-CodAtivo
								  { visible  : false,                                     targets: 6 }, // 6-TpRendTributavel
								  { bSortable: false,                    sWidth: "5px",   targets: 7,   // 7-Acao
									  render: function ( data, type, row ) {
										  var btnVis = "";
										  var btnDis = '';
										  var btnCor = 'primary';
										  if ( type == "display") {
											  var TotTotalAtual  = row[4]; // 4-ValorAtual
											  var CodAtivo       = row[5]; // 5-CodAtivo
											  var TpBensDireitos = row[6]; // 6-TpRendTributavel
											  if( TpBensDireitos == "DIV"  || TpBensDireitos == "JSCP" ) { btnDis = ' disabled'; btnCor = 'secondary'; }
											  //btnVis += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
											  btnVis += '<a class="btn btn-sm btn-icon btn-icon-mini btn-round btn-simple btn-'+btnCor+btnDis+'"'+btnDis+' style="font-size:9px;" title="Visualizar Bens e Direitos" href="javascript:void(0);" onclick="fAbrirModalDetalheBensEDireitos( \''+urlPadrao+'\', \''+AnoDeclaracao+'\', \''+TpBensDireitos+'\', \''+CodAtivo+'\', \''+TotTotalAtual+'\' );">'; 
											  btnVis += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
											  btnVis += '</a>';
											  //btnVis += '</div>';
										  }
										  return btnVis;
									  } 
								  } //  6-Acao
				],
				createdRow : function(row,data,dataIndex) {			  
                      $('td', row).eq(0).addClass('text-center');
                      $('td', row).eq(1).addClass('text-center');
                      $('td', row).eq(2).addClass('text-center');
                      $('td', row).eq(3).addClass('text-center');
                      $('td', row).eq(4).addClass('text-center');
				}, //createdRow
				initComplete: function( settings, json ) {
				}, //initComplete
                  dom: 'frtBpi', //Bfrtip //frtBip  //frtBpi
                  buttons: [
                        {
                           extend:    'excelHtml5',
                           text:      '<i class="fa fa-file-excel-o"></i> Excel',
                           className: 'btn btn-outline-default btn-sm',
                           title: NOME_PROJETO + ' - Bens e Direitos - ' + AnoDeclaracao,
                           titleAttr: 'Excel',
                           exportOptions: {  columns: [ 0, 1, 2, 3, 4 ] }
                        },
                        {
                          extend: 'csvHtml5',
                          charset: 'UTF-8',
                          fieldSeparator: ';',
                          titleAttr: 'CSV',
                          text:      '<i class="fa fa-file-o"></i> CSV',
                          className: 'btn btn-outline-default btn-sm',
                          title: NOME_PROJETO + ' - Bens e Direitos - ' + AnoDeclaracao,
                          bom: true,
                          exportOptions: {  columns: [ 0, 1, 2, 3, 4 ] } //orthogonal: 'export',
                        },
                        {
                          extend: 'pdfHtml5',
                          text:      '<i class="fa fa-file-pdf-o"></i> PDF',
                          className: 'btn btn-default btn-sm',
                          titleAttr: 'PDF',
                          title: NOME_PROJETO + ' - Bens e Direitos - ' + AnoDeclaracao,
                          pageSize: 'A3',
                          alignment: 'center',
                          exportOptions: {  columns: [ 0, 1, 2, 3, 4 ] }, //orthogonal: 'export',
                          footer: true,
                          customize: function (doc) {
                              doc.defaultStyle.fontSize = 12;
                              doc.styles.tableHeader.fontSize = 14;
                          }
                        },
                        {
                          extend: 'print',
                          text:      '<i class="fa fa-print"></i> Imprimir',
                          title: NOME_PROJETO + ' - Bens e Direitos - ' + AnoDeclaracao,
                          titleAttr: 'Imprimir',
                          className: 'btn btn-default btn-sm',
                          exportOptions: {  columns: [ 0, 1, 2, 3, 4 ] } //orthogonal: 'export',
                        }
                  ],
                  order: [],
                  bFilter: false,
                  bInfo: false,
                  bLengthChange: false,
                  bSearchable: false,
                  bOrderable: false,
                  bSortable: false,
                  bAutoWidth: false,
                  bPaginate: false,
                  bOrdering: false
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
        if ( e.description != undefined )
		  fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fCarregarGridBensEDireitos( urlPadrao, AnoDeclaracao ){
  try {   

		 promise = new Promise( (resolve, reject) => {

			$('#GridBensDireitos').dataTable().fnClearTable();
			$("#GridBensDireitos").dataTable({ bDestroy: true }).fnDestroy();
	
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url : urlPadrao + "IRPF/gridBensEDiretos",
				data: { AnoDeclaracao : AnoDeclaracao },
				success: function(result) {
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
	
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						// fLimparSomenteGrid(( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						// fLimparSomenteGrid(( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridBensEDireitos( urlPadrao, lista, AnoDeclaracao );
					} else{
						// fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					// fLimparSomenteGrid(( urlPadrao );( urlPadrao );
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
      	if ( e.description != undefined )
			fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fAbrirModalDetalheBensEDireitos( urlPadrao, AnoDeclaracao, TpBensDireitos, CodAtivo, TotTotalAtual ){
	try {  

		 promise = new Promise( (resolve, reject) => {
	
			fLimparAreaAlertaPrinc();
			
			var DivGridIRPFBensDireitos = $("#DivGridIRPFBensDireitos");
			DivGridIRPFBensDireitos.html("");

			if( (AnoDeclaracao=="") || (TpBensDireitos=="") || (CodAtivo=="") ){
				fCriarAlertaPrinc(TP_ALERTA_AVISO, "Dados da pesquisa inválido!");
				return false;
			}	

			var vURL = "";
			if( TpBensDireitos == "ACAO" || TpBensDireitos == "FII" || TpBensDireitos == "ETF" || TpBensDireitos == "BDR" || TpBensDireitos == "CRIPTO" ) vURL = urlPadrao + "Analise/gridOper";
			if( TpBensDireitos == "DIV"  || TpBensDireitos == "JSCP" ) vURL = urlPadrao + "IRPF/gridBensEDiretosDetalhe";
			
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : vURL,
				data    : { AnoDeclaracao: AnoDeclaracao, TpBensDireitos: TpBensDireitos, CodAtivo: CodAtivo },
				success: function(result) {  
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
					
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						$("#PopModalDetalheIRPFBensDireitos").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						$("#PopModalDetalheIRPFBensDireitos").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					} else if (resultado == "OK") {

						if ( lista.length > 0 ){

								var content = '';

								if( TpBensDireitos == "ACAO" || TpBensDireitos == "FII" || TpBensDireitos == "ETF" || TpBensDireitos == "BDR" || TpBensDireitos == "CRIPTO" ) {
											
										content += '<table class="table table-sm table-hover table-condensed nowrap" style="font-size: 12px;" border="0" cellspacing="0" width="100%" style="margin: 0px;">';
										content += '  <thead>';
										content += '    <tr style="font-size: 12px;" class="thead-dark font-weight-bold"> ';
										content += '      <th>Data</th>';
										content += '      <th>Ativo</th>';
										content += '      <th>Tipo</th>';
										content += '      <th>Quant.</th>';
										content += '      <th>Custo/Ação</th>';
										content += '      <th>Preço Médio</th>';
										content += '      <th>Total</th>';
										content += '      <th>Valorização</th>';
										content += '    </tr>';  
										content += '  </thead>';
										content += '  <tbody>';

										var TotQuant      = 0;
										var TotPrecoMedio = 0.00;
					
										$.each(lista, function (index, value) {

											var vCorLinha      = 'text-dark';
												var OperCodAtivo   = CodAtivo;
												var OperTipo       = value[0]; // 0-Tipo
												var OperCateg      = value[1]; // 1-Categoria
												var OperCorret     = value[2]; // 2-Corretora
												var OperData       = value[3]; // 3-Data
												var OperQuant      = value[4]; // 4-Quant
												var OperPrecoCusto = value[5]; // parseFloat( GetValorDecimal(value[5]) ); // 5-PrecoCusto
												var OperPrecoMedio = value[6]; // parseFloat( GetValorDecimal(value[6]) ); // 6-PrecoMedio
												var OperTotal      = value[7]; // parseFloat( GetValorDecimal(value[7]) ); // 7-Total 
												var OperValoriz    = value[8]; // parseFloat( GetValorDecimal(value[8]) ); // 8-Valorizacao 
												
												if ( OperTipo == "Venda" || OperTipo == "Venda/Troca" ){
													if ( OperValoriz != "" && parseFloat(GetValorDecimal(OperValoriz)) > 0 ) vCorLinha = 'text-success';
													if ( OperValoriz != "" && parseFloat(GetValorDecimal(OperValoriz)) < 0 ) vCorLinha = 'text-danger';
												}

												if ( OperTipo != 'Projetado' ) {
													TotPrecoMedio = parseFloat( GetValorDecimal(OperPrecoMedio) );
														if ( OperTipo == "Compra" || OperTipo == "Compra/Troca" || OperTipo == "Bonificação" ) TotQuant += GetValorInteiro(OperQuant);
														if ( OperTipo == "Venda" || OperTipo == "Venda/Troca"                               ) TotQuant -= GetValorInteiro(OperQuant);
														content += '    <tr class="text-center '+vCorLinha+'" > ';
														content += '      <td style="width:auto;">'+OperData+'</td>';
														content += '      <td class="font-weight-bold" style="width:auto;">'+OperCodAtivo+'</td>';
														content += '      <td style="width:auto;">'+OperTipo+'</td>';
														content += '      <td style="width:auto;">'+OperQuant+'</td>';
														content += '      <td style="width:auto;">R$ '+OperPrecoCusto+'</td>';
														content += '      <td style="width:auto;">R$ '+OperPrecoMedio+'</td>';
														content += '      <td class="font-weight-bold" style="width:auto;">R$ '+OperTotal+'</td>';
														content += '      <td class="font-weight-bold" style="width:auto;">'+OperValoriz+'</td>';
														content += '    </tr>'; 
												} //	if ( OperTipo != 'Projetado' ) {

										}); //$.each(lista, function (index, value) {
																
										content += '    <tr style="font-size: 12px;" class="text-center text-dark font-weight-bold" > ';
										content += '      <td> </td>'; //OperData
										content += '      <td>TOTAL</td>'; //OperCodAtivo
										content += '      <td> </td>'; //OperTipo
										content += '      <td>'+colcarFormacataoInteiro(TotQuant)+'</td>'; //OperQuant
										content += '      <td> </td>'; //OperPrecoCusto
										content += '      <td>R$ '+fMascaraValor(TotPrecoMedio)+'</td>'; //OperPrecoMedio
										content += '      <td class="font-weight-bold" style="width:auto;">R$ '+ TotTotalAtual +'</td>';//OperTotal
										content += '      <td> </td>'; //OperValoriz
										content += '    </tr>'; 									
																
										content += '  </tbody>';
										content += '</table>';
										
										DivGridIRPFBensDireitos.html("");
										DivGridIRPFBensDireitos.append( content );	
										$("#PopModalDetalheIRPFBensDireitos").modal({backdrop: "static"});
										return true;

									} //if( TpBensDireitos == "ACAO" || TpBensDireitos == "FII" || TpBensDireitos == "ETF" || TpBensDireitos == "BDR" )
										
									if( TpBensDireitos == "DIV" || TpBensDireitos == "JSCP" ) {
										DivGridIRPFBensDireitos.html("");
										DivGridIRPFBensDireitos.append( content );	
										$("#PopModalDetalheIRPFBensDireitos").modal({backdrop: "static"});
										return true;
									} // if( TpBensDireitos == "DIV" || TpBensDireitos == "JSCP" ) {
								
						}// if ( lista.length > 0 ){

						fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Sem Dados para Exibir!'); 
						return true;
		
					} else {
						$("#PopModalDetalheIRPFBensDireitos").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					$("#PopModalDetalheIRPFBensDireitos").modal("hide");	
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
		$("#PopModalDetalheIRPFBensDireitos").modal("hide");	
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	}  
}	

async function fLimparDadosGridMeses( NomeMes ){

     promise = new Promise( (resolve, reject) => {

		var ValorDafault = "R$ 0,00";

		$('#MercAvst-Comum-'+NomeMes).html(              ValorDafault );
		$('#MercAvst-DayTrade-'+NomeMes).html(           ValorDafault );
		$('#ResultLiq-Comum-'+NomeMes).html(             ValorDafault );
		$('#ResultLiq-DayTrade-'+NomeMes).html(          ValorDafault );
		$('#ResultNeg-Comum-'+NomeMes).html(             ValorDafault );
		$('#ResultNeg-DayTrade-'+NomeMes).html(          ValorDafault );
		$('#ResultBase-Comum-'+NomeMes).html(            ValorDafault );
		$('#ResultBase-DayTrade-'+NomeMes).html(         ValorDafault );
		$('#ResultPrej-Comum-'+NomeMes).html(            ValorDafault );
		$('#ResultPrej-DayTrade-'+NomeMes).html(         ValorDafault );
		$('#ResultDev-Comum-'+NomeMes).html(             ValorDafault );
		$('#ResultDev-DayTrade-'+NomeMes).html(          ValorDafault );
		$('#Consolid-Devido-'+NomeMes).html(             ValorDafault );
		$('#Consolid-DayTrade-MesAtual-'+NomeMes).html(  ValorDafault );
		$('#Consolid-DayTrade-MesAnt-'+NomeMes).html(    ValorDafault );
		$('#Consolid-DayTrade-Compensar-'+NomeMes).html( ValorDafault );
		$('#Consolid-Comum-MesAtual-'+NomeMes).html(     ValorDafault );
		$('#Consolid-Comum-MesAnt-'+NomeMes).html(       ValorDafault );
		$('#Consolid-Comum-Compensar-'+NomeMes).html(    ValorDafault );
		$('#Consolid-Pagar-'+NomeMes).html(              ValorDafault );

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
    })
    .then( txt => {
        //console.log('Sucesso: ' + txt);
    })
    .catch( txt => {
        //fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    });

}

async function fLimparGridMeses( urlPadrao ){

     promise = new Promise( (resolve, reject) => {

		fLimparDadosGridMeses('JAN');
		fLimparDadosGridMeses('FEV');
		fLimparDadosGridMeses('MAR');
		fLimparDadosGridMeses('ABR');
		fLimparDadosGridMeses('MAI');
		fLimparDadosGridMeses('JUN');
		fLimparDadosGridMeses('JUL');
		fLimparDadosGridMeses('AGO');
		fLimparDadosGridMeses('SET');
		fLimparDadosGridMeses('OUT');
		fLimparDadosGridMeses('NOV');
		fLimparDadosGridMeses('DEZ');	

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
    })
    .then( txt => {
        //console.log('Sucesso: ' + txt);
    })
    .catch( txt => {
        //fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    });
}


async function fMostrarDadosGridMeses( Dados, NomeMes, AnoDeclaracao ){
    
     promise = new Promise( (resolve, reject) => {

		if( Dados ){
			$('#MercAvst-Comum-'+NomeMes).html(              "R$ " + Dados.MercAvst[0]  );
			$('#MercAvst-DayTrade-'+NomeMes).html(           "R$ " + Dados.MercAvst[1]  );					
			$('#ResultLiq-Comum-'+NomeMes).html(             "R$ " + Dados.ResultLiq[0] );
			$('#ResultLiq-DayTrade-'+NomeMes).html(          "R$ " + Dados.ResultLiq[1] );
			$('#ResultNeg-Comum-'+NomeMes).html(             "R$ " + Dados.ResultLiq[2] );
			$('#ResultNeg-DayTrade-'+NomeMes).html(          "R$ " + Dados.ResultLiq[3] );
			$('#ResultBase-Comum-'+NomeMes).html(            "R$ " + Dados.ResultLiq[4] );
			$('#ResultBase-DayTrade-'+NomeMes).html(         "R$ " + Dados.ResultLiq[5] );
			$('#ResultPrej-Comum-'+NomeMes).html(            "R$ " + Dados.ResultLiq[6] );
			$('#ResultPrej-DayTrade-'+NomeMes).html(         "R$ " + Dados.ResultLiq[7] );
			$('#ResultDev-Comum-'+NomeMes).html(             "R$ " + Dados.ResultLiq[8] );
			$('#ResultDev-DayTrade-'+NomeMes).html(          "R$ " + Dados.ResultLiq[9] );					
			$('#Consolid-Devido-'+NomeMes).html(             "R$ " + Dados.Consolid[0]  );
			$('#Consolid-DayTrade-MesAtual-'+NomeMes).html(  "R$ " + Dados.Consolid[1]  );
			$('#Consolid-DayTrade-MesAnt-'+NomeMes).html(    "R$ " + Dados.Consolid[2]  );
			$('#Consolid-DayTrade-Compensar-'+NomeMes).html( "R$ " + Dados.Consolid[3]  );
			$('#Consolid-Comum-MesAtual-'+NomeMes).html(     "R$ " + Dados.Consolid[4]  );
			$('#Consolid-Comum-MesAnt-'+NomeMes).html(       "R$ " + Dados.Consolid[5]  );
			$('#Consolid-Comum-Compensar-'+NomeMes).html(    "R$ " + Dados.Consolid[6]  );
			$('#Consolid-Pagar-'+NomeMes).html(              "R$ " + Dados.Consolid[7]  );
		}	
	
		//$('#GridMes'+NomeMes).dataTable().fnClearTable();
		$('#GridMes'+NomeMes).dataTable({ bDestroy: true }).fnDestroy();

		$('#GridMes'+NomeMes).DataTable( {
			oLanguage: fTraduzirGrid(), 
			aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth: "400px", targets: 0 }, //  0-Descricao
					{ bSortable: false, bOrderable: false, sWidth: "200px", targets: 1 }, //  1-Operações Comums
					{ bSortable: false, bOrderable: false, sWidth: "20px",  targets: 2 }  //  2-Day-Trade
				 ],
			  createdRow : function(row,data,dataIndex) {			  
					$('td', row).addClass('text-center'); 
			  }, //createdRow
			  initComplete: function( settings, json ) {
			  }, //initComplete
			dom: 'frtBpi', //Bfrtip //frtBip  //frtBpi
			buttons: [  
			  {
				 extend:    'excelHtml5',
				 text:      '<i class="fa fa-file-excel-o"></i> Excel',
				 className: 'btn btn-outline-default btn-sm',
				title: NOME_PROJETO + ' - Renda Variavel - Ganhos ou Perdas Liquidos em Operacoes Comuns ou Day-Trade - ' + NomeMes + '-' + AnoDeclaracao,
				 titleAttr: 'Excel',
				 exportOptions: {  columns: [ 0, 1, 2 ] }
			  }, 
			  {
				extend: 'csvHtml5',
				charset: 'UTF-8',
				fieldSeparator: ';',
				titleAttr: 'CSV',
				text:      '<i class="fa fa-file-o"></i> CSV',
				className: 'btn btn-outline-default btn-sm',
				title: NOME_PROJETO + ' - Renda Variavel - Ganhos ou Perdas Liquidos em Operacoes Comuns ou Day-Trade - ' + NomeMes + '-' + AnoDeclaracao,
				bom: true,
				exportOptions: {  columns: [ 0, 1, 2 ] } //orthogonal: 'export',
			  },
			  {
				extend: 'pdfHtml5',
				text:      '<i class="fa fa-file-pdf-o"></i> PDF',
				className: 'btn btn-default btn-sm',
				titleAttr: 'PDF',
				title: NOME_PROJETO + ' - Renda Variavel - Ganhos ou Perdas Liquidos em Operacoes Comuns ou Day-Trade - ' + NomeMes + '-' + AnoDeclaracao,
				pageSize: 'A3',
				alignment: 'center',
				exportOptions: {  columns: [ 0, 1, 2 ] }, //orthogonal: 'export',
				footer: true,
				customize: function (doc) { 
					doc.defaultStyle.fontSize = 12; 
					doc.styles.tableHeader.fontSize = 14; 
				}
			  },
			  {
				extend: 'print',
				text:      '<i class="fa fa-print"></i> Imprimir',
				title: NOME_PROJETO + ' - Renda Variavel - Ganhos ou Perdas Liquidos em Operacoes Comuns ou Day-Trade - ' + NomeMes + '-' + AnoDeclaracao,
				titleAttr: 'Imprimir',
				className: 'btn btn-default btn-sm',
				exportOptions: {  columns: [ 0, 1, 2 ] } //orthogonal: 'export',
			  }
			],			
			order: [],
			bFilter: false,
			bInfo: false,
			bLengthChange: false,
			bSearchable: false,
			bOrderable: false,
			bSortable: false,
			bAutoWidth: false,
			bPaginate: false,
			bOrdering: false
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

} 

async function fCarregarGridMeses( urlPadrao, AnoDeclaracao, CalcVlrSuperior ){
  try {   
		
		 promise = new Promise( (resolve, reject) => {

			$('#TabMes a[href="#AbaMesJAN"]').tab('show');

			//$('#GridMesJAN').dataTable().fnClearTable();
			//$('#GridMesFEV').dataTable().fnClearTable();
			//$('#GridMesMAR').dataTable().fnClearTable();
			//$('#GridMesABR').dataTable().fnClearTable();
			//$('#GridMesMAI').dataTable().fnClearTable();
			//$('#GridMesJUN').dataTable().fnClearTable();
			//$('#GridMesJUL').dataTable().fnClearTable();
			//$('#GridMesAGO').dataTable().fnClearTable();
			//$('#GridMesSET').dataTable().fnClearTable();
			//$('#GridMesOUT').dataTable().fnClearTable();
			//$('#GridMesNOV').dataTable().fnClearTable();
			//$('#GridMesDEZ').dataTable().fnClearTable();
			// $('#GridMesJAN').dataTable({ bDestroy: true }).fnDestroy();
			// $('#GridMesFEV').dataTable({ bDestroy: true }).fnDestroy();
			// $('#GridMesMAR').dataTable({ bDestroy: true }).fnDestroy();
			// $('#GridMesABR').dataTable({ bDestroy: true }).fnDestroy();
			// $('#GridMesMAI').dataTable({ bDestroy: true }).fnDestroy();
			// $('#GridMesJUN').dataTable({ bDestroy: true }).fnDestroy();
			// $('#GridMesJUL').dataTable({ bDestroy: true }).fnDestroy();
			// $('#GridMesAGO').dataTable({ bDestroy: true }).fnDestroy();
			// $('#GridMesAGO').dataTable({ bDestroy: true }).fnDestroy();
			// $('#GridMesOUT').dataTable({ bDestroy: true }).fnDestroy();
			// $('#GridMesNOV').dataTable({ bDestroy: true }).fnDestroy();
			// $('#GridMesDEZ').dataTable({ bDestroy: true }).fnDestroy();
	
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url : urlPadrao + "IRPF/gridRendaVariavel",
				data: { AnoDeclaracao: AnoDeclaracao, CalcVlrSuperior: CalcVlrSuperior },
				success: function(result) {
			
					finalizarAnimacaoPesquisa();
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var Meses     = result.data.Dados; 
					var Dados     = ""; 
	
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						// fLimparSomenteGrid(( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						// fLimparSomenteGrid(( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
	
						fMostrarDadosGridMeses( Meses.JAN, 'JAN', AnoDeclaracao );
						fMostrarDadosGridMeses( Meses.FEV, 'FEV', AnoDeclaracao );
						fMostrarDadosGridMeses( Meses.MAR, 'MAR', AnoDeclaracao );
						fMostrarDadosGridMeses( Meses.ABR, 'ABR', AnoDeclaracao );
						fMostrarDadosGridMeses( Meses.MAI, 'MAI', AnoDeclaracao );
						fMostrarDadosGridMeses( Meses.JUN, 'JUN', AnoDeclaracao );
						fMostrarDadosGridMeses( Meses.JUL, 'JUL', AnoDeclaracao );
						fMostrarDadosGridMeses( Meses.AGO, 'AGO', AnoDeclaracao );
						fMostrarDadosGridMeses( Meses.SET, 'SET', AnoDeclaracao );
						fMostrarDadosGridMeses( Meses.OUT, 'OUT', AnoDeclaracao );
						fMostrarDadosGridMeses( Meses.NOV, 'NOV', AnoDeclaracao );
						fMostrarDadosGridMeses( Meses.DEZ, 'DEZ', AnoDeclaracao );	
								
						return true;
					} else{
						// fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					// fLimparSomenteGrid(( urlPadrao );( urlPadrao );
					finalizarAnimacaoPesquisa();
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
      	finalizarAnimacaoPesquisa();
		if ( e.description != undefined )
			fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fLimparDadosGridMesesFII( NomeMes ){

	 promise = new Promise( (resolve, reject) => {

		var ColResultLiqMes    = $('#FII-RENDA-VAR-'+NomeMes+'-ResultLiqMes');
		var ColResultNegMesAnt = $('#FII-RENDA-VAR-'+NomeMes+'-ResultNegMesAnt');
		var ColBaseCaclIR      = $('#FII-RENDA-VAR-'+NomeMes+'-BaseCaclIR');
		var ColPrejuAComp      = $('#FII-RENDA-VAR-'+NomeMes+'-PrejuAComp');
		var ColAliquotaIR      = $('#FII-RENDA-VAR-'+NomeMes+'-AliquotaIR');
		var ColIRDevido        = $('#FII-RENDA-VAR-'+NomeMes+'-IRDevido');

		ColResultLiqMes.html(    "R$ 0,00" );
		ColResultNegMesAnt.html( "R$ 0,00" );
		ColBaseCaclIR.html(      "R$ 0,00" );
		ColPrejuAComp.html(      "R$ 0,00" );
		ColAliquotaIR.html(      "20,00%"  );
		ColIRDevido.html(        "R$ 0,00" );

		ColResultLiqMes.addClass('text-dark');
		ColResultLiqMes.removeClass('text-success');
		ColResultLiqMes.removeClass('text-danger');
		
		if ( NomeMes == "JAN" ) ColResultNegMesAnt.addClass('text-dark');
		ColResultNegMesAnt.removeClass('text-success');
		ColResultNegMesAnt.removeClass('text-danger');
		
		ColBaseCaclIR.removeClass('text-success');
		ColBaseCaclIR.removeClass('text-danger');
		
		ColPrejuAComp.removeClass('text-success');
		ColPrejuAComp.removeClass('text-danger');
		
		ColIRDevido.removeClass('text-success');
		ColIRDevido.removeClass('text-danger');
		
		resolve(true);
		// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
	})
	.then( txt => {
		//console.log('Sucesso: ' + txt);
	})
	.catch( txt => {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	});
}


async function fLimparGridMesesFII( urlPadrao ){
	try {	

		 promise = new Promise( (resolve, reject) => {
	
			fLimparDadosGridMesesFII('JAN');
			fLimparDadosGridMesesFII('FEV');
			fLimparDadosGridMesesFII('MAR');
			fLimparDadosGridMesesFII('ABR');
			fLimparDadosGridMesesFII('MAI');
			fLimparDadosGridMesesFII('JUN');
			fLimparDadosGridMesesFII('JUL');
			fLimparDadosGridMesesFII('AGO');
			fLimparDadosGridMesesFII('SET');
			fLimparDadosGridMesesFII('OUT');
			fLimparDadosGridMesesFII('NOV');
			fLimparDadosGridMesesFII('DEZ');
	
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

async function fMostrarDadosGridMesesFII( Dados, NomeMes ){
	
     promise = new Promise( (resolve, reject) => {

		if( Dados ){

			var ColResultLiqMes    = $('#FII-RENDA-VAR-'+NomeMes+'-ResultLiqMes');
			var ColResultNegMesAnt = $('#FII-RENDA-VAR-'+NomeMes+'-ResultNegMesAnt');
			var ColBaseCaclIR      = $('#FII-RENDA-VAR-'+NomeMes+'-BaseCaclIR');
			var ColPrejuAComp      = $('#FII-RENDA-VAR-'+NomeMes+'-PrejuAComp');
			var ColAliquotaIR      = $('#FII-RENDA-VAR-'+NomeMes+'-AliquotaIR');
			var ColIRDevido        = $('#FII-RENDA-VAR-'+NomeMes+'-IRDevido');
	
			ColResultLiqMes.html(    "R$ "+Dados.ResultLiqMes );
			ColResultNegMesAnt.html( "R$ "+Dados.ResultNegMesAnt );
			ColBaseCaclIR.html(      "R$ "+Dados.BaseCaclIR );
			ColPrejuAComp.html(      "R$ "+Dados.PrejuAComp );
			ColAliquotaIR.html(      Dados.AliquotaIR+"%" );
			ColIRDevido.html(        "R$ "+Dados.IRDevido );
			
			var VlrResultLiqMes    = parseFloat( GetValorDecimal( Dados.ResultLiqMes    ) );
			var VlrResultNegMesAnt = parseFloat( GetValorDecimal( Dados.ResultNegMesAnt ) );
			var VlrBaseCaclIR      = parseFloat( GetValorDecimal( Dados.BaseCaclIR      ) ); 
			var VlrPrejuAComp      = parseFloat( GetValorDecimal( Dados.PrejuAComp      ) ); 
			var VlrIRDevido        = parseFloat( GetValorDecimal( Dados.IRDevido        ) );
			
			if ( VlrResultLiqMes    !=  0.00 ) ColResultLiqMes.removeClass('text-dark'); 
			if ( VlrResultLiqMes    >   0.00 ) ColResultLiqMes.addClass('text-success'); 
			if ( VlrResultLiqMes    <   0.00 ) ColResultLiqMes.addClass('text-danger'); 
	
			if ( VlrResultNegMesAnt !=  0.00 ) ColResultNegMesAnt.removeClass('text-dark'); 
			if ( VlrResultNegMesAnt !=  0.00 ) ColResultNegMesAnt.addClass('text-danger');
	
			if ( VlrBaseCaclIR      !=  0.00 ) ColBaseCaclIR.addClass('text-success');  
	
			if ( VlrPrejuAComp      !=  0.00 ) ColPrejuAComp.addClass('text-danger'); 
	
			if ( VlrIRDevido        !=  0.00 ) ColIRDevido.addClass('text-danger'); 
	
		}		

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
    })
    .then( txt => {
        //console.log('Sucesso: ' + txt);
    })
    .catch( txt => {
        //fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	});
} 

async function fCarregarGridMesesFII( urlPadrao, AnoDeclaracao ){
	try {   
		
		 promise = new Promise( (resolve, reject) => {

			//$('#GridRendVarFII').dataTable().fnClearTable();
			$("#GridRendVarFII").dataTable({ bDestroy: true }).fnDestroy();

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url : urlPadrao + "IRPF/gridRendaVariavelFII",
				data: { AnoDeclaracao: AnoDeclaracao },
				success: function(result) {
			
					finalizarAnimacaoPesquisa();
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var Meses     = result.data.Dados;  
					var Dados     = ''; 
	
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						// fLimparSomenteGrid(( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						// fLimparSomenteGrid(( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {

						fMostrarDadosGridMesesFII( Meses.JAN, 'JAN' );
						fMostrarDadosGridMesesFII( Meses.FEV, 'FEV' );
						fMostrarDadosGridMesesFII( Meses.MAR, 'MAR' );
						fMostrarDadosGridMesesFII( Meses.ABR, 'ABR' );
						fMostrarDadosGridMesesFII( Meses.MAI, 'MAI' );
						fMostrarDadosGridMesesFII( Meses.JUN, 'JUN' );
						fMostrarDadosGridMesesFII( Meses.JUL, 'JUL' );
						fMostrarDadosGridMesesFII( Meses.AGO, 'AGO' );
						fMostrarDadosGridMesesFII( Meses.SET, 'SET' );
						fMostrarDadosGridMesesFII( Meses.OUT, 'OUT' );
						fMostrarDadosGridMesesFII( Meses.NOV, 'NOV' );
						fMostrarDadosGridMesesFII( Meses.DEZ, 'DEZ' );	

						$('#GridRendVarFII').DataTable( {
							oLanguage: fTraduzirGrid(), 
							aoColumns: [
									{ bSortable: false, bOrderable: false, sWidth: "10px",  targets: 0 }, //  0-Mês
									{ bSortable: false, bOrderable: false, sWidth: "100px", targets: 1 }, //  1-Resultado Líquido do Mês
									{ bSortable: false, bOrderable: false, sWidth: "100px", targets: 2 }, //  2-Resultado Negativo até o Mês Anterior
									{ bSortable: false, bOrderable: false, sWidth: "100px", targets: 3 }, //  3-Base de Cálculo do Imposto
									{ bSortable: false, bOrderable: false, sWidth: "60px",  targets: 4 }, //  4-Prejuízo a Compensar
									{ bSortable: false, bOrderable: false, sWidth: "50px",  targets: 5 }, //  5-Alíquota do Imposto
									{ bSortable: false, bOrderable: false, sWidth: "50px",  targets: 6 }  //  6-Imposto Devido
								],
							createdRow : function(row,data,dataIndex) {			  
									$('td', row).addClass('text-center'); 
							}, //createdRow
								initComplete: function( settings, json ) {
							}, //initComplete
							dom: 'frtBpi', //Bfrtip //frtBip  //frtBpi
							buttons: [  
							{
								extend:    'excelHtml5',
								text:      '<i class="fa fa-file-excel-o"></i> Excel',
								className: 'btn btn-outline-default btn-sm',
								title: NOME_PROJETO + ' - Renda Variavel - Operacoes de Fundos de Investimento Imobiliario - ' + AnoDeclaracao,
								titleAttr: 'Excel',
								exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6 ] }
							}, 
							{
								extend: 'csvHtml5',
								charset: 'UTF-8',
								fieldSeparator: ';',
								titleAttr: 'CSV',
								text:      '<i class="fa fa-file-o"></i> CSV',
								className: 'btn btn-outline-default btn-sm',
								title: NOME_PROJETO + ' - Renda Variavel - Operacoes de Fundos de Investimento Imobiliario - ' + AnoDeclaracao,
								bom: true,
								exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6 ] } //orthogonal: 'export',
							},
							{
								extend: 'pdfHtml5',
								text:      '<i class="fa fa-file-pdf-o"></i> PDF',
								className: 'btn btn-default btn-sm',
								titleAttr: 'PDF',
								title: NOME_PROJETO + ' - Renda Variavel - Operacoes de Fundos de Investimento Imobiliario - ' + AnoDeclaracao,
								pageSize: 'A3',
								alignment: 'center',
								exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6 ] }, //orthogonal: 'export',
								footer: true,
								customize: function (doc) { 
									doc.defaultStyle.fontSize = 12; 
									doc.styles.tableHeader.fontSize = 14; 
								}
							},
							{
								extend: 'print',
								text:      '<i class="fa fa-print"></i> Imprimir',
								title: NOME_PROJETO + ' - Renda Variavel - Operacoes de Fundos de Investimento Imobiliario - ' + AnoDeclaracao,
								titleAttr: 'Imprimir',
								className: 'btn btn-default btn-sm',
								exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6 ] } //orthogonal: 'export',
							}
							],			
							order: [],
							bFilter: false,
							bInfo: false,
							bLengthChange: false,
							bSearchable: false,
							bOrderable: false,
							bSortable: false,
							bAutoWidth: false,
							bPaginate: false,
							bOrdering: false
						});

						return true;
					} else{
						// fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					// fLimparSomenteGrid(( urlPadrao );( urlPadrao );
					finalizarAnimacaoPesquisa();
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
			finalizarAnimacaoPesquisa();
		  if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	  }
}

async function fSalvarConfigApuracao( urlPadrao, cb ){
	try {

		 promise = new Promise( (resolve, reject) => {

            var CalcVlrSuperior = cb.checked ? "S" : "N";

			 $.ajax({
				 cache   : "false",
				 dataType: "json",
				 async   : true,
				 type    : "POST",
				 url     : urlPadrao + "apuracao/salvarconfig",
				 data    : { CalcVlrSuperior : CalcVlrSuperior },
				 success: function(result) {

				 },
				 error: function(data) {
					 fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
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
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		return;
	}
}