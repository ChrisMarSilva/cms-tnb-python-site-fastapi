
function iniciarAnimacaoPesquisarAnaliseYiedlCost() {	
	$("#iRefreshYiledCost").addClass("fa-spin");
	$("#btnAnaliseYiledCostPesquisar").addClass("disabled");
	//$("#btnYieldCostLimpar").addClass("disabled");
	//$("#txtYieldCostAtivo").attr("readonly", "readonly");
	//$("#txtYieldCostAtivo").attr("disabled","disabled");
	//$("#txtYieldCostAtivo").addClass("disabled");
}

function finalizarAnimacaoPesquisaAnaliseYiedlCost() {
	$("#iRefreshYiledCost").removeClass("fa-spin");
	$("#btnAnaliseYiledCostPesquisar").removeClass("disabled");
	//$("#btnYieldCostLimpar").removeClass("disabled");
	//$("#txtYieldCostAtivo").removeAttr("readonly");
	//$("#txtYieldCostAtivo").removeAttr("disabled");
	//$("#txtYieldCostAtivo").removeClass("disabled");
    //$("#txtYieldCostAtivo").focus();
}

async function fLimparGridAnaliseYiedlCost( urlPadrao ){	

     promise = new Promise( (resolve, reject) => {

		fLimparAreaAlerta("AreaAlertaPrincAnaliseYiledCost");
	
		$("#txtFiltroAnaliseYiledCostAtivo").val( "" );	
		fDefinirPadraoSelect('txtFiltroAnaliseYiledCostAtivo');
	
		$("#txtFiltroAnaliseYiledCostAno").val( "" );	
		fDefinirPadraoSelect('txtFiltroAnaliseYiledCostAno');
	
		fLimparSomenteGridAnaliseYiedlCost( urlPadrao );

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

async function fLimparSomenteGridAnaliseYiedlCost( urlPadrao ){
	try {	

		 promise = new Promise( (resolve, reject) => {
	
			finalizarAnimacaoPesquisaAnaliseYiedlCost();
		
			$("th").addClass('text-center');
			
			$('#GridAnaliseYiledCost').dataTable().fnClearTable();
			$("#GridAnaliseYiledCost").dataTable({ bDestroy: true }).fnDestroy();
			
			$('#GridAnaliseYiledCost').DataTable( {
				oLanguage: fTraduzirGrid(), 
				aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets:  0 }, //  0-Ativo
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets:  1 }, //  1-Ano
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets:  2 }, //  2-Preço Médio
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets:  3 }, //  3-Preço Prov.
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets:  4 }, //  4-Total Prov.
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets:  5 }  //  4-Yield on Cost
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
		fCriarAlerta("AreaAlertaPrincAnaliseYiledCost",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

async function fMontarGridAnaliseYiedlCost( urlPadrao, dataSet ){
	try { 
		
		 promise = new Promise( (resolve, reject) => {

			var data     = new Date();
			var anoAtual = data.getFullYear();
	  
			var CodAtivoAtual  = "";
			var CodAtivoUltimo = "";
			var CorLinha       = "table-info";
	
			$('#GridAnaliseYiledCost').DataTable( {
			  processing: true,
			  serverSide: false,
			  iDisplayLength: 10,
			  oLanguage: fTraduzirGrid(), 
			  data: dataSet,
			  aoColumns: [
				   { bSortable: true, bOrderable: true, sWidth: "50px", targets:  0,   //  1-JAN
					  render: function ( data, type, row ) {
						  if ( type == "display") return '<a class="text-dark font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+row[1]+'\', \'13\' );"> '+row[0]+' </i> </a>';
						  return data;
					  } 				
					}, //  0-Ativo
					{ bSortable: true, bOrderable: true, sWidth: "50px", targets:  1 }, //  1-Ano
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets:  2 }, //  2-Preço Médio
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets:  3 }, //  3-Preço Prov.
					{ bSortable: true, bOrderable: true, sWidth: "50px", targets:  4 }, //  4-Total Prov.
					{ bSortable: true, bOrderable: true, sWidth: "50px", targets:  5 }  //  4-Yield on Cost
			  ],
			  createdRow : function( row, data, dataIndex) {	
			  
				$('td', row).addClass('text-center');
				
				CodAtivoAtual = data[0]; //  0-Ativo
				Ano           = data[1]; //  1-Ano
				
				if ( CodAtivoAtual != CodAtivoUltimo ){
					CodAtivoUltimo = CodAtivoAtual;
					if ( CorLinha == "table-info" )  CorLinha = "" 
					else CorLinha = "table-info";
				}
				
				$(row).addClass( CorLinha ); // $('td', row).addClass( CorLinha );
  
				if ( Ano == anoAtual )  $(row).addClass("font-weight-bold");
				
			  }, //createdRow
			  initComplete: function( settings, json ) {
				  finalizarAnimacaoPesquisaAnaliseYiedlCost();
			  }, //initComplete
				order: [],
				dom: 'frtBpi',
				buttons: [  
					  {
						 extend:    'excelHtml5',
						 text:      '<i class="fa fa-file-excel-o"></i> Excel',
						 className: 'btn btn-outline-default btn-sm',
						 title: NOME_PROJETO + ' - Análise do Yield on Cost',
						 titleAttr: 'Excel',
						 exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ] } 
					  }, 
					  {
						extend: 'csvHtml5',
						charset: 'UTF-8',
						fieldSeparator: ';',
						titleAttr: 'CSV',
						text:      '<i class="fa fa-file-o"></i> CSV',
						className: 'btn btn-outline-default btn-sm',
						title: NOME_PROJETO + ' - Análise do Yield on Cost',
						bom: true,
						exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ] } 
					  },
					  {
						extend: 'pdfHtml5',
						text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						className: 'btn btn-default btn-sm',
						titleAttr: 'PDF',
						title: NOME_PROJETO + ' - Análise do Yield on Cost',
						pageSize: 'A3',
						alignment: 'center',
						exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ] },
						footer: true,
						customize: function (doc) { 
							doc.defaultStyle.fontSize = 12; 
							doc.styles.tableHeader.fontSize = 14; 
						}
					  },
					  {
						extend: 'print',
						text:      '<i class="fa fa-print"></i> Imprimir',
						title: NOME_PROJETO + ' - Análise do Yield on Cost',
						titleAttr: 'Imprimir',
						className: 'btn btn-default btn-sm',
						exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ] }
					  }
				],
				order: [[ 0, "asc" ], [ 1, "asc" ]],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				bSearchable: false,
				bOrderable: true,
				bSortable: true,
				bAutoWidth: false,
				bPaginate: false,
				bOrdering: true
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
		  fLimparSomenteGridAnaliseYiedlCost( urlPadrao );
		  finalizarAnimacaoPesquisaAnaliseYiedlCost();
		if ( e.description != undefined ){
		  fCriarAlerta("AreaAlertaPrincAnaliseYiledCost",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		}
	  }
  }  

async function fCarregarGridAnaliseYiedlCost( urlPadrao ){
	try {   

		 promise = new Promise( (resolve, reject) => {
	
			fLimparAreaAlertaPrinc();
		  
			$('#GridAnaliseYiledCost').dataTable().fnClearTable();
			$("#GridAnaliseYiledCost").dataTable({ bDestroy: true }).fnDestroy();	
			
			finalizarAnimacaoPesquisaAnaliseYiedlCost();
			iniciarAnimacaoPesquisarAnaliseYiedlCost();
			
			var CodAtivo = $("#txtFiltroAnaliseYiledCostAtivo").val();	
			var Ano     = $("#txtFiltroAnaliseYiledCostAno").val();	
  
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url: urlPadrao + "Analise/gridYieldOnCost",
				data: { CodAtivo: CodAtivo, Ano: Ano },
				success: function(result) {
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
	
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						finalizarAnimacaoPesquisaAnaliseYiedlCost();
						fLimparSomenteGridAnaliseYiedlCost( urlPadrao );
						fCriarAlerta("AreaAlertaPrincAnaliseYiledCost",  TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						finalizarAnimacaoPesquisaAnaliseYiedlCost();
						fLimparSomenteGridAnaliseYiedlCost( urlPadrao );( urlPadrao );
						fCriarAlerta("AreaAlertaPrincAnaliseYiledCost",  TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridAnaliseYiedlCost( urlPadrao, lista );
					} else{
						finalizarAnimacaoPesquisaAnaliseYiedlCost();
						fLimparSomenteGridAnaliseYiedlCost( urlPadrao );( urlPadrao );
						fCriarAlerta("AreaAlertaPrincAnaliseYiledCost",  TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					finalizarAnimacaoPesquisaAnaliseYiedlCost();
					fLimparSomenteGridAnaliseYiedlCost( urlPadrao );( urlPadrao );
					fCriarAlerta("AreaAlertaPrincAnaliseYiledCost",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
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
		  finalizarAnimacaoPesquisaAnaliseYiedlCost();
		  fLimparSomenteGridAnaliseYiedlCost( urlPadrao );( urlPadrao );
		if ( e.description != undefined ){
		  fCriarAlerta("AreaAlertaPrincAnaliseYiledCost",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		}
	  }
}
