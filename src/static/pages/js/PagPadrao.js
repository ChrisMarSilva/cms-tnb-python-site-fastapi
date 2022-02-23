	
//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

NOME_PROJETO      = "TamoNaBolsa";
MSG_ALERTA_ERRO   = 'Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!';
TP_ALERTA_AVISO   = "alert-info"; //"alert-primary";
TP_ALERTA_SUCESSO = "alert-success";
TP_ALERTA_ERRO    = "alert-danger";
TP_ALERTA_ALERTA  = "alert-warning";

$(document).ready(function() {
	try {


		//fRemoverMenuAtivo();
		//fMarcarMenuAtivo();        
        
      $(document).keyup(function(e) {
        if (e.keyCode == 27 || e.keyCode == 13) {
          $("#PopModalAviso").modal(       "hide" );
          $("#PopModalErro").modal(        "hide" );
          $("#PopModalConfirmacao").modal( "hide" );
          $("#PopModalLogout").modal(      "hide" );
        }
      });

      $("#BtnModalConfirmacaoSim").click(function() {
        $("#PopModalConfirmacao").modal("hide");
      });

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
});

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fLimparAreaAlerta(IdAreaAlerta){
	$("#"+IdAreaAlerta).html("");  //$("#AreaAlerta").html(""); //$("#AreaAlerta").remove();
}
function fLimparAreaAlertaPrinc(){
	fLimparAreaAlerta("AreaAlertaPrinc");
}
function fLimparAreaAlertaModalCad(){
	fLimparAreaAlerta("AreaAlertaModalCad"); 
}
function fLimparAreaAlertaModalExc(){
	fLimparAreaAlerta("AreaAlertaModalExc"); 
}

function fCriarAlerta(IdAreaAlerta, Tipo, Mensagem){

//    var DivAlerta = $("<div/>");
//    DivAlerta.addClass( "alert alert "+Tipo+" alert-dismissible fade show" );
//    DivAlerta.attr("id", 'DivAlerta'+fGerarNumeroAleatorio());
//    DivAlerta.attr("role", "alert");
//
//    var DivAlertaContainer = $("<div/>");
//    DivAlertaContainer.addClass( "container" );
//    DivAlertaContainer.append( '<button type="button" class="close" data-dismiss="alert" aria-label="Close"> <span aria-hidden="true">&times;</span> </button>' );
//
//    if( Tipo == TP_ALERTA_AVISO   ) DivAlertaContainer.append( '<small> <strong>Aviso:</strong> ' +Mensagem+'</small> ' );
//    if( Tipo == TP_ALERTA_SUCESSO ) DivAlertaContainer.append( '<small> <strong>OK:</strong> '    +Mensagem+'</small> ' );
//    if( Tipo == TP_ALERTA_ERRO    ) DivAlertaContainer.append( '<small> <strong>Erro:</strong> '  +Mensagem+'</small> ' );
//    if( Tipo == TP_ALERTA_ALERTA  ) DivAlertaContainer.append( '<small> <strong>Alerta:</strong> '+Mensagem+'</small> ' );
//
//    DivAlerta.append( DivAlertaContainer );
//    DivAlerta.delay(5000).fadeOut("slow", function () { $(this).remove(); });
//
//    $("#"+IdAreaAlerta).append( DivAlerta );

    if( Tipo == TP_ALERTA_AVISO   ) showNotification('bg-info', Mensagem);
    if( Tipo == TP_ALERTA_SUCESSO ) showNotification('bg-success', Mensagem);
    if( Tipo == TP_ALERTA_ERRO    ) showNotification('bg-danger', Mensagem);
    if( Tipo == TP_ALERTA_ALERTA  ) showNotification('bg-warning', Mensagem);

}

function fCriarAlertaPrinc(Tipo, Mensagem){
	fCriarAlerta("AreaAlertaPrinc",Tipo, Mensagem);
}
function fCriarAlertaModalCad(Tipo, Mensagem){
	fCriarAlerta("AreaAlertaModalCad",Tipo, Mensagem);
}
function fCriarAlertaModalExc(Tipo, Mensagem){
	fCriarAlerta("AreaAlertaModalExc",Tipo, Mensagem);
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

async function fRemoverMenuAtivo() {	
	try {

       promise = new Promise( (resolve, reject) => {

        if( $('#MnPrincPortfolio').hasClass('active') )
          $("#MnPrincPortfolio").removeClass("active");   
        if( $('#MnPrincOperacoes').hasClass('active') )
          $("#MnPrincOperacoes").removeClass("active");   
        if( $('#MnPrincComprarAtivo').hasClass('active') )
          $("#MnPrincComprarAtivo").removeClass("active");    
        if( $('#MnPrincVenderAtivo').hasClass('active') )
          $("#MnPrincVenderAtivo").removeClass("active");   
        if( $('#MnPrincDividendos').hasClass('active') )
          $("#MnPrincDividendos").removeClass("active");    
        //if($('#MnPrincSair').hasClass('acrtive'))
        //  $("#MnPrincSair").removeClass("active");

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
	}
}

function fMarcarMenuAtivo() {	
	try {	
		//var URL = $(location).attr('href') || location.href || window.location.href; //http://localhost:8088/portfolio
		//var PathName = $(location).attr('pathname') || window.location.pathname; // /portfolio
		//var iUlt = PathName.split('/').length - 1;
		//PathName = PathName.split('/')[iUlt].toUpperCase();
		//alert( PathName );		
		//if( PathName == "portfolio".toUpperCase() )//	$("#MnPrincPortfolio").addClass("active");
		//if( PathName == "operacoes".toUpperCase() )//	$("#MnPrincOperacoes").addClass("active");
		//if( PathName == "comprarativo".toUpperCase() )//	$("#MnPrincComprarAtivo").addClass("active");
		//if( PathName == "venderativo".toUpperCase() )//	$("#MnPrincVenderAtivo").addClass("active");
		//if( PathName == "dividendos".toUpperCase() )//	$("#MnPrincDividendos").addClass("active");	
	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

(function() {
'use strict';
window.addEventListener('load', function() {
  var forms = document.getElementsByClassName('needs-validation');
  var validation = Array.prototype.filter.call(forms, function(form) {
	form.addEventListener('submit', function(event) {
	  if (form.checkValidity() === false) {
		event.preventDefault();
		event.stopPropagation();
	  }
	  form.classList.add('was-validated');
	}, false);
  });
}, false);
})();

function fGerarNumeroAleatorio(){
	return Math.floor(Math.random() * 65536); //entre 0 e 65536
}

function chamaModalAviso(texto) {
  $("#PopModalAvisoTexto").html(texto);
  $("#PopModalAviso").modal("show");
}

function chamaModalErro(texto) {
  $("#PopModalErroTexto").html(texto);
  $("#PopModalErro").modal("show");
}

function chamaModalConfirmacao(texto, url) {
  $("#PopModalConfirmacaoTexto").html(texto);
  $("#BtnModalConfirmacaoSim").attr("href", url); //linkSel.href
  $("#PopModalConfirmacao").modal("show");
}

function iniciarAnimacaoLogin() {
    $("#iEntrar").removeClass("fa-sign-in");
    $("#iEntrar").addClass("fa-spinner");
    $("#iEntrar").addClass("fa-pulse");
}

function finalizarAnimacaoLogin() {
   $("#iEntrar").removeClass("fa-spinner");
   $("#iEntrar").removeClass("fa-pulse");
   $("#iEntrar").addClass("fa-sign-in");
}

function iniciarAnimacaoSalvar() {
    $("#iSalvar").removeClass("fa-check");
    $("#iSalvar").addClass("fa-spinner");
    $("#iSalvar").addClass("fa-pulse");
}

function finalizarAnimacaoSalvar() {
   $("#iSalvar").removeClass("fa-spinner");
   $("#iSalvar").removeClass("fa-pulse");
   $("#iSalvar").addClass("fa-check");
}

function iniciarAnimacaoExcluir() {
    $("#iExcluir").removeClass("fa-check");
    $("#iExcluir").addClass("fa-spinner");
    $("#iExcluir").addClass("fa-pulse");
}

function finalizarAnimacaoExcluir() {
   $("#iExcluir").removeClass("fa-spinner");
   $("#iExcluir").removeClass("fa-pulse");
   $("#iExcluir").addClass("fa-check"); //fa-check-square-o
}

function getPathPagina(){
    try {
      var href = $(location).attr('href'); //  http://localhost/cms/PAG.html
      var pos = href.lastIndexOf("/");   
      var novoHref = href.slice(0, pos);  //  http://localhost/cms
	    //alert(novoHref);
      return novoHref;  
    } catch (e) {
        return "";  
    }  
}

function fTraduzirGrid(){
   return {
			"sEmptyTable": "Nenhum registro encontrado",
			"sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
			"sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
			"sInfoFiltered": "(Filtrados de _MAX_ registros)",
			"sInfoPostFix": "",
			"sInfoThousands": ".",
			"sLengthMenu": "Mostrar _MENU_ registros",
			"sLoadingRecords": "Carregando...",
			"sProcessing": "Processando...",
			"sZeroRecords": "Nenhum registro encontrado",
			"sSearch": "Buscar:",
			"oPaginate": {"sNext": "Próximo","sPrevious": "Anterior","sFirst": "Primeiro","sLast": "Último"},
			"oAria": {"sSortAscending": ": Ordenar colunas de forma ascendente","sSortDescending": ": Ordenar colunas de forma descendente"}
		}
}

function fCriarDivAlertaMsg( urlPadrao, Titulo, Hora, Texto, Foto ) {
  try { 

    var content = "";
    content = content + '<li>';
    content = content + '    <a href="'+urlPadrao+'comentarios">';
    content = content + '        <div class="media">';
    content = content + '            <img class="rounded-circle media-object" width="30" height="30" src="'+ ( urlPadrao + (( Foto != "" ) ? Foto : "static/pages/img/pessoa-icon.png") ) +'" onerror="this.onerror=null;this.src=\'/static/pages/img/pessoa-icon.png\';" alt="">';
    content = content + '            <div class="media-body">';
    content = content + '                <span class="name" style="font-s ize: 13px;">'+Titulo+'<span class="time" style="font-size: 9px;">'+colcarFormacataoDataHora(Hora) +'</span></span>';
    content = content + '                <span class="message">'+Texto+'</span>';
    content = content + '            </div>';
    content = content + '        </div>';
    content = content + '    </a>';
    content = content + '</li>';
    return content;

    } catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}

async function fVerificarAlertaMsg( urlPadrao ){
  try {

     promise = new Promise( (resolve, reject) => {

        var DivMenuAlertaMsg = $("#DivMenuAlertaMsg");         
        DivMenuAlertaMsg.html("");
        
        var MnPrincAlertaMsgCount = $("#MnPrincAlertaMsgCount");         
        MnPrincAlertaMsgCount.html("");

        $.ajax({
          cache   : "false",
          dataType: "json",
          async   : true,
          type    : "POST",
          url     : urlPadrao + "comentarios/montarMenu",
          success: function(result) {  
          
            var resultado = result.data.Resultado; 
            var mensagem  = result.data.Mensagem; 
            var Existe    = result.data.Existe;
            var lista     = result.data.Lista; 

            if (resultado == "NSESSAO") {
              $(location).attr('href', urlPadrao + '/login');
              return false;
            } else if (resultado == "NOK") {
              fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
              return false;
            } else if (resultado == "OK") {

              if ( lista.length > 0 ){
                  if (Existe == "SIM") {
                      $('#MnPrincAlertaMsg').show();
                      $("#MnPrincAlertaMsg").css("visibility","visible");
                      MnPrincAlertaMsgCount.html( lista.length );
                      var content = "";
                      //content = content + '<ul class="menu list-unstyled" style="overflow: y:auto; -webkit-overflow-scrolling: touch; width: auto; max-height: 280px; height: 280px;">';
                      $.each(lista, function (index, value) {
                          if ( index > 3 ) return true;
                          //DivMenuAlertaMsg.append( fCriarDivAlertaMsg( urlPadrao, value[0], value[1], value[2]) );
                          content = content + fCriarDivAlertaMsg( urlPadrao, value[0], value[1], value[2], value[3] );
                      });
                      //content = content + '</ul>';
                      //content = content + '<div class="slimScrollBar" style="background: rgba(0, 0, 0, 0.2); width: 3px; position: absolute; top: 0px; opacity: 0.4; display: block; border-radius: 3px; z-index: 99; right: 1px;"></div>';
                      //content = content + '<div class="slimScrollRail" style="width: 3px; height: 100%; position: absolute; top: 0px; display: none; border-radius: 0px; background: rgb(51, 51, 51); opacity: 0.2; z-index: 90; right: 1px;"></div>';
                      DivMenuAlertaMsg.html( content );
                    }
                }

                if (Existe == "NAO") {
                  $('#MnPrincAlertaMsg').hide();
                  $("#MnPrincAlertaMsg").css("visibility","hidden");
                }
              return true;
            } else {
              fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
              return false;
            }
          },
          error: function(data) {
            fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
            return false;
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
  
  } catch(e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}

async function fMarcarTodosAvisoComoLidos( urlPadrao ){
  try {

       promise = new Promise( (resolve, reject) => {

        $.ajax({
          cache   : "false",
          dataType: "json",
          async   : true,
          type    : "POST",
          url     : urlPadrao + "comentarios/marcarTodosPend",
          success: function(result) {  
          
            var resultado = result.data.Resultado; 
            var mensagem  = result.data.Mensagem; 

            if (resultado == "NSESSAO") {
              $(location).attr('href', urlPadrao + '/login');
              return false;
            } else if (resultado == "NOK") {
              fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
              return false;
            } else if (resultado == "OK") { 
              return true;
            } else {
              fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
              return false;
            }
          },
          error: function(data) {
            fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
            return false;
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
  
  } catch(e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fCriarDivLogErros( urlPadrao, Titulo, Hora, Texto ){
  try { 
    
    var content = "";
    content = content + '<li>';
    content = content + '  <a href="javascript:void(0);">';
    content = content + '    <div class="media">';
    content = content + '      <div class="media-body">';
    content = content + '        <span class="name">'+Titulo+'<span class="time">'+colcarFormacataoDataHora(Hora) +'</span></span>';
    content = content + '        <span class="message">'+Texto+'</span>';
    content = content + '      </div>';
    content = content + '    </div>';
    content = content + '  </a>';
    content = content + '</li>';
    return content;
  
    // var DivSeparador = $("<div/>");
    //     DivSeparador.addClass( "dropdown-divider" ); 
    
    // var DivLinkTitulo = $("<span/>");
    //     DivLinkTitulo.addClass( "text-danger" );
    //     DivLinkTitulo.append( "<strong>"+Titulo+" </strong>" );
    //     DivLinkTitulo.click(function() { fVerTodosErros( urlPadrao); });
    
    // var DivLinkHora = $("<span/>");
    //     DivLinkHora.addClass( "small float-right text-muted" );
    //     DivLinkHora.append( colcarFormacataoDataHora(Hora) );
    
    // var DivLinkTexto = $("<div/>");
    //     DivLinkTexto.addClass( "dropdown-message small" );
    //     //DivLinkTexto.css( "white-space", "nowrap" );
    //     //DivLinkTexto.css( "word-wrap", "break-word" );
    //     DivLinkTexto.append( Texto );
    
    // var DivLink = $("<a/>");
    //     DivLink.addClass( "dropdown-item" ); 
    //     DivLink.attr("id", 'btnLinkLogErro');
    //     DivLink.attr("href", "#");
    //     //DivLink.css( "white-space", "nowrap" );
    //     DivLink.css( "word-wrap", "break-word" );
    //     DivLink.append( DivLinkTitulo );
    //     DivLink.append( DivLinkHora );
    //     DivLink.append( DivLinkTexto );
    
    // return DivLink;   
  
    } catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}

async function fVerificarLogErros( urlPadrao ){
  try {
    
     promise = new Promise( (resolve, reject) => {

        var DivMenuLogErros = $("#DivMenuLogErros");         
        DivMenuLogErros.html("");
        
        var MnPrincLogErrosCount = $("#MnPrincLogErrosCount");         
        MnPrincLogErrosCount.html("");
        
        $.ajax({
          cache   : "false",
          dataType: "json",
          async   : true,
          type    : "POST",
          url     : urlPadrao + "logErro/montarMenu",
          success: function(result) {  
          
            var resultado = result.data.Resultado; 
            var mensagem  = result.data.Mensagem; 
            var Existe    = result.data.Existe;
            var lista     = result.data.Lista; 

            if (resultado == "NSESSAO") {
          $(location).attr('href', urlPadrao + '/login');
          return false;
        } else if (resultado == "NOK") {
              fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
              return false;
            } else if (resultado == "OK") {
              
              if (Existe == "SIM") {

                $('#MnPrincLogErros').show();
                $("#MnPrincLogErros").css("visibility","visible");
                MnPrincLogErrosCount.html( lista.length );

                var content = "";
                //content = content + '<ul class="menu list-unstyled" style="overflow: y:auto; -webkit-overflow-scrolling: touch; width: auto; max-height: 280px; height: 280px;">';
                if ( lista.length > 0 ){
                  $.each(lista, function (index, value) {
                    if ( index > 3 ) return true;
                    //DivMenuLogErros.append( fCriarDivLogErros( urlPadrao, value[0], value[1], value[2]) );
                     content = content + fCriarDivLogErros( urlPadrao, value[0], value[1], value[2]);
                  });
                }
                //content = content + '</ul>';
                //content = content + '<div class="slimScrollBar" style="background: rgba(0, 0, 0, 0.2); width: 3px; position: absolute; top: 0px; opacity: 0.4; display: block; border-radius: 3px; z-index: 99; right: 1px;"></div>';
                //content = content + '<div class="slimScrollRail" style="width: 3px; height: 100%; position: absolute; top: 0px; display: none; border-radius: 0px; background: rgb(51, 51, 51); opacity: 0.2; z-index: 90; right: 1px;"></div>';
                //DivMenuLogErros.html( content );

              }

              if (Existe == "NAO") {
                $('#MnPrincLogErros').hide();
                $("#MnPrincLogErros").css("visibility","hidden");
              }

              return true;
            } else {
              fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
              return false;
            }
          },
          error: function(data) {
            fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
            return false;
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
  
  } catch(e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function iniciarAnimacaoSair() {
  $("#iSair").removeClass("fa-sign-out");
  $("#iSair").addClass("fa-spinner");
  $("#iSair").addClass("fa-pulse");
  $("#btnModalLogoutSair").addClass("disabled");
  $("#btnModalLogoutCancelar").addClass("disabled");
}

function finalizarAnimacaoSair() {
  $("#iSair").removeClass("fa-spinner");
  $("#iSair").removeClass("fa-pulse");
  $("#iSair").addClass("fa-sign-outk");  
  $("#btnModalLogoutSair").removeClass("disabled");
  $("#btnModalLogoutCancelar").removeClass("disabled");
}


function sairSistema( urlPadrao ){
 try {

//        finalizarAnimacaoSair();
//        iniciarAnimacaoSair();

        $.ajax({
        cache    : "false",
        dataType : "json",
        async    : true,
        type     : "post",
        url      : urlPadrao + "login/sair",
        success: function(result) {
            //finalizarAnimacaoSair();
            try {
                $(location).attr('href', '/login');
            } catch (e) {
                $(location).attr('href', urlPadrao + '/login');
                //$(location).prop('href', urlPadrao + '/login');
                //location.href = urlPadrao + '/login'
            }
        },
        error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
              finalizarAnimacaoSair();
              fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); // request.responseText //MSG_ALERTA_ERRO
            }
        });

  } catch (e) {
    finalizarAnimacaoSair();
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}

function NomeMesResumido( NroMes ){
	var retorno = "";
    switch ( NroMes ) {
        case  1: retorno = "JAN"; break;
        case  2: retorno = "FEV"; break;
        case  3: retorno = "MAR"; break;
        case  4: retorno = "ABR"; break;
        case  5: retorno = "MAI"; break;
        case  6: retorno = "JUN"; break;
        case  7: retorno = "JUL"; break;
        case  8: retorno = "AGO"; break;
        case  9: retorno = "SET"; break;
        case 10: retorno = "OUT"; break;
        case 11: retorno = "NOV"; break;
        case 12: retorno = "DEZ"; break;
        default: retorno = "";
	}
	return retorno;
}  


function trocar_tag_br(str) {
    return str.replace(/<br>/g, '\n').replace(/(<br\/>)+/g, "\n");
}  
