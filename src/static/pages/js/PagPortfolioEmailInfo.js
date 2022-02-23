
function fAbrirModalDetalheEmailInfo( urlPadrao ) {
    try {

		$("#AreaAlertaModalInfo").html("");
		$("#AreaAlertaPrinc").html("");
		
		//$("#txtPortEmailInfoStatus").attr("checked", false);
		document.getElementById("txtPortEmailInfoStatus").checked = false;

		var IdPortfolio = fGetAbaIdPortfolio();
		var TipoInvest  = fGetAbaTipoPortfolio();

		var NomePortfolio = $("#Aba"+IdPortfolio).html();
		if ( NomePortfolio )  NomePortfolio = NomePortfolio.replace('<i class="fa fa-sliders"></i>&nbsp;', "");
		if ( !NomePortfolio ) NomePortfolio = 'Meu Portfólio';
		$("#txtPortEmailInfoCart").html('"'+NomePortfolio.trim()+'"');

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "portfolio/carregarEmailInfo",
			data: { IdPortfolio: IdPortfolio, TipoInvest: TipoInvest },
			success: function(result) {  
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var EmailInfo = result.data.Dados;
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					if (EmailInfo.StatusInfo) {
						 $("#txtPortEmailInfoStatus").attr("checked", EmailInfo.StatusInfo == 'A' );
						 document.getElementById("txtPortEmailInfoStatus").checked = EmailInfo.StatusInfo == 'A';
						$("#PopModalEmailInfoPortfolio").modal({backdrop: "static"});
					}
				} else {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function(data) {
				finalizarAnimacaoSalvar();
				fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});

    } catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fSalvarDadosEmailInfoPortfolio( urlPadrao ) {
    try {
		
		$("#AreaAlertaModalInfo").html("");
		$("#AreaAlertaPrinc").html("");

		var IdPortfolio = fGetAbaIdPortfolio();
		var TipoInvest  = fGetAbaTipoPortfolio();

		var StatusInfo  = $("#txtPortEmailInfoStatus").is(":checked") ? "A" : "I";

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "portfolio/salvarEmailInfo",
			data: { IdPortfolio: IdPortfolio, TipoInvest: TipoInvest, StatusInfo:  StatusInfo },
			success: function(result) {  
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var EmailInfo = result.data.Dados;
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaModalInfo",TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaModalInfo",TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					//$("#txtPortEmailInfoStatus").attr("checked", false);
					document.getElementById("txtPortEmailInfoStatus").checked = false;
					$("#txtPortEmailInfoCart").html("");
					$("#PopModalEmailInfoPortfolio").modal("hide");
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
				} else {
					fCriarAlerta("AreaAlertaModalInfo",TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function(data) {
				finalizarAnimacaoSalvar();
				fCriarAlerta("AreaAlertaModalInfo",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});

    } catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}
