
$(document).ready(function() {

	//$(this).attr("title", ":: TnB - Dashboard ::");

	$("#MnPrincDashboard").addClass("active open");

	fLimparAreaAlertaPrinc();
	fLimparAreaAlertaModalCad();
	fLimparAreaAlertaModalExc();
	fLimparAreaAlerta("AreaAlertaModalCadProv");

    $("#FormOper input[type=text]").bind("keyup change", function(){ fCalcularOperacao(); });
    $("#FormOperCripto input[type=text]").bind("keyup change", function(){ fCalcularOperacaoCripto(); });

	$("#txtDivQuant").bind("keyup change",      function(){ fCalcularDividendo(); } );
	$("#txtDivPreco").bind("keyup change",      function(){ fCalcularDividendo(); } );
	$("#selDivTipo").bind("change",             function(){ fMostrarCalcVlrLiq(); fMostrarValorBruto(); fCalcularDividendo(); } );
	$("#txtDivCalcVlrLiq").bind("change",       function(){ fMostrarValorBruto(); fCalcularDividendo(); } );
	$("#txtDivPrecoBruto" ).unbind( "keyup"  );
	$("#txtDivPrecoBruto" ).unbind( "change" );

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

                fCarregarDadosPagina( urlPadrao );

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

async function fCarregarDadosPagina(urlPadrao) {
    // fMostrarEsconderValores();
    // fLimparTotalizadores(urlPadrao);
    fCarrgarDadosTotalizadores(urlPadrao);
    setTimeout( function(){
        fCarrgarDadosProventos(urlPadrao);
        fCarrgarDadosCalendario(urlPadrao);
    }, 1000);
}