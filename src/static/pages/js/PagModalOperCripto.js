
function fLimparDadosModalOperCripto( urlPadrao = '', TipoOper = '' ){
	$("#txtDetOperCriptoId").val("");
	$("#txtDetOperCriptoCod").val("");
	$("#txtDetOperCriptoTipo").val("");
	$("#txtDetOperCriptoData").val( fDataAtual() );
	$("#selDetOperCritpoAtivo").val("");
	fDefinirPadraoSelect('selDetOperCritpoAtivo');
	$("#txtDetOperCriptoQuant").val("0,00");
	$("#txtDetOperCriptoPreco").val("0,00");
	$("#selDetOperCriptoCorretora").val("");
	$('#selDetOperCriptoCorretora')[0].selectedIndex = 0; // Primeira Corretora
	fDefinirPadraoSelect('selDetOperCriptoCorretora');
	$("#txtDetOperCriptoTaxas").val("0,00");
	$("#txtDetOperCriptoTotal").val("0,00");
	$("#BtnDetOperCriptoQuantAtual").hide();
	if ( TipoOper == "V" ) $("#BtnDetOperCriptoQuantAtual").show();
	fCalcularOperacaoCripto();
}

function fMudarOperCriptoTipo(urlPadrao = '', TipoOper = '', CodAtivo = '') {
    fLimparDadosModalOperCripto( urlPadrao, TipoOper );
    $("#PopModalDetalheOperCriptoTit").html("");
    if ( TipoOper == "C" ) $("#PopModalDetalheOperCriptoTit").html("Compra");
    if ( TipoOper == "V" ) $("#PopModalDetalheOperCriptoTit").html("Venda");
    $("#txtDetOperCriptoTipo").val(TipoOper);
    if ( TipoOper == "C" ) $('#TabOperCripto a[href="#AbaOperCriptoCompra"]').tab('show');
    if ( TipoOper == "V" ) $('#TabOperCripto a[href="#AbaOperCriptoVenda"]').tab('show');
    fCalcularOperacaoCripto();
    fCarregarModalOperCriptoCodigoAtivos( urlPadrao, TipoOper, CodAtivo );
}

function fAbrirModalDetalheOperCripto( urlPadrao, IdOper, TipoModal, TipoOper, CodAtivo, Quant, Preco, Data ) {
    try {

		if ( TipoOper == "" ){
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, "Tipo Inválido.");
			$("#PopModalDetalheOperCripto").modal("hide");
			return false;
		}

    	// fLimparDadosModalOperCripto( urlPadrao, TipoOper );
    	fMudarOperCriptoTipo( urlPadrao, TipoOper, CodAtivo );

		if ( TipoModal == "Novo" ){
	    	$('#PopModalDetalheOperCripto').modal({backdrop: 'static'});
			// fCarregarModalOperCriptoCodigoAtivos( urlPadrao, TipoOper, CodAtivo );
			$("#selDetOperCritpoAtivo").val( CodAtivo );
			fDefinirPadraoSelect('selDetOperCritpoAtivo');
			if ( Data && Data != "" ) $("#txtDetOperCriptoData").val( Data );
			$("#txtDetOperCriptoQuant").val( Quant );
			$("#txtDetOperCriptoPreco").val( Preco );
			fCalcularOperacaoCripto();
		}

		if ( TipoModal == "Alterar" )
	        fCarregarDadosModalDetalheOperCripto( urlPadrao, IdOper, CodAtivo, TipoModal );

    } catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

function fCarregarDadosModalDetalheOperCripto( urlPadrao, IdOper, CodAtivo, TipoModal ) {
    try {

		if ( IdOper == "" ){
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, 'Id. Oper. não informado!');
			return;
		}

		if ( CodAtivo == "" ){
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, 'Cód. Ativo não informado!');
			return;
		}

         $.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "operacoes/carregar",
            data    : { IdOper: IdOper, CodAtivo: CodAtivo },
            success: function (result) {

				var resultado = result.data.Resultado;
				var mensagem  = result.data.Mensagem;
				var Oper      = result.data.Dados;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, mensagem);
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem);
				} else if (resultado == "OK") {

				   if ( Oper.IdOper ) {

						// fCarregarModalOperCriptoCodigoAtivos( urlPadrao, Oper.Tipo, Oper.CodAtivo );

						$("#txtDetOperCriptoId").val( Oper.IdOper );
						$("#txtDetOperCriptoTipo").val( Oper.Tipo );
						$("#txtDetOperCriptoData").val( Oper.Data );
						$("#selDetOperCritpoAtivo").val( Oper.CodAtivo );
						$("#txtDetOperCriptoQuant").val( Oper.Quant );
						$("#txtDetOperCriptoPreco").val( Oper.Preco );
						$("#selDetOperCriptoCorretora").val( Oper.Corretora );
						$("#txtDetOperCriptoTaxas").val( Oper.TxCorret );

						fCalcularOperacaoCripto();
						fDefinirPadraoSelect('selDetOperCritpoAtivo');
						fDefinirPadraoSelect('selDetOperCriptoCorretora');

						$('#PopModalDetalheOperCripto').modal({backdrop: 'static'});

					} else {
						fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem);
					}

				} else {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem);
				}

            },
            error: function (data) {
               fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
            }
        });

    } catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

function fCalcularOperacaoCripto() {
	try {

		var Tipo     = "";
		var Quant    = 0.0;
		var Preco    = 0.0;
		var TotPreco = 0.0;
		var Taxas    = 0.0;
		var Total    = 0.0;


		if ( $('#txtDetOperCriptoTipo').length   ) Tipo  = $("#txtDetOperCriptoTipo").val();
		if ( $('#txtDetOperCriptoQuant').length  ) Quant = GetValorDecimalMaior( $('#txtDetOperCriptoQuant').val() );
		if ( $('#txtDetOperCriptoPreco').length  ) Preco = GetValorDecimalMaior( $('#txtDetOperCriptoPreco').val() );
		if ( $('#txtDetOperCriptoTaxas').length  ) Taxas = GetValorDecimalMaior( $('#txtDetOperCriptoTaxas').val() );

		 if ( Preco > 0 && Quant > 0 )
		    TotPreco = parseFloat(Preco) * parseFloat(Quant);

		TotPreco = parseFloat(TotPreco);

		 if ( Tipo  == "C" ) Total = parseFloat( parseFloat(TotPreco) + parseFloat(Taxas) );
		 if ( Tipo  == "V" ) Total = parseFloat( parseFloat(TotPreco) - parseFloat(Taxas) );

		 $("#txtDetOperCriptoTotal").val( fMascaraValor( Total ) );

	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

function fBuscarOperCriptoPrecoAtual( urlPadrao ) {
    try {

		$("#txtDetOperCriptoPreco").val( "0,00" );
		fCalcularOperacaoCripto();

		var CodAtivo = $("#selDetOperCritpoAtivo").val();
		if ( CodAtivo == "" ){
			//fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, 'Ativo não informado!');
			return;
		}

		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "operacoes/precoatual",
			data: { CodAtivo : CodAtivo },
			success: function (result) {
				var resultado = result.data.Resultado;
				var mensagem  = result.data.Mensagem;
				var Oper      = result.data.Dados;
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, mensagem);
					return false;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
					return;
				} else if (resultado == "OK") {
					if ( Oper.PrecoAtual ){
						$("#txtDetOperCriptoPreco").val( Oper.PrecoAtual );
						fCalcularOperacaoCripto();
					}
					return true;
				} else {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
					return false;
				}
			},
			error: function (data) {
				fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			}
		});

    } catch (e) {
		fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

function fBuscarOperCriptoQuantAtual( urlPadrao ) {
    try {

        $("#txtDetOperCriptoQuant").val( "0,00" );
		fCalcularOperacaoCripto();

		var CodAtivo = $("#selDetOperCritpoAtivo").val();
		if ( CodAtivo == "" ){
			fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, 'Ativo não informado!');
			return;
		}

		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "operacoes/quantidade",
			data: { CodAtivo : CodAtivo },
			success: function (result) {

				var resultado = result.data.Resultado;
				var mensagem  = result.data.Mensagem;
				var Oper      = result.data.Dados;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, mensagem);
					return false;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
					return;
				} else if (resultado == "OK") {
					if ( Oper.QuantAtual ){
                        $("#txtDetOperCriptoQuant").val( Oper.QuantAtual );
                        fCalcularOperacaoCripto();
					}
					return true;
				} else {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
					return false;
				}
			},
			error: function (data) {
				fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			}
		});

    } catch (e) {
		fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

function fCarregarModalOperCriptoCodigoAtivos( urlPadrao, TipoOper, CodAtivo ){
	try {

		$('#selDetOperCritpoAtivo').empty();
        $('#selDetOperCritpoAtivo').append('<option value="" selected>Selecione...</option>');

        var UrlLista = "";
        if ( TipoOper == "C" ) UrlLista = "lista_codigo_completo_cripto";
        if ( TipoOper == "V" ) UrlLista = "lista_codigo_user_comprado_cripto";

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "listas/" + UrlLista,
			// data    : {  },
			success: function(result) {

				var resultado = result.data.Resultado;
				var mensagem  = result.data.Mensagem;
				var lista     = result.data.Lista;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, mensagem);
					return false;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem);
					return false;
				} else if (resultado == "OK") {
				    if ( lista.length > 0 ){
                        $('#selDetOperCritpoAtivo').empty();
                        $('#selDetOperCritpoAtivo').append('<option value="" selected>Selecione...</option>');
						$.each(lista, function (index, value) {
							$('#selDetOperCritpoAtivo').append('<option data-subtext=" - '+ value[3] +'" value="'+ value[0] +'">'+value[1]+'</option>');
						});
                    }
                    $("#selDetOperCritpoAtivo").val( CodAtivo );
                    fDefinirPadraoSelect('selDetOperCritpoAtivo');
                    return true;
				} else {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem);
					return false;
				}

			},
			error: function(data) {
				fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
				return false;
			}
		});

	} catch(e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

function fValidarDadosOperCripto() {
	try {

		var Tipo  = $("#txtDetOperCriptoTipo").val();
		var Ativo = $("#selDetOperCritpoAtivo").val();
		var Data  = $("#txtDetOperCriptoData").val();
		var Quant = $("#txtDetOperCriptoQuant").val();
		var Preco = $("#txtDetOperCriptoPreco").val();

		var ListaErros = "";
		if ( Ativo == ""                                    ) ListaErros = ListaErros + " - Código<br/>";
		if ( Data  == ""                                    ) ListaErros = ListaErros + " - Data<br/>";
		if ( Quant == "" || Quant == "0" || Quant == "0,00" ) ListaErros = ListaErros + " - Quant<br/>";
		if ( Preco == "" || Preco == "0" || Preco == "0,00" ) ListaErros = ListaErros + " - Preço <br/>";
		if ( ListaErros != "" ){
			fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, "Os seguintes campos não estão preenchido: <br/>"+ListaErros);
			return false;
		}

		return true;

	} catch (e) {
		fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		return false;
	}
}

function iniciarAnimacaoOperCriptoSalvar() {
    $("#iSalvarOperCripto").removeClass("fa-check");
    $("#iSalvarOperCripto").addClass("fa-spinner");
    $("#iSalvarOperCripto").addClass("fa-pulse");
	$("#BtnModalDetalheOperCriptoSalvar").addClass("disabled");
}

function finalizarAnimacaoOperCriptoSalvar() {
   $("#iSalvarOperCripto").removeClass("fa-spinner");
   $("#iSalvarOperCripto").removeClass("fa-pulse");
   $("#iSalvarOperCripto").addClass("fa-check");
	$("#BtnModalDetalheOperCriptoSalvar").removeClass("disabled");
}

function fSalvarDadosOperCripto( urlPadrao ){
	try {

		if ( !fValidarDadosOperCripto() ) return;

		iniciarAnimacaoOperCriptoSalvar();

		var Id        = $("#txtDetOperCriptoId").val();
		var Tipo      = $("#txtDetOperCriptoTipo").val();
		var Ativo     = $("#selDetOperCritpoAtivo").val();
		var Data      = $("#txtDetOperCriptoData").val();
		var Quant     = $("#txtDetOperCriptoQuant").val();
		var Preco     = $("#txtDetOperCriptoPreco").val();
		var Corretora = $("#selDetOperCriptoCorretora").val();
		var Taxas     = $("#txtDetOperCriptoTaxas").val();

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "operacoes/salvar",
			data    : { Id : Id, Tipo : Tipo, Ativo : Ativo, Data : Data, Quant : Quant, Preco : Preco, Corretora : Corretora, TxCorret : Taxas, },
			success: function(result) {

				finalizarAnimacaoOperCriptoSalvar();

				var resultado = result.data.Resultado;
				var mensagem = result.data.Mensagem;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, mensagem);
					return;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
					return;
				} else if (resultado == "OK") {

					//var URL = $(location).attr('href') || location.href || window.location.href; //http://localhost:8088/portfolio
					var PathName = $(location).attr('pathname') || window.location.pathname; // /portfolio
					var iUlt = PathName.split('/').length - 1;
					if ( PathName.split('/')[iUlt] != '' ) PathName = PathName.split('/')[iUlt];
					PathName = PathName.toLowerCase(); //toUpperCase
	                PathName = PathName.replace('/index.fcgi/', '');
	                PathName = PathName.replace('index.fcgi/', '');
    	            PathName = PathName.replace('/index.fcgi', '');
    	            PathName = PathName.trim();

					if( PathName == "operacoes" || PathName == "/operacoes/" || PathName == "operacoes/" || PathName == "/operacoes" ){
						if( (Id == undefined || Id.toString() == "undefined" || Id.toString() == "") && ( Tipo=='C' || Tipo=='V' ) ){
							fLimparDadosModalOperCripto(urlPadrao, Tipo);
							fMudarOperCriptoTipo( urlPadrao, 'C', '' );
							//$("#txtDetOperCriptoTipo").val( 'C' );
							//$("#txtDetOperCriptoData").val( fDataAtual() );
							//$("#txtDetOperCriptoQuant").val( "0,00" );
							//$("#BtnDetOperCriptoQuantAtual").hide();
							//if ( Tipo == "V" ) $("#BtnDetOperCriptoQuantAtual").show();
							fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
						}
						else{
							$("#PopModalDetalheOperCripto").modal("hide");
							fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
						}
						// buscar_todos_codigos_comprados( urlPadrao, 'selOperAtivo', false, true, false, true, true, true, true);
						fCarregarGrid( urlPadrao );
						return;
					}
					else{

						$("#PopModalDetalheOperCripto").modal("hide");

						if( PathName == "portfolio" || PathName == "/portfolio/" || PathName == "portfolio/" || PathName == "/portfolio" ) {
							fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
							fRecarregarPagina( urlPadrao );
						}

						if( PathName == "ativo" || PathName == "/ativo/" || PathName == "ativ/o" || PathName == "/ativo" )  {
							fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
							fCarregarListaGrupos( urlPadrao, '' );
						}

						if( PathName == "cei" || PathName == "/cei/" || PathName == "cei/" || PathName == "/cei" ){
							fAlterarSitOperCei( urlPadrao, PagCeiLstIdOper, '', PagCeiSitLanc, 0, false );
							fProcurarAlterarLinhaGridOper( urlPadrao, PagCeiLstIdxTr, PagCeiSitLanc );
							return;
						}
					}

				} else {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
					return;
				}

			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				finalizarAnimacaoOperCriptoSalvar();
				fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText //MSG_ALERTA_ERRO
				return;
			}
		});

	} catch (e) {
		finalizarAnimacaoOperCriptoSalvar();
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		return;
	}
}
