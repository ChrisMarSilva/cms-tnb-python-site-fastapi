
function fAbrirModalDetalheAtivo( urlPadrao ) {
    try {

		$("#AreaAlertaModalCadAtivo").html("");
		$("#txtCadAtivoCodigo").val("");
		
		fDefinirPadraoSelect('txtCadAtivoCodigo');
		
		$('#PopModalDetalheAtivo').modal({backdrop: 'static'});
		
		$('#PopModalDetalheAtivo').on('shown.bs.modal', function() {
			$('#txtCadAtivoCodigo').focus();
		})

    } catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fCriarAlertaModalCadAtivo(Tipo, Mensagem){
	
	var DivAlerta = $("<div/>"); 
	DivAlerta.addClass( "alert "+Tipo+" alert-dismissible fade show" ); 
	DivAlerta.attr("id", 'DivAlerta'+fGerarNumeroAleatorio());
	DivAlerta.append( '<button type="button" class="close" data-dismiss="alert" aria-label="Close"> <span aria-hidden="true">&times;</span> </button>' );	
	if(Tipo==TP_ALERTA_AVISO)
		DivAlerta.append( '<small> <strong>Aviso:</strong> '+Mensagem+'</small> ' );
	if(Tipo==TP_ALERTA_SUCESSO)
		DivAlerta.append( '<small> <strong>OK:</strong> '+Mensagem+'</small> ' );
	if(Tipo==TP_ALERTA_ERRO)
		DivAlerta.append( '<small> <strong>Erro:</strong> '+Mensagem+'</small> ' );
	if(Tipo==TP_ALERTA_ALERTA)
		DivAlerta.append( '<small> <strong>Alerta:</strong> '+Mensagem+'</small> ' );
	DivAlerta.delay(5000).fadeOut("slow", function () { $(this).remove(); });
	
	$("#AreaAlertaModalCadAtivo").append( DivAlerta );	
}


function fValidarDadosAtivo() {	
	try {
		
		$("#AreaAlertaModalCadAtivo").html("");
		
		if( $("#txtCadAtivoCodigo").val() == "" ){
			fCriarAlertaModalCadAtivo(TP_ALERTA_AVISO, 'Por favor, preencha o campo Cód Ativo!'); 
			return false;
		}	
		
		return true;
	
	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return false;
	} 
}

function fSalvarDadosAtivo( urlPadrao ){
	try {
		
		var IdPortfolio = fGetAbaIdPortfolio();
	   
        if ( IdPortfolio  == "" ){
          fCriarAlertaModalCadAtivo(TP_ALERTA_AVISO, 'Id. Portfólio não informado!'); 
          return;
        }
		
		if ( !fValidarDadosAtivo() )
			return false;

		iniciarAnimacaoSalvar();

		var CodAtivo = $("#txtCadAtivoCodigo").val(); 
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "portfolio/salvarAtivo",
			data    : { IdPortfolio : IdPortfolio, CodAtivo : CodAtivo },
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
					$("#PopModalDetalheAtivo").modal("hide");					
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					fRecarregarPagina( urlPadrao, IdPortfolio );
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
		fCriarAlertaModalCadAtivo(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function fAbrirModalRemoverAtivo( urlPadrao, IdPortfolio, IdAtivo, CodAtivo ) {
    try {
		
		fLimparAreaAlerta("AreaAlertaPrinc");	

		if ( IdPortfolio == "" ){
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, 'Id. Portfólio não informado!');
			return;
		}

		if ( IdAtivo == "" ){
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, 'Id. Ativo não informado!');
			return;
		}

		if ( CodAtivo == "" ){
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, 'Cod. Ativo não informado!');
			return;
		}
	  
		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "portfolio/excluirAtivo",
			data: {  IdPortfolio: IdPortfolio, IdAtivo: IdAtivo, CodAtivo: CodAtivo },
			success: function (result) {			
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, mensagem); 
					return false;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {					
				    fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO, mensagem); 
				    fRecarregarPagina( urlPadrao, IdPortfolio );
					return true;
				} else {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem); 
					return false;
				}
				
			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);  // request.responseText // MSG_ALERTA_ERRO
			}
		});

    } catch (e) {
        $("#PopModalDelPortfolio").modal("hide");
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}
