
//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

$(document).ready(function() {

	//$(this).attr("title", ":: TnB - Aluguel ::");
	
	$("#MnPrincAluguel").addClass("active open");	
	
	$("#txtCadAlugVlrBruto").bind("keyup change", function(){ fCalcularVlrLiquido(); } );
	$("#txtCadAlugVlrIR").bind("keyup change",    function(){ fCalcularVlrLiquido(); } );	
	
	fLimparAreaAlertaPrinc();	
	fLimparAreaAlertaModalCad();
	fLimparAreaAlertaModalExc();

});

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function iniciarAnimacaoPesquisar() {
	$("#iRefresh").addClass("fa-spin");
	$("#btnAlugPesquisar").addClass("disabled");
	$("#btnAlugLimpar").addClass("disabled");
}

function finalizarAnimacaoPesquisa() {
	$("#iRefresh").removeClass("fa-spin");
	$("#btnAlugPesquisar").removeClass("disabled");
	$("#btnAlugLimpar").removeClass("disabled");
}

function fLimparGrid( urlPadrao ){	
	
	$("#txtFiltroAlugAtivo").val("");
	$("#txtFiltroAlugDtIni").val(""); //fDataAnoPrimeira()
	$("#txtFiltroAlugDtFim").val(""); //fDataAnoUltima()
	
	fDefinirPadraoSelect('txtFiltroAlugAtivo');

	fLimparSomenteGrid( urlPadrao );
	
}

function fLimparSomenteGrid( urlPadrao ){
	try {	

		finalizarAnimacaoPesquisa();
		
		$("th").addClass('text-center');

		$('#Grid').dataTable().fnClearTable();
		$("#Grid").dataTable({ bDestroy: true }).fnDestroy();

		$('#Grid').DataTable( {
		    data: [],
			oLanguage: fTraduzirGrid(), 
			aoColumns: [
				{ bSortable: true, sWidth:  "50px", targets: 0 }, //  0-Data
				{ bSortable: true, sWidth:  "50px", targets: 1 }, //  1-CodAtivo
				{ bSortable: true, sWidth:  "50px", targets: 2 }, //  2-Vlrbruto
				{ bSortable: true, sWidth:  "50px", targets: 3 }, //  3-VlrIR
				{ bSortable: true, sWidth:  "50px", targets: 4 }, //  4-VlrLiquido
				{ visible  : false,                 targets: 5 }, //  5-IdAlug
				{ bSortable: true, sWidth:  "50px", targets: 6 }  //  6-Acao
			],
			order: [],
			bFilter: false,
			bInfo: false,
            iDisplayLength: 100,
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
		  oLanguage: fTraduzirGrid(), 
		  data: dataSet,
          aoColumns: [
				{ bSortable: true, sWidth:  "50px", targets: 0, //  0-Data
					render: function ( data, type, row ) { 
						if ( type == "display")
							return colcarFormacataoData(row[0]);//  0-Data
						return data;
					} 
				}, //  0-Data
				{ bSortable: true, sWidth:  "50px", targets: 1 }, //  1-CodAtivo
				{ bSortable: true, sWidth:  "50px", targets: 2,   //  2-Vlrbruto
					render: function ( data, type, row ) {
						if ( type == "display")
							return "R$ " + row[2]; //  2-Vlrbruto
						return data;
					} 
				}, //  2-Vlrbruto
				{ bSortable: true, sWidth:  "50px", targets: 3,    //  3-VlrIR
					render: function ( data, type, row ) {
						if ( type == "display")
							return "R$ " + row[3];  //  3-VlrIR
						return data;
					} 
				}, //  3-VlrIR
				{ bSortable: true, sWidth:  "50px", targets: 4,   //  4-VlrLiquido
					render: function ( data, type, row ) {
						if ( type == "display")
							return "R$ " + row[4]; //  4-VlrLiquido
						return data;
					} 
				}, //  4-VlrLiquido
				{ visible  : false,                 targets: 5 }, //  5-IdAlug
				{ bSortable: true, sWidth:  "10px", targets: 6,   //  6-Acao
					render: function ( data, type, row ) {
						
						var btnEdt = "";
						var btnDel = "";

						if ( type == "display") {
							
							IdAlug = row[5]; //  5-IdAlug

							btnEdt += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';

							btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar" href="javascript:void(0);" onclick="fAbrirModalDetalheAlug( \''+urlPadrao+'\', \''+IdAlug+'\', \'Alterar\' );">';
							btnEdt += '   <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> ';
							btnEdt += '</a>';
							
							btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Excluir" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fChamarPagExclusaoCorret( \''+IdAlug+'\' );">';
							btnDel += '   <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ';
							btnDel += '</a>';
							
							btnDel += '</div>';
						}
						
						return btnEdt + '&nbsp;' + btnDel;
						
					} 
				} //  6-Acao
          ],
          createdRow : function(row,data,dataIndex) {
            $('td', row).addClass('text-center');
          }, //createdRow
          initComplete: function( settings, json ) {
			finalizarAnimacaoPesquisa();
          },
            order: [[ 0, "asc" ]],
			dom: 'frtBpi',
			buttons: [  
				  {
					 extend:    'excelHtml5',
					 text:      '<i class="fa fa-file-excel-o"></i> Excel',
					 className: 'btn btn-outline-default btn-sm',
					 title: NOME_PROJETO + ' - Aluguel de Ativos',
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
					title: NOME_PROJETO + ' - Aluguel de Ativos',
					bom: true,
					exportOptions: {  columns: [ 0, 1, 2, 3, 4 ] } 
				  },
				  {
					extend: 'pdfHtml5',
					text:      '<i class="fa fa-file-pdf-o"></i> PDF',
					className: 'btn btn-default btn-sm',
					titleAttr: 'PDF',
					title: NOME_PROJETO + ' - Aluguel de Ativos', 
					pageSize: 'A3',
					alignment: 'center',
					exportOptions: {  columns: [ 0, 1, 2, 3, 4 ] },
					footer: true,
					customize: function (doc) { 
						doc.defaultStyle.fontSize = 12; 
						doc.styles.tableHeader.fontSize = 14; 
					}
				  },
				  {
					extend: 'print',
					text:      '<i class="fa fa-print"></i> Imprimir',
					title: NOME_PROJETO + ' - Aluguel de Ativos',
					titleAttr: 'Imprimir',
					className: 'btn btn-default btn-sm',
					exportOptions: {  columns: [ 0, 1, 2, 3, 4 ] }
				  }
			],
            iDisplayLength: 100,
			bLengthChange: false,
			bFilter: false,
			bInfo: false,
			bSearchable: false,
			bPaginate: false,
			bOrderable: true,
			bSortable: true,
			bOrdering: true,
			searchable: true,
			orderable: true,
			bAutoWidth: false
        });
		
		$( document ).ajaxError(function( event, request, settings, thrownError ) {
			fLimparGrid( urlPadrao );
		});

    } catch (e) {
		fLimparGrid( urlPadrao );
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
		
		finalizarAnimacaoPesquisa();
		iniciarAnimacaoPesquisar();

		var CodAtivo  = $("#txtFiltroAlugAtivo").val().trim();
		var DataIni   = $("#txtFiltroAlugDtIni").val().trim();
		var DataFim   = $("#txtFiltroAlugDtFim").val().trim();
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "aluguel/grid",
			data: { CodAtivo: CodAtivo, DataIni: tirarFormacataoData(DataIni), DataFim: tirarFormacataoData(DataFim) },
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
					fLimparSomenteGrid( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					return;
				}else if (resultado == "OK") {
					fMontarGrid( urlPadrao, lista );
				} else{
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				fLimparGrid( urlPadrao );
				fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return false;
			}
		});		
		
    } catch (e) {
		fLimparGrid( urlPadrao );
		  if ( e.description != undefined ){
			fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		  }
    }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fCalcularVlrLiquido() {	
	try {	
		
		$("#txtCadAlugVlrLiquido").val( "0,00" );
		
		var VlrBruto   = GetValorDecimal( $('#txtCadAlugVlrBruto').val() ); 
		var VlrIR      = GetValorDecimal( $('#txtCadAlugVlrIR').val()    );
		var VlrLiquido = parseFloat( parseFloat(VlrBruto) - parseFloat(VlrIR) );

		$("#txtCadAlugVlrLiquido").val( fMascaraValor(VlrLiquido) );

	} catch (e) {
		fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	} 
}

function fLimparDadosModalAluguel( ) {

	fLimparAreaAlertaModalCad();
	
	$("#txtCadAlugId").val(         ""           );
	$("#txtCadAlugData").val(       fDataAtual() );
	$("#txtCadAlugAtivo").val(      ""           );
	$("#txtCadAlugVlrBruto").val(   "0,00"       );
	$("#txtCadAlugVlrIR").val(      "0,00"       );
	$("#txtCadAlugVlrLiquido").val( "0,00"       );
	
	fDefinirPadraoSelect('txtCadAlugAtivo');

}

function fAbrirModalDetalheAlug( urlPadrao, IdAlug, TipoModal ) {
    try {

    	fLimparDadosModalAluguel();

    	$("#fPopModalDetalheAlugTit").html("");
    	$("#fPopModalDetalheAlugTit").html(" - "+TipoModal);
	
		$("#txtCadAlugData").removeAttr("readonly");
		$("#txtCadAlugAtivo").removeAttr("readonly");
		$("#txtCadAlugAtivo").removeClass("disabled");
		$("#txtCadAlugAtivo").removeAttr("disabled");	
		$("#txtCadAlugVlrBruto").removeAttr("readonly");	
		$("#txtCadAlugVlrBruto").attr("required", "required");	
		$("#txtCadAlugVlrIR").removeAttr("readonly");	

		$("#BtnModalDetalheAlugSalvar").show();
		if ( TipoModal == "Visualizar" )
			$("#BtnModalDetalheAlugSalvar").hide();
			
		// buscar_todos_codigos_comprados_acoes( urlPadrao, "txtCadAlugAtivo", false, false, true );
					
		if ( TipoModal == "Novo" ){
	    	$('#PopModalDetalheAluguel').modal({backdrop: 'static'});
		}

		if ( TipoModal == "Alterar" || TipoModal == "Visualizar" )
	        fCarregarDadosModalDetalheAlug( urlPadrao, IdAlug, TipoModal );

		$("#selDivAtivo").focus();

    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------


function fCarregarDadosModalDetalheAlug( urlPadrao, IdAlug, TipoModal ) {
    try {
		
       if ( IdAlug == "" ){
		   fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Aluguel não informado!');
          return;
		}
		
         $.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "aluguel/carregar",
            data    : { IdAlug : IdAlug  },
            success: function (result) {
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var Alug    = result.data.Dados;
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
				} else if (resultado == "OK") {
					
				   if ( Alug.Id ) { 
				   
						$("#txtCadAlugId").val(         Alug.Id         );
						$("#txtCadAlugData").val(       Alug.Data       );
						$("#txtCadAlugAtivo").val(      Alug.CodAtivo   );
						$("#txtCadAlugVlrBruto").val(   Alug.VlrBruto   );
						$("#txtCadAlugVlrIR").val(      Alug.VlrIR      );
						$("#txtCadAlugVlrLiquido").val( Alug.VlrLiquido );
						
						fDefinirPadraoSelect('txtCadAlugAtivo');
						
						if ( TipoModal == "Visualizar" ){
							$("#txtCadAlugData").attr("readonly", "readonly");
							$("#txtCadAlugData").removeAttr("required");
							$("#txtCadAlugAtivo").attr("readonly", "readonly");
							$("#txtCadAlugAtivo").attr("disabled","disabled");
							$("#txtCadAlugAtivo").addClass("disabled");
							$("#txtCadAlugVlrBruto").attr("readonly", "readonly");
							$("#txtCadAlugVlrBruto").removeAttr("required");
							$("#txtCadAlugVlrIR").attr("readonly", "readonly");
							$("#BtnModalDetalheAlugSalvar").attr("disabled","disabled");
							$("#BtnModalDetalheAlugSalvar").addClass("disabled");
						}

						$('#PopModalDetalheAluguel').modal({backdrop: 'static'});

					} else {
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					}
					
				} else {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
				}

            },
            error: function (data) {
               fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
            }
        });        

    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}


//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------


function fValidarDados() {	
	try {
		
		fLimparAreaAlertaModalCad();

		var Data     = $("#txtCadAlugData").val(); 
		var Ativo    = $("#txtCadAlugAtivo").val(); 
		var VlrBruto = $("#txtCadAlugVlrBruto").val();
		
		var ListaErros = "";
		if( Data == ""                                                ) ListaErros = ListaErros + " - Data<br/>";
		if( Ativo == ""                                               ) ListaErros = ListaErros + " - Ativo<br/>";
		if( VlrBruto == "" || VlrBruto == ",00" || VlrBruto == "0,00" ) ListaErros = ListaErros + " - Valor Bruto<br/>";
		if( ListaErros != "" ){
			fCriarAlertaModalCad(TP_ALERTA_AVISO, "Os seguintes campos não estão preenchido: <br/>"+ListaErros);
			return false;
		}		
		
		return true;
	
	} catch (e) {
		fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return false;
	} 
}


function fSalvarDadosAluguel( urlPadrao ){
	try {
		
		if ( !fValidarDados() )
			return false;

		iniciarAnimacaoSalvar();

		var Id         = $("#txtCadAlugId").val();  
		var Data       = $("#txtCadAlugData").val(); 
		var CodAtivo   = $("#txtCadAlugAtivo").val(); 
		var VlrBruto   = $("#txtCadAlugVlrBruto").val(); 
		var VlrIR      = $("#txtCadAlugVlrIR").val(); 
		var VlrLiquido = $("#txtCadAlugVlrLiquido").val(); 

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "aluguel/salvar",
			data    : { Id         : Id,
				        Data       : tirarFormacataoData( Data ),
				        CodAtivo   : CodAtivo,
				        VlrBruto   : VlrBruto,
				        VlrIR      : VlrIR,
				        VlrLiquido : VlrLiquido	   
			},
			success: function(result) {  
			
				finalizarAnimacaoSalvar();
				
				var resultado = result.data.Resultado; 
				var mensagem = result.data.Mensagem; 
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaModalCad(TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlertaModalCad(TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					fLimparDadosModalAluguel();
					$("#PopModalDetalheAluguel").modal("hide");					
					fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					buscar_todos_codigos_alugueis_acoes(  urlPadrao, "txtFiltroAlugAtivo",  false, true, false );
					fCarregarGrid( urlPadrao );	
				} else {
					fCriarAlertaModalCad(TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				finalizarAnimacaoSalvar();
				fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}


//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fChamarPagExclusaoCorret( IdAlug ) {
    try {

       $("#txtDelAlugId").val("");
	   
       if (  IdAlug  == "" ){
          fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Aluguel não informado!'); 
          return;
        }
		
       $("#PopModalDelAluguel").modal({backdrop: "static"});

       $("#txtDelAlugId").val( IdAlug );

    } catch (e) {
        $("#PopModalDelAluguel").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fExcluirDadosAluguel( urlPadrao ) {
    try {

		finalizarAnimacaoExcluir();

		var IdAlug = $("#txtDelAlugId").val();

		if ( IdAlug == "" ){
			fCriarAlertaModalExc(TP_ALERTA_AVISO, 'Id. Aluguel não informado!');
			return;
		}

		iniciarAnimacaoExcluir();
	  
		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "aluguel/excluir",
			data: {  IdAlug : IdAlug },
			success: function (result) {
				
				finalizarAnimacaoExcluir();				
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaModalExc(TP_ALERTA_AVISO, mensagem); 
					return false;
				} else if (resultado == "FALHA") {
					fCriarAlertaModalExc(TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {					
				    fCriarAlertaPrinc(TP_ALERTA_SUCESSO, mensagem); 
					$("#txtDelAlugId").val("");
					$("#PopModalDelAluguel").modal("hide");
					buscar_todos_codigos_alugueis_acoes(  urlPadrao, "txtFiltroAlugAtivo",  false, true, false );
					fCarregarGrid( urlPadrao );
					return true;
				} else {
					fCriarAlertaModalExc(TP_ALERTA_ERRO, mensagem); 
					return false;
				}
				
			},
			error: function (data) {
				$("#PopModalDelAluguel").modal("hide");
				finalizarAnimacaoExcluir();
				fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
			}
		});

    } catch (e) {
        $("#PopModalDelAluguel").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------