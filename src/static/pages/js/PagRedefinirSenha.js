
$(document).ready(function() {
	
	//$(this).attr("title", "Redefinir a Senha - " + NOME_PROJETO);
	
	fLimparAreaAlertaPrinc();
	limparDados();
	
});

function limparDados(){
	$("#txtNovaSenha").val(""); 
	$("#txtConfirNovaSenha").val(""); 
}

function fValidarDados() {	
	try {
		
		fLimparAreaAlertaPrinc();
		 
		 var txtUserEmail         = $("#txtUserEmail").val(); 
		 var txtUserSenha         = $("#txtNovaSenha").val(); 
		 var txtUserConfirmaSenha = $("#txtConfirNovaSenha").val(); 
	
		 if( txtUserEmail == "" ){
			  fCriarAlertaPrinc(TP_ALERTA_AVISO, "E-mail não informado.");
			  return;
		 }
		 
		 if( txtUserSenha == "" ){
			  fCriarAlertaPrinc(TP_ALERTA_AVISO, "Senha não informada.");
			  return;
		 }
		 
		 if( txtUserConfirmaSenha == "" ){
			  fCriarAlertaPrinc(TP_ALERTA_AVISO, "Confirmação de Senha não informada.");
			  return;
		 }
		 
		 if( txtUserSenha != txtUserConfirmaSenha ){
			 fCriarAlertaPrinc(TP_ALERTA_AVISO, "As senhas informadas não são iguais.");
		     return;
		 }	 
		
		return true;
	
	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return false;
	} 
}

function fSalvarSenha( urlPadrao ){
	try {
		
		if ( !fValidarDados() )
			return;

		iniciarAnimacaoSalvar();
		 
		 var txtUserEmail = $("#txtUserEmail").val(); 
		 var txtUserSenha = $("#txtNovaSenha").val();
			
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "usuario/salvarnovasenha",
			 data    : { txtUserEmail : txtUserEmail, txtUserSenha : txtUserSenha },
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
					//limparDados();
					//fCriarAlertaPrinc(TP_ALERTA_SUCESSO, mensagem);	
					$(location).attr('href', urlPadrao + 'usuario/sucessoredefinirsenha');
				} else {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				finalizarAnimacaoSalvar();
				fCriarAlertaPrinc(TP_ALERTA_ERRO, request.responseText);   // request.responseText // MSG_ALERTA_ERRO
				return;
			}
		});
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}
