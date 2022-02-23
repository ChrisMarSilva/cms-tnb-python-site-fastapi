function fMontaDadosOperacao(a){var e=a[0],r=a[1],t=a[2],l=a[3],o=a[4],s=a[5];return"C"==r?'<small style="font-size:13px;" class="font-italic text-muted">'+colcarFormacataoData(e)+" - <b>"+t+"</b> "+colcarFormacataoInteiro(l)+" x R$ "+o+" = <b>R$ "+s+"</b></small><br/>":"B"==r?'<small style="font-size:13px;" class="font-italic text-muted">'+colcarFormacataoData(e)+" - <b>"+t+"</b> "+colcarFormacataoInteiro(l)+" x R$ "+o+" = <b>R$ "+s+"</b></small><br/>":"V"==r?'<small style="font-size:13px;" class="font-italic text-muted">'+colcarFormacataoData(e)+" - <b>"+t+"</b> "+colcarFormacataoInteiro(l)+" x R$ "+o+" = <b>R$ "+s+"</b></small><br/>":""}async function fCarrgarDadosOperacoes(a){try{promise=new Promise((e,r)=>{$("#DivConteudoOperCompra").html(""),$("#DivConteudoOperVenda").html(""),$("#DivConteudoOperBonus").html(""),$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"principal/carregarOperacoesAcoes",data:{TipoInvest:"ACAO"},success:function(e){var r=e.data.Resultado,t=e.data.Mensagem,l=e.data.Lista;if("NSESSAO"==r)return $(location).attr("href",a+"/login"),!1;if("NOK"==r)return fCriarAlertaPrinc(TP_ALERTA_AVISO,t),!1;if("FALHA"==r)return fCriarAlertaPrinc(TP_ALERTA_ERRO,t),!1;if("OK"!=r)return fCriarAlertaPrinc(TP_ALERTA_ERRO,t),!1;var o="",s="",c=0,i=0;l&&l.length>0&&$.each(l,function(a,e){"C"==e[1]?(c+=parseFloat(GetValorDecimal(e[5])),o+=fMontaDadosOperacao(e)):"B"==e[1]?(c+=parseFloat(GetValorDecimal(e[5])),o+=fMontaDadosOperacao(e)):"V"==e[1]&&(i+=parseFloat(GetValorDecimal(e[5])),s+=fMontaDadosOperacao(e))}),""==o&&(o=' <small style="font-size:14px;" class="font-italic text-muted text-center">Nenhuma Compra realizada...</small><br/>'),$("#DivConteudoOperCompra").append('<div class="row clearfix item text-center">  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12">     <small style="font-size:13px;" class="text-success font-weight-bold text-center">TOTAL DE COMPRAS - R$ '+fMascaraValor(c)+"</small><br/>   "+o+"  </div></div>"),""==s&&(s=' <small style="font-size:14px;" class="font-italic text-muted text-center">Nenhuma Venda realizada...</small><br/>'),$("#DivConteudoOperVenda").append('<div class="row clearfix item text-center">  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12">     <small style="font-size:13px;" class="text-danger font-weight-bold text-center">TOTAL DE VENDAS - R$ '+fMascaraValor(i)+"</small><br/>   "+s+"  </div></div>")},error:function(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}),e(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fLimparDadosInvestidores(),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosOperacoesFII(a){try{promise=new Promise((e,r)=>{$("#DivConteudoOperFIICompra").html(""),$("#DivConteudoOperFIIVenda").html(""),$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"principal/carregarOperacoesFiis",data:{TipoInvest:"FII"},success:function(e){var r=e.data.Resultado,t=e.data.Mensagem,l=e.data.Lista;if("NSESSAO"==r)return $(location).attr("href",a+"/login"),!1;if("NOK"==r)return fCriarAlertaPrinc(TP_ALERTA_AVISO,t),!1;if("FALHA"==r)return fCriarAlertaPrinc(TP_ALERTA_ERRO,t),!1;if("OK"!=r)return fCriarAlertaPrinc(TP_ALERTA_ERRO,t),!1;var o="",s="",c=0,i=0;l&&l.length>0&&$.each(l,function(a,e){"C"==e[1]?(c+=parseFloat(GetValorDecimal(e[5])),o+=fMontaDadosOperacao(e)):"B"==e[1]?(c+=parseFloat(GetValorDecimal(e[5])),o+=fMontaDadosOperacao(e)):"V"==e[1]&&(i+=parseFloat(GetValorDecimal(e[5])),s+=fMontaDadosOperacao(e))}),""==o&&(o=' <small style="font-size:14px;" class="font-italic text-muted">Nenhuma Compra realizada...</small><br/>'),$("#DivConteudoOperFIICompra").append('<div class="row clearfix item text-center">  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12">     <small style="font-size:13px;" class="text-success font-weight-bold">TOTAL DE COMPRAS - R$ '+fMascaraValor(c)+"</small><br/>   "+o+"  </div></div>"),""==s&&(s=' <small style="font-size:14px;" class="font-italic text-muted">Nenhuma Venda realizada...</small><br/>'),$("#DivConteudoOperFIIVenda").append('<div class="row clearfix item text-center">  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12">     <small style="font-size:13px;" class="text-danger font-weight-bold">TOTAL DE VENDAS - R$ '+fMascaraValor(i)+"</small><br/>   "+s+"  </div></div>")},error:function(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}),e(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fLimparDadosInvestidores(),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosOperacoesETF(a){try{promise=new Promise((e,r)=>{$("#DivConteudoOperETFCompra").html(""),$("#DivConteudoOperETFVenda").html(""),$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"principal/carregarOperacoesEtfs",data:{TipoInvest:"ETF"},success:function(e){var r=e.data.Resultado,t=e.data.Mensagem,l=e.data.Lista;if("NSESSAO"==r)return $(location).attr("href",a+"/login"),!1;if("NOK"==r)return fCriarAlertaPrinc(TP_ALERTA_AVISO,t),!1;if("FALHA"==r)return fCriarAlertaPrinc(TP_ALERTA_ERRO,t),!1;if("OK"!=r)return fCriarAlertaPrinc(TP_ALERTA_ERRO,t),!1;var o="",s="",c=0,i=0;l&&l.length>0&&$.each(l,function(a,e){"C"==e[1]?(c+=parseFloat(GetValorDecimal(e[5])),o+=fMontaDadosOperacao(e)):"B"==e[1]?(c+=parseFloat(GetValorDecimal(e[5])),o+=fMontaDadosOperacao(e)):"V"==e[1]&&(i+=parseFloat(GetValorDecimal(e[5])),s+=fMontaDadosOperacao(e))}),""==o&&(o=' <small style="font-size:14px;" class="font-italic text-muted">Nenhuma Compra realizada...</small><br/>'),$("#DivConteudoOperETFCompra").append('<div class="row clearfix item text-center">  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12">     <small style="font-size:13px;" class="text-success font-weight-bold">TOTAL DE COMPRAS - R$ '+fMascaraValor(c)+"</small><br/>   "+o+"  </div></div>"),""==s&&(s=' <small style="font-size:14px;" class="font-italic text-muted">Nenhuma Venda realizada...</small><br/>'),$("#DivConteudoOperETFVenda").append('<div class="row clearfix item text-center">  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12">     <small style="font-size:13px;" class="text-danger font-weight-bold">TOTAL DE VENDAS - R$ '+fMascaraValor(i)+"</small><br/>   "+s+"  </div></div>")},error:function(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}),e(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fLimparDadosInvestidores(),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}async function fCarrgarDadosOperacoesBDR(a){try{promise=new Promise((e,r)=>{$("#DivConteudoOperBDRCompra").html(""),$("#DivConteudoOperBDRVenda").html(""),$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"principal/carregarOperacoesBdrs",data:{TipoInvest:"BDR"},success:function(e){var r=e.data.Resultado,t=e.data.Mensagem,l=e.data.Lista;if("NSESSAO"==r)return $(location).attr("href",a+"/login"),!1;if("NOK"==r)return fCriarAlertaPrinc(TP_ALERTA_AVISO,t),!1;if("FALHA"==r)return fCriarAlertaPrinc(TP_ALERTA_ERRO,t),!1;if("OK"!=r)return fCriarAlertaPrinc(TP_ALERTA_ERRO,t),!1;var o="",s="",c=0,i=0;l&&l.length>0&&$.each(l,function(a,e){"C"==e[1]?(c+=parseFloat(GetValorDecimal(e[5])),o+=fMontaDadosOperacao(e)):"B"==e[1]?(c+=parseFloat(GetValorDecimal(e[5])),o+=fMontaDadosOperacao(e)):"V"==e[1]&&(i+=parseFloat(GetValorDecimal(e[5])),s+=fMontaDadosOperacao(e))}),""==o&&(o=' <small style="font-size:14px;" class="font-italic text-muted">Nenhuma Compra realizada...</small><br/>'),$("#DivConteudoOperBDRCompra").append('<div class="row clearfix item text-center">  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12">     <small style="font-size:13px;" class="text-success font-weight-bold">TOTAL DE COMPRAS - R$ '+fMascaraValor(c)+"</small><br/>   "+o+"  </div></div>"),""==s&&(s=' <small style="font-size:14px;" class="font-italic text-muted">Nenhuma Venda realizada...</small><br/>'),$("#DivConteudoOperBDRVenda").append('<div class="row clearfix item text-center">  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12">     <small style="font-size:13px;" class="text-danger font-weight-bold">TOTAL DE VENDAS - R$ '+fMascaraValor(i)+"</small><br/>   "+s+"  </div></div>")},error:function(a){fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}),e(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fLimparDadosInvestidores(),fCriarAlertaPrinc(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}