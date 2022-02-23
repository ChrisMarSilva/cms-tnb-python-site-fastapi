
$(document).ready(function() {
	
	// $(this).attr("title", ":: TnB - Login ::");
	
	fLimparAreaAlertaPrinc();
	
	$("#txtEmail").val("");
	$("#txtSenha").val("");
	$("#chkLembrar").attr( "checked", false ) ;
	
	if (typeof(Storage) !== "undefined") {
	    $("#chkLembrar").attr( "checked", true ) ;
		var txtEmail   = localStorage.getItem( "TamoNaBolsa_PagLogin_TxtLogin"  );
		var txtSenha   = localStorage.getItem( "TamoNaBolsa_PagLogin_TxtSenha"  );
		var chkLembrar = localStorage.getItem( "TamoNaBolsa_PagLogin_ChkLembar" );
		if (chkLembrar == 'true') {
			$("#txtEmail").val( txtEmail );
			$("#txtSenha").val( txtSenha );
			$("#chkLembrar").attr( "checked", true ) ;
		} else  {
	        $("#chkLembrar").attr( "checked", false ) ;
		}
	}
	
});

function iniciarAnimacao() {
    $("#iEntrar").removeClass("fa-sign-in");
    $("#iEntrar").addClass("fa-spinner");
    $("#iEntrar").addClass("fa-pulse");
}

function finalizarAnimacao() {
    $("#iEntrar").removeClass("fa-spinner");
    $("#iEntrar").removeClass("fa-pulse");
    $("#iEntrar").addClass("fa-sign-in");
}

async function loginEntrar( urlPadrao ){
  try {

       promise = new Promise( (resolve, reject) => {

           finalizarAnimacao();

           var start = new Date().getTime();

           var txtEmail   = $("#txtEmail").val(); 
           var txtSenha   = $("#txtSenha").val(); 
           var chkLembrar = $("#chkLembrar").is(":checked");
          
            if( txtEmail == "" ){
              fCriarAlertaPrinc(TP_ALERTA_AVISO, "E-mail não informado!"); 
              return;
            }

           if( txtSenha == "" ){
              fCriarAlertaPrinc(TP_ALERTA_AVISO, "Senha não informada!"); 
              return;
           }
           
           if (typeof(Storage) !== "undefined") {
                  if (chkLembrar == true ){
                      localStorage.setItem("TamoNaBolsa_PagLogin_TxtLogin",  txtEmail  );
                      localStorage.setItem("TamoNaBolsa_PagLogin_TxtSenha",  txtSenha  );
                      localStorage.setItem("TamoNaBolsa_PagLogin_ChkLembar", 'true' );
                  }else{
                      localStorage.setItem("TamoNaBolsa_PagLogin_TxtLogin",  null );
                      localStorage.setItem("TamoNaBolsa_PagLogin_TxtSenha",  null );
                      localStorage.setItem("TamoNaBolsa_PagLogin_ChkLembar", null );
                  }
           }

           iniciarAnimacao();     

           $.ajax({
            cache   : "false",
            dataType: "json",
            async   : true,
            type    : "post",
            url     : urlPadrao + "login/entrar",
            data    : {
             txtEmail : txtEmail,
             txtSenha : txtSenha
          },
            success: function(result) {

              if( typeof(result) === 'string')
                result = JSON.parse( result ); // Converter para JSON

              var resultado = result.data.Resultado;
              var mensagem  = result.data.Mensagem;

              if (resultado == "NOK") {
                  finalizarAnimacao();
                  fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
                  return;
              } else if (resultado == "OK") {
                     // $(location).attr('href', urlPadrao + 'principal/inicial');
                      $(location).attr('href', urlPadrao + 'principal');
                     return true;
              } else {
                  finalizarAnimacao();
                  fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
                  return;
              }

            },
            error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
              finalizarAnimacao();
              fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); // request.responseText //MSG_ALERTA_ERRO
          return;
            }
          });



            // axios({
            //      method: 'post',
            //      url: urlPadrao + "login/entrar",
            //      timeout: 60000, // 60seg // 1Min
            //      responseType: 'text',
            //      headers: { 'Content-Type': 'application/json' }, // 'application/json'  // 'application/text charset=utf-8'
            //      data: JSON.stringify({ txtEmail: txtEmail, txtSenha: txtSenha }),
            //  })
            // .then( (response) => {
            //         try {
            //             let JSONString = response.data;
            //             let JSONObj = undefined;
            //             if( typeof(JSONString) === 'string') JSONObj = JSON.parse( JSONString.trim() );
            //             if( typeof(JSONString) === 'object') JSONObj = JSONString;
            //             let resultado = JSONObj.data.Resultado;
            //             let mensagem = JSONObj.data.Mensagem;
            //             // let Dados = JSONObj.data.Dados;
            //             if (resultado == "NOK") {
            //                 finalizarAnimacao();
            //                 fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
            //                 return;
            //             } else if (resultado == "OK") {
            //                 // $(location).attr('href', urlPadrao + 'principal/inicial');
            //                 $(location).attr('href', urlPadrao + 'principal');
            //                 return true;
            //             } else {
            //                 finalizarAnimacao();
            //                 fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
            //                 return;
            //             }
            //         } catch (error) {
            //             console.log('@TamoNaBolsa:Login-Catch',error);
            //         }
            // })
            // .catch( (error) => {
            //     console.log('@TamoNaBolsa:Login-Error',error);
            // });

            resolve(true);
      })
      .then( txt => {
            //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });

  } catch (e) {
    finalizarAnimacao();
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);  // MSG_ALERTA_ERRO // e.message()
	return;
  }
}