
$(document).ready(function () {
	// $(this).attr("title", "Log Erros - " + NOME_PROJETO);
	$("#MnPrincLogErros").addClass("active open");
	fLimparAreaAlertaPrinc();
});

function fLimparGrid() {
	try {

		$('#GridGeral tr').not(':nth-child(1)').remove();

	} catch (e) {
		if (e.description != undefined) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

function fCarregarGrid(urlPadrao, LogErrTipo) {
	try {

		$.ajax({
			cache: "false",
			dataType: "json",
			async: true,
			type: "POST",
			url: urlPadrao + "logErro/grid",
			//data: { LogErrTipo: LogErrTipo, LogErrData: LogErrData, LogErrIdUltimo: LogErrIdUltimo },
			success: function (result) {

				var resultado = result.data.Resultado;
				var mensagem  = result.data.Mensagem;
				var lista     = result.data.Lista;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
					return;
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
					return;
				} else if (resultado == "OK") {
					if (lista.length > 0) {
						var textLinha = "";
						$.each(lista, function (index, value) {
							textLinha = "text-muted";
                            if (value[7] == "N") textLinha = "text-danger"; // 7-Situacao
                            $('#GridGeral tr:first').after(
                                '<tr class="' + textLinha + '">' +
                                ' <td style="width:20px;">' + colcarFormacataoDataHora(value[0]) + '</td>' + // 0-Hora
                                ' <td style="width:20px;">' + value[1] + '</td>' + // 1-Arquivo
                                ' <td style="width:20px;">' + value[2] + '</td>' + // 2-Usuário
                                ' <td style="width:10px;">' + value[3] + '</td>' + // 3-Linha
                                ' <td style="width:10px;">' + value[4] + '</td>' + // 4-Código
                                ' <td style="width:500px;">' + value[5] + '</td>' + // 5-Texto
                                ' <td style="display: none;">' + value[6] + '</td>' + // 6-IdLogErro
                                '</tr>'
                            );
						});
					}
				} else {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
					return;
				}

			},
			error: function (data) {
				fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
				return false;
			}
		});

	} catch (e) {
		if (e.description != undefined) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

function fExcluirLog(urlPadrao, LogErrTipo) {
	try {

		$.ajax({
			cache: "false",
			dataType: "json",
			async: true,
			type: "POST",
			url: urlPadrao + "logErro/excluir",
			//data: { LogErrTipo: LogErrTipo, LogErrData: LogErrData, LogErrIdUltimo: LogErrIdUltimo },
			success: function (result) {

				var resultado = result.data.Resultado;
				var mensagem = result.data.Mensagem;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
					return;
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
					return;
				} else if (resultado == "OK") {
					//fCriarAlertaPrinc(TP_ALERTA_SUCESSO, "Ok");
					fLimparGrid(urlPadrao);
					fCarregarGrid(urlPadrao);
				} else {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
					return;
				}
			},
			error: function (data) {
				fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
				return false;
			}
		});

	} catch (e) {
		if (e.description != undefined) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

function fMarcarLog(urlPadrao, LogErrTipo) {
	try {


		$.ajax({
			cache: "false",
			dataType: "json",
			async: true,
			type: "POST",
			url: urlPadrao + "logErro/marcar",
			// data: { LogErrTipo: LogErrTipo, LogErrData: LogErrData, LogErrIdUltimo: LogErrIdUltimo },
			success: function (result) {

				var resultado = result.data.Resultado;
				var mensagem = result.data.Mensagem;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
					return;
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
					return;
				} else if (resultado == "OK") {
					//fCriarAlertaPrinc(TP_ALERTA_SUCESSO, "Ok");
					fLimparGrid(urlPadrao);
					fCarregarGrid(urlPadrao);
				} else {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
					return;
				}
			},
			error: function (data) {
				fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
				return false;
			}
		});

	} catch (e) {
		if (e.description != undefined) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}
