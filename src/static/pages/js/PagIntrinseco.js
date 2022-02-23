
//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

$(document).ready(function() {
	//$(this).attr("title", "Valor Intrinseco - " + NOME_PROJETO);
	$("#MnPrincIntrinseco").addClass("active open");
	fLimparAreaAlertaPrinc();
});

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function iniciarAnimacaoPesquisar() {
	$("#iRefresh").addClass("fa-spin");
	$("#btnIntrPesquisar").addClass("disabled");
	$("#btnIntrLimpar").addClass("disabled");
}

function finalizarAnimacaoPesquisa() {
	$("#iRefresh").removeClass("fa-spin");
	$("#btnIntrPesquisar").removeClass("disabled");
	$("#btnIntrLimpar").removeClass("disabled");
}

function fLimparGrid( urlPadrao ){	

	$("#selFiltroSetor").val("");
	$("#selFiltroSubSetor").val("");
	$("#selFiltroSegmento").val("");
	$("#selFiltroAtivo").val("");
	//$("#selFiltroTipo").val("");
	//$('#txtFiltroPerc').val( "20,00" );
	$('#txtFiltroPerc').val( "0,00" );
		
	$("#iRefresh").removeClass("fa-spin");
	
	fLimparSomenteGrid( urlPadrao );	
}

function fLimparSomenteGrid( urlPadrao ){
	try {	

		$("th").addClass('text-center');
		
		$('#Grid').dataTable().fnClearTable();
		$("#Grid").dataTable({ bDestroy: true }).fnDestroy();
		
		$('#Grid').DataTable( {
			oLanguage: fTraduzirGrid(), 
			aoColumns: [
				{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-CodAtivo
				{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 1 }, //  1-NomeAtivo
				{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 2 }, //  2-Preço
				{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 3 }, //  3-Intrinseco
				{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 4 }, //  4-Percentual
				{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 5 }  //  5-Status				
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

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}


function fMontarGrid( urlPadrao, dataSet ){
  try {   
  
       $('#Grid').DataTable( {
          processing: true,
          serverSide: false,
          iDisplayLength: 10,
		  oLanguage: fTraduzirGrid(), 
		  data: dataSet,
          aoColumns: [
				{ bSortable: true, bOrderable: true, sWidth: "50px", targets: 0 }, //  0-CodAtivo
				{ bSortable: true, bOrderable: true, sWidth: "50px", targets: 1 }, //  1-NomeAtivo
				{ bSortable: true, bOrderable: true, sWidth: "50px", targets: 2 ,  //  2-Preço
					render: function ( data, type, row ) { 
						if ( type == "display")
							return "R$ " + row[2]; //  2-Preço
						return data;
					} 				 
				}, //  2-Preço
				{ bSortable: true, bOrderable: true, sWidth: "50px", targets: 3, //  3-Intrinseco
					render: function ( data, type, row ) { 
						if ( type == "display")
							return "R$ " + row[3]; //  3-Intrinseco
						return data;
					} 				 
				}, //  3-Intrinseco
				{ bSortable: true, bOrderable: true, sWidth: "50px", targets: 4, //  4-Percentual 
					render: function ( data, type, row ) { 
						if ( type == "display")
							return row[4]+"%"; //  4-Percentual
						return data;
					} 	
				}, //  4-Percentual
				{ bSortable: true, bOrderable: true, sWidth: "50px", targets: 5 }  //  5-Status	
          ],
          createdRow : function(row,data,dataIndex) {			  
				$('td', row).addClass('text-center');				
				var Status = data[5];//  5-Status					
				if ( Status == "Barato" )
					$('td', row).addClass('text-success');
				if ( Status == "Caro" )
					$('td', row).addClass('text-danger');		 
				
          }, //createdRow
          initComplete: function( settings, json ) {
				finalizarAnimacaoPesquisa();
          }, //initComplete
			order: [],
			bFilter: true,
			bInfo: true,
			bLengthChange: false,
			bSearchable: true,
			bOrderable: true,
			bSortable: true,
			bAutoWidth: false,
			bPaginate: false,
			bOrdering: true
        });
		
		$( document ).ajaxError(function( event, request, settings, thrownError ) {
			finalizarAnimacaoPesquisa();
		});

    } catch (e) {
		fLimparSomenteGrid( urlPadrao );
		finalizarAnimacaoPesquisa();
      if ( e.description != undefined ){
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      }
    }
}

function fCarregarGrid( urlPadrao ){
  try {   
		
		fLimparAreaAlertaPrinc();

        $('#Grid').dataTable().fnClearTable();
        $("#Grid").dataTable({ bDestroy: true }).fnDestroy();
		
		var Setor    = $("#selFiltroSetor").val().trim();
		var SubSetor = $("#selFiltroSubSetor").val().trim();
		var Segmento = $("#selFiltroSegmento").val().trim();
		var CodAtivo = $("#selFiltroAtivo").val().trim();
		var Tipo     = $("#selFiltroTipo").val().trim();
		var Perc     = $("#txtFiltroPerc").val().trim();
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "intrinseco/grid",
            data: { Setor: Setor, SubSetor: SubSetor, Segmento: Segmento, CodAtivo: CodAtivo, Tipo: Tipo, Perc: Perc },
			success: function(result) {
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var lista     = result.data.Lista;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					return;
				}else if (resultado == "OK") {
					fMontarGrid( urlPadrao, lista );
				} else{
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function(data) {
				finalizarAnimacaoPesquisa();
				fLimparSomenteGrid( urlPadrao );( urlPadrao );
				fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return false;
			}
		});		

    } catch (e) {
		fLimparSomenteGrid( urlPadrao );
		finalizarAnimacaoPesquisa();
		if ( e.description != undefined )
			fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------