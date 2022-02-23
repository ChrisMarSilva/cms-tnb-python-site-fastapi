

function fMostrarEsconderValores() {
	$(".DivTextValor").toggle();
	$(".DivIconeValor").toggle();
}

async function fLimparTotalizadores(urlPadrao) {
	try {

		 promise = new Promise((resolve, reject) => {

			$("#DivPrincPortTotInvest").html("R$ 0,00");
			$("#DivPrincPortTotAtual").html("R$ 0,00");
			$("#DivPrincPortTotValoriz").html("R$ 0,00 <small><em>( 0.00% )</em></small>");
			$("#DivPrincPortTotProv").html("R$ 0,00");
			$("#DivPrincPortTotValoriz").addClass("text-muted");
			$("#DivPrincPortTotValoriz").removeClass("text-success");
			$("#DivPrincPortTotValoriz").removeClass("text-danger");

			$("#DivPrincAcaoTotInvest").html("R$ 0,00");
			$("#DivPrincAcaoTotAtual").html("R$ 0,00");
			$("#DivPrincAcaoTotValoriz").html("R$ 0,00 <small><em>( 0.00% )</em></small>");
			$("#DivPrincAcaoTotProv").html("R$ 0,00");
			$("#DivPrincAcaoTotValoriz").addClass("text-muted");
			$("#DivPrincAcaoTotValoriz").removeClass("text-success");
			$("#DivPrincAcaoTotValoriz").removeClass("text-danger");

			$("#DivPrincFIITotInvest").html("R$ 0,00");
			$("#DivPrincFIITotAtual").html("R$ 0,00");
			$("#DivPrincFIITotValoriz").html("R$ 0,00 <small><em>( 0.00% )</em></small>");
			$("#DivPrincFIITotProv").html("R$ 0,00");
			$("#DivPrincFIITotValoriz").addClass("text-muted");
			$("#DivPrincFIITotValoriz").removeClass("text-success");
			$("#DivPrincFIITotValoriz").removeClass("text-danger");

			$("#DivPrincETFTotInvest").html("R$ 0,00");
			$("#DivPrincETFTotAtual").html("R$ 0,00");
			$("#DivPrincETFTotValoriz").html("R$ 0,00 <small><em>( 0.00% )</em></small>");
			$("#DivPrincETFTotProv").html("R$ 0,00");
			$("#DivPrincETFTotValoriz").addClass("text-muted");
			$("#DivPrincETFTotValoriz").removeClass("text-success");
			$("#DivPrincETFTotValoriz").removeClass("text-danger");

			$("#DivPrincBDRTotInvest").html("R$ 0,00");
			$("#DivPrincBDRTotAtual").html("R$ 0,00");
			$("#DivPrincBDRTotValoriz").html("R$ 0,00 <small><em>( 0.00% )</em></small>");
			$("#DivPrincBDRTotProv").html("R$ 0,00");
			$("#DivPrincBDRTotValoriz").addClass("text-muted");
			$("#DivPrincBDRTotValoriz").removeClass("text-success");
			$("#DivPrincBDRTotValoriz").removeClass("text-danger");

			$("#DivPrincCRIPTOTotInvest").html("R$ 0,00");
			$("#DivPrincCRIPTOTotAtual").html("R$ 0,00");
			$("#DivPrincCRIPTOTotValoriz").html("R$ 0,00 <small><em>( 0.00% )</em></small>");
			$("#DivPrincCRIPTOTotProv").html("R$ 0,00");
			$("#DivPrincCRIPTOTotValoriz").addClass("text-muted");
			$("#DivPrincCRIPTOTotValoriz").removeClass("text-success");
			$("#DivPrincCRIPTOTotValoriz").removeClass("text-danger");

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		if (e.description != undefined) fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosTotalizadores(urlPadrao) {
	try {

		 promise = new Promise((resolve, reject) => {

            let logNome = '@TamoNaBolsa - PagPrincipalTotalizadores'

            // console.log(logNome + ' - INI - ', moment().format())
            console.time(logNome + ' - TEMPO')

			DataSetPagina = {};

			$.ajax({
				cache: "false",
				dataType: "json",
				async: true,
				type: "POST",
				url: urlPadrao + "portfolio/DataSetPagina",
				// data    : { TipoInvest : 'ACAO'  },
				success: function (result) {

					var resultado = result.data.Resultado;
					var mensagem = result.data.Mensagem;
					var lista = result.data.Lista;

					DataSetPagina = result

					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
						return false;
					} else if (resultado == "FALHA") {
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return false;
					} else if (resultado == "OK") {

						fCarrgarDadosTotalizadoresPortfolio(urlPadrao);
						fCarrgarDadosGraficoPortfolio(urlPadrao);

						fCarrgarDadosTotalizadoresAcoes(urlPadrao);
						fCarrgarDadosGraficoAcoes(urlPadrao);

						fCarrgarDadosTotalizadoresFIIs(urlPadrao);
						fCarrgarDadosGraficoFIIs(urlPadrao);

						fCarrgarDadosTotalizadoresETFs(urlPadrao);
						fCarrgarDadosGraficoETFs(urlPadrao);

						fCarrgarDadosTotalizadoresBDRs(urlPadrao);
						fCarrgarDadosGraficoBDRs(urlPadrao);

						fCarrgarDadosTotalizadoresCRIPTOs(urlPadrao);
						fCarrgarDadosGraficoCRIPTOs(urlPadrao);

                        console.timeEnd(logNome + ' - TEMPO')

					} else {
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return false;
					}

				},
				error: function (data) {
                    console.error(logNome + ' - ERRO: ', error)
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
					return;
				}
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
        .then(txt => {
            //console.log('Sucesso: ' + txt);
        })
        .catch(txt => {
            console.error(logNome + ' - ERRO: ', error)
            fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
        });

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosTotalizadoresPortfolio(urlPadrao) {
	try {

		 promise = new Promise((resolve, reject) => {

			var TotInvest = 0.00;
			var TotAtual = 0.00;
			var TotValoriz = 0.00;
			var PercValoriz = 0.00;
			var TotProv = 0.00;

			if ((DataSetPagina) && (DataSetPagina.data) && (DataSetPagina.data.Lista)) {
				var lista = DataSetPagina.data.Lista;
				if (lista.length > 0) {
					$.each(lista, function (index, value) {
						TotInvest += parseFloat(GetValorDecimal(value.AtvTotInvest));
						TotAtual += parseFloat(GetValorDecimal(value.AtvTotAtual));
						TotValoriz += parseFloat(GetValorDecimal(value.AtvTotValoriz));
						TotProv += parseFloat(GetValorDecimal(value.AtvTotProv));
					}); // $.each(lista, function (index, value) {
				} // if ( lista.length > 0 ){
			} //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){

			if (TotValoriz != 0 && TotInvest > 0)
				PercValoriz = (TotValoriz / TotInvest) * 100;

			$("#DivPrincPortTotInvest").html("R$ " + fMascaraValor(TotInvest));
			$("#DivPrincPortTotAtual").html("R$ " + fMascaraValor(TotAtual));
			$("#DivPrincPortTotValoriz").html("R$ " + fMascaraValor(TotValoriz) + " <small><em>( " + fMascaraValor(PercValoriz) + "% )</em></small>");
			$("#DivPrincPortTotProv").html("R$ " + fMascaraValor(TotProv));

			if (TotValoriz > 0.00) {
				$("#DivPrincPortTotValoriz").removeClass("text-muted");
				$("#DivPrincPortTotValoriz").addClass("text-success");
			}

			if (TotValoriz < 0.00) {
				$("#DivPrincPortTotValoriz").removeClass("text-muted");
				$("#DivPrincPortTotValoriz").addClass("text-danger");
			}

			Highcharts.setOptions({ global: { useUTC: false }, lang: { decimalPoint: ',', thousandsSep: '.' } });

			Highcharts.chart('DivChartPrincPort', {
				lang: {
					months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
					shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
					weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
					loading: ['Atualizando o gráfico...aguarde'],
					contextButtonTitle: 'Exportar gráfico',
					decimalPoint: ',',
					thousandsSep: '.',
					viewFullscreen: 'Exibir em tela cheia',
					openInCloud: 'Abri em Highcharts Cloud',
					downloadJPEG: 'Baixar imagem JPEG',
					downloadPDF: 'Baixar arquivo PDF',
					downloadPNG: 'Baixar imagem PNG',
					downloadSVG: 'Baixar vetor SVG',
					printChart: 'Imprimir gráfico',
					rangeSelectorFrom: 'De',
					rangeSelectorTo: 'Para',
					rangeSelectorZoom: 'Zoom',
					resetZoom: 'Limpar Zoom',
					resetZoomTitle: 'Voltar Zoom para nível 1:1',
				},
				exporting: { enabled: false },
				data: { table: 'datatable' },
				chart: { type: 'column' },
				title: { text: null },
				legend: { enabled: true },
				//xAxis: { categories: ['Carteira'], labels: { style: { fontSize: '8.5px' } } },
				xAxis: { categories: [''], title: { text: null }, labels: { enabled: true, y: 20, rotation: -45, align: 'right' } },
				yAxis: { allowDecimals: false, title: { text: null }, labels: { style: { fontSize: '8.5px' } } },
				colors: ['#2f7ed8', '#8bbc21', '#492970', '#f28f43'],
				credits: { enabled: false },
				tooltip: { pointFormatter: function () { var value = Number(this.y).toFixed(2).replace(/./g, function (c, i, a) { return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.', ',').replace(/X/g, '.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true },
				series: [{ name: 'Tot. Investido', data: [TotInvest] }, { name: 'Tot. Atual', data: [TotAtual] }, { name: 'Total Valorização', data: [TotAtual - TotInvest] }, { name: 'Tot. Proventos', data: [TotProv] }]
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosTotalizadoresAcoes(urlPadrao) {
	try {

		 promise = new Promise((resolve, reject) => {

			// var start = new Date().getTime();
			// console.log('fCarrgarDadosTotalizadoresAcoes - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );

			var TotInvest = 0.00;
			var TotAtual = 0.00;
			var TotValoriz = 0.00;
			var PercValoriz = 0.00;
			var TotProv = 0.00;

			var IdPortfolio = '';
			var TipoInvest = "ACAO";
			if ((DataSetPagina) && (DataSetPagina.data) && (DataSetPagina.data.Lista)) {
				var lista = DataSetPagina.data.Lista;
				if (lista.length > 0) {
					$.each(lista, function (index, value) {
						var CartId = value.CartId;
						var AtvTipoInvest = value.AtvTipoInvest;
						if ((IdPortfolio == "") || (IdPortfolio == CartId)) {
							if ((TipoInvest == "") || (TipoInvest == AtvTipoInvest)) {
								TotInvest += parseFloat(GetValorDecimal(value.AtvTotInvest));
								TotAtual += parseFloat(GetValorDecimal(value.AtvTotAtual));
								TotValoriz += parseFloat(GetValorDecimal(value.AtvTotValoriz));
								// PercValoriz += parseFloat(GetValorDecimal(value.AtvPercValoriz));
								TotProv += parseFloat(GetValorDecimal(value.AtvTotProv)); //AtvTotAlug
							} // if ( (TipoInvest == "") || (TipoInvest == value.AtvTipoInvest) ){
						} // if ( (IdPortfolio == "") || (IdPortfolio == value.CartId) ){
					}); // $.each(lista, function (index, value) {
				} // if ( lista.length > 0 ){
			} //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){	

			if (TotValoriz != 0 && TotInvest > 0)
				PercValoriz = (TotValoriz / TotInvest) * 100;

			if (TotAtual == 0.0) {
				$('#DivPrincAcao').hide();
			}

			if (TotAtual > 0.0) {

				$('#DivPrincAcao').show();

				$("#DivPrincAcaoTotInvest").html("R$ " + fMascaraValor(TotInvest));
				$("#DivPrincAcaoTotAtual").html("R$ " + fMascaraValor(TotAtual));
				$("#DivPrincAcaoTotValoriz").html("R$ " + fMascaraValor(TotValoriz) + " <small><em>( " + fMascaraValor(PercValoriz) + "% )</em></small>");
				$("#DivPrincAcaoTotProv").html("R$ " + fMascaraValor(TotProv));

				if (TotValoriz > 0.00) {
					$("#DivPrincAcaoTotValoriz").removeClass("text-muted");
					$("#DivPrincAcaoTotValoriz").addClass("text-success");
				}
				if (TotValoriz < 0.00) {
					$("#DivPrincAcaoTotValoriz").removeClass("text-muted");
					$("#DivPrincAcaoTotValoriz").addClass("text-danger");
				}

				Highcharts.setOptions({ global: { useUTC: false }, lang: { decimalPoint: ',', thousandsSep: '.' } });

				Highcharts.chart('DivChartPrincAcao', {
					lang: {
						months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
						shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
						weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
						loading: ['Atualizando o gráfico...aguarde'],
						contextButtonTitle: 'Exportar gráfico',
						decimalPoint: ',',
						thousandsSep: '.',
						viewFullscreen: 'Exibir em tela cheia',
						openInCloud: 'Abri em Highcharts Cloud',
						downloadJPEG: 'Baixar imagem JPEG',
						downloadPDF: 'Baixar arquivo PDF',
						downloadPNG: 'Baixar imagem PNG',
						downloadSVG: 'Baixar vetor SVG',
						printChart: 'Imprimir gráfico',
						rangeSelectorFrom: 'De',
						rangeSelectorTo: 'Para',
						rangeSelectorZoom: 'Zoom',
						resetZoom: 'Limpar Zoom',
						resetZoomTitle: 'Voltar Zoom para nível 1:1',
					},
					exporting: { enabled: false },
					data: { table: 'datatable' },
					chart: { type: 'column' },
					title: { text: null },
					legend: { enabled: true },
					//xAxis: { categories: ['Carteira'], labels: { style: { fontSize: '8.5px' } } },
					xAxis: { categories: [''], title: { text: null }, labels: { enabled: true, y: 20, rotation: -45, align: 'right' } },
					yAxis: { allowDecimals: false, title: { text: null }, labels: { style: { fontSize: '8.5px' } } },
					colors: ['#2f7ed8', '#8bbc21', '#492970', '#f28f43'],
					credits: { enabled: false },
					tooltip: { pointFormatter: function () { var value = Number(this.y).toFixed(2).replace(/./g, function (c, i, a) { return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.', ',').replace(/X/g, '.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true },
					series: [{ name: 'Tot. Investido', data: [TotInvest] }, { name: 'Tot. Atual', data: [TotAtual] }, { name: 'Total Valorização', data: [TotAtual - TotInvest] }, { name: 'Tot. Proventos', data: [TotProv] }]
				});

			} //if ( TotAtual > 0.0 ){

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosTotalizadoresFIIs(urlPadrao) {
	try {
		
		 promise = new Promise((resolve, reject) => {

			var TotInvest = 0.00;
			var TotAtual = 0.00;
			var TotValoriz = 0.00;
			var PercValoriz = 0.00;
			var TotProv = 0.00;

			var IdPortfolio = '';
			var TipoInvest = "FII";
			if ((DataSetPagina) && (DataSetPagina.data) && (DataSetPagina.data.Lista)) {
				var lista = DataSetPagina.data.Lista;
				if (lista.length > 0) {
					$.each(lista, function (index, value) {
						var CartId = value.CartId;
						var AtvTipoInvest = value.AtvTipoInvest;
						if ((IdPortfolio == "") || (IdPortfolio == CartId)) {
							if ((TipoInvest == "") || (TipoInvest == AtvTipoInvest)) {
								TotInvest += parseFloat(GetValorDecimal(value.AtvTotInvest));
								TotAtual += parseFloat(GetValorDecimal(value.AtvTotAtual));
								TotValoriz += parseFloat(GetValorDecimal(value.AtvTotValoriz));
								// PercValoriz += parseFloat(GetValorDecimal(value.AtvPercValoriz));
								TotProv += parseFloat(GetValorDecimal(value.AtvTotProv)); //AtvTotAlug
							} // if ( (TipoInvest == "") || (TipoInvest == value.AtvTipoInvest) ){
						} // if ( (IdPortfolio == "") || (IdPortfolio == value.CartId) ){
					}); // $.each(lista, function (index, value) {
				} // if ( lista.length > 0 ){
			} //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){	

			if (TotValoriz != 0 && TotInvest > 0)
				PercValoriz = (TotValoriz / TotInvest) * 100;

			if (TotAtual == 0.0) {
				$('#DivPrincFII').hide();
			}

			if (TotAtual > 0.0) {

				$('#DivPrincFII').show();

				$("#DivPrincFIITotInvest").html("R$ " + fMascaraValor(TotInvest));
				$("#DivPrincFIITotAtual").html("R$ " + fMascaraValor(TotAtual));
				$("#DivPrincFIITotValoriz").html("R$ " + fMascaraValor(TotValoriz) + " <small><em>( " + fMascaraValor(PercValoriz) + "% )</em></small>");
				$("#DivPrincFIITotProv").html("R$ " + fMascaraValor(TotProv));

				if (TotValoriz > 0.00) {
					$("#DivPrincFIITotValoriz").removeClass("text-muted");
					$("#DivPrincFIITotValoriz").addClass("text-success");
				}
				if (TotValoriz < 0.00) {
					$("#DivPrincFIITotValoriz").removeClass("text-muted");
					$("#DivPrincFIITotValoriz").addClass("text-danger");
				}

				Highcharts.setOptions({ global: { useUTC: false }, lang: { decimalPoint: ',', thousandsSep: '.' } });

				Highcharts.chart('DivChartPrincFII', {
					lang: {
						months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
						shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
						weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
						loading: ['Atualizando o gráfico...aguarde'],
						contextButtonTitle: 'Exportar gráfico',
						decimalPoint: ',',
						thousandsSep: '.',
						viewFullscreen: 'Exibir em tela cheia',
						openInCloud: 'Abri em Highcharts Cloud',
						downloadJPEG: 'Baixar imagem JPEG',
						downloadPDF: 'Baixar arquivo PDF',
						downloadPNG: 'Baixar imagem PNG',
						downloadSVG: 'Baixar vetor SVG',
						printChart: 'Imprimir gráfico',
						rangeSelectorFrom: 'De',
						rangeSelectorTo: 'Para',
						rangeSelectorZoom: 'Zoom',
						resetZoom: 'Limpar Zoom',
						resetZoomTitle: 'Voltar Zoom para nível 1:1',
					},
					exporting: { enabled: false },
					data: { table: 'datatable' },
					chart: { type: 'column' },
					title: { text: null },
					legend: { enabled: true },
					//xAxis: { categories: ['Carteira'], labels: { style: { fontSize: '8.5px' } } },
					xAxis: { categories: [''], title: { text: null }, labels: { enabled: true, y: 20, rotation: -45, align: 'right' } },
					yAxis: { allowDecimals: false, title: { text: null }, labels: { style: { fontSize: '8.5px' } } },
					colors: ['#2f7ed8', '#8bbc21', '#492970', '#f28f43'],
					credits: { enabled: false },
					tooltip: { pointFormatter: function () { var value = Number(this.y).toFixed(2).replace(/./g, function (c, i, a) { return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.', ',').replace(/X/g, '.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true },
					series: [{ name: 'Tot. Investido', data: [TotInvest] }, { name: 'Tot. Atual', data: [TotAtual] }, { name: 'Total Valorização', data: [TotAtual - TotInvest] }, { name: 'Tot. Proventos', data: [TotProv] }]
				});

			} //if ( TotAtual > 0.0 ){

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosTotalizadoresETFs(urlPadrao) {
	try {

		 promise = new Promise((resolve, reject) => {

			// var start = new Date().getTime();
			// console.log('fCarrgarDadosTotalizadoresETFs - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );

			var TotInvest = 0.00;
			var TotAtual = 0.00;
			var TotValoriz = 0.00;
			var PercValoriz = 0.00;
			var TotProv = 0.00;

			var IdPortfolio = '';
			var TipoInvest = "ETF";
			if ((DataSetPagina) && (DataSetPagina.data) && (DataSetPagina.data.Lista)) {
				var lista = DataSetPagina.data.Lista;
				if (lista.length > 0) {
					$.each(lista, function (index, value) {
						var CartId = value.CartId;
						var AtvTipoInvest = value.AtvTipoInvest;
						if ((IdPortfolio == "") || (IdPortfolio == CartId)) {
							if ((TipoInvest == "") || (TipoInvest == AtvTipoInvest)) {
								TotInvest += parseFloat(GetValorDecimal(value.AtvTotInvest));
								TotAtual += parseFloat(GetValorDecimal(value.AtvTotAtual));
								TotValoriz += parseFloat(GetValorDecimal(value.AtvTotValoriz));
								// PercValoriz += parseFloat(GetValorDecimal(value.AtvPercValoriz));
								TotProv += parseFloat(GetValorDecimal(value.AtvTotProv)); //AtvTotAlug
							} // if ( (TipoInvest == "") || (TipoInvest == value.AtvTipoInvest) ){
						} // if ( (IdPortfolio == "") || (IdPortfolio == value.CartId) ){
					}); // $.each(lista, function (index, value) {
				} // if ( lista.length > 0 ){
			} //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){	

			if (TotValoriz != 0 && TotInvest > 0)
				PercValoriz = (TotValoriz / TotInvest) * 100;

			if (TotAtual == 0.0) {
				$('#DivPrincETF').hide();
			}

			if (TotAtual > 0.0) {

				$('#DivPrincETF').show();

				$("#DivPrincETFTotInvest").html("R$ " + fMascaraValor(TotInvest));
				$("#DivPrincETFTotAtual").html("R$ " + fMascaraValor(TotAtual));
				$("#DivPrincETFTotValoriz").html("R$ " + fMascaraValor(TotValoriz) + " <small><em>( " + fMascaraValor(PercValoriz) + "% )</em></small>");
				$("#DivPrincETFTotProv").html("R$ " + fMascaraValor(TotProv));

				if (TotValoriz > 0.00) {
					$("#DivPrincETFTotValoriz").removeClass("text-muted");
					$("#DivPrincETFTotValoriz").addClass("text-success");
				}
				if (TotValoriz < 0.00) {
					$("#DivPrincETFTotValoriz").removeClass("text-muted");
					$("#DivPrincETFTotValoriz").addClass("text-danger");
				}

				if ($("#DivChartPrincETF").length) {

					Highcharts.setOptions({ global: { useUTC: false }, lang: { decimalPoint: ',', thousandsSep: '.' } });

					Highcharts.chart('DivChartPrincETF', {
						lang: {
							months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
							shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
							weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
							loading: ['Atualizando o gráfico...aguarde'],
							contextButtonTitle: 'Exportar gráfico',
							decimalPoint: ',',
							thousandsSep: '.',
							viewFullscreen: 'Exibir em tela cheia',
							openInCloud: 'Abri em Highcharts Cloud',
							downloadJPEG: 'Baixar imagem JPEG',
							downloadPDF: 'Baixar arquivo PDF',
							downloadPNG: 'Baixar imagem PNG',
							downloadSVG: 'Baixar vetor SVG',
							printChart: 'Imprimir gráfico',
							rangeSelectorFrom: 'De',
							rangeSelectorTo: 'Para',
							rangeSelectorZoom: 'Zoom',
							resetZoom: 'Limpar Zoom',
							resetZoomTitle: 'Voltar Zoom para nível 1:1',
						},
						exporting: { enabled: false },
						data: { table: 'datatable' },
						chart: { type: 'column' },
						title: { text: null },
						legend: { enabled: true },
						//xAxis: { categories: ['Carteira'], labels: { style: { fontSize: '8.5px' } } },
						xAxis: { categories: [''], title: { text: null }, labels: { enabled: true, y: 20, rotation: -45, align: 'right' } },
						yAxis: { allowDecimals: false, title: { text: null }, labels: { style: { fontSize: '8.5px' } } },
						colors: ['#2f7ed8', '#8bbc21', '#492970', '#f28f43'],
						credits: { enabled: false },
						tooltip: { pointFormatter: function () { var value = Number(this.y).toFixed(2).replace(/./g, function (c, i, a) { return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.', ',').replace(/X/g, '.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true },
						series: [{ name: 'Tot. Investido', data: [TotInvest] }, { name: 'Tot. Atual', data: [TotAtual] }, { name: 'Total Valorização', data: [TotAtual - TotInvest] }, { name: 'Tot. Proventos', data: [TotProv] }]
					});

				} // if ( $( "#DivChartPrincETF" ).length ) {

			} //if ( TotAtual > 0.0 ){

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosTotalizadoresBDRs(urlPadrao) {
	try {

		 promise = new Promise((resolve, reject) => {

			var TotInvest = 0.00;
			var TotAtual = 0.00;
			var TotValoriz = 0.00;
			var PercValoriz = 0.00;
			var TotProv = 0.00;

			var IdPortfolio = '';
			var TipoInvest = "BDR";
			if ((DataSetPagina) && (DataSetPagina.data) && (DataSetPagina.data.Lista)) {
				var lista = DataSetPagina.data.Lista;
				if (lista.length > 0) {
					$.each(lista, function (index, value) {
						var CartId = value.CartId;
						var AtvTipoInvest = value.AtvTipoInvest;
						if ((IdPortfolio == "") || (IdPortfolio == CartId)) {
							if ((TipoInvest == "") || (TipoInvest == AtvTipoInvest)) {
								TotInvest += parseFloat(GetValorDecimal(value.AtvTotInvest));
								TotAtual += parseFloat(GetValorDecimal(value.AtvTotAtual));
								TotValoriz += parseFloat(GetValorDecimal(value.AtvTotValoriz));
								// PercValoriz += parseFloat(GetValorDecimal(value.AtvPercValoriz));
								TotProv += parseFloat(GetValorDecimal(value.AtvTotProv)); //AtvTotAlug
							} // if ( (TipoInvest == "") || (TipoInvest == value.AtvTipoInvest) ){
						} // if ( (IdPortfolio == "") || (IdPortfolio == value.CartId) ){
					}); // $.each(lista, function (index, value) {
				} // if ( lista.length > 0 ){
			} //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){

			if (TotValoriz != 0 && TotInvest > 0)
				PercValoriz = (TotValoriz / TotInvest) * 100;

			if (TotAtual == 0.0) {
				$('#DivPrincBDR').hide();
			}

			if (TotAtual > 0.0) {

				$('#DivPrincBDR').show();

				$("#DivPrincBDRTotInvest").html("R$ " + fMascaraValor(TotInvest));
				$("#DivPrincBDRTotAtual").html("R$ " + fMascaraValor(TotAtual));
				$("#DivPrincBDRTotValoriz").html("R$ " + fMascaraValor(TotValoriz) + " <small><em>( " + fMascaraValor(PercValoriz) + "% )</em></small>");
				$("#DivPrincBDRTotProv").html("R$ " + fMascaraValor(TotProv));

				if (TotValoriz > 0.00) {
					$("#DivPrincBDRTotValoriz").removeClass("text-muted");
					$("#DivPrincBDRTotValoriz").addClass("text-success");
				}
				if (TotValoriz < 0.00) {
					$("#DivPrincBDRTotValoriz").removeClass("text-muted");
					$("#DivPrincBDRTotValoriz").addClass("text-danger");
				}

				if ($("#DivChartPrincBDR").length) {

					Highcharts.setOptions({ global: { useUTC: false }, lang: { decimalPoint: ',', thousandsSep: '.' } });

					Highcharts.chart('DivChartPrincBDR', {
						lang: {
							months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
							shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
							weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
							loading: ['Atualizando o gráfico...aguarde'],
							contextButtonTitle: 'Exportar gráfico',
							decimalPoint: ',',
							thousandsSep: '.',
							viewFullscreen: 'Exibir em tela cheia',
							openInCloud: 'Abri em Highcharts Cloud',
							downloadJPEG: 'Baixar imagem JPEG',
							downloadPDF: 'Baixar arquivo PDF',
							downloadPNG: 'Baixar imagem PNG',
							downloadSVG: 'Baixar vetor SVG',
							printChart: 'Imprimir gráfico',
							rangeSelectorFrom: 'De',
							rangeSelectorTo: 'Para',
							rangeSelectorZoom: 'Zoom',
							resetZoom: 'Limpar Zoom',
							resetZoomTitle: 'Voltar Zoom para nível 1:1',
						},
						exporting: { enabled: false },
						data: { table: 'datatable' },
						chart: { type: 'column' },
						title: { text: null },
						legend: { enabled: true },
						//xAxis: { categories: ['Carteira'], labels: { style: { fontSize: '8.5px' } } },
						xAxis: { categories: [''], title: { text: null }, labels: { enabled: true, y: 20, rotation: -45, align: 'right' } },
						yAxis: { allowDecimals: false, title: { text: null }, labels: { style: { fontSize: '8.5px' } } },
						colors: ['#2f7ed8', '#8bbc21', '#492970', '#f28f43'],
						credits: { enabled: false },
						tooltip: { pointFormatter: function () { var value = Number(this.y).toFixed(2).replace(/./g, function (c, i, a) { return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.', ',').replace(/X/g, '.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true },
						series: [{ name: 'Tot. Investido', data: [TotInvest] }, { name: 'Tot. Atual', data: [TotAtual] }, { name: 'Total Valorização', data: [TotAtual - TotInvest] }, { name: 'Tot. Proventos', data: [TotProv] }]
					});

				} // if ( $( "#DivChartPrincBDR" ).length ) {

			} //if ( TotAtual > 0.0 ){

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosTotalizadoresCRIPTOs(urlPadrao) {
	try {

		 promise = new Promise((resolve, reject) => {

			var TotInvest = 0.00;
			var TotAtual = 0.00;
			var TotValoriz = 0.00;
			var PercValoriz = 0.00;
			var TotProv = 0.00;

			var IdPortfolio = '';
			var TipoInvest = "CRIPTO";
			if ((DataSetPagina) && (DataSetPagina.data) && (DataSetPagina.data.Lista)) {
				var lista = DataSetPagina.data.Lista;
				if (lista.length > 0) {
					$.each(lista, function (index, value) {
						var CartId = value.CartId;
						var AtvTipoInvest = value.AtvTipoInvest;
						if ((IdPortfolio == "") || (IdPortfolio == CartId)) {
							if ((TipoInvest == "") || (TipoInvest == AtvTipoInvest)) {
								TotInvest += parseFloat(GetValorDecimal(value.AtvTotInvest));
								TotAtual += parseFloat(GetValorDecimal(value.AtvTotAtual));
								TotValoriz += parseFloat(GetValorDecimal(value.AtvTotValoriz));
								// PercValoriz += parseFloat(GetValorDecimal(value.AtvPercValoriz));
								TotProv += parseFloat(GetValorDecimal(value.AtvTotProv)); //AtvTotAlug
							} // if ( (TipoInvest == "") || (TipoInvest == value.AtvTipoInvest) ){
						} // if ( (IdPortfolio == "") || (IdPortfolio == value.CartId) ){
					}); // $.each(lista, function (index, value) {
				} // if ( lista.length > 0 ){
			} //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){

			if (TotValoriz != 0 && TotInvest > 0)
				PercValoriz = (TotValoriz / TotInvest) * 100;

			if (TotAtual == 0.0) {
				$('#DivPrincCRIPTO').hide();
			}

			if (TotAtual > 0.0) {

				$('#DivPrincCRIPTO').show();

				$("#DivPrincCRIPTOTotInvest").html("R$ " + fMascaraValor(TotInvest));
				$("#DivPrincCRIPTOTotAtual").html("R$ " + fMascaraValor(TotAtual));
				$("#DivPrincCRIPTOTotValoriz").html("R$ " + fMascaraValor(TotValoriz) + " <small><em>( " + fMascaraValor(PercValoriz) + "% )</em></small>");
				$("#DivPrincCRIPTOTotProv").html("R$ " + fMascaraValor(TotProv));

				if (TotValoriz > 0.00) {
					$("#DivPrincCRIPTOTotValoriz").removeClass("text-muted");
					$("#DivPrincCRIPTOTotValoriz").addClass("text-success");
				}
				if (TotValoriz < 0.00) {
					$("#DivPrincCRIPTOTotValoriz").removeClass("text-muted");
					$("#DivPrincCRIPTOTotValoriz").addClass("text-danger");
				}

				Highcharts.setOptions({ global: { useUTC: false }, lang: { decimalPoint: ',', thousandsSep: '.' } });

				Highcharts.chart('DivChartPrincCRIPTO', {
					lang: {
						months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
						shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
						weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
						loading: ['Atualizando o gráfico...aguarde'],
						contextButtonTitle: 'Exportar gráfico',
						decimalPoint: ',',
						thousandsSep: '.',
						viewFullscreen: 'Exibir em tela cheia',
						openInCloud: 'Abri em Highcharts Cloud',
						downloadJPEG: 'Baixar imagem JPEG',
						downloadPDF: 'Baixar arquivo PDF',
						downloadPNG: 'Baixar imagem PNG',
						downloadSVG: 'Baixar vetor SVG',
						printChart: 'Imprimir gráfico',
						rangeSelectorFrom: 'De',
						rangeSelectorTo: 'Para',
						rangeSelectorZoom: 'Zoom',
						resetZoom: 'Limpar Zoom',
						resetZoomTitle: 'Voltar Zoom para nível 1:1',
					},
					exporting: { enabled: false },
					data: { table: 'datatable' },
					chart: { type: 'column' },
					title: { text: null },
					legend: { enabled: true },
					//xAxis: { categories: ['Carteira'], labels: { style: { fontSize: '8.5px' } } },
					xAxis: { categories: [''], title: { text: null }, labels: { enabled: true, y: 20, rotation: -45, align: 'right' } },
					yAxis: { allowDecimals: false, title: { text: null }, labels: { style: { fontSize: '8.5px' } } },
					colors: ['#2f7ed8', '#8bbc21', '#492970', '#f28f43'],
					credits: { enabled: false },
					tooltip: { pointFormatter: function () { var value = Number(this.y).toFixed(2).replace(/./g, function (c, i, a) { return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.', ',').replace(/X/g, '.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true },
					series: [{ name: 'Tot. Investido', data: [TotInvest] }, { name: 'Tot. Atual', data: [TotAtual] }, { name: 'Total Valorização', data: [TotAtual - TotInvest] }, { name: 'Tot. Proventos', data: [TotProv] }]
				});

			} //if ( TotAtual > 0.0 ){

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosGraficoPortfolio(urlPadrao) {
	try {

		 promise = new Promise((resolve, reject) => {

			var TotACAO = 0.00;
			var TotFII = 0.00;
			var TotETF = 0.00;
			var TotBDR = 0.00;
			var TotCRIPTO = 0.00;

			if ((DataSetPagina) && (DataSetPagina.data) && (DataSetPagina.data.Lista)) {
				var lista = DataSetPagina.data.Lista;
				if (lista.length > 0) {
					$.each(lista, function (index, value) {
						if (value.AtvTipoInvest == 'ACAO') TotACAO += parseFloat(GetValorDecimal(value.AtvTotAtual));
						if (value.AtvTipoInvest == 'FII') TotFII += parseFloat(GetValorDecimal(value.AtvTotAtual));
						if (value.AtvTipoInvest == 'ETF') TotETF += parseFloat(GetValorDecimal(value.AtvTotAtual));
						if (value.AtvTipoInvest == 'BDR') TotBDR += parseFloat(GetValorDecimal(value.AtvTotAtual));
						if (value.AtvTipoInvest == 'CRIPTO') TotCRIPTO += parseFloat(GetValorDecimal(value.AtvTotAtual));
					}); // $.each(lista, function (index, value) {
				} // if ( lista.length > 0 ){
			} //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){	

			if (TotACAO > 0.00 || TotFII > 0.00 || TotETF > 0.00 || TotBDR > 0.00 || TotCRIPTO > 0.00) {


                var dataSetGrafico = []
                if (TotACAO > 0.00) dataSetGrafico.push({ name: 'AÇÕES', y: parseFloat(TotACAO), sliced: true, selected: true })
                if (TotFII > 0.00) dataSetGrafico.push({ name: 'FIIs', y: parseFloat(TotFII) })
                if (TotETF > 0.00) dataSetGrafico.push({ name: 'ETFs', y: parseFloat(TotETF) })
                if (TotBDR > 0.00) dataSetGrafico.push({ name: 'BDRs', y: parseFloat(TotBDR) })
                if (TotCRIPTO > 0.00) dataSetGrafico.push({ name: 'CRIPTOs', y: parseFloat(TotCRIPTO) })

				Highcharts.chart('DivGraficoPortfAlocacaoCateg', {
					lang: {
						months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
						shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
						weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
						loading: ['Atualizando o gráfico...aguarde'],
						contextButtonTitle: 'Exportar gráfico',
						decimalPoint: ',',
						thousandsSep: '.',
						viewFullscreen: 'Exibir em tela cheia',
						openInCloud: 'Abri em Highcharts Cloud',
						downloadJPEG: 'Baixar imagem JPEG',
						downloadPDF: 'Baixar arquivo PDF',
						downloadPNG: 'Baixar imagem PNG',
						downloadSVG: 'Baixar vetor SVG',
						printChart: 'Imprimir gráfico',
						rangeSelectorFrom: 'De',
						rangeSelectorTo: 'Para',
						rangeSelectorZoom: 'Zoom',
						resetZoom: 'Limpar Zoom',
						resetZoomTitle: 'Voltar Zoom para nível 1:1',
					},
					exporting: { enabled: false },
					chart: { plotBackgroundColor: null, plotBorderWidth: null, plotShadow: false, type: 'pie' },
					title: { text: null }, // 'Alocação por Categoria'
					tooltip: { pointFormatter: function () { var value = Number(this.y).toFixed(2).replace(/./g, function (c, i, a) { return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.', ',').replace(/X/g, '.'); return 'Total: <b>R$ ' + value + '</b> <br> Percent.: <b>' + Number(this.percentage).toFixed(2) + '%</b> '; }, shared: true },
					accessibility: { point: { valueSuffix: '%' } },
					plotOptions: { pie: { allowPointSelect: true, cursor: 'pointer', dataLabels: { enabled: true, format: '<b>{point.name}</b>: {point.percentage:.2f} %' } } },
					series: [{ name: 'Categoria', colorByPoint: true, data: dataSetGrafico }]
				});
			}

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosGraficoAcoes(urlPadrao) {
	try {

		 promise = new Promise((resolve, reject) => {

			var IdPortfolio = '';
			var TipoInvest = "ACAO";
			var arCodAtivos = [];
			var arValAtual = [];

			if ((DataSetPagina) && (DataSetPagina.data) && (DataSetPagina.data.Lista)) {
				var lista = DataSetPagina.data.Lista;
				if (lista.length > 0) {
					var idx = -1;
					$.each(lista, function (index, value) {
						var CartId = value.CartId;
						var AtvTipoInvest = value.AtvTipoInvest;
						if ((IdPortfolio == "") || (IdPortfolio == CartId)) {
							if ((TipoInvest == "") || (TipoInvest == AtvTipoInvest)) {
								var AtvCodigo = value.AtvCodigo;
								var AtvTotAtual = parseFloat(GetValorDecimal(value.AtvTotAtual));  //value.AtvTotAtual;
								idx += 1;
								arCodAtivos[idx] = AtvCodigo;
								arValAtual[idx] = AtvTotAtual;
							} // if ( (TipoInvest == "") || (TipoInvest == value.AtvTipoInvest) ){
						} // if ( (IdPortfolio == "") || (IdPortfolio == value.CartId) ){
					}); // $.each(lista, function (index, value) {
				} // if ( lista.length > 0 ){
			} //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){

			var fLen = arCodAtivos.length;

			var arProftfolio = [];
			var TotalAtual = 0.00;
			for (i = 0; i < fLen; i++) {
				TotalAtual += parseFloat(arValAtual[i]);
				arProftfolio.push({ Codigo: arCodAtivos[i], ValorAtual: arValAtual[i] });
			}

			arProftfolio.sort(function (a, b) {
				var APercentAtual = parseFloat(a.ValorAtual);
				var BPercentAtual = parseFloat(b.ValorAtual);
				if (APercentAtual == BPercentAtual) return 0;
				return APercentAtual > BPercentAtual ? 1 : -1;
			});

			arProftfolio.reverse();

			var DataSetAtivos = [];
			for (i = 0; i < fLen; i++) {
				DataSetAtivos[i] = { name: arProftfolio[i].Codigo, y: parseFloat(arProftfolio[i].ValorAtual), sliced: (i == 0), selected: (i == 0) };
			}

			Highcharts.chart('DivGraficoACAOAlocacaoAtivos', {
				lang: {
					months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
					shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
					weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
					loading: ['Atualizando o gráfico...aguarde'],
					contextButtonTitle: 'Exportar gráfico',
					decimalPoint: ',',
					thousandsSep: '.',
					viewFullscreen: 'Exibir em tela cheia',
					openInCloud: 'Abri em Highcharts Cloud',
					downloadJPEG: 'Baixar imagem JPEG',
					downloadPDF: 'Baixar arquivo PDF',
					downloadPNG: 'Baixar imagem PNG',
					downloadSVG: 'Baixar vetor SVG',
					printChart: 'Imprimir gráfico',
					rangeSelectorFrom: 'De',
					rangeSelectorTo: 'Para',
					rangeSelectorZoom: 'Zoom',
					resetZoom: 'Limpar Zoom',
					resetZoomTitle: 'Voltar Zoom para nível 1:1',
				},
				exporting: { enabled: false },
				chart: { plotBackgroundColor: null, plotBorderWidth: null, plotShadow: false, type: 'pie' },
				title: { text: null }, // 'Alocação por Ativos'
				//tooltip: { pointFormat: '{series.name}: <b>{point.percentage:.2f}%</b>' },
				//tooltip: { pointFormat: 'R$ {point.y:.2f} <b>{point.percentage:.2f}%</b>' },
				tooltip: { pointFormatter: function () { var value = Number(this.y).toFixed(2).replace(/./g, function (c, i, a) { return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.', ',').replace(/X/g, '.'); return 'Total: <b>R$ ' + value + '</b> <br> Percent.: <b>' + Number(this.percentage).toFixed(2) + '%</b> '; }, shared: true },
				plotOptions: { pie: { allowPointSelect: true, cursor: 'pointer', dataLabels: { enabled: true, format: '<b>{point.name}</b>: {point.percentage:.2f} %' } } },
				series: [{ name: 'Alocação por Ativos', colorByPoint: true, data: DataSetAtivos }]
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosGraficoFIIs(urlPadrao) {
	try {

		promise = new Promise((resolve, reject) => {

			var IdPortfolio = '';
			var TipoInvest = "FII";
			var arCodAtivos = [];
			var arValAtual = [];

			if ((DataSetPagina) && (DataSetPagina.data) && (DataSetPagina.data.Lista)) {
				var lista = DataSetPagina.data.Lista;
				if (lista.length > 0) {
					var idx = -1;
					$.each(lista, function (index, value) {
						var CartId = value.CartId;
						var AtvTipoInvest = value.AtvTipoInvest;
						if ((IdPortfolio == "") || (IdPortfolio == CartId)) {
							if ((TipoInvest == "") || (TipoInvest == AtvTipoInvest)) {
								var AtvCodigo = value.AtvCodigo;
								var AtvTotAtual = parseFloat(GetValorDecimal(value.AtvTotAtual));  //value.AtvTotAtual;
								idx += 1;
								arCodAtivos[idx] = AtvCodigo;
								arValAtual[idx] = AtvTotAtual;
							} // if ( (TipoInvest == "") || (TipoInvest == value.AtvTipoInvest) ){
						} // if ( (IdPortfolio == "") || (IdPortfolio == value.CartId) ){
					}); // $.each(lista, function (index, value) {
				} // if ( lista.length > 0 ){
			} //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){

			var fLen = arCodAtivos.length;

			var arProftfolio = [];
			var TotalAtual = 0.00;
			for (i = 0; i < fLen; i++) {
				TotalAtual += parseFloat(arValAtual[i]);
				arProftfolio.push({ Codigo: arCodAtivos[i], ValorAtual: arValAtual[i] });
			}

			arProftfolio.sort(function (a, b) {
				var APercentAtual = parseFloat(a.ValorAtual);
				var BPercentAtual = parseFloat(b.ValorAtual);
				if (APercentAtual == BPercentAtual) return 0;
				return APercentAtual > BPercentAtual ? 1 : -1;
			});

			arProftfolio.reverse();

			var DataSetAtivos = [];
			for (i = 0; i < fLen; i++) {
				DataSetAtivos[i] = { name: arProftfolio[i].Codigo, y: parseFloat(arProftfolio[i].ValorAtual), sliced: (i == 0), selected: (i == 0) };
			}

			Highcharts.chart('DivGraficoFIIAlocacaoAtivos', {
				lang: {
					months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
					shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
					weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
					loading: ['Atualizando o gráfico...aguarde'],
					contextButtonTitle: 'Exportar gráfico',
					decimalPoint: ',',
					thousandsSep: '.',
					viewFullscreen: 'Exibir em tela cheia',
					openInCloud: 'Abri em Highcharts Cloud',
					downloadJPEG: 'Baixar imagem JPEG',
					downloadPDF: 'Baixar arquivo PDF',
					downloadPNG: 'Baixar imagem PNG',
					downloadSVG: 'Baixar vetor SVG',
					printChart: 'Imprimir gráfico',
					rangeSelectorFrom: 'De',
					rangeSelectorTo: 'Para',
					rangeSelectorZoom: 'Zoom',
					resetZoom: 'Limpar Zoom',
					resetZoomTitle: 'Voltar Zoom para nível 1:1',
				},
				exporting: { enabled: false },
				chart: { plotBackgroundColor: null, plotBorderWidth: null, plotShadow: false, type: 'pie' },
				title: { text: null }, // 'Alocação por FIIs'
				//tooltip: { pointFormat: '{series.name}: <b>{point.percentage:.2f}%</b>' },
				//tooltip: { pointFormat: 'R$ {point.y:.2f} <b>{point.percentage:.2f}%</b>' },
				tooltip: { pointFormatter: function () { var value = Number(this.y).toFixed(2).replace(/./g, function (c, i, a) { return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.', ',').replace(/X/g, '.'); return 'Total: <b>R$ ' + value + '</b> <br> Percent.: <b>' + Number(this.percentage).toFixed(2) + '%</b> '; }, shared: true },
				plotOptions: { pie: { allowPointSelect: true, cursor: 'pointer', dataLabels: { enabled: true, format: '<b>{point.name}</b>: {point.percentage:.2f} %' } } },
				series: [{ name: 'Ativos', colorByPoint: true, data: DataSetAtivos }]
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosGraficoETFs(urlPadrao) {
	try {

		promise = new Promise((resolve, reject) => {

			var IdPortfolio = '';
			var TipoInvest = "ETF";
			var arCodAtivos = [];
			var arValAtual = [];

			if ((DataSetPagina) && (DataSetPagina.data) && (DataSetPagina.data.Lista)) {
				var lista = DataSetPagina.data.Lista;
				if (lista.length > 0) {
					var idx = -1;
					$.each(lista, function (index, value) {
						var CartId = value.CartId;
						var AtvTipoInvest = value.AtvTipoInvest;
						if ((IdPortfolio == "") || (IdPortfolio == CartId)) {
							if ((TipoInvest == "") || (TipoInvest == AtvTipoInvest)) {
								var AtvCodigo = value.AtvCodigo;
								var AtvTotAtual = parseFloat(GetValorDecimal(value.AtvTotAtual));  //value.AtvTotAtual;
								idx += 1;
								arCodAtivos[idx] = AtvCodigo;
								arValAtual[idx] = AtvTotAtual;
							} // if ( (TipoInvest == "") || (TipoInvest == value.AtvTipoInvest) ){
						} // if ( (IdPortfolio == "") || (IdPortfolio == value.CartId) ){
					}); // $.each(lista, function (index, value) {
				} // if ( lista.length > 0 ){
			} //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){

			var fLen = arCodAtivos.length;

			var arProftfolio = [];
			var TotalAtual = 0.00;
			for (i = 0; i < fLen; i++) {
				TotalAtual += parseFloat(arValAtual[i]);
				arProftfolio.push({ Codigo: arCodAtivos[i], ValorAtual: arValAtual[i] });
			}

			arProftfolio.sort(function (a, b) {
				var APercentAtual = parseFloat(a.ValorAtual);
				var BPercentAtual = parseFloat(b.ValorAtual);
				if (APercentAtual == BPercentAtual) return 0;
				return APercentAtual > BPercentAtual ? 1 : -1;
			});

			arProftfolio.reverse();

			var DataSetAtivos = [];
			for (i = 0; i < fLen; i++) {
				DataSetAtivos[i] = { name: arProftfolio[i].Codigo, y: parseFloat(arProftfolio[i].ValorAtual), sliced: (i == 0), selected: (i == 0) };
			}

			Highcharts.chart('DivGraficoETFAlocacaoAtivos', {
				lang: {
					months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
					shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
					weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
					loading: ['Atualizando o gráfico...aguarde'],
					contextButtonTitle: 'Exportar gráfico',
					decimalPoint: ',',
					thousandsSep: '.',
					viewFullscreen: 'Exibir em tela cheia',
					openInCloud: 'Abri em Highcharts Cloud',
					downloadJPEG: 'Baixar imagem JPEG',
					downloadPDF: 'Baixar arquivo PDF',
					downloadPNG: 'Baixar imagem PNG',
					downloadSVG: 'Baixar vetor SVG',
					printChart: 'Imprimir gráfico',
					rangeSelectorFrom: 'De',
					rangeSelectorTo: 'Para',
					rangeSelectorZoom: 'Zoom',
					resetZoom: 'Limpar Zoom',
					resetZoomTitle: 'Voltar Zoom para nível 1:1',
				},
				exporting: { enabled: false },
				chart: { plotBackgroundColor: null, plotBorderWidth: null, plotShadow: false, type: 'pie' },
				title: { text: null }, // 'Alocação por ETFs'
				//tooltip: { pointFormat: '{series.name}: <b>{point.percentage:.2f}%</b>' },
				//tooltip: { pointFormat: 'R$ {point.y:.2f} <b>{point.percentage:.2f}%</b>' },
				tooltip: { pointFormatter: function () { var value = Number(this.y).toFixed(2).replace(/./g, function (c, i, a) { return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.', ',').replace(/X/g, '.'); return 'Total: <b>R$ ' + value + '</b> <br> Percent.: <b>' + Number(this.percentage).toFixed(2) + '%</b> '; }, shared: true },
				plotOptions: { pie: { allowPointSelect: true, cursor: 'pointer', dataLabels: { enabled: true, format: '<b>{point.name}</b>: {point.percentage:.2f} %' } } },
				series: [{ name: 'Ativos', colorByPoint: true, data: DataSetAtivos }]
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosGraficoBDRs(urlPadrao) {
	try {

		 promise = new Promise((resolve, reject) => {

			var IdPortfolio = '';
			var TipoInvest = "BDR";
			var arCodAtivos = [];
			var arValAtual = [];

			if ((DataSetPagina) && (DataSetPagina.data) && (DataSetPagina.data.Lista)) {
				var lista = DataSetPagina.data.Lista;
				if (lista.length > 0) {
					var idx = -1;
					$.each(lista, function (index, value) {
						var CartId = value.CartId;
						var AtvTipoInvest = value.AtvTipoInvest;
						if ((IdPortfolio == "") || (IdPortfolio == CartId)) {
							if ((TipoInvest == "") || (TipoInvest == AtvTipoInvest)) {
								var AtvCodigo = value.AtvCodigo;
								var AtvTotAtual = parseFloat(GetValorDecimal(value.AtvTotAtual));  //value.AtvTotAtual;
								idx += 1;
								arCodAtivos[idx] = AtvCodigo;
								arValAtual[idx] = AtvTotAtual;
							} // if ( (TipoInvest == "") || (TipoInvest == value.AtvTipoInvest) ){
						} // if ( (IdPortfolio == "") || (IdPortfolio == value.CartId) ){
					}); // $.each(lista, function (index, value) {
				} // if ( lista.length > 0 ){
			} //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){

			var fLen = arCodAtivos.length;

			var arProftfolio = [];
			var TotalAtual = 0.00;
			for (i = 0; i < fLen; i++) {
				TotalAtual += parseFloat(arValAtual[i]);
				arProftfolio.push({ Codigo: arCodAtivos[i], ValorAtual: arValAtual[i] });
			}

			arProftfolio.sort(function (a, b) {
				var APercentAtual = parseFloat(a.ValorAtual);
				var BPercentAtual = parseFloat(b.ValorAtual);
				if (APercentAtual == BPercentAtual) return 0;
				return APercentAtual > BPercentAtual ? 1 : -1;
			});

			arProftfolio.reverse();

			var DataSetAtivos = [];
			for (i = 0; i < fLen; i++) {
				DataSetAtivos[i] = { name: arProftfolio[i].Codigo, y: parseFloat(arProftfolio[i].ValorAtual), sliced: (i == 0), selected: (i == 0) };
			}

			Highcharts.chart('DivGraficoBDRAlocacaoAtivos', {
				lang: {
					months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
					shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
					weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
					loading: ['Atualizando o gráfico...aguarde'],
					contextButtonTitle: 'Exportar gráfico',
					decimalPoint: ',',
					thousandsSep: '.',
					viewFullscreen: 'Exibir em tela cheia',
					openInCloud: 'Abri em Highcharts Cloud',
					downloadJPEG: 'Baixar imagem JPEG',
					downloadPDF: 'Baixar arquivo PDF',
					downloadPNG: 'Baixar imagem PNG',
					downloadSVG: 'Baixar vetor SVG',
					printChart: 'Imprimir gráfico',
					rangeSelectorFrom: 'De',
					rangeSelectorTo: 'Para',
					rangeSelectorZoom: 'Zoom',
					resetZoom: 'Limpar Zoom',
					resetZoomTitle: 'Voltar Zoom para nível 1:1',
				},
				exporting: { enabled: false },
				chart: { plotBackgroundColor: null, plotBorderWidth: null, plotShadow: false, type: 'pie' },
				title: { text: null }, // 'Alocação por BDRs'
				//tooltip: { pointFormat: '{series.name}: <b>{point.percentage:.2f}%</b>' },
				//tooltip: { pointFormat: 'R$ {point.y:.2f} <b>{point.percentage:.2f}%</b>' },
				tooltip: { pointFormatter: function () { var value = Number(this.y).toFixed(2).replace(/./g, function (c, i, a) { return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.', ',').replace(/X/g, '.'); return 'Total: <b>R$ ' + value + '</b> <br> Percent.: <b>' + Number(this.percentage).toFixed(2) + '%</b> '; }, shared: true },
				plotOptions: { pie: { allowPointSelect: true, cursor: 'pointer', dataLabels: { enabled: true, format: '<b>{point.name}</b>: {point.percentage:.2f} %' } } },
				series: [{ name: 'Ativos', colorByPoint: true, data: DataSetAtivos }]
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarrgarDadosGraficoCRIPTOs(urlPadrao) {
	try {

		promise = new Promise((resolve, reject) => {

			var IdPortfolio = '';
			var TipoInvest = "CRIPTO";
			var arCodAtivos = [];
			var arValAtual = [];

			if ((DataSetPagina) && (DataSetPagina.data) && (DataSetPagina.data.Lista)) {
				var lista = DataSetPagina.data.Lista;
				if (lista.length > 0) {
					var idx = -1;
					$.each(lista, function (index, value) {
						var CartId = value.CartId;
						var AtvTipoInvest = value.AtvTipoInvest;
						if ((IdPortfolio == "") || (IdPortfolio == CartId)) {
							if ((TipoInvest == "") || (TipoInvest == AtvTipoInvest)) {
								var AtvCodigo = value.AtvCodigo;
								var AtvTotAtual = parseFloat(GetValorDecimal(value.AtvTotAtual));  //value.AtvTotAtual;
								idx += 1;
								arCodAtivos[idx] = AtvCodigo;
								arValAtual[idx] = AtvTotAtual;
							} // if ( (TipoInvest == "") || (TipoInvest == value.AtvTipoInvest) ){
						} // if ( (IdPortfolio == "") || (IdPortfolio == value.CartId) ){
					}); // $.each(lista, function (index, value) {
				} // if ( lista.length > 0 ){
			} //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){

			var fLen = arCodAtivos.length;

			var arProftfolio = [];
			var TotalAtual = 0.00;
			for (i = 0; i < fLen; i++) {
				TotalAtual += parseFloat(arValAtual[i]);
				arProftfolio.push({ Codigo: arCodAtivos[i], ValorAtual: arValAtual[i] });
			}

			arProftfolio.sort(function (a, b) {
				var APercentAtual = parseFloat(a.ValorAtual);
				var BPercentAtual = parseFloat(b.ValorAtual);
				if (APercentAtual == BPercentAtual) return 0;
				return APercentAtual > BPercentAtual ? 1 : -1;
			});

			arProftfolio.reverse();

			var DataSetAtivos = [];
			for (i = 0; i < fLen; i++) {
				DataSetAtivos[i] = { name: arProftfolio[i].Codigo, y: parseFloat(arProftfolio[i].ValorAtual), sliced: (i == 0), selected: (i == 0) };
			}

			Highcharts.chart('DivGraficoCRIPTOAlocacaoAtivos', {
				lang: {
					months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
					shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
					weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
					loading: ['Atualizando o gráfico...aguarde'],
					contextButtonTitle: 'Exportar gráfico',
					decimalPoint: ',',
					thousandsSep: '.',
					viewFullscreen: 'Exibir em tela cheia',
					openInCloud: 'Abri em Highcharts Cloud',
					downloadJPEG: 'Baixar imagem JPEG',
					downloadPDF: 'Baixar arquivo PDF',
					downloadPNG: 'Baixar imagem PNG',
					downloadSVG: 'Baixar vetor SVG',
					printChart: 'Imprimir gráfico',
					rangeSelectorFrom: 'De',
					rangeSelectorTo: 'Para',
					rangeSelectorZoom: 'Zoom',
					resetZoom: 'Limpar Zoom',
					resetZoomTitle: 'Voltar Zoom para nível 1:1',
				},
				exporting: { enabled: false },
				chart: { plotBackgroundColor: null, plotBorderWidth: null, plotShadow: false, type: 'pie' },
				title: { text: null }, // 'Alocação por FIIs'
				//tooltip: { pointFormat: '{series.name}: <b>{point.percentage:.2f}%</b>' },
				//tooltip: { pointFormat: 'R$ {point.y:.2f} <b>{point.percentage:.2f}%</b>' },
				tooltip: { pointFormatter: function () { var value = Number(this.y).toFixed(2).replace(/./g, function (c, i, a) { return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.', ',').replace(/X/g, '.'); return 'Total: <b>R$ ' + value + '</b> <br> Percent.: <b>' + Number(this.percentage).toFixed(2) + '%</b> '; }, shared: true },
				plotOptions: { pie: { allowPointSelect: true, cursor: 'pointer', dataLabels: { enabled: true, format: '<b>{point.name}</b>: {point.percentage:.2f} %' } } },
				series: [{ name: 'Ativos', colorByPoint: true, data: DataSetAtivos }]
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
			.then(txt => {
				//console.log('Sucesso: ' + txt);
			})
			.catch(txt => {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			});

	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}