
//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

$(document).ready(function() {
	//$(this).attr("title", "2 -Fundo Imob. Prov. - " + NOME_PROJETO);
	$("#MnPrincFiiFundoImobProv").addClass("active open");		
	fLimparAreaAlertaPrinc();	
	fLimparAreaAlertaModalCad();
	fLimparAreaAlertaModalExc();	
});

		
//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function iniciarAnimacaoPesquisar() {
	$("#iRefresh").addClass("fa-spin");
	$("#btnFundoProvPesquisar").addClass("disabled");
	//$("#btnFundoProvLimpar").addClass("disabled");
}

function finalizarAnimacaoPesquisa() {
	$("#iRefresh").removeClass("fa-spin");
	$("#btnFundoProvPesquisar").removeClass("disabled");
	//$("#btnFundoProvLimpar").removeClass("disabled");
}

function fLimparGrid( urlPadrao ){	
	
	$("#txtFiltroFundoProvDataIni").val( fDataPrimeira() );
	$("#txtFiltroFundoProvDataFim").val( ""              ); //fDataPrimeira() 
	$("#txtFiltroFundoProvFundo").val(   ""              );
	$("#txtFiltroFundoProvTipo").val(    ""              );

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
				{ bSortable: true, sWidth: "50px", targets:  2 }, // 2-CodFundo
				{ bSortable: true, sWidth: "50px", targets:  3 }, // 3-Tipo
				{ bSortable: true, sWidth: "50px", targets:  4 }, // 4-Preco
				{ visible  : false,                targets:  5 }, // 5-IdFundoProv 
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
				{ bSortable: true, sWidth: "20px", targets:  2 }, // 2-CodFundo
				{ bSortable: true, sWidth: "20px", targets:  3 }, // 3-Tipo
				{ bSortable: true, sWidth:  "50px", targets: 4,   // 4-Preco
					render: function ( data, type, row ) {
						if ( type == "display") return "R$ " + row[4].replace('.', ',') ; // 4-Preco
						return data;
					} 
				}, // 4-Preco
				{ visible  : false,                targets:  5 }, // 5-IdFundoProv 
				{ bSortable: true, sWidth: "20px", targets:  6,   // 6-Acao
					render: function ( data, type, row ) {
						var btnEdt = "";
						var btnDel = "";
						if ( type == "display") {	
							IdFundoProv = row[5]; //  5-IdFundoProv	
							btnEdt += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
							btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar" href="javascript:void(0);" onclick="fAbrirModalDetalheFundoProv( \''+urlPadrao+'\', \''+IdFundoProv+'\', \'Alterar\' );">';
							btnEdt += '   <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> ';
							btnEdt += '</a>';							
							btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Excluir" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fChamarPagExclusaoFundoProv( \''+IdFundoProv+'\' );">';
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
  
		var ProvDtExIni = $("#txtFiltroFundoProvDataIni").val();
		var ProvDtExFim = $("#txtFiltroFundoProvDataFim").val();
		var CodFundo    = $("#txtFiltroFundoProvFundo").val();
		var Tipo        = $("#txtFiltroFundoProvTipo").val();
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "FiiFundoImobProv/grid",
			data    : { ProvDtExIni : tirarFormacataoData( ProvDtExIni ), 
				        ProvDtExFim : tirarFormacataoData( ProvDtExFim ), 
				        CodFundo    : CodFundo, 
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

function fLimparDadosModalFundoProv( ) {

	fLimparAreaAlertaModalCad();
	
	$("#txtCadFundoProvId").val(      ""           );
	$("#txtCadFundoProvFundo").val(   ""           );
	$("#txtCadFundoProvTipo").val(    ""           );
	$("#txtCadFundoProvCateg").val(   ""           );
	$("#txtCadFundoProvDtAprov").val( fDataAtual() );
	$("#txtCadFundoProvDtCom").val(   ""           );
	$("#txtCadFundoProvDtEx").val(    fDataAtual() );
	$("#txtCadFundoProvDtPagto").val( ""           );
	$("#txtCadFundoProvPreco").val(   "0,00"       );
	
	fDefinirPadraoSelect('txtCadFundoProvFundo');

}


function fAbrirModalDetalheFundoProv( urlPadrao, IdFundoProv, TipoModal ) {
    try {

    	fLimparDadosModalFundoProv();

    	$("#PopModalDetalheFundoProvTit").html("");
    	$("#PopModalDetalheFundoProvTit").html(" - "+TipoModal);
	
		// $("#txtCadFundoProvDtEx").removeAttr("readonly");
		// $("#txtCadFundoProvDtPagto").removeAttr("readonly");
		// $("#txtCadFundoProvFundo").removeAttr("readonly");
		// $("#txtCadFundoProvFundo").removeClass("disabled");
		// $("#txtCadFundoProvFundo").removeAttr("disabled");	
		// $("#txtCadFundoProvTipo").removeAttr("readonly");	
		// $("#txtCadFundoProvTipo").attr("required", "required");	
		// $("#txtCadAlugVlrIR").removeAttr("readonly");	
		// $("#txtCadFundoProvPreco").removeAttr("readonly");	

		$("#BtnModalDetalheFundoProvSalvar").show();
		if ( TipoModal == "Visualizar" ) $("#BtnModalDetalheFundoProvSalvar").hide();
					
		if ( TipoModal == "Novo" ) $('#PopModalDetalheFundoProv').modal({backdrop: 'static'});

		if ( TipoModal == "Alterar" || TipoModal == "Visualizar" )
	        fCarregarDadosModalDetalheFundoProv( urlPadrao, IdFundoProv, TipoModal );

		$("#txtCadFundoProvFundo").focus();


    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}


//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------


function fCarregarDadosModalDetalheFundoProv( urlPadrao, IdFundoProv, TipoModal ) {
    try {

		
       if ( IdFundoProv == "" ){
		   fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Fundo Provento não informado!');
          return;
		}
		
         $.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "FiiFundoImobProv/carregar",
            data    : { IdFundoProv : IdFundoProv },
            success: function (result) {
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var FundoProv  = result.data.Dados;
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
				} else if (resultado == "OK") {
					
				   if ( FundoProv.Id ) { 
				   
						$("#txtCadFundoProvId").val(      FundoProv.Id       );
						$("#txtCadFundoProvFundo").val(   FundoProv.CodFundo );
						$("#txtCadFundoProvTipo").val(    FundoProv.Tipo     );
						$("#txtCadFundoProvCateg").val(   FundoProv.Categ    );
						$("#txtCadFundoProvDtAprov").val( FundoProv.DtAprov  );
						$("#txtCadFundoProvDtCom").val(   FundoProv.DtCom    );
						$("#txtCadFundoProvDtEx").val(    FundoProv.DtEx     );
						$("#txtCadFundoProvDtPagto").val( FundoProv.DtPagto  );
						$("#txtCadFundoProvPreco").val(   FundoProv.Preco.replace('.', ',')    );

						fDefinirPadraoSelect('txtCadFundoProvFundo');
						
						if ( TipoModal == "Visualizar" ){
							// $("#txtCadFundoProvDtEx").attr("readonly", "readonly");
							// $("#txtCadFundoProvDtEx").removeAttr("required");
							// $("#txtCadFundoProvDtPagto").attr("readonly", "readonly");
							// $("#txtCadFundoProvDtPagto").removeAttr("required");
							// $("#txtCadFundoProvFundo").attr("readonly", "readonly");
							// $("#txtCadFundoProvFundo").attr("disabled","disabled");
							// $("#txtCadFundoProvFundo").addClass("disabled");
							// $("#txtCadFundoProvTipo").attr("readonly", "readonly");
							// $("#txtCadFundoProvTipo").attr("disabled","disabled");
							// $("#txtCadFundoProvTipo").addClass("disabled");
							// $("#txtCadFundoProvPreco").attr("readonly", "readonly");
							// $("#txtCadFundoProvPreco").removeAttr("required");
							$("#BtnModalDetalheFundoProvSalvar").attr("disabled","disabled");
							$("#BtnModalDetalheFundoProvSalvar").addClass("disabled");
						}

						$('#PopModalDetalheFundoProv').modal({backdrop: 'static'});

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

		//var Id        = $("#txtCadFundoProvId").val();  
		var CodFundo  = $("#txtCadFundoProvFundo").val(); 
		var Tipo      = $("#txtCadFundoProvTipo").val(); 
		//var Categ     = $("#txtCadFundoProvCateg").val(); 
		var DtAprov   = $("#txtCadFundoProvDtAprov").val(); 
		//var DtCom     = $("#txtCadFundoProvDtCom").val(); 
		//var DtEx      = $("#txtCadFundoProvDtEx").val(); 
		//var DtPagto   = $("#txtCadFundoProvDtPagto").val(); 
		var Preco     = $("#txtCadFundoProvPreco").val();
		
		var ListaErros = ""
		if( CodFundo  == ""                                      ) ListaErros = ListaErros + " - Fundo<br/>";
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


function fSalvarDadosFundoProv( urlPadrao ){
	try {
		
		if ( !fValidarDados() ) return false;

		iniciarAnimacaoSalvar();

		var Id        = $("#txtCadFundoProvId").val();  
		var CodFundo  = $("#txtCadFundoProvFundo").val(); 
		var Tipo      = $("#txtCadFundoProvTipo").val(); 
		var Categ     = $("#txtCadFundoProvCateg").val(); 
		var DtAprov   = $("#txtCadFundoProvDtAprov").val(); 
		var DtCom     = $("#txtCadFundoProvDtCom").val(); 
		var DtEx      = $("#txtCadFundoProvDtEx").val(); 
		var DtPagto   = $("#txtCadFundoProvDtPagto").val(); 
		var Preco     = $("#txtCadFundoProvPreco").val();

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "FiiFundoImobProv/salvar",
			data    : { Id        : Id,
				        CodFundo  : CodFundo,
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
					fLimparDadosModalFundoProv();
					$("#PopModalDetalheFundoProv").modal("hide");					
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

function fChamarPagExclusaoFundoProv( FundoProvId ) {
    try {


       $("#txtDelFundoProvId").val("");
	   
       if ( FundoProvId  == "" ){
          fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Fundo Provento não informado!'); 
          return;
        }
		
       $("#PopModalDelFundoProv").modal({backdrop: "static"});

       $("#txtDelFundoProvId").val( FundoProvId );

    } catch (e) {
        $("#PopModalDelFundoProv").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fExcluirDadosFundoProv( urlPadrao ) {
    try {

		finalizarAnimacaoExcluir();

		var FundoProvId = $("#txtDelFundoProvId").val();

		if ( FundoProvId == "" ){
			fCriarAlertaModalExc(TP_ALERTA_AVISO, 'Id. Fundo Provento não informado!');
			return;
		}

		iniciarAnimacaoExcluir();
	  
		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "FiiFundoImobProv/excluir",
			data: {  FundoProvId : FundoProvId },
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
					$("#txtDelFundoProvId").val("");
					$("#PopModalDelFundoProv").modal("hide");
					fCarregarGrid( urlPadrao );
					return true;
				} else {
					fCriarAlertaModalExc(TP_ALERTA_ERRO, mensagem); 
					return false;
				}
				
			},
			error: function (data) {
				$("#PopModalDelFundoProv").modal("hide");
				finalizarAnimacaoExcluir();
				fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
			}
		});

    } catch (e) {
        $("#PopModalDelFundoProv").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------
