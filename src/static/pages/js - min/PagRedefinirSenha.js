function limparDados(){$("#txtNovaSenha").val(""),$("#txtConfirNovaSenha").val("")}function fValidarDados(){try{fLimparAreaAlertaPrinc();var a=$("#txtUserEmail").val(),r=$("#txtNovaSenha").val(),i=$("#txtConfirNovaSenha").val();return""==a?void fCriarAlertaPrinc(TP_ALERTA_AVISO,"E-mail não informado."):""==r?void fCriarAlertaPrinc(TP_ALERTA_AVISO,"Senha não informada."):""==i?void fCriarAlertaPrinc(TP_ALERTA_AVISO,"Confirmação de Senha não informada."):r==i||void fCriarAlertaPrinc(TP_ALERTA_AVISO,"As senhas informadas não são iguais.")}catch(a){return fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}function fSalvarSenha(a){try{if(!fValidarDados())return;iniciarAnimacaoSalvar();var r=$("#txtUserEmail").val(),i=$("#txtNovaSenha").val();$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"usuario/salvarnovasenha",data:{txtUserEmail:r,txtUserSenha:i},success:function(r){finalizarAnimacaoSalvar();var i=r.data.Resultado,n=r.data.Mensagem;"NOK"!=i?"FALHA"!=i&&"OK"==i?$(location).attr("href",a+"usuario/sucessoredefinirsenha"):fCriarAlertaPrinc(TP_ALERTA_ERRO,n):fCriarAlertaPrinc(TP_ALERTA_AVISO,n)},error:function(a,r,i){finalizarAnimacaoSalvar(),fCriarAlertaPrinc(TP_ALERTA_ERRO,a.responseText)}})}catch(a){return finalizarAnimacaoSalvar(),void fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}$(document).ready(function(){fLimparAreaAlertaPrinc(),limparDados()});