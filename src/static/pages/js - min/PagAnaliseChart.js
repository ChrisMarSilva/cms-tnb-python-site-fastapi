async function fMontaGraficoProvAnualValor(a,r){try{promise=new Promise((a,e)=>{$("#DivGraficoAnaliseEvolucaoProventos").html("");var o=r.length;if(o<=0)return $("#DivGraficoAnaliseEvolucaoProventos").html("<br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/>"),void fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",TP_ALERTA_AVISO,"Sem registro.");var n=[],t=[],s=[],l=0,A=0,c=0;for(i=0;i<o;i++)n[i]=r[i][0],l=parseFloat(GetValorDecimal(r[i][1])),t[i]=l,s[i]=0,i>0&&(A=l-c,s[i]=A/c*100),c=l;Highcharts.chart("DivGraficoAnaliseEvolucaoProventos",{title:{text:null},chart:{zoomType:"xy"},xAxis:{categories:n,crosshair:!0},yAxis:[{title:{text:"Total - R$",style:{color:Highcharts.getOptions().colors[1]}},labels:{format:"R$ {value:.2f}",style:{color:Highcharts.getOptions().colors[1]}}},{title:{text:"Percentual - %",style:{color:Highcharts.getOptions().colors[0]}},labels:{format:"{value:.2f}%",style:{color:Highcharts.getOptions().colors[0]}},opposite:!0}],series:[{type:"column",name:"Total Proventos",yAxis:1,data:t,tooltip:{pointFormatter:function(){var a=Number(this.y).toFixed(2).replace(/./g,function(a,r,e){return r>0&&"."!==a&&(e.length-r)%3==0?"X"+a:a}).replace(".",",").replace(/X/g,".");return'<span style="color:'+this.series.color+'">'+this.series.name+"</span>: <b>R$ "+a+"</b><br />"},shared:!0}},{type:"spline",name:"% Evolução",data:s,marker:{lineWidth:2,lineColor:Highcharts.getOptions().colors[3],fillColor:"white"},tooltip:{pointFormatter:function(){var a=Number(this.y).toFixed(2).replace(/./g,function(a,r,e){return r>0&&"."!==a&&(e.length-r)%3==0?"X"+a:a}).replace(".",",").replace(/X/g,".");return'<span style="color:'+this.series.color+'">'+this.series.name+"</span>: <b>"+a+"%</b><br />"},shared:!0}}]}),a(!0)}).then(a=>{}).catch(a=>{})}catch(a){null!=a.description&&fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function iniciarAnimacaoPesquisarAnaliseGrafProvAno(){$("#iRefreshGrafProvAno").addClass("fa-spin"),$("#btnAnaliseGrafProvAnoPesquisar").addClass("disabled")}function finalizarAnimacaoPesquisaAnaliseGrafProvAno(){$("#iRefreshGrafProvAno").removeClass("fa-spin"),$("#btnAnaliseGrafProvAnoPesquisar").removeClass("disabled")}async function fCarregarGraficoProvAnual(a){try{promise=new Promise((r,e)=>{fLimparAreaAlerta("AreaAlertaPrincAnaliseGrafAno"),finalizarAnimacaoPesquisaAnaliseGrafProvAno(),iniciarAnimacaoPesquisarAnaliseGrafProvAno();var i=$("#txtFiltroAnaliseGrafProvAno").val().trim();$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"Analise/graficoProvAno",data:{CodAtivo:i},success:function(r){finalizarAnimacaoPesquisaAnaliseGrafProvAno();var e=r.data.Resultado,i=r.data.Mensagem,o=r.data.Lista;if("NSESSAO"==e)return $(location).attr("href",a+"/login"),!1;"NOK"!=e?"FALHA"!=e&&"OK"==e?fMontaGraficoProvAnualValor(a,o):fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",TP_ALERTA_ERRO,i):fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",TP_ALERTA_AVISO,i)},error:function(a){return finalizarAnimacaoPesquisaAnaliseGrafProvAno(),fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}),r(!0)}).then(a=>{}).catch(a=>{})}catch(a){finalizarAnimacaoPesquisaAnaliseGrafProvAno(),null!=a.description&&fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}