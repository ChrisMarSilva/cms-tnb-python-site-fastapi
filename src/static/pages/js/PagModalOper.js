
function fCarregarModalCodigoAtivos( urlPadrao, TipoModal, TipoOper, CodAtivo ){
	try {

		$('#selDetOperAtivo').empty();
        $('#selDetOperAtivo').append('<option value="" selected>Selecione...</option>');

        var UrlLista = "";
        if ( TipoOper == "B" || TipoOper == "C" ) UrlLista = "lista_codigo_completo";
        if ( TipoOper == "A" || TipoOper == "V" || TipoOper == "D" || TipoOper == "G" ) UrlLista = "lista_codigo_user_comprado";
		
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

				    if ( lista.length > 0 )
						$.each(lista, function (index, value) {
							$('#selDetOperAtivo').append('<option data-subtext=" - '+ value[4] +'" value="'+ value[0] +'">'+value[1]+'</option>');
						});

                    $("#selDetOperAtivo").val( CodAtivo );

                    fDefinirPadraoSelect('selDetOperAtivo');
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

function fCalcularPrecoTotal() {

}

function fCalcularTaxaLiquid() {
	try {
		
		var Quant    = 0;
		var Preco    = 0;
		var TotPreco = 0;
		var TxLiquid = 0; 
		
		Quant = GetValorInteiro( $('#txtDetOperQuant').val() ); 
		Preco = GetValorDecimal( $('#txtDetOperPreco').val() ); 
		//var TotPreco = GetValorDecimal( $('#txtDetOperTotPreco').val() );
		
		if ( Preco    > 0 && Quant > 0 ) TotPreco = ( Preco * Quant );	
		//if ( TotPreco > 0              ) TxLiquid = fTrucarValor( fCalcularJuros( TotPreco, 0.0275 ) );
		if ( TotPreco > 0              ) TxLiquid = fCalcularJuros( TotPreco, 0.0275 );
		
		$("#txtDetOperTxLiquid").val( fMascaraValor( TxLiquid ) );	
		fCalcularOperacao();
		
	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	} 
}

function fCalcularTaxaEmol() {	
	try {
		
		var Quant    = 0;
		var Preco    = 0;
		var TotPreco = 0;
		var TxEmol   = 0; 
		
		Quant = GetValorInteiro( $('#txtDetOperQuant').val() ); 
		Preco = GetValorDecimal( $('#txtDetOperPreco').val() ); 
		//var TotPreco = GetValorDecimal( $('#txtDetOperTotPreco').val() );
		
		if ( Preco    > 0 && Quant > 0 ) TotPreco = ( Preco * Quant );	
		//if ( TotPreco > 0              ) TxEmol   = fTrucarValor( fCalcularJuros( TotPreco, 0.003125 ) );
		if ( TotPreco > 0              ) TxEmol   = fCalcularJuros( TotPreco, 0.003125 );
		
		$("#txtDetOperTxEmol").val(  fMascaraValor( TxEmol ) );
		fCalcularOperacao();
		
	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	} 
}

function fCalcularTaxaISS() {	
	try {
		
		var TxCorret = 0;
		var TxISS    = 0; 
		
		TxCorret = GetValorDecimal( $('#txtDetOperTxCorret').val() ); 

		if ( TxCorret > 0 ) TxISS = (TxCorret / 100 ) * 9.65;
		
		$("#txtDetOperTxISS").val(  fMascaraValor( TxISS ) );
		fCalcularOperacao();
		
	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	} 
}

function fCalcularTaxaIRRF() {
	try {	
		
		var Quant    = 0;
		var Preco    = 0;
		var TotPreco = 0;
		var TxIRRF   = 0; 
	
		Quant = GetValorInteiro( $('#txtDetOperQuant').val() ); 
		Preco = GetValorDecimal( $('#txtDetOperPreco').val() ); 
		//var TotPreco = GetValorDecimal( $('#txtDetOperTotPreco').val() );
		
		if ( Preco    > 0 && Quant > 0 ) TotPreco = ( Preco * Quant );
		if ( TotPreco > 0              ) TxIRRF   = fTrucarValor( fCalcularJuros( TotPreco, 0.0050 ) );	
		
		$("#txtDetOperTxIRRF").val(  fMascaraValor( TxIRRF ) );
		fCalcularOperacao();
		
	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	} 
}

function fCalcularOperacao() {	
	try {
				
		var Tipo      = "";
		var Quant     = 0;
		var Preco     = 0;
		var TxLiquid  = 0;
		var TxEmol    = 0;
		var TxCorret  = 0;
		var TxISS     = 0;
		var TxIRRF    = 0; 
		var TxOutros  = 0;
		var TotPreco  = 0;
		var TotTaxa   = 0;
		var Total     = 0;
		var CustoAcao = 0;

		if ( $('#txtDetOperTipo').length     ) Tipo      = $("#txtDetOperTipo").val();		
		if ( $('#txtDetOperQuant').length    ) Quant     = GetValorInteiro( $('#txtDetOperQuant').val()    ); 
		if ( $('#txtDetOperPreco').length    ) Preco     = GetValorDecimal( $('#txtDetOperPreco').val()    ); 
		if ( $('#txtDetOperTxLiquid').length ) TxLiquid  = GetValorDecimal( $('#txtDetOperTxLiquid').val() ); 
		if ( $('#txtDetOperTxEmol').length   ) TxEmol    = GetValorDecimal( $('#txtDetOperTxEmol').val()   ); 
		if ( $('#txtDetOperTxCorret').length ) TxCorret  = GetValorDecimal( $('#txtDetOperTxCorret').val() ); 
		if ( $('#txtDetOperTxISS').length    ) TxISS     = GetValorDecimal( $('#txtDetOperTxISS').val()    );
		if ( $('#txtDetOperTxIRRF').length   ) TxIRRF    = GetValorDecimal( $('#txtDetOperTxIRRF').val()   ); 
		if ( $('#txtDetOperTxOutros').length ) TxOutros  = GetValorDecimal( $('#txtDetOperTxOutros').val() );
	
		if ( Preco > 0 && Quant > 0 ) TotPreco = parseFloat( parseFloat(Preco) * parseInt(Quant) );	
		TotTaxa = parseFloat( parseFloat(TxLiquid) + parseFloat(TxEmol) + parseFloat(TxCorret) + parseFloat(TxISS) + parseFloat(TxOutros) + parseFloat(TxIRRF) );
		
		if ( Tipo  == "C"           ) Total     = parseFloat( parseFloat(TotPreco) + parseFloat(TotTaxa) );
		if ( Tipo  == "V"           ) Total     = parseFloat( parseFloat(TotPreco) - parseFloat(TotTaxa) );
		if ( Tipo  == "B"           ) Total     = parseFloat( parseFloat(TotPreco) + parseFloat(TotTaxa) );
		if ( Tipo  == "A"           ) Total     = parseFloat( parseFloat(TotPreco) + parseFloat(TotTaxa) );
		//if ( Preco > 0 && Quant > 0 ) CustoAcao = parseFloat( parseFloat(Total) / parseInt(Quant) ); 
		
		//$("#txtDetOperTotPreco").val(  fMascaraValor( TotPreco  ) );
		//$("#txtDetOperTotTaxa").val(   fMascaraValor( TotTaxa   ) );		
		$("#txtDetOperTotal").val(     fMascaraValor( Total     ) );
		//$("#txtDetOperCustoAcao").val( fMascaraValor( CustoAcao ) );	

	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	} 
}

function fLimparDadosModalOper( urlPadrao = '', TipoOper = '' ){

	fLimparAreaAlerta("AreaAlertaModalCadOper"); 
	
	$("#txtDetOperId").val(        ""     );
	$("#txtDetOperTipo").val(      ""     );
	$("#txtDetOperData").val(      ""     );
	$("#selDetOperAtivo").val(     ""     );
	$("#txtDetOperQuant").val(     "0"    );
	$("#txtDetOperPreco").val(     "0,00" );
	//$("#selDetOperCorretora").val( ""     );
	$('#selDetOperCorretora')[0].selectedIndex = 2; // Primeira Corretora
	$("#txtDetOperTxCorret").val(  "0,00" );
	$("#txtDetOperTxLiquid").val(  "0,00" );
	$("#txtDetOperTxEmol").val(    "0,00" );
	$("#txtDetOperTxISS").val(     "0,00" );
	$("#txtDetOperTxIRRF").val(    "0,00" );
	$("#txtDetOperTxOutros").val(  "0,00" );
	//$("#txtDetOperTotPreco").val(  "0,00" );
	//$("#txtDetOperTotTaxa").val(   "0,00" );
	$("#txtDetOperTotal").val(     "0,00" );
	//$("#txtDetOperCustoAcao").val( "0,00" );
	
	fDefinirPadraoSelect('selDetOperAtivo');
	fDefinirPadraoSelect('selDetOperCorretora');
	
	var IdCorret = $("#selDetOperCorretora").val();
	if ( IdCorret != null && IdCorret != ""  ) fBuscarVlrCorretagem(urlPadrao, TipoOper);

	if ( TipoOper == 'B' ) $("#txtDetOperTipo").val( TipoOper );
	
	$("#BtnDetOperQuantAtual").hide();
	fCalcularOperacao();

}

function fAbrirModalDetalheOper( urlPadrao, IdOper, TipoModal, TipoOper, CodAtivo, Quant, Preco, Data ) {
    try {
		
		if ( TipoOper == "" ){
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, "Tipo Inválido."); 
			$("#PopModalDetalheOper").modal("hide");
			return false;
		}
		
    	fLimparDadosModalOper(urlPadrao, TipoOper);
		
    	$("#txtDetOperTipo").val( TipoOper );	
		
		if ( TipoOper == "A" || TipoOper == "C" || TipoOper == "B" || TipoOper == "V"  ){
			$("#DivDetOperPreco").show();
			$("#DivDetOperCorretora").show();
		}		

		if ( TipoOper == "C" || TipoOper == "V"  ){
			$("#DivDetOperTxCorret").show();
			$("#DivDetOperTxLiquid").show();
			$("#DivDetOperTxEmol").show();
			$("#DivDetOperTxISS").show();
			$("#DivDetOperTxOutros").show();
			$("#DivDetOperTxIRRF").hide();
			if ( TipoOper == "V" ) $("#DivDetOperTxIRRF").show();
		}			
		
		if ( TipoOper == "D" || TipoOper == "G" ){
			$("#DivDetOperPreco").hide();
			$("#DivDetOperCorretora").hide();
		}	
		
		if ( TipoOper == "A" || TipoOper == "B" || TipoOper == "D" || TipoOper == "G" ){
			$("#DivDetOperTxCorret").hide();
			$("#DivDetOperTxLiquid").hide();
			$("#DivDetOperTxEmol").hide();
			$("#DivDetOperTxISS").hide();
			$("#DivDetOperTxOutros").hide();
			$("#DivDetOperTxIRRF").hide();
		}

    	$("#lblDetOperQuant").html("&nbsp;&nbsp;Quant.");
		if ( TipoOper == "D" || TipoOper == "G" ) $("#lblDetOperQuant").html("&nbsp;&nbsp;Fator");
		
    	$("#PopModalDetalheOperTit").html("");

		if ( TipoOper == "C" && TipoModal == "Novo"       ) $("#PopModalDetalheOperTit").html("Nova Compra");
		if ( TipoOper == "C" && TipoModal == "Alterar"    ) $("#PopModalDetalheOperTit").html("Alterar Compra");
		
		if ( TipoOper == "V" && TipoModal == "Novo"       ) $("#PopModalDetalheOperTit").html("Nova Venda");
		if ( TipoOper == "V" && TipoModal == "Alterar"    ) $("#PopModalDetalheOperTit").html("Alterar Venda");
		
		if ( TipoOper == "B" && TipoModal == "Novo"       ) $("#PopModalDetalheOperTit").html("Nova Bonificação");
		if ( TipoOper == "B" && TipoModal == "Alterar"    ) $("#PopModalDetalheOperTit").html("Alterar Bonificação");
		
		if ( TipoOper == "D" && TipoModal == "Novo"       ) $("#PopModalDetalheOperTit").html("Novo Desdobramento");
		if ( TipoOper == "D" && TipoModal == "Alterar"    ) $("#PopModalDetalheOperTit").html("Alterar Desdobramento");
		
		if ( TipoOper == "G" && TipoModal == "Novo"       ) $("#PopModalDetalheOperTit").html("Novo Grupamento");
		if ( TipoOper == "G" && TipoModal == "Alterar"    ) $("#PopModalDetalheOperTit").html("Alterar Grupamento");
		
		if ( TipoOper == "A" && TipoModal == "Novo"       ) $("#PopModalDetalheOperTit").html("Nova Amortização");
		if ( TipoOper == "A" && TipoModal == "Alterar"    ) $("#PopModalDetalheOperTit").html("Alterar Amortização");

		$("#BtnModalDetalheOperSalvar").show();
		if ( TipoModal == "Visualizar" ) $("#BtnModalDetalheOperSalvar").hide();

		$("#DivDetOperTotal").hide();
		if ( TipoOper == "C" || TipoOper == "V" || TipoOper == "A" || TipoOper == "B" ) $("#DivDetOperTotal").show();

		if ( TipoModal == "Novo" ){
	    	$('#PopModalDetalheOper').modal({backdrop: 'static'});
			fCarregarModalCodigoAtivos( urlPadrao, TipoModal, TipoOper, CodAtivo );	
			$("#selDetOperAtivo").val( CodAtivo );
			fDefinirPadraoSelect('selDetOperAtivo');
			$("#txtDetOperData").val( fDataAtual() );
			if ( Data && Data != "" ) $("#txtDetOperData").val( Data );
			$("#txtDetOperQuant").val( GetValorInteiro( Quant ) );	
			if ( TipoOper == "A" || TipoOper == "C" || TipoOper == "V" ) $("#txtDetOperPreco").val( Preco );
			if ( TipoOper == "A" || TipoOper == "V" || TipoOper == "B" ) $("#BtnDetOperQuantAtual").show();
			fCalcularOperacao();
		}

		if ( TipoModal == "Alterar" || TipoModal == "Visualizar" )
	        fCarregarDadosModalDetalheOper( urlPadrao, IdOper, CodAtivo, TipoModal );

		$("#selDivAtivo").focus();
		
    } catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

function fCarregarDadosModalDetalheOper( urlPadrao, IdOper, CodAtivo, TipoModal ) {
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

						fCarregarModalCodigoAtivos( urlPadrao, TipoModal, Oper.Tipo, Oper.CodAtivo );

						$("#txtDetOperId").val(        Oper.IdOper   );
						$("#txtDetOperTipo").val(      Oper.Tipo     );
						$("#txtDetOperData").val(      Oper.Data     );
						$("#selDetOperAtivo").val(     Oper.CodAtivo );
						$("#txtDetOperQuant").val(     Oper.Quant    );
						$("#txtDetOperPreco").val(     Oper.Preco    );
						$("#selDetOperCorretora").val( Oper.Corretora );
						$("#txtDetOperTxCorret").val(  Oper.TxCorret );
						$("#txtDetOperTxLiquid").val(  Oper.TxLiquid );
						$("#txtDetOperTxEmol").val(    Oper.TxEmol   );
						$("#txtDetOperTxISS").val(     Oper.TxISS    );
						$("#txtDetOperTxIRRF").val(    Oper.TxIRRF   );
						$("#txtDetOperTxOutros").val(  Oper.TxOutras );

						fCalcularOperacao();
											
						fDefinirPadraoSelect('selDetOperAtivo');
						fDefinirPadraoSelect('selDetOperCorretora');
						
						$('#PopModalDetalheOper').modal({backdrop: 'static'});

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

function fBuscarVlrCorretagem( urlPadrao = '', TipoOper = '' ) {
    try {
		
		fLimparAreaAlerta("AreaAlertaModalCadOper"); 
		
		$("#txtDetOperTxCorret").val( "0,00" );
		fCalcularOperacao();
		
		var IdCorret = $("#selDetOperCorretora").val();
		if ( IdCorret == "" ){
			//fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, 'Corretora não informada!');
			return;
		}

		if ( TipoOper == "B" ){
           return;
		}

        var TipoOper = $("#txtDetOperTipo").val();
		if ( TipoOper == "B" ){
           return;
		}

		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "corretora/carregar",
			data: { IdCorret : IdCorret },
			success: function (result) {
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var Corret    = result.data.Dados;

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
					if ( Corret.Id ){
						$("#txtDetOperTxCorret").val( Corret.Valor );
						fCalcularOperacao();
					}
					return true;
				} else {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, "Corretagem: " + mensagem); 
					return false;
				}
			},
			error: function (data) {
				fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, "Corretagem: " + MSG_ALERTA_ERRO); 
			}
		});

    } catch (e) {
		fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, "Corretagem: " + MSG_ALERTA_ERRO); 
    }	
}

function fBuscarQuantAtualOper( urlPadrao, tipo = '' ) {
    try {
		
		fLimparAreaAlerta("AreaAlertaModalCadOper"); 

        if ( tipo == '' ) $("#txtDetOperQuant").val( "0" );
        if ( tipo == 'A') $("#txtDetOperIncorporacaoQuantAtual").val( "0" ); // Atual
        if ( tipo == 'N') $("#txtDetOperIncorporacaoQuantNovo").val( "0" ); // Novo

		var CodAtivo  = '';
        if ( tipo == '' ) CodAtivo = $("#selDetOperAtivo").val().trim();
        if ( tipo == 'A') CodAtivo = $("#selDetOperIncorporacaoAtivoAtual").val().trim(); // Atual
        if ( tipo == 'N') CodAtivo = $("#selDetOperIncorporacaoAtivoNovo").val().trim(); // Novo
        if ( tipo == 'A') fCalcularOperacaoIncorporacao();
        if ( tipo == 'N') fCalcularOperacaoIncorporacao();
		
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
                        if ( tipo == '' ) $("#txtDetOperQuant").val( Oper.QuantAtual );
                        if ( tipo == 'A') $("#txtDetOperIncorporacaoQuantAtual").val( Oper.QuantAtual ); // Atual
                        if ( tipo == 'N') $("#selDetOperIncorporacaoAtivoNovo").val( Oper.QuantAtual ); // Novo
                        if ( tipo == '' ) fCalcularOperacao();
                        if ( tipo == 'A') fCalcularOperacaoIncorporacao();
                        if ( tipo == 'N') fCalcularOperacaoIncorporacao();
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

function fBuscarPrecoAtualOper( urlPadrao ) {
    try {
		
		fLimparAreaAlerta("AreaAlertaModalCadOper"); 
		
		$("#txtDetOperPreco").val( "0" );
		fCalcularOperacao();
		
		var CodAtivo  = $("#selDetOperAtivo").val().trim();
		
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
						$("#txtDetOperPreco").val( Oper.PrecoAtual );
						fCalcularOperacao();
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

function fValidarDadosOper() {	
	try {
		
		fLimparAreaAlerta("AreaAlertaModalCadOper"); 
		
		var Tipo  = $("#txtDetOperTipo").val();
		var Ativo = $("#selDetOperAtivo").val();
		var Data  = $("#txtDetOperData").val();
		var Quant = $("#txtDetOperQuant").val();
		var Preco = $("#txtDetOperPreco").val();
		
		var ListaErros = "";
		if ( Ativo == ""                                       ) ListaErros = ListaErros + " - Cód. Ativo/Fundo<br/>";
		if ( Data  == ""                                       ) ListaErros = ListaErros + " - Data<br/>";
		if ( Quant == ""  || Quant == "0"                      ) ListaErros = ListaErros + " - Quant<br/>";
		if ( Tipo  == "A" || Tipo  == "C" || Tipo  == "V"                      )
			if ( Preco == ""  || Preco == ",00" || Preco == "0,00" ) ListaErros = ListaErros + " - Preço <br/>";
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

function fSalvarDadosOper( urlPadrao ){
	try {

		if ( !fValidarDadosOper() ) return;

		iniciarAnimacaoSalvar();	
		
		var Id        = $("#txtDetOperId").val();
		var Tipo      = $("#txtDetOperTipo").val();
		var Ativo     = $("#selDetOperAtivo").val();
		var Data      = $("#txtDetOperData").val();
		var Quant     = $("#txtDetOperQuant").val();
		var Preco     = '0' + $("#txtDetOperPreco").val();
		var Corretora =  $("#selDetOperCorretora").val();
		var TxCorret  = '0' + $("#txtDetOperTxCorret").val();
		var TxLiquid  = '0' + $("#txtDetOperTxLiquid").val();
		var TxEmol    = '0' + $("#txtDetOperTxEmol").val();
		var TxISS     = '0' + $("#txtDetOperTxISS").val();
		var TxIRRF    = '0' + $("#txtDetOperTxIRRF").val();
		var TxOutros  = '0' + $("#txtDetOperTxOutros").val();
			
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "operacoes/salvar",
			data    : {
				Id        : Id,
				Tipo      : Tipo, 
				Ativo     : Ativo,
				Data      : Data,
				Quant     : Quant,
				Preco     : Preco,
				Corretora : Corretora,
				TxCorret  : TxCorret,
				TxLiquid  : TxLiquid,
				TxEmol    : TxEmol,
				TxISS     : TxISS,
				TxIRRF    : TxIRRF,
				TxOutros  : TxOutros		   
			},
			success: function(result) {  
			
				finalizarAnimacaoSalvar();
				
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
							fLimparDadosModalOper(urlPadrao, Tipo);
							$("#txtDetOperTipo").val( Tipo );
							$("#txtDetOperData").val( fDataAtual() );
							$("#txtDetOperQuant").val( "100"  );
							if ( Tipo == "V" ) $("#BtnDetOperQuantAtual").show();
							fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
						}
						else{
							$("#PopModalDetalheOper").modal("hide");
							fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
						}
						buscar_todos_codigos_comprados( urlPadrao, 'selOperAtivo', false, true, false, true, true, true, true);
						fCarregarGrid( urlPadrao );
						return;
					}
					else{

						$("#PopModalDetalheOper").modal("hide");

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
				finalizarAnimacaoSalvar();
				fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText //MSG_ALERTA_ERRO
				return;
			}
		});
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

