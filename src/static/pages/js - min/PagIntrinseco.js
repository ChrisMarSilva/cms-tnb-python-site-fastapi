function iniciarAnimacaoPesquisar(){$("#iRefresh").addClass("fa-spin"),$("#btnIntrPesquisar").addClass("disabled"),$("#btnIntrLimpar").addClass("disabled")}function finalizarAnimacaoPesquisa(){$("#iRefresh").removeClass("fa-spin"),$("#btnIntrPesquisar").removeClass("disabled"),$("#btnIntrLimpar").removeClass("disabled")}function fLimparGrid(a){$("#selFiltroSetor").val(""),$("#selFiltroSubSetor").val(""),$("#selFiltroSegmento").val(""),$("#selFiltroAtivo").val(""),$("#txtFiltroPerc").val("0,00"),$("#iRefresh").removeClass("fa-spin"),fLimparSomenteGrid(a)}function fLimparSomenteGrid(a){try{$("th").addClass("text-center"),$("#Grid").dataTable().fnClearTable(),$("#Grid").dataTable({bDestroy:!0}).fnDestroy(),$("#Grid").DataTable({oLanguage:fTraduzirGrid(),aoColumns:[{bSortable:!1,bOrderable:!1,sWidth:"50px",targets:0},{bSortable:!1,bOrderable:!1,sWidth:"50px",targets:1},{bSortable:!1,bOrderable:!1,sWidth:"50px",targets:2},{bSortable:!1,bOrderable:!1,sWidth:"50px",targets:3},{bSortable:!1,bOrderable:!1,sWidth:"50px",targets:4},{bSortable:!1,bOrderable:!1,sWidth:"50px",targets:5}],order:[],bFilter:!1,bInfo:!1,bLengthChange:!1,bSearchable:!1,bOrderable:!1,bSortable:!1,bAutoWidth:!1,bPaginate:!1,bOrdering:!1})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fMontarGrid(a,r){try{$("#Grid").DataTable({processing:!0,serverSide:!1,iDisplayLength:10,oLanguage:fTraduzirGrid(),data:r,aoColumns:[{bSortable:!0,bOrderable:!0,sWidth:"50px",targets:0},{bSortable:!0,bOrderable:!0,sWidth:"50px",targets:1},{bSortable:!0,bOrderable:!0,sWidth:"50px",targets:2,render:function(a,r,e){return"display"==r?"R$ "+e[2]:a}},{bSortable:!0,bOrderable:!0,sWidth:"50px",targets:3,render:function(a,r,e){return"display"==r?"R$ "+e[3]:a}},{bSortable:!0,bOrderable:!0,sWidth:"50px",targets:4,render:function(a,r,e){return"display"==r?e[4]+"%":a}},{bSortable:!0,bOrderable:!0,sWidth:"50px",targets:5}],createdRow:function(a,r,e){$("td",a).addClass("text-center");var t=r[5];"Barato"==t&&$("td",a).addClass("text-success"),"Caro"==t&&$("td",a).addClass("text-danger")},initComplete:function(a,r){finalizarAnimacaoPesquisa()},order:[],bFilter:!0,bInfo:!0,bLengthChange:!1,bSearchable:!0,bOrderable:!0,bSortable:!0,bAutoWidth:!1,bPaginate:!1,bOrdering:!0}),$(document).ajaxError(function(a,r,e,t){finalizarAnimacaoPesquisa()})}catch(r){fLimparSomenteGrid(a),finalizarAnimacaoPesquisa(),null!=r.description&&fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fCarregarGrid(a){try{fLimparAreaAlertaPrinc(),$("#Grid").dataTable().fnClearTable(),$("#Grid").dataTable({bDestroy:!0}).fnDestroy();var r=$("#selFiltroSetor").val().trim(),e=$("#selFiltroSubSetor").val().trim(),t=$("#selFiltroSegmento").val().trim(),i=$("#selFiltroAtivo").val().trim(),n=$("#selFiltroTipo").val().trim(),l=$("#txtFiltroPerc").val().trim();$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"intrinseco/grid",data:{Setor:r,SubSetor:e,Segmento:t,CodAtivo:i,Tipo:n,Perc:l},success:function(r){var e=r.data.Resultado,t=r.data.Mensagem,i=r.data.Lista;return"NSESSAO"==e?($(location).attr("href",a+"/login"),!1):"NOK"==e?(finalizarAnimacaoPesquisa(),fLimparSomenteGrid(a),void fCriarAlertaPrinc(TP_ALERTA_AVISO,t)):"FALHA"==e?(finalizarAnimacaoPesquisa(),fLimparSomenteGrid(a),void fCriarAlertaPrinc(TP_ALERTA_ERRO,t)):"OK"!=e?(finalizarAnimacaoPesquisa(),fLimparSomenteGrid(a),void fCriarAlertaPrinc(TP_ALERTA_ERRO,t)):void fMontarGrid(a,i)},error:function(r){return finalizarAnimacaoPesquisa(),fLimparSomenteGrid(a),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}})}catch(r){fLimparSomenteGrid(a),finalizarAnimacaoPesquisa(),null!=r.description&&fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}$(document).ready(function(){$("#MnPrincIntrinseco").addClass("active open"),fLimparAreaAlertaPrinc()});