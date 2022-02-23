
$(document).ready(function() {

});

function iniciarAnimacaoProcessar() {
    $("#iProcessar").removeClass("fa-check");
    $("#iProcessar").addClass("fa-spin");
    $("#iProcessar").addClass("fa-refresh");
    $("#btnProcessar").addClass("disabled");
}

function finalizarAnimacaoProcessar() {
    $("#iProcessar").addClass("fa-check");
    $("#iProcessar").removeClass("fa-spin");
    $("#iProcessar").removeClass("fa-refresh");
    $("#btnProcessar").removeClass("disabled");
}

async function fProcessar( urlPadrao ){
    try {

        finalizarAnimacaoProcessar();
        iniciarAnimacaoProcessar();

        $("#DivResultado").html("");

        var trades = $("#txtTrades").val();

        if ( trades.trim() == "" ){
            $("#DivResultado").html("VAZIO");
            finalizarAnimacaoProcessar();
            return;
        }

        $("#DivResultado").html(
            '<div class="row clearfix"> '+
            '  <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 text-center" style="padding-left: 5px; padding-right: 5px;" > '+
            '    <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> '+
            '  </div> '+
            '</div> '
        );

        promise = new Promise( (resolve, reject) => {

            $.ajax({
                cache   : "false",
                dataType: "html",
                async   : true,
                type    : "POST",
                url: "/criptofoxbit/processar",
                data: { trades: trades },
                success: function(result) {
                    $("#DivResultado").html("");
                    $("#DivResultado").html(result);
                    finalizarAnimacaoProcessar();
                },
                error: function(data) {
                    finalizarAnimacaoProcessar();
                     $("#DivResultado").html(MSG_ALERTA_ERRO);
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
			finalizarAnimacaoProcessar();
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

    } catch (e) {
        finalizarAnimacaoProcessar();
        if ( e.description != undefined ) $("#DivResultado").html(MSG_ALERTA_ERRO);
    }
}

async function fSalvar( indexTr, Tipo, Ativo, Data, Quant, Preco, Taxas ){
	try {

        promise = new Promise( (resolve, reject) => {

            $("#GridTr-"+indexTr).children('td').removeClass('text-muted');
            $("#GridTr-"+indexTr).children('td').removeClass('text-danger');
            $("#GridTr-"+indexTr).children('td').removeClass('text-danger');

            $("#GridTr-"+indexTr).children('td').addClass('text-muted');
            // var tr =$("#GridTr-"+indexTr).closest('tr');
            // tr.fadeOut(400);

            $("#GridSalvar-"+indexTr).addClass("disabled");

		    $.ajax({
                cache   : "false",
                dataType: "json",
                async   : true,
                type    : "POST",
                url     : "/operacoes/salvar",
                data    : { Id: "", Tipo: Tipo, Ativo: Ativo, Data: Data, Quant: Quant, Preco: Preco, Corretora: 184, TxCorret: Taxas, },
                success: function(result) {
                    var resultado = result.data.Resultado;
                    var mensagem = result.data.Mensagem;
                    if (resultado == "NSESSAO") {
                        $(location).attr('href', urlPadrao + '/login');
                        return false;
                    } else if (resultado == "NOK") {
                        $("#GridTr-"+indexTr).children('td').removeClass('text-muted');
                        $("#GridTr-"+indexTr).children('td').addClass('text-danger');
                        $("#GridSalvar-"+indexTr).removeClass("disabled");
                        fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, mensagem);
                        return;
                    } else if (resultado == "FALHA") {
                        $("#GridTr-"+indexTr).children('td').removeClass('text-muted');
                        $("#GridTr-"+indexTr).children('td').addClass('text-danger');
                        $("#GridSalvar-"+indexTr).removeClass("disabled");
                        fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
                        return;
                    } else if (resultado == "OK") {
                        $("#GridTr-"+indexTr).children('td').removeClass('text-muted');
                        $("#GridTr-"+indexTr).children('td').addClass('text-success');
                        $("#GridTr-"+indexTr).find("td:eq(7)").text('');
                    } else {
                        $("#GridTr-"+indexTr).children('td').removeClass('text-muted');
                        $("#GridTr-"+indexTr).children('td').addClass('text-danger');
                        $("#GridSalvar-"+indexTr).removeClass("disabled");
                        fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
                        return;
                    }
                },
                error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
                    $("#GridTr-"+indexTr).children('td').removeClass('text-muted');
                    $("#GridTr-"+indexTr).children('td').addClass('text-danger');
                    $("#GridSalvar-"+indexTr).removeClass("disabled");
                    fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText //MSG_ALERTA_ERRO
                    return;
                }
            });

            resolve(true);
            // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
        })
        .then( txt => {
            //console.log('Sucesso: ' + txt);
        })
        .catch( txt => {
            $("#GridTr-"+indexTr).children('td').removeClass('text-muted');
            $("#GridTr-"+indexTr).children('td').addClass('text-danger');
            $("#GridSalvar-"+indexTr).removeClass("disabled");
            fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
        });

	} catch (e) {
		if ( e.description != undefined ) CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}