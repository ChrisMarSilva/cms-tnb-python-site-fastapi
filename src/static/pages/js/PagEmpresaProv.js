
//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

$(document).ready(function() {
	//$(this).attr("title", "Empresa Prov. - " + NOME_PROJETO);
	$("#MnPrincEmpresaProv").addClass("active open");		
	fLimparAreaAlertaPrinc();	
	fLimparAreaAlertaModalCad();
	fLimparAreaAlertaModalExc();	
});

		
//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function iniciarAnimacaoPesquisar() {
	$("#iRefresh").addClass("fa-spin");
	$("#btnEmprProvPesquisar").addClass("disabled");
	$("#btnEmprProvLimpar").addClass("disabled");
}

function finalizarAnimacaoPesquisa() {
	$("#iRefresh").removeClass("fa-spin");
	$("#btnEmprProvPesquisar").removeClass("disabled");
	$("#btnEmprProvLimpar").removeClass("disabled");
}

function fLimparGrid( urlPadrao ){	
	
	$("#txtFiltroEmprProvDataIni").val( fDataPrimeira() );
	$("#txtFiltroEmprProvDataFim").val( ""              ); //fDataPrimeira() 
	$("#txtFiltroEmprProvAtivo").val(   ""              );
	$("#txtFiltroEmprProvTipo").val(    ""              );

	fLimparSomenteGrid( urlPadrao );
	
}

function fLimparSomenteGrid( urlPadrao ){
	try {	
  
		finalizarAnimacaoPesquisa();
		
		$("th").addClass('text-center');

		$('#Grid').dataTable().fnClearTable();
		$("#Grid").dataTable({ bDestroy: true }).fnDestroy();

		$('#Grid').DataTable( {
			oLanguage: fTraduzirGrid(), 
			aoColumns: [
				{ bSortable: true, sWidth: "50px", targets:  0 }, // 0-DataEx
				{ bSortable: true, sWidth: "50px", targets:  1 }, // 1-DataPagto
				{ bSortable: true, sWidth: "50px", targets:  2 }, // 2-CodAtivo
				{ bSortable: true, sWidth: "50px", targets:  3 }, // 3-Tipo
				{ bSortable: true, sWidth: "50px", targets:  4 }, // 4-Preco
				{ visible  : false,                targets:  5 }, // 5-IdEmprProv 
				{ bSortable: true, sWidth: "50px", targets:  6 }  // 6-Acao
			],
			bFilter: true,
			searchable: true,
			orderable: true,
			bAutoWidth: false
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
				{ bSortable: true, sWidth:  "50px", targets: 0, // 0-DataEx
					render: function ( data, type, row ) { 
						if ( type == "display") return colcarFormacataoData(row[0]); // 0-DataEx
						return data;
					} 
				}, // 0-DataEx
				{ bSortable: true, sWidth:  "50px", targets: 1, // 1-DataPagto
					render: function ( data, type, row ) { 
						if ( type == "display") return colcarFormacataoData(row[1]); // 1-DataPagto
						return data;
					} 
				}, // 1-DataPagto
				{ bSortable: true, sWidth: "20px", targets:  2 }, // 2-CodAtivo
				{ bSortable: true, sWidth: "20px", targets:  3 }, // 3-Tipo
				{ bSortable: true, sWidth:  "50px", targets: 4,   // 4-Preco
					render: function ( data, type, row ) {
						if ( type == "display") return "R$ " + row[4].replace('.', ',') ; // 4-Preco
						return data;
					} 
				}, // 4-Preco
				{ visible  : false,                targets:  5 }, // 5-IdEmprProv 
				{ bSortable: true, sWidth: "20px", targets:  6,   // 6-Acao
					render: function ( data, type, row ) {
						var btnEdt = "";
						var btnDel = "";
						if ( type == "display") {	
							IdEmprProv = row[5]; //  5-IdEmprProv	
							btnEdt += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
							btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar" href="javascript:void(0);" onclick="fAbrirModalDetalheEmprProv( \''+urlPadrao+'\', \''+IdEmprProv+'\', \'Alterar\' );">';
							btnEdt += '   <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> ';
							btnEdt += '</a>';							
							btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Excluir" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fChamarPagExclusaoEmprProv( \''+IdEmprProv+'\' );">';
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
          pageLength: 100, 
		  bLengthChange: false,
          bFilter: true,
          searchable: true,
          orderable: true,
          bAutoWidth: false
        });
		
		$( document ).ajaxError(function( event, request, settings, thrownError ) {
			fLimparSomenteGrid( urlPadrao );
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
		

		finalizarAnimacaoPesquisa();
		fLimparAreaAlertaPrinc();
		
		$('#Grid').dataTable().fnClearTable();
		$("#Grid").dataTable({ bDestroy: true }).fnDestroy();		
		
		iniciarAnimacaoPesquisar();
  
		var ProvDtExIni = $("#txtFiltroEmprProvDataIni").val().trim();
		var ProvDtExFim = $("#txtFiltroEmprProvDataFim").val().trim();
		var CodAtivo    = $("#txtFiltroEmprProvAtivo").val().trim();
		var Tipo        = $("#txtFiltroEmprProvTipo").val().trim();
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "empresaProv/grid",
			data    : { ProvDtExIni : tirarFormacataoData( ProvDtExIni ), 
				        ProvDtExFim : tirarFormacataoData( ProvDtExFim ), 
				        CodAtivo    : CodAtivo, 
				        Tipo        : Tipo 
			},
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
			error: function(data) {
				finalizarAnimacaoPesquisa();
				fLimparSomenteGrid( urlPadrao );
				fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return false;
			}
		});		
		
    } catch (e) {
		finalizarAnimacaoPesquisa();
		fLimparSomenteGrid( urlPadrao );
		  if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}


//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fLimparDadosModalEmprProv( ) {

	fLimparAreaAlertaModalCad();
	
	$("#txtCadEmprProvId").val(      ""           );
	$("#txtCadEmprProvAtivo").val(   ""           );
	$("#txtCadEmprProvTipo").val(    ""           );
	$("#txtCadEmprProvCateg").val(   ""           );
	$("#txtCadEmprProvDtAprov").val( fDataAtual() );
	$("#txtCadEmprProvDtCom").val(   ""           );
	$("#txtCadEmprProvDtEx").val(    fDataAtual() );
	$("#txtCadEmprProvDtPagto").val( "" );
	$("#txtCadEmprProvPreco").val(   "0,00"       );
	
	fDefinirPadraoSelect('txtCadEmprProvAtivo');

}


function fAbrirModalDetalheEmprProv( urlPadrao, IdEmprProv, TipoModal ) {
    try {

    	fLimparDadosModalEmprProv();

    	$("#PopModalDetalheEmprProvTit").html("");
    	$("#PopModalDetalheEmprProvTit").html(" - "+TipoModal);
	
		// $("#txtCadEmprProvDtEx").removeAttr("readonly");
		// $("#txtCadEmprProvDtPagto").removeAttr("readonly");
		// $("#txtCadEmprProvAtivo").removeAttr("readonly");
		// $("#txtCadEmprProvAtivo").removeClass("disabled");
		// $("#txtCadEmprProvAtivo").removeAttr("disabled");	
		// $("#txtCadEmprProvTipo").removeAttr("readonly");	
		// $("#txtCadEmprProvTipo").attr("required", "required");	
		// $("#txtCadAlugVlrIR").removeAttr("readonly");	
		// $("#txtCadEmprProvPreco").removeAttr("readonly");	

		$("#BtnModalDetalheEmprProvSalvar").show();
		if ( TipoModal == "Visualizar" ) $("#BtnModalDetalheEmprProvSalvar").hide();
					
		if ( TipoModal == "Novo" ) $('#PopModalDetalheEmprProv').modal({backdrop: 'static'});

		if ( TipoModal == "Alterar" || TipoModal == "Visualizar" )
	        fCarregarDadosModalDetalheEmprProv( urlPadrao, IdEmprProv, TipoModal );

		$("#txtCadEmprProvAtivo").focus();


    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}


//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------


function fCarregarDadosModalDetalheEmprProv( urlPadrao, IdEmprProv, TipoModal ) {
    try {

		
       if ( IdEmprProv == "" ){
		   fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Empresa Provento não informado!');
          return;
		}
		
         $.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "empresaProv/carregar",
            data    : { IdEmprProv : IdEmprProv },
            success: function (result) {
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var EmprProv  = result.data.Dados;
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
				} else if (resultado == "OK") {
					
				   if ( EmprProv.Id ) { 
				   
						$("#txtCadEmprProvId").val(      EmprProv.Id       );
						$("#txtCadEmprProvAtivo").val(   EmprProv.CodAtivo );
						$("#txtCadEmprProvTipo").val(    EmprProv.Tipo     );
						$("#txtCadEmprProvCateg").val(   EmprProv.Categ    );
						$("#txtCadEmprProvDtAprov").val( EmprProv.DtAprov  );
						$("#txtCadEmprProvDtCom").val(   EmprProv.DtCom    );
						$("#txtCadEmprProvDtEx").val(    EmprProv.DtEx     );
						$("#txtCadEmprProvDtPagto").val( EmprProv.DtPagto  );
						$("#txtCadEmprProvPreco").val(   EmprProv.Preco.replace('.', ',')    );

						fDefinirPadraoSelect('txtCadEmprProvAtivo');
						
						if ( TipoModal == "Visualizar" ){
							// $("#txtCadEmprProvDtEx").attr("readonly", "readonly");
							// $("#txtCadEmprProvDtEx").removeAttr("required");
							// $("#txtCadEmprProvDtPagto").attr("readonly", "readonly");
							// $("#txtCadEmprProvDtPagto").removeAttr("required");
							// $("#txtCadEmprProvAtivo").attr("readonly", "readonly");
							// $("#txtCadEmprProvAtivo").attr("disabled","disabled");
							// $("#txtCadEmprProvAtivo").addClass("disabled");
							// $("#txtCadEmprProvTipo").attr("readonly", "readonly");
							// $("#txtCadEmprProvTipo").attr("disabled","disabled");
							// $("#txtCadEmprProvTipo").addClass("disabled");
							// $("#txtCadEmprProvPreco").attr("readonly", "readonly");
							// $("#txtCadEmprProvPreco").removeAttr("required");
							$("#BtnModalDetalheEmprProvSalvar").attr("disabled","disabled");
							$("#BtnModalDetalheEmprProvSalvar").addClass("disabled");
						}

						$('#PopModalDetalheEmprProv').modal({backdrop: 'static'});

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

		//var Id        = $("#txtCadEmprProvId").val();  
		var CodAtivo  = $("#txtCadEmprProvAtivo").val(); 
		var Tipo      = $("#txtCadEmprProvTipo").val(); 
		//var Categ     = $("#txtCadEmprProvCateg").val(); 
		var DtAprov   = $("#txtCadEmprProvDtAprov").val(); 
		//var DtCom     = $("#txtCadEmprProvDtCom").val(); 
		//var DtEx      = $("#txtCadEmprProvDtEx").val(); 
		//var DtPagto   = $("#txtCadEmprProvDtPagto").val(); 
		var Preco     = $("#txtCadEmprProvPreco").val();
		
		var ListaErros = ""
		if( CodAtivo  == ""                                      ) ListaErros = ListaErros + " - Ativo<br/>";
		if( Tipo      == ""                                      ) ListaErros = ListaErros + " - Tipo<br/>";
		if( DtAprov   == ""                                      ) ListaErros = ListaErros + " - Data Aprov<br/>";
		//if( DataEx    == ""                                      ) ListaErros = ListaErros + " - Data Ex<br/>";
		//if( DataPagto == ""                                      ) ListaErros = ListaErros + " - Data Pagto<br/>";
		if( Preco     == "" || Preco == ",00" || Preco == "0,00" ) ListaErros = ListaErros + " - Preço<br/>";
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


function fSalvarDadosEmprProv( urlPadrao ){
	try {
		
		if ( !fValidarDados() ) return false;

		iniciarAnimacaoSalvar();

		var Id        = $("#txtCadEmprProvId").val();  
		var CodAtivo  = $("#txtCadEmprProvAtivo").val(); 
		var Tipo      = $("#txtCadEmprProvTipo").val(); 
		var Categ     = $("#txtCadEmprProvCateg").val(); 
		var DtAprov   = $("#txtCadEmprProvDtAprov").val(); 
		var DtCom     = $("#txtCadEmprProvDtCom").val(); 
		var DtEx      = $("#txtCadEmprProvDtEx").val(); 
		var DtPagto   = $("#txtCadEmprProvDtPagto").val(); 
		var Preco     = $("#txtCadEmprProvPreco").val();

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "empresaProv/salvar",
			data    : { Id        : Id,
				        CodAtivo  : CodAtivo,
				        Tipo      : Tipo,
				        Categ     : Categ,
				        DtAprov   : tirarFormacataoData( DtAprov ),
				        DtCom     : tirarFormacataoData( DtCom   ),
				        DtEx      : tirarFormacataoData( DtEx    ),
				        DtPagto   : tirarFormacataoData( DtPagto ),
				        Preco     : Preco	   
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
					fLimparDadosModalEmprProv();
					$("#PopModalDetalheEmprProv").modal("hide");					
					fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					fCarregarGrid( urlPadrao );	
				} else {
					fCriarAlertaModalCad(TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function(data) {
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

function fChamarPagExclusaoEmprProv( EmprProvId ) {
    try {


       $("#txtDelEmprProvId").val("");
	   
       if (  EmprProvId  == "" ){
          fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Empresa Provento não informado!'); 
          return;
        }
		
       $("#PopModalDelEmprProv").modal({backdrop: "static"});

       $("#txtDelEmprProvId").val( EmprProvId );

    } catch (e) {
        $("#PopModalDelEmprProv").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fExcluirDadosEmprProv( urlPadrao ) {
    try {

		finalizarAnimacaoExcluir();

		var EmprProvId = $("#txtDelEmprProvId").val();

		if ( EmprProvId == "" ){
			fCriarAlertaModalExc(TP_ALERTA_AVISO, 'Id. Empresa Provento não informado!');
			return;
		}

		iniciarAnimacaoExcluir();
	  
		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "empresaProv/excluir",
			data: {  EmprProvId : EmprProvId },
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
					$("#txtDelEmprProvId").val("");
					$("#PopModalDelEmprProv").modal("hide");
					fCarregarGrid( urlPadrao );
					return true;
				} else {
					fCriarAlertaModalExc(TP_ALERTA_ERRO, mensagem); 
					return false;
				}
				
			},
			error: function (data) {
				$("#PopModalDelEmprProv").modal("hide");
				finalizarAnimacaoExcluir();
				fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
			}
		});

    } catch (e) {
        $("#PopModalDelEmprProv").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------
