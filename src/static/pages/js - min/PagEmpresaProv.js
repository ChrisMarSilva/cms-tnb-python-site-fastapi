function iniciarAnimacaoPesquisar(){$("#iRefresh").addClass("fa-spin"),$("#btnEmprProvPesquisar").addClass("disabled"),$("#btnEmprProvLimpar").addClass("disabled")}function finalizarAnimacaoPesquisa(){$("#iRefresh").removeClass("fa-spin"),$("#btnEmprProvPesquisar").removeClass("disabled"),$("#btnEmprProvLimpar").removeClass("disabled")}function fLimparGrid(a){$("#txtFiltroEmprProvDataIni").val(fDataPrimeira()),$("#txtFiltroEmprProvDataFim").val(""),$("#txtFiltroEmprProvAtivo").val(""),$("#txtFiltroEmprProvTipo").val(""),fLimparSomenteGrid(a)}function fLimparSomenteGrid(a){try{finalizarAnimacaoPesquisa(),$("th").addClass("text-center"),$("#Grid").dataTable().fnClearTable(),$("#Grid").dataTable({bDestroy:!0}).fnDestroy(),$("#Grid").DataTable({oLanguage:fTraduzirGrid(),aoColumns:[{bSortable:!0,sWidth:"50px",targets:0},{bSortable:!0,sWidth:"50px",targets:1},{bSortable:!0,sWidth:"50px",targets:2},{bSortable:!0,sWidth:"50px",targets:3},{bSortable:!0,sWidth:"50px",targets:4},{visible:!1,targets:5},{bSortable:!0,sWidth:"50px",targets:6}],bFilter:!0,searchable:!0,orderable:!0,bAutoWidth:!1})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fMontarGrid(a,r){try{$("#Grid").DataTable({processing:!0,serverSide:!1,oLanguage:fTraduzirGrid(),data:r,aoColumns:[{bSortable:!0,sWidth:"50px",targets:0,render:function(a,r,t){return"display"==r?colcarFormacataoData(t[0]):a}},{bSortable:!0,sWidth:"50px",targets:1,render:function(a,r,t){return"display"==r?colcarFormacataoData(t[1]):a}},{bSortable:!0,sWidth:"20px",targets:2},{bSortable:!0,sWidth:"20px",targets:3},{bSortable:!0,sWidth:"50px",targets:4,render:function(a,r,t){return"display"==r?"R$ "+t[4].replace(".",","):a}},{visible:!1,targets:5},{bSortable:!0,sWidth:"20px",targets:6,render:function(r,t,o){var i="",e="";return"display"==t&&(IdEmprProv=o[5],i+='<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">',i+='<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar" href="javascript:void(0);" onclick="fAbrirModalDetalheEmprProv( \''+a+"', '"+IdEmprProv+"', 'Alterar' );\">",i+='   <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> ',i+="</a>",e+='<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Excluir" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fChamarPagExclusaoEmprProv( \''+IdEmprProv+"' );\">",e+='   <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ',e+="</a>",e+="</div>"),i+"&nbsp;"+e}}],createdRow:function(a,r,t){$("td",a).addClass("text-center")},initComplete:function(a,r){finalizarAnimacaoPesquisa()},pageLength:100,bLengthChange:!1,bFilter:!0,searchable:!0,orderable:!0,bAutoWidth:!1}),$(document).ajaxError(function(r,t,o,i){fLimparSomenteGrid(a),finalizarAnimacaoPesquisa()})}catch(r){fLimparSomenteGrid(a),finalizarAnimacaoPesquisa(),null!=r.description&&fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fCarregarGrid(a){try{finalizarAnimacaoPesquisa(),fLimparAreaAlertaPrinc(),$("#Grid").dataTable().fnClearTable(),$("#Grid").dataTable({bDestroy:!0}).fnDestroy(),iniciarAnimacaoPesquisar();var r=$("#txtFiltroEmprProvDataIni").val().trim(),t=$("#txtFiltroEmprProvDataFim").val().trim(),o=$("#txtFiltroEmprProvAtivo").val().trim(),i=$("#txtFiltroEmprProvTipo").val().trim();$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"empresaProv/grid",data:{ProvDtExIni:tirarFormacataoData(r),ProvDtExFim:tirarFormacataoData(t),CodAtivo:o,Tipo:i},success:function(r){var t=r.data.Resultado,o=r.data.Mensagem,i=r.data.Lista;return"NSESSAO"==t?($(location).attr("href",a+"/login"),!1):"NOK"==t?(finalizarAnimacaoPesquisa(),fLimparSomenteGrid(a),void fCriarAlertaPrinc(TP_ALERTA_AVISO,o)):"FALHA"==t?(finalizarAnimacaoPesquisa(),fLimparSomenteGrid(a),void fCriarAlertaPrinc(TP_ALERTA_ERRO,o)):"OK"!=t?(finalizarAnimacaoPesquisa(),fLimparSomenteGrid(a),void fCriarAlertaPrinc(TP_ALERTA_ERRO,o)):void fMontarGrid(a,i)},error:function(r){return finalizarAnimacaoPesquisa(),fLimparSomenteGrid(a),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}})}catch(r){finalizarAnimacaoPesquisa(),fLimparSomenteGrid(a),null!=r.description&&fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fLimparDadosModalEmprProv(){fLimparAreaAlertaModalCad(),$("#txtCadEmprProvId").val(""),$("#txtCadEmprProvAtivo").val(""),$("#txtCadEmprProvTipo").val(""),$("#txtCadEmprProvCateg").val(""),$("#txtCadEmprProvDtAprov").val(fDataAtual()),$("#txtCadEmprProvDtCom").val(""),$("#txtCadEmprProvDtEx").val(fDataAtual()),$("#txtCadEmprProvDtPagto").val(""),$("#txtCadEmprProvPreco").val("0,00"),fDefinirPadraoSelect("txtCadEmprProvAtivo")}function fAbrirModalDetalheEmprProv(a,r,t){try{fLimparDadosModalEmprProv(),$("#PopModalDetalheEmprProvTit").html(""),$("#PopModalDetalheEmprProvTit").html(" - "+t),$("#BtnModalDetalheEmprProvSalvar").show(),"Visualizar"==t&&$("#BtnModalDetalheEmprProvSalvar").hide(),"Novo"==t&&$("#PopModalDetalheEmprProv").modal({backdrop:"static"}),"Alterar"!=t&&"Visualizar"!=t||fCarregarDadosModalDetalheEmprProv(a,r,t),$("#txtCadEmprProvAtivo").focus()}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fCarregarDadosModalDetalheEmprProv(a,r,t){try{if(""==r)return void fCriarAlertaPrinc(TP_ALERTA_AVISO,"Id. Empresa Provento não informado!");$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"empresaProv/carregar",data:{IdEmprProv:r},success:function(r){var o=r.data.Resultado,i=r.data.Mensagem,e=r.data.Dados;if("NSESSAO"==o)return $(location).attr("href",a+"/login"),!1;"NOK"==o?fCriarAlertaPrinc(TP_ALERTA_AVISO,i):"FALHA"==o?fCriarAlertaPrinc(TP_ALERTA_ERRO,i):"OK"==o&&e.Id?($("#txtCadEmprProvId").val(e.Id),$("#txtCadEmprProvAtivo").val(e.CodAtivo),$("#txtCadEmprProvTipo").val(e.Tipo),$("#txtCadEmprProvCateg").val(e.Categ),$("#txtCadEmprProvDtAprov").val(e.DtAprov),$("#txtCadEmprProvDtCom").val(e.DtCom),$("#txtCadEmprProvDtEx").val(e.DtEx),$("#txtCadEmprProvDtPagto").val(e.DtPagto),$("#txtCadEmprProvPreco").val(e.Preco.replace(".",",")),fDefinirPadraoSelect("txtCadEmprProvAtivo"),"Visualizar"==t&&($("#BtnModalDetalheEmprProvSalvar").attr("disabled","disabled"),$("#BtnModalDetalheEmprProvSalvar").addClass("disabled")),$("#PopModalDetalheEmprProv").modal({backdrop:"static"})):fCriarAlertaPrinc(TP_ALERTA_ERRO,i)},error:function(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}})}catch(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fValidarDados(){try{fLimparAreaAlertaModalCad();var a=$("#txtCadEmprProvAtivo").val(),r=$("#txtCadEmprProvTipo").val(),t=$("#txtCadEmprProvDtAprov").val(),o=$("#txtCadEmprProvPreco").val(),i="";return""==a&&(i+=" - Ativo<br/>"),""==r&&(i+=" - Tipo<br/>"),""==t&&(i+=" - Data Aprov<br/>"),""!=o&&",00"!=o&&"0,00"!=o||(i+=" - Preço<br/>"),""==i||(fCriarAlertaModalCad(TP_ALERTA_AVISO,"Os seguintes campos não estão preenchido: <br/>"+i),!1)}catch(a){return fCriarAlertaModalCad(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}function fSalvarDadosEmprProv(a){try{if(!fValidarDados())return!1;iniciarAnimacaoSalvar();var r=$("#txtCadEmprProvId").val(),t=$("#txtCadEmprProvAtivo").val(),o=$("#txtCadEmprProvTipo").val(),i=$("#txtCadEmprProvCateg").val(),e=$("#txtCadEmprProvDtAprov").val(),l=$("#txtCadEmprProvDtCom").val(),d=$("#txtCadEmprProvDtEx").val(),n=$("#txtCadEmprProvDtPagto").val(),s=$("#txtCadEmprProvPreco").val();$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"empresaProv/salvar",data:{Id:r,CodAtivo:t,Tipo:o,Categ:i,DtAprov:tirarFormacataoData(e),DtCom:tirarFormacataoData(l),DtEx:tirarFormacataoData(d),DtPagto:tirarFormacataoData(n),Preco:s},success:function(r){finalizarAnimacaoSalvar();var t=r.data.Resultado,o=r.data.Mensagem;if("NSESSAO"==t)return $(location).attr("href",a+"/login"),!1;"NOK"!=t?"FALHA"!=t&&"OK"==t?(fLimparDadosModalEmprProv(),$("#PopModalDetalheEmprProv").modal("hide"),fCriarAlertaPrinc(TP_ALERTA_SUCESSO,"Dados salvo com sucesso!"),fCarregarGrid(a)):fCriarAlertaModalCad(TP_ALERTA_ERRO,o):fCriarAlertaModalCad(TP_ALERTA_AVISO,o)},error:function(a){finalizarAnimacaoSalvar(),fCriarAlertaModalCad(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}})}catch(a){return finalizarAnimacaoSalvar(),void CriarAlertaModal(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fChamarPagExclusaoEmprProv(a){try{if($("#txtDelEmprProvId").val(""),""==a)return void fCriarAlertaPrinc(TP_ALERTA_AVISO,"Id. Empresa Provento não informado!");$("#PopModalDelEmprProv").modal({backdrop:"static"}),$("#txtDelEmprProvId").val(a)}catch(a){$("#PopModalDelEmprProv").modal("hide"),finalizarAnimacaoExcluir(),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fExcluirDadosEmprProv(a){try{finalizarAnimacaoExcluir();var r=$("#txtDelEmprProvId").val();if(""==r)return void fCriarAlertaModalExc(TP_ALERTA_AVISO,"Id. Empresa Provento não informado!");iniciarAnimacaoExcluir(),$.ajax({dataType:"json",type:"post",url:a+"empresaProv/excluir",data:{EmprProvId:r},success:function(r){finalizarAnimacaoExcluir();var t=r.data.Resultado,o=r.data.Mensagem;return"NSESSAO"==t?($(location).attr("href",a+"/login"),!1):"NOK"==t?(fCriarAlertaModalExc(TP_ALERTA_AVISO,o),!1):"FALHA"==t?void fCriarAlertaModalExc(TP_ALERTA_ERRO,o):"OK"==t?(fCriarAlertaPrinc(TP_ALERTA_SUCESSO,o),$("#txtDelEmprProvId").val(""),$("#PopModalDelEmprProv").modal("hide"),fCarregarGrid(a),!0):(fCriarAlertaModalExc(TP_ALERTA_ERRO,o),!1)},error:function(a){$("#PopModalDelEmprProv").modal("hide"),finalizarAnimacaoExcluir(),fCriarAlertaModalExc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}})}catch(a){$("#PopModalDelEmprProv").modal("hide"),finalizarAnimacaoExcluir(),fCriarAlertaModalExc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}$(document).ready(function(){$("#MnPrincEmpresaProv").addClass("active open"),fLimparAreaAlertaPrinc(),fLimparAreaAlertaModalCad(),fLimparAreaAlertaModalExc()});