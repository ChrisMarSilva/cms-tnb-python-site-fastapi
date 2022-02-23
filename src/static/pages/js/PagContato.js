$(document).ready(function() {
	$("#MnHomeContato").addClass("active open");
	fLimparAreaAlertaPrinc();
	limparDados();
});

function limparDados(){
	$("#txtContatoNome").val(""); 
	$("#txtContatoEmail").val(""); 
	$("#txtContatoAssunto").val(""); 
	$("#txtContatoMensagem").val(""); 
}

function fValidarDados() {
    try {

        fLimparAreaAlertaPrinc();

        var txtContatoNome          = $("#txtContatoNome").val();
        var txtContatoEmail         = $("#txtContatoEmail").val();
        var txtContatoAssunto       = $("#txtContatoAssunto").val();
        var txtContatoMensagem      = $("#txtContatoMensagem").val();

        var ListaErros = "";
        if( txtContatoNome == "" ) ListaErros = ListaErros + " - Nome<br/>";
        if( txtContatoEmail == "" )ListaErros = ListaErros + " - E-mail<br/>";
        if( txtContatoAssunto == "" )ListaErros = ListaErros + " - Assunto<br/>";
        if( txtContatoMensagem == "" )ListaErros = ListaErros + " - Mensagem<br/>";

        if( ListaErros != "" ){
            fCriarAlertaPrinc(TP_ALERTA_AVISO, "Os seguintes campos não estão preenchido: <br/>"+ListaErros);
            return false;
        }

        return true;

    } catch (e) {
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
        return false;
    }
}

function enviarMensagem( urlPadrao ){
	try {
		
		if ( !fValidarDados() )
			return;

		iniciarAnimacaoSalvar();
		
		 var txtContatoNome          = $("#txtContatoNome").val(); 
		 var txtContatoEmail         = $("#txtContatoEmail").val(); 
		 var txtContatoAssunto       = $("#txtContatoAssunto").val(); 
		 var txtContatoMensagem      = $("#txtContatoMensagem").val(); 
		 var txtContatoCodigoCaptcha = ""; //$("#txtContatoCodigoCaptcha").val(); 
			
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "contato/enviarMensagem",
			 data    : { txtContatoNome  : txtContatoNome, txtContatoEmail : txtContatoEmail, txtContatoAssunto : txtContatoAssunto, txtContatoMensagem : txtContatoMensagem, txtContatoCodigoCaptcha : txtContatoCodigoCaptcha },
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
			error: function(data) {
				finalizarAnimacaoSalvar();
				fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}