function iniciarAnimacaoPesquisarAnaliseOper(){$("#iRefreshOper").addClass("fa-spin"),$("#btnAnaliseOperPesquisar").addClass("disabled"),$("#txtFiltroAnaliseOperAtivo").attr("disabled","disabled"),fDefinirPadraoSelect("txtFiltroAnaliseOperAtivo")}function finalizarAnimacaoPesquisaAnaliseOper(){$("#iRefreshOper").removeClass("fa-spin"),$("#btnAnaliseOperPesquisar").removeClass("disabled"),$("#txtFiltroAnaliseOperAtivo").removeAttr("disabled"),fDefinirPadraoSelect("txtFiltroAnaliseOperAtivo")}function fLimparGridAnaliseOper(e){fLimparAreaAlerta("AreaAlertaPrincAnaliseOper"),$("#txtFiltroAnaliseOperAtivo").val(""),$("#DivAnaliseOperAtivo").text("..."),$("#DivAnaliseOperTotInvest").text("R$ 0,00"),$("#DivAnaliseOperTotAtual").text("R$ 0,00"),$("#DivAnaliseOperValorizacao").text("R$ 0,00 (0.00%)"),$("#DivAnaliseOperValorizacao").removeClass("text-success"),$("#DivAnaliseOperValorizacao").removeClass("text-danger"),fLimparSomenteGridAnaliseOper(e)}async function fLimparSomenteGridAnaliseOper(e){try{promise=new Promise((e,a)=>{finalizarAnimacaoPesquisaAnaliseOper(),$("th").addClass("text-center"),$("#GridAnaliseOper").dataTable().fnClearTable(),$("#GridAnaliseOper").dataTable({bDestroy:!0}).fnDestroy(),$("#GridAnaliseOper").DataTable({oLanguage:fTraduzirGrid(),aoColumns:[{bSortable:!0,sWidth:"50px",targets:0},{bSortable:!0,sWidth:"50px",targets:1},{bSortable:!0,sWidth:"50px",targets:2},{bSortable:!0,sWidth:"50px",targets:3},{bSortable:!0,sWidth:"50px",targets:4},{bSortable:!0,sWidth:"50px",targets:5},{bSortable:!0,sWidth:"50px",targets:6},{bSortable:!0,sWidth:"50px",targets:7},{bSortable:!0,sWidth:"50px",targets:8}],order:[],bFilter:!1,bInfo:!1,bLengthChange:!1,searchable:!1,orderable:!1,bAutoWidth:!1,bPaginate:!1,ordering:!1}),e(!0)}).then(e=>{}).catch(e=>{})}catch(e){fCriarAlerta("AreaAlertaPrincAnaliseOper",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fMontarGridAnaliseOper(e,a){try{promise=new Promise((r,t)=>{var i=parseFloat(0),o=parseFloat(0),l=parseFloat(0),n=parseFloat(0),s=[],d=[],p=[],A=[];$("#GridAnaliseOper").DataTable({processing:!0,serverSide:!1,iDisplayLength:10,oLanguage:fTraduzirGrid(),data:a,aoColumns:[{bSortable:!0,sWidth:"50px",targets:0},{bSortable:!0,sWidth:"50px",targets:1},{bSortable:!0,sWidth:"50px",targets:2},{bSortable:!0,sWidth:"50px",targets:3},{bSortable:!0,sWidth:"50px",targets:4},{bSortable:!0,sWidth:"50px",targets:5,render:function(e,a,r){return"display"==a?"R$ "+r[5]:e}},{bSortable:!0,sWidth:"50px",targets:6,render:function(e,a,r){return"display"==a?"R$ "+r[6]:e}},{bSortable:!0,sWidth:"50px",targets:7,render:function(e,a,r){return"display"==a?"R$ "+r[7]:e}},{bSortable:!0,sWidth:"50px",targets:8,render:function(e,a,r){return"display"==a&&""!=r[8]?"R$ "+r[8]:e}}],createdRow:function(e,a,r){$("td",e).addClass("text-center");var t=a[0],l=a[3],n=parseFloat(GetValorDecimal(a[5])),c=parseFloat(GetValorDecimal(a[6])),m=parseFloat(GetValorDecimal(a[7])),u=0;s[r]=t,d[r]=l,p[r]=n,A[r]=c,"Compra"!=t&&"Bonificação"!=t||(i+=m),"Venda"!=t&&"Projetado"!=t||(o+=m),"Venda"!=t&&"Projetado"!=t||(""!=a[8]&&(u=parseFloat(GetValorDecimal(a[8]))),u>0&&$("td",e).addClass("text-success"),u<0&&$("td",e).addClass("text-danger"))},initComplete:function(a,r){finalizarAnimacaoPesquisaAnaliseOper(),0!=i&&0!=o&&(l=parseFloat(o)-parseFloat(i),n=l/i*100),$("#DivAnaliseOperTotInvest").text("R$ "+fMascaraValor(i)),$("#DivAnaliseOperTotAtual").text("R$ "+fMascaraValor(o)),$("#DivAnaliseOperValorizacao").text("R$ "+fMascaraValor(l)+" ("+fMascaraValor(n)+"%)"),parseFloat(l)>0&&$("#DivAnaliseOperValorizacao").addClass("text-success"),parseFloat(l)<0&&$("#DivAnaliseOperValorizacao").addClass("text-danger"),s.length>2&&fMontarGraficoAnaliseOper(e,s,d,p,A)},order:[],dom:"frtBpi",buttons:[{extend:"excelHtml5",text:'<i class="fa fa-file-excel-o"></i> Excel',className:"btn btn-outline-default btn-sm",title:NOME_PROJETO+" - Análise de Operações",titleAttr:"Excel",exportOptions:{columns:[0,1,2,3,4,5,6,7,8]},customizeData:function(e){for(var a=0;a<e.body.length;a++)for(var r=0;r<e.body[a].length;r++)4==r&&(e.body[a][r]="‌"+e.body[a][r])}},{extend:"csvHtml5",charset:"UTF-8",fieldSeparator:";",titleAttr:"CSV",text:'<i class="fa fa-file-o"></i> CSV',className:"btn btn-outline-default btn-sm",title:NOME_PROJETO+" - Análise de Operações",bom:!0,exportOptions:{columns:[0,1,2,3,4,5,6,7,8]}},{extend:"pdfHtml5",text:'<i class="fa fa-file-pdf-o"></i> PDF',className:"btn btn-default btn-sm",titleAttr:"PDF",title:NOME_PROJETO+" - Análise de Operações",pageSize:"A3",alignment:"center",exportOptions:{columns:[0,1,2,3,4,5,6,7,8]},footer:!0,customize:function(e){e.defaultStyle.fontSize=12,e.styles.tableHeader.fontSize=14}},{extend:"print",text:'<i class="fa fa-print"></i> Imprimir',title:NOME_PROJETO+" - Análise de Operações",titleAttr:"Imprimir",className:"btn btn-default btn-sm",exportOptions:{columns:[0,1,2,3,4,5,6,7,8]}}],bFilter:!1,bInfo:!1,bLengthChange:!1,searchable:!1,orderable:!1,bAutoWidth:!1,bPaginate:!1,ordering:!1}),r(!0)}).then(e=>{}).catch(e=>{})}catch(a){fLimparSomenteGridAnaliseOper(e),null!=a.description&&fCriarAlerta("AreaAlertaPrincAnaliseOper",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarregarGridAnaliseOper(e){try{promise=new Promise((a,r)=>{finalizarAnimacaoPesquisaAnaliseOper(),fLimparAreaAlerta("AreaAlertaPrincAnaliseOper"),$("#DivGraficoOper").html(""),$("#GridAnaliseOper").dataTable().fnClearTable(),$("#GridAnaliseOper").dataTable({bDestroy:!0}).fnDestroy(),$("#DivAnaliseOperTotInvest").text("R$ 0,00"),$("#DivAnaliseOperTotAtual").text("R$ 0,00"),$("#DivAnaliseOperValorizacao").text("R$ 0,00 (0.00%)"),$("#DivAnaliseOperValorizacao").removeClass("text-success"),$("#DivAnaliseOperValorizacao").removeClass("text-danger"),$("#DivAnaliseOperAtivo").text("...");var t=$("#txtFiltroAnaliseOperAtivo").val().trim();if(""==t)return fLimparGridAnaliseOper(e),fCriarAlerta("AreaAlertaPrincAnaliseOper",TP_ALERTA_AVISO,"Selecione um Ativo!"),!1;iniciarAnimacaoPesquisarAnaliseOper(),$("#DivAnaliseOperAtivo").text(t),$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:e+"Analise/gridOper",data:{CodAtivo:t},success:function(a){var r=a.data.Resultado,t=a.data.Mensagem,i=a.data.Lista;return"NSESSAO"==r?($(location).attr("href",e+"/login"),!1):"NOK"==r?(fLimparSomenteGridAnaliseOper(e),void fCriarAlerta("AreaAlertaPrincAnaliseOper",TP_ALERTA_AVISO,t)):"FALHA"==r?(fLimparSomenteGridAnaliseOper(e),void fCriarAlerta("AreaAlertaPrincAnaliseOper",TP_ALERTA_ERRO,t)):"OK"!=r?(fLimparSomenteGridAnaliseOper(e),void fCriarAlerta("AreaAlertaPrincAnaliseOper",TP_ALERTA_ERRO,t)):void fMontarGridAnaliseOper(e,i)},error:function(a){return fLimparSomenteGridAnaliseOper(e),fCriarAlerta("AreaAlertaPrincAnaliseOper",TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}),a(!0)}).then(e=>{}).catch(e=>{})}catch(a){fLimparSomenteGridAnaliseOper(e),null!=a.description&&fCriarAlerta("AreaAlertaPrincAnaliseOper",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fMontarGraficoAnaliseOper(e,a,r,t,o){try{promise=new Promise((e,l)=>{var n=[],s=[],d=r.length;for(iIndex=-1,i=0;i<d;i++)"Compra"!=a[i]&&"Projetado"!=a[i]||(iIndex+=1,n[iIndex]=[moment(colcarFormacataoDataXMLPadrao(r[i])).valueOf(),t[i]],s[iIndex]=[moment(colcarFormacataoDataXMLPadrao(r[i])).valueOf(),o[i]]);Highcharts.setOptions({global:{useUTC:!1},lang:{decimalPoint:",",thousandsSep:"."}}),Highcharts.setOptions({lang:{months:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],shortMonths:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],weekdays:["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"],loading:["Atualizando o gráfico...aguarde"],contextButtonTitle:"Exportar gráfico",decimalPoint:",",thousandsSep:".",downloadJPEG:"Baixar imagem JPEG",downloadPDF:"Baixar arquivo PDF",downloadPNG:"Baixar imagem PNG",downloadSVG:"Baixar vetor SVG",printChart:"Imprimir gráfico",rangeSelectorFrom:"De",rangeSelectorTo:"Para",rangeSelectorZoom:"Zoom",resetZoom:"Limpar Zoom",resetZoomTitle:"Voltar Zoom para nível 1:1"}}),Highcharts.stockChart("DivGraficoOper",{title:{align:"center",useHTML:!0,text:'<h6 class="font-weight-bold text-muted">Custo/Ação x Preço Médio</h6>'},global:{useUTC:!1},colors:["#7798BF","#55BF3B"],lang:{months:["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],shortMonths:["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],weekdays:["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"],loading:["Atualizando o gráfico...aguarde"],contextButtonTitle:"Exportar gráfico",decimalPoint:",",thousandsSep:".",downloadJPEG:"Baixar imagem JPEG",downloadPDF:"Baixar arquivo PDF",downloadPNG:"Baixar imagem PNG",downloadSVG:"Baixar vetor SVG",printChart:"Imprimir gráfico",rangeSelectorFrom:"De",rangeSelectorTo:"Para",rangeSelectorZoom:"Zoom",resetZoom:"Limpar Zoom",resetZoomTitle:"Voltar Zoom para nível 1:1"},rangeSelector:{selected:5,inputEnabled:!1},plotOptions:{series:{showInNavigator:!0}},tooltip:{valueDecimals:2},xAxis:{type:"datetime",dateTimeLabelFormats:{day:"%e. %b",month:"%b '%y",year:"%Y"},labels:{formatter:function(){return moment(this.value).format("DD/MM/YYYY")}}},yAxis:{labels:{formatter:function(){return"R$ "+this.value}},plotLines:[{value:0,width:2,color:"silver"}]},tooltip:{split:!0,valueDecimals:2,pointFormat:'<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>'},series:[{name:"Custo/Ação",data:n,dataGrouping:{groupPixelWidth:10}},{name:"Preço Médio",data:s,dataGrouping:{groupPixelWidth:50}}]}),e(!0)}).then(e=>{}).catch(e=>{})}catch(e){null!=e.description&&fCriarAlerta("AreaAlertaPrincAnaliseOper",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}