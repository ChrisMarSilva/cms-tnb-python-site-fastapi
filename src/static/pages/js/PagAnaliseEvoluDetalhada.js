
async function fCarregarGridEvoluDetalhada( urlPadrao ){
	try { 
		
		 promise = new Promise( (resolve, reject) => {

			//$("#DivEvolucaoDetalhada").html("");

			$.ajax({
				cache   : "false",
				dataType: "html",
				async   : true,
				type    : "POST",
				url: urlPadrao + "Analise/EvolucaoDetalhada",
				//data: {  },
				success: function(result) {
					$("#DivEvolucaoDetalhada").html("");
					$("#DivEvolucaoDetalhada").html(result);
				},
				error: function(data) {
					$("#DivEvolucaoDetalhada").html(MSG_ALERTA_ERRO); //fCriarAlerta("AreaAlertaPrincAnaliseEvoluPratrim",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
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

	} catch (e) {
		if ( e.description != undefined )  $("#DivEvolucaoDetalhada").html(MSG_ALERTA_ERRO); //fCriarAlerta("AreaAlertaPrincAnaliseEvoluPratrim",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}  