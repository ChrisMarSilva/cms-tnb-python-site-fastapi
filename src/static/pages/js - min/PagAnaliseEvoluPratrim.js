async function fMontaGraficoEvoluPratrimValor(r,a){try{promise=new Promise((r,e)=>{$("#DivGraficoAnaliseEvolucaoPatrimonio").html("");var t=a.length;if(t<=0)return $("#DivGraficoAnaliseEvolucaoPatrimonio").html("<br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/>"),void fCriarAlerta("AreaAlertaPrincAnaliseEvoluPratrim",TP_ALERTA_AVISO,"Sem registro.");var o=0,l=0,s=0,n=[],c=[],A=[];for(i=0;i<t;i++)n[i]=a[i][0],o=parseFloat(GetValorDecimal(a[i][1])),c[i]=o,A[i]=0,i>0&&(l=o-s,A[i]=l/s*100),s=o;Highcharts.chart("DivGraficoAnaliseEvolucaoPatrimonio",{title:{text:null},chart:{zoomType:"xy"},xAxis:{categories:n,crosshair:!0},yAxis:[{title:{text:"Total - R$",style:{color:Highcharts.getOptions().colors[1]}},labels:{format:"R$ {value:.2f}",style:{color:Highcharts.getOptions().colors[1]}}},{title:{text:"Percentual- %",style:{color:Highcharts.getOptions().colors[0]}},labels:{format:"{value:.2f}%",style:{color:Highcharts.getOptions().colors[0]}},opposite:!0}],series:[{type:"column",name:"Total Patrimônio",yAxis:1,data:c,tooltip:{pointFormatter:function(){var r=Number(this.y).toFixed(2).replace(/./g,function(r,a,i){return a>0&&"."!==r&&(i.length-a)%3==0?"X"+r:r}).replace(".",",").replace(/X/g,".");return'<span style="color:'+this.series.color+'">'+this.series.name+"</span>: <b>R$ "+r+"</b><br />"},shared:!0}},{type:"spline",name:"% Evolução",data:A,marker:{lineWidth:2,lineColor:Highcharts.getOptions().colors[3],fillColor:"white"},tooltip:{pointFormatter:function(){var r=Number(this.y).toFixed(2).replace(/./g,function(r,a,i){return a>0&&"."!==r&&(i.length-a)%3==0?"X"+r:r}).replace(".",",").replace(/X/g,".");return'<span style="color:'+this.series.color+'">'+this.series.name+"</span>: <b>"+r+"%</b><br />"},shared:!0}}]}),r(!0)}).then(r=>{}).catch(r=>{})}catch(r){null!=r.description&&fCriarAlerta("AreaAlertaPrincAnaliseEvoluPratrim",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function iniciarAnimacaoPesquisarAnaliseGrafEvoluPratrim(){$("#iRefreshEvoluPratrim").addClass("fa-spin"),$("#btnAnaliseEvoluPratrimPesquisar").addClass("disabled")}function finalizarAnimacaoPesquisaAnaliseEvoluPratrim(){$("#iRefreshEvoluPratrim").removeClass("fa-spin"),$("#btnAnaliseEvoluPratrimPesquisar").removeClass("disabled")}async function fCarregarGridAnaliseEvoluPratrim(r){try{promise=new Promise((a,i)=>{fLimparAreaAlerta("AreaAlertaPrincAnaliseEvoluPratrim"),finalizarAnimacaoPesquisaAnaliseEvoluPratrim(),iniciarAnimacaoPesquisarAnaliseGrafEvoluPratrim();var e=$("#txtFiltroAnaliseEvoluPratrimTipo").val(),t=$("#txtFiltroAnaliseEvoluPratrimAtivo").val();$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:r+"Analise/graficoEvolucaoPratrimonio",data:{TpGrafico:e,CodAtivo:t},success:function(a){finalizarAnimacaoPesquisaAnaliseEvoluPratrim();var i=a.data.Resultado,e=a.data.Mensagem,t=a.data.Lista;if("NSESSAO"==i)return $(location).attr("href",r+"/login"),!1;"NOK"!=i?"FALHA"!=i&&"OK"==i?fMontaGraficoEvoluPratrimValor(r,t):fCriarAlerta("AreaAlertaPrincAnaliseEvoluPratrim",TP_ALERTA_ERRO,e):fCriarAlerta("AreaAlertaPrincAnaliseEvoluPratrim",TP_ALERTA_AVISO,e)},error:function(r){return finalizarAnimacaoPesquisaAnaliseEvoluPratrim(),fCriarAlerta("AreaAlertaPrincAnaliseEvoluPratrim",TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}),a(!0)}).then(r=>{}).catch(r=>{})}catch(r){finalizarAnimacaoPesquisaAnaliseEvoluPratrim(),null!=r.description&&fCriarAlerta("AreaAlertaPrincAnaliseEvoluPratrim",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}