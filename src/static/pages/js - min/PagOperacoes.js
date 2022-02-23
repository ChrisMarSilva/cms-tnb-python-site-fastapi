function iniciarAnimacaoPesquisar(){$("#iRefresh").addClass("fa-spin"),$("#btnOperPesquisar").addClass("disabled"),$("#btnOperLimpar").addClass("disabled")}function finalizarAnimacaoPesquisa(){$("#iRefresh").removeClass("fa-spin"),$("#btnOperPesquisar").removeClass("disabled"),$("#btnOperLimpar").removeClass("disabled")}function fLimparGrid(t){fLimparAreaAlertaPrinc(),$("#txtOperDataIni").val(fDataPrimeira()),$("#txtOperDataFim").val(fDataAnoUltima()),$("#selOperAtivo").val(""),$("#selOperCorretora").val(""),fLimparSomenteGrid(t)}async function fLimparSomenteGrid(t){try{promise=new Promise((t,a)=>{finalizarAnimacaoPesquisa(),$("th").addClass("text-center"),$("#Grid").dataTable().fnClearTable(),$("#Grid").dataTable({bDestroy:!0}).fnDestroy(),$("#Grid").DataTable({data:[],oLanguage:fTraduzirGrid(),aoColumns:[{bSortable:!0,sWidth:"40px",targets:0},{bSortable:!0,sWidth:"30px",targets:1},{bSortable:!0,sWidth:"20px",targets:2},{bSortable:!0,sWidth:"30px",targets:3},{bSortable:!0,sWidth:"30px",targets:4},{bSortable:!0,sWidth:"30px",targets:5},{bSortable:!0,sWidth:"30px",targets:6},{bSortable:!0,sWidth:"30px",targets:7},{bSortable:!0,sWidth:"30px",targets:8},{bSortable:!0,sWidth:"30px",targets:9},{visible:!1,targets:10},{bSortable:!1,sWidth:"30px",targets:11}],order:[[0,"desc"],[10,"desc"]],iDisplayLength:100,bLengthChange:!1,bFilter:!1,searchable:!0,orderable:!0,bAutoWidth:!1}),t(!0)}).then(t=>{}).catch(t=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(t){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fMontarGrid(t,a){try{promise=new Promise((r,e)=>{$("#Grid").DataTable({processing:!0,serverSide:!1,oLanguage:fTraduzirGrid(),data:a,aoColumns:[{bSortable:!0,sWidth:"10px",targets:0,render:function(t,a,r){return"display"==a?colcarFormacataoData(r[0]):t}},{bSortable:!0,sWidth:"20px",targets:1},{bSortable:!0,sWidth:"10px",targets:2},{bSortable:!0,sWidth:"10px",targets:3,render:function(t,a,r){return"display"==a?colcarFormacataoInteiro(r[3]):t}},{bSortable:!0,sWidth:"20px",targets:4,render:function(t,a,r){return"display"==a?"R$ "+r[4]:t}},{bSortable:!0,sWidth:"40px",targets:5},{bSortable:!0,sWidth:"15px",targets:6,render:function(t,a,r){return"display"==a?"R$ "+r[6]:t}},{bSortable:!0,sWidth:"15px",targets:7,render:function(t,a,r){return"display"==a?"R$ "+r[7]:t}},{bSortable:!0,sWidth:"30px",targets:8,render:function(t,a,r){return"display"==a?"R$ "+r[8]:t}},{bSortable:!0,sWidth:"15px",targets:9,render:function(t,a,r){return"display"==a?"R$ "+r[9]:t}},{visible:!1,targets:10},{bSortable:!1,sWidth:"25px",targets:11,render:function(a,r,e){var o="",i="",l="";return"display"==r&&(Tipo=e[1],CodAtivo=e[2],IdOper=e[10],Tipo=Tipo.substr(0,1),o+='<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">',i+='<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAbrirModalDetalheOper( \''+t+"', '"+IdOper+"', 'Alterar', '"+Tipo+"', '"+CodAtivo+"' );\">",i+='   <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> ',i+="</a>",l+='<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;"  title="Excluir Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fChamarPagExclusaoOper( \''+IdOper+"', '"+CodAtivo+"' );\">",l+='   <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ',l+="</a>",l+="</div>"),o+"&nbsp;"+i+"&nbsp;"+l}}],createdRow:function(t,a,r){$("td",t).addClass("text-center"),"Compra"==a[1]&&$("td",t).addClass("text-muted"),"Venda"==a[1]&&$("td",t).addClass("text-danger")},initComplete:function(t,a){finalizarAnimacaoPesquisa()},order:[[0,"desc"],[10,"desc"]],dom:"frtBpi",buttons:[{extend:"excelHtml5",text:'<i class="fa fa-file-excel-o"></i> Excel',className:"btn btn-outline-default btn-sm",title:NOME_PROJETO+" - Operações",titleAttr:"Excel",exportOptions:{columns:[0,1,2,3,4,5,6,7,8,9]},customizeData:function(t){for(var a=0;a<t.body.length;a++)for(var r=0;r<t.body[a].length;r++)3==r&&(t.body[a][r]="‌"+t.body[a][r])}},{extend:"csvHtml5",charset:"UTF-8",fieldSeparator:";",titleAttr:"CSV",text:'<i class="fa fa-file-o"></i> CSV',className:"btn btn-outline-default btn-sm",title:NOME_PROJETO+" - Operações",bom:!0,exportOptions:{columns:[0,1,2,3,4,5,6,7,8,9]}},{extend:"pdfHtml5",text:'<i class="fa fa-file-pdf-o"></i> PDF',className:"btn btn-default btn-sm",titleAttr:"PDF",title:NOME_PROJETO+" - Operações",pageSize:"A3",alignment:"center",exportOptions:{columns:[0,1,2,3,4,5,6,7,8,9]},footer:!0,customize:function(t){t.defaultStyle.fontSize=12,t.styles.tableHeader.fontSize=14}},{extend:"print",text:'<i class="fa fa-print"></i> Imprimir',title:NOME_PROJETO+" - Operações",titleAttr:"Imprimir",className:"btn btn-default btn-sm",exportOptions:{columns:[0,1,2,3,4,5,6,7,8,9]}}],pageLength:100,bLengthChange:!1,bFilter:!1,searchable:!0,orderable:!0,bAutoWidth:!1,bInfo:!0,bSearchable:!1,bOrderable:!0,bSortable:!0,bPaginate:!0,bOrdering:!0}),$(document).ajaxError(function(t,a,r,e){finalizarAnimacaoPesquisa()}),r(!0)}).then(t=>{}).catch(t=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fLimparSomenteGrid(t),finalizarAnimacaoPesquisa(),null!=a.description&&fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarregarGrid(t){try{promise=new Promise((a,r)=>{fLimparAreaAlertaPrinc(),finalizarAnimacaoPesquisa(),iniciarAnimacaoPesquisar(),$("#Grid").dataTable().fnClearTable(),$("#Grid").dataTable({bDestroy:!0}).fnDestroy();var e=$("#txtOperDataIni").val(),o=$("#txtOperDataFim").val(),i=$("#selOperAtivo").val(),l=$("#selOperCorretora").val();e=tirarFormacataoData(e),o=tirarFormacataoData(o),$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:t+"operacoes/grid",data:{CodAtivo:i,Corretora:l,DataIni:e,DataFim:o},success:function(a){var r=a.data.Resultado,e=a.data.Mensagem,o=a.data.Lista;return"NSESSAO"==r?($(location).attr("href",t+"/login"),!1):"NOK"==r?(finalizarAnimacaoPesquisa(),fLimparSomenteGrid(t),void fCriarAlertaPrinc(TP_ALERTA_AVISO,e)):"FALHA"==r?(finalizarAnimacaoPesquisa(),fLimparSomenteGrid(t),void fCriarAlertaPrinc(TP_ALERTA_ERRO,e)):"OK"!=r?(finalizarAnimacaoPesquisa(),fLimparSomenteGrid(t),void fCriarAlertaPrinc(TP_ALERTA_ERRO,e)):void fMontarGrid(t,o)},error:function(a,r,e){return finalizarAnimacaoPesquisa(),fLimparSomenteGrid(t),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}),a(!0)}).then(t=>{}).catch(t=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){finalizarAnimacaoPesquisa(),fLimparSomenteGrid(t),null!=a.description&&fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fChamarPagExclusaoOper(t,a){try{if($("#txtDetOperId").val(""),$("#txtDetOperCod").val(""),""==a)return void fCriarAlertaPrinc(TP_ALERTA_AVISO,"Cód. Aitvo não informado!");if(""==t)return void fCriarAlertaPrinc(TP_ALERTA_AVISO,"Id. Oper. não informado!");$("#PopModalDelOper").modal({backdrop:"static"}),$("#txtDetOperCod").val(a),$("#txtDetOperId").val(t)}catch(t){$("#PopModalDelOper").modal("hide"),finalizarAnimacaoExcluir(),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fExcluirDadosOperacao(t,a,r){try{promise=new Promise((e,o)=>{fLimparAreaAlerta("AreaAlertaModalImportOper"),fLimparAreaAlertaModalExc(),finalizarAnimacaoExcluir();var i=$("#txtDetOperId").val(),l=$("#txtDetOperCod").val();return a&&(i=a),r&&(l=r),""==l?(r||fCriarAlertaModalExc(TP_ALERTA_AVISO,"Cód. Ativo não informado!"),void(r&&fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_SUCESSO,"Cód. Ativo não informado!"))):""==i?(a||fCriarAlertaModalExc(TP_ALERTA_AVISO,"Id. Oper. não informado!"),void(a&&fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_SUCESSO,"Id. Oper. não informado!"))):(iniciarAnimacaoExcluir(),$.ajax({dataType:"json",type:"post",url:t+"operacoes/excluir",data:{IdOper:i,CodAtivo:l},success:function(r){finalizarAnimacaoExcluir();var e=r.data.Resultado,o=r.data.Mensagem;if("NSESSAO"==e)return $(location).attr("href",t+"/login"),!1;if("NOK"==e)return a||fCriarAlertaModalExc(TP_ALERTA_AVISO,o),a&&fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_AVISO,o),!1;if("FALHA"==e)return a||fCriarAlertaModalExc(TP_ALERTA_ERRO,o),void(a&&fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_ERRO,o));if("OK"==e){if(a||($("#txtDetOperId").val(""),fCriarAlertaPrinc(TP_ALERTA_SUCESSO,o),$("#PopModalDelOper").modal("hide"),fCarregarGrid(t),fCarregarCodigoAtivos(t)),a){var i=$("#TrImport"+a).closest("tr");i.fadeOut(400,function(){i.remove(),$("#GridImport tr").length<=1&&$("#AreaTableModalImportOper").html("")})}return!0}return a||fCriarAlertaModalExc(TP_ALERTA_ERRO,o),a&&fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_ERRO,o),!1},error:function(t,r,e){$("#PopModalDelOper").modal("hide"),finalizarAnimacaoExcluir(),a||fCriarAlertaModalExc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),a&&fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}),void e(!0))}).then(t=>{}).catch(t=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(t){$("#PopModalDelOper").modal("hide"),finalizarAnimacaoExcluir(),a||fCriarAlertaModalExc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),a&&fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fAbrirModalDetalheOperImportarOper(t){try{fLimparAreaAlerta("AreaAlertaModalImportOper"),$("#AreaTableModalImportOper").html(""),$("#PopModalImportCSVOper").modal({backdrop:"static"})}catch(t){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function iniciarAnimacaoImportar(){$("#iImportar").addClass("fa-spinner"),$("#iImportar").addClass("fa-pulse"),$("#iImportar").addClass("fa-pulse")}function finalizarAnimacaImportar(){$("#iImportar").removeClass("fa-spinner"),$("#iImportar").removeClass("fa-pulse"),$("#iImportar").addClass("fa fa-upload")}function fImportarCSVOper(t){try{finalizarAnimacaImportar(),fLimparAreaAlerta("AreaAlertaModalImportOper");var a=$("#AreaTableModalImportOper");a.html("");var r=$("#arquivo");if(""==r.val().trim())return fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_AVISO,"Nenhum arquivo selecionado para importação."),!1;if(!new RegExp("([a-zA-Z0-9s_\\.-:])+(.csv)$").test(r.val().toLowerCase()))return fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_AVISO,"Tipo de Arquivo inválido para importação."),!1;iniciarAnimacaoImportar();var e=new FormData;e.append("arquivo",r[0].files[0]),$.ajax({dataType:"json",type:"POST",url:t+"operacoes/importarcsv",data:e,processData:!1,contentType:!1,cache:!1,timeout:6e5,success:function(e){finalizarAnimacaImportar();var o=e.data.Resultado,i=e.data.Mensagem,l=e.data.Lista;if("NSESSAO"==o)return $(location).attr("href",t+"/login"),!1;if("NOK"==o)return fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_AVISO,i),!1;if("FALHA"!=o){if("OK"==o){if(r.val(""),fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_SUCESSO,i),l.length>0){var d="";d+="<hr />",d+='<div class="form-group">',d+='  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">',d+='    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" ',d+="       onclick=\"fExcluirTodosDadosOperacao( '"+t+'\', );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ',d+="    </a>",d+="  </div>",d+="</div>",d+='<div class="table-responsive">',d+='<table id="GridImport" border="0" style="font-size: 14px" class="table table-sm table-hover table-condensed" cellspacing="0" width="100%">',d+='    <col width="10">',d+='    <col width="15">',d+='    <col width="15">',d+='    <col width="15">',d+='    <col width="15">',d+='    <col width="15">',d+='    <col width="10">',d+='    <col width="10">',d+='    <col width="10">',d+='    <col width="10">',d+='    <col width="10">',d+='    <col width="10">',d+='    <col width="15">',d+='    <col width="10">',d+="  <thead>",d+='    <tr style="font-size: 14px" class="bg-secondary text-white text-center">',d+='      <th style="width:2px;">Linha</th>',d+='      <th style="width:12px;">Data</th>',d+='      <th style="width:15px;">Tipo</th>',d+='      <th style="width:5px;">Ativo</th>',d+='      <th style="width:5px;">Quant.</th>',d+='      <th style="width:5px;">Preco</th>',d+='      <th style="width:2px;">Corret.</th>',d+='      <th style="width:2px;">Liq.</th>',d+='      <th style="width:2px;">Emol.</th>',d+='      <th style="width:2px;">ISS</th>',d+='      <th style="width:2px;">IRRF</th>',d+='      <th style="width:2px;">Outras</th>',d+='      <th style="width:12px;">Situação</th>',d+='      <th style="width:10px;display: none; ">IdLanc</th>',d+='      <th style="width:2px;">Ação</th>',d+="    </tr>",d+="  </thead>",d+="  <tbody>",$.each(l,function(a,r){CodAtivo=r[2],IdOper=r[12];var e="",o="Importado"==r[11]?"":" disabled";e+='<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple'+o+'"'+o+' style="font-size:0.5rem;" title="Excluir Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ',e+="   onclick=\"fExcluirDadosOperacao( '"+t+"', '"+IdOper+"', '"+CodAtivo+'\' );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ',e+="</a>",d+='    <tr style="font-size: 12px" id="TrImport'+IdOper+'" class="text-center font-weight-bold "> ',d+="      <td>"+colcarFormacataoInteiro(r[13])+"</td>",d+="      <td>"+colcarFormacataoData(r[0])+"</td>",d+="      <td>"+r[1]+"</td>",d+="      <td>"+r[2]+"</td>",d+="      <td>"+colcarFormacataoInteiro(r[3])+"</td>",d+="      <td>R$ "+r[4]+"</td>",d+="      <td>R$ "+r[5]+"</td>",d+="      <td>R$ "+r[6]+"</td>",d+="      <td>R$ "+r[7]+"</td>",d+="      <td>R$ "+r[8]+"</td>",d+="      <td>R$ "+r[9]+"</td>",d+="      <td>R$ "+r[10]+"</td>",d+='      <td class="text-center '+("Importado"==r[11]?"text-success":"text-danger")+'">'+r[11]+"</td>",d+='      <td style="display: none;">'+r[12]+"</td>",d+="      <td>"+e+"</td>",d+="    </tr>"}),d+="  </tbody>",d+="</table>",d+="</div>",d+='<div class="form-group">',d+='  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">',d+='    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" ',d+="       onclick=\"fExcluirTodosDadosOperacao( '"+t+'\', );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ',d+="    </a>",d+="  </div>",d+="</div>",a.append(d)}return!0}return finalizarAnimacaImportar(),fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_ERRO,i),!1}fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_ERRO,i)},error:function(t,a,r){finalizarAnimacaImportar(),fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}})}catch(t){finalizarAnimacaImportar(),fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fExcluirTodosDadosOperacao(t){try{promise=new Promise((a,r)=>{fLimparAreaAlerta("AreaAlertaModalImportOper"),$("#GridImport > tbody  > tr").each(function(){var a=$(this).find("td").eq(3).html(),r=$(this).find("td").eq(13).html();fExcluirDadosOperacao(t,r,a)}),a(!0)}).then(t=>{}).catch(t=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(t){fCriarAlerta("AreaAlertaModalImportOper",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fAbrirModalDetalheOperImportarOperCEI(t){try{fLimparAreaAlerta("AreaAlertaModalImportOperCEI"),$("#TxtDadosImportCEI").val(""),$("#AreaTableModalImportOperCEI").html(""),$("#PopModalImportOperCEI").modal({backdrop:"static"})}catch(t){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fExcluirTodosDadosOperacaoCEI(t){try{promise=new Promise((a,r)=>{fLimparAreaAlerta("AreaAlertaModalImportOperCEI"),$("#GridImport > tbody  > tr").each(function(){var a=$(this).find("td").eq(3).html(),r=$(this).find("td").eq(13).html();fExcluirDadosOperacao(t,r,a)}),a(!0)}).then(t=>{}).catch(t=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(t){fCriarAlerta("AreaAlertaModalImportOperCEI",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function iniciarAnimacaoImportarCEI(){$("#iImportarCEI").addClass("fa-spinner"),$("#iImportarCEI").addClass("fa-pulse")}function finalizarAnimacaImportarCEI(){$("#iImportarCEI").removeClass("fa-spinner"),$("#iImportarCEI").removeClass("fa-pulse"),$("#iImportarCEI").addClass("fa fa-upload")}function fImportarOperCEI(t){try{finalizarAnimacaImportarCEI(),fLimparAreaAlerta("AreaAlertaModalImportOperCEI");var a=$("#AreaTableModalImportOperCEI");a.html("");var r=$("#TxtDadosImportCEI").val().trim();if(""==r)return fCriarAlerta("AreaAlertaModalImportOperCEI",TP_ALERTA_AVISO,"Dados da CEI não informado"),!1;iniciarAnimacaoImportarCEI(),$.ajax({dataType:"json",type:"POST",async:!0,url:t+"operacoes/importarcei",data:{DadosCEI:r},cache:!1,success:function(r){finalizarAnimacaImportarCEI();var e=r.data.Resultado,o=r.data.Mensagem,i=r.data.Lista;if("NSESSAO"==e)return $(location).attr("href",t+"/login"),!1;if("NOK"==e)return fCriarAlerta("AreaAlertaModalImportOperCEI",TP_ALERTA_AVISO,o),!1;if("FALHA"!=e){if("OK"==e){if(fCriarAlerta("AreaAlertaModalImportOperCEI",TP_ALERTA_SUCESSO,o),i.length>0){var l="";l+="<hr />",l+='<div class="form-group">',l+='  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">',l+='    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" ',l+="       onclick=\"fExcluirTodosDadosOperacaoCEI( '"+t+'\', );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ',l+="    </a>",l+="  </div>",l+="</div>",l+='<div class="table-responsive">',l+='<table id="GridImport" border="0" style="font-size: 14px" class="table table-sm table-hover table-condensed" cellspacing="0" width="100%">',l+='    <col width="10">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="10">',l+="  <thead>",l+='    <tr style="font-size: 14px" class="bg-secondary text-white text-center">',l+='      <th style="width:2px;">Linha</th>',l+='      <th style="width:12px;">Data</th>',l+='      <th style="width:15px;">Tipo</th>',l+='      <th style="width:5px;">Ativo</th>',l+='      <th style="width:5px;">Quant.</th>',l+='      <th style="width:5px;">Preco</th>',l+='      <th style="width:12px;">Situação</th>',l+='      <th style="width:10px;display: none; ">IdLanc</th>',l+='      <th style="width:2px;">Ação</th>',l+="    </tr>",l+="  </thead>",l+="  <tbody>",$.each(i,function(a,r){CodAtivo=r[2],IdOper=r[12];var e="",o="Importado"==r[11]?"":" disabled";e+='<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple'+o+'"'+o+' style="font-size:0.5rem;" title="Excluir Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ',e+="   onclick=\"fExcluirDadosOperacao( '"+t+"', '"+IdOper+"', '"+CodAtivo+'\' );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ',e+="</a>",l+='    <tr style="font-size: 12px" id="TrImport'+IdOper+'" class="text-center font-weight-bold "> ',l+="      <td>"+colcarFormacataoInteiro(r[13])+"</td>",l+="      <td>"+colcarFormacataoData(r[0])+"</td>",l+="      <td>"+r[1]+"</td>",l+="      <td>"+r[2]+"</td>",l+="      <td>"+colcarFormacataoInteiro(r[3])+"</td>",l+="      <td>R$ "+r[4]+"</td>",l+='      <td style="display: none;">R$ '+r[5]+"</td>",l+='      <td style="display: none;">R$ '+r[6]+"</td>",l+='      <td style="display: none;">R$ '+r[7]+"</td>",l+='      <td style="display: none;">R$ '+r[8]+"</td>",l+='      <td style="display: none;">R$ '+r[9]+"</td>",l+='      <td style="display: none;">R$ '+r[10]+"</td>",l+='      <td class="text-center '+("Importado"==r[11]?"text-success":"text-danger")+'">'+r[11]+"</td>",l+='      <td style="display: none;">'+r[12]+"</td>",l+="      <td>"+e+"</td>",l+="    </tr>"}),l+="  </tbody>",l+="</table>",l+="</div>",l+='<div class="form-group">',l+='  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">',l+='    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" ',l+="       onclick=\"fExcluirTodosDadosOperacaoCEI( '"+t+'\', );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ',l+="    </a>",l+="  </div>",l+="</div>",a.append(l)}return!0}return finalizarAnimacaImportar(),fCriarAlerta("AreaAlertaModalImportOperCEI",TP_ALERTA_ERRO,o),!1}fCriarAlerta("AreaAlertaModalImportOperCEI",TP_ALERTA_ERRO,o)},error:function(t,a,r){finalizarAnimacaImportar(),fCriarAlerta("AreaAlertaModalImportOperCEI",TP_ALERTA_ERRO,t.responseText)}})}catch(t){finalizarAnimacaImportar(),fCriarAlerta("AreaAlertaModalImportOperCEI",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fAbrirModalDetalheOperImportarOperNotaCorretagem(t){try{$("#txtArquivoNota").val(""),$("#txtCorretoraNota").val(""),fLimparAreaAlerta("AreaAlertaModalImportOperNotaCorretagem"),$("#AreaTableModalImportOperNotaCorretagem").html(""),$("#PopModalImportOperNotaCorretagem").modal({backdrop:"static"})}catch(t){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fExcluirTodosDadosOperacaoNotaCorretagem(t){try{promise=new Promise((a,r)=>{fLimparAreaAlerta("AreaAlertaModalImportOperNotaCorretagem"),$("#GridImport > tbody  > tr").each(function(){var a=$(this).find("td").eq(3).html(),r=$(this).find("td").eq(13).html();fExcluirDadosOperacao(t,r,a)}),a(!0)}).then(t=>{}).catch(t=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(t){fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function iniciarAnimacaoImportarNotaCorretagem(){$("#BtnModalImportOperNotaCorretagemSalvar").addClass("disabled"),$("#iImportarNotaCorretagem").addClass("fa-spinner"),$("#iImportarNotaCorretagem").addClass("fa-pulse")}function finalizarAnimacaImportarNotaCorretagem(){$("#BtnModalImportOperNotaCorretagemSalvar").removeClass("disabled"),$("#iImportarNotaCorretagem").removeClass("fa-spinner"),$("#iImportarNotaCorretagem").removeClass("fa-pulse"),$("#iImportarNotaCorretagem").addClass("fa fa-upload")}function fImportarOperNotaCorretagem(t){try{finalizarAnimacaImportarNotaCorretagem(),fLimparAreaAlerta("AreaAlertaModalImportOperNotaCorretagem");var a=$("#AreaTableModalImportOperNotaCorretagem");a.html("");var r=$("#txtArquivoNota"),e=$("#txtCorretoraNota").val();if(""==r.val().trim())return fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem",TP_ALERTA_AVISO,"Nenhum arquivo selecionado para importação."),!1;if(!new RegExp("([a-zA-Z0-9s_\\.-:])+(.pdf)$").test(r.val().toLowerCase()))return fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem",TP_ALERTA_AVISO,"Tipo de Arquivo inválido para importação."),!1;a.html("<br><br><br> <h6 class='text-center font-weight-bold'>Aguarde, estamos importando a sua nota!!!</h6>"),iniciarAnimacaoImportarNotaCorretagem();var o=new FormData;o.append("corretora",e.trim()),o.append("arquivo",r[0].files[0]),$.ajax({dataType:"json",type:"POST",url:t+"operacoes/importarnotacorretagem",data:o,processData:!1,contentType:!1,cache:!1,timeout:6e5,success:function(r){a.html(""),finalizarAnimacaImportarNotaCorretagem();var e=r.data.Resultado,o=r.data.Mensagem,i=r.data.Lista;if("NSESSAO"==e)return $(location).attr("href",t+"/login"),!1;if("NOK"==e)return fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem",TP_ALERTA_AVISO,o),!1;if("FALHA"!=e){if("OK"==e){if(fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem",TP_ALERTA_SUCESSO,o),i.length>0){var l="";l+="<hr />",l+="<br />",l+='<div class="table-responsive">',l+='<table border="0" style="font-size: 13px" class="table table-sm table-hover table-condensed" cellspacing="0" width="100%">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+="  <thead>",l+='    <tr style="font-size: 13px" class="bg-secondary text-white text-center">',l+='      <th style="width:12px;">Data</th>',l+='      <th style="width:5px;">Tot. Bruto</th>',l+='      <th style="width:2px;">Liq.</th>',l+='      <th style="width:2px;">Emol.</th>',l+='      <th style="width:2px;">Corret.</th>',l+='      <th style="width:2px;">ISS</th>',l+='      <th style="width:2px;">IRRF</th>',l+='      <th style="width:2px;">Outras</th>',l+='      <th style="width:5px;">Tot. Líquido</th>',l+="    </tr>",l+="  </thead>",l+="  <tbody>",$.each(i,function(t,a){"CALC"==a[0]&&(l+='    <tr style="font-size: 12px" class="text-center font-weight-bold"> ',l+="      <td>"+colcarFormacataoData(a[1])+"</td>",l+="      <td>R$ "+a[2]+"</td>",l+="      <td>R$ "+a[3]+"</td>",l+="      <td>R$ "+a[4]+"</td>",l+="      <td>R$ "+a[5]+"</td>",l+="      <td>R$ "+a[6]+"</td>",l+="      <td>R$ "+a[7]+"</td>",l+="      <td>R$ "+a[8]+"</td>",l+="      <td>R$ "+a[9]+"</td>",l+="    </tr>")}),l+="  </tbody>",l+="</table>",l+="</div>",l+="<hr />",l+='<div class="form-group">',l+='  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">',l+='    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" ',l+="       onclick=\"fExcluirTodosDadosOperacaoNotaCorretagem( '"+t+'\', );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ',l+="    </a>",l+="  </div>",l+="</div>",l+='<div class="table-responsive">',l+='<table id="GridImport" border="0" style="font-size: 13px" class="table table-sm table-hover table-condensed" cellspacing="0" width="100%">',l+='    <col width="10">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="15">',l+='    <col width="10">',l+="  <thead>",l+='    <tr style="font-size: 13px" class="bg-secondary text-white text-center">',l+='      <th style="width:2px;">Linha</th>',l+='      <th style="width:12px;">Data</th>',l+='      <th style="width:15px;">Tipo</th>',l+='      <th style="width:5px;">Ativo</th>',l+='      <th style="width:5px;">Quant.</th>',l+='      <th style="width:5px;">Preco</th>',l+='      <th style="width:2px;">Corret.</th>',l+='      <th style="width:2px;">Liq.</th>',l+='      <th style="width:2px;">Emol.</th>',l+='      <th style="width:2px;">ISS</th>',l+='      <th style="width:2px;">IRRF</th>',l+='      <th style="width:2px;">Outras</th>',l+='      <th style="width:12px;">Situação</th>',l+='      <th style="width:10px;display: none; ">IdLanc</th>',l+='      <th style="width:2px;">Ação</th>',l+="    </tr>",l+="  </thead>",l+="  <tbody>",$.each(i,function(a,r){if("CALC"!=r[0]){CodAtivo=r[2],IdOper=r[12];var e="",o="Importado"==r[11]?"":" disabled";e+='<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple'+o+'"'+o+' style="font-size:0.5rem;" title="Excluir Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ',e+="   onclick=\"fExcluirDadosOperacao( '"+t+"', '"+IdOper+"', '"+CodAtivo+'\' );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ',e+="</a>",l+='    <tr style="font-size: 12px" id="TrImport'+IdOper+'" class="text-center font-weight-bold "> ',l+="      <td>"+colcarFormacataoInteiro(r[13])+"</td>",l+="      <td>"+colcarFormacataoData(r[0])+"</td>",l+="      <td>"+r[1]+"</td>",l+="      <td>"+r[2]+"</td>",l+="      <td>"+colcarFormacataoInteiro(r[3])+"</td>",l+="      <td>R$ "+r[4]+"</td>",l+="      <td>R$ "+r[5]+"</td>",l+="      <td>R$ "+r[6]+"</td>",l+="      <td>R$ "+r[7]+"</td>",l+="      <td>R$ "+r[8]+"</td>",l+="      <td>R$ "+r[9]+"</td>",l+="      <td>R$ "+r[10]+"</td>",l+='      <td class="text-center '+("Importado"==r[11]?"text-success":"text-danger")+'">'+r[11]+"</td>",l+='      <td style="display: none;">'+r[12]+"</td>",l+="      <td>"+e+"</td>",l+="    </tr>"}}),l+="  </tbody>",l+="</table>",l+="</div>",l+='<div class="form-group">',l+='  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">',l+='    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" ',l+="       onclick=\"fExcluirTodosDadosOperacaoNotaCorretagem( '"+t+'\', );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ',l+="    </a>",l+="  </div>",l+="</div>",a.append(l)}return!0}return finalizarAnimacaImportar(),fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem",TP_ALERTA_ERRO,o),a.html(""),!1}fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem",TP_ALERTA_ERRO,o)},error:function(t,r,e){finalizarAnimacaImportar(),fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem",TP_ALERTA_ERRO,t.responseText),a.html("")}})}catch(t){finalizarAnimacaImportar(),fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem",TP_ALERTA_ERRO,MSG_ALERTA_ERRO),a.html("")}}function iniciarAnimacaoExcluirTds(){$("#iExcluirTds").removeClass("fa-check"),$("#iExcluirTds").addClass("fa-spinner"),$("#iExcluirTds").addClass("fa-pulse"),$("#BtnModalDelTdsOperSim").addClass("disabled")}function finalizarAnimacaoExcluirTds(){$("#iExcluirTds").removeClass("fa-spinner"),$("#iExcluirTds").removeClass("fa-pulse"),$("#iExcluirTds").addClass("fa-check"),$("#BtnModalDelTdsOperSim").removeClass("disabled")}function fAbrirModalLimparTodasOper(){try{fLimparAreaAlerta("AreaAlertaModalExcTds"),$("#PopModalDelTdsOper").modal({backdrop:"static"})}catch(t){$("#PopModalDelTdsOper").modal("hide"),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fExcluirTodasOperacao(t){try{promise=new Promise((a,r)=>{finalizarAnimacaoExcluirTds(),iniciarAnimacaoExcluirTds(),fLimparAreaAlerta("AreaAlertaModalExcTds"),$.ajax({dataType:"json",type:"post",url:t+"operacoes/excluirtudo",data:{},success:function(a){finalizarAnimacaoExcluirTds();var r=a.data.Resultado,e=a.data.Mensagem;return"NSESSAO"==r?($(location).attr("href",t+"/login"),!1):"NOK"==r?(fCriarAlerta("AreaAlertaModalExcTds",TP_ALERTA_AVISO,e),!1):"FALHA"==r?void fCriarAlerta("AreaAlertaModalExcTds",TP_ALERTA_ERRO,e):"OK"==r?($("#PopModalDelTdsOper").modal("hide"),fCriarAlertaPrinc(TP_ALERTA_SUCESSO,e),fCarregarGrid(t),fCarregarCodigoAtivos(t),!0):(fCriarAlerta("AreaAlertaModalExcTds",TP_ALERTA_ERRO,e),!1)},error:function(t,a,r){finalizarAnimacaoExcluirTds(),$("#PopModalDelTdsOper").modal("hide"),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}),a(!0)}).then(t=>{}).catch(t=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(t){finalizarAnimacaoExcluirTds(),$("#PopModalDelTdsOper").modal("hide"),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}$(document).ready(function(){promise=new Promise((t,a)=>{$("#MnPrincOperacoes").addClass("active open"),fLimparAreaAlertaPrinc(),fLimparAreaAlertaModalCad(),fLimparAreaAlertaModalExc(),$("#FormOper input[type=text]").bind("keyup change",function(){fCalcularPrecoTotal(),fCalcularOperacao()}),t(!0)}).then(t=>{}).catch(t=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})});