
function iniciarAnimacaoPesquisarAnaliseProv() {
	$("#iRefreshProv").addClass("fa-spin");
	$("#btnAnaliseProvPesquisar").addClass("disabled");
	//$("#btnAnRendLimpar").addClass("disabled");
}

function finalizarAnimacaoPesquisaAnaliseProv() {
	$("#iRefreshProv").removeClass("fa-spin");
	$("#btnAnaliseProvPesquisar").removeClass("disabled");
	//$("#btnAnRendLimpar").removeClass("disabled");
}

async function fLimparGridAnaliseProv( urlPadrao ){	

     promise = new Promise( (resolve, reject) => {

		fLimparAreaAlerta("AreaAlertaPrincAnaliseProv");
	
		$("#txtFiltroAnaliseProvDataIni").val(   fDataAnoPrimeira() );
		$("#txtFiltroAnaliseProvDataFim").val(   fDataAnoUltima()   );
		$("#txtFiltroAnaliseProvAtivo").val(     ""                 );	
		$("#txtFiltroAnaliseProvTipo").val(      ""                 );
		$("#txtFiltroAnaliseProvCorretora").val( ""                 );
		
		$("#DivAnaliseProvTotal").text("R$ 0,00");
	
		fLimparSomenteGridAnaliseProv( urlPadrao );

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

async function fLimparSomenteGridAnaliseProv( urlPadrao ){
	try {	

		 promise = new Promise( (resolve, reject) => {
	
			finalizarAnimacaoPesquisaAnaliseProv();
  
			$("th").addClass('text-center');
			
			$('#GridAnaliseProv').dataTable().fnClearTable();
			$("#GridAnaliseProv").dataTable({ bDestroy: true }).fnDestroy();

			
			$('#GridAnaliseProv').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: true, sWidth: "50px", targets:  0 }, //  0-DataPagto
					{ bSortable: true, sWidth: "50px", targets:  1 }, //  1-Ativo
					{ bSortable: true, sWidth: "50px", targets:  2 }, //  2-Tipo
					{ bSortable: true, sWidth: "50px", targets:  3 }, //  3-Descr.
					{ bSortable: true, sWidth: "50px", targets:  4 }, //  4-Quant
					{ bSortable: true, sWidth: "50px", targets:  5 }, //  5-Preco
					{ bSortable: true, sWidth: "50px", targets:  6 }  //  6-Total
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
		fCriarAlerta("AreaAlertaPrincAnaliseProv",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

async function fMontarGridAnaliseProv( urlPadrao, dataSet ){	
	try { 

		 promise = new Promise( (resolve, reject) => {

			var Total = parseFloat(0);
  
			$('#GridAnaliseProv').DataTable( {
			  processing: true,
			  serverSide: false,
			  iDisplayLength: 10,
			  oLanguage: fTraduzirGrid(), 
			  data: dataSet,
			  aoColumns: [
					{ bSortable: true, sWidth: "50px", targets:  0 }, //  0-DataPagto
					{ bSortable: true, sWidth: "50px", targets:  1 }, //  1-Ativo
					{ bSortable: true, sWidth: "50px", targets:  2 ,  //  2-Tipo
					  render: function ( data, type, row ) { 
						  if ( type == "display") {
							  Tipo   = row[2]; //  2-Tipo
								  if ( Tipo == "DIVIDENDOS"     ) return '<span style="font-size:12px;" class="badge badge-success">'+Tipo+'</span>'
							  else if ( Tipo == "JRS CAP PRÓPRIO") return '<span style="font-size:12px;" class="badge badge-primary">'+Tipo+'</span>'; 
							  else if ( Tipo == "REST CAP DIN"   ) return '<span style="font-size:12px;" class="badge badge-danger">'+Tipo+'</span>'; 
							  else if ( Tipo == "RENDIMENTO"     ) return '<span style="font-size:12px;" class="badge badge-warning">'+Tipo+'</span>'; 
							  else                                 return '<span style="font-size:12px;" class="badge badge-default">'+Tipo+'</span>'; 
						  }
						  return data;
					  }
					}, //  2-Tipo
					{ bSortable: true, sWidth: "50px", targets:  3 }, //  3-Descr.
					{ bSortable: true, sWidth: "50px", targets:  4 }, //  4-Quant
					{ bSortable: true, sWidth: "50px", targets:  5,   //  5-Preco 
						render: function ( data, type, row ) {
							if ( type == "display") return "R$ " + row[5]; //  5-Preco 
							return data;
						} 				
					}, //  5-Preco
					{ bSortable: true, sWidth: "50px", targets:  6,   //  6-Total
						render: function ( data, type, row ) {
							if ( type == "display") return "R$ " + row[6]; //  6-Total
							return data;
						} 				
					}  //  6-Total
			  ],
			  createdRow : function(row,data,dataIndex) {
				$('td', row).addClass('text-center');
				Total += parseFloat(GetValorDecimal(data[6]));  //  6-Total
			  }, //createdRow
			  initComplete: function( settings, json ) {
				  finalizarAnimacaoPesquisaAnaliseProv();
				  $("#DivAnaliseProvTotal").text("R$ " + fMascaraValor(Total) );
			  }, //initComplete
				order: [],		
				dom: 'frtBpi',
				buttons: [  
					  {
						 extend:    'excelHtml5',
						 text:      '<i class="fa fa-file-excel-o"></i> Excel',
						 className: 'btn btn-outline-default btn-sm',
						 title: NOME_PROJETO + ' - Análise de Proventos',
						 titleAttr: 'Excel',
						 exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ] },
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
						title: NOME_PROJETO + ' - Análise de Proventos',
						bom: true,
						exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ] } 
					  },
					  {
						extend: 'pdfHtml5',
						text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						className: 'btn btn-default btn-sm',
						titleAttr: 'PDF',
						title: NOME_PROJETO + ' - Análise de Proventos', 
						pageSize: 'A3',
						alignment: 'center',
						exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ] },
						footer: true,
						customize: function (doc) { 
							doc.defaultStyle.fontSize = 12; 
							doc.styles.tableHeader.fontSize = 14; 
						}
					  },
					  {
						extend: 'print',
						text:      '<i class="fa fa-print"></i> Imprimir',
						title: NOME_PROJETO + ' - Análise de Proventos',
						titleAttr: 'Imprimir',
						className: 'btn btn-default btn-sm',
						exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ] }
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
		  fLimparSomenteGridAnaliseProv( urlPadrao );
		  finalizarAnimacaoPesquisaAnaliseProv();
		if ( e.description != undefined ){
		  fCriarAlerta("AreaAlertaPrincAnaliseProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		}
	  }
}  
  
async function fCarregarGridAnaliseProv( urlPadrao ){
	try {   

		 promise = new Promise( (resolve, reject) => {

			fLimparAreaAlerta("AreaAlertaPrincAnaliseProv");
  
			$('#GridAnaliseProv').dataTable().fnClearTable();
			$("#GridAnaliseProv").dataTable({ bDestroy: true }).fnDestroy();	
			
			finalizarAnimacaoPesquisaAnaliseProv();
			iniciarAnimacaoPesquisarAnaliseProv();
			
			$("#DivAnaliseProvTotal").text("R$ 0,00");
			
			var CodAtivo  = $("#txtFiltroAnaliseProvAtivo").val().trim();
			var TipoRend = $("#txtFiltroAnaliseProvTipo").val().trim();
			var DataIni   = $("#txtFiltroAnaliseProvDataIni").val().trim();
			var DataFim   = $("#txtFiltroAnaliseProvDataFim").val().trim();
			var Corretora = $("#txtFiltroAnaliseProvCorretora").val().trim();
			
			DataIni = tirarFormacataoData(DataIni);
			DataFim = tirarFormacataoData(DataFim);
			
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url: urlPadrao + "Analise/gridProv",
				data: {
					CodAtivo  : CodAtivo, 
					TipoRend  : TipoRend,
					Corretora : Corretora,
					DataIni   : DataIni, 
					DataFim   : DataFim
				},
				success: function(result) {
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
	
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fLimparSomenteGridAnaliseProv( urlPadrao );
						fCriarAlerta("AreaAlertaPrincAnaliseProv", TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						fLimparSomenteGridAnaliseProv( urlPadrao );
						fCriarAlerta("AreaAlertaPrincAnaliseProv", TP_ALERTA_AVISO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridAnaliseProv( urlPadrao, lista );
					} else{
						fLimparSomenteGridAnaliseProv( urlPadrao );
						fCriarAlerta("AreaAlertaPrincAnaliseProv", TP_ALERTA_AVISO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					fLimparSomenteGridAnaliseProv( urlPadrao );
					fCriarAlerta("AreaAlertaPrincAnaliseProv", TP_ALERTA_AVISO, MSG_ALERTA_ERRO); 
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
		fLimparSomenteGridAnaliseProv( urlPadrao );
		if ( e.description != undefined ){
		  fCriarAlerta("AreaAlertaPrincAnaliseProv", TP_ALERTA_AVISO, MSG_ALERTA_ERRO); 
		}
	  }
  }
  