function fMostrarCalcVlrLiq(){try{"J"==$("#selDivTipo").val()?$("#DivCalcVlrLiq").show():$("#DivCalcVlrLiq").hide(),$("#txtDivCalcVlrLiq").attr("checked",!1)}catch(a){fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fMostrarValorBruto(){try{var a=$("#selDivTipo").val(),r=$("#txtDivCalcVlrLiq").is(":checked");"J"==a&&1==r?($("#DivPrecoBruto").show(),$("#DivTotalBruto").show(),$("#txtDivPreco").attr("readonly","readonly"),$("#txtDivPrecoBruto").val($("#txtDivPreco").val()),$("#txtDivPrecoBruto").bind("keyup change",function(){fCalcularDividendo()}),$("#txtDivPreco").unbind("keyup"),$("#txtDivPreco").unbind("change")):($("#DivPrecoBruto").hide(),$("#DivTotalBruto").hide(),$("#txtDivPreco").removeAttr("readonly"),$("#txtDivPreco").val($("#txtDivPrecoBruto").val()),$("#txtDivPreco").bind("keyup change",function(){fCalcularDividendo()}),$("#txtDivPrecoBruto").unbind("keyup"),$("#txtDivPrecoBruto").unbind("change"))}catch(a){fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fCalcularDividendo(){try{$("#txtDivTotalBruto").val("0,00"),$("#txtDivTotal").val("0,00");var a=$("#selDivTipo").val(),r=$("#txtDivCalcVlrLiq").is(":checked"),t=GetValorInteiro($("#txtDivQuant").val()),e=GetValorDecimalMaior($("#txtDivPrecoBruto").val()),o=GetValorDecimalMaior($("#txtDivPreco").val()),l=0,i=0;if(t<=0)return!1;if(e<=0&&o<=0)return!1;"J"==a&&1==r?(o=0,e>0&&(o=e-15*e/100),$("#txtDivPreco").val(fMascaraValorMaior(o))):(e=0,o>0&&(e=o),$("#txtDivPrecoBruto").val($("#txtDivPreco").val())),e>0&&(l=e*t),o>0&&(i=o*t),$("#txtDivTotalBruto").val(fMascaraValor(l)),$("#txtDivTotal").val(fMascaraValor(i))}catch(a){fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fLimparDadosModalRend(){fLimparAreaAlerta("AreaAlertaModalCadProv"),$("#txtDivId").val(""),$("#selDivTipo")[0].selectedIndex=2,$("#selDivAtivo").val(""),$("#selDivCorretora")[0].selectedIndex=2,$("#txtDivDataEx").val(""),$("#txtDivDataPagto").val(""),$("#txtDivQuant").val("0"),$("#txtDivCalcVlrLiq").attr("checked",!1),$("#txtDivPrecoBruto").val("0,00"),$("#txtDivPreco").val("0,00"),$("#txtDivTotalBruto").val("0,00"),$("#txtDivTotal").val("0,00"),fDefinirPadraoSelect("selDivTipo"),fDefinirPadraoSelect("selDivAtivo"),fDefinirPadraoSelect("selDivCorretora"),fMostrarCalcVlrLiq(),fMostrarValorBruto(),$("#BtnDivQuantAtual").hide()}function fAbrirModalDetalheRend(a,r,t,e){try{fLimparDadosModalRend(),$("#PopModalDetalheRendTit").html(""),$("#PopModalDetalheRendTit").html(" - "+e),$("#selDivTipo").removeAttr("readonly"),$("#selDivTipo").removeAttr("disabled"),$("#selDivTipo").removeClass("disabled"),$("#selDivAtivo").removeAttr("readonly"),$("#selDivAtivo").removeClass("disabled"),$("#selDivAtivo").removeAttr("disabled"),$("#selDivCorretora").removeAttr("readonly"),$("#selDivCorretora").removeAttr("disabled"),$("#selDivCorretora").removeClass("disabled"),$("#txtDivDataEx").removeAttr("readonly"),$("#txtDivDataPagto").removeAttr("readonly"),$("#txtDivQuant").removeAttr("readonly"),$("#txtDivCalcVlrLiq").removeAttr("readonly"),$("#txtDivCalcVlrLiq").removeAttr("disabled"),$("#txtDivCalcVlrLiq").removeClass("disabled"),$("#txtDivPrecoBruto").removeAttr("readonly"),$("#txtDivPreco").removeAttr("readonly"),$("#BtnModalDetalheRendSalvar").show(),"Visualizar"==e&&$("#BtnModalDetalheRendSalvar").hide(),"Novo"==e&&($("#PopModalDetalheRend").modal({backdrop:"static"}),$("#txtDivDataEx").val(fDataAtual()),$("#txtDivDataPagto").val(fDataAtual()),$("#BtnDivQuantAtual").show()),"Alterar"!=e&&"Visualizar"!=e||fCarregarDadosModalDetalheRend(a,r,t,e),$("#selDivAtivo").focus()}catch(a){fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fAbrirModalDetalheRendCalend(a,r,t,e,o,l,i,d="100"){try{fAbrirModalDetalheRend(a,"","","Novo"),$("#txtDivId").val(""),$("#selDivTipo").val(r),$("#selDivAtivo").val(t),$("#selDivCorretora").val(""),$("#txtDivDataEx").val(e),$("#txtDivDataPagto").val(o),$("#txtDivQuant").val(d.toString()),fDefinirPadraoSelect("selDivTipo"),fDefinirPadraoSelect("selDivAtivo"),fDefinirPadraoSelect("selDivCorretora"),"J"==r?$("#DivCalcVlrLiq").show():($("#DivCalcVlrLiq").hide(),$("#txtDivCalcVlrLiq").attr("checked",!1)),fMostrarValorBruto(),$("#txtDivPrecoBruto").val(l),$("#txtDivPreco").val(l),fCalcularDividendo()}catch(a){fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fCarregarDadosModalDetalheRend(a,r,t,e){try{if(""==r)return void fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_AVISO,"Id. Provendo não informado!");if(""==t)return void fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_AVISO,"Cód. Ativo não informado!");$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"proventos/carregar",data:{IdRent:r,CodAtivo:t},success:function(r){var t=r.data.Resultado,o=r.data.Mensagem,l=r.data.Dados;if("NSESSAO"==t)return $(location).attr("href",a+"/login"),!1;"NOK"==t?fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_AVISO,o):"FALHA"==t?fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,o):"OK"==t&&l.IdRent?($("#txtDivId").val(l.IdRent),$("#selDivTipo").val(l.Tipo),$("#selDivAtivo").val(l.CodAtivo),$("#selDivCorretora").val(l.Corretora),$("#txtDivDataEx").val(l.DataEx),$("#txtDivDataPagto").val(l.DataPagto),$("#txtDivQuant").val(l.Quant),fDefinirPadraoSelect("selDivTipo"),fDefinirPadraoSelect("selDivAtivo"),fDefinirPadraoSelect("selDivCorretora"),"J"==l.Tipo?($("#DivCalcVlrLiq").show(),"S"==l.CalcVlrLiq&&$("#txtDivCalcVlrLiq").attr("checked",!0)):($("#DivCalcVlrLiq").hide(),$("#txtDivCalcVlrLiq").attr("checked",!1)),fMostrarValorBruto(),$("#txtDivPrecoBruto").val(l.PrecoBruto),$("#txtDivPreco").val(l.Preco),fCalcularDividendo(),"Visualizar"==e&&($("#selDivTipo").attr("readonly","readonly"),$("#selDivTipo").addClass("disabled"),$("#selDivTipo").attr("disabled","disabled"),$("#selDivAtivo").attr("readonly","readonly"),$("#selDivAtivo").attr("disabled","disabled"),$("#selDivAtivo").addClass("disabled"),$("#selDivCorretora").attr("readonly","readonly"),$("#selDivCorretora").attr("disabled","disabled"),$("#selDivCorretora").addClass("disabled"),$("#txtDivDataEx").attr("readonly","readonly"),$("#txtDivDataPagto").attr("readonly","readonly"),$("#txtDivQuant").attr("readonly","readonly"),$("#txtDivCalcVlrLiq").attr("readonly","readonly"),$("#txtDivCalcVlrLiq").attr("disabled","disabled"),$("#txtDivCalcVlrLiq").addClass("disabled"),$("#txtDivPrecoBruto").attr("readonly","readonly"),$("#txtDivPreco").attr("readonly","readonly")),$("#PopModalDetalheRend").modal({backdrop:"static"})):fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,o)},error:function(a){fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}})}catch(a){fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fBuscarQuantAtualRend(a){try{fLimparAreaAlerta("AreaAlertaModalCadProv"),$("#txtDivQuant").val("0"),fCalcularDividendo();var r=$("#selDivAtivo").val().trim();if(""==r)return;$.ajax({dataType:"json",type:"post",url:a+"operacoes/quantidade",data:{CodAtivo:r},success:function(r){var t=r.data.Resultado,e=r.data.Mensagem,o=r.data.Dados;return"NSESSAO"==t?($(location).attr("href",a+"/login"),!1):"NOK"==t?(fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_AVISO,e),!1):"FALHA"==t?void fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,e):"OK"==t?(o.QuantAtual&&$("#txtDivQuant").val(o.QuantAtual),fCalcularDividendo(),!0):(fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,e),!1)},error:function(a){fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}})}catch(a){fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fValidarDadosRend(){try{fLimparAreaAlerta("AreaAlertaModalCadProv");var a=$("#selDivTipo").val(),r=$("#selDivAtivo").val(),t=$("#txtDivDataEx").val(),e=$("#txtDivDataPagto").val(),o=$("#txtDivQuant").val(),l=$("#txtDivPreco").val(),i="";return""==a&&(i+=" - Tipo<br/>"),""==r&&(i+=" - Cód. Ativo/Fundo<br/>"),""==t&&(i+=" - Data Ex.<br/>"),""==e&&(i+=" - Data Pagto<br/>"),""==o&&(i+=" - Quant.<br/>"),""!=l&&",00"!=l&&"0,00"!=l||(i+=" - Preço<br/>"),""==i||(fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_AVISO,"Os seguintes campos não estão preenchido: <br/>"+i),!1)}catch(a){return fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}function fSalvarDadosRend(a){try{if(!fValidarDadosRend())return!1;iniciarAnimacaoSalvar();var r=$("#txtDivId").val(),t=$("#selDivTipo").val(),e=$("#selDivAtivo").val(),o=$("#selDivCorretora").val(),l=$("#txtDivDataEx").val(),i=$("#txtDivDataPagto").val(),d=$("#txtDivQuant").val(),A="N",v=$("#txtDivPrecoBruto").val(),n=$("#txtDivPreco").val();$("#txtDivCalcVlrLiq").is(":checked")&&(A="S"),$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"proventos/salvar",data:{Id:r,Tipo:t,Ativo:e,Corretora:o,DataEx:l,DataPagto:i,Quant:d,CalcVlrLiq:A,PrecoBruto:v,Preco:n},success:function(t){finalizarAnimacaoSalvar();var e=t.data.Resultado,o=t.data.Mensagem;if("NSESSAO"==e)return $(location).attr("href",a+"/login"),!1;if("NOK"!=e)if("FALHA"!=e)if("OK"==e){var l=$(location).attr("pathname")||window.location.pathname,i=l.split("/").length-1;if(""!=l.split("/")[i].toUpperCase()&&(l=l.split("/")[i].toUpperCase()),l.toUpperCase()=="proventos".toUpperCase()||l.toUpperCase()=="/proventos/".toUpperCase()||l.toUpperCase()=="/proventos".toUpperCase())""==r?(fLimparDadosModalRend(),fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_SUCESSO,"Dados salvo com sucesso!"),$("#txtDivDataEx").val(fDataAtual()),$("#txtDivDataPagto").val(fDataAtual()),$("#BtnDivQuantAtual").show()):($("#PopModalDetalheRend").modal("hide"),fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO,"Dados salvo com sucesso!")),buscar_todos_codigos_proventos(a,"selRendAtivo",!1,!0,!1),fCarregarGrid(a);else if(l.toUpperCase()=="principal".toUpperCase()||l.toUpperCase()=="/principal/".toUpperCase()||l.toUpperCase()=="/principal".toUpperCase())$("#PopModalDetalheRend").modal("hide"),fCarrgarDadosProventos(a);else{if(l.toUpperCase()=="CEI".toUpperCase()||l.toUpperCase()=="/CEI/".toUpperCase()||l.toUpperCase()=="/CEI".toUpperCase())return $("#PopModalDetalheRend").modal("hide"),fAlterarSitProvCei(a,PagCeiLstIdProv,"",PagCeiSitLanc,0,!1),void fProcurarAlterarLinhaGridProv(a,PagCeiLstIdxTr,PagCeiSitLanc);$("#PopModalDetalheRend").modal("hide"),fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO,"Dados salvo com sucesso!")}}else fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,o);else fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,o);else fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_AVISO,o)},error:function(a,r,t){finalizarAnimacaoSalvar(),fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,a.responseText)}})}catch(a){return finalizarAnimacaoSalvar(),void fCriarAlerta("AreaAlertaModalCadProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fAprovarProventos(a,r,t){try{if(""==r)return fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO,"Id. Provento não Informado..."),!1;if(""==t)return fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO,"Cód. Ativo/Fundo não Informado..."),!1;$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"proventos/aprovar",data:{Id:r,CodAtivo:t},success:function(r){var t=r.data.Resultado,e=r.data.Mensagem;if("NSESSAO"==t)return $(location).attr("href",a+"/login"),!1;if("NOK"!=t)if("FALHA"!=t)if("OK"==t){var o=$(location).attr("pathname")||window.location.pathname,l=o.split("/").length-1;""!=o.split("/")[l].toUpperCase()&&(o=o.split("/")[l].toUpperCase()),o.toUpperCase()=="proventos".toUpperCase()||o.toUpperCase()=="/proventos/".toUpperCase()||o.toUpperCase()=="/proventos".toUpperCase()?(fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO,"Dados salvo com sucesso!"),fCarregarGrid(a)):o.toUpperCase()=="principal".toUpperCase()||o.toUpperCase()=="/principal/".toUpperCase()||o.toUpperCase()=="/principal".toUpperCase()?fCarrgarDadosProventos(a):fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO,"Dados salvo com sucesso!")}else fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,e);else fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,e);else fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO,e)},error:function(a){fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}})}catch(a){return void fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fChamarPagExclusaoRend(a,r){try{if($("#txtIdRendDel").val(""),$("#txtCodRendDel").val(""),""==a)return void fCriarAlertaPrinc(TP_ALERTA_AVISO,"Id. Provento não informado!");if(""==r)return void fCriarAlertaPrinc(TP_ALERTA_AVISO,"Cód. Aitvo não informado!");$("#PopModalDelRend").modal({backdrop:"static"}),$("#txtIdRendDel").val(a),$("#txtCodRendDel").val(r)}catch(a){$("#PopModalDelRend").modal("hide"),finalizarAnimacaoExcluir(),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fExcluirDadosRendimento(a,r,t){try{fLimparAreaAlerta("AreaAlertaModalImportProv"),finalizarAnimacaoExcluir();var e=$("#txtIdRendDel").val(),o=$("#txtCodRendDel").val();if(r&&(e=r),t&&(o=t),""==e)return r||fCriarAlertaModalExc(TP_ALERTA_AVISO,"Id. Provento não informado!"),void(r&&fCriarAlerta("AreaAlertaModalImportProv",TP_ALERTA_SUCESSO,"Id. Provento não informado!"));if(""==o)return t||fCriarAlertaModalExc(TP_ALERTA_AVISO,"Cód. Ativo não informado!"),void(t&&fCriarAlerta("AreaAlertaModalImportProv",TP_ALERTA_SUCESSO,"Cód. Ativo não informado!"));iniciarAnimacaoExcluir(),$.ajax({dataType:"json",type:"post",url:a+"proventos/excluir",data:{IdRend:e,CodAtivo:o},success:function(t){finalizarAnimacaoExcluir();var e=t.data.Resultado,o=t.data.Mensagem;if("NSESSAO"==e)return $(location).attr("href",a+"/login"),!1;if("NOK"==e)return r||fCriarAlertaModalExc(TP_ALERTA_AVISO,o),r&&fCriarAlerta("AreaAlertaModalImportProv",TP_ALERTA_AVISO,o),!1;if("FALHA"==e)return r||fCriarAlertaModalExc(TP_ALERTA_ERRO,o),void(r&&fCriarAlerta("AreaAlertaModalImportProv",TP_ALERTA_ERRO,o));if("OK"==e){var l=$(location).attr("pathname")||window.location.pathname,i=l.split("/").length-1;if(""!=l.split("/")[i].toUpperCase()&&(l=l.split("/")[i].toUpperCase()),l.toUpperCase()=="proventos".toUpperCase()||l.toUpperCase()=="/proventos".toUpperCase()||l.toUpperCase()=="/proventos/".toUpperCase()){if(r||(fCriarAlertaPrinc(TP_ALERTA_SUCESSO,o),$("#txtIdRendDel").val(""),$("#PopModalDelRend").modal("hide"),fCarregarGrid(a),buscar_todos_codigos_proventos(a,"selRendAtivo",!1,!0,!1)),r){var d=$("#TrImport"+r).closest("tr");d.fadeOut(400,function(){d.remove(),$("#GridImport tr").length<=1&&$("#AreaTableModalImportProv").html("")})}}else l.toUpperCase()!="principal".toUpperCase()&&l.toUpperCase()!="/principal/".toUpperCase()&&l.toUpperCase()!="/principal".toUpperCase()||(fCarrgarDadosProventos(a),$("#PopModalDelRend").modal("hide"));return!0}return r||fCriarAlertaModalExc(TP_ALERTA_ERRO,o),r&&fCriarAlerta("AreaAlertaModalImportProv",TP_ALERTA_ERRO,o),!1},error:function(a){$("#PopModalDelRend").modal("hide"),finalizarAnimacaoExcluir(),r||fCriarAlertaModalExc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),r&&fCriarAlerta("AreaAlertaModalImportProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}})}catch(a){$("#PopModalDelRend").modal("hide"),finalizarAnimacaoExcluir(),r||fCriarAlertaModalExc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO),r&&fCriarAlerta("AreaAlertaModalImportProv",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}