
$(document).ready(function() {

    //$(this).attr("title", "Perfil - " + NOME_PROJETO);
    $("#MnPrincPerfil").addClass("active open");

    fLimparAreaAlertaPrinc();

});

function fLimparDadosPerfil( urlPadrao ){
	$("#txtNome").val(""); 
  $("#txtChatId").val(""); 
  $("#txtEmail").val(""); 
}

function fLimparDadosFoto( urlPadrao ){
  $("#txtFoto").val(""); 
  $("#imgPerfil").attr('src', urlPadrao + "static/pages/img/pessoa-icon.png" );
}

function fLimparDadosSenha( urlPadrao ){
  $("#txtSenhaAtual").val(""); 
  $("#txtNovaSenha").val("");  
  $("#txtConfirNovaSenha").val(""); 
  $("#txtSenhaResetar").val(""); 
}

function fLimparDadosCei( urlPadrao ){
  $("#txtCeiCPF").val(""); 
  $("#txtCeiSenha").val("");  
  $("#txtDetCeiSitDescr").html("");  
  $("#txtCeiCPF").attr('autocomplete', 'off');
  $("#txtCeiCPF").attr('autocomplete', 'off');
}

function fCarregarDados( urlPadrao ){
  try {

       promise = new Promise( (resolve, reject) => {

        // fLimparAreaAlertaPrinc();

        fLimparDadosPerfil( urlPadrao );
        fLimparDadosFoto(   urlPadrao );
        fLimparDadosSenha(  urlPadrao );
        fLimparDadosCei(    urlPadrao );
        
        $.ajax({
          cache   : "false",
          dataType: "json",
          async   : true,
          type    : "POST",
          url     : urlPadrao + "perfil/carregar",
          success: function(result) {  
          
              var resultado = result.data.Resultado; 
              var mensagem  = result.data.Mensagem; 
              var Dados     = result.data.Dados; 
              
              if (resultado == "NSESSAO") {
                $(location).attr('href', urlPadrao + '/login');
                return false;
              } else if (resultado == "NOK") {
                fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
                return false;
              } else if (resultado == "FALHA") {
                fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                return false;
              } else if (resultado == "OK") { 
                if ( Dados.Nome ) {       


                    try {
                        $("#txtNome").val( Dados.Nome );
                        $("#txtChatId").val( Dados.ChaId );
                        $("#txtEmail").val( Dados.Email );
                        ///$("#txtCeiCPF").val( Dados.Cpf );
                        $("#txtCeiCPF").val( FormatarCPFCNPJ(Dados.Cpf) );
                      } catch (e) {
                      }

                    try {
                        CeiSit = Dados.Status;
                        $("#txtDetCeiSitDescr").removeClass("text-muted");
                        $("#txtDetCeiSitDescr").removeClass("text-success");
                        $("#txtDetCeiSitDescr").removeClass("text-danger");
                        if(CeiSit == "A"){
                            $("#txtDetCeiSitDescr").html('Habilitada');
                            $("#txtDetCeiSitDescr").addClass('text-success');
                        } else if(CeiSit == "I"){
                            $("#txtDetCeiSitDescr").html('Desabilitada');
                            $("#txtDetCeiSitDescr").addClass('text-danger');
                        } else{
                            $("#txtDetCeiSitDescr").html('Desconhedida');
                            $("#txtDetCeiSitDescr").addClass('table-muted');
                        }
                      } catch (e) {
                      }

                    if (  Dados.Foto  && Dados.Foto != "" ) $("#imgPerfil").attr('src',  urlPadrao + Dados.Foto );
                    if (  !Dados.Foto || Dados.Foto == "" ) $("#imgPerfil").attr('src',  urlPadrao + "static/pages/img/pessoa-icon.png" );

                } else {;
                  fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                  return;
                }
              } else {
                fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                return false;
              }
              
          },
          error: function(data) {
          fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
          return;
          }
        });
        

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
	
  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	return;
  }
}

function fSalvarPerfil( urlPadrao ){
  try {

       promise = new Promise( (resolve, reject) => {

          fLimparAreaAlertaPrinc();
          
          var txtNome   = $("#txtNome").val(); 
          var txtChatId = $("#txtChatId").val(); 
          var txtEmail  = $("#txtEmail").val(); 
         
           if( txtNome == "" ){
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Nome não informado!'); 
              return;
           }
           if( txtEmail == "" ){
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'E-mail não informado!'); 
              return;
           }

          $.ajax({
            cache   : "false",
            dataType: "json",
            async   : true,
            type    : "POST",
          url     : urlPadrao + "perfil/salvarDados",
          data    : { txtNome: txtNome, txtChatId: txtChatId, txtEmail: txtEmail, },
            success: function(result) {  

              var resultado = result.data.Resultado; 
              var mensagem  = result.data.Mensagem; 

              if (resultado == "NSESSAO") {
                $(location).attr('href', urlPadrao + '/login');
                return false;
               } else if (resultado == "NOK") {
                fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
                return;
              } else if (resultado == "OK") {
                fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados Salvo!'); 
              } else {
                fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                return;
              }
          
            },
            error: function(data) {
              fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
          return;
            }
          });

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
	
  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	return;
  }
}

 $(document).on('change', ':file', function() {
	//$('#imgPerfil').attr('src', "");	
	var input = $(this);
	var numFiles = input.get(0).files ? input.get(0).files.length : 1;
	var label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
	input.trigger('fileselect', [numFiles, label]);		
	readImgUrlAndPreview(this);		
	function readImgUrlAndPreview(input){
		 if (input.files && input.files[0]) {
				var reader = new FileReader();
				reader.onload = function (e) {			            	
          $('#imgPerfil').attr('src', e.target.result);
          $('#imgPerfilPag').attr('src', e.target.result);
					}
			  };
			  reader.readAsDataURL(input.files[0]);
		 }	
});

function fSalvarSenha( urlPadrao ){
  try {

       promise = new Promise( (resolve, reject) => {

          
          fLimparAreaAlertaPrinc();
          
          var txtSenhaAtual    = $("#txtSenhaAtual").val(); 
           var txtNovaSenha     = $("#txtNovaSenha").val(); 
           var txtConfirmaSenha = $("#txtConfirNovaSenha").val(); 

           if( txtSenhaAtual == "" ){
            fCriarAlertaPrinc(TP_ALERTA_AVISO,'Senha Atual não informada!');
            return;
           }
           if( txtNovaSenha == "" ){
            fCriarAlertaPrinc(TP_ALERTA_AVISO,'Nova Senha não informada!');
            return;
           }
           if( txtConfirmaSenha == "" ){
            fCriarAlertaPrinc(TP_ALERTA_AVISO,'Confirma&ccedil;ão de Senha não informada!');
            return;
           }
           if( txtSenhaAtual == txtNovaSenha ){
            fCriarAlertaPrinc(TP_ALERTA_AVISO,'Nova Senha e Senha Atual são iguais.');
            return;
           }   
           if( txtNovaSenha != txtConfirmaSenha ){
            fCriarAlertaPrinc(TP_ALERTA_AVISO,'Nova Senha e Confirmar Senha não são iguais.');
            return;
           }   

          $.ajax({
            cache   : "false",
            dataType: "json",
            async   : true,
            type    : "POST",
            url     : urlPadrao + "perfil/salvarSenha",
            data    : { txtSenhaAtual : txtSenhaAtual, txtNovaSenha  : txtNovaSenha    },
            success: function(result) {  

                var resultado = result.data.Resultado; 
                var mensagem  = result.data.Mensagem; 

                if (resultado == "NSESSAO") {
                  $(location).attr('href', urlPadrao + '/login');
                  return false;
                } else if (resultado == "NOK") {
                  fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
                    return;
                } else if (resultado == "OK") {
                    fLimparDadosSenha( urlPadrao );
                    fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Senha Salva!');
                } else {
                    fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
                    return;
                }
          
            },
            error: function(data) {
              fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
          return;
            }
          });

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
	
  } catch (e) {
   fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	return;
  }
}

function iniciarAnimacaoResetar() {
  $("#iRefreshResetarOperac").removeClass("fa-trash-o");
  $("#iRefreshResetarOperac").addClass("fa-refresh");
  $("#iRefreshResetarOperac").addClass("fa-spin");
  $("#btnResetarOperac").addClass("disabled");
}

function finalizarAnimacaoResetar() {
  $("#iRefreshResetarOperac").removeClass("fa-spin");
  $("#iRefreshResetarOperac").removeClass("fa-refresh");
  $("#iRefreshResetarOperac").addClass("fa-trash-o");
  $("#btnResetarOperac").removeClass("disabled");
}

function fResetarOperac( urlPadrao ){
  try {

       promise = new Promise( (resolve, reject) => {

            fLimparAreaAlertaPrinc();
            
            var SenhaResetar = $("#txtSenhaResetar").val(); 

             if( SenhaResetar == "" ){
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Senha não informada!');
              return;
             }

            finalizarAnimacaoResetar();
            iniciarAnimacaoResetar();

            $.ajax({
              cache   : "false",
              dataType: "json",
              async   : true,
              type    : "POST",
              url     : urlPadrao + "perfil/resetarOperac",
              data    : { SenhaResetar : SenhaResetar },
              success: function(result) {  

                var resultado = result.data.Resultado; 
                var mensagem  = result.data.Mensagem; 

                if (resultado == "NSESSAO") {
                  $(location).attr('href', urlPadrao + '/login');
                  return false;
                } else if (resultado == "NOK") {
                  fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
                  return;
                } else if (resultado == "OK") {
                  fLimparDadosSenha( urlPadrao );
                  fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Todas as Operações/Proventos foram Excluídos!');
                  finalizarAnimacaoResetar();
                } else {
                  fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
                  return;
                }

              },
              error: function(data) {
                fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
                return;
              }
            });

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
	
  } catch (e) {
     fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	return;
  }
}

function fImportarFoto(urlPadrao) {
    try {

         promise = new Promise( (resolve, reject) => {

              fLimparAreaAlertaPrinc();
            
              var filePath = $("#txtFoto");

              if ( filePath.val().trim() == '' ) {
                fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Nenhuma imagem selecionada para importação.');
                return false;
              }

              // var fileType = ['jpg', 'png', 'gif'];
              // var regex    = new RegExp("([a-zA-Z0-9\s_\\.\-:])+("+ fileType + ")$");
              // if ( !regex.test( filePath.val().toLowerCase() ) ) {
              //   fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_AVISO, 'Tipo de Imagem inválida para importação.');
              //   return false;
              // }

              // alert("Size: " + filePath[0].files[0].size);
              // if(typeof extPermitidas.find(function(ext){ return fileInput.val().split('.').pop() == ext; }) == 'undefined')
              //var validos = /(\.jpg|\.png|\.gif|\.pdf|\.txt|\.doc|\.docx)$/i;
              // if (!validos.test(nome)) {

              var formData = new FormData(); 
              formData.append("arquivo", filePath[0].files[0] );

              $.ajax({
                  dataType: "json", 
                  type: "POST",
                  url: urlPadrao + "perfil/importarfoto",
                  data: formData,
                  processData: false,
                  contentType: false,
                  cache: false,
                  timeout: 600000,
                  success: function(result) {
                  
                      var resultado = result.data.Resultado;
                      var mensagem  = result.data.Mensagem;
                  
                      if (resultado == "NSESSAO") {
                          $(location).attr("href", urlPadrao + "/login");
                          return false;
                      } else if (resultado == "NOK") {
                        fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
                          return false;
                      } else if (resultado == "FALHA") {
                        fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
                          return;
                      } else if (resultado == "OK") {
                          filePath.val('');
                          fCriarAlertaPrinc(TP_ALERTA_SUCESSO, mensagem);
                          //fCarregarDados( urlPadrao );
                          return true;
                      } else {
                        fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
                          return false;
                      }
                  },
                  error: function (request, status, error) { //error: function(data) {  //error: function (request, status, error) {
                      finalizarAnimacaImportar();
                      fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText //MSG_ALERTA_ERRO
                  }
              });

          resolve(true);
          // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
        })
        .then( txt => {
          //console.log('Sucesso: ' + txt);
        })
        .catch( txt => {
          fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
        });

    } catch (e) {
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
        return;
    }
}

function iniciarAnimacaoSalvarCei() {
  $("#iSalvarCei").removeClass("fa-check");
  $("#iSalvarCei").addClass("fa-spinner");
  $("#iSalvarCei").addClass("fa-pulse");
  $("#btnSalvarCei").addClass("disabled");
}

function finalizarAnimacaoSalvarCei() {
  $("#iSalvarCei").removeClass("fa-spinner");
  $("#iSalvarCei").removeClass("fa-pulse");
  $("#iSalvarCei").addClass("fa-check");
  $("#btnSalvarCei").removeClass("disabled");
}

function fSalvarDadosCei( urlPadrao ){
  try {

       promise = new Promise( (resolve, reject) => {

          fLimparAreaAlertaPrinc();
          finalizarAnimacaoSalvarCei();
          iniciarAnimacaoSalvarCei();
          
          var txtCPF   = tirarFormacataoCPFCNPJ( $("#txtCeiCPF").val().trim() ); 
          var txtSenha = $("#txtCeiSenha").val().trim(); 

          if( txtCPF != ""){
             
             if( !ValidarCPF( document.getElementById('txtCeiCPF') ) ){
                finalizarAnimacaoSalvarCei();
                fCriarAlertaPrinc(TP_ALERTA_AVISO, 'CPF inválido!'); 
                return;
             }

             if( txtSenha == "" ){
                finalizarAnimacaoSalvarCei();
                fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Senha não informada!'); 
                return;
             }

          }

           if( txtSenha != "" ){
                if( txtCPF == ""){
                  finalizarAnimacaoSalvarCei();
                  fCriarAlertaPrinc(TP_ALERTA_AVISO, 'CPF não informado!'); 
                  return;
                } 
           }

          $.ajax({
            cache   : "false",
            dataType: "json",
            async   : true,
            type    : "POST",
            url     : urlPadrao + "cei/salvar",
            data    : { txtCPF: txtCPF, txtSenha: txtSenha },
            success: function(result) {  

              finalizarAnimacaoSalvarCei();

              var resultado = result.data.Resultado; 
              var mensagem  = result.data.Mensagem; 
              var Dados     = result.data.Dados; 

              if (resultado == "NSESSAO") {
                  $(location).attr('href', urlPadrao + '/login');
                  return false;
               } else if (resultado == "NOK") {
                  fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
                  return;
              } else if (resultado == "OK") {

                  CeiSit = Dados.Sit;

                  $("#txtDetCeiSitDescr").removeClass("text-muted"); 
                  $("#txtDetCeiSitDescr").removeClass("text-success");
                  $("#txtDetCeiSitDescr").removeClass("text-danger"); 

                  if(CeiSit == "A"){
                      $("#txtDetCeiSitDescr").html('Habilitada');
                      $("#txtDetCeiSitDescr").addClass('text-success');
                  } else if(CeiSit == "I"){
                      $("#txtDetCeiSitDescr").html('Desabilitada');
                      $("#txtDetCeiSitDescr").addClass('text-danger');
                  } else{
                      $("#txtDetCeiSitDescr").html('Desconhedida');
                      $("#txtDetCeiSitDescr").addClass('table-muted');
                  }        

                fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados Salvo!'); 
              } else {
                fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                return;
              }
          
            },
            error: function(data) {
              finalizarAnimacaoSalvarCei();
              fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
          return;
            }
          });

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        finalizarAnimacaoSalvarCei();
        fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    finalizarAnimacaoSalvarCei();
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  return;
  }
}


function fLimparDadosAlertas( urlPadrao ){

  $('#chk_E_TODOS').attr('checked', false);
  $('#chk_T_TODOS').attr('checked', false);

  $('#chk_E_LOGIN_01').attr('checked', false);
  $('#chk_T_LOGIN_01').attr('checked', false);
  $('#chk_E_LOGIN_02').attr('checked', false);
  $('#chk_T_LOGIN_02').attr('checked', false);
  $('#chk_E_LOGIN_03').attr('checked', false);
  $('#chk_T_LOGIN_03').attr('checked', false);

  $('#chk_E_PERFIL_01').attr('checked', false);
  $('#chk_T_PERFIL_01').attr('checked', false);
  $('#chk_E_PERFIL_02').attr('checked', false);
  $('#chk_T_PERFIL_02').attr('checked', false);  
  $('#chk_E_PERFIL_03').attr('checked', false);
  $('#chk_T_PERFIL_03').attr('checked', false);
  $('#chk_E_PERFIL_04').attr('checked', false);
  $('#chk_T_PERFIL_04').attr('checked', false);

  $('#chk_E_PORTFOLIO_01').attr('checked', false);
  $('#chk_T_PORTFOLIO_01').attr('checked', false);

  $('#chk_E_PROVENTOS_01').attr('checked', false);
  $('#chk_T_PROVENTOS_01').attr('checked', false);
  $('#chk_E_PROVENTOS_02').attr('checked', false);
  $('#chk_T_PROVENTOS_02').attr('checked', false);
  $('#chk_E_PROVENTOS_03').attr('checked', false);
  $('#chk_T_PROVENTOS_03').attr('checked', false);

  $('#chk_E_CEI_01').attr('checked', false);
  $('#chk_T_CEI_01').attr('checked', false);
  $('#chk_E_CEI_02').attr('checked', false);
  $('#chk_T_CEI_02').attr('checked', false);
  $('#chk_E_CEI_03').attr('checked', false);
  $('#chk_T_CEI_03').attr('checked', false);

  $('#chk_E_FATOS_01').attr('checked', false);
  $('#chk_T_FATOS_01').attr('checked', false);
  $('#chk_E_FATOS_02').attr('checked', false);
  $('#chk_T_FATOS_02').attr('checked', false);
  $('#chk_E_FATOS_03').attr('checked', false);
  $('#chk_T_FATOS_03').attr('checked', false);
  $('#chk_E_FATOS_04').attr('checked', false);
  $('#chk_T_FATOS_04').attr('checked', false);
  $('#chk_E_FATOS_05').attr('checked', false);
  $('#chk_T_FATOS_05').attr('checked', false);
  $('#chk_E_FATOS_06').attr('checked', false);
  $('#chk_T_FATOS_06').attr('checked', false);
  $('#chk_E_FATOS_07').attr('checked', false);
  $('#chk_T_FATOS_07').attr('checked', false);
  $('#chk_E_FATOS_08').attr('checked', false);
  $('#chk_T_FATOS_08').attr('checked', false);
  $('#chk_E_FATOS_09').attr('checked', false);
  $('#chk_T_FATOS_09').attr('checked', false);

  $('#chk_E_NOTICIA_01').attr('checked', false);
  $('#chk_T_NOTICIA_01').attr('checked', false);
  $('#chk_E_NOTICIA_02').attr('checked', false);
  $('#chk_T_NOTICIA_02').attr('checked', false);
  $('#chk_E_NOTICIA_03').attr('checked', false);
  $('#chk_T_NOTICIA_03').attr('checked', false);
  $('#chk_E_NOTICIA_04').attr('checked', false);
  $('#chk_T_NOTICIA_04').attr('checked', false);
  $('#chk_E_NOTICIA_05').attr('checked', false);
  $('#chk_T_NOTICIA_05').attr('checked', false);
  $('#chk_E_NOTICIA_06').attr('checked', false);
  $('#chk_T_NOTICIA_06').attr('checked', false);
  $('#chk_E_NOTICIA_07').attr('checked', false);
  $('#chk_T_NOTICIA_07').attr('checked', false);
  $('#chk_E_NOTICIA_08').attr('checked', false);
  $('#chk_T_NOTICIA_08').attr('checked', false);
  $('#chk_E_NOTICIA_09').attr('checked', false);
  $('#chk_T_NOTICIA_09').attr('checked', false);
  $('#chk_E_NOTICIA_10').attr('checked', false);
  $('#chk_T_NOTICIA_10').attr('checked', false);
  $('#chk_E_NOTICIA_11').attr('checked', false);
  $('#chk_T_NOTICIA_11').attr('checked', false);
  $('#chk_E_NOTICIA_12').attr('checked', false);
  $('#chk_T_NOTICIA_12').attr('checked', false);
  $('#chk_E_NOTICIA_13').attr('checked', false);
  $('#chk_T_NOTICIA_13').attr('checked', false);
  $('#chk_E_NOTICIA_14').attr('checked', false);
  $('#chk_T_NOTICIA_14').attr('checked', false);
  $('#chk_E_NOTICIA_15').attr('checked', false);
  $('#chk_T_NOTICIA_15').attr('checked', false);
  $('#chk_E_NOTICIA_16').attr('checked', false);
  $('#chk_T_NOTICIA_16').attr('checked', false);
  $('#chk_E_NOTICIA_17').attr('checked', false);
  $('#chk_T_NOTICIA_17').attr('checked', false);
  $('#chk_E_NOTICIA_18').attr('checked', false);
  $('#chk_T_NOTICIA_18').attr('checked', false);
  $('#chk_E_NOTICIA_19').attr('checked', false);
  $('#chk_T_NOTICIA_19').attr('checked', false);
  $('#chk_E_NOTICIA_20').attr('checked', false);
  $('#chk_T_NOTICIA_20').attr('checked', false);
  $('#chk_E_NOTICIA_21').attr('checked', false);
  $('#chk_T_NOTICIA_21').attr('checked', false);
  $('#chk_E_NOTICIA_22').attr('checked', false);
  $('#chk_T_NOTICIA_22').attr('checked', false);
  $('#chk_E_NOTICIA_23').attr('checked', false);
  $('#chk_T_NOTICIA_23').attr('checked', false);
  $('#chk_E_NOTICIA_24').attr('checked', false);
  $('#chk_T_NOTICIA_24').attr('checked', false);
  $('#chk_E_NOTICIA_25').attr('checked', false);
  $('#chk_T_NOTICIA_25').attr('checked', false);
  $('#chk_E_NOTICIA_26').attr('checked', false);
  $('#chk_T_NOTICIA_26').attr('checked', false);
  $('#chk_E_NOTICIA_27').attr('checked', false);
  $('#chk_T_NOTICIA_27').attr('checked', false);
  $('#chk_E_NOTICIA_28').attr('checked', false);
  $('#chk_T_NOTICIA_28').attr('checked', false);
  $('#chk_E_NOTICIA_29').attr('checked', false);
  $('#chk_T_NOTICIA_29').attr('checked', false);
  $('#chk_E_NOTICIA_30').attr('checked', false);
  $('#chk_T_NOTICIA_30').attr('checked', false);
  $('#chk_E_NOTICIA_31').attr('checked', false);
  $('#chk_T_NOTICIA_31').attr('checked', false);
  $('#chk_E_NOTICIA_32').attr('checked', false);
  $('#chk_T_NOTICIA_32').attr('checked', false);
  $('#chk_E_NOTICIA_33').attr('checked', false);
  $('#chk_T_NOTICIA_33').attr('checked', false);
  $('#chk_E_NOTICIA_34').attr('checked', false);
  $('#chk_T_NOTICIA_34').attr('checked', false);
  $('#chk_E_NOTICIA_35').attr('checked', false);
  $('#chk_T_NOTICIA_35').attr('checked', false);
  $('#chk_E_NOTICIA_36').attr('checked', false);
  $('#chk_T_NOTICIA_36').attr('checked', false);
  $('#chk_E_NOTICIA_37').attr('checked', false);
  $('#chk_T_NOTICIA_37').attr('checked', false);
  $('#chk_E_NOTICIA_38').attr('checked', false);
  $('#chk_T_NOTICIA_38').attr('checked', false);
  $('#chk_E_NOTICIA_39').attr('checked', false);
  $('#chk_T_NOTICIA_39').attr('checked', false);
  $('#chk_E_NOTICIA_40').attr('checked', false);
  $('#chk_T_NOTICIA_40').attr('checked', false);
  $('#chk_E_NOTICIA_41').attr('checked', false);
  $('#chk_T_NOTICIA_41').attr('checked', false);
  $('#chk_E_NOTICIA_42').attr('checked', false);
  $('#chk_T_NOTICIA_42').attr('checked', false);
  $('#chk_E_NOTICIA_43').attr('checked', false);
  $('#chk_T_NOTICIA_43').attr('checked', false);
  $('#chk_E_NOTICIA_44').attr('checked', false);
  $('#chk_T_NOTICIA_44').attr('checked', false);
  $('#chk_E_NOTICIA_45').attr('checked', false);
  $('#chk_T_NOTICIA_45').attr('checked', false);
  $('#chk_E_NOTICIA_46').attr('checked', false);
  $('#chk_T_NOTICIA_46').attr('checked', false);
  $('#chk_E_NOTICIA_47').attr('checked', false);
  $('#chk_T_NOTICIA_47').attr('checked', false);
  $('#chk_E_NOTICIA_48').attr('checked', false);
  $('#chk_T_NOTICIA_48').attr('checked', false);
  $('#chk_E_NOTICIA_49').attr('checked', false);
  $('#chk_T_NOTICIA_49').attr('checked', false);
  $('#chk_E_NOTICIA_50').attr('checked', false);
  $('#chk_T_NOTICIA_50').attr('checked', false);
  $('#chk_E_NOTICIA_51').attr('checked', false);
  $('#chk_T_NOTICIA_51').attr('checked', false);
  $('#chk_E_NOTICIA_52').attr('checked', false);
  $('#chk_T_NOTICIA_52').attr('checked', false);
  $('#chk_E_NOTICIA_53').attr('checked', false);
  $('#chk_T_NOTICIA_53').attr('checked', false);
  $('#chk_E_NOTICIA_54').attr('checked', false);
  $('#chk_T_NOTICIA_54').attr('checked', false);
  $('#chk_E_NOTICIA_55').attr('checked', false);
  $('#chk_T_NOTICIA_55').attr('checked', false);
  $('#chk_E_NOTICIA_56').attr('checked', false);
  $('#chk_T_NOTICIA_56').attr('checked', false);
  $('#chk_E_NOTICIA_99').attr('checked', false);
  $('#chk_T_NOTICIA_99').attr('checked', false);

}

function fCarregarDadosAlertas( urlPadrao ){
  try {

       promise = new Promise( (resolve, reject) => {

        fLimparAreaAlertaPrinc();

        fLimparDadosAlertas( urlPadrao );
        
        $.ajax({
          cache   : "false",
          dataType: "json",
          async   : true,
          type    : "POST",
          url     : urlPadrao + "alerta/carregarassinaturas",
          success: function(result) {  
          
              var resultado = result.data.Resultado; 
              var mensagem  = result.data.Mensagem; 
              var lista     = result.data.Lista; 
              
              if (resultado == "NSESSAO") {
                $(location).attr('href', urlPadrao + '/login');
                return false;
              } else if (resultado == "NOK") {
                fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
                return false;
              } else if (resultado == "FALHA") {
                fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                return false;
              } else if (resultado == "OK") { 

                  if ( lista && lista.length > 0 ){
                    $.each(lista, function (index, value) {
                       try {
                         var tipo_assinatura = value[0].toString(); // 0-TipoAssinatura
                         var tipo_alerta     = value[1].toString().replace('-', '_'); // 1-TipoAlerta
                         var situacao        = value[2].toString(); // 2-Situacao
                         $('#chk_'+tipo_assinatura+'_'+tipo_alerta).attr("checked", (situacao == "A"));
                       } catch (e) {
                         // faz nada
                       }
                    });  
                  }

                  // verificar se todos com check true
                  var checkTodosEmail    = true;  
                  var checkTodosTelegram = true;  

                  $(".material-switch").each(function() { 
                    var id_alerta       = $(this).children().attr('id').replace('chk_', '');
                    var tipo_assinatura = id_alerta.toString().substring(0, 1); // pegar somente o primeiro digito do id alerta
                    var tipo_alerta     = id_alerta.toString().substring(2, id_alerta.toString().length ).replace('_', '-'); // pegar todos digitos do id alerta a partir do terceiro item, ou segundo indice
                    var situacao        = $(this).children().is(":checked") == true ? "A" : "I"; // setar A-Ativo para cheche true, ou I-Inativo para check false
                    if ( tipo_alerta != 'TODOS' && situacao == 'I' ){
                        if ( tipo_assinatura == 'E' ) checkTodosEmail    = false;  
                        if ( tipo_assinatura == 'T' ) checkTodosTelegram = false;  
                    }
                  }); 

                  $('#chk_E_TODOS').attr('checked', checkTodosEmail    );
                  $('#chk_T_TODOS').attr('checked', checkTodosTelegram );

                  return;
              } else {
                fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                return false;
              }
              
          },
          error: function(data) {
          fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
          return;
          }
        });
        

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  return;
  }
}


function fSalvarDadosAlertas(urlPadrao, tipo_assinatura, tipo_alerta, situacao ){
  try {

       promise = new Promise( (resolve, reject) => {

           if( tipo_alerta == "" ){
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Tipo Alerta não informado!'); 
              return;
           }

           if( tipo_assinatura == "" ){
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Tipo Assinatura não informado!'); 
              return;
           }

           if( situacao == "" ){
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Situação não informada!'); 
              return;
           }

          $.ajax({
            cache   : "false",
            dataType: "json",
            async   : true,
            type    : "POST",
            url     : urlPadrao + "alerta/salvarassinatura",
            data    : { tipo_assinatura: tipo_assinatura, tipo_alerta: tipo_alerta, situacao: situacao },
            success: function(result) {  

              var resultado = result.data.Resultado; 
              var mensagem  = result.data.Mensagem; 

              if (resultado == "NSESSAO") {
                  $(location).attr('href', urlPadrao + '/login');
                  return false;
               } else if (resultado == "NOK") {
                  fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
                  return;
              } else if (resultado == "OK") {
                // fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados Salvo!'); 
              } else {
                fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                return;
              }
          
            },
            error: function(data) {
              fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
          return;
            }
          });

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    return;
  }
}
