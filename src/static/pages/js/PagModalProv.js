
//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fMostrarCalcVlrLiq() {	
	try {
		 
		var Tipo = $("#selDivTipo").val(); 

		if( Tipo == "J" ){ //J-Juros Sobre Capital Proprio
			$("#DivCalcVlrLiq").show();
		}else{
			$("#DivCalcVlrLiq").hide();
		}

		$("#txtDivCalcVlrLiq").attr( "checked", false );	

	} catch (e) {
		fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	} 
}

function fMostrarValorBruto() {	
	try {
		 
		var Tipo          = $("#selDivTipo").val(); 
		var chkCalcVlrLiq = $("#txtDivCalcVlrLiq").is(":checked");

		if( Tipo == "J" && chkCalcVlrLiq==true ){ //J-Juros Sobre Capital Proprio
			$("#DivPrecoBruto").show();
			$("#DivTotalBruto").show();

			$("#txtDivPreco").attr("readonly", "readonly");
			//$("#txtDivPreco").removeAttr("required");
			$("#txtDivPrecoBruto").val( $('#txtDivPreco').val() );
				
			$("#txtDivPrecoBruto").bind("keyup change",      function(){ fCalcularDividendo(); } );
			$( "#txtDivPreco" ).unbind( "keyup" );
			$( "#txtDivPreco" ).unbind( "change" );
			
		}else{
			$("#DivPrecoBruto").hide();
			$("#DivTotalBruto").hide();

			$("#txtDivPreco").removeAttr("readonly");
			//$("#txtDivPreco").attr("required", "required");
			$("#txtDivPreco").val( $('#txtDivPrecoBruto').val() );
			
			$("#txtDivPreco").bind("keyup change",      function(){ fCalcularDividendo(); } );
			$( "#txtDivPrecoBruto" ).unbind( "keyup" );
			$( "#txtDivPrecoBruto" ).unbind( "change" );
		}	

	} catch (e) {
		fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	} 
}

function fCalcularDividendo() {	
	try {	
		
		$("#txtDivTotalBruto").val( "0,00" );//TotBrt
		$("#txtDivTotal").val(      "0,00" );//TotLiq

		var Tipo       = $("#selDivTipo").val();  
		var CalcVlrLiq = $("#txtDivCalcVlrLiq").is(":checked");
		var Quant      = GetValorInteiro(      $('#txtDivQuant').val()      ); 
		var PrecoBrt   = GetValorDecimalMaior( $('#txtDivPrecoBruto').val() );
		var PrecoLiq   = GetValorDecimalMaior( $('#txtDivPreco').val() );
		var TotalBrt   = 0.00;
		var TotalLiq   = 0.00;

		if ( Quant <= 0                     ) return false;
		if ( PrecoBrt <= 0 && PrecoLiq <= 0 ) return false;

		if( Tipo=="J" && CalcVlrLiq==true ){
			PrecoLiq = 0.00;	
			if( PrecoBrt > 0 ) PrecoLiq = PrecoBrt - ( ( PrecoBrt * 15.00 ) / 100 ); 
			$("#txtDivPreco").val( fMascaraValorMaior(PrecoLiq) );
		}else{
			PrecoBrt = 0.00;	
			if( PrecoLiq > 0 ) PrecoBrt = PrecoLiq; 
			$("#txtDivPrecoBruto").val( $('#txtDivPreco').val() );
		}
		
		if ( PrecoBrt > 0 )  TotalBrt = PrecoBrt * Quant;	
		if ( PrecoLiq > 0 )  TotalLiq = PrecoLiq * Quant;	
		
		$("#txtDivTotalBruto").val( fMascaraValor(TotalBrt) );//TotBrt
		$("#txtDivTotal").val(      fMascaraValor(TotalLiq) );//TotLiq

	} catch (e) {
		fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	} 
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fLimparDadosModalRend() {

	fLimparAreaAlerta("AreaAlertaModalCadProv");
	
	$("#txtDivId").val(          "" );
	//$("#selDivTipo").val(        "" );
	$('#selDivTipo')[0].selectedIndex = 2; // Primeiro Tipo - dividendos
	$("#selDivAtivo").val(       "" );
	//$("#selDivCorretora").val(   "" );
	$('#selDivCorretora')[0].selectedIndex = 2; // Primeira Corretora
	$("#txtDivDataEx").val(      "" );
	$("#txtDivDataPagto").val(   "" );
	$("#txtDivQuant").val(       "0" );
	$("#txtDivCalcVlrLiq").attr( "checked", false ) ;
	$("#txtDivPrecoBruto").val(  "0,00" );
	$("#txtDivPreco").val(       "0,00" );
	$("#txtDivTotalBruto").val(  "0,00" );
	$("#txtDivTotal").val(       "0,00" );
	
	fDefinirPadraoSelect('selDivTipo');
	fDefinirPadraoSelect('selDivAtivo');
	fDefinirPadraoSelect('selDivCorretora');
	
	fMostrarCalcVlrLiq();
	fMostrarValorBruto();

	$("#BtnDivQuantAtual").hide();
}

function fAbrirModalDetalheRend( urlPadrao, IdRent, CodAtivo, TipoModal ) {
    try {

    	fLimparDadosModalRend();

    	$("#PopModalDetalheRendTit").html(" - "+TipoModal);
					
		if ( TipoModal == "Novo" ){
	    	$('#PopModalDetalheRend').modal({backdrop: 'static'})  ;
			$("#txtDivDataEx").val(  fDataAtual() );
			$("#txtDivDataPagto").val(  fDataAtual() );
			$("#BtnDivQuantAtual").show();
			$("#selDivAtivo").focus();
		} else if ( TipoModal == "Alterar" ) {
		    fCarregarDadosModalDetalheRend( urlPadrao, IdRent, CodAtivo, TipoModal );
		}

    } catch (e) {
		fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fAbrirModalDetalheRendCalend( urlPadrao, ProvTipo, ProvCodigo, ProvDtEx, ProvDtPagto, ProvValor, TipoInvest, ProvQuant = '100' ) {
    try {

    	fAbrirModalDetalheRend( urlPadrao, '', '', 'Novo' );

		$("#txtDivId").val(         ""          );
		$("#selDivTipo").val(       ProvTipo    );
		$("#selDivAtivo").val(      ProvCodigo  );
		$("#selDivCorretora").val(  ""          );
		$("#txtDivDataEx").val(     ProvDtEx    );
		$("#txtDivDataPagto").val(  ProvDtPagto );
		$("#txtDivQuant").val(      ProvQuant.toString() );
			
		fDefinirPadraoSelect('selDivTipo');
		fDefinirPadraoSelect('selDivAtivo');
		fDefinirPadraoSelect('selDivCorretora');

		if( ProvTipo == "J" ){ //J-Juros Sobre Capital Proprio
			$("#DivCalcVlrLiq").show();
		}else{
			$("#DivCalcVlrLiq").hide();
			$("#txtDivCalcVlrLiq").attr( "checked", false );	
		}		
		
		// fBuscarQuantAtualRend( urlPadrao );
		fMostrarValorBruto();
		
		$("#txtDivPrecoBruto").val( ProvValor );
		$("#txtDivPreco").val(      ProvValor );

		fCalcularDividendo();	

    } catch (e) {
		fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fCarregarDadosModalDetalheRend( urlPadrao, IdRent, CodAtivo, TipoModal ) {
    try {

		if ( IdRent == "" ){
			 fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_AVISO, 'Id. Provendo não informado!');
			   return;
		 }

       if ( CodAtivo == "" ){
			fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_AVISO, 'Cód. Ativo não informado!');
          	return;
        }

         $.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "proventos/carregar",
            data    : { IdRent: IdRent, CodAtivo: CodAtivo },
            success: function (result) {
			
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var Rent      = result.data.Dados;
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_AVISO, mensagem); 
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, mensagem); 
				} else if (resultado == "OK") {
					
				   if ( Rent.IdRent ) { 

						$("#txtDivId").val(         Rent.IdRent     );
						$("#selDivTipo").val(       Rent.Tipo       );
						$("#selDivAtivo").val(      Rent.CodAtivo   );
						$("#selDivCorretora").val(  Rent.Corretora  );
						$("#txtDivDataEx").val(     Rent.DataEx     );
						$("#txtDivDataPagto").val(  Rent.DataPagto  );
						$("#txtDivQuant").val(      Rent.Quant      );

						fDefinirPadraoSelect('selDivTipo');
						fDefinirPadraoSelect('selDivAtivo');
						fDefinirPadraoSelect('selDivCorretora');

						// fMostrarCalcVlrLiq();
						if( Rent.Tipo == "J" ){ //J-Juros Sobre Capital Proprio
							$("#DivCalcVlrLiq").show();
							if ( Rent.CalcVlrLiq=="S" ) $("#txtDivCalcVlrLiq").attr( "checked", true );
						}else{
							$("#DivCalcVlrLiq").hide();
							$("#txtDivCalcVlrLiq").attr( "checked", false );	
						}						

						fMostrarValorBruto();
						
						$("#txtDivPrecoBruto").val( Rent.PrecoBruto );
						$("#txtDivPreco").val(      Rent.Preco      );

						fCalcularDividendo();

						$('#PopModalDetalheRend').modal({backdrop: 'static'}); 

					} else {
						fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, mensagem); 
					}
					
				} else {
					fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, mensagem); 
				}

            },
            error: function (data) {
				fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
            }
        });        

    } catch (e) {
		fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}


//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fBuscarQuantAtualRend( urlPadrao ) {
    try {
		
		fLimparAreaAlerta("AreaAlertaModalCadProv");
		
		$("#txtDivQuant").val( "0" );
		fCalcularDividendo();
		
		var CodAtivo = $("#selDivAtivo").val().trim();		

		if ( CodAtivo == "" ){
			//fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_AVISO, 'Ativo não informado!');
			return;
		}

		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "operacoes/quantidade",
			data: { CodAtivo: CodAtivo },
			success: function (result) {
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var Oper      = result.data.Dados;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_AVISO, mensagem); 
					return false;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {	
					if ( Oper.QuantAtual )
						$("#txtDivQuant").val( Oper.QuantAtual );
						fCalcularDividendo();
					return true;
				} else {
					fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, mensagem); 
					return false;
				}
			},
			error: function (data) {
				fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
			}
		});

    } catch (e) {
		fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }	
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fValidarDadosRend() {	
	try {
		
		fLimparAreaAlerta("AreaAlertaModalCadProv");

		var Tipo      = $("#selDivTipo").val(); 
		var Ativo     = $("#selDivAtivo").val(); 
		var DataEx    = $("#txtDivDataEx").val(); 
		var DataPagto = $("#txtDivDataPagto").val(); 
		var Quant     = $("#txtDivQuant").val(); 
		var Preco     = $("#txtDivPreco").val(); 
		
		var ListaErros = "";
		if( Tipo      == ""                                      ) ListaErros = ListaErros + " - Tipo<br/>";
		if( Ativo     == ""                                      ) ListaErros = ListaErros + " - Cód. Ativo/Fundo<br/>";
		if( DataEx    == ""                                      ) ListaErros = ListaErros + " - Data Ex.<br/>";
		if( DataPagto == ""                                      ) ListaErros = ListaErros + " - Data Pagto<br/>";
		if( Quant     == ""                                      ) ListaErros = ListaErros + " - Quant.<br/>";
		if( Preco     == "" || Preco == ",00" || Preco == "0,00" ) ListaErros = ListaErros + " - Preço<br/>";
		if( ListaErros != "" ){
			fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_AVISO, "Os seguintes campos não estão preenchido: <br/>"+ListaErros);
			return false;
		}		
		
		return true;
	
	} catch (e) {
		fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return false;
	} 
}

function fSalvarDadosRend( urlPadrao ){
	try {
		
		if ( !fValidarDadosRend() ) return false;

		iniciarAnimacaoSalvar();

		var Id         = $("#txtDivId").val(); 
		var Tipo       = $("#selDivTipo").val(); 
		var Ativo      = $("#selDivAtivo").val(); 
		var Corretora  = $("#selDivCorretora").val();
		var DataEx     = $("#txtDivDataEx").val(); 
		var DataPagto  = $("#txtDivDataPagto").val(); 
		var Quant      = $("#txtDivQuant").val(); 
		var CalcVlrLiq = "N";
		var PrecoBruto = $("#txtDivPrecoBruto").val(); 
		var Preco      = $("#txtDivPreco").val(); 

		if( $("#txtDivCalcVlrLiq").is(":checked") ) CalcVlrLiq = "S";
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "proventos/salvar",
			data    : {
				Id         : Id,
				Tipo       : Tipo,
				Ativo      : Ativo,
				Corretora  : Corretora,
				DataEx     : DataEx,
				DataPagto  : DataPagto,
				Quant      : Quant,
				CalcVlrLiq : CalcVlrLiq,
				PrecoBruto : PrecoBruto,
				Preco      : Preco	   
			},
			success: function(result) {  
			
				finalizarAnimacaoSalvar();
				
				var resultado = result.data.Resultado; 
				var mensagem = result.data.Mensagem; 
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {

					var PathName = $(location).attr('pathname') || window.location.pathname;
					var iUlt = PathName.split('/').length - 1;
					if ( PathName.split('/')[iUlt] != '' ) PathName = PathName.split('/')[iUlt];
					PathName = PathName.toLowerCase(); //toUpperCase
	                PathName = PathName.replace('/index.fcgi/', '');
	                PathName = PathName.replace('index.fcgi/', '');
    	            PathName = PathName.replace('/index.fcgi', '');
    	            PathName = PathName.trim();

					if( PathName == "proventos" || PathName == "/proventos/" || PathName == "proventos/" || PathName == "/proventos" ){
						if( Id == undefined || Id.toString() == "undefined" || Id.toString() == "" ){
							fLimparDadosModalRend();
							fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
							$("#txtDivDataEx").val( fDataAtual() );
							$("#txtDivDataPagto").val( fDataAtual() );
							$("#BtnDivQuantAtual").show();
						}
						else{
							$("#PopModalDetalheRend").modal("hide");
							fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
						}
						buscar_todos_codigos_proventos( urlPadrao, 'selRendAtivo', false, true, false );
						fCarregarGrid(urlPadrao);
					}else if( PathName == "principal" || PathName == "/principal/" || PathName == "principal/" || PathName == "/principal" ){
						$("#PopModalDetalheRend").modal("hide");
						fCarrgarDadosProventos(urlPadrao);
					}else if( PathName == "cei" || PathName == "/cei/" || PathName == "cei/" || PathName == "/cei" ){
						$("#PopModalDetalheRend").modal("hide");
						fAlterarSitProvCei( urlPadrao, PagCeiLstIdProv, '', PagCeiSitLanc, 0, false );
						fProcurarAlterarLinhaGridProv( urlPadrao, PagCeiLstIdxTr, PagCeiSitLanc ); 
						return;
					}else{
						$("#PopModalDetalheRend").modal("hide");
						fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					}

				} else {
					fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function (request, status, error) { //error: function(data) {  //error: function (request, status, error) {
				finalizarAnimacaoSalvar();
				fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, request.responseText); // request.responseText //MSG_ALERTA_ERRO
				return;
			}
		});
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		fCriarAlerta("AreaAlertaModalCadProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fAprovarProventos( urlPadrao, IdProv, CodAtivo ){
	try {

		if( IdProv == "" ){
			fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, "Id. Provento não Informado...");
			return false;
		}
		
		if( CodAtivo == "" ){
			fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, "Cód. Ativo/Fundo não Informado...");
			return false;
		}

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "proventos/aprovar",
			data    : { Id: IdProv, CodAtivo: CodAtivo },
			success: function(result) {  
				
				var resultado = result.data.Resultado; 
				var mensagem = result.data.Mensagem; 
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {

					var PathName = $(location).attr('pathname') || window.location.pathname; // /portfolio
					var iUlt = PathName.split('/').length - 1;
					if ( PathName.split('/')[iUlt] != '' ) PathName = PathName.split('/')[iUlt];
					PathName = PathName.toLowerCase(); //toUpperCase
	                PathName = PathName.replace('/index.fcgi/', '');
	                PathName = PathName.replace('index.fcgi/', '');
    	            PathName = PathName.replace('/index.fcgi', '');
    	            PathName = PathName.trim();

					if( PathName == "proventos" || PathName == "/proventos/" || PathName == "proventos/" || PathName == "/proventos" ){
						fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
						fCarregarGrid(urlPadrao);	
					}else if( PathName == "principal" || PathName == "/principal/" || PathName == "principal/" || PathName == "/principal" ){
						fCarrgarDadosProventos(urlPadrao);
					}else{
						fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					}

				} else {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				}
			},
			error: function(data) {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});
	
	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fChamarPagExclusaoRend( IdRend, CodAtivo ) {
	try {

		$("#txtIdRendDel").val("");
		$("#txtCodRendDel").val("");

		if ( IdRend == "" ){
			fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Provento não informado!'); 
			return;
		}

	if ( CodAtivo == "" ){
		fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Cód. Aitvo não informado!'); 
		return;
	}
	
		 $("#PopModalDelRend").modal({backdrop: "static"});

		 $("#txtIdRendDel").val(  IdRend   );
		 $("#txtCodRendDel").val( CodAtivo );

	} catch (e) {
			$("#PopModalDelRend").modal("hide");
			finalizarAnimacaoExcluir();
	fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

function fExcluirDadosRendimento( urlPadrao, IdProv, CodProv ) {
	try {

	fLimparAreaAlerta("AreaAlertaModalImportProv");
	finalizarAnimacaoExcluir();

	var IdRend   = $("#txtIdRendDel").val();
	var CodAtivo = $("#txtCodRendDel").val();

	if ( IdProv  ) IdRend   = IdProv;
	if ( CodProv ) CodAtivo = CodProv;
	
	if ( IdRend == "" ){
		if ( !IdProv ) fCriarAlertaModalExc(TP_ALERTA_AVISO, 'Id. Provento não informado!');
		if (  IdProv ) fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_SUCESSO, 'Id. Provento não informado!');
		return;
	}
	
	if ( CodAtivo == "" ){
		if ( !CodProv ) fCriarAlertaModalExc(TP_ALERTA_AVISO, 'Cód. Ativo não informado!');
		if (  CodProv ) fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_SUCESSO, 'Cód. Ativo não informado!');
		return;
	}

	iniciarAnimacaoExcluir();
	
	$.ajax({
		dataType: "json",
		type: "post",
		url : urlPadrao + "proventos/excluir",
		data: { IdRend: IdRend, CodAtivo: CodAtivo },
		success: function (result) {
			
			finalizarAnimacaoExcluir();				
			
			var resultado = result.data.Resultado; 
			var mensagem  = result.data.Mensagem;

			if (resultado == "NSESSAO") {
				$(location).attr('href', urlPadrao + '/login');
				return false;
			} else if (resultado == "NOK") {
				if ( !IdProv ) fCriarAlertaModalExc(TP_ALERTA_AVISO, mensagem); 
				if (  IdProv ) fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_AVISO, mensagem);
				return false;
			} else if (resultado == "FALHA") {
				if ( !IdProv ) fCriarAlertaModalExc(TP_ALERTA_ERRO, mensagem); 
				if (  IdProv ) fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_ERRO, mensagem);
				return;
			} else if (resultado == "OK") {	
				
				var PathName = $(location).attr('pathname') || window.location.pathname;
				var iUlt = PathName.split('/').length - 1;
				if ( PathName.split('/')[iUlt] != '' ) PathName = PathName.split('/')[iUlt];
				PathName = PathName.toLowerCase(); //toUpperCase
				PathName = PathName.replace('/index.fcgi/', '');
				PathName = PathName.replace('index.fcgi/', '');
				PathName = PathName.replace('/index.fcgi', '');
				PathName = PathName.trim();

				if( PathName == "proventos" || PathName == "/proventos/" || PathName == "proventos/" || PathName == "/proventos" ){
                    if ( !IdProv ) {
                        fCriarAlertaPrinc(TP_ALERTA_SUCESSO, mensagem);
                        $("#txtIdRendDel").val("");
                        $("#PopModalDelRend").modal("hide");
                        fCarregarGrid( urlPadrao );
                        buscar_todos_codigos_proventos( urlPadrao, 'selRendAtivo', false, true, false );
                    }
                    if ( IdProv ) {
                        var tr = $('#TrImport'+IdProv).closest('tr');	 //tr.fadeOut(400);
                        tr.fadeOut(400, function() {
                            tr.remove();
                            var rowCount = $('#GridImport tr').length;
                            if ( rowCount <= 1 )  $("#AreaTableModalImportProv").html( "" ); //$("#GridImport").remove();
                        });
                    }
				}else if( PathName == "principal" || PathName == "/principal/" || PathName == "principal/" || PathName == "/principal" ){
					fCarrgarDadosProventos(urlPadrao);
					$("#PopModalDelRend").modal("hide");
				}
		
				return true;

			} else {
				if ( !IdProv ) fCriarAlertaModalExc(TP_ALERTA_ERRO, mensagem); 
				if (  IdProv ) fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_ERRO, mensagem);
				return false;
			}
			
		},
		error: function (data) {
			$("#PopModalDelRend").modal("hide");
			finalizarAnimacaoExcluir();
			if ( !IdProv ) fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
			if (  IdProv ) fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		}
	});

	} catch (e) {
			$("#PopModalDelRend").modal("hide");
			finalizarAnimacaoExcluir();
	if ( !IdProv ) fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	if (  IdProv ) fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------