
function fMontaDadosProvento( urlPadrao, value ){

	var retorno = "";

	var dataa = new Date();
	var dia   = ("0" + dataa.getDate()).substr(-2);
	var mes   = ("0" + (dataa.getMonth() + 1)).substr(-2) ;
	var ano   = dataa.getFullYear();
	var DataAtual = ano + mes + dia;

	var DtPagto     = value[0]; // 0 - Data
	var Tipo        = value[1]; // 1 - Tipo
	var Ativos      = value[2]; // 2 - Ativos
	var Qtde        = value[3]; // 3 - Qtde
	var Preco       = value[4]; // 4 - Preco
	var Total       = value[5]; // 5 - Total
	var Situacao    = value[6]; // 6 - Situacao
	var IdProv      = value[7]; // 7 - IdProv
	
	var DscSituacao = "";	
	var DscTipo     = "";	
	var CorSituacao = "";	
	var LegSituacao = "";	
	
	if ( Situacao  == 'A' ){ // A - Ativo
		DscSituacao = 'Aprovado';
		CorSituacao = ( DtPagto > DataAtual ? 'badge-primary' : 'badge-success' );
		LegSituacao = ( DtPagto > DataAtual ? 'PROVENTO A RECEBER' : 'PROVENTO RECEBIDO' );
	}
	if ( Situacao  == 'B' ){ // B - Pendente Aprovação/Confirmação
		DscSituacao = 'Pendente';
		CorSituacao = ( DtPagto > DataAtual ? 'badge-warning' : 'badge-danger' );
		LegSituacao = ( DtPagto > DataAtual ? 'PROVENTO A RECEBER PENDENTE DE APROVAÇÃO' : 'PROVENTO RECEBIDO PENDENTE DE APROVAÇÃO' );
	}

	if ( Tipo == 'D'  ) DscTipo = 'DIVIDENDOS';
	if ( Tipo == 'J'  ) DscTipo = 'JRS CAP PRÓPRIO';
	if ( Tipo == 'R'  ) DscTipo = 'REST CAP DIN';
	if ( Tipo == 'FR' ) DscTipo = 'RENDIMENTO';

	retorno += "<tr style='height: 30px;' class='"+( DtPagto > DataAtual  ? 'text-muted' : 'text-muted' )+"'>";
	retorno += "  <td style='width=5px;'>"+colcarFormacataoData(DtPagto)+"</td>";
	retorno += "  <td style='width=5px; font-size:11px;' ><b>"+Ativos+"</b></td>";
	retorno += "  <td style='width=150px; font-size:11px;' >"+DscTipo+"</td>";
	retorno += "  <td style='width=150px; font-size:11px;' class='font-weight-bold'>R$ "+Total+"</td>";
	retorno += "  <td style='width=150px; vertical-align: bottom;'> ";
	retorno += "    <span style=' vertical-align: bottom; font-size:11px;' title='"+LegSituacao+"' class='badge badge-pill "+CorSituacao+"'>"+DscSituacao+"</span>";
	retorno += "    <span style='float: right;'>";
	if ( Situacao  == 'B' ) {
		retorno += '      <a class="btn btn-sm btn-success btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.6rem; min-width: 1.6rem; width: 1.6rem; margin: 1px 1px; font-size:0.5rem;" title="Aprovar Provento" href="javascript:void(0);" onclick="fAprovarProventos( \''+urlPadrao+'\', \''+IdProv+'\', \''+Ativos+'\' );"><i class="fa fa-check fa-2x" aria-hidden="true"></i> </a>';
		retorno += "      &nbsp;";
	}
	retorno += '      <a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.6rem; min-width: 1.6rem; width: 1.6rem; margin: 1px 1px; font-size:0.5rem;" title="Editar Provento" href="javascript:void(0)" onclick="fAbrirModalDetalheRend( \''+urlPadrao+'\', \''+IdProv+'\', \''+Ativos+'\', \'Alterar\' );"><i class="fa fa-pencil fa-2x" aria-hidden="true"></i> </a>';
	retorno += "      &nbsp;";
	retorno += '      <a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.6rem; min-width: 1.6rem; width: 1.6rem; margin: 1px 1px; font-size:0.5rem;" title="Excluir Provento" href="javascript:void(0);" onclick="fChamarPagExclusaoRend( \''+IdProv+'\', \''+Ativos+'\' );"><i class="fa fa-trash-o fa-2x" aria-hidden="true"></i> </a>';
	retorno += "    </span>";
	retorno += "  </td>";
	retorno += "</tr>";

	return retorno;
	
}

async function fCarrgarDadosProventos( urlPadrao ){
  try {

		 promise = new Promise( (resolve, reject) => {

            let logNome = '@TamoNaBolsa - PagPrincipalProventos'

            // console.log(logNome + ' - INI - ', moment().format())
            console.time(logNome + ' - TEMPO')

            $.ajax({
              cache   : "false",
              dataType: "json",
              async   : true,
              type    : "POST",
              url     : urlPadrao + "principal/carregarProventos",
              success: function(result) {

                  var resultado = result.data.Resultado;
                  var mensagem  = result.data.Mensagem;
                  var lista     = result.data.Lista;

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

                         if ( lista && lista.length > 0 ){

                                $("#DivConteudoProv").html('');

                                var TotalGeral   = 0.00;
                                var Total        = 0.00;
                                var UltimoMesAno = "";
                                var MesAnoAtual  = "";
                                var arTotal      = [];
                                var iLen         = 0;

                                lista.sort(function(a, b){
                                    var MesA = a[0]
                                    var MesB = b[0]
                                    if (MesA == MesB) return 0;
                                    return MesA > MesB ? 1 : -1;
                                });

                                $.each(lista, function (index, value) {
                                    MesAnoAtual = value[0].substring(0, 6);
                                    if ( UltimoMesAno == "" )  UltimoMesAno = MesAnoAtual;
                                    if ( UltimoMesAno != MesAnoAtual ){
                                        arTotal[iLen] = Total;
                                        iLen++;
                                        UltimoMesAno = MesAnoAtual;
                                        Total        = 0.00;
                                    }
                                    Total      += parseFloat( GetValorDecimal( value[5] ) );
                                    TotalGeral += parseFloat( GetValorDecimal( value[5] ) );
                                });

                                arTotal[iLen] = Total;
                                iLen          = 0;
                                UltimoMesAno  = "";
                                sDivMes       = "";

                                $('#DivConteudoProv').append( '<h6 class="text-dark text-center" style="border: 0px solid blue;">TOTAL A RECEBER R$ ' + fMascaraValor(TotalGeral) + ' </h6>' );

                                $.each(lista, function (index, value) {

                                    MesAnoAtual = value[0].substring(0, 6);

                                    if ( UltimoMesAno == "" ) {
                                        UltimoMesAno = MesAnoAtual;
                                        Total = arTotal[iLen];
                                        iLen++;
                                        sDivMes  = "";
                                        sDivMes += '<span style="font-size:13px;" class="text-success font-weight-bold"> MÊS ' + UltimoMesAno.substring(4,6)+ "/" + UltimoMesAno.substring(0,4) + ' - TOTAL R$ ' + fMascaraValor(Total) + '</span>';
                                        sDivMes += "<br/>";
                                        sDivMes += '<div class="table-responsive-sm">';
                                        sDivMes += '  <table style="font-size:12px;" id="ProvMes'+UltimoMesAno+'" class="table table-sm table-bo rdered table-hover table-condensed table-borderless nowrap" border="0" cellpadding="0" cellspacing="0">';
                                        // sDivMes += '    <col width="50">';
                                        // sDivMes += '    <col width="50">';
                                        // sDivMes += '    <col width="150">';
                                        // sDivMes += '    <col width="150">';
                                        // sDivMes += '    <col width="150">';
                                        sDivMes += '    <thead>';
                                        sDivMes += '      <tr class="thead-dark font-weight-bold text-center">';
                                        sDivMes += '      <th>Dt. Pagto</th>';
                                        sDivMes += '      <th>Ativo</th>';
                                        sDivMes += '      <th>Tipo</>';
                                        sDivMes += '      <th>Total a Receber</th>';
                                        sDivMes += '      <th>Situação</th>';
                                        sDivMes += '      </tr>';
                                        sDivMes += '    </thead>';
                                        sDivMes += '    <tbody>';
                                    }

                                    if ( UltimoMesAno != MesAnoAtual ){
                                        UltimoMesAno = MesAnoAtual;
                                        Total = arTotal[iLen];
                                        iLen++;

                                        sDivMes += '    </tbody>';
                                        // sDivMes += '    <tfoot>';
                                        // sDivMes += '      <tr>';
                                        // sDivMes += '        <th></th>';
                                        // sDivMes += '        <th></th>';
                                        // sDivMes += '        <th></th>';
                                        // sDivMes += '        <th></th>';
                                        // sDivMes += '        <th></th>';
                                        // sDivMes += '      </tr>';
                                        // sDivMes += '    </tfoot>';
                                        sDivMes += '  </table>';
                                        sDivMes += '</div>';
                                        $('#DivConteudoProv').append(sDivMes);

                                        sDivMes  = "";
                                        sDivMes += '<span style="font-size:13px;" class="text-success font-weight-bold"> MÊS ' + UltimoMesAno.substring(4,6)+ "/" + UltimoMesAno.substring(0,4) + ' - TOTAL R$ ' + fMascaraValor(Total) + '</span>';
                                        sDivMes += "<br/>";
                                        sDivMes += '<div class="table-responsive-sm">';
                                        sDivMes += '  <table style="font-size:12px;" id="ProvMes'+UltimoMesAno+'" class="table table-sm table-bord ered table-hover table-condensed table-borderless nowrap" border="0" cellpadding="0" cellspacing="0">';
                                        // sDivMes += '    <col width="50">';
                                        // sDivMes += '    <col width="50">';
                                        // sDivMes += '    <col width="150">';
                                        // sDivMes += '    <col width="150">';
                                        // sDivMes += '    <col width="150">';
                                        // sDivMes += '    <col width="150">';
                                        sDivMes += '    <thead>';
                                        sDivMes += '      <tr class="thead-dark font-weight-bold text-center">';
                                        sDivMes += '      <th>Dt. Pagto</th>';
                                        sDivMes += '      <th>Ativo</th>';
                                        sDivMes += '      <th>Tipo</>';
                                        sDivMes += '      <th>Total a Receber</th>';
                                        sDivMes += '      <th>Situação</th>';
                                        sDivMes += '      </tr>';
                                        sDivMes += '    </thead>';
                                        sDivMes += '    <tbody>';

                                    }

                                    sDivMes += fMontaDadosProvento( urlPadrao, value );

                                });

                                sDivMes += '    </tbody>';
                                // sDivMes += '    <tfoot>';
                                // sDivMes += '      <tr>';
                                // sDivMes += '        <th></th>';
                                // sDivMes += '        <th></th>';
                                // sDivMes += '        <th></th>';
                                // sDivMes += '        <th></th>';
                                // sDivMes += '        <th></th>';
                                // sDivMes += '      </tr>';
                                // sDivMes += '    </tfoot>';
                                sDivMes += '  </table>';
                                sDivMes += '</div>';
                                $('#DivConteudoProv').append( sDivMes );


                            }else{
                                $("#DivConteudoProv").html('<span style="font-size:14px;" class="font-italic text-muted">Nenhum provento a receber...</span><br/>');
                            }

                        console.timeEnd(logNome + ' - TEMPO')

                  } else {
                    fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
                    return false;
                  }
              },
              error: function(data) {
                  fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
                  return;
              }
            });


			// var end = new Date().getTime();
			// var time = end - start;
			// sec = Math.floor((time/1000) % 60);
			// console.log('fCarrgarDadosProventos - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
  
  } catch(e) {
    fLimparDadosInvestidores();
	fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}