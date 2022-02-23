

function fAbrirModalDetalheAgendaTrimestre(urlPadrao) {
    fBuscarDadosAgendaTrimestre(urlPadrao, 'P'); // P-Portfolio
    fBuscarDadosAgendaTrimestre(urlPadrao, 'R'); // R-Radar
    fBuscarDadosAgendaTrimestre(urlPadrao, 'T'); // T-Todos
}

function fBuscarDadosAgendaTrimestre( urlPadrao, Tipo ) {
    try {

        if ( Tipo == 'P'){ // P-Portfolio
            var DivTable = $("#AreaTableModalAgendaTrimestrePortfolio");
            DivTable.html( "" );
        } else if ( Tipo == 'R'){ // R-Radar
            var DivTable = $("#AreaTableModalAgendaTrimestreRadar");
            DivTable.html( "" );
        } else if ( Tipo == 'T'){ // T-Todos
            var DivTable = $("#AreaTableModalAgendaTrimestreTodos");
            DivTable.html( "" );
        } else {
            fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, 'Tipo Inválido: ' + Tipo );
            return;
        }

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "principal/agendatrimestre",
			data: { Tipo: Tipo },
			success: function(result) {
				var resultado = result.data.Resultado;
				var mensagem  = result.data.Mensagem;
				var lista     = result.data.Lista;
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
                    let dataAtual = moment().format('YYYYMMDD').toString();
                    var content = '';
                    if ( lista.length > 0 ){
                        content += '<div class="table-responsive">';
                        content += '<table border="0" style="font-size: 13px" class="table table-sm table-hover table-condensed" cellspacing="0" width="100%">';
                        content += '  <tbody>';
                        $.each(lista, function (index, value) {
                            empresa = value[0];
                            codigo = value[1];
                            divulgacao = value[2];
                            horario = value[3];
                            let corTexto =  dataAtual >= divulgacao ? 'text-primary font-weight-bold ' : 'text-dark'
                            content += '    <tr class="'+corTexto+'"> ';
                            content += '      <td class="font-weight-bold">'+codigo+'</td>';
                            content += '      <td>'+empresa+'</td>';
                            content += '      <td class="font-weight-bold">'+colcarFormacataoData(divulgacao)+'</td>';
                            content += '      <td>'+horario+'</td>';
                            content += '    </tr>';
                        });
                        content += '  </tbody>';
                        content += '</table>';
                        content += '</div>';
                    } else {
                        content += ' <div class="text-center"><small style="font-size:14px; margin: 20px; " class="font-italic text-muted">Agenda de Divulgação do Trimestre Vazia!!!</small></div> ';
                    }

                    DivTable.append( content );
                    $("#PopModalAgendaTrimestre").modal({backdrop: "static"});
                    return;

				} else {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem);
					return;
				}

			},
			error: function(data) {
				fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
				return;
			}
		});

    } catch (e) {
        $("#PopModalAgendaTrimestre").modal("hide");
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}