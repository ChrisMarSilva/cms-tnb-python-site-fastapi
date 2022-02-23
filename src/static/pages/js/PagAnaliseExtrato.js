
function iniciarAnimacaoPesquisarAnaliseExtrat() {
	$("#iRefreshExtrat").addClass("fa-spin");
	$("#btnAnaliseExtratPesquisar").addClass("disabled");
}

function finalizarAnimacaoPesquisaAnaliseExtrat() {
	$("#iRefreshExtrat").removeClass("fa-spin");
	$("#btnAnaliseExtratPesquisar").removeClass("disabled");
}

function fLimparGridAnaliseExtrat( urlPadrao ){	
	fLimparAreaAlerta("AreaAlertaPrincAnaliseExtrato");	
	$("#txtFiltroAnaliseExtratDataIni").val(   fDataAnoPrimeira() );
	$("#txtFiltroAnaliseExtratDataFim").val(   fDataAnoUltima()   );
	$("#txtFiltroAnaliseExtratAtivo").val(     ""                 );	
	fDefinirPadraoSelect('txtFiltroAnaliseExtratAtivo');
}

async function fCarregarGridAnaliseExtrat( urlPadrao ){
	try {   

		 promise = new Promise( (resolve, reject) => {
	
			fLimparAreaAlerta("AreaAlertaPrincAnaliseExtrato");
			finalizarAnimacaoPesquisaAnaliseExtrat();
			iniciarAnimacaoPesquisarAnaliseExtrat();
	
			var DivAnaliseExtrato = $("#DivAnaliseExtrato");
			DivAnaliseExtrato.html("<br/>	<br/>	<br/>	<br/>	<br/>	<br/>	<br/>	<br/>	");
	
			var DataIni  = tirarFormacataoData($("#txtFiltroAnaliseExtratDataIni").val());
			var DataFim  = tirarFormacataoData($("#txtFiltroAnaliseExtratDataFim").val());
			var CodAtivo = $("#txtFiltroAnaliseExtratAtivo").val();
	
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url: urlPadrao + "Analise/extrato",
				data: { CodAtivo: CodAtivo, DataIni: DataIni, DataFim: DataFim },
				success: function(result) {
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
	
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						finalizarAnimacaoPesquisaAnaliseExtrat();
						fCriarAlerta("AreaAlertaPrincAnaliseExtrato", TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						finalizarAnimacaoPesquisaAnaliseExtrat();
						fCriarAlerta("AreaAlertaPrincAnaliseExtrato", TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridAnaliseExtrat( urlPadrao, lista );
					} else{
						finalizarAnimacaoPesquisaAnaliseExtrat();
						fCriarAlerta("AreaAlertaPrincAnaliseExtrato", TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					fCriarAlerta("AreaAlertaPrincAnaliseExtrato", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
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
		if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrincAnaliseExtrato", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);   
	}
}

async function fMontarGridAnaliseExtrat( urlPadrao, lista ){
	try {   

		 promise = new Promise( (resolve, reject) => {
	
			var DivAnaliseExtrato = $("#DivAnaliseExtrato");
			DivAnaliseExtrato.html("<br/>	<br/>	<br/>	<br/>	<br/>	<br/>	<br/>	<br/>	");
			
			var listaAno    = [];
			$.each(lista, function (index, value) {
	
				var LancData      = value[0];                                 // 0-Data
				var LancTipo      = value[1];                                 // 1-Tipo
				var LancAtivo     = value[2];                                 // 2-Ativo/Fundo
				var LancQuant     = value[3];                                 // 3-Quant
				var LancPreco     = parseFloat( GetValorDecimal(value[4]) );  // 4-Preco
				var LancDespesa   = parseFloat( GetValorDecimal(value[5]) );  // 5-Taxa Tot
				var LancTotal     = parseFloat( GetValorDecimal(value[6]) );  // 6-Total
				var LancTpInvest  = value[7];                                 // 7-TipoInvest

				if ( LancTpInvest == 'CRIPTO' ){
				    LancQuant = parseFloat( value[3] );  // 3-Quant
				    LancPreco = parseFloat(GetValorDecimalMaior( value[4] ));  // 4-Preco
                }

				var objLanc = { data: LancData, tipoInvest: LancTpInvest, tipo: LancTipo, ativo: LancAtivo, quant: LancQuant, preco: LancPreco, despesa: LancDespesa, total: LancTotal };
	
				var totalC = 0.00;
				var totalV = 0.00;
				if ( LancTipo == "Compra" || LancTipo == "Compra/Troca" ) totalC = LancTotal;
				if ( LancTipo == "Venda" || LancTipo == "Venda/Troca"  ) totalV = LancTotal;
				var objAtivo = { codigo: LancAtivo, totalC: totalC, totalV: totalV };
	
				var mesAtual = LancData.substring(4,6);
				var objMes   = { mes: mesAtual, lancamentos: [objLanc], ativos: [objAtivo] };
	
				var anoAtual = LancData.substring(0,4);
				var objAno   = { ano: anoAtual, meses: [objMes] };
	
				adicionarAno( listaAno, objAno, objMes, objLanc, objAtivo );    
	
			}); // $.each(lista, function (index, value) {
			
			montarCardAno( listaAno ) ;
	
			finalizarAnimacaoPesquisaAnaliseExtrat();
	
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
		finalizarAnimacaoPesquisaAnaliseExtrat();
		if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrincAnaliseExtrato", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);   
	}
}

// -----------------------------------------------------------------------------------------------------------------------
// -----------------------------------------------------------------------------------------------------------------------

function adicionarAno( listaAno, objAno, objMes, objLanc, objAtivo ){  
	if ( !existeAno(listaAno, objAno, objMes, objLanc, objAtivo) )  
		listaAno.push(objAno);
}

function existeAno(listaAno, objAno, objMes, objLanc, objAtivo) {
	return !!listaAno.filter(function (objLocal) {
		if ( objLocal.ano == objAno.ano ){
			adicionarMes( objLocal.meses, objMes, objLanc, objAtivo );
			return true;  
		}
	}).length;
}

function adicionarMes( listaMes, objMes, objLanc, objAtivo ){  
	if ( !existeMes(listaMes, objMes, objLanc, objAtivo) )  
		listaMes.push(objMes);
}

function existeMes(listaMes, objMes, objLanc, objAtivo) {
	return !!listaMes.filter(function (objLocal) {
		if ( objLocal.mes == objMes.mes ){ 
			adicionarLancamento( objLocal.lancamentos, objLanc );
			adicionarAtivo(      objLocal.ativos,     objAtivo );
			return true;  
		}
	}).length;
}

function adicionarLancamento( listaLanc, objLanc ){  
	listaLanc.push(objLanc);
}

function existeAtivo(listaAtivos, objAtivo) {
	return !!listaAtivos.filter(function (objLocal) {
		if ( objLocal.codigo == objAtivo.codigo ){ 
			objLocal.totalC += objAtivo.totalC;
			objLocal.totalV += objAtivo.totalV;
			return true;  
		}
	}).length;
}

function adicionarAtivo( listaAtivos, objAtivo ){  
	if ( !existeAtivo(listaAtivos, objAtivo) )  
		listaAtivos.push(objAtivo);
}

async function montarCardAno( listaAno ){
	
     promise = new Promise( (resolve, reject) => {

		var DivAnaliseExtrato = $("#DivAnaliseExtrato");
		
		if ( listaAno.length > 0 ){
			listaAno.reverse();
			var content  = "";
			content      += '<div id="Div Accordion">';
			$.each(listaAno, function (index, value) {  
				var anoAtual      = value.ano;
				var isPrimeiroAno = index === 0;
				var DivNmTitulo   = 'DivTitulo'+anoAtual;
				var DivNmConteudo = 'DivConteudo'+anoAtual;
				content += '<div class="card border-dark" style="margin-bottom: 10px; ">';
				content += '  <div class="card-header bg-dark" id="'+DivNmTitulo+'" style="padding: 0px; ">';
				content += '    <button class="btn btn-sm btn-link text-white '+(isPrimeiroAno ? '' : 'collapsed')+'" data-toggle="collapse" data-target="#'+DivNmConteudo+'" aria-expanded="'+(isPrimeiroAno ? 'true' : 'false')+'" aria-controls="'+DivNmConteudo+'">Ano: '+anoAtual+' </button>';
				content += '  </div>';
				content += '  <div id="'+DivNmConteudo+'" class="collapse '+(isPrimeiroAno ? 'show' : '')+'" aria-labelledby="'+DivNmTitulo+'" data-parent="#DivAccordion">';
				content += '    <div class="card-body" style="padding: 10px; " >';
				content += '    '+montarCardMes( anoAtual, isPrimeiroAno, value.meses );
				content += '    </div>';
				content += '  </div>';
				content += '</div>';
			});
			content += '</div>';
			DivAnaliseExtrato.html(content);
		} else{
			DivAnaliseExtrato.html("<br/>	<br/>	<br/>	<br/>	<br/>	<br/>	<br/>	<br/>	");
		}

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
    })
    .then( txt => {
        //console.log('Sucesso: ' + txt);
    })
    .catch( txt => {
        //fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    });
}

function buscarMes(listaMes, mesAtual) {
	return !!listaMes.filter(function (objLocal) {
		if ( objLocal.mes == mesAtual ){
		    return true;
		}
	}).length;
}

function montarCardMes( anoAtual, isPrimeiroAno, listaMes ){

	var content            = "";
	var isMesActiveOrig    = false;
	var arrMesNro          = ['01',      '02',        '03',    '04',    '05',   '06',    '07',    '08',     '09',       '10',      '11',       '12'      ];
	var arrMesNome         = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
	var arrMesNomeCurtoMin = ["Jan",     "Fev",       "Mar",   "Abr",   "Mai",  "Jun",   "Jul",   "Ago",    "Set",      "Out",     "Nov",      "Dez"     ];
	var arrMesNomeCurtoMai = ["JAN",     "FEV",       "MAR",   "ABR",   "MAI",  "JUN",   "JUL",   "AGO",    "SET",      "OUT",     "NOV",      "DEZ"     ];

	isMesActiveOrig = false;
	content += '<ul class="nav nav-tabs justify-content-center" id="NavTab'+anoAtual+'Header" role="tablist">';
	$.each(arrMesNro, function (index, value) {  
		var mesAtual        = value;
		var isPrimeiroMes   = index === 0;
		var isMesEncontrado = buscarMes(listaMes, mesAtual);
		var isMesActive     = (isMesActiveOrig===false) && ( (isPrimeiroMes===true && isMesEncontrado===true) || (isPrimeiroMes===false && isMesEncontrado===true) );
		if ( isMesActive ) isMesActiveOrig = true;
		content += 
			'<li class="nav-item"> '+
			'<a style="width: 80px;" '+
			'class="border border-dark text-center font-weight-bold nav-link '+( isMesActive ? 'active' : '')+' '+(isMesEncontrado ? '' : 'disabled font-line-through font-italic text-danger')+'" '+
			(isMesEncontrado ? '' : ' style="pointer-events: none; cursor: default; " tabindex="-1" aria-disabled="true" ')+' '+
			'id="Nav'+anoAtual+arrMesNomeCurtoMin[index]+'Tab" '+
			'data-toggle="tab" '+
			'href="#Nav'+anoAtual+arrMesNomeCurtoMin[index]+'" '+
			'aria-controls="Nav'+anoAtual+arrMesNomeCurtoMin[index]+'" '+
			'aria-selected="'+( isMesActive ? 'true' : 'false')+'" >'+
			arrMesNomeCurtoMai[index]+
			'</a>'+
			'</li>';
	});
	content += '</ul>';

	isMesActiveOrig = false;
	content += '<div class="tab-content" id="NavTab'+anoAtual+'Content">';
	$.each(arrMesNro, function (index, value) {  
		var mesAtual        = value;
		var isPrimeiroMes   = index === 0;
		var isMesEncontrado = buscarMes(listaMes, mesAtual);
		var isMesActive     = (isMesActiveOrig===false) && ( (isPrimeiroMes===true && isMesEncontrado===true) || (isPrimeiroMes===false && isMesEncontrado===true) );
		if ( isMesActive ) isMesActiveOrig = true;
		content += '<div class="tab-pane fade '+( isMesActive ? 'show active' : '')+'" id="Nav'+anoAtual+arrMesNomeCurtoMin[index]+'" role="tabpanel" aria-labelledby="Nav'+anoAtual+arrMesNomeCurtoMin[index]+'Tab">';
		if ( isMesEncontrado )
		listaMes.filter(function (objLocal) {
			if ( objLocal.mes == mesAtual ){
				//content += montarCardCarteiraMes( objLocal.ativos      );
				content += montarCardResumoMes(   objLocal.ativos      );
				content += montarCardLancMes(     objLocal.lancamentos );
			}
		});//listaMes.filter(function (objLocal) {
		content += '</div>';
	});
	content += '</div>';
	return content;
}

function montarCardCarteiraMes( listaAtivo ){
	var content = '';
	content = '';
	content += '<br>';
	content += '<h6 class="font-weight-bold">PORTFÓLIO ATUAL</h6>';
	content += '<div class="table-responsive">';	
	content += '<table class="table table-sm table-hover table-condensed nowrap" border="0" cellspacing="0" width="100%" style="font-size: 12px; margin: 0px;">';
	content += '  <thead>';
	content += '    <tr class="thead-dark font-weight-bold"> ';
	content += '      <th>Tipo</th>';
	content += '      <th>Ativo</th>';
	content += '      <th>Quant.</th>';
	content += '      <th>Preço Médio</th>';
	content += '      <th>Tot. Invest.</th>';
	content += '      <th>% Portfólio</th>';
	content += '      <th></th>';
	content += '      <th>Quant. Compra/Bônus</th>';
	content += '      <th>Quant. Venda</th>';
	content += '      <th>Tot. Compra</th>';
	content += '      <th>Tot. Venda</th>';
	content += '      <th>Saldo Mês</th>';
	content += '    </tr>'; 
	content += '  </thead>';
	content += '  <tbody>';
	$.each(listaAtivo, function (index, value) {
		// var LancId        = value.id;
		// var LancData      = value.data;
		// var LancTipo      = value.tipo;
		// var LancAtivo     = value.ativo;
		// var LancQuant     = value.quant;
		// var LancPreco     = value.preco;
		// var LancDespesa   = value.despesa;
		// var LancTotal     = value.total;
		// content += '    <tr class="text-center"> ';
		// content += '      <td>'+colcarFormacataoData(LancData)+'</td>';
		// content += '      <td>'+LancTipo+'</td>';
		// content += '      <td>'+LancAtivo+'</td>';
		// content += '      <td>'+colcarFormacataoInteiro(LancQuant)+'</td>';
		// content += '      <td>R$ '+fMascaraValor(LancPreco)+'</td>';
		// content += '      <td>R$ '+fMascaraValor(LancDespesa)+'</td>';
		// content += '      <td>R$ '+fMascaraValor(LancTotal)+'</td>'; 
		// content += '    </tr>'; 
	});
	content += '  </tbody>';
	content += '  <tfoot>';
	content += '  </tfoot>';
	content += '</table>';
	content += '</div>';
	//content += '<br>';
	return content;
}

function montarCardResumoMes( listaAtivo ){
	var content = '';
	content = '';
	content += '<br>';
	content += '<h6 class="font-weight-bold">RESUMO</h6>';
	content += '<div class="table-responsive">';	
	content += '<table class="table table-sm table-hover table-condensed nowrap" border="0" cellspacing="0" width="100%" style="font-size: 12px; margin: 0px;">';
	content += '  <thead>';
	content += '    <tr class="thead-dark font-weight-bold"> ';
	content += '      <th>Ativo</th>';
	content += '      <th>Total Compra</th>';
	content += '      <th>Total Venda</th>';
	content += '      <th>Saldo</th>';
	content += '    </tr>'; 
	content += '  </thead>';
	content += '  <tbody>';	
	listaAtivo.sort(function(a, b){
		var AtivoA =  a.codigo; 
		var AtivoB =  b.codigo; 
		if(AtivoA== AtivoB) return 0;
		return AtivoA> AtivoB? 1: -1;
	});
	var totCompra = 0.00;
	var totVenda  = 0.00;
	$.each(listaAtivo, function (index, value) {
		var ativo  = value.codigo;
		var totalC = value.totalC;
		var totalV = value.totalV;
		if ( totalC > 0.00 || totalV > 0.00 ){
			content += '    <tr class="text-center"> ';
			content += '      <td class="text-dark font-weight-bold">'+ativo+'</td>';
			content += '      <td>R$ '+fMascaraValor(totalC)+'</td>';
			content += '      <td>R$ '+fMascaraValor(totalV)+'</td>';
			content += '      <td class="text-dark font-weight-bold">R$ '+fMascaraValor( totalC - totalV )+'</td>'; 
			content += '    </tr>'; 
		}
		totCompra += totalC;
		totVenda  += totalV;
	});
	content += '  </tbody>';
	content += '  <tfoot>';
	content += '    <tr class="bg-light text-dark font-weight-bold" style="font-size: 13px;"> ';
	content += '      <td>TOTAL</td>';
	content += '      <td>R$ '+fMascaraValor(totCompra)+'</td>';
	content += '      <td>R$ '+fMascaraValor(totVenda)+'</td>';
	content += '      <td>R$ '+fMascaraValor( totCompra - totVenda )+'</td>'; 
	content += '    </tr>'; 
	content += '  </tfoot>';
	content += '</table>';
	content += '</div>';
	//content += '<br>';
	return content;
}

function montarCardLancMes( listaLanc ){
	var content = '';
	content = '';
	content += '<br>';
	content += '<h6 class="font-weight-bold">LANÇAMENTOS</h6>';
	content += '<div class="table-responsive">';	
	content += '<table class="table table-sm table-hover table-condensed nowrap" border="0" cellspacing="0" width="100%" style="font-size: 12px; margin: 0px;">';
	content += '  <thead>';
	content += '    <tr class="thead-dark font-weight-bold"> ';
	content += '      <th>Data</th>';
	content += '      <th>Categoria</th>';
	content += '      <th>Tipo</th>';
	content += '      <th>Ativo</th>';
	content += '      <th>Quant.</th>';
	content += '      <th>Preço</th>';
	content += '      <th>Despesas</th>';
	content += '      <th>Total</th>';
	content += '    </tr>'; 
	content += '  </thead>';
	content += '  <tbody>';	
	listaLanc.sort(function(a, b){
		var DataA =  a.data; 
		var DataB =  b.data; 
		if(DataA== DataB) return 0;
		return DataA> DataB? 1: -1;
	});
	$.each(listaLanc, function (index, value) {
		var LancData      = value.data;
		var LancTpInvest  = value.tipoInvest == "ACAO" ? 'AÇÃO' : value.tipoInvest;
		var LancTipo      = value.tipo;
		var LancAtivo     = value.ativo;
		var LancQuant     = value.quant;
		var LancPreco     = value.preco;
		var LancDespesa   = value.despesa;
		var LancTotal     = value.total;
		content += '    <tr class="text-center"> ';
		content += '      <td class="text-dark font-weight-bold">'+colcarFormacataoData(LancData)+'</td>';
		content += '      <td>'+LancTpInvest+'</td>';
		content += '      <td>'+LancTipo+'</td>';
		content += '      <td class="text-dark font-weight-bold">'+LancAtivo+'</td>';
		if ( LancTpInvest == 'CRIPTO' ){
		    content += '      <td>'+fMascaraValorSemLimite(LancQuant)+'</td>';
		    content += '      <td>R$ '+fMascaraValorSemLimite(LancPreco)+'</td>';
        } else {
		    content += '      <td>'+colcarFormacataoInteiro(LancQuant)+'</td>';
		    content += '      <td>R$ '+fMascaraValor(LancPreco)+'</td>';
        }
		content += '      <td>R$ '+fMascaraValor(LancDespesa)+'</td>';
		content += '      <td class="text-dark font-weight-bold">R$ '+fMascaraValor(LancTotal)+'</td>'; 
		content += '    </tr>'; 
	});
	content += '  </tbody>';
	content += '  <tfoot>';
	content += '  </tfoot>';
	content += '</table>';
	content += '</div>';
	content += '<br>';
	return content;
}
