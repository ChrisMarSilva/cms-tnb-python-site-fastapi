
//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

$(document).ready(function() {
	//$(this).attr("title", "Valuation Simples - " + NOME_PROJETO);
	$("#MnPrincValiationSimples").addClass("active open");
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
	//$("#selFiltroAtivo").val("");
	$('#txtFiltroSelic').val( "4,25" );
	$('#txtFiltroMargem').val( "20,00" );
		
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
				{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 2 }, //  2-Preço Atual
				{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 3 }, //  3-Preço Teto
				{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 4 }, //  4-Preço Margem
				{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 5 }, //  5-Percentual
				{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 6 }  //  6-Status				
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
				{ bSortable: true, bOrderable: true, sWidth: "50px", targets: 2 ,  //  2-Preço Atual
					render: function ( data, type, row ) { 
						if ( type == "display")
							return "R$ " + row[2]; //  2-Preço Atual
						return data;
					} 				 
				}, //  2-Preço Atual
				{ bSortable: true, bOrderable: true, sWidth: "50px", targets: 3, //  3-Preço Teto 
					render: function ( data, type, row ) { 
						if ( type == "display")
							return "R$ " + row[3]; //  3-Preço Teto
						return data;
					} 				 
				}, //  3-Preço Teto
				{ bSortable: true, bOrderable: true, sWidth: "50px", targets: 4, //  4-Preço Margem
					render: function ( data, type, row ) { 
						if ( type == "display")
							return "R$ " + row[4]; //  4-Preço Margem
						return data;
					} 	
				}, //  4-Preço Margem
				{ bSortable: true, bOrderable: true, sWidth: "50px", targets: 5, //  5-Percentaul
					render: function ( data, type, row ) { 
						if ( type == "display")
							return row[5] + "%"; //   5-Percentaul
						return data;
					} 	
				}, //   5-Percentaul
				{ bSortable: true, bOrderable: true, sWidth: "50px", targets: 6 }  //  6-Status	
          ],
          createdRow : function(row,data,dataIndex) {			  
				$('td', row).addClass('text-center');				
				var Status = data[6];// 6-Status				
				if ( Status == "Comprar" )
					$('td', row).addClass('text-success');
				if ( Status == "NÃO Comprar" )
					$('td', row).addClass('text-secondary');		 
				
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
		
		var Setor     = $("#selFiltroSetor").val();
		var SubSetor  = $("#selFiltroSubSetor").val();
		var Segmento  = $("#selFiltroSegmento").val();
		var CodAtivo  = $("#selFiltroAtivo").val();
		var Tipo      = $("#selFiltroTipo").val();
		var Selic     = $("#txtFiltroSelic").val();
		var MargemSeg = $("#txtFiltroMargem").val();
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "valuation/grid",
            data: { Setor: Setor, SubSetor: SubSetor, Segmento: Segmento, CodAtivo: CodAtivo, Tipo: Tipo, Selic: Selic, MargemSeg: MargemSeg },
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
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				finalizarAnimacaoPesquisa();
				fLimparSomenteGrid( urlPadrao );( urlPadrao );
				fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);   // request.responseText //MSG_ALERTA_ERRO
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