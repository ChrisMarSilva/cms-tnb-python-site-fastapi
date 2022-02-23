
async function fMontaGraficoProvAnualValor( urlPadrao, dataSet ){
	try { 

		 promise = new Promise( (resolve, reject) => {
	
			$("#DivGraficoAnaliseEvolucaoProventos").html("");
		
			var fLen = dataSet.length;
	
			if ( fLen <= 0 ){
				$("#DivGraficoAnaliseEvolucaoProventos").html("<br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/>");
				fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",  TP_ALERTA_AVISO, 'Sem registro.');
				return;
			}
				
			var arAnos     = []; 
			var arVlrProv  = [];	 
			var arPercProv = [];		
			var vlrProv    = 0.00; 
			var vlrProvDif = 0.00; 
			var vlrProvAnt = 0.00; 
	
			for (i = 0; i < fLen; i++) {
				arAnos[i]     = dataSet[i][0];
				vlrProv       = parseFloat(GetValorDecimal( dataSet[i][1] ));
				arVlrProv[i]  = vlrProv;
				arPercProv[i] = 0.00;
				if ( i > 0 ){
					vlrProvDif    = vlrProv - vlrProvAnt;
					arPercProv[i] = ( vlrProvDif / vlrProvAnt ) * 100;
				}
				vlrProvAnt = vlrProv;
			}
			
			Highcharts.chart('DivGraficoAnaliseEvolucaoProventos', {
				title: { text: null },
				chart: {zoomType: 'xy' },
				xAxis: { categories: arAnos, crosshair: true },
				yAxis: [
					{ title: { text: 'Total - R$',   style: { color: Highcharts.getOptions().colors[1] } }, labels: { format: 'R$ {value:.2f}', style: { color: Highcharts.getOptions().colors[1] } },                },// Primary yAxis
					{ title: { text: 'Percentual - %', style: { color: Highcharts.getOptions().colors[0] } }, labels: { format: '{value:.2f}%',   style: { color: Highcharts.getOptions().colors[0] } }, opposite: true } // Secondary yAxis
				],
				series: [
					{ 
							type: 'column', 
							name: 'Total Proventos', 
							yAxis: 1,
							data: arVlrProv,
							tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true }
					} , 
					{ 
							type: 'spline', 
							name: '% Evolução', 
							data: arPercProv, 
							marker: { lineWidth: 2, lineColor: Highcharts.getOptions().colors[3], fillColor: 'white' } ,
							//tooltip: { headerFormat: '<b>{point.x}</b><br/>', pointFormat: '{series.name}: {point.y:.2f}%' }
							tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>' + value + '%</b><br />'; }, shared: true }
						}
				]
		});
	
	
	
			// Highcharts.chart('DivGraficoAnaliseEvolucaoProventos', {
			// 		title: { text: null },
			// 		xAxis: { categories: arAnos },
			// 		series: [
			// 			{ 
			// 					type: 'column', 
			// 					name: 'Total Proventos', 
			// 					data: arVlrProv,
			// 					tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true }
			// 			} , 
			// 			{ 
			// 					type: 'spline', 
			// 					name: '% Evolução', 
			// 					data: arPercProv, 
			// 					marker: { lineWidth: 2, lineColor: Highcharts.getOptions().colors[3], fillColor: 'white' } ,
			// 					//tooltip: { headerFormat: '<b>{point.x}</b><br/>', pointFormat: '{series.name}: {point.y:.2f}%' }
			// 					tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>' + value + '%</b><br />'; }, shared: true }
			// 				}
			// 		]
			// });
	
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
		if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}  

function iniciarAnimacaoPesquisarAnaliseGrafProvAno() {	
	$("#iRefreshGrafProvAno").addClass("fa-spin");
	$("#btnAnaliseGrafProvAnoPesquisar").addClass("disabled");
}

function finalizarAnimacaoPesquisaAnaliseGrafProvAno() {
	$("#iRefreshGrafProvAno").removeClass("fa-spin");
	$("#btnAnaliseGrafProvAnoPesquisar").removeClass("disabled");
}

async function fCarregarGraficoProvAnual( urlPadrao ){
	try {   

		 promise = new Promise( (resolve, reject) => {
	
			fLimparAreaAlerta("AreaAlertaPrincAnaliseGrafAno");
		
			finalizarAnimacaoPesquisaAnaliseGrafProvAno();
			iniciarAnimacaoPesquisarAnaliseGrafProvAno();
	
			var CodAtivo = $("#txtFiltroAnaliseGrafProvAno").val().trim();	
	
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url: urlPadrao + "Analise/graficoProvAno",
				data: { CodAtivo: CodAtivo },
				success: function(result) {
					
					finalizarAnimacaoPesquisaAnaliseGrafProvAno();
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
	
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",  TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",  TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontaGraficoProvAnualValor( urlPadrao, lista );
					} else{
						fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",  TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					finalizarAnimacaoPesquisaAnaliseGrafProvAno();
					fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
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
		finalizarAnimacaoPesquisaAnaliseGrafProvAno();
	  if ( e.description != undefined ){
		fCriarAlerta("AreaAlertaPrincAnaliseGrafAno",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	  }
	}
}