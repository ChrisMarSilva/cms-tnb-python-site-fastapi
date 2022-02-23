function fBuscarListaProventos(t){try{promise=new Promise((a,r)=>{$("#DivListaCalendario").html("");var o=$("#txtFiltroCalendAtivo").val();o&&""!=o&&($("#txtFiltroCalendAtivo").prop("disabled",!0),$("#DivListaCalendario").html('<i class="fa fa-spinner fa-spin fa-3x" aria-hidden="true"> </i> <br/> <br/> <span style="font-size:12px;" class="txt-muted font-weight-bold">Carregando Proventos</span><br/> <span style="font-size:14px;" class="txt-muted font-weight-bold">'+o+"</span>"),$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:t+"calendario/grid",data:{TipoInvest:"ACAO",CodAtivo:o},success:function(a){var r=a.data.Resultado,o=a.data.Mensagem,e=a.data.Lista;if("NSESSAO"==r)return $("#DivListaCalendario").html(""),$("#txtFiltroCalendAtivo").prop("disabled",!1),$(location).attr("href",t+"/login"),!1;if("NOK"==r)return $("#DivListaCalendario").html(""),$("#txtFiltroCalendAtivo").prop("disabled",!1),void fCriarAlertaPrinc(TP_ALERTA_AVISO,o);if("FALHA"==r)return $("#DivListaCalendario").html(""),$("#txtFiltroCalendAtivo").prop("disabled",!1),void fCriarAlertaPrinc(TP_ALERTA_ERRO,o);if("OK"!=r)return $("#DivListaCalendario").html(""),$("#txtFiltroCalendAtivo").prop("disabled",!1),void fCriarAlertaPrinc(TP_ALERTA_ERRO,o);var n="";e&&e.length>0?$.each(e,function(t,a){a[0],a[1];var r=a[2],o=a[3],e=a[4],i=a[5];""!=e&&(e=colcarFormacataoData(e)),""==e&&(e="SEM PREVISÃO");var s="";if("D"==r&&(s="DIVIDENDO"),"J"==r&&(s="JRS CAP PRÓPRIO"),"R"==r&&(s="REST CAP DIN"),"E"==r&&(s="DESDOBRAMENTO"),"G"==r&&(s="GRUPAMENTO"),"B"==r&&(s="BONIFICAÇÃO"),"D"!=r&&"J"!=r&&"R"!=r||(n+=' <div class="text-center" style="border: 0px solid blue;">',n+=' <span class="font-weight-bold text-dark" style="font-size:14px;">'+s+"</span>",n+=" <br>",n+=' <span class="font-weight-bold text-secondary" style="font-size:12px;">Dt Ex: <span class="font-weight-normal text-muted" style="font-size:13px;">'+colcarFormacataoData(o)+"</span></span>",n+=" <br>",n+=' <span class="font-weight-bold text-secondary" style="font-size:12px;">Dt Pagto: <span class="font-weight-normal text-muted" style="font-size:13px;">'+e+"</span></span>",n+=" <br>",n+=' <span class="font-weight-bold text-secondary" style="font-size:12px;">Valor: <span class="font-weight-normal text-muted" style="font-size:13px;">R$ '+i.replace(".",",")+"</span></span>",n+=" </div>",n+=' <hr style="margin-top: 5px; margin-bottom: 5px;">'),"E"==r||"G"==r||"B"==r){var l=0;"E"==r&&(l=Math.round(1/i*100)),"G"==r&&(l=Math.round(1/i));var p="";"E"==r&&(p="1 para "+l),"G"==r&&(p=l+" para 1"),"B"==r&&(p=i+"%"),n+=' <div class="text-center" style="border: 0px solid blue;">',n+=' <span class="font-weight-bold text-dark" style="font-size:14px;">'+s+"</span>",n+=" <br>",n+=' <span class="font-weight-bold text-secondary" style="font-size:12px;">Dt Ex: <span class="font-weight-normal text-muted" style="font-size:13px;">'+colcarFormacataoData(o)+"</span></span>",n+=" <br>",n+=' <span class="font-weight-bold text-secondary" style="font-size:12px;">Valor: <span class="font-weight-normal text-muted" style="font-size:13px;">'+p+"</span></span>",n+=" </div>",n+=' <hr style="margin-top: 5px; margin-bottom: 5px;">'}}):n='<small style="font-size:14px;" class="font-italic text-muted">Nenhum provento encontrado...</small><br/>',$("#DivListaCalendario").html(n),$("#txtFiltroCalendAtivo").prop("disabled",!1)},error:function(t){return $("#DivListaCalendario").html(""),$("#txtFiltroCalendAtivo").prop("disabled",!1),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}),a(!0))}).then(t=>{}).catch(t=>{})}catch(t){return $("#DivListaCalendario").html(""),$("#txtFiltroCalendAtivo").prop("disabled",!1),void fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fCarregarListaProvento(t){try{promise=new Promise((a,r)=>{$("#calendar").fullCalendar({defaultDate:fDataAtual(),displayEventTime:!1,eventStartEditable:!1,height:600,contentHeight:550,weekends:!0,footer:!0,ignoreTimezone:!1,editable:!1,businessHours:!0,locale:"pt-br",titleFormat:"MMMM YYYY",defaultView:"month",monthNames:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],monthNamesShort:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],dayNames:["Domingo","Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira","Sabado"],dayNamesShort:["Dom","Seg","Ter","Qua","Qui","Sex","Sab"],header:{left:"prev,next today",center:"title",right:"month,listWeek,listDay,listMonth",close:"fa-times",prev:"fa-chevron-left",next:"fa-chevron-right",prevYear:"fa-angle-double-left",nextYear:"fa-angle-double-right"},views:{month:{titleFormat:"MMMM YYYY"},week:{titleFormat:"D MMMM YYYY"},day:{titleFormat:"ddd, d MMMM YYYY"},listDay:{buttonText:"Dia"},listWeek:{buttonText:"Semana"},listMonth:{buttonText:"Lista"}},eventLimit:!0,themeSystem:"standard",navLinks:!0,eventSources:[{textColor:"#31708f",color:"#d9edf7",backgroundColor:"#b9def0",borderColor:"#9acfea",events:function(a,r,o,e){$(".popover").popover("hide"),$.ajax({url:t+"calendario/lista",dataType:"json",cache:"false",async:!0,type:"POST",data:{TipoInvest:"ACAO",TpLista:"DTEX",DataIni:a.format("YYYYMMDD"),DataFim:r.format("YYYYMMDD")},error:function(){return fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1},success:function(a){var r=a.data.Resultado,o=a.data.Mensagem,n=a.data.Lista;if("NSESSAO"==r)return $(location).attr("href",t+"/login"),!1;if("NOK"!=r)if("FALHA"!=r)if("OK"==r){var i=[];$.each(n,function(t,a){var r,o=a[0],e="",n=a[1],s=a[2],l=a[3],p=a[4],c=a[5];"D"==s&&(e=n+" Ex Div"),"J"==s&&(e=n+" Ex JSCP"),"R"==s&&(e=n+" Ex REST CAP DIN"),r=l,i.push({id:o,start:r,title:e,codigo:n,provTipo:s,provDtEx:l,provDtPagto:p,provValor:c})}),e(i)}else fCriarAlertaPrinc(TP_ALERTA_ERRO,o);else fCriarAlertaPrinc(TP_ALERTA_ERRO,o);else fCriarAlertaPrinc(TP_ALERTA_AVISO,o)}})}},{color:"#dff0d8",textColor:"#3c763d",backgroundColor:"#c8e5bc",borderColor:"#b2dba1",events:function(a,r,o,e){$.ajax({url:t+"calendario/lista",dataType:"json",cache:"false",async:!0,type:"POST",data:{TipoInvest:"ACAO",TpLista:"DTPAGTO",DataIni:a.format("YYYYMMDD"),DataFim:r.format("YYYYMMDD")},error:function(){return fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1},success:function(a){var r=a.data.Resultado,o=a.data.Mensagem,n=a.data.Lista;if("NSESSAO"==r)return $(location).attr("href",t+"/login"),!1;if("NOK"!=r)if("FALHA"!=r)if("OK"==r){var i=[];$.each(n,function(t,a){var r,o=a[0],e="",n=a[1],s=a[2],l=a[3],p=a[4],c=a[5];"D"==s&&(e=n+" Pagto Div"),"J"==s&&(e=n+" Pagto JSCP"),"R"==s&&(e=n+" Pagto REST CAP DIN"),r=p,i.push({id:o,start:r,title:e,codigo:n,provTipo:s,provDtEx:l,provDtPagto:p,provValor:c})}),e(i)}else fCriarAlertaPrinc(TP_ALERTA_ERRO,o);else fCriarAlertaPrinc(TP_ALERTA_ERRO,o);else fCriarAlertaPrinc(TP_ALERTA_AVISO,o)}})}},{color:"#FFFFAA",textColor:"#555500",backgroundColor:"#D4D46A",borderColor:"#808015",events:function(a,r,o,e){$.ajax({url:t+"calendario/lista",dataType:"json",cache:"false",async:!0,type:"POST",data:{TipoInvest:"ACAO",TpLista:"COMPRA",DataIni:a.format("YYYYMMDD"),DataFim:r.format("YYYYMMDD")},error:function(){return fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1},success:function(a){var r=a.data.Resultado,o=a.data.Mensagem,n=a.data.Lista;if("NSESSAO"==r)return $(location).attr("href",t+"/login"),!1;if("NOK"!=r)if("FALHA"!=r)if("OK"==r){var i=[];$.each(n,function(t,a){var r,o,e=a[0],n=a[1],s=a[2],l=a[3],p=a[4],c=a[5],d=a[6];r=n+" "+s+" "+colcarFormacataoInteiro(p),o=l,i.push({id:e,start:o,title:r,codigo:n,operTipo:s,operData:l,operQuant:p,operPreco:c,operTotal:d})}),e(i)}else fCriarAlertaPrinc(TP_ALERTA_ERRO,o);else fCriarAlertaPrinc(TP_ALERTA_ERRO,o);else fCriarAlertaPrinc(TP_ALERTA_AVISO,o)}})}},{color:"#E498AF",textColor:"#4C0017",backgroundColor:"#BE5F7C",borderColor:"#4C0017",events:function(a,r,o,e){$.ajax({url:t+"calendario/lista",dataType:"json",cache:"false",async:!0,type:"POST",data:{TipoInvest:"ACAO",TpLista:"VENDA",DataIni:a.format("YYYYMMDD"),DataFim:r.format("YYYYMMDD")},error:function(){return fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1},success:function(a){var r=a.data.Resultado,o=a.data.Mensagem,n=a.data.Lista;if("NSESSAO"==r)return $(location).attr("href",t+"/login"),!1;if("NOK"!=r)if("FALHA"!=r)if("OK"==r){var i=[];$.each(n,function(t,a){var r,o,e=a[0],n=a[1],s=a[2],l=a[3],p=a[4],c=a[5],d=a[6];r=n+" "+s+" "+colcarFormacataoInteiro(p),o=l,i.push({id:e,start:o,title:r,codigo:n,operTipo:s,operData:l,operQuant:p,operPreco:c,operTotal:d})}),e(i)}else fCriarAlertaPrinc(TP_ALERTA_ERRO,o);else fCriarAlertaPrinc(TP_ALERTA_ERRO,o);else fCriarAlertaPrinc(TP_ALERTA_AVISO,o)}})}},{events:function(a,r,o,e){$.ajax({url:t+"calendario/lista",dataType:"json",cache:"false",async:!0,type:"POST",data:{TipoInvest:"ACAO",TpLista:"OUTROS",DataIni:a.format("YYYYMMDD"),DataFim:r.format("YYYYMMDD")},error:function(){return fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1},success:function(a){var r=a.data.Resultado,o=a.data.Mensagem,n=a.data.Lista;if("NSESSAO"==r)return $(location).attr("href",t+"/login"),!1;if("NOK"!=r)if("FALHA"!=r)if("OK"==r){var i=[];$.each(n,function(t,a){var r,o=a[0],e="",n=a[1],s=a[2],l=a[3],p=a[4],c=a[5];"E"==s&&(e=n+" Desdobro"),"G"==s&&(e=n+" Grupar"),"B"==s&&(e=n+" Bonificar"),r=l;var d=0;"E"==s&&(d=Math.round(1/c*100)),"G"==s&&(d=Math.round(1/c));var f="";"E"==s&&(f="1 para "+d),"G"==s&&(f=d+" para 1"),"B"==s&&(f=c+"%"),i.push({id:o,start:r,title:e,codigo:n,provTipo:s,provDtEx:l,provDtPagto:p,provValor:f})}),e(i)}else fCriarAlertaPrinc(TP_ALERTA_ERRO,o);else fCriarAlertaPrinc(TP_ALERTA_ERRO,o);else fCriarAlertaPrinc(TP_ALERTA_AVISO,o)}})}}],eventRender:function(t,a,r){a.attr("href","javascript:void(0);"),popoverElement=a.popover({html:!0,animation:!0,title:'<span class="text-muted">'+t.codigo+'</span> <button type="button" id="closepopover" class="close" onclick="fFecharPopover();">&times;</button>',container:"body",trigger:"click",placement:"top",content:function(){if($(".popover").popover("hide"),setTimeout(function(){a.popover("hide")},1e4),""!=t.provDtPagto&&(t.provDtPagto=colcarFormacataoData(t.provDtPagto)),""==t.provDtPagto&&(t.provDtPagto="SEM PREVISÃO"),t.provTipo){if("D"==t.provTipo||"J"==t.provTipo||"R"==t.provTipo){var r="";return"D"==t.provTipo&&(r="DIVIDENDO"),"J"==t.provTipo&&(r="JRS CAP PRÓPRIO"),"R"==t.provTipo&&(r="REST CAP DIN"),'<table border="0" >  <tr>    <td colspan="2" style="text-align:center;"> <span style="font-size:12px; color:gray; font-weight:bold;">'+r+'</span> </td>  </tr>  <tr>    <td style="text-align:right;"> <span style="font-size:12px; color:gray;">Data Ex:</span> </td>    <td> <span style="font-size : 12px; color:gray; font-weight:bold;">&nbsp;'+colcarFormacataoData(t.provDtEx)+'</span> </td>  </tr>  <tr>    <td style="text-align:right;">  <span style="font-size:12px; color:gray;">Data Pagto:</span> </td>    <td> <span style="font-size:12px; color:gray; font-weight:bold;">&nbsp;'+t.provDtPagto+'</span> </td>  </tr>  <tr>    <td style="text-align:right;"> <span style="font-size : 12px; color:gray;">Valor:</span> </td>    <td> <span style="font-size:12px; color:gray; font-weight:bold;">&nbsp;R$ '+t.provValor.replace(".",",")+'</span> </td>  </tr>  <tr>    <td colspan="2"> &nbsp; </td>  </tr><table>'}if("E"==t.provTipo||"G"==t.provTipo||"B"==t.provTipo){r="";return"E"==t.provTipo&&(r="DESDOBRAMENTO"),"G"==t.provTipo&&(r="GRUPAMENTO"),"B"==t.provTipo&&(r="BONIFICAÇÃO"),'<table border="0" >  <tr>    <td colspan="2" style="text-align:center;"> <span style="font-size:12px; color:gray; font-weight:bold;">'+r+'</span> </td>  </tr>  <tr>    <td style="text-align:right;"> <span style="font-size:12px; color:gray;">Data Ex:</span> </td>    <td> <span style="font-size : 12px; color:gray; font-weight:bold;">&nbsp;'+colcarFormacataoData(t.provDtEx)+'</span> </td>  </tr>  <tr>    <td style="text-align:right;"> <span style="font-size : 12px; color:gray;">Valor:</span> </td>    <td> <span style="font-size:12px; color:gray; font-weight:bold;">&nbsp;'+t.provValor.replace(".",",")+'</span> </td>  </tr>  <tr>    <td colspan="2"> &nbsp; </td>  </tr><table>'}}if(t.operTipo)return'<table border="0" >  <tr>    <td colspan="2" style="text-align:center;"> <span style="font-size:12px; color:gray; font-weight:bold;">'+t.operTipo+'</span> </td>  </tr>  <tr>    <td style="text-align:right;"> <span style="font-size:12px; color:gray;">Data:</span> </td>    <td> <span style="font-size : 12px; color:gray; font-weight:bold;">&nbsp;'+colcarFormacataoData(t.operData)+'</span> </td>  </tr>  <tr>    <td style="text-align:right;">  <span style="font-size:12px; color:gray;">Quant:</span> </td>    <td> <span style="font-size:12px; color:gray; font-weight:bold;">&nbsp;R$ '+colcarFormacataoInteiro(t.operQuant)+'</span> </td>  </tr>  <tr>    <td style="text-align:right;"> <span style="font-size : 12px; color:gray;">Preço:</span> </td>    <td> <span style="font-size:12px; color:gray; font-weight:bold;">&nbsp;R$ '+t.operPreco+'</span> </td>  </tr>  <tr>    <td style="text-align:right;"> <span style="font-size : 12px; color:gray;">Total:</span> </td>    <td> <span style="font-size:12px; color:gray; font-weight:bold;">&nbsp;R$ '+t.operTotal+'</span> </td>  </tr>  <tr>    <td colspan="2"> &nbsp; </td>  </tr><table>'}}).popover("show")}}),a(!0)}).then(t=>{}).catch(t=>{})}catch(t){return void fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fFecharPopover(){$(".popover").click(function(){$(this).popover("hide")})}