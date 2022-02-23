

async function fCarregarListaPortfolios( urlPadrao, IdPortfolio = null){
	try {		

		 promise = new Promise( (resolve, reject) => {
			
			$('#btnPortAddAtivo').hide(); 
			$('#btnPortAltPortfolio').hide(); 
			$('#btnPortExcPortfolio').hide(); 	
			$('#btnPortAddPortfolio').show();

			$('#TabPortfolios').empty(); 
			$("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioBdrs"    data-toggle="tab" href="#PortfolioBdrs"    role="tab" aria-controls="PortfolioBdrs"    aria-selected="false" title="Portfólio BDRs - Todos os Bdrs da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; Minhas BDRs   </a> </li>' );
			$("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioIndices" data-toggle="tab" href="#PortfolioIndices" role="tab" aria-controls="PortfolioIndices" aria-selected="false" title="Portfólio ETFs - Todos os Etfs da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; Meus ETFs   </a> </li>' );
			$("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioFundos"  data-toggle="tab" href="#PortfolioFundos"  role="tab" aria-controls="PortfolioFundos"  aria-selected="false" title="Portfólio FIIs - Todos os Fiis da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; Meus FIIs     </a> </li>' );
			$("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioAcoes"   data-toggle="tab" href="#PortfolioAcoes"   role="tab" aria-controls="PortfolioAcoes"   aria-selected="false" title="Portfólio Ações - Todos as Ações da Carteira">    <i class="fa fa-bar-chart"></i>&nbsp; Minhas Ações  </a> </li>' );
			$("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="nav-link active" id="AbaPortfolio"        data-toggle="tab" href="#Portfolio"        role="tab" aria-controls="Portfolio"        aria-selected="true"  title="Portfólio Completo - Todos os Ativos da Carteira"><i class="fa fa-bar-chart"></i>&nbsp; Meu Portfólio </a> </li>' );
		
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "listas/lista_nomes_carteira_user",
				// data    : {  },
				success: function(result) {  
				
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista; 

					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, mensagem); 
						return false;
					} else if (resultado == "FALHA") {
						fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem); 
						return false;
					} else if (resultado == "OK") {	
							
						$('#TabPortfolios').empty(); 

						if ( lista.length > 0 )
							$.each(lista, function (index, value) {
								$('<li class="nav-item"> <a style="font-size: 10px; " class="nav-link" id="Aba'+value[0]+'" data-toggle="tab" href="#'+value[0]+'" role="tab" aria-controls="'+value[0]+'" aria-selected="false" title="Portfólio Personalizado - Ativos Selecionados da Carteira"><i class="fa fa-sliders"></i>&nbsp; '+value[1]+'</a> </li>').appendTo('#TabPortfolios');
							});

						$("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioIndices" data-toggle="tab" href="#PortfolioIndices" role="tab" aria-controls="PortfolioIndices" aria-selected="false" title="Portfólio Indices - Todos os Indices da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; Meus ETFs   </a> </li>' );
						$("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioFundos"  data-toggle="tab" href="#PortfolioFundos"  role="tab" aria-controls="PortfolioFundos"  aria-selected="false" title="Portfólio Fundos - Todos os Fundos da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; Meus FIIs     </a> </li>' );
						$("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="nav-link"        id="AbaPortfolioAcoes"   data-toggle="tab" href="#PortfolioAcoes"   role="tab" aria-controls="PortfolioAcoes"   aria-selected="false" title="Portfólio Ações - Todos as Ações da Carteira">    <i class="fa fa-bar-chart"></i>&nbsp; Minhas Ações  </a> </li>' );
						$("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="nav-link active" id="AbaPortfolio"        data-toggle="tab" href="#Portfolio"        role="tab" aria-controls="Portfolio"        aria-selected="true"  title="Portfólio Completo - Todos os Ativos da Carteira"><i class="fa fa-bar-chart"></i>&nbsp; Meu Portfólio </a> </li>' );

						$('#TabPortfolios a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
							// e.target        // newly activated tab
							// e.relatedTarget // previous active tab
							fMontarPagina( urlPadrao );
						});

						return true;
					} else {
						fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem); 
						return false;
					}
					
				},
				error: function(data) {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
					return false;
				}
			});	

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
	
	} catch(e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

function fAbrirModalDetalhePortfolio( urlPadrao, TipoModal ) {
    try {

		fLimparAreaAlerta("AreaAlertaModalCad"); 
		
    	$("#PopModalDetalhePortfolioTit").html(" - "+TipoModal);
		$("#txtCadPortfolioId").val(   "" );
		$("#txtCadPortfolioNome").val( "" );
		
		if ( TipoModal == "Alterar" || TipoModal == "Visualizar" ){
				
			var IdPortfolio = fGetAbaIdPortfolio();
			
			if ( IdPortfolio == "" ){
				fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, 'Id. Portfólio não informado!');
				return;
			}
			
			var NomePortfolio = $("#Aba"+IdPortfolio).html();
			NomePortfolio     = NomePortfolio.replace('<i class="fa fa-sliders"></i>&nbsp;', "");
			
			$("#txtCadPortfolioId").val(   IdPortfolio   );
			$("#txtCadPortfolioNome").val( NomePortfolio );
		}

		//$("#txtCadPortfolioNome").focus();
		$('#PopModalDetalhePortfolio').modal({backdrop: 'static'});

		$('#PopModalDetalhePortfolio').on('shown.bs.modal', function() {
			$('#txtCadPortfolioNome').focus();
		})

    } catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fValidarDadosPortfolio() {	
	try {
		
		fLimparAreaAlerta("AreaAlertaModalCad"); 
		
		if( $("#txtCadPortfolioNome").val() == "" ){
			fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_AVISO, "Por favor, preencha o campo Nome!");
			return false;
		}	
		
		return true;
	
	} catch (e) {
		fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return false;
	} 
}

function fSalvarDadosPortfolio( urlPadrao ){
	try {
		
		if ( !fValidarDadosPortfolio() )
			return false;

		iniciarAnimacaoSalvar();

		var Id   = $("#txtCadPortfolioId").val(); 
		var Nome = $("#txtCadPortfolioNome").val(); 
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "portfolio/salvarPortfolio",
			data    : { Id : Id, Nome : Nome },
			success: function(result) {  
			
				finalizarAnimacaoSalvar();
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					$("#PopModalDetalhePortfolio").modal("hide");					
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					if ( Id == '' ) {
						fRecarregarPagina( urlPadrao, Id );
					}
					else{
						$("#Aba"+Id).html( '<i class="fa fa-sliders"></i>&nbsp;'+Nome );
					}		
				} else {
					fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function(data) {
				finalizarAnimacaoSalvar();
				fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});
		
	} catch (e) {
		finalizarAnimacaoSalvar();
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function fAbrirModalRemoverPortfolio() {
    try {

       $("#txtDelPortfolioId").val("");
	   
	   var IdPortfolio = fGetAbaIdPortfolio();
	   
       if ( IdPortfolio  == "" ){
          fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, 'Id. Portfólio não informado!'); 
          return;
        }
      
       $("#PopModalDelPortfolio").modal({backdrop: "static"});
	   
       $("#txtDelPortfolioId").val( IdPortfolio );

    } catch (e) {
        $("#PopModalDelPortfolio").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fExcluirDadosPortfolio( urlPadrao ) {
    try {

		finalizarAnimacaoExcluir();

		var IdPortfolio = $("#txtDelPortfolioId").val();
		if ( IdPortfolio == "" ){
			fCriarAlerta("AreaAlertaModalExc",TP_ALERTA_AVISO, 'Id. Portfólio não informado!');
			return;
		}

		iniciarAnimacaoExcluir();
	  
		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "portfolio/excluirPortfolio",
			data: {  IdPortfolio : IdPortfolio },
			success: function (result) {
				
				finalizarAnimacaoExcluir();				
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaModalExc",TP_ALERTA_AVISO, mensagem); 
					return false;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaModalExc",TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {					
				    //fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO, mensagem); 
					$("#txtDelPortfolioId").val("");
					$("#PopModalDelPortfolio").modal("hide");
					fRecarregarPagina( urlPadrao, IdPortfolio );
					return true;
				} else {
					fCriarAlerta("AreaAlertaModalExc",TP_ALERTA_ERRO, mensagem); 
					return false;
				}
				
			},
			error: function (data) {
				$("#PopModalDelPortfolio").modal("hide");
				finalizarAnimacaoExcluir();
				fCriarAlerta("AreaAlertaModalExc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
			}
		});

    } catch (e) {
        $("#PopModalDelPortfolio").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlerta("AreaAlertaModalExc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}