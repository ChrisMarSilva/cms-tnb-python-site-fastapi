function fLimparAreaAlerta(a){$("#"+a).html("")}function fLimparAreaAlertaPrinc(){fLimparAreaAlerta("AreaAlertaPrinc")}function fLimparAreaAlertaModalCad(){fLimparAreaAlerta("AreaAlertaModalCad")}function fLimparAreaAlertaModalExc(){fLimparAreaAlerta("AreaAlertaModalExc")}function fCriarAlerta(a,r,i){r==TP_ALERTA_AVISO&&showNotification("bg-info",i),r==TP_ALERTA_SUCESSO&&showNotification("bg-success",i),r==TP_ALERTA_ERRO&&showNotification("bg-danger",i),r==TP_ALERTA_ALERTA&&showNotification("bg-warning",i)}function fCriarAlertaPrinc(a,r){fCriarAlerta("AreaAlertaPrinc",a,r)}function fCriarAlertaModalCad(a,r){fCriarAlerta("AreaAlertaModalCad",a,r)}function fCriarAlertaModalExc(a,r){fCriarAlerta("AreaAlertaModalExc",a,r)}async function fRemoverMenuAtivo(){try{promise=new Promise((a,r)=>{$("#MnPrincPortfolio").hasClass("active")&&$("#MnPrincPortfolio").removeClass("active"),$("#MnPrincOperacoes").hasClass("active")&&$("#MnPrincOperacoes").removeClass("active"),$("#MnPrincComprarAtivo").hasClass("active")&&$("#MnPrincComprarAtivo").removeClass("active"),$("#MnPrincVenderAtivo").hasClass("active")&&$("#MnPrincVenderAtivo").removeClass("active"),$("#MnPrincDividendos").hasClass("active")&&$("#MnPrincDividendos").removeClass("active"),a(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fMarcarMenuAtivo(){}function fGerarNumeroAleatorio(){return Math.floor(65536*Math.random())}function chamaModalAviso(a){$("#PopModalAvisoTexto").html(a),$("#PopModalAviso").modal("show")}function chamaModalErro(a){$("#PopModalErroTexto").html(a),$("#PopModalErro").modal("show")}function chamaModalConfirmacao(a,r){$("#PopModalConfirmacaoTexto").html(a),$("#BtnModalConfirmacaoSim").attr("href",r),$("#PopModalConfirmacao").modal("show")}function iniciarAnimacaoLogin(){$("#iEntrar").removeClass("fa-sign-in"),$("#iEntrar").addClass("fa-spinner"),$("#iEntrar").addClass("fa-pulse")}function finalizarAnimacaoLogin(){$("#iEntrar").removeClass("fa-spinner"),$("#iEntrar").removeClass("fa-pulse"),$("#iEntrar").addClass("fa-sign-in")}function iniciarAnimacaoSalvar(){$("#iSalvar").removeClass("fa-check"),$("#iSalvar").addClass("fa-spinner"),$("#iSalvar").addClass("fa-pulse")}function finalizarAnimacaoSalvar(){$("#iSalvar").removeClass("fa-spinner"),$("#iSalvar").removeClass("fa-pulse"),$("#iSalvar").addClass("fa-check")}function iniciarAnimacaoExcluir(){$("#iExcluir").removeClass("fa-check"),$("#iExcluir").addClass("fa-spinner"),$("#iExcluir").addClass("fa-pulse")}function finalizarAnimacaoExcluir(){$("#iExcluir").removeClass("fa-spinner"),$("#iExcluir").removeClass("fa-pulse"),$("#iExcluir").addClass("fa-check")}function getPathPagina(){try{var a=$(location).attr("href"),r=a.lastIndexOf("/");return a.slice(0,r)}catch(a){return""}}function fTraduzirGrid(){return{sEmptyTable:"Nenhum registro encontrado",sInfo:"Mostrando de _START_ até _END_ de _TOTAL_ registros",sInfoEmpty:"Mostrando 0 até 0 de 0 registros",sInfoFiltered:"(Filtrados de _MAX_ registros)",sInfoPostFix:"",sInfoThousands:".",sLengthMenu:"Mostrar _MENU_ registros",sLoadingRecords:"Carregando...",sProcessing:"Processando...",sZeroRecords:"Nenhum registro encontrado",sSearch:"Buscar:",oPaginate:{sNext:"Próximo",sPrevious:"Anterior",sFirst:"Primeiro",sLast:"Último"},oAria:{sSortAscending:": Ordenar colunas de forma ascendente",sSortDescending:": Ordenar colunas de forma descendente"}}}function fCriarDivAlertaMsg(a,r,i,e,n){try{var o="";return o=(o+="<li>")+'    <a href="'+a+'comentarios">',o=(o+='        <div class="media">')+'            <img class="rounded-circle media-object" width="30" height="30" src="'+(a+(""!=n?n:"static/pages/img/pessoa-icon.png"))+'" alt="">',o=(o=(o+='            <div class="media-body">')+'                <span class="name" style="font-s ize: 13px;">'+r+'<span class="time" style="font-size: 9px;">'+colcarFormacataoDataHora(i)+"</span></span>")+'                <span class="message">'+e+"</span>",o+="            </div>",o+="        </div>",o+="    </a>",o+="</li>"}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fVerificarAlertaMsg(a){try{promise=new Promise((r,i)=>{var e=$("#DivMenuAlertaMsg");e.html("");var n=$("#MnPrincAlertaMsgCount");n.html(""),$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"comentarios/montarMenu",success:function(r){var i=r.data.Resultado,o=r.data.Mensagem,t=r.data.Existe,s=r.data.Lista;if("NSESSAO"==i)return $(location).attr("href",a+"/login"),!1;if("NOK"==i)return fCriarAlertaPrinc(TP_ALERTA_AVISO,o),!1;if("OK"==i){if(s.length>0&&"SIM"==t){$("#MnPrincAlertaMsg").show(),$("#MnPrincAlertaMsg").css("visibility","visible"),n.html(s.length);var c="";$.each(s,function(r,i){if(r>3)return!0;c+=fCriarDivAlertaMsg(a,i[0],i[1],i[2],i[3])}),e.html(c)}return"NAO"==t&&($("#MnPrincAlertaMsg").hide(),$("#MnPrincAlertaMsg").css("visibility","hidden")),!0}return fCriarAlertaPrinc(TP_ALERTA_ERRO,o),!1},error:function(a){return fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}),r(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fMarcarTodosAvisoComoLidos(a){try{promise=new Promise((r,i)=>{$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"comentarios/marcarTodosPend",success:function(r){var i=r.data.Resultado,e=r.data.Mensagem;return"NSESSAO"==i?($(location).attr("href",a+"/login"),!1):"NOK"==i?(fCriarAlertaPrinc(TP_ALERTA_AVISO,e),!1):"OK"==i||(fCriarAlertaPrinc(TP_ALERTA_ERRO,e),!1)},error:function(a){return fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}),r(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fCriarDivLogErros(a,r,i,e){try{var n="";return n+="<li>",n+='  <a href="javascript:void(0);">',n+='    <div class="media">',n=(n=(n+='      <div class="media-body">')+'        <span class="name">'+r+'<span class="time">'+colcarFormacataoDataHora(i)+"</span></span>")+'        <span class="message">'+e+"</span>",n+="      </div>",n+="    </div>",n+="  </a>",n+="</li>"}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fVerificarLogErros(a){try{promise=new Promise((r,i)=>{$("#DivMenuLogErros").html("");var e=$("#MnPrincLogErrosCount");e.html(""),$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"logErro/montarMenu",success:function(r){var i=r.data.Resultado,n=r.data.Mensagem,o=r.data.Existe,t=r.data.Lista;if("NSESSAO"==i)return $(location).attr("href",a+"/login"),!1;if("NOK"==i)return fCriarAlertaPrinc(TP_ALERTA_AVISO,n),!1;if("OK"==i){if("SIM"==o){$("#MnPrincLogErros").show(),$("#MnPrincLogErros").css("visibility","visible"),e.html(t.length);t.length>0&&$.each(t,function(r,i){if(r>3)return!0;fCriarDivLogErros(a,i[0],i[1],i[2])})}return"NAO"==o&&($("#MnPrincLogErros").hide(),$("#MnPrincLogErros").css("visibility","hidden")),!0}return fCriarAlertaPrinc(TP_ALERTA_ERRO,n),!1},error:function(a){return fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}),r(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function iniciarAnimacaoSair(){$("#iSair").removeClass("fa-sign-out"),$("#iSair").addClass("fa-spinner"),$("#iSair").addClass("fa-pulse"),$("#btnModalLogoutSair").addClass("disabled"),$("#btnModalLogoutCancelar").addClass("disabled")}function finalizarAnimacaoSair(){$("#iSair").removeClass("fa-spinner"),$("#iSair").removeClass("fa-pulse"),$("#iSair").addClass("fa-sign-outk"),$("#btnModalLogoutSair").removeClass("disabled"),$("#btnModalLogoutCancelar").removeClass("disabled")}function sairSistema(a){try{$.ajax({cache:"false",dataType:"json",async:!0,type:"post",url:a+"login/sair",success:function(r){try{$(location).attr("href","/login")}catch(r){$(location).attr("href",a+"/login")}},error:function(a,r,i){finalizarAnimacaoSair(),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}})}catch(a){finalizarAnimacaoSair(),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function NomeMesResumido(a){var r="";switch(a){case 1:r="JAN";break;case 2:r="FEV";break;case 3:r="MAR";break;case 4:r="ABR";break;case 5:r="MAI";break;case 6:r="JUN";break;case 7:r="JUL";break;case 8:r="AGO";break;case 9:r="SET";break;case 10:r="OUT";break;case 11:r="NOV";break;case 12:r="DEZ";break;default:r=""}return r}function trocar_tag_br(a){return a.replace(/<br>/g,"\n").replace(/(<br\/>)+/g,"\n")}NOME_PROJETO="TamoNaBolsa",MSG_ALERTA_ERRO="Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!",TP_ALERTA_AVISO="alert-info",TP_ALERTA_SUCESSO="alert-success",TP_ALERTA_ERRO="alert-danger",TP_ALERTA_ALERTA="alert-warning",$(document).ready(function(){try{$(document).keyup(function(a){27!=a.keyCode&&13!=a.keyCode||($("#PopModalAviso").modal("hide"),$("#PopModalErro").modal("hide"),$("#PopModalConfirmacao").modal("hide"),$("#PopModalLogout").modal("hide"))}),$("#BtnModalConfirmacaoSim").click(function(){$("#PopModalConfirmacao").modal("hide")})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}),function(){"use strict";window.addEventListener("load",function(){var a=document.getElementsByClassName("needs-validation");Array.prototype.filter.call(a,function(a){a.addEventListener("submit",function(r){!1===a.checkValidity()&&(r.preventDefault(),r.stopPropagation()),a.classList.add("was-validated")},!1)})},!1)}();