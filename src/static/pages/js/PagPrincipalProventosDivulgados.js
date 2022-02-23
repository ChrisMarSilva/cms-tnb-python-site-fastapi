
async function fCarrgarDadosCalendario( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

            let logNome = '@TamoNaBolsa - PagPrincipalCalendario'

            // console.log(logNome + ' - INI - ', moment().format())
            console.time(logNome + ' - TEMPO')

            $.ajax({
              cache   : "false",
              dataType: "json",
              async   : true,
              type    : "POST",
              url     : urlPadrao + "principal/carregarCalendario",
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

                        var sDivConteudo = "";

                        if ( lista.length > 0 ){

                            sDivConteudo += '<div class="table-responsive-sm">';
                            sDivConteudo += '  <table id="GridCalProv" style="font-size: 11px; widt:100%" class="table table-sm table-b ordered table-hover table-condensed table-borderless nowrap" cellpadding="0" cellspacing="0">';
                            sDivConteudo += '    <thead>';
                            sDivConteudo += '      <tr class="thead-dark font-weight-bold text-center">';
                            sDivConteudo += '        <th>Dt. Ex</th>';
                            sDivConteudo += '        <th>Dt. Pagto</th>';
                            sDivConteudo += '        <th>Ativo</th>';
                            sDivConteudo += '        <th>Tipo</th>';
                            sDivConteudo += '        <th>Preço/Quant.</th>';
                            sDivConteudo += '        <th>Ação</th>';
                            sDivConteudo += '      </tr>';
                            sDivConteudo += '    </thead>';
                            sDivConteudo += '    <tbody>';

                            $.each(lista, function (index, value) {

                                var CalId       = value[0]; // 0-CalendarioId
                                var ProvCodigo  = value[1]; // 1-AtivoCodigo
                                var ProvTipo    = value[2]; // 2-ProventoTipo
                                var ProvDtEx    = value[3]; // 3-ProventoDtEx
                                var ProvDtPagto = value[4]; // 4-ProventoDtPagto
                                var ProvValor   = value[5]; // 5-ProventoValor
                                var TipoInvest  = value[6]; // 6-TipoInvest

                                if ( ProvTipo == 'D' || ProvTipo == 'J' || ProvTipo == 'R' || ProvTipo == 'B' || ProvTipo == 'E' || ProvTipo == 'G' || ProvTipo == 'FR' ){

                                    var ProvTipoDescr = "";
                                    if ( ProvTipo == 'D' ) ProvTipoDescr = 'DIVIDENDO';
                                    if ( ProvTipo == 'J' ) ProvTipoDescr = 'JRS CAP PRÓPRIO';
                                    if ( ProvTipo == 'B' ) ProvTipoDescr = 'BONIFICAÇÃO';
                                    if ( ProvTipo == 'E' ) ProvTipoDescr = 'DESDOBRAMENTO';
                                    if ( ProvTipo == 'G' ) ProvTipoDescr = 'GRUPAMENTO';
                                    if ( ProvTipo == 'R' ) ProvTipoDescr = 'REST CAP DIN';
                                    if ( ProvTipo == 'FR') ProvTipoDescr = 'REDIMENTO';

                                    if ( ProvTipo == 'D' || ProvTipo == 'J' || ProvTipo == 'R' || ProvTipo == 'FR' ){
                                        sDivConteudo += '      <tr id="TrProvDivulg-'+ProvTipo+'-'+ProvCodigo+'-'+CalId+'">';
                                        sDivConteudo += '        <td>'+colcarFormacataoData(ProvDtEx)+'</td>';
                                        sDivConteudo += '        <td>'+colcarFormacataoData(ProvDtPagto)+'</td>';
                                        sDivConteudo += '        <td class="font-weight-bold">'+ProvCodigo+'</td>';
                                        sDivConteudo += '        <td class="fon t-weight-bold">'+ProvTipoDescr+'</td>';
                                        sDivConteudo += '        <td  class="text-left font-weight-bold">'+ProvValor.replace('.', ',')+'</td>';
                                        sDivConteudo += '        <td>';
                                        sDivConteudo += '            <a class="text-success" style="float: center; font-size:10px;" title="Adicionar Provento" href="javascript:void(0)" onclick="fAbrirModalDetalheRendCalend( \''+urlPadrao+'\', \''+ProvTipo+'\', \''+ProvCodigo+'\', \''+ProvDtEx+'\', \''+ProvDtPagto+'\', \''+ProvValor.replace('.', ',')+'\', \''+TipoInvest+'\' );">';
                                        sDivConteudo += '              <i class="fa fa-plus-circle fa-2x" aria-hidden="true"></i>';
                                        sDivConteudo += '            </a>'
                                        sDivConteudo += '            &nbsp;';
                                        sDivConteudo += '            <a class="text-danger" style="float: center; font-size:10px;" title="Remover Provento" href="javascript:void(0)" onclick="fRemoverProventDivulg( \''+urlPadrao+'\', \''+CalId+'\', \''+ProvCodigo+'\', \''+ProvTipo+'\', \''+ProvDtEx+'\' );">';
                                        sDivConteudo += '              <i class="fa fa-minus-square-o fa-2x" aria-hidden="true"></i>';
                                        sDivConteudo += '            </a>';
                                        sDivConteudo += "        </td>";
                                        sDivConteudo += '      </tr>';
                                    }

                                    if ( ProvTipo == 'B' || ProvTipo == 'E' || ProvTipo == 'G' ){

                                        var OperTipo = "";
                                        if ( ProvTipo == 'B') OperTipo = 'B';
                                        if ( ProvTipo == 'E') OperTipo = 'D';
                                        if ( ProvTipo == 'G') OperTipo = 'G';

                                        var OperQtde = 100;
                                        if ( ProvTipo == 'E') OperQtde = Math.round( ( ProvValor / 100) + 1 ); // Math.round( (1 / ProvValor) * 100 ); //Desdobro
                                        if ( ProvTipo == 'G') OperQtde = Math.round( ( 100 / ProvValor ) * 1 ); // Math.round(1 / ProvValor ); //Grupar

                                        var OperQtdeDescr = "";
                                        if ( ProvTipo == 'E') OperQtdeDescr = '1 para '+OperQtde;//Desdobro
                                        if ( ProvTipo == 'G') OperQtdeDescr = OperQtde+' para 1';//Grupar
                                        if ( ProvTipo == 'B') OperQtdeDescr = ProvValor.replace('.', ',')+'%';//Grupar

                                        var OperPreco= "";
                                        if ( ProvTipo == 'B') OperPreco = ProvValor.replace('.', ',');

                                        var OperData= "";
                                        if ( ProvTipo == 'E') OperData = ProvDtEx;
                                        if ( ProvTipo == 'G') OperData = ProvDtEx;
                                        if ( ProvTipo == 'B') OperData = ProvDtEx;

                                        sDivConteudo += '      <tr id="TrProvDivulg-'+ProvTipo+'-'+ProvCodigo+'-'+CalId+'">';
                                        sDivConteudo += '        <td>'+colcarFormacataoData(ProvDtEx)+'</td>';
                                        sDivConteudo += '        <td>'+colcarFormacataoData(ProvDtPagto)+'</td>';
                                        sDivConteudo += '        <td class="font-weight-bold">'+ProvCodigo+'</td>';
                                        sDivConteudo += '        <td class="font-weight-bold">'+ProvTipoDescr+'</td>';
                                        sDivConteudo += '        <td class="text-left font-weight-bold">'+OperQtdeDescr+'</td>';
                                        sDivConteudo += '        <td>';
                                        sDivConteudo += '            <a class="text-success" style="float: center; font-size:10px;" title="Adicionar Operação" href="javascript:void(0)" onclick="fAbrirModalDetalheOper( \''+urlPadrao+'\', \'\', \'Novo\', \''+OperTipo+'\', \''+ProvCodigo+'\', \''+OperQtde+'\', \''+OperPreco+'\' , \''+OperData+'\' );">';
                                        sDivConteudo += '              <i class="fa fa-plus-circle fa-2x" aria-hidden="true"></i>';
                                        sDivConteudo += '            </a>';
                                        sDivConteudo += '            &nbsp;';
                                        sDivConteudo += '            <a class="text-danger" style="float: center; font-size:10px;" title="Remover Operação" href="javascript:void(0)" onclick="fRemoverProventDivulg( \''+urlPadrao+'\', \''+CalId+'\', \''+ProvCodigo+'\', \''+ProvTipo+'\', \''+ProvDtEx+'\' );">';
                                        sDivConteudo += '              <i class="fa fa-minus-square-o fa-2x" aria-hidden="true"></i>';
                                        sDivConteudo += '            </a>';
                                        sDivConteudo += "        </td>";
                                        sDivConteudo += '      </tr>';
                                    }

                                }

                            });

                            sDivConteudo += '    </tbody>';
                            sDivConteudo += '    <tfoot>';
                            sDivConteudo += '    </tfoot>';
                            sDivConteudo += '  </table>';
                            sDivConteudo += '</div>';

                        }else{
                            sDivConteudo = '<span style="font-size:14px;" class="font-italic text-muted">Nenhum provento divulgado...</span><br/>';
                        }

                        $("#DivConteudoCalendarioProv").html( sDivConteudo );

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
	  fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

async function fRemoverProventDivulg( urlPadrao, IdEmprProv, CodAtivo, Tipo, DataEx ){
	try {	

		 promise = new Promise( (resolve, reject) => {

			var tr = $('#TrProvDivulg-'+Tipo+'-'+CodAtivo+'-'+IdEmprProv).closest('tr');	
			tr.fadeOut(300, function() { 
				tr.remove(); 
				if ( $('#GridCalProv tr').length <= 1 )  
					$("#DivConteudoCalendarioProv").html( '<span style="font-size:14px;" class="font-italic text-muted">Nenhum provento divulgado...</span><br/>' ); 
			}); 

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "principal/removerProvDivulgado",
				data    : { IdEmprProv: IdEmprProv, CodAtivo: CodAtivo, Tipo: Tipo, DataEx: DataEx },
				success: function(result) {  
				
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 

					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, mensagem); 
						return false;
					} else if (resultado == "FALHA") {
						fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem); 
						return false;
					} else if (resultado == "OK") {	
						// fCarrgarDadosCalendario( urlPadrao );
						return true;
					} else {
						fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem); 
						return false;
					}
					
				},
				error: function(data) {
					fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
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
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});	
	
	} catch(e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}