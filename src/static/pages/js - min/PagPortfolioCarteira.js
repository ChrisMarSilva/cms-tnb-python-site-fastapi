async function fCarregarListaPortfolios(a,o=null){try{promise=new Promise((o,r)=>{$("#btnPortAddAtivo").hide(),$("#btnPortAltPortfolio").hide(),$("#btnPortExcPortfolio").hide(),$("#btnPortAddPortfolio").show(),$("#TabPortfolios").empty(),$("#TabPortfolios").append('<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioBdrs"    data-toggle="tab" href="#PortfolioBdrs"    role="tab" aria-controls="PortfolioBdrs"    aria-selected="false" title="Portfólio BDRs - Todos os Bdrs da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; Minhas BDRs   </a> </li>'),$("#TabPortfolios").append('<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioIndices" data-toggle="tab" href="#PortfolioIndices" role="tab" aria-controls="PortfolioIndices" aria-selected="false" title="Portfólio ETFs - Todos os Etfs da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; Meus ETFs   </a> </li>'),$("#TabPortfolios").append('<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioFundos"  data-toggle="tab" href="#PortfolioFundos"  role="tab" aria-controls="PortfolioFundos"  aria-selected="false" title="Portfólio FIIs - Todos os Fiis da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; Meus FIIs     </a> </li>'),$("#TabPortfolios").append('<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioAcoes"   data-toggle="tab" href="#PortfolioAcoes"   role="tab" aria-controls="PortfolioAcoes"   aria-selected="false" title="Portfólio Ações - Todos as Ações da Carteira">    <i class="fa fa-bar-chart"></i>&nbsp; Minhas Ações  </a> </li>'),$("#TabPortfolios").append('<li class="nav-item"> <a style="font-size: 10px; " class="nav-link active" id="AbaPortfolio"        data-toggle="tab" href="#Portfolio"        role="tab" aria-controls="Portfolio"        aria-selected="true"  title="Portfólio Completo - Todos os Ativos da Carteira"><i class="fa fa-bar-chart"></i>&nbsp; Meu Portfólio </a> </li>'),$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"listas/lista_nomes_carteira_user",success:function(o){var r=o.data.Resultado,t=o.data.Mensagem,l=o.data.Lista;return"NSESSAO"==r?($(location).attr("href",a+"/login"),!1):"NOK"==r?(fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO,t),!1):"FALHA"==r?(fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,t),!1):"OK"==r?($("#TabPortfolios").empty(),l.length>0&&$.each(l,function(a,o){$('<li class="nav-item"> <a style="font-size: 10px; " class="nav-link" id="Aba'+o[0]+'" data-toggle="tab" href="#'+o[0]+'" role="tab" aria-controls="'+o[0]+'" aria-selected="false" title="Portfólio Personalizado - Ativos Selecionados da Carteira"><i class="fa fa-sliders"></i>&nbsp; '+o[1]+"</a> </li>").appendTo("#TabPortfolios")}),$("#TabPortfolios").append('<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioIndices" data-toggle="tab" href="#PortfolioIndices" role="tab" aria-controls="PortfolioIndices" aria-selected="false" title="Portfólio Indices - Todos os Indices da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; Meus ETFs   </a> </li>'),$("#TabPortfolios").append('<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioFundos"  data-toggle="tab" href="#PortfolioFundos"  role="tab" aria-controls="PortfolioFundos"  aria-selected="false" title="Portfólio Fundos - Todos os Fundos da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; Meus FIIs     </a> </li>'),$("#TabPortfolios").append('<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioAcoes"   data-toggle="tab" href="#PortfolioAcoes"   role="tab" aria-controls="PortfolioAcoes"   aria-selected="false" title="Portfólio Ações - Todos as Ações da Carteira">    <i class="fa fa-bar-chart"></i>&nbsp; Minhas Ações  </a> </li>'),$("#TabPortfolios").append('<li class="nav-item"> <a style="font-size: 10px; " class="nav-link active" id="AbaPortfolio"        data-toggle="tab" href="#Portfolio"        role="tab" aria-controls="Portfolio"        aria-selected="true"  title="Portfólio Completo - Todos os Ativos da Carteira"><i class="fa fa-bar-chart"></i>&nbsp; Meu Portfólio </a> </li>'),$('#TabPortfolios a[data-toggle="tab"]').on("shown.bs.tab",function(o){fMontarPagina(a)}),!0):(fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,t),!1)},error:function(a){return fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}),o(!0)}).then(a=>{}).catch(a=>{fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)})}catch(a){fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fAbrirModalDetalhePortfolio(a,o){try{if(fLimparAreaAlerta("AreaAlertaModalCad"),$("#PopModalDetalhePortfolioTit").html(" - "+o),$("#txtCadPortfolioId").val(""),$("#txtCadPortfolioNome").val(""),"Alterar"==o||"Visualizar"==o){var r=fGetAbaIdPortfolio();if(""==r)return void fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO,"Id. Portfólio não informado!");var t=$("#Aba"+r).html();t=t.replace('<i class="fa fa-sliders"></i>&nbsp;',""),$("#txtCadPortfolioId").val(r),$("#txtCadPortfolioNome").val(t)}$("#PopModalDetalhePortfolio").modal({backdrop:"static"}),$("#PopModalDetalhePortfolio").on("shown.bs.modal",function(){$("#txtCadPortfolioNome").focus()})}catch(a){fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fValidarDadosPortfolio(){try{return fLimparAreaAlerta("AreaAlertaModalCad"),""!=$("#txtCadPortfolioNome").val()||(fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_AVISO,"Por favor, preencha o campo Nome!"),!1)}catch(a){return fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_ERRO,MSG_ALERTA_ERRO),!1}}function fSalvarDadosPortfolio(a){try{if(!fValidarDadosPortfolio())return!1;iniciarAnimacaoSalvar();var o=$("#txtCadPortfolioId").val(),r=$("#txtCadPortfolioNome").val();$.ajax({cache:"false",dataType:"json",async:!0,type:"POST",url:a+"portfolio/salvarPortfolio",data:{Id:o,Nome:r},success:function(t){finalizarAnimacaoSalvar();var l=t.data.Resultado,i=t.data.Mensagem;if("NSESSAO"==l)return $(location).attr("href",a+"/login"),!1;"NOK"!=l?"FALHA"!=l&&"OK"==l?($("#PopModalDetalhePortfolio").modal("hide"),fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO,"Dados salvo com sucesso!"),""==o?fRecarregarPagina(a,o):$("#Aba"+o).html('<i class="fa fa-sliders"></i>&nbsp;'+r)):fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_ERRO,i):fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_AVISO,i)},error:function(a){finalizarAnimacaoSalvar(),fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}})}catch(a){return finalizarAnimacaoSalvar(),void CriarAlertaModal(TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fAbrirModalRemoverPortfolio(){try{$("#txtDelPortfolioId").val("");var a=fGetAbaIdPortfolio();if(""==a)return void fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO,"Id. Portfólio não informado!");$("#PopModalDelPortfolio").modal({backdrop:"static"}),$("#txtDelPortfolioId").val(a)}catch(a){$("#PopModalDelPortfolio").modal("hide"),finalizarAnimacaoExcluir(),fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}function fExcluirDadosPortfolio(a){try{finalizarAnimacaoExcluir();var o=$("#txtDelPortfolioId").val();if(""==o)return void fCriarAlerta("AreaAlertaModalExc",TP_ALERTA_AVISO,"Id. Portfólio não informado!");iniciarAnimacaoExcluir(),$.ajax({dataType:"json",type:"post",url:a+"portfolio/excluirPortfolio",data:{IdPortfolio:o},success:function(r){finalizarAnimacaoExcluir();var t=r.data.Resultado,l=r.data.Mensagem;return"NSESSAO"==t?($(location).attr("href",a+"/login"),!1):"NOK"==t?(fCriarAlerta("AreaAlertaModalExc",TP_ALERTA_AVISO,l),!1):"FALHA"==t?void fCriarAlerta("AreaAlertaModalExc",TP_ALERTA_ERRO,l):"OK"==t?($("#txtDelPortfolioId").val(""),$("#PopModalDelPortfolio").modal("hide"),fRecarregarPagina(a,o),!0):(fCriarAlerta("AreaAlertaModalExc",TP_ALERTA_ERRO,l),!1)},error:function(a){$("#PopModalDelPortfolio").modal("hide"),finalizarAnimacaoExcluir(),fCriarAlerta("AreaAlertaModalExc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}})}catch(a){$("#PopModalDelPortfolio").modal("hide"),finalizarAnimacaoExcluir(),fCriarAlerta("AreaAlertaModalExc",TP_ALERTA_ERRO,MSG_ALERTA_ERRO)}}