
$(document).ready(function() {
	$("#MnHomeConta").addClass("active open");
	fLimparAreaAlertaPrinc();
	limparDados();
});

function limparDados(){
	$("#txtUserNome").val(""); 
	$("#txtUserEmail").val(""); 
	$("#txtUserSenha").val(""); 
	$("#txtUserConfirmaSenha").val("");
	$("#chkUserTermosAcesso").attr( "checked", false ) ;
}

function fValidarDados() {	
	try {
		
		fLimparAreaAlertaPrinc();
		
		 var txtUserNome          = $("#txtUserNome").val().trim(); 
		 var txtUserEmail         = $("#txtUserEmail").val().trim(); 
		 var txtUserSenha         = $("#txtUserSenha").val().trim(); 
		 var txtUserConfirmaSenha = $("#txtUserConfirmaSenha").val().trim();
		 var chkUserTermosAcesso  = $("#chkUserTermosAcesso").is( ":checked" );
		
		var ListaErros = "";
		
		 if( txtUserNome == "" ) ListaErros = ListaErros + " - Nome<br/>";
		 if( txtUserEmail == "" ) ListaErros = ListaErros + " - E-mail<br/>";
		 if( txtUserSenha == "" ) ListaErros = ListaErros + " - Senha<br/>";
		 if( txtUserConfirmaSenha == "" ) ListaErros = ListaErros + " - Confirmação de Senha<br/>";
		 
		if( ListaErros != "" ){
			fCriarAlertaPrinc(TP_ALERTA_AVISO, "Os seguintes campos não estão preenchido: <br/>"+ListaErros);
			return false;
		}	
		 
		 if( txtUserSenha != txtUserConfirmaSenha ){
			 fCriarAlertaPrinc(TP_ALERTA_AVISO, "As senhas informadas não são iguais.");
		     return;
		 }	 
		 
		 if( chkUserTermosAcesso != true ){
			 fCriarAlertaPrinc(TP_ALERTA_AVISO, "Você deve aceitar os termos e condições de acesso.");
		  return;
		 }
		
		return true;
	
	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return false;
	} 
}

function criarNovaConta( urlPadrao ){
	try {
		
		if ( !fValidarDados() )
			return;

		iniciarAnimacaoSalvar();
		
		 var txtUserNome  = $("#txtUserNome").val().trim();
		 var txtUserEmail = $("#txtUserEmail").val().trim();
		 var txtUserSenha = $("#txtUserSenha").val().trim();
			
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "usuario/salvarDadosConta",
			 data    : { txtUserNome  : txtUserNome, txtUserEmail : txtUserEmail, txtUserSenha : txtUserSenha },
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
				fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText //MSG_ALERTA_ERRO
				return;
			}
		});
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}