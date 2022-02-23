
var ListaAno = [];

$(document).ready(function() {

     promise = new Promise( (resolve, reject) => {

		//$(this).attr("title", ":: TnB - Análise ::");
		$("#MnPrincAnalise").addClass("active open");
	
		ListaAno = [];
		
		fLimparAreaAlerta("AreaAlertaPrincAnaliseOper");
		fLimparAreaAlerta("AreaAlertaPrincAnaliseProv");
		fLimparAreaAlerta("AreaAlertaPrincAnaliseYiledCost");


        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
    })
    .then( txt => {
        //console.log('Sucesso: ' + txt);
    })
    .catch( txt => {
        //fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    });

});

async function fAbrirModalGerarPortfolio( urlPadrao ) {
    try {

        $("#PopModalGerarPortfolio").modal({backdrop: "static", keyboard: false});
        $("#iRefreshGerarPortfolio").addClass("fa-spin");

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "principal/gerarportifolio",
			success: function(result) {

				setTimeout(function(){
				    $("#iRefreshGerarPortfolio").removeClass("fa-spin");
				    $('#PopModalGerarPortfolio').modal('hide');
				}, 500);

			},
			error: function(data) {
				$("#iRefreshGerarPortfolio").removeClass("fa-spin");
				$('#PopModalGerarPortfolio').modal('hide');
				fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
				return;
			}
		});

    } catch (e) {
        $("#iRefreshGerarPortfolio").removeClass("fa-spin");
        $('#PopModalGerarPortfolio').modal('hide');
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fCarregarListaDeAnosProventosLocal( urlPadrao ){
	try {
		
		 promise = new Promise( (resolve, reject) => {

			ListaAno = [];

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "listas/lista_anos_user_provento",
				// data    : {  },
				success: function(result) {  
				
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista; 

					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						CriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return false;
					} else if (resultado == "OK") {					
						if ( lista.length > 0 ){

								ListaAno = lista;
								var ano  = '';
								$.each(lista, function (index, value) { 
									ano = value; 
								}); 

								var data     = new Date();
								var anoAtual = data.getFullYear();
								if ( ano == ''      ) ano = anoAtual;
								if ( ano > anoAtual ) ano = anoAtual;

								SetAnoAtual(urlPadrao, parseInt( ano ) );

							}
							return true;
					} else {
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return false;
					}
					
				},
				error: function(data) {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
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
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
		
	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

function GetAnoIncial(){
	if ( ListaAno.length >= 1 && ListaAno[0] !== '')   
		return parseInt( ListaAno[0] );
	return parseInt( $("#DivAno").text() );
} 

function GetAnoFinal(){
	if ( ListaAno.length > 1 )   
		return parseInt( ListaAno[ ListaAno.length - 1 ] )
	 return parseInt( $("#DivAno").text() );
}  

function GetAnoAtual(){
		return parseInt( $("#DivAno").text() );
}  

async function SetAnoAtual( urlPadrao, Ano ){
	
     promise = new Promise( (resolve, reject) => {

		$("#DivAno").text( Ano );

		var AnoIncial = GetAnoIncial();
		var AnoFinal  = GetAnoFinal();

		if ( Ano == AnoIncial && Ano == AnoFinal ){
			$("#DivVolarTudo").addClass("disabled"); 
			$("#DivVolarUm").addClass("disabled"); 
			$("#DivAvancarUm").addClass("disabled");
			$("#DivAvancarTudo").addClass("disabled");
		}else if ( Ano == AnoIncial ){
			$("#DivVolarTudo").addClass("disabled");
			$("#DivVolarUm").addClass("disabled"); 
			$("#DivAvancarUm").removeClass("disabled");
			$("#DivAvancarTudo").removeClass("disabled");
		}else if ( Ano == AnoFinal ){
			$("#DivVolarTudo").removeClass("disabled");
			$("#DivVolarUm").removeClass("disabled");
			$("#DivAvancarUm").addClass("disabled");
			$("#DivAvancarTudo").addClass("disabled");
		}else{
			$("#DivVolarTudo").removeClass("disabled");
			$("#DivVolarUm").removeClass("disabled");
			$("#DivAvancarUm").removeClass("disabled");
			$("#DivAvancarTudo").removeClass("disabled");
		}

		fCarregarGridAnaliseCalProv( urlPadrao );

		$( "#GridAnaliseCalProv" ).focus();

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
    })
    .then( txt => {
        //console.log('Sucesso: ' + txt);
    })
    .catch( txt => {
        //fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    });

  } 

  function fVolarTodosAnos( urlPadrao ){
		SetAnoAtual( urlPadrao, GetAnoIncial() );	
  }

  function fVolarUmAno( urlPadrao ){
		var AnoIncial = GetAnoIncial();
		var AnoAtual  = GetAnoAtual();
		if ( AnoAtual > AnoIncial )
			AnoAtual = AnoAtual - 1;
		SetAnoAtual( urlPadrao, AnoAtual );
  }

  function fAvancarUmAno( urlPadrao ){
		var AnoFinal = GetAnoFinal();
		var AnoAtual = GetAnoAtual();
		if ( AnoAtual < AnoFinal )
			AnoAtual = AnoAtual + 1;
		SetAnoAtual( urlPadrao, AnoAtual );
  }

  function fAvancarTodosAnos( urlPadrao ){
		SetAnoAtual( urlPadrao, GetAnoFinal() );
  }
