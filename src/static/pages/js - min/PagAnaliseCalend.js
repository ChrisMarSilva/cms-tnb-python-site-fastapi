function iniciarAnimacaoPesquisarAnaliseCalProv(){$("#iRefreshCalProv").addClass("fa-spin"),$("#btnAnaliseCalProvPesquisar").addClass("disabled")}function finalizarAnimacaoPesquisaAnaliseCalProv(){$("#iRefreshCalProv").removeClass("fa-spin"),$("#btnAnaliseCalProvPesquisar").removeClass("disabled")}function fLimparGridAnaliseCalProv(t){fLimparAreaAlerta("AreaAlertaPrincAnaliseCalProv"),fLimparSomenteGridAnaliseCalProv(t)}async function fLimparSomenteGridAnaliseCalProv(t){try{promise=new Promise((t,a)=>{finalizarAnimacaoPesquisaAnaliseCalProv(),$("th").addClass("text-center"),$("#GridAnaliseCalProv").dataTable().fnClearTable(),$("#GridAnaliseCalProv").dataTable({bDestroy:!0}).fnDestroy(),$("#GridAnaliseCalProv").DataTable({oLanguage:fTraduzirGrid(),aoColumns:[{bSortable:!0,sWidth:"50px",targets:0},{bSortable:!0,sWidth:"50px",targets:1},{bSortable:!0,sWidth:"50px",targets:2},{bSortable:!0,sWidth:"50px",targets:3},{bSortable:!0,sWidth:"50px",targets:4},{bSortable:!0,sWidth:"50px",targets:5},{bSortable:!0,sWidth:"50px",targets:6},{bSortable:!0,sWidth:"50px",targets:7},{bSortable:!0,sWidth:"50px",targets:8},{bSortable:!0,sWidth:"50px",targets:9},{bSortable:!0,sWidth:"50px",targets:10},{bSortable:!0,sWidth:"50px",targets:11},{bSortable:!0,sWidth:"50px",targets:12},{bSortable:!0,sWidth:"50px",targets:13},{bSortable:!0,sWidth:"50px",targets:14}],order:[],bFilter:!1,bInfo:!1,bLengthChange:!1,searchable:!1,orderable:!1,bAutoWidth:!1,bPaginate:!1,ordering:!1}),t(!0)}).then(t=>{}).catch(t=>{})}catch(t){fCriarAlerta("AreaAlertaPrincAnaliseCalProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fMontarGridAnaliseCalProv(t,a,e){try{promise=new Promise((r,i)=>{$("#GridAnaliseCalProv").dataTable().fnClearTable(),$("#GridAnaliseCalProv").dataTable({bDestroy:!0}).fnDestroy(),$("#GridAnaliseCalProv").DataTable({processing:!0,serverSide:!1,iDisplayLength:10,oLanguage:fTraduzirGrid(),data:a,aoColumns:[{bSortable:!0,sWidth:"50px",targets:0},{bSortable:!0,sWidth:"50px",targets:1,render:function(a,r,i){return"display"==r?"0,00"!=i[1]?'<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '1' );\"> "+i[1]+" </i> </a>":i[1]:a}},{bSortable:!0,sWidth:"50px",targets:2,render:function(a,r,i){return"display"==r?"0,00"!=i[2]?'<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '2' );\"> "+i[2]+" </i> </a>":i[2]:a}},{bSortable:!0,sWidth:"50px",targets:3,render:function(a,r,i){return"display"==r?"0,00"!=i[3]?'<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '3' );\"> "+i[3]+" </i> </a>":i[3]:a}},{bSortable:!0,sWidth:"50px",targets:4,render:function(a,r,i){return"display"==r?"0,00"!=i[4]?'<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '4' );\"> "+i[4]+" </i> </a>":i[4]:a}},{bSortable:!0,sWidth:"50px",targets:5,render:function(a,r,i){return"display"==r?"0,00"!=i[5]?'<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '5' );\"> "+i[5]+" </i> </a>":i[5]:a}},{bSortable:!0,sWidth:"50px",targets:6,render:function(a,r,i){return"display"==r?"0,00"!=i[6]?'<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '6' );\"> "+i[6]+" </i> </a>":i[6]:a}},{bSortable:!0,sWidth:"50px",targets:7,render:function(a,r,i){return"display"==r?"0,00"!=i[7]?'<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '7' );\"> "+i[7]+" </i> </a>":i[7]:a}},{bSortable:!0,sWidth:"50px",targets:8,render:function(a,r,i){return"display"==r?"0,00"!=i[8]?'<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '8' );\"> "+i[8]+" </i> </a>":i[8]:a}},{bSortable:!0,sWidth:"50px",targets:9,render:function(a,r,i){return"display"==r?"0,00"!=i[9]?'<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '9' );\"> "+i[9]+" </i> </a>":i[9]:a}},{bSortable:!0,sWidth:"50px",targets:10,render:function(a,r,i){return"display"==r?"0,00"!=i[10]?'<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '10' );\"> "+i[10]+" </i> </a>":i[10]:a}},{bSortable:!0,sWidth:"50px",targets:11,render:function(a,r,i){return"display"==r?"0,00"!=i[11]?'<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '11' );\"> "+i[11]+" </i> </a>":i[11]:a}},{bSortable:!0,sWidth:"50px",targets:12,render:function(a,r,i){return"display"==r?"0,00"!=i[12]?'<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '12' );\"> "+i[12]+" </i> </a>":i[12]:a}},{bSortable:!0,sWidth:"50px",targets:13,render:function(a,r,i){return"display"==r?"0,00"!=i[13]?'<a class="text-dark font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+t+"', '"+i[0]+"', '"+e+"', '13' );\"> "+i[13]+" </i> </a>":i[13]:a}},{bSortable:!0,sWidth:"50px",targets:14,render:function(t,a,e){return"display"==a?e[14]:t}}],createdRow:function(t,a,e){$("td",t).addClass("text-center"),"TOTAL"==a[0]?($(t).addClass("table-secondary text-dark font-weight-bold"),$(t).css("height","35")):($("td",t).eq(0).addClass("table-secondary text-dark font-weight-bold"),$("td",t).eq(13).addClass("table-secondary text-dark font-weight-bold"),$("td",t).eq(14).addClass("table-secondary text-dark font-weight-bold"),"0,00"!=a[1]&&$("td",t).eq(1).addClass("text-success font-weight-bold"),"0,00"!=a[2]&&$("td",t).eq(2).addClass("text-success font-weight-bold"),"0,00"!=a[3]&&$("td",t).eq(3).addClass("text-success font-weight-bold"),"0,00"!=a[4]&&$("td",t).eq(4).addClass("text-success font-weight-bold"),"0,00"!=a[5]&&$("td",t).eq(5).addClass("text-success font-weight-bold"),"0,00"!=a[6]&&$("td",t).eq(6).addClass("text-success font-weight-bold"),"0,00"!=a[7]&&$("td",t).eq(7).addClass("text-success font-weight-bold"),"0,00"!=a[8]&&$("td",t).eq(8).addClass("text-success font-weight-bold"),"0,00"!=a[9]&&$("td",t).eq(9).addClass("text-success font-weight-bold"),"0,00"!=a[10]&&$("td",t).eq(10).addClass("text-success font-weight-bold"),"0,00"!=a[11]&&$("td",t).eq(11).addClass("text-success font-weight-bold"),"0,00"!=a[12]&&$("td",t).eq(12).addClass("text-success font-weight-bold"))},initComplete:function(t,a){finalizarAnimacaoPesquisaAnaliseCalProv()},order:[],dom:"frtBpi",buttons:[{extend:"excelHtml5",text:'<i class="fa fa-file-excel-o"></i> Excel',className:"btn btn-outline-default btn-sm",title:NOME_PROJETO+" - Análise do Calendário de Proventos - Ano "+e,titleAttr:"Excel",exportOptions:{columns:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]}},{extend:"csvHtml5",charset:"UTF-8",fieldSeparator:";",titleAttr:"CSV",text:'<i class="fa fa-file-o"></i> CSV',className:"btn btn-outline-default btn-sm",title:NOME_PROJETO+" - Análise do Calendário de Proventos - Ano "+e,bom:!0,exportOptions:{columns:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]}},{extend:"pdfHtml5",text:'<i class="fa fa-file-pdf-o"></i> PDF',className:"btn btn-default btn-sm",titleAttr:"PDF",title:NOME_PROJETO+" - Análise do Calendário de Proventos - Ano "+e,pageSize:"A3",alignment:"center",exportOptions:{columns:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]},footer:!0,customize:function(t){t.defaultStyle.fontSize=12,t.styles.tableHeader.fontSize=14}},{extend:"print",text:'<i class="fa fa-print"></i> Imprimir',title:NOME_PROJETO+" - Análise do Calendário de Proventos - Ano "+e,titleAttr:"Imprimir",className:"btn btn-default btn-sm",exportOptions:{columns:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]}}],bFilter:!1,bInfo:!1,bLengthChange:!1,searchable:!1,orderable:!1,bAutoWidth:!1,bPaginate:!1,ordering:!1}),r(!0)}).then(t=>{}).catch(t=>{})}catch(a){fLimparSomenteGridAnaliseCalProv(t),finalizarAnimacaoPesquisaAnaliseCalProv(),null!=a.description&&fCriarAlerta("AreaAlertaPrincAnaliseCalProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarregarGridAnaliseCalProv(t){try{promise=new Promise((a,e)=>{fLimparAreaAlerta("AreaAlertaPrincAnaliseCalProv"),finalizarAnimacaoPesquisaAnaliseCalProv(),iniciarAnimacaoPesquisarAnaliseCalProv();var r=GetAnoAtual();if(""==r)return fLimparSomenteGridAnaliseCalProv(t),fCriarAlerta("AreaAlertaPrincAnaliseCalProv",TP_ALERTA_AVISO,"Ano não Informado"),!1;$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:t+"Analise/gridCalProv",data:{Ano:r},success:function(a){var e=a.data.Resultado,i=a.data.Mensagem,l=a.data.Lista;return"NSESSAO"==e?($(location).attr("href",t+"/login"),!1):"NOK"==e?(fLimparSomenteGridAnaliseCalProv(t),void fCriarAlerta("AreaAlertaPrincAnaliseCalProv",TP_ALERTA_AVISO,i)):"FALHA"==e?(fLimparSomenteGridAnaliseCalProv(t),void fCriarAlerta("AreaAlertaPrincAnaliseCalProv",TP_ALERTA_AVISO,i)):"OK"!=e?(fLimparSomenteGridAnaliseCalProv(t),void fCriarAlerta("AreaAlertaPrincAnaliseCalProv",TP_ALERTA_AVISO,i)):void fMontarGridAnaliseCalProv(t,l,r)},error:function(a){return fLimparSomenteGridAnaliseCalProv(t),fCriarAlerta("AreaAlertaPrincAnaliseCalProv",TP_ALERTA_AVISO,MSG_ALERTA_ERRO),!1}}),a(!0)}).then(t=>{}).catch(t=>{})}catch(a){fLimparSomenteGridAnaliseCalProv(t),null!=a.description&&fCriarAlerta("AreaAlertaPrincAnaliseCalProv",TP_ALERTA_AVISO,MSG_ALERTA_ERRO)}}async function fAbrirModalDetalheAnaliseCalProv(t,a,e,r){try{promise=new Promise((i,l)=>{fLimparAreaAlertaPrinc();var o=$("#DivGridModalDetalheAnaliseCalProv");o.html(""),"TOTAL"==a&&(a=""),"ACAO"==a&&(a=""),"FII"==a&&(a=""),"ETF"==a&&(a=""),""==e&&(e="9999"),"TOTAL"==e&&(e="9999");var s="",n="";""!=e&&"TOTAL"!=e&&"13"==r&&(s=e+"0101",n=e+"1231"),""!=e&&"TOTAL"!=e&&""!=r&&"13"!=r&&(s=e+("00"+r).slice(-2)+"01",n=e+("00"+r).slice(-2)+"31"),$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:t+"proventos/grid",data:{CodAtivo:a,TipoRend:"",Corretora:"",DataIni:s,DataFim:n},success:function(a){var e=a.data.Resultado,r=a.data.Mensagem,i=a.data.Lista;if("NSESSAO"==e)return $(location).attr("href",t+"/login"),!1;if("NOK"==e)return $("#PopModalDetalheAnaliseCalProv").modal("hide"),void fCriarAlertaPrinc(TP_ALERTA_AVISO,r);if("FALHA"==e)return $("#PopModalDetalheAnaliseCalProv").modal("hide"),void fCriarAlertaPrinc(TP_ALERTA_ERRO,r);if("OK"==e){var l="";if(i.length>0){l+='<table class="table table-sm table-hover table-condensed nowrap" style="font-size: 12px;" border="0" cellspacing="0" width="100%" style="margin: 0px;">',l+="  <thead>",l+='    <tr style="font-size: 12px;" class="thead-dark font-weight-bold"> ',l+="      <th>Data Ex.</th>",l+="      <th>Data Pagto</th>",l+="      <th>Código</th>",l+="      <th>Tipo</th>",l+="      <th>Quant.</th>",l+="      <th>Preço</th>",l+="      <th>Total</th>",l+="    </tr>",l+="  </thead>",l+="  <tbody>";var s=0;$.each(i,function(t,a){var e=a[0],r=a[1],i=a[2],o=a[3],n=(a[4],a[5]),d=parseFloat(GetValorDecimal(a[6])),c=parseFloat(GetValorDecimal(a[7]));a[8],a[8];s+=c,l+='    <tr class="text-center text-dark" > ',l+='      <td style="width:auto;">'+colcarFormacataoData(e)+"</td>",l+='      <td style="width:auto;">'+colcarFormacataoData(r)+"</td>",l+='      <td class="font-weight-bold" style="width:auto;">'+i+"</td>",l+='      <td style="width:auto;">'+o+"</td>",l+='      <td style="width:auto;">'+colcarFormacataoInteiro(n)+"</td>",l+='      <td style="width:auto;">R$ '+fMascaraValor(d)+"</td>",l+='      <td class="font-weight-bold" style="width:auto;">R$ '+fMascaraValor(c)+"</td>",l+="    </tr>"}),l+='    <tr style="font-size: 12px;" class="text-center text-dark font-weight-bold" > ',l+="      <td> </td>",l+="      <td> </td>",l+='      <td class="font-weight-bold" style="width:auto;">TOTAL</td>',l+="      <td> </td>",l+="      <td> </td>",l+="      <td> </td>",l+='      <td class="font-weight-bold" >R$ '+fMascaraValor(s)+"</td>",l+="    </tr>",l+="  </tbody>",l+="</table>"}else l="Nenhum Provento encontrado para o Ativo no Período...";return o.html(""),o.append(l),$("#PopModalDetalheAnaliseCalProv").modal({backdrop:"static"}),!0}return $("#PopModalDetalheAnaliseCalProv").modal("hide"),void fCriarAlertaPrinc(TP_ALERTA_ERRO,r)},error:function(t){$("#PopModalDetalheAnaliseCalProv").modal("hide"),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}),i(!0)}).then(t=>{}).catch(t=>{})}catch(t){return $("#PopModalDetalheAnaliseCalProv").modal("hide"),void fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}