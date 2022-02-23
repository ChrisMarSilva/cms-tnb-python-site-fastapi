
$(document).ready(function() {

	//$(this).attr("title", "Empresa - " + NOME_PROJETO);
	$("#MnPrincEmpresa").addClass("active open");	
	
	fLimparAreaAlertaPrinc();
	fLimparAreaAlertaModalCad();
	
});

function iniciarAnimacaoPesquisar() {
	$("#iRefresh").addClass("fa-spin");
	$("#btnEmprPesquisar").addClass("disabled");
	$("#btnEmprLimpar").addClass("disabled");
}

function finalizarAnimacaoPesquisa() {
	$("#iRefresh").removeClass("fa-spin");
	$("#btnEmprPesquisar").removeClass("disabled");
	$("#btnEmprLimpar").removeClass("disabled");
}

function fLimparGrid( urlPadrao ){	
	
	$("#selFiltroSetor").val("");
	$("#selFiltroSubSetor").val("");
	$("#selFiltroSegmento").val("");
	$("#selFiltroAtivo").val("");
	$("#selFiltroTipo").val("");

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
				{ bSortable: true, sWidth: "10px", targets:  0 }, // 1-Ativo
				{ bSortable: true, sWidth: "20px", targets:  1 }, // 2-Nome
				{ bSortable: true, sWidth: "40px", targets:  2 }, // 3-Empresa
				{ bSortable: true, sWidth: "40px", targets:  3 }, // 4-Setor
				{ bSortable: true, sWidth: "40px", targets:  4 }, // 5-Sub-Setor
				{ bSortable: true, sWidth: "40px", targets:  5 }, // 5-Segmento
				{ visible  : false,                targets:  6 }, // 6-Situacao
				{ visible  : false,                targets:  7 }, // 7-Id 
				{ bSortable: true, sWidth: "20px", targets:  8 }  // 8-Acao
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
				{ bSortable: true, sWidth: "10px", targets:  0 }, // 1-Ativo
				{ bSortable: true, sWidth: "20px", targets:  1 }, // 2-Nome
				{ bSortable: true, sWidth: "40px", targets:  2 }, // 3-Empresa
				{ bSortable: true, sWidth: "40px", targets:  3 }, // 4-Setor
				{ bSortable: true, sWidth: "40px", targets:  4 }, // 5-Sub-Setor
				{ bSortable: true, sWidth: "40px", targets:  5 }, // 5-Segmento
				{ visible  : false,                targets:  6 }, // 6-Situacao
				{ visible  : false,                targets:  7 }, // 7-Id 
				{ bSortable: true, sWidth: "20px", targets:  8,   // 8-Acao
					render: function ( data, type, row ) {
						var btnEdt = "";
						if ( type == "display") {
							IdEmpresa = row[7]; // 7-Id 
							btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar ' + IdEmpresa + '" href="javascript:void(0);" onclick="fAbrirModalDetalheEmpr( \''+urlPadrao+'\', \''+IdEmpresa+'\' );">';
							btnEdt += '   <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> ';
							btnEdt += '</a>';
						}
						return btnEdt;
					} 
				} //  9-Acao
          ],
          createdRow : function(row,data,dataIndex) {
            $('td', row).addClass('text-center');
          }, //createdRow
          initComplete: function( settings, json ) {
			finalizarAnimacaoPesquisa();
          },
		  bFilter: true,
		  bInfo: true,
		  bLengthChange: false,
		  searchable: true,
		  orderable: true,
		  bOrdering: true,
		  bSortable: true,
		  sAutoWidth: false,
		  bPaginate: false,
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
		
		fLimparAreaAlertaPrinc();
		
		$('#Grid').dataTable().fnClearTable();
		$("#Grid").dataTable({ bDestroy: true }).fnDestroy();		
		
		finalizarAnimacaoPesquisa();
		iniciarAnimacaoPesquisar();
  
		var Setor    = $("#selFiltroSetor").val().trim();
		var SubSetor = $("#selFiltroSubSetor").val().trim();
		var Segmento = $("#selFiltroSegmento").val().trim();
		var CodAtivo = $("#selFiltroAtivo").val().trim();
		var Tipo     = $("#selFiltroTipo").val().trim();
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "empresa/grid",
			data    : { Setor: Setor, SubSetor: SubSetor, Segmento: Segmento, CodAtivo: CodAtivo, Tipo: Tipo },
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
		  if ( e.description != undefined ){
			fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		  }
    }
}

function fAbrirModalDetalheEmpr( urlPadrao, IdEmpresa ) {
    try {

       if ( IdEmpresa == "" ){
		   fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Empresa não informado!');
          return;
        }
		
		fLimparAreaAlertaModalCad();

		$("#txtCadEmprId").val( "" );
		$("#txtCadEmprSetor").val( "" );
		$("#txtCadEmprSubSetor").val( "" );
		$("#txtCadEmprSegmento").val( "" );
		$("#txtCadEmprNome").val( "" );
		$("#txtCadEmprRazao").val( "" );
		$("#txtCadEmprCNPJ").val( "" );
		$("#txtCadEmprAtividade").val( "" );
		$("#txtCadEmprCodCVM").val( "" );
		$("#txtCadEmprSitCVM").val( "" );
		$("#txtCadEmprSituacao").val( "" );

         $.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "empresa/carregar",
            data    : { IdEmpresa : IdEmpresa },
            success: function (result) {
			
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var Empr      = result.data.Dados;
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
				} else if (resultado == "OK") {
					
				   if ( Empr.Id ) { 
				   
						$("#txtCadEmprId").val( Empr.Id );
						$("#txtCadEmprSetor").val( Empr.SetorId );
						$("#txtCadEmprSubSetor").val( Empr.SubSetorId );
						$("#txtCadEmprSegmento").val( Empr.SegmentoId );
						$("#txtCadEmprNome").val( Empr.Nome );
						$("#txtCadEmprRazao").val( Empr.RazaoSocial );
						$("#txtCadEmprCNPJ").val( Empr.CNPJ );
						$("#txtCadEmprAtividade").val( Empr.Atividade );
						$("#txtCadEmprCodCVM").val( Empr.CodCVM );
						$("#txtCadEmprSitCVM").val( Empr.SitCVM );
						$("#txtCadEmprSituacao").val( Empr.Situacao );
						
						fDefinirPadraoSelect('txtCadEmprSetor');
						fDefinirPadraoSelect('txtCadEmprSubSetor');
						fDefinirPadraoSelect('txtCadEmprSegmento');
						
						//$("#PopModalDetalheEmpresa").modal("show");
						//$('#PopModalDetalheEmpresa').modal({backdrop: 'static', keyboard: false});
						$('#PopModalDetalheEmpresa').modal({backdrop: 'static'});

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

function fValidarDados() {	
	try {
		
		fLimparAreaAlertaModalCad();
		
		var EmprId        = $("#txtCadEmprId").val();
		var EmprSetor     = $("#txtCadEmprSetor").val();
		var EmprSubSetor  = $("#txtCadEmprSubSetor").val();
		var EmprSegmento  = $("#txtCadEmprSegmento").val();
		var EmprNome      = $("#txtCadEmprNome").val();
		var EmprRazao     = $("#txtCadEmprRazao").val();
		var EmprCNPJ      = $("#txtCadEmprCNPJ").val();
		var EmprAtividade = $("#txtCadEmprAtividade").val();
		var EmprCodCVM    = $("#txtCadEmprCodCVM").val();
		var EmprSitCVM    = $("#txtCadEmprSitCVM").val();		
		var EmprSituacao  = $("#txtCadEmprSituacao").val();
		
		var ListaErros = "";
		if( EmprId == "" )
			ListaErros = ListaErros + " - Id<br/>";
		if( EmprNome == "" )
			ListaErros = ListaErros + " - Nome<br/>";
		if( EmprRazao == "" )
			ListaErros = ListaErros + " - Razao<br/>";
		if( EmprCNPJ == "" )
			ListaErros = ListaErros + " - CNPJ<br/>";
		if( EmprSituacao == "" )
			ListaErros = ListaErros + " - Situacao<br/>";
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

function fSalvarDados( urlPadrao ){
	try {
		
		if ( !fValidarDados() )
			return false;

		iniciarAnimacaoSalvar();
		
		var EmprId        = $("#txtCadEmprId").val();
		var EmprSetor     = $("#txtCadEmprSetor").val();
		var EmprSubSetor  = $("#txtCadEmprSubSetor").val();
		var EmprSegmento  = $("#txtCadEmprSegmento").val();
		var EmprNome      = $("#txtCadEmprNome").val();
		var EmprRazao     = $("#txtCadEmprRazao").val();
		var EmprCNPJ      = $("#txtCadEmprCNPJ").val();
		var EmprAtividade = $("#txtCadEmprAtividade").val();
		var EmprCodCVM    = $("#txtCadEmprCodCVM").val();
		var EmprSitCVM    = $("#txtCadEmprSitCVM").val();		
		var EmprSituacao  = $("#txtCadEmprSituacao").val();	
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "empresa/salvar",
			data    : {
				EmprId        : EmprId,
				EmprSetor     : EmprSetor,
				EmprSubSetor  : EmprSubSetor,
				EmprSegmento  : EmprSegmento,
				EmprNome      : EmprNome,
				EmprRazao     : EmprRazao,
				EmprCNPJ      : EmprCNPJ,
				EmprAtividade : EmprAtividade,
				EmprCodCVM    : EmprCodCVM,
				EmprSitCVM    : EmprSitCVM,
				EmprSituacao  : EmprSituacao
			},
			success: function(result) {  
			
				finalizarAnimacaoSalvar();
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				
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
					$("#PopModalDetalheEmpresa").modal("hide");	
					fCarregarGrid( urlPadrao );	
					buscar_todos_nomes_empresas_acoes(urlPadrao, 'txtCadInclAtvEmpresa', false, false, true);
					fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
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


function fLimparAreaAlertaModalCadEmpr(){
	fLimparAreaAlerta("AreaAlertaModalCadEmpr"); 
}

function fCriarAlertaModalCadEmpr(Tipo, Mensagem){
	fCriarAlerta("AreaAlertaModalCadEmpr",Tipo, Mensagem);
}

function fAbrirModalIncEmpresa( urlPadrao ) {
    try {
		$("#txtCadInclEmprSetor").val("");
		$("#txtCadInclEmprSubSetor").val("");
		$("#txtCadInclEmprSegmento").val("");
		$("#txtCadInclEmprNome").val("");
		$("#txtCadInclEmprRazao").val("");
		$("#txtCadInclEmprCNPJ").val("");
		$("#txtCadInclEmprAtividade").val("");
		$("#txtCadInclEmprCodCVM").val("");
		$("#txtCadInclEmprSitCVM").val("");
		$("#txtCadInclEmprSituacao").val("A");
		$('#PopModalIncluirEmpresa').modal({backdrop: 'static'});
    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fValidarDadosEmpresa() {	
	try {
		
		fLimparAreaAlertaModalCadEmpr();
		
		var EmprSetor     = $("#txtCadInclEmprSetor").val();
		var EmprSubSetor  = $("#txtCadInclEmprSubSetor").val();
		var EmprSegmento  = $("#txtCadInclEmprSegmento").val();
		var EmprNome      = $("#txtCadInclEmprNome").val();
		var EmprRazao     = $("#txtCadInclEmprRazao").val();
		var EmprCNPJ      = $("#txtCadInclEmprCNPJ").val();
		var EmprSituacao  = $("#txtCadInclEmprSituacao").val();
		
		var ListaErros = "";
		
		if( EmprSetor == "" )
			ListaErros = ListaErros + " - Setor<br/>";
		if( EmprSubSetor == "" )
			ListaErros = ListaErros + " - Sub-Setor<br/>";
		if( EmprSegmento == "" )
			ListaErros = ListaErros + " - Segmento<br/>";
		if( EmprNome == "" )
			ListaErros = ListaErros + " - Nome<br/>";
		if( EmprRazao == "" )
			ListaErros = ListaErros + " - Razao<br/>";
		if( EmprCNPJ == "" )
			ListaErros = ListaErros + " - CNPJ<br/>";
		if( EmprSituacao == "" )
			ListaErros = ListaErros + " - Situacao<br/>";
		if( ListaErros != "" ){
			fCriarAlertaModalCadEmpr(TP_ALERTA_AVISO, "Os seguintes campos não estão preenchido: <br/>"+ListaErros);
			return false;
		}	
		
		return true;
	
	} catch (e) {
		fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return false;
	} 
}

function fSalvarDadosEmpr( urlPadrao ){
	try {
		
		if ( !fValidarDadosEmpresa() )
			return false;

		iniciarAnimacaoSalvar();
		
		var EmprSetor     = $("#txtCadInclEmprSetor").val();
		var EmprSubSetor  = $("#txtCadInclEmprSubSetor").val();
		var EmprSegmento  = $("#txtCadInclEmprSegmento").val();
		var EmprNome      = $("#txtCadInclEmprNome").val();
		var EmprRazao     = $("#txtCadInclEmprRazao").val();
		var EmprCNPJ      = $("#txtCadInclEmprCNPJ").val();
		var EmprAtividade = $("#txtCadInclEmprAtividade").val();
		var EmprCodCVM    = $("#txtCadInclEmprCodCVM").val();
		var EmprSitCVM    = $("#txtCadInclEmprSitCVM").val();
		var EmprSituacao  = $("#txtCadInclEmprSituacao").val();	
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "empresa/salvarEmpresa",
			data    : {
				EmprSetor     : EmprSetor,
				EmprSubSetor  : EmprSubSetor,
				EmprSegmento  : EmprSegmento,
				EmprNome      : EmprNome,
				EmprRazao     : EmprRazao,
				EmprCNPJ      : EmprCNPJ,
				EmprAtividade : EmprAtividade,
				EmprCodCVM    : EmprCodCVM,
				EmprSitCVM    : EmprSitCVM,
				EmprSituacao  : EmprSituacao
			},
			success: function(result) {  
			
				finalizarAnimacaoSalvar();
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaModalCadEmpr(TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlertaModalCadEmpr(TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					$("#PopModalIncluirEmpresa").modal("hide");	
					fCarregarFiltroEmpresa( urlPadrao );
					fCarregarGrid( urlPadrao );	
					buscar_todos_nomes_empresas_acoes(urlPadrao, 'txtCadInclAtvEmpresa', false, false, true);
					fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
				} else {
					fCriarAlertaModalCadEmpr(TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function(data) {
				finalizarAnimacaoSalvar();
				fCriarAlertaModalCadEmpr(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function fLimparAreaAlertaModalCadAtivo(){
	fLimparAreaAlerta("AreaAlertaModalCadAtv"); 
}

function fCriarAlertaModalCadAtivo(Tipo, Mensagem){
	fCriarAlerta("AreaAlertaModalCadAtv",Tipo, Mensagem);
}

function fAbrirModalIncAtivo( urlPadrao ) {
    try {
		$("#txtCadInclAtvEmpresa").val("");
		$("#txtCadInclAtvCodigo").val("");
		$("#txtCadInclAtvCodIsin").val("");
		$("#txtCadInclAtvTipo").val("");
		$("#txtCadInclAtvSituacao").val("A");		
		$('#PopModalIncluirAtivo').modal({backdrop: 'static'});
    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fValidarDadosAtivo() {	
	try {
		
		fLimparAreaAlertaModalCadAtivo();
		
		var AtvEmpresa  = $("#txtCadInclAtvEmpresa").val();
		var AtvCodigo   = $("#txtCadInclAtvCodigo").val();
		var AtvCodIsin  = $("#txtCadInclAtvCodIsin").val();
		var AtvTipo     = $("#txtCadInclAtvTipo").val();
		var AtvSituacao = $("#txtCadInclAtvSituacao").val();
		
		var ListaErros = "";
		
		if( AtvEmpresa == "" )
			ListaErros = ListaErros + " - Empresa<br/>";
		if( AtvCodigo == "" )
			ListaErros = ListaErros + " - Ativo<br/>";
		if( AtvSituacao == "" )
			ListaErros = ListaErros + " - Situacao<br/>";
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

function fSalvarDadosAtivo( urlPadrao ){
	try {
		
		if ( !fValidarDadosAtivo() )
			return false;

		iniciarAnimacaoSalvar();
		
		var AtvEmpresa  = $("#txtCadInclAtvEmpresa").val();
		var AtvCodigo   = $("#txtCadInclAtvCodigo").val();
		var AtvCodIsin  = $("#txtCadInclAtvCodIsin").val();
		var AtvTipo     = $("#txtCadInclAtvTipo").val();
		var AtvSituacao = $("#txtCadInclAtvSituacao").val();
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "empresa/salvarAtivo",
			data    : {
				AtvEmpresa  : AtvEmpresa,
				AtvCodigo   : AtvCodigo,
				AtvCodIsin  : AtvCodIsin,
				AtvTipo     : AtvTipo,
				AtvSituacao : AtvSituacao
			},
			success: function(result) {  
			
				finalizarAnimacaoSalvar();
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaModalCadAtivo(TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlertaModalCadAtivo(TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					$("#PopModalIncluirAtivo").modal("hide");	
					fCarregarGrid( urlPadrao );	
					fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
				} else {
					fCriarAlertaModalCadAtivo(TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function(data) {
				finalizarAnimacaoSalvar();
				fCriarAlertaModalCadAtivo(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}
