
$(document).ready(function() {
	
	//$(this).attr("title", "Fatos Relevantes - " + NOME_PROJETO);
	$("#MnPrincFatos").addClass("active open");
	
	$("#txtFatoEmpresa").val( ""              );
	//$("#txtFatoDataIni").val( fDataPrimeira() );
	//$("#txtFatoDataFim").val( fDataUltima()   );
	
	fLimparAreaAlertaPrinc();
});

function iniciarAnimacaoPesquisar() {
	$("#iRefresh").addClass("fa-spin");
	$("#btnFatoPesquisar").addClass("disabled");
	$("#btnFatoLimpar").addClass("disabled");
}

function finalizarAnimacaoPesquisa() {
	$("#iRefresh").removeClass("fa-spin");
	$("#btnFatoPesquisar").removeClass("disabled");
	$("#btnFatoLimpar").removeClass("disabled");
}

async function fCarregarGrid( urlPadrao, iPagAtual ){
  try {   

		 promise = new Promise( (resolve, reject) => {

				var DivListaFatos = $("#DivListaFatos");
				DivListaFatos.empty();
				
				var BtnPaginacao = $("#BtnPaginacao");
				BtnPaginacao.empty();

				fLimparAreaAlertaPrinc();	
				finalizarAnimacaoPesquisa();
				iniciarAnimacaoPesquisar();
		  
				var IdEmpresa = $("#txtFatoEmpresa").val();
				var DataIni   = ''; //$("#txtFatoDataIni").val().trim();
				var DataFim   = ''; //$("#txtFatoDataFim").val().trim();

				$.ajax({
					cache   : "false",
					dataType: "json",
					async   : true,
					type    : "POST",
					url     : urlPadrao + "fatos/gridAcao",
					data: {
		                TipoInvest: 'ACAO', 
		                IdEmpresa : IdEmpresa, 
		                DataIni   : tirarFormacataoData(DataIni), 
						DataFim   : tirarFormacataoData(DataFim),
						PagAtual  : iPagAtual
		            },
					success: function(result) {
						
						var resultado = result.data.Resultado; 
						var mensagem  = result.data.Mensagem; 
						var lista     = result.data.Lista;
						var PagAtual  = parseInt( result.data.PagAtual ); 
						var PagTotal  = parseInt( result.data.PagTotal ); 

						if (resultado == "NSESSAO") {
							$(location).attr('href', urlPadrao + '/login');
							return false;
						} else if (resultado == "NOK") {
							finalizarAnimacaoPesquisa();
							fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
							return;
						} else if (resultado == "FALHA") {
							finalizarAnimacaoPesquisa();
							fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
							return;
						}else if (resultado == "OK") {

							finalizarAnimacaoPesquisa();
							var Conteudo = '';

							if ( lista && lista.length > 0 ){

								Conteudo += '<ul style="margin-right: 5px; ">';
								
								$.each(lista, function (index, value) {

									var FatoId        = value[0];
									var FatoEmpresa   = value[1];
									var FatoData      = colcarFormacataoDataHora(value[2])
									FatoData          = FatoData.substring(0,16);
									var FatoLink      = value[3];
									var FatoAssunto   = value[4];
									var FatoConteudo  = value[5];
									var FatoProtocolo = value[6];
									
									 Conteudo += '<li style="list-style-type:circle; margin-bottom: 5px;">';
									 Conteudo += '<a title="Clique aqui para ver o conteúdo oficial" style="font-size: 12px; "href="'+FatoLink+'" target="_blank" class="text-dark">';
									 Conteudo += '<span class="font-weight-bold">'+FatoData+'</span>';
									 Conteudo += ' - <span class="font-weight-normal">Protocolo: '+FatoProtocolo+'</span>';
									 Conteudo += ' - <span class="text-primary font-weight-bold">'+FatoEmpresa+'</span>';
									 Conteudo += ' - <span class="font-text-muted weight-normal">'+FatoAssunto+'</span>';
									 Conteudo += '</a>';
									 Conteudo += '</li>';

								});

								Conteudo += '</ul>';
								DivListaFatos.html(Conteudo);

								if ( PagTotal && PagTotal > 1 ){
									if ( PagAtual > 1                                                                                                  ) BtnPaginacao.append('<li class="page-item"> <a class="page-link text-muted" href="javascript:void(0);" onclick="fCarregarGrid(\''+urlPadrao+'\',\''+(parseInt(PagAtual)-1)+'\');" title="Página Anterior" aria-label="Anterior"> <span aria-hidden="true">&laquo;</span> <span class="sr-only">Previous</span> </a> </li>');
									for (Num = 1; Num <= PagTotal; Num++) {
										if ( Num == 9 && PagTotal > 10                                                                                 ) BtnPaginacao.append('<li class="page-item disabled"> <a class="page-link text-muted disabled" href="javascript:void(0);"> ... </a></li>');
										if ( (Num <= 8) || ( Num == 9 && PagTotal <= 10 ) || ( Num == 10 && PagTotal <= 10 ) || ( Num >= PagTotal -1 ) ) BtnPaginacao.append('<li class="page-item '+( Num==PagAtual ? "active" : "")+'"> <a class="page-link '+( Num==PagAtual ? "" : "text-muted")+'" href="javascript:void(0);" '+( Num==PagAtual ? '' : 'onclick="fCarregarGrid(\''+urlPadrao+'\',\''+Num+'\');"' )+' title="Página '+Num+'" >'+Num+'</a></li>');
									}	
									if ( PagAtual < PagTotal                                                                                          ) BtnPaginacao.append('<li class="page-item"> <a class="page-link text-muted" href="javascript:void(0);" onclick="fCarregarGrid(\''+urlPadrao+'\',\''+(parseInt(PagAtual)+1)+'\');"  title="Próxima Página" aria-label="Next"> <span aria-hidden="true">&raquo;</span> <span class="sr-only">Next</span> </a> </li>');
								}

							}else{
								Conteudo = '<small style="font-size:14px;" class="font-italic text-muted">Nenhum Fato Relevante encontrado...</small><br/>';
								DivListaFatos.html(Conteudo);
							}

						} else{
							finalizarAnimacaoPesquisa();
							fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
							return;
						}
						
					},
					error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
						finalizarAnimacaoPesquisa();
						fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); // request.responseText //MSG_ALERTA_ERRO
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
		
    } catch (e) {
		finalizarAnimacaoPesquisa();
		  if ( e.description != undefined ){
			fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		  }
    }
}

function iniciarAnimacaoPesquisarFII() {
	$("#iRefreshFII").addClass("fa-spin");
	$("#btnFatoFIIPesquisar").addClass("disabled");
}

function finalizarAnimacaoPesquisaFII() {
	$("#iRefreshFII").removeClass("fa-spin");
	$("#btnFatoFIIPesquisar").removeClass("disabled");
}

async function fCarregarGridFundo( urlPadrao, iPagAtual ){
  try {   

		 promise = new Promise( (resolve, reject) => {

	  		fLimparAreaAlerta("AreaAlertaPrincFII");

			var DivListaFatosFII = $("#DivListaFatosFII");
			DivListaFatosFII.empty();
			
			var BtnPaginacaoFII = $("#BtnPaginacaoFII");
			BtnPaginacaoFII.empty();

			finalizarAnimacaoPesquisaFII();
			iniciarAnimacaoPesquisarFII();
	  
			var IdFundo = $("#txtFatoFundo").val();
			var DataIni   = '';
			var DataFim   = '';

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "fatos/gridFii",
				data: {
	                TipoInvest: 'FII', 
	                IdEmpresa : IdFundo, 
	                DataIni   : tirarFormacataoData(DataIni), 
					DataFim   : tirarFormacataoData(DataFim),
					PagAtual  : iPagAtual
	            },
				success: function(result) {
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
					var PagAtual  = parseInt( result.data.PagAtual ); 
					var PagTotal  = parseInt( result.data.PagTotal ); 

					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						finalizarAnimacaoPesquisaFII();
						CriarAlerta("AreaAlertaPrincFII", TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						finalizarAnimacaoPesquisaFII();
						CriarAlerta("AreaAlertaPrincFII", TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {

						finalizarAnimacaoPesquisaFII();
						var Conteudo = '';

						if ( lista && lista.length > 0 ){
							
							Conteudo += '<ul style="margin-right: 5px; ">';
							
							$.each(lista, function (index, value) {

								var FatoId        = value[0];
								var FatoFundo     = value[1];
								var FatoData      = colcarFormacataoDataHora(value[2])
								FatoData          = FatoData.substring(0,16);
								var FatoLink      = value[3];
								var FatoAssunto   = value[4];
								var FatoConteudo  = value[5];
								var FatoProtocolo = value[6];
								
								 Conteudo += '<li style="list-style-type:circle; margin-bottom: 5px;">';
								 Conteudo += '<a title="Clique aqui para ver o conteúdo oficial" style="font-size: 12px; "href="'+FatoLink+'" target="_blank" class="text-dark">';
								 Conteudo += '<span class="font-weight-bold">'+FatoData+'</span>';
								 Conteudo += ' - <span class="font-weight-normal">Protocolo: '+FatoProtocolo+'</span>';
								 Conteudo += ' - <span class="text-primary font-weight-bold">'+FatoFundo+'</span>';
								 Conteudo += ' - <span class="font-text-muted weight-normal">'+FatoAssunto+'</span>';
								 Conteudo += '</a>';
								 Conteudo += '</li>';

							});

							Conteudo += '</ul>';

							BtnPaginacaoFII.empty();
							DivListaFatosFII.html(Conteudo); 

							if ( PagTotal && PagTotal > 1 ){

								if ( PagAtual > 1 )                   
									BtnPaginacaoFII.append('<li class="page-item"> <a class="page-link text-muted" href="javascript:void(0);" onclick="fCarregarGridFundo(\''+urlPadrao+'\',\''+(parseInt(PagAtual)-1)+'\');" title="Página Anterior" aria-label="Anterior"> <span aria-hidden="true">&laquo;</span> <span class="sr-only">Previous</span> </a> </li>');
								
									for (Num = 1; Num <= PagTotal; Num++) {
									if ( Num == 9 && PagTotal > 10 )
										BtnPaginacaoFII.append('<li class="page-item disabled"> <a class="page-link text-muted disabled" href="javascript:void(0);"> ... </a></li>');
									if ( (Num <= 8) || ( Num == 9 && PagTotal <= 10 ) || ( Num == 10 && PagTotal <= 10 ) || ( Num >= PagTotal -1 ) )
										BtnPaginacaoFII.append('<li class="page-item '+( Num==PagAtual ? "active" : "")+'"> <a class="page-link '+( Num==PagAtual ? "" : "text-muted")+'" href="javascript:void(0);" '+( Num==PagAtual ? '' : 'onclick="fCarregarGridFundo(\''+urlPadrao+'\',\''+Num+'\');"' )+' title="Página '+Num+'" >'+Num+'</a></li>');
								}	

								if ( PagAtual < PagTotal )           
									BtnPaginacaoFII.append('<li class="page-item"><a class="page-link text-muted" href="javascript:void(0);" onclick="fCarregarGridFundo(\''+urlPadrao+'\',\''+(parseInt(PagAtual)+1)+'\');"  title="Próxima Página" aria-label="Next"> <span aria-hidden="true">&raquo;</span> <span class="sr-only">Next</span> </a> </li>');
							}

						}else{
							Conteudo = '<small style="font-size:14px;" class="font-italic text-muted">Nenhum Fato Relevante encontrado...</small><br/>';
							DivListaFatosFII.empty();
							DivListaFatosFII.html(Conteudo); 

						}


					} else{
						finalizarAnimacaoPesquisaFII();
						fCriarAlerta("AreaAlertaPrincFII", TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
					finalizarAnimacaoPesquisaFII();
					CriarAlerta("AreaAlertaPrincFII", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); // request.responseText //MSG_ALERTA_ERRO
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
		
    } catch (e) {
		finalizarAnimacaoPesquisaFII();
		if ( e.description != undefined ) CriarAlerta("AreaAlertaPrincFII", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

function iniciarAnimacaoPesquisarETF() {
	$("#iRefreshETF").addClass("fa-spin");
	$("#btnFatoETFPesquisar").addClass("disabled");
}

function finalizarAnimacaoPesquisaETF() {
	$("#iRefreshETF").removeClass("fa-spin");
	$("#btnFatoETFPesquisar").removeClass("disabled");
}

async function fCarregarGridIndice( urlPadrao, iPagAtual ){
  try {   

		 promise = new Promise( (resolve, reject) => {

				
		  		fLimparAreaAlerta("AreaAlertaPrincETF");

				var DivListaFatosETF = $("#DivListaFatosETF");
				DivListaFatosETF.empty();
				
				var BtnPaginacaoETF = $("#BtnPaginacaoETF");
				BtnPaginacaoETF.empty();

				finalizarAnimacaoPesquisaETF();
				iniciarAnimacaoPesquisarETF();
		  
				var IdIndice = $("#txtFatoIndice").val();
				var DataIni   = '';
				var DataFim   = '';
				
				$.ajax({
					cache   : "false",
					dataType: "json",
					async   : true,
					type    : "POST",
					url     : urlPadrao + "fatos/gridEtf",
					data: {
		                TipoInvest: 'ETF', 
		                IdEmpresa : IdIndice, 
		                DataIni   : tirarFormacataoData(DataIni), 
						DataFim   : tirarFormacataoData(DataFim),
						PagAtual  : iPagAtual
		            },
					success: function(result) {
						
						var resultado = result.data.Resultado; 
						var mensagem  = result.data.Mensagem; 
						var lista     = result.data.Lista;
						var PagAtual  = parseInt( result.data.PagAtual ); 
						var PagTotal  = parseInt( result.data.PagTotal ); 

						if (resultado == "NSESSAO") {
							$(location).attr('href', urlPadrao + '/login');
							return false;
						} else if (resultado == "NOK") {
							finalizarAnimacaoPesquisaETF();
							CriarAlerta("AreaAlertaPrincETF", TP_ALERTA_AVISO, mensagem); 
							return;
						} else if (resultado == "FALHA") {
							finalizarAnimacaoPesquisaETF();
							CriarAlerta("AreaAlertaPrincETF", TP_ALERTA_ERRO, mensagem); 
							return;
						}else if (resultado == "OK") {

							finalizarAnimacaoPesquisaETF();
							var Conteudo = '';

							if ( lista && lista.length > 0 ){
								
								Conteudo += '<ul style="margin-right: 5px; ">';
								
								$.each(lista, function (index, value) {

									var FatoId        = value[0];
									var FatoIndice    = value[1];
									var FatoData      = colcarFormacataoDataHora(value[2])
									FatoData          = FatoData.substring(0,16);
									var FatoLink      = value[3];
									var FatoAssunto   = value[4];
									var FatoConteudo  = value[5];
									var FatoProtocolo = value[6];
									
									 Conteudo += '<li style="list-style-type:circle; margin-bottom: 5px;">';
									 Conteudo += '<a title="Clique aqui para ver o conteúdo oficial" style="font-size: 12px; "href="'+FatoLink+'" target="_blank" class="text-dark">';
									 Conteudo += '<span class="font-weight-bold">'+FatoData+'</span>';
									 Conteudo += ' - <span class="font-weight-normal">Protocolo: '+FatoProtocolo+'</span>';
									 Conteudo += ' - <span class="text-primary font-weight-bold">'+FatoIndice+'</span>';
									 Conteudo += ' - <span class="font-text-muted weight-normal">'+FatoAssunto+'</span>';
									 Conteudo += '</a>';
									 Conteudo += '</li>';

								});

								Conteudo += '</ul>';

								BtnPaginacaoETF.empty();
								DivListaFatosETF.html(Conteudo); 

								if ( PagTotal && PagTotal > 1 ){

									if ( PagAtual > 1 )                   
										BtnPaginacaoETF.append('<li class="page-item"> <a class="page-link text-muted" href="javascript:void(0);" onclick="fCarregarGridIndice(\''+urlPadrao+'\',\''+(parseInt(PagAtual)-1)+'\');" title="Página Anterior" aria-label="Anterior"> <span aria-hidden="true">&laquo;</span> <span class="sr-only">Previous</span> </a> </li>');
									
										for (Num = 1; Num <= PagTotal; Num++) {
										if ( Num == 9 && PagTotal > 10 )
											BtnPaginacaoETF.append('<li class="page-item disabled"> <a class="page-link text-muted disabled" href="javascript:void(0);"> ... </a></li>');
										if ( (Num <= 8) || ( Num == 9 && PagTotal <= 10 ) || ( Num == 10 && PagTotal <= 10 ) || ( Num >= PagTotal -1 ) )
											BtnPaginacaoETF.append('<li class="page-item '+( Num==PagAtual ? "active" : "")+'"> <a class="page-link '+( Num==PagAtual ? "" : "text-muted")+'" href="javascript:void(0);" '+( Num==PagAtual ? '' : 'onclick="fCarregarGridIndice(\''+urlPadrao+'\',\''+Num+'\');"' )+' title="Página '+Num+'" >'+Num+'</a></li>');
									}	

									if ( PagAtual < PagTotal )           
										BtnPaginacaoETF.append('<li class="page-item"><a class="page-link text-muted" href="javascript:void(0);" onclick="fCarregarGridIndice(\''+urlPadrao+'\',\''+(parseInt(PagAtual)+1)+'\');"  title="Próxima Página" aria-label="Next"> <span aria-hidden="true">&raquo;</span> <span class="sr-only">Next</span> </a> </li>');
								}

							}else{
								Conteudo = '<small style="font-size:14px;" class="font-italic text-muted">Nenhum Fato Relevante encontrado...</small><br/>';
								DivListaFatosETF.empty();
								DivListaFatosETF.html(Conteudo); 

							}


						} else{
							finalizarAnimacaoPesquisaETF();
							fCriarAlerta("AreaAlertaPrincETF", TP_ALERTA_ERRO, mensagem); 
							return;
						}
						
					},
					error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
						finalizarAnimacaoPesquisaETF();
						CriarAlerta("AreaAlertaPrincETF", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); // request.responseText //MSG_ALERTA_ERRO
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
		
    } catch (e) {
		finalizarAnimacaoPesquisaETF();
		if ( e.description != undefined ) CriarAlerta("AreaAlertaPrincETF", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

function iniciarAnimacaoPesquisarBDR() {
	$("#iRefreshBDR").addClass("fa-spin");
	$("#btnFatoBDRPesquisar").addClass("disabled");
}

function finalizarAnimacaoPesquisaBDR() {
	$("#iRefreshBDR").removeClass("fa-spin");
	$("#btnFatoBDRPesquisar").removeClass("disabled");
}

async function fCarregarGridBdr( urlPadrao, iPagAtual ){
  try {

		 promise = new Promise( (resolve, reject) => {

		  		fLimparAreaAlerta("AreaAlertaPrincBDR");

				var DivListaFatosBDR = $("#DivListaFatosBDR");
				DivListaFatosBDR.empty();

				var BtnPaginacaoBDR = $("#BtnPaginacaoBDR");
				BtnPaginacaoBDR.empty();

				finalizarAnimacaoPesquisaBDR();
				iniciarAnimacaoPesquisarBDR();

				var IdBdr = $("#txtFatoBdr").val();
				var DataIni   = '';
				var DataFim   = '';

				$.ajax({
					cache   : "false",
					dataType: "json",
					async   : true,
					type    : "POST",
					url     : urlPadrao + "fatos/gridBdr",
					data: {
		                TipoInvest: 'BDR',
		                IdEmpresa : IdBdr,
		                DataIni   : tirarFormacataoData(DataIni),
						DataFim   : tirarFormacataoData(DataFim),
						PagAtual  : iPagAtual
		            },
					success: function(result) {

						var resultado = result.data.Resultado;
						var mensagem  = result.data.Mensagem;
						var lista     = result.data.Lista;
						var PagAtual  = parseInt( result.data.PagAtual );
						var PagTotal  = parseInt( result.data.PagTotal );

						if (resultado == "NSESSAO") {
							$(location).attr('href', urlPadrao + '/login');
							return false;
						} else if (resultado == "NOK") {
							finalizarAnimacaoPesquisaBDR();
							CriarAlerta("AreaAlertaPrincBDR", TP_ALERTA_AVISO, mensagem);
							return;
						} else if (resultado == "FALHA") {
							finalizarAnimacaoPesquisaBDR();
							CriarAlerta("AreaAlertaPrincBDR", TP_ALERTA_ERRO, mensagem);
							return;
						}else if (resultado == "OK") {

							finalizarAnimacaoPesquisaBDR();
							var Conteudo = '';

							if ( lista && lista.length > 0 ){

								Conteudo += '<ul style="margin-right: 5px; ">';

								$.each(lista, function (index, value) {

									var FatoId        = value[0];
									var FatoIndice    = value[1];
									var FatoData      = colcarFormacataoDataHora(value[2])
									FatoData          = FatoData.substring(0,16);
									var FatoLink      = value[3];
									var FatoAssunto   = value[4];
									var FatoConteudo  = value[5];
									var FatoProtocolo = value[6];

									 Conteudo += '<li style="list-style-type:circle; margin-bottom: 5px;">';
									 Conteudo += '<a title="Clique aqui para ver o conteúdo oficial" style="font-size: 12px; "href="'+FatoLink+'" target="_blank" class="text-dark">';
									 Conteudo += '<span class="font-weight-bold">'+FatoData+'</span>';
									 Conteudo += ' - <span class="font-weight-normal">Protocolo: '+FatoProtocolo+'</span>';
									 Conteudo += ' - <span class="text-primary font-weight-bold">'+FatoIndice+'</span>';
									 Conteudo += ' - <span class="font-text-muted weight-normal">'+FatoAssunto+'</span>';
									 Conteudo += '</a>';
									 Conteudo += '</li>';

								});

								Conteudo += '</ul>';

								BtnPaginacaoBDR.empty();
								DivListaFatosBDR.html(Conteudo);

								if ( PagTotal && PagTotal > 1 ){

									if ( PagAtual > 1 )
										BtnPaginacaoBDR.append('<li class="page-item"> <a class="page-link text-muted" href="javascript:void(0);" onclick="fCarregarGridBdr(\''+urlPadrao+'\',\''+(parseInt(PagAtual)-1)+'\');" title="Página Anterior" aria-label="Anterior"> <span aria-hidden="true">&laquo;</span> <span class="sr-only">Previous</span> </a> </li>');

										for (Num = 1; Num <= PagTotal; Num++) {
										if ( Num == 9 && PagTotal > 10 )
											BtnPaginacaoBDR.append('<li class="page-item disabled"> <a class="page-link text-muted disabled" href="javascript:void(0);"> ... </a></li>');
										if ( (Num <= 8) || ( Num == 9 && PagTotal <= 10 ) || ( Num == 10 && PagTotal <= 10 ) || ( Num >= PagTotal -1 ) )
											BtnPaginacaoBDR.append('<li class="page-item '+( Num==PagAtual ? "active" : "")+'"> <a class="page-link '+( Num==PagAtual ? "" : "text-muted")+'" href="javascript:void(0);" '+( Num==PagAtual ? '' : 'onclick="fCarregarGridBdr(\''+urlPadrao+'\',\''+Num+'\');"' )+' title="Página '+Num+'" >'+Num+'</a></li>');
									}

									if ( PagAtual < PagTotal )
										BtnPaginacaoBDR.append('<li class="page-item"><a class="page-link text-muted" href="javascript:void(0);" onclick="fCarregarGridBdr(\''+urlPadrao+'\',\''+(parseInt(PagAtual)+1)+'\');"  title="Próxima Página" aria-label="Next"> <span aria-hidden="true">&raquo;</span> <span class="sr-only">Next</span> </a> </li>');
								}

							}else{
								Conteudo = '<small style="font-size:14px;" class="font-italic text-muted">Nenhum Fato Relevante encontrado...</small><br/>';
								DivListaFatosBDR.empty();
								DivListaFatosBDR.html(Conteudo);

							}


						} else{
							finalizarAnimacaoPesquisaBDR();
							fCriarAlerta("AreaAlertaPrincBDR", TP_ALERTA_ERRO, mensagem);
							return;
						}

					},
					error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
						finalizarAnimacaoPesquisaBDR();
						CriarAlerta("AreaAlertaPrincBDR", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); // request.responseText //MSG_ALERTA_ERRO
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

    } catch (e) {
		finalizarAnimacaoPesquisaBDR();
		if ( e.description != undefined ) CriarAlerta("AreaAlertaPrincBDR", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}