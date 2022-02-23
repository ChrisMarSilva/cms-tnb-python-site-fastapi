
//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

$(document).ready(function() {
	
	//$(this).attr("title", ":: TnB - Esqueceu a Senha ::");
	
	fLimparAreaAlertaPrinc();
	limparDados();
	
});

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function limparDados(){
	$("#txtEmail").val(""); 
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------


function fValidarDados() {	
	try {
		
		fLimparAreaAlertaPrinc();
		 
		 var txtUserEmail= $("#txtEmail").val(); 
	
		 if( txtUserEmail == "" ){
			  fCriarAlertaPrinc(TP_ALERTA_AVISO, "E-mail não informado.");
			  return;
		 }
		
		return true;
	
	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return false;
	} 
}

function enviarEmailSenha( urlPadrao ){
	try {
		
		if ( !fValidarDados() )
			return;

		iniciarAnimacaoSalvar();
		 
		 var txtUserEmail = $("#txtEmail").val(); 
			
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "usuario/enviarEmailSenha", 
			 data    : { txtUserEmail : txtUserEmail },
			success: function(result) {  
			
				finalizarAnimacaoSalvar();
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				
				if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					limparDados();
					fCriarAlertaPrinc(TP_ALERTA_SUCESSO, mensagem);		
				} else {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				finalizarAnimacaoSalvar();
				fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);  // request.responseText //MSG_ALERTA_ERRO
				return;
			}
		});
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------


