function fMostrarEsconderValores(){$(".DivTextValor").toggle(),$(".DivIconeValor").toggle()}async function fLimparTotalizadores(a){try{promise=new Promise((a,t)=>{$("#DivPrincPortTotInvest").html("R$ 0,00"),$("#DivPrincPortTotAtual").html("R$ 0,00"),$("#DivPrincPortTotValoriz").html("R$ 0,00 <small><em>( 0.00% )</em></small>"),$("#DivPrincPortTotProv").html("R$ 0,00"),$("#DivPrincPortTotValoriz").addClass("text-muted"),$("#DivPrincPortTotValoriz").removeClass("text-success"),$("#DivPrincPortTotValoriz").removeClass("text-danger"),$("#DivPrincAcaoTotInvest").html("R$ 0,00"),$("#DivPrincAcaoTotAtual").html("R$ 0,00"),$("#DivPrincAcaoTotValoriz").html("R$ 0,00 <small><em>( 0.00% )</em></small>"),$("#DivPrincAcaoTotProv").html("R$ 0,00"),$("#DivPrincAcaoTotValoriz").addClass("text-muted"),$("#DivPrincAcaoTotValoriz").removeClass("text-success"),$("#DivPrincAcaoTotValoriz").removeClass("text-danger"),$("#DivPrincFIITotInvest").html("R$ 0,00"),$("#DivPrincFIITotAtual").html("R$ 0,00"),$("#DivPrincFIITotValoriz").html("R$ 0,00 <small><em>( 0.00% )</em></small>"),$("#DivPrincFIITotProv").html("R$ 0,00"),$("#DivPrincFIITotValoriz").addClass("text-muted"),$("#DivPrincFIITotValoriz").removeClass("text-success"),$("#DivPrincFIITotValoriz").removeClass("text-danger"),$("#DivPrincETFTotInvest").html("R$ 0,00"),$("#DivPrincETFTotAtual").html("R$ 0,00"),$("#DivPrincETFTotValoriz").html("R$ 0,00 <small><em>( 0.00% )</em></small>"),$("#DivPrincETFTotProv").html("R$ 0,00"),$("#DivPrincETFTotValoriz").addClass("text-muted"),$("#DivPrincETFTotValoriz").removeClass("text-success"),$("#DivPrincETFTotValoriz").removeClass("text-danger"),$("#DivPrincBDRTotInvest").html("R$ 0,00"),$("#DivPrincBDRTotAtual").html("R$ 0,00"),$("#DivPrincBDRTotValoriz").html("R$ 0,00 <small><em>( 0.00% )</em></small>"),$("#DivPrincBDRTotProv").html("R$ 0,00"),$("#DivPrincBDRTotValoriz").addClass("text-muted"),$("#DivPrincBDRTotValoriz").removeClass("text-success"),$("#DivPrincBDRTotValoriz").removeClass("text-danger"),a(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){null!=a.description&&fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosTotalizadores(a){try{promise=new Promise((t,e)=>{DataSetPagina={},$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"portfolio/DataSetPagina",success:function(t){var e=t.data.Resultado,o=t.data.Mensagem;t.data.Lista;return DataSetPagina=t,"NSESSAO"==e?($(location).attr("href",a+"/login"),!1):"NOK"==e?(fCriarAlertaPrinc(TP_ALERTA_AVISO,o),!1):"FALHA"==e?(fCriarAlertaPrinc(TP_ALERTA_ERRO,o),!1):"OK"!=e?(fCriarAlertaPrinc(TP_ALERTA_ERRO,o),!1):(fCarrgarDadosTotalizadoresPortfolio(a),fCarrgarDadosGraficoPortfolio(a),fCarrgarDadosTotalizadoresAcoes(a),fCarrgarDadosGraficoAcoes(a),fCarrgarDadosTotalizadoresFIIs(a),fCarrgarDadosGraficoFIIs(a),fCarrgarDadosTotalizadoresETFs(a),fCarrgarDadosGraficoETFs(a),fCarrgarDadosTotalizadoresBDRs(a),void fCarrgarDadosGraficoBDRs(a))},error:function(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}),t(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosTotalizadoresPortfolio(a){try{promise=new Promise((a,t)=>{var e=0,o=0,r=0,i=0,l=0;if(DataSetPagina&&DataSetPagina.data&&DataSetPagina.data.Lista){var n=DataSetPagina.data.Lista;n.length>0&&$.each(n,function(a,t){e+=parseFloat(GetValorDecimal(t.AtvTotInvest)),o+=parseFloat(GetValorDecimal(t.AtvTotAtual)),r+=parseFloat(GetValorDecimal(t.AtvTotValoriz)),l+=parseFloat(GetValorDecimal(t.AtvTotProv))})}0!=r&&e>0&&(i=r/e*100),$("#DivPrincPortTotInvest").html("R$ "+fMascaraValor(e)),$("#DivPrincPortTotAtual").html("R$ "+fMascaraValor(o)),$("#DivPrincPortTotValoriz").html("R$ "+fMascaraValor(r)+" <small><em>( "+fMascaraValor(i)+"% )</em></small>"),$("#DivPrincPortTotProv").html("R$ "+fMascaraValor(l)),r>0&&($("#DivPrincPortTotValoriz").removeClass("text-muted"),$("#DivPrincPortTotValoriz").addClass("text-success")),r<0&&($("#DivPrincPortTotValoriz").removeClass("text-muted"),$("#DivPrincPortTotValoriz").addClass("text-danger")),Highcharts.setOptions({global:{useUTC:!1},lang:{decimalPoint:",",thousandsSep:"."}}),Highcharts.chart("DivChartPrincPort",{lang:{months:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],shortMonths:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],weekdays:["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"],loading:["Atualizando o gráfico...aguarde"],contextButtonTitle:"Exportar gráfico",decimalPoint:",",thousandsSep:".",viewFullscreen:"Exibir em tela cheia",openInCloud:"Abri em Highcharts Cloud",downloadJPEG:"Baixar imagem JPEG",downloadPDF:"Baixar arquivo PDF",downloadPNG:"Baixar imagem PNG",downloadSVG:"Baixar vetor SVG",printChart:"Imprimir gráfico",rangeSelectorFrom:"De",rangeSelectorTo:"Para",rangeSelectorZoom:"Zoom",resetZoom:"Limpar Zoom",resetZoomTitle:"Voltar Zoom para nível 1:1"},exporting:{enabled:!1},data:{table:"datatable"},chart:{type:"column"},title:{text:null},legend:{enabled:!0},xAxis:{categories:[""],title:{text:null},labels:{enabled:!0,y:20,rotation:-45,align:"right"}},yAxis:{allowDecimals:!1,title:{text:null},labels:{style:{fontSize:"8.5px"}}},colors:["#2f7ed8","#8bbc21","#492970","#f28f43"],credits:{enabled:!1},tooltip:{pointFormatter:function(){var a=Number(this.y).toFixed(2).replace(/./g,function(a,t,e){return t>0&&"."!==a&&(e.length-t)%3==0?"X"+a:a}).replace(".",",").replace(/X/g,".");return'<span style="color:'+this.series.color+'">'+this.series.name+"</span>: <b>R$ "+a+"</b><br />"},shared:!0},series:[{name:"Tot. Investido",data:[e]},{name:"Tot. Atual",data:[o]},{name:"Total Valorização",data:[o-e]},{name:"Tot. Proventos",data:[l]}]}),a(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosTotalizadoresAcoes(a){try{promise=new Promise((a,t)=>{var e=0,o=0,r=0,i=0,l=0;if(DataSetPagina&&DataSetPagina.data&&DataSetPagina.data.Lista){var n=DataSetPagina.data.Lista;n.length>0&&$.each(n,function(a,t){t.CartId;"ACAO"==t.AtvTipoInvest&&(e+=parseFloat(GetValorDecimal(t.AtvTotInvest)),o+=parseFloat(GetValorDecimal(t.AtvTotAtual)),r+=parseFloat(GetValorDecimal(t.AtvTotValoriz)),l+=parseFloat(GetValorDecimal(t.AtvTotProv)))})}0!=r&&e>0&&(i=r/e*100),0==o&&$("#DivPrincAcao").hide(),o>0&&($("#DivPrincAcao").show(),$("#DivPrincAcaoTotInvest").html("R$ "+fMascaraValor(e)),$("#DivPrincAcaoTotAtual").html("R$ "+fMascaraValor(o)),$("#DivPrincAcaoTotValoriz").html("R$ "+fMascaraValor(r)+" <small><em>( "+fMascaraValor(i)+"% )</em></small>"),$("#DivPrincAcaoTotProv").html("R$ "+fMascaraValor(l)),r>0&&($("#DivPrincAcaoTotValoriz").removeClass("text-muted"),$("#DivPrincAcaoTotValoriz").addClass("text-success")),r<0&&($("#DivPrincAcaoTotValoriz").removeClass("text-muted"),$("#DivPrincAcaoTotValoriz").addClass("text-danger")),Highcharts.setOptions({global:{useUTC:!1},lang:{decimalPoint:",",thousandsSep:"."}}),Highcharts.chart("DivChartPrincAcao",{lang:{months:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],shortMonths:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],weekdays:["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"],loading:["Atualizando o gráfico...aguarde"],contextButtonTitle:"Exportar gráfico",decimalPoint:",",thousandsSep:".",viewFullscreen:"Exibir em tela cheia",openInCloud:"Abri em Highcharts Cloud",downloadJPEG:"Baixar imagem JPEG",downloadPDF:"Baixar arquivo PDF",downloadPNG:"Baixar imagem PNG",downloadSVG:"Baixar vetor SVG",printChart:"Imprimir gráfico",rangeSelectorFrom:"De",rangeSelectorTo:"Para",rangeSelectorZoom:"Zoom",resetZoom:"Limpar Zoom",resetZoomTitle:"Voltar Zoom para nível 1:1"},exporting:{enabled:!1},data:{table:"datatable"},chart:{type:"column"},title:{text:null},legend:{enabled:!0},xAxis:{categories:[""],title:{text:null},labels:{enabled:!0,y:20,rotation:-45,align:"right"}},yAxis:{allowDecimals:!1,title:{text:null},labels:{style:{fontSize:"8.5px"}}},colors:["#2f7ed8","#8bbc21","#492970","#f28f43"],credits:{enabled:!1},tooltip:{pointFormatter:function(){var a=Number(this.y).toFixed(2).replace(/./g,function(a,t,e){return t>0&&"."!==a&&(e.length-t)%3==0?"X"+a:a}).replace(".",",").replace(/X/g,".");return'<span style="color:'+this.series.color+'">'+this.series.name+"</span>: <b>R$ "+a+"</b><br />"},shared:!0},series:[{name:"Tot. Investido",data:[e]},{name:"Tot. Atual",data:[o]},{name:"Total Valorização",data:[o-e]},{name:"Tot. Proventos",data:[l]}]})),a(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosTotalizadoresFIIs(a){try{promise=new Promise((a,t)=>{var e=0,o=0,r=0,i=0,l=0;if(DataSetPagina&&DataSetPagina.data&&DataSetPagina.data.Lista){var n=DataSetPagina.data.Lista;n.length>0&&$.each(n,function(a,t){t.CartId;"FII"==t.AtvTipoInvest&&(e+=parseFloat(GetValorDecimal(t.AtvTotInvest)),o+=parseFloat(GetValorDecimal(t.AtvTotAtual)),r+=parseFloat(GetValorDecimal(t.AtvTotValoriz)),l+=parseFloat(GetValorDecimal(t.AtvTotProv)))})}0!=r&&e>0&&(i=r/e*100),0==o&&$("#DivPrincFII").hide(),o>0&&($("#DivPrincFII").show(),$("#DivPrincFIITotInvest").html("R$ "+fMascaraValor(e)),$("#DivPrincFIITotAtual").html("R$ "+fMascaraValor(o)),$("#DivPrincFIITotValoriz").html("R$ "+fMascaraValor(r)+" <small><em>( "+fMascaraValor(i)+"% )</em></small>"),$("#DivPrincFIITotProv").html("R$ "+fMascaraValor(l)),r>0&&($("#DivPrincFIITotValoriz").removeClass("text-muted"),$("#DivPrincFIITotValoriz").addClass("text-success")),r<0&&($("#DivPrincFIITotValoriz").removeClass("text-muted"),$("#DivPrincFIITotValoriz").addClass("text-danger")),Highcharts.setOptions({global:{useUTC:!1},lang:{decimalPoint:",",thousandsSep:"."}}),Highcharts.chart("DivChartPrincFII",{lang:{months:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],shortMonths:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],weekdays:["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"],loading:["Atualizando o gráfico...aguarde"],contextButtonTitle:"Exportar gráfico",decimalPoint:",",thousandsSep:".",viewFullscreen:"Exibir em tela cheia",openInCloud:"Abri em Highcharts Cloud",downloadJPEG:"Baixar imagem JPEG",downloadPDF:"Baixar arquivo PDF",downloadPNG:"Baixar imagem PNG",downloadSVG:"Baixar vetor SVG",printChart:"Imprimir gráfico",rangeSelectorFrom:"De",rangeSelectorTo:"Para",rangeSelectorZoom:"Zoom",resetZoom:"Limpar Zoom",resetZoomTitle:"Voltar Zoom para nível 1:1"},exporting:{enabled:!1},data:{table:"datatable"},chart:{type:"column"},title:{text:null},legend:{enabled:!0},xAxis:{categories:[""],title:{text:null},labels:{enabled:!0,y:20,rotation:-45,align:"right"}},yAxis:{allowDecimals:!1,title:{text:null},labels:{style:{fontSize:"8.5px"}}},colors:["#2f7ed8","#8bbc21","#492970","#f28f43"],credits:{enabled:!1},tooltip:{pointFormatter:function(){var a=Number(this.y).toFixed(2).replace(/./g,function(a,t,e){return t>0&&"."!==a&&(e.length-t)%3==0?"X"+a:a}).replace(".",",").replace(/X/g,".");return'<span style="color:'+this.series.color+'">'+this.series.name+"</span>: <b>R$ "+a+"</b><br />"},shared:!0},series:[{name:"Tot. Investido",data:[e]},{name:"Tot. Atual",data:[o]},{name:"Total Valorização",data:[o-e]},{name:"Tot. Proventos",data:[l]}]})),a(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosTotalizadoresETFs(a){try{promise=new Promise((a,t)=>{var e=0,o=0,r=0,i=0,l=0;if(DataSetPagina&&DataSetPagina.data&&DataSetPagina.data.Lista){var n=DataSetPagina.data.Lista;n.length>0&&$.each(n,function(a,t){t.CartId;"ETF"==t.AtvTipoInvest&&(e+=parseFloat(GetValorDecimal(t.AtvTotInvest)),o+=parseFloat(GetValorDecimal(t.AtvTotAtual)),r+=parseFloat(GetValorDecimal(t.AtvTotValoriz)),l+=parseFloat(GetValorDecimal(t.AtvTotProv)))})}0!=r&&e>0&&(i=r/e*100),0==o&&$("#DivPrincETF").hide(),o>0&&($("#DivPrincETF").show(),$("#DivPrincETFTotInvest").html("R$ "+fMascaraValor(e)),$("#DivPrincETFTotAtual").html("R$ "+fMascaraValor(o)),$("#DivPrincETFTotValoriz").html("R$ "+fMascaraValor(r)+" <small><em>( "+fMascaraValor(i)+"% )</em></small>"),$("#DivPrincETFTotProv").html("R$ "+fMascaraValor(l)),r>0&&($("#DivPrincETFTotValoriz").removeClass("text-muted"),$("#DivPrincETFTotValoriz").addClass("text-success")),r<0&&($("#DivPrincETFTotValoriz").removeClass("text-muted"),$("#DivPrincETFTotValoriz").addClass("text-danger")),$("#DivChartPrincETF").length&&(Highcharts.setOptions({global:{useUTC:!1},lang:{decimalPoint:",",thousandsSep:"."}}),Highcharts.chart("DivChartPrincETF",{lang:{months:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],shortMonths:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],weekdays:["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"],loading:["Atualizando o gráfico...aguarde"],contextButtonTitle:"Exportar gráfico",decimalPoint:",",thousandsSep:".",viewFullscreen:"Exibir em tela cheia",openInCloud:"Abri em Highcharts Cloud",downloadJPEG:"Baixar imagem JPEG",downloadPDF:"Baixar arquivo PDF",downloadPNG:"Baixar imagem PNG",downloadSVG:"Baixar vetor SVG",printChart:"Imprimir gráfico",rangeSelectorFrom:"De",rangeSelectorTo:"Para",rangeSelectorZoom:"Zoom",resetZoom:"Limpar Zoom",resetZoomTitle:"Voltar Zoom para nível 1:1"},exporting:{enabled:!1},data:{table:"datatable"},chart:{type:"column"},title:{text:null},legend:{enabled:!0},xAxis:{categories:[""],title:{text:null},labels:{enabled:!0,y:20,rotation:-45,align:"right"}},yAxis:{allowDecimals:!1,title:{text:null},labels:{style:{fontSize:"8.5px"}}},colors:["#2f7ed8","#8bbc21","#492970","#f28f43"],credits:{enabled:!1},tooltip:{pointFormatter:function(){var a=Number(this.y).toFixed(2).replace(/./g,function(a,t,e){return t>0&&"."!==a&&(e.length-t)%3==0?"X"+a:a}).replace(".",",").replace(/X/g,".");return'<span style="color:'+this.series.color+'">'+this.series.name+"</span>: <b>R$ "+a+"</b><br />"},shared:!0},series:[{name:"Tot. Investido",data:[e]},{name:"Tot. Atual",data:[o]},{name:"Total Valorização",data:[o-e]},{name:"Tot. Proventos",data:[l]}]}))),a(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosTotalizadoresBDRs(a){try{promise=new Promise((a,t)=>{var e=0,o=0,r=0,i=0,l=0;if(DataSetPagina&&DataSetPagina.data&&DataSetPagina.data.Lista){var n=DataSetPagina.data.Lista;n.length>0&&$.each(n,function(a,t){t.CartId;"BDR"==t.AtvTipoInvest&&(e+=parseFloat(GetValorDecimal(t.AtvTotInvest)),o+=parseFloat(GetValorDecimal(t.AtvTotAtual)),r+=parseFloat(GetValorDecimal(t.AtvTotValoriz)),l+=parseFloat(GetValorDecimal(t.AtvTotProv)))})}0!=r&&e>0&&(i=r/e*100),0==o&&$("#DivPrincBDR").hide(),o>0&&($("#DivPrincBDR").show(),$("#DivPrincBDRTotInvest").html("R$ "+fMascaraValor(e)),$("#DivPrincBDRTotAtual").html("R$ "+fMascaraValor(o)),$("#DivPrincBDRTotValoriz").html("R$ "+fMascaraValor(r)+" <small><em>( "+fMascaraValor(i)+"% )</em></small>"),$("#DivPrincBDRTotProv").html("R$ "+fMascaraValor(l)),r>0&&($("#DivPrincBDRTotValoriz").removeClass("text-muted"),$("#DivPrincBDRTotValoriz").addClass("text-success")),r<0&&($("#DivPrincBDRTotValoriz").removeClass("text-muted"),$("#DivPrincBDRTotValoriz").addClass("text-danger")),$("#DivChartPrincBDR").length&&(Highcharts.setOptions({global:{useUTC:!1},lang:{decimalPoint:",",thousandsSep:"."}}),Highcharts.chart("DivChartPrincBDR",{lang:{months:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],shortMonths:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],weekdays:["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"],loading:["Atualizando o gráfico...aguarde"],contextButtonTitle:"Exportar gráfico",decimalPoint:",",thousandsSep:".",viewFullscreen:"Exibir em tela cheia",openInCloud:"Abri em Highcharts Cloud",downloadJPEG:"Baixar imagem JPEG",downloadPDF:"Baixar arquivo PDF",downloadPNG:"Baixar imagem PNG",downloadSVG:"Baixar vetor SVG",printChart:"Imprimir gráfico",rangeSelectorFrom:"De",rangeSelectorTo:"Para",rangeSelectorZoom:"Zoom",resetZoom:"Limpar Zoom",resetZoomTitle:"Voltar Zoom para nível 1:1"},exporting:{enabled:!1},data:{table:"datatable"},chart:{type:"column"},title:{text:null},legend:{enabled:!0},xAxis:{categories:[""],title:{text:null},labels:{enabled:!0,y:20,rotation:-45,align:"right"}},yAxis:{allowDecimals:!1,title:{text:null},labels:{style:{fontSize:"8.5px"}}},colors:["#2f7ed8","#8bbc21","#492970","#f28f43"],credits:{enabled:!1},tooltip:{pointFormatter:function(){var a=Number(this.y).toFixed(2).replace(/./g,function(a,t,e){return t>0&&"."!==a&&(e.length-t)%3==0?"X"+a:a}).replace(".",",").replace(/X/g,".");return'<span style="color:'+this.series.color+'">'+this.series.name+"</span>: <b>R$ "+a+"</b><br />"},shared:!0},series:[{name:"Tot. Investido",data:[e]},{name:"Tot. Atual",data:[o]},{name:"Total Valorização",data:[o-e]},{name:"Tot. Proventos",data:[l]}]}))),a(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosGraficoPortfolio(a){try{promise=new Promise((a,t)=>{var e=0,o=0,r=0,i=0;if(DataSetPagina&&DataSetPagina.data&&DataSetPagina.data.Lista){var l=DataSetPagina.data.Lista;l.length>0&&$.each(l,function(a,t){"ACAO"==t.AtvTipoInvest&&(e+=parseFloat(GetValorDecimal(t.AtvTotAtual))),"FII"==t.AtvTipoInvest&&(o+=parseFloat(GetValorDecimal(t.AtvTotAtual))),"ETF"==t.AtvTipoInvest&&(r+=parseFloat(GetValorDecimal(t.AtvTotAtual))),"BDR"==t.AtvTipoInvest&&(i+=parseFloat(GetValorDecimal(t.AtvTotAtual)))})}(e>0||o>0||r>0||i>0)&&Highcharts.chart("DivGraficoPortfAlocacaoCateg",{lang:{months:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],shortMonths:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],weekdays:["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"],loading:["Atualizando o gráfico...aguarde"],contextButtonTitle:"Exportar gráfico",decimalPoint:",",thousandsSep:".",viewFullscreen:"Exibir em tela cheia",openInCloud:"Abri em Highcharts Cloud",downloadJPEG:"Baixar imagem JPEG",downloadPDF:"Baixar arquivo PDF",downloadPNG:"Baixar imagem PNG",downloadSVG:"Baixar vetor SVG",printChart:"Imprimir gráfico",rangeSelectorFrom:"De",rangeSelectorTo:"Para",rangeSelectorZoom:"Zoom",resetZoom:"Limpar Zoom",resetZoomTitle:"Voltar Zoom para nível 1:1"},exporting:{enabled:!1},chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:!1,type:"pie"},title:{text:null},tooltip:{pointFormatter:function(){return"Total: <b>R$ "+Number(this.y).toFixed(2).replace(/./g,function(a,t,e){return t>0&&"."!==a&&(e.length-t)%3==0?"X"+a:a}).replace(".",",").replace(/X/g,".")+"</b> <br> Percent.: <b>"+Number(this.percentage).toFixed(2)+"%</b> "},shared:!0},accessibility:{point:{valueSuffix:"%"}},plotOptions:{pie:{allowPointSelect:!0,cursor:"pointer",dataLabels:{enabled:!0,format:"<b>{point.name}</b>: {point.percentage:.2f} %"}}},series:[{name:"Categoria",colorByPoint:!0,data:[{name:"AÇÕES",y:parseFloat(e),sliced:!0,selected:!0},{name:"FIIs",y:parseFloat(o)},{name:"ETFs",y:parseFloat(r)},{name:"BDRs",y:parseFloat(i)}]}]}),a(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosGraficoAcoes(a){try{promise=new Promise((a,t)=>{var e=[],o=[];if(DataSetPagina&&DataSetPagina.data&&DataSetPagina.data.Lista){var r=DataSetPagina.data.Lista;if(r.length>0){var l=-1;$.each(r,function(a,t){t.CartId;if("ACAO"==t.AtvTipoInvest){var r=t.AtvCodigo,i=parseFloat(GetValorDecimal(t.AtvTotAtual));e[l+=1]=r,o[l]=i}})}}var n=e.length,s=[];for(i=0;i<n;i++)parseFloat(o[i]),s.push({Codigo:e[i],ValorAtual:o[i]});s.sort(function(a,t){var e=parseFloat(a.ValorAtual),o=parseFloat(t.ValorAtual);return e==o?0:e>o?1:-1}),s.reverse();var c=[];for(i=0;i<n;i++)c[i]={name:s[i].Codigo,y:parseFloat(s[i].ValorAtual),sliced:0==i,selected:0==i};Highcharts.chart("DivGraficoACAOAlocacaoAtivos",{lang:{months:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],shortMonths:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],weekdays:["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"],loading:["Atualizando o gráfico...aguarde"],contextButtonTitle:"Exportar gráfico",decimalPoint:",",thousandsSep:".",viewFullscreen:"Exibir em tela cheia",openInCloud:"Abri em Highcharts Cloud",downloadJPEG:"Baixar imagem JPEG",downloadPDF:"Baixar arquivo PDF",downloadPNG:"Baixar imagem PNG",downloadSVG:"Baixar vetor SVG",printChart:"Imprimir gráfico",rangeSelectorFrom:"De",rangeSelectorTo:"Para",rangeSelectorZoom:"Zoom",resetZoom:"Limpar Zoom",resetZoomTitle:"Voltar Zoom para nível 1:1"},exporting:{enabled:!1},chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:!1,type:"pie"},title:{text:null},tooltip:{pointFormatter:function(){return"Total: <b>R$ "+Number(this.y).toFixed(2).replace(/./g,function(a,t,e){return t>0&&"."!==a&&(e.length-t)%3==0?"X"+a:a}).replace(".",",").replace(/X/g,".")+"</b> <br> Percent.: <b>"+Number(this.percentage).toFixed(2)+"%</b> "},shared:!0},plotOptions:{pie:{allowPointSelect:!0,cursor:"pointer",dataLabels:{enabled:!0,format:"<b>{point.name}</b>: {point.percentage:.2f} %"}}},series:[{name:"Alocação por Ativos",colorByPoint:!0,data:c}]}),a(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosGraficoFIIs(a){try{promise=new Promise((a,t)=>{var e=[],o=[];if(DataSetPagina&&DataSetPagina.data&&DataSetPagina.data.Lista){var r=DataSetPagina.data.Lista;if(r.length>0){var l=-1;$.each(r,function(a,t){t.CartId;if("FII"==t.AtvTipoInvest){var r=t.AtvCodigo,i=parseFloat(GetValorDecimal(t.AtvTotAtual));e[l+=1]=r,o[l]=i}})}}var n=e.length,s=[];for(i=0;i<n;i++)parseFloat(o[i]),s.push({Codigo:e[i],ValorAtual:o[i]});s.sort(function(a,t){var e=parseFloat(a.ValorAtual),o=parseFloat(t.ValorAtual);return e==o?0:e>o?1:-1}),s.reverse();var c=[];for(i=0;i<n;i++)c[i]={name:s[i].Codigo,y:parseFloat(s[i].ValorAtual),sliced:0==i,selected:0==i};Highcharts.chart("DivGraficoFIIAlocacaoAtivos",{lang:{months:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],shortMonths:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],weekdays:["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"],loading:["Atualizando o gráfico...aguarde"],contextButtonTitle:"Exportar gráfico",decimalPoint:",",thousandsSep:".",viewFullscreen:"Exibir em tela cheia",openInCloud:"Abri em Highcharts Cloud",downloadJPEG:"Baixar imagem JPEG",downloadPDF:"Baixar arquivo PDF",downloadPNG:"Baixar imagem PNG",downloadSVG:"Baixar vetor SVG",printChart:"Imprimir gráfico",rangeSelectorFrom:"De",rangeSelectorTo:"Para",rangeSelectorZoom:"Zoom",resetZoom:"Limpar Zoom",resetZoomTitle:"Voltar Zoom para nível 1:1"},exporting:{enabled:!1},chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:!1,type:"pie"},title:{text:null},tooltip:{pointFormatter:function(){return"Total: <b>R$ "+Number(this.y).toFixed(2).replace(/./g,function(a,t,e){return t>0&&"."!==a&&(e.length-t)%3==0?"X"+a:a}).replace(".",",").replace(/X/g,".")+"</b> <br> Percent.: <b>"+Number(this.percentage).toFixed(2)+"%</b> "},shared:!0},plotOptions:{pie:{allowPointSelect:!0,cursor:"pointer",dataLabels:{enabled:!0,format:"<b>{point.name}</b>: {point.percentage:.2f} %"}}},series:[{name:"Ativos",colorByPoint:!0,data:c}]}),a(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosGraficoETFs(a){try{promise=new Promise((a,t)=>{var e=[],o=[];if(DataSetPagina&&DataSetPagina.data&&DataSetPagina.data.Lista){var r=DataSetPagina.data.Lista;if(r.length>0){var l=-1;$.each(r,function(a,t){t.CartId;if("ETF"==t.AtvTipoInvest){var r=t.AtvCodigo,i=parseFloat(GetValorDecimal(t.AtvTotAtual));e[l+=1]=r,o[l]=i}})}}var n=e.length,s=[];for(i=0;i<n;i++)parseFloat(o[i]),s.push({Codigo:e[i],ValorAtual:o[i]});s.sort(function(a,t){var e=parseFloat(a.ValorAtual),o=parseFloat(t.ValorAtual);return e==o?0:e>o?1:-1}),s.reverse();var c=[];for(i=0;i<n;i++)c[i]={name:s[i].Codigo,y:parseFloat(s[i].ValorAtual),sliced:0==i,selected:0==i};Highcharts.chart("DivGraficoETFAlocacaoAtivos",{lang:{months:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],shortMonths:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],weekdays:["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"],loading:["Atualizando o gráfico...aguarde"],contextButtonTitle:"Exportar gráfico",decimalPoint:",",thousandsSep:".",viewFullscreen:"Exibir em tela cheia",openInCloud:"Abri em Highcharts Cloud",downloadJPEG:"Baixar imagem JPEG",downloadPDF:"Baixar arquivo PDF",downloadPNG:"Baixar imagem PNG",downloadSVG:"Baixar vetor SVG",printChart:"Imprimir gráfico",rangeSelectorFrom:"De",rangeSelectorTo:"Para",rangeSelectorZoom:"Zoom",resetZoom:"Limpar Zoom",resetZoomTitle:"Voltar Zoom para nível 1:1"},exporting:{enabled:!1},chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:!1,type:"pie"},title:{text:null},tooltip:{pointFormatter:function(){return"Total: <b>R$ "+Number(this.y).toFixed(2).replace(/./g,function(a,t,e){return t>0&&"."!==a&&(e.length-t)%3==0?"X"+a:a}).replace(".",",").replace(/X/g,".")+"</b> <br> Percent.: <b>"+Number(this.percentage).toFixed(2)+"%</b> "},shared:!0},plotOptions:{pie:{allowPointSelect:!0,cursor:"pointer",dataLabels:{enabled:!0,format:"<b>{point.name}</b>: {point.percentage:.2f} %"}}},series:[{name:"Ativos",colorByPoint:!0,data:c}]}),a(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosGraficoBDRs(a){try{promise=new Promise((a,t)=>{var e=[],o=[];if(DataSetPagina&&DataSetPagina.data&&DataSetPagina.data.Lista){var r=DataSetPagina.data.Lista;if(r.length>0){var l=-1;$.each(r,function(a,t){t.CartId;if("BDR"==t.AtvTipoInvest){var r=t.AtvCodigo,i=parseFloat(GetValorDecimal(t.AtvTotAtual));e[l+=1]=r,o[l]=i}})}}var n=e.length,s=[];for(i=0;i<n;i++)parseFloat(o[i]),s.push({Codigo:e[i],ValorAtual:o[i]});s.sort(function(a,t){var e=parseFloat(a.ValorAtual),o=parseFloat(t.ValorAtual);return e==o?0:e>o?1:-1}),s.reverse();var c=[];for(i=0;i<n;i++)c[i]={name:s[i].Codigo,y:parseFloat(s[i].ValorAtual),sliced:0==i,selected:0==i};Highcharts.chart("DivGraficoBDRAlocacaoAtivos",{lang:{months:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],shortMonths:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],weekdays:["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"],loading:["Atualizando o gráfico...aguarde"],contextButtonTitle:"Exportar gráfico",decimalPoint:",",thousandsSep:".",viewFullscreen:"Exibir em tela cheia",openInCloud:"Abri em Highcharts Cloud",downloadJPEG:"Baixar imagem JPEG",downloadPDF:"Baixar arquivo PDF",downloadPNG:"Baixar imagem PNG",downloadSVG:"Baixar vetor SVG",printChart:"Imprimir gráfico",rangeSelectorFrom:"De",rangeSelectorTo:"Para",rangeSelectorZoom:"Zoom",resetZoom:"Limpar Zoom",resetZoomTitle:"Voltar Zoom para nível 1:1"},exporting:{enabled:!1},chart:{plotBackgroundColor:null,plotBorderWidth:null,plotShadow:!1,type:"pie"},title:{text:null},tooltip:{pointFormatter:function(){return"Total: <b>R$ "+Number(this.y).toFixed(2).replace(/./g,function(a,t,e){return t>0&&"."!==a&&(e.length-t)%3==0?"X"+a:a}).replace(".",",").replace(/X/g,".")+"</b> <br> Percent.: <b>"+Number(this.percentage).toFixed(2)+"%</b> "},shared:!0},plotOptions:{pie:{allowPointSelect:!0,cursor:"pointer",dataLabels:{enabled:!0,format:"<b>{point.name}</b>: {point.percentage:.2f} %"}}},series:[{name:"Ativos",colorByPoint:!0,data:c}]}),a(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}