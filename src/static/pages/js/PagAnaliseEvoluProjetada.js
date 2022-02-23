
var arNomeMeses = ["", "JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL","AGO", "SET", "OUT", "NOV", "DEZ"];
var WidthCampo01 =  1; // Nro
var WidthCampo02 =  1; // Ano
var WidthCampo03 =  1; // Mês
var WidthCampo04 = 30; // Invest
var WidthCampo05 = 40; // Invest Ano
var WidthCampo06 = 40; // Invest Geral
var WidthCampo07 =  1; // Mês Ini
var WidthCampo08 = 40; // Mês Fim
var WidthCampo09 = 30; // Lucro Mês
var WidthCampo10 =  1; // % Mês
var WidthCampo11 = 30; // Lucro Ano
var WidthCampo12 =  1; // % Ano
var WidthCampo13 = 30; // Lucro Geral
var WidthCampo14 =  1; // % Geral
var WidthCampo15 =  1; // Tipo
var WidthCampo16 =  1; // Ação

async function fLimparDadosModalProjecao( ) {

     promise = new Promise( (resolve, reject) => {

		fLimparAreaAlerta("AreaAlertaPrincAnaliseEvoluProjetada");	
		fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetada");	
		fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc");
	
		$("#txtAnaliseEvoluProjetDescricao").val(    "Projeção Criada em " + new Date().toLocaleDateString("pt-BR") );
		$("#txtAnaliseEvoluProjetAnoInicial").val(   new Date().getFullYear()  );
		$("#txtAnaliseEvoluProjetMesInicial").val(   new Date().getMonth() + 1 );
		$("#txtAnaliseEvoluProjetTotInicial").val(   "10.000,0"                );
		$("#txtAnaliseEvoluProjetInvestMensal").val( "1.000,00"                );
		$("#txtAnaliseEvoluProjetRendMensal").val(   "1,00"                    );
		$("#txtAnaliseEvoluProjetQtdeMeses").val(    "120"                     );
	
		fDefinirPadraoSelect('txtAnaliseEvoluProjetMesInicial');

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

function fAbrirDadosModalProjecao( urlPadrao ) {
	fLimparDadosModalProjecao();
	$('#PopModalDetalheEvolucaoProjecao').modal({backdrop: 'static'})  ;
	$(document).on('shown.bs.modal', function (e) { $("#txtAnaliseEvoluProjetDescricao").focus(); });
}

function fValidarDadosProjecao() {	
	try {
		
		fLimparAreaAlerta("AreaAlertaPrincAnaliseEvoluProjetada");	
		fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetada");	
		fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc");

		var Descricao    = $("#txtAnaliseEvoluProjetDescricao").val(); 
		var AnoInicial   = parseInt(   GetValorInteiro( $("#txtAnaliseEvoluProjetAnoInicial").val()   ) ); 
		var MesInicial   = parseInt(   GetValorInteiro( $("#txtAnaliseEvoluProjetMesInicial").val()   ) );  
		var TotInicial   = parseFloat( GetValorDecimal( $("#txtAnaliseEvoluProjetTotInicial").val()   ) );  
		var InvestMensal = parseFloat( GetValorDecimal( $("#txtAnaliseEvoluProjetInvestMensal").val() ) );  
		var RendMensal   = parseFloat( GetValorDecimal( $("#txtAnaliseEvoluProjetRendMensal").val()   ) );  
		var QtdeMeses    = parseInt(   GetValorInteiro( $("#txtAnaliseEvoluProjetQtdeMeses").val()    ) );  
		
		var ListaErros = "";
		if( Descricao  == ""                           ) ListaErros = ListaErros + " - Ano Descrição<br/>";
		if( AnoInicial <= 0                            ) ListaErros = ListaErros + " - Ano Início<br/>";
		if( MesInicial <= 0                            ) ListaErros = ListaErros + " - Mês Início<br/>";
		if( TotInicial <= 0.00 && InvestMensal <= 0.00 ) ListaErros = ListaErros + " - Valor Inicial ou Mensal<br/>";
		if( QtdeMeses  <= 0                            ) ListaErros = ListaErros + " - Qtd. Meses<br/>";
  
		if( ListaErros != "" ){
			fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetada", TP_ALERTA_AVISO, "Os seguintes campos não estão preenchido: <br/>"+ListaErros); 
			return false;
		}	
		
		return true;
	
	} catch (e) {
		fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetada", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return false;
	} 
}

function iniciarAnimacaoCriarAnaliseProjecao() {
    $("#iSalvarProjecao").removeClass("fa-check-square-o");
    $("#iSalvarProjecao").addClass("fa-spinner");
	$("#iSalvarProjecao").addClass("fa-pulse");
	$("#BtnModalDetalheProjecaoSalvar").addClass("disabled");
}

function finalizarAnimacaoCriarAnaliseProjecao() {
    $("#iSalvarProjecao").addClass("fa-check-square-o");
    $("#iSalvarProjecao").removeClass("fa-spinner");
	$("#iSalvarProjecao").removeClass("fa-pulse");
	$("#BtnModalDetalheProjecaoSalvar").removeClass("disabled");
}

async function fSalvarDadosProjecao( urlPadrao ){
	try {
		
		 promise = new Promise( (resolve, reject) => {

			if ( !fValidarDadosProjecao() ) return false;

			finalizarAnimacaoCriarAnaliseProjecao();
			iniciarAnimacaoCriarAnaliseProjecao();

			var Descricao    = $("#txtAnaliseEvoluProjetDescricao").val(); 
			var AnoInicial   = parseInt(   GetValorInteiro( $("#txtAnaliseEvoluProjetAnoInicial").val()   ) ); 
			var MesInicial   = parseInt(   GetValorInteiro( $("#txtAnaliseEvoluProjetMesInicial").val()   ) );  
			var TotInicial   = parseFloat( GetValorDecimal( $("#txtAnaliseEvoluProjetTotInicial").val()   ) ); 
			var InvestMensal = parseFloat( GetValorDecimal( $("#txtAnaliseEvoluProjetInvestMensal").val() ) ); 
			var RendMensal   = parseFloat( GetValorDecimal( $("#txtAnaliseEvoluProjetRendMensal").val()   ) ); 
			var QtdeMeses    = parseInt(   GetValorInteiro( $("#txtAnaliseEvoluProjetQtdeMeses").val()    ) );  
			
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "Analise/salvarProjecao",
				data    : { Descricao: Descricao, AnoInicio: AnoInicial, MesInicio: MesInicial, QtdMeses: QtdeMeses, VlrInvestInicio: TotInicial, VlrInvestMensal: InvestMensal, TxRendMensal: RendMensal },
				success: function(result) {  
				
					finalizarAnimacaoCriarAnaliseProjecao();
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var CartProj  = result.data.Dados;

					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetada", TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetada", TP_ALERTA_ERRO, mensagem); 
						return;
					} else if (resultado == "OK") {
						$("#PopModalDetalheEvolucaoProjecao").modal("hide");
						buscar_todos_nomes_projecoes(urlPadrao, 'txtFiltroProjecaoDescricao', false, false, true);
						BuscarDadosProjecao( urlPadrao, CartProj.Id );
						//fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					} else {
						fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetada", TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
					finalizarAnimacaoCriarAnaliseProjecao();
					fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetada", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);  // request.responseText //MSG_ALERTA_ERRO
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
			$("#PopModalGraficoEvolucaoProjecao").modal("hide");
			fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada",  TP_ALERTA_ERRO, 'Erro ao Montar Tabela da Projeção - ' + txt + ' - ' + MSG_ALERTA_ERRO); 
		});
	
	} catch (e) {
		finalizarAnimacaoCriarAnaliseProjecao();
		fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetada", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

async function BuscarDadosProjecao( urlPadrao, IdProjecao = "" ){
	try { 
		
		 promise = new Promise( (resolve, reject) => {

			$('#DivEvolucaoProjetada').html("");
			fLimparAreaAlerta("AreaAlertaPrincAnaliseEvoluProjetada");	
			fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetada");	
			fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc");
			
			$("#BtnProjecaoSalvar").addClass("disabled");
			//$("#BtnProjecaoResetar").addClass("disabled");
			$("#BtnProjecaoExcluir").addClass("disabled");
			
			$("#BtnProjecaoSalvar").hide();
			//$("#BtnProjecaoResetar").hide();
			$("#BtnProjecaoExcluir").hide();

			if ( IdProjecao == "" ) IdProjecao = $('#txtFiltroProjecaoDescricao').val();
			if ( IdProjecao == "" ) return;
			
			$('#txtFiltroProjecaoDescricao').val( IdProjecao );
			fDefinirPadraoSelect('txtFiltroProjecaoDescricao');
			
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "Analise/carregarProjecao",
				data    : { IdProjecao: IdProjecao },
				success: function(result) {  
								
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;

					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_ERRO, mensagem); 
						return;
					} else if (resultado == "OK") {

						MontarTabelaProjetada( urlPadrao, lista );

						$('#txtFiltroProjecaoDescricao').val( IdProjecao );
						fDefinirPadraoSelect('txtFiltroProjecaoDescricao');
						
						$("#BtnProjecaoSalvar").removeClass("disabled");
						//$("#BtnProjecaoResetar").removeClass("disabled");
						$("#BtnProjecaoExcluir").removeClass("disabled");
									
						$("#BtnProjecaoSalvar").show();
						//$("#BtnProjecaoResetar").show();
						$("#BtnProjecaoExcluir").show();
					
					} else {
						fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
					finalizarAnimacaoCriarAnaliseProjecao();
					fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);  // request.responseText //MSG_ALERTA_ERRO
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
			$("#PopModalGraficoEvolucaoProjecao").modal("hide");
			fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada",  TP_ALERTA_ERRO, 'Erro ao Montar Tabela da Projeção - ' + txt + ' - ' + MSG_ALERTA_ERRO); 
		});

	} catch (e) {
		if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

function GetTableButton( urlPadrao, fVlrInvestIni ){
	var conteudoHtml = "";	
	conteudoHtml += '<br/>';
	conteudoHtml += '<!-- Div Row clearfix -->';
	conteudoHtml += '<div class="row clearfix">';
	conteudoHtml += '  <div class="col-xl-2 col-lg-1 col-md-6 col-sm-12 form-control-label text-right" style="border: 0px solid blue;">';
	conteudoHtml += '    <label for="TxtGridEvoluProjVlrInvestIni" style="font-size:14px;" class="font-weight-bold">Vlr. Inicial:</label>';
	conteudoHtml += '  </div>';
	conteudoHtml += '  <div class="col-xl-2 col-lg-2 col-md-6 col-sm-12" style="border: 0px solid red;">';
	conteudoHtml += '      <input required type="text" id="TxtGridEvoluProjVlrInvestIni" value="'+ ( fVlrInvestIni != 0.00 ? fMascaraValor(fVlrInvestIni) : '' ) +'" class="form-control text-right" style="font-size:16px; height:30px;" onkeyup="javascript:validaKey(this, FMT_DECIMAL,2); ReCalcularTabelaProjetada();"  XXXonkeypress="ReCalcularTabelaProjetada();" XXXonchange="ReCalcularTabelaProjetada();" onfocus="javascript:desformataCampo(this, FMT_DECIMAL,2)" onblur="javascript:formataCampo(this, FMT_DECIMAL,2)">';
	conteudoHtml += '  </div>';
	// conteudoHtml += '  <div class="col-xl-8 col-lg-2 col-md-6 col-sm-12 text-right" style="border: 0px solid blue;">';
	// conteudoHtml += '    <a onclick="fAbrirModalAddMaisProjecao(\''+urlPadrao+'\');" style="width: 230px;" class="btn btn-info btn-round btn-simple font-weight-bold" id="BtnProjecaoAddMes" name="BtnProjecaoAddMes" href="javascript:void(0);" role="button" aria-pressed="true"> <i class="fa fa-plus-square" aria-hidden="true"></i> &nbsp; Adicionar Mais Projeção </a> ';
	// conteudoHtml += '  </div>';
	conteudoHtml += '</div>';
	conteudoHtml += '<!-- Div Row clearfix -->';
	conteudoHtml += '<br/>';
	return conteudoHtml;
}

function GetTableHead( urlPadrao ){
	var conteudoHtml = "";	
	conteudoHtml    += '<!-- Div table-responsive -->';
	conteudoHtml    += '<div class="table-responsive" id="AreaGrid">';
	conteudoHtml    += '  <table border="0" id="GridAnaliseEvoluProj" style="font-size: 12px; " class="table table-sm table-hover table-condensed nowrap" cellspacing="0" width="100%">';
	conteudoHtml    += '      <col width="'+WidthCampo01+'">'; // Nro
	conteudoHtml    += '      <col width="'+WidthCampo02+'">'; // Ano
	conteudoHtml    += '      <col width="'+WidthCampo03+'">'; // Mês
	conteudoHtml    += '      <col width="'+WidthCampo04+'">'; // Invest
	conteudoHtml    += '      <col width="'+WidthCampo05+'">'; // Invest Ano
	conteudoHtml    += '      <col width="'+WidthCampo06+'">'; // Invest Geral
	conteudoHtml    += '      <col width="'+WidthCampo07+'">'; // Mês Ini
	conteudoHtml    += '      <col width="'+WidthCampo08+'">'; // Mês Fim
	conteudoHtml    += '      <col width="'+WidthCampo09+'">'; // Lucro Mês
	conteudoHtml    += '      <col width="'+WidthCampo10+'">'; // % Mês
	conteudoHtml    += '      <col width="'+WidthCampo11+'">'; // Lucro Ano
	conteudoHtml    += '      <col width="'+WidthCampo12+'">'; // % Ano
	conteudoHtml    += '      <col width="'+WidthCampo13+'">'; // Lucro Geral
	conteudoHtml    += '      <col width="'+WidthCampo14+'">'; // % Geral
	conteudoHtml    += '      <col width="'+WidthCampo15+'">'; // Tipo
	conteudoHtml    += '      <col width="'+WidthCampo16+'">'; // Ação
	conteudoHtml    += '    <thead>';
	conteudoHtml    += '      <tr class="thead-dark font-weight-bold">'; //  thead-dark // xl-blue
	conteudoHtml    += '        <th width="'+WidthCampo01+'" style="width: '+WidthCampo01+'px; display: none;"> Nro </td>'; 
	conteudoHtml    += '        <th width="'+WidthCampo02+'" style="width: '+WidthCampo02+'px;"> Ano </td>';
	conteudoHtml    += '        <th width="'+WidthCampo03+'" style="width: '+WidthCampo03+'px;"> Mês </th>';
	conteudoHtml    += '        <th width="'+WidthCampo04+'" style="width: '+WidthCampo04+'px;"> Vlr. Mensal </th>';
	conteudoHtml    += '        <th width="'+WidthCampo05+'" style="width: '+WidthCampo05+'px;"> Tot. Invest. Ano </th>';
	conteudoHtml    += '        <th width="'+WidthCampo06+'" style="width: '+WidthCampo06+'px;"> Tot. Invest. </th>';
	conteudoHtml    += '        <th width="'+WidthCampo07+'" style="width: '+WidthCampo07+'px; display: none;"> Mês Ini </th>'; //Mês Ini
	conteudoHtml    += '        <th width="'+WidthCampo08+'" style="width: '+WidthCampo08+'px;"> Tot. Atual </th>'; // Mês Fim
	conteudoHtml    += '        <th width="'+WidthCampo09+'" style="width: '+WidthCampo09+'px;"> Lucro Mensal </th>';
	conteudoHtml    += '        <th width="'+WidthCampo10+'" style="width: '+WidthCampo10+'px;"> % </th>';
	conteudoHtml    += '        <th width="'+WidthCampo11+'" style="width: '+WidthCampo11+'px;"> Lucro Anual </th>';
	conteudoHtml    += '        <th width="'+WidthCampo12+'" style="width: '+WidthCampo12+'px;"> % </th>';
	conteudoHtml    += '        <th width="'+WidthCampo13+'" style="width: '+WidthCampo13+'px;"> Lucro Geral </th>';
	conteudoHtml    += '        <th width="'+WidthCampo14+'" style="width: '+WidthCampo14+'px;"> % </th>';
	conteudoHtml    += '        <th width="'+WidthCampo15+'" style="width: '+WidthCampo15+'px; display: none;"> Tipo </th>'; 
	conteudoHtml    += '        <th width="'+WidthCampo16+'" style="width: '+WidthCampo16+'px;"> Ação </th>';
	conteudoHtml    += '      </tr>';
	conteudoHtml    += '    </thead>';	
	conteudoHtml    += '    <tbody>';
	return conteudoHtml;
}

function GetTableFoot( urlPadrao, iAnoUlt ){
	var conteudoHtml = "";		
    conteudoHtml += '    </tbody>';
    conteudoHtml += '  </table>';
    conteudoHtml += '</div>';
    conteudoHtml += '<!-- Div table-responsive -->';
    //conteudoHtml += '<br/>';
	return conteudoHtml;
}

function GetTableLinha( urlPadrao, iNroMes, iAnoUlt, iAnoAtual, iMesAtual, fVlrInvestMensal, fVlrInvestFinal, fPercLucroMes, sTipo ){

	var BtnGraficMes    = '';

	// Botao Ajustar Valor Atual
	BtnGraficMes += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.6rem; min-width: 1.6rem; width: 1.6rem; margin: 1px 1px; font-size:0.3rem; " title="Ajustar Valor Atual do Mês '+arNomeMeses[iMesAtual]+'/'+iAnoUlt+'" href="javascript:void(0);" role="button" aria-pressed="true" onclick="AbrirModalValorAtualProjecao(\''+urlPadrao+'\', \''+iNroMes+'\');">';
	BtnGraficMes += '  <i class="fa fa-pencil fa-lg" aria-hidden="true"></i>';
	BtnGraficMes += '</a>';

	// Botao Grafico Anual
	var BtnGraficMesDisA = ( iMesAtual == 1 ? 'disabled' : '');
	BtnGraficMes        += '<a class="btn btn-sm btn-primary btn-icon btn-icon-mini btn-round btn-simple '+BtnGraficMesDisA+'" '+BtnGraficMesDisA+' style="height: 1.6rem; min-width: 1.6rem; width: 1.6rem; margin: 1px 1px; font-size:0.3rem; " title="Gráfico Anual até o Mês '+arNomeMeses[iMesAtual]+'" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fAbrirModalGraficoProjecao(\''+urlPadrao+'\', \'A\', \''+iMesAtual+'\', \''+iAnoUlt+'\');">';
	BtnGraficMes        += '  <i class="fa fa-area-chart fa-lg" aria-hidden="true"></i>';
	BtnGraficMes        += '</a>';

	// Botao Grafico Geral
	var BtnGraficMesDisG = ( iNroMes == 1 ? 'disabled' : '');
	BtnGraficMes        += '<a class="btn btn-sm btn-primary btn-icon btn-icon-mini btn-round btn-simple '+BtnGraficMesDisG+'" '+BtnGraficMesDisG+' style="height: 1.6rem; min-width: 1.6rem; width: 1.6rem; margin: 1px 1px; font-size:0.3rem; " title="Gráfico Geral até o Mês '+arNomeMeses[iMesAtual]+'/'+iAnoUlt+'" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fAbrirModalGraficoProjecao(\''+urlPadrao+'\', \'G\', \''+iMesAtual+'\', \''+iAnoUlt+'\');">';
	BtnGraficMes        += '  <i class="fa fa-area-chart fa-lg" aria-hidden="true"></i>';
	BtnGraficMes        += '</a>';

	var conteudoHtml = "";	
	conteudoHtml += '      <tr>';
	conteudoHtml += '        <td width="'+WidthCampo01+'" style="width: '+WidthCampo01+'px; display: none;" class="font-weight-bold">'+colcarFormacataoInteiro(iNroMes)+'</td>'; //Nro
	conteudoHtml += '        <td width="'+WidthCampo02+'" style="width: '+WidthCampo02+'px;"> '+iAnoAtual+' </td>'; //Ano
	conteudoHtml += '        <td width="'+WidthCampo03+'" style="width: '+WidthCampo03+'px;"> '+arNomeMeses[iMesAtual]+' </td>'; // Mês
	conteudoHtml += '        <td width="'+WidthCampo04+'" style="width: '+WidthCampo04+'px;"> <input required class="form-control text-right" style="margin: 0 auto; font-size:12px; width:95px; height:25px; " type="text" id="TxtGridEvoluProjVlrInvestMes'+iNroMes+'" value="'+ ( fVlrInvestMensal != 0.00 ? fMascaraValor(fVlrInvestMensal) : '' ) +'" onkeyup="ReCalcularTabelaProjetada();" XXXonkeypress="ReCalcularTabelaProjetada();" XXXonchange="ReCalcularTabelaProjetada();" > </td>'; //Vlr. Invest.
	conteudoHtml += '        <td width="'+WidthCampo05+'" style="width: '+WidthCampo05+'px;"> <span id="TxtGridEvoluProjVlrInvestAno'+iNroMes+'">R$ 0,00</span> </td>'; // Vlr. Invest Ano
	conteudoHtml += '        <td width="'+WidthCampo06+'" style="width: '+WidthCampo06+'px;"> <span id="TxtGridEvoluProjVlrInvestGeral'+iNroMes+'">R$ 0,00</span> </td>'; // Vlr. Invest Geral
	conteudoHtml += '        <td width="'+WidthCampo07+'" style="width: '+WidthCampo07+'px; display: none;"> <span id="TxtGridEvoluProjVlrMesInicio'+iNroMes+'">R$ 0,00</span> </td>'; // Vlr. Mês Inicio
	conteudoHtml += '        <td width="'+WidthCampo08+'" style="width: '+WidthCampo08+'px;"> <span id="TxtGridEvoluProjVlrMesFinal'+iNroMes+'">R$ '+fMascaraValor(fVlrInvestFinal)+'</span> </td>'; // Vlr. Mês Fim
	conteudoHtml += '        <td width="'+WidthCampo09+'" style="width: '+WidthCampo09+'px;"> <span id="TxtGridEvoluProjVlrLucroMes'+iNroMes+'">R$ 0,00</span> </td>'; // Vlr. Lucro Mês
	conteudoHtml += '        <td width="'+WidthCampo10+'" style="width: '+WidthCampo10+'px; font-size: 11px;"> <span id="TxtGridEvoluProjPercLucroMes'+iNroMes+'">'+fMascaraValor(fPercLucroMes)+'%</span> </td>'; // % Lucro Mês
	conteudoHtml += '        <td width="'+WidthCampo11+'" style="width: '+WidthCampo11+'px;"> <span id="TxtGridEvoluProjVlrLucroAno'+iNroMes+'">R$ 0,00</span> </td>'; // Vlr. Lucro Ano
	conteudoHtml += '        <td width="'+WidthCampo12+'" style="width: '+WidthCampo12+'px; font-size: 11px;"> <span id="TxtGridEvoluProjPercLucroAno'+iNroMes+'">0,00%</span> </td>'; // % Lucro Ano
	conteudoHtml += '        <td width="'+WidthCampo13+'" style="width: '+WidthCampo13+'px;"> <span id="TxtGridEvoluProjVlrLucroGeral'+iNroMes+'">R$ 0,00</span> </td>'; // Vlr. Lucro Geral
	conteudoHtml += '        <td width="'+WidthCampo14+'" style="width: '+WidthCampo14+'px; font-size: 11px;"> <span id="TxtGridEvoluProjPercLucroGeral'+iNroMes+'">0,00%</span> </td>'; // % Lucro Geral
	conteudoHtml += '        <td width="'+WidthCampo15+'" style="width: '+WidthCampo15+'px; display: none;"> <span id="TxtGridEvoluProjTipo'+iNroMes+'">'+sTipo+'</span> </td>'; // Tipo
	conteudoHtml += '        <td width="'+WidthCampo16+'" style="width: '+WidthCampo16+'px;">  <span id="TxtGridEvoluProjAcaoMes'+iNroMes+'">'+BtnGraficMes+'</span> </td>';  // Ação
	conteudoHtml += '      </tr>';
	return conteudoHtml;
	
}

async function MontarTabelaProjetada( urlPadrao, arDadosProjecao ){
	try { 

		 promise = new Promise( (resolve, reject) => {

			$('#DivEvolucaoProjetada').html("");
			
			var conteudoHtml = "";	
			
			if ( arDadosProjecao.length > 0 ){

				var iNroMes          = 0;
				var iAnoAtual        = 0;
				var iMesAtual        = 0;
				var fVlrInvestMensal = 0.00;
				var fPercLucroMes      = 0.00;
				var iAnoUlt          = 0;
				var fVlrInvestIni    = parseFloat( GetValorDecimal( arDadosProjecao[0].VlrInvestIni ) );

				conteudoHtml += GetTableButton( urlPadrao, fVlrInvestIni );

				$.each(arDadosProjecao, function (index, value) {
					
					iNroMes          = GetValorInteiro( value.NroMes   ); 
					iAnoAtual        = GetValorInteiro( value.AnoAtual );
					iMesAtual        = GetValorInteiro( value.MesAtual ); 
					fVlrInvestMensal = parseFloat( GetValorDecimal( value.VlrInvestMensal ) ); 
					fVlrInvestFinal  = parseFloat( GetValorDecimal( value.VlrInvestFim    ) );
					fPercLucroMes    = parseFloat( GetValorDecimal( value.TaxaMensal      ) );
					sTipo            = value.Tipo;  
					
					if ( iNroMes == 1 ) iAnoUlt = iAnoAtual;

					if ( (iMesAtual == 1) || ( iNroMes == 1) ){
						if ( iNroMes > 1 ){
							conteudoHtml += GetTableFoot( urlPadrao, iAnoUlt );
							iAnoUlt       = iAnoAtual;
						}// if ( iNroMes == 1 ){
						conteudoHtml += GetTableHead( urlPadrao );
					} //if ( iAnoAtual = 1 ){
					
					conteudoHtml += GetTableLinha( urlPadrao, iNroMes, iAnoUlt, iAnoAtual, iMesAtual, fVlrInvestMensal, fVlrInvestFinal, fPercLucroMes, sTipo );

				}); // $.each(arDadosProjecao, function (index, value) {

				iAnoUlt       = iAnoAtual;
				conteudoHtml += GetTableFoot( urlPadrao, iAnoUlt );
				
			} // if ( arDadosProjecao.length > 0 ){
			
			$('#DivEvolucaoProjetada').html(conteudoHtml); 

			ReCalcularTabelaProjetada();
			
			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada",  TP_ALERTA_ERRO, 'Erro ao Montar Tabela da Projeção - ' + txt + ' - ' + MSG_ALERTA_ERRO); 
		});

	} catch (e) {
		if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada",  TP_ALERTA_ERRO, 'Falha geral ao Montar Tabela da Projeção - ' + MSG_ALERTA_ERRO); 
	}
}  

async function ReCalcularTabelaProjetada(){
	try { 

		 promise = new Promise( (resolve, reject) => {

			//console.clear();

			var iAnoAtual        = 0;
			var iAnoUlt          = 0;
			var fVlrInvestIni    = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjVlrInvestIni').val() ) );
			var fTotInvestAno    = 0.00;
			var fTotInvestGeral  = 0.00;	
			var fVlrMesInicio    = 0.00;
			var fVlrMesFinal     = 0.00;
			var fVlrLucroMes     = 0.00;	
			var fPercLucroMes    = 0.00;	
			var fVlrLucroAno     = 0.00;	
			var fPercLucroAno    = 0.00;	
			var fVlrLucroGeral   = 0.00;	
			var fPercLucroGeral  = 0.00;	

			$('#GridAnaliseEvoluProj > tbody > tr').each(function(){
				try {
					
					var iNroMes          = GetValorInteiro( $(this).find("td").eq(0).html().trim() );
					iAnoAtual            = GetValorInteiro( $(this).find("td").eq(1).html().trim() );
					var fVlrInvestMensal = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjVlrInvestMes'+iNroMes).val().trim() ) );
					var sTipo            = $('#TxtGridEvoluProjTipo'+iNroMes).html().trim();
					
					if ( iNroMes == 1 ) {
					 	iAnoUlt         = iAnoAtual;
						fTotInvestAno   = fVlrInvestIni;
						fTotInvestGeral = fVlrInvestIni;
						fVlrMesInicio   = fVlrInvestIni;
						fVlrMesFinal    = fVlrInvestIni;
					}// if ( iNroMes == 1 ) {

					if ( iAnoAtual != iAnoUlt ){
						fTotInvestAno = 0.00;
						fVlrLucroAno  = 0.00;
					 	iAnoUlt       = iAnoAtual;
					} // if ( iAnoUlt !=  iAnoAtual ){

					fTotInvestAno       += fVlrInvestMensal;
					fTotInvestGeral     += fVlrInvestMensal;
					fVlrMesInicio       += fVlrInvestMensal;

					$('#TxtGridEvoluProjVlrMesFinal'+iNroMes).removeAttr( "title" );

					if (sTipo == 'C'){ // C - Calculado
						fVlrMesFinal        += fVlrInvestMensal;
						fPercLucroMes        = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjPercLucroMes'+iNroMes).html().trim().replace('%', '') ) ); 
						fVlrLucroMes         = fTrucarValorFixed( ( fVlrMesFinal * fPercLucroMes ) / 100 ); 
						fVlrMesFinal        += fVlrLucroMes;
						$('#TxtGridEvoluProjVlrMesFinal'+iNroMes).removeClass("font-weight-bold");
						$('#TxtGridEvoluProjVlrMesFinal'+iNroMes).attr( "title", 'Valor Atual Calculado' );
					} //if (sTipo == 'C'){

					if (sTipo == 'M'){ // M - Modificado
						fVlrMesFinal  = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjVlrMesFinal'+iNroMes).html().trim().replace('R$', '') ) ); 
						fVlrLucroMes  = (fVlrMesFinal - fVlrMesInicio);
						fPercLucroMes = 0.00;
						if ( fVlrLucroMes != 0.00 && fVlrMesInicio != 0.00 ) fPercLucroMes = ( fVlrLucroMes / fVlrMesInicio ) * 100;
						$('#TxtGridEvoluProjVlrMesFinal'+iNroMes).addClass("font-weight-bold");
						$('#TxtGridEvoluProjVlrMesFinal'+iNroMes).attr( "title", 'Valor Atual Modificado' );
					} //if (sTipo == 'M'){
					
					fVlrLucroAno += fVlrLucroMes;
					fPercLucroAno = 0.00;
					if ( fVlrLucroAno != 0.00 && fTotInvestAno != 0.00 ) fPercLucroAno = ( fVlrLucroAno / fTotInvestAno ) * 100;

					fVlrLucroGeral += fVlrLucroMes;
					fPercLucroGeral = 0.00;
					if ( fVlrLucroGeral != 0.00 && fTotInvestGeral != 0.00 ) fPercLucroGeral = ( fVlrLucroGeral / fTotInvestGeral ) * 100;

					$('#TxtGridEvoluProjVlrInvestAno'+iNroMes).html(    'R$ '+fMascaraValor(fTotInvestAno)    ); 
					$('#TxtGridEvoluProjVlrInvestGeral'+iNroMes).html(  'R$ '+fMascaraValor(fTotInvestGeral)  );
					$('#TxtGridEvoluProjVlrMesInicio'+iNroMes).html(    'R$ '+fMascaraValor(fVlrMesInicio)    ); 
					$('#TxtGridEvoluProjVlrMesFinal'+iNroMes).html(     'R$ '+fMascaraValor(fVlrMesFinal)     );
					$('#TxtGridEvoluProjVlrLucroMes'+iNroMes).html(     'R$ '+fMascaraValor(fVlrLucroMes)     ); 
					$('#TxtGridEvoluProjPercLucroMes'+iNroMes).html(    fMascaraValor(fPercLucroMes) + '%'    ); 
					$('#TxtGridEvoluProjVlrLucroAno'+iNroMes).html(     'R$ '+fMascaraValor(fVlrLucroAno)     ); 
					$('#TxtGridEvoluProjPercLucroAno'+iNroMes).html(    fMascaraValor(fPercLucroAno) + '%'    ); 
					$('#TxtGridEvoluProjVlrLucroGeral'+iNroMes).html(   'R$ '+fMascaraValor(fVlrLucroGeral)   ); 
					$('#TxtGridEvoluProjPercLucroGeral'+iNroMes).html(  fMascaraValor(fPercLucroGeral) + '%'  ); 
					
					$('#TxtGridEvoluProjVlrLucroMes'+iNroMes).removeClass("text-success");
					$('#TxtGridEvoluProjVlrLucroMes'+iNroMes).removeClass("text-danger");
					if( fTrucarValor(fVlrLucroMes) != 0.00 && fTrucarValor(fVlrLucroMes) > 0.00 ) $('#TxtGridEvoluProjVlrLucroMes'+iNroMes).addClass("text-success");
					if( fTrucarValor(fVlrLucroMes) != 0.00 && fTrucarValor(fVlrLucroMes) < 0.00 ) $('#TxtGridEvoluProjVlrLucroMes'+iNroMes).addClass("text-danger");
					
					$('#TxtGridEvoluProjVlrLucroAno'+iNroMes).removeClass("text-success");
					$('#TxtGridEvoluProjVlrLucroAno'+iNroMes).removeClass("text-danger");
					if( fTrucarValor(fVlrLucroAno) != 0.00 && fTrucarValor(fVlrLucroAno) > 0.00 ) $('#TxtGridEvoluProjVlrLucroAno'+iNroMes).addClass("text-success");
					if( fTrucarValor(fVlrLucroAno) != 0.00 && fTrucarValor(fVlrLucroAno) < 0.00 ) $('#TxtGridEvoluProjVlrLucroAno'+iNroMes).addClass("text-danger");
					
					$('#TxtGridEvoluProjVlrLucroGeral'+iNroMes).removeClass("text-success");
					$('#TxtGridEvoluProjVlrLucroGeral'+iNroMes).removeClass("text-danger");
					if( fTrucarValor(fVlrLucroGeral) != 0.00 && fTrucarValor(fVlrLucroGeral) > 0.00 ) $('#TxtGridEvoluProjVlrLucroGeral'+iNroMes).addClass("text-success");
					if( fTrucarValor(fVlrLucroGeral) != 0.00 && fTrucarValor(fVlrLucroGeral) < 0.00 ) $('#TxtGridEvoluProjVlrLucroGeral'+iNroMes).addClass("text-danger");

					fVlrMesInicio = fVlrMesFinal;

				} catch (e) {
					//console.log('Message = ' + e.message );
				} 
			}); //  $('#GridAnaliseEvoluProj > tbody > tr').each(function(){
			
			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada",  TP_ALERTA_ERRO, 'Erro ao ReCalcular Tabela da Projeção - ' + MSG_ALERTA_ERRO); 
		});

	} catch (e) {
		if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada",  TP_ALERTA_ERRO, 'Faha Geral ao ReCalcular Tabela da Projeção - ' + MSG_ALERTA_ERRO); 
	}
}

function AbrirModalExcluirProjecao( urlPadrao ) {
    try {
	   
	   var IdProjecao = $('#txtFiltroProjecaoDescricao').val();
       if ( IdProjecao == "" ){
		  fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_AVISO, 'Id. Projeção não informado!'); 
          return;
        }
		
       $("#PopModalExcluirEvolucaoProjecao").modal({backdrop: "static"});

    } catch (e) {
        $("#PopModalExcluirEvolucaoProjecao").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function iniciarAnimacaoExcluirAnaliseProjecao() {	
	$("#iSalvarProjecao").addClass("fa-spin");
	$("#BtnModalDetalheProjecaoSalvar").addClass("disabled");
}

function finalizarAnimacaoExcluirAnaliseProjecao() {
	$("#iSalvarProjecao").removeClass("fa-spin");
	$("#BtnModalDetalheProjecaoSalvar").removeClass("disabled");
}

async function fExcluirDadosProjecao( urlPadrao ) {
    try {

		 promise = new Promise( (resolve, reject) => {

			fLimparAreaAlerta("AreaAlertaPrincAnaliseEvoluProjetada");	
			fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetada");	
			fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc");

			var IdProjecao = $('#txtFiltroProjecaoDescricao').val();
			if ( IdProjecao == "" ){
				fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_AVISO, 'Id. Projeção não informado!'); 
				return;
			}

			finalizarAnimacaoExcluirAnaliseProjecao();
			iniciarAnimacaoExcluirAnaliseProjecao();
		
			$.ajax({
				dataType: "json",
				type: "post",
				url : urlPadrao + "Analise/excluirProjecao",
				data: { IdProjecao: IdProjecao },
				success: function (result) {
					
					finalizarAnimacaoExcluirAnaliseProjecao();				
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 

					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc", TP_ALERTA_AVISO, mensagem); 
						return false;
					} else if (resultado == "FALHA") {
						fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc", TP_ALERTA_ERRO, mensagem); 
						return;
					} else if (resultado == "OK") {					
						fCriarAlertaPrinc(TP_ALERTA_SUCESSO, mensagem); 

						$("#PopModalExcluirEvolucaoProjecao").modal("hide");
						$('#DivEvolucaoProjetada').html("");

						buscar_todos_nomes_projecoes(urlPadrao, 'txtFiltroProjecaoDescricao', false, false, true);

						$("#BtnProjecaoSalvar").addClass("disabled");
						//$("#BtnProjecaoResetar").addClass("disabled");
						$("#BtnProjecaoExcluir").addClass("disabled");
									
						$("#BtnProjecaoSalvar").hide();
						//$("#BtnProjecaoResetar").hide();
						$("#BtnProjecaoExcluir").hide();
						
						return true;
					} else {
						ffCriarAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc", TP_ALERTA_ERRO, mensagem); 
						return false;
					}
					
				},
				error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
					$("#PopModalExcluirEvolucaoProjecao").modal("hide");
					finalizarAnimacaoExcluirAnaliseProjecao();
					fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);  // request.responseText //MSG_ALERTA_ERRO
				}
			});
			
			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			$("#PopModalGraficoEvolucaoProjecao").modal("hide");
			fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada",  TP_ALERTA_ERRO, 'Erro ao Montar Tabela da Projeção - ' + txt + ' - ' + MSG_ALERTA_ERRO); 
		});

    } catch (e) {
        $("#PopModalExcluirEvolucaoProjecao").modal("hide");
        finalizarAnimacaoExcluirAnaliseProjecao();
		fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function iniciarAnimacaoAlterarAnaliseProjecao() {	
    $("#iAlterarProjecao").removeClass("fa-check-square-o");
    $("#iAlterarProjecao").addClass("fa-spinner");
	$("#iAlterarProjecao").addClass("fa-pulse");
	$("#BtnProjecaoSalvar").addClass("disabled");
}

function finalizarAnimacaoAlterarAnaliseProjecao() {
    $("#iAlterarProjecao").addClass("fa-check-square-o");
    $("#iAlterarProjecao").removeClass("fa-spinner");
	$("#iAlterarProjecao").removeClass("fa-pulse");
	$("#BtnProjecaoSalvar").removeClass("disabled");
}

async function fAlterarDadosProjecao( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {
						
			fLimparAreaAlerta("AreaAlertaPrincAnaliseEvoluProjetada");	
			fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetada");	
			fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc");

			var IdProjecao = $('#txtFiltroProjecaoDescricao').val();
			if ( IdProjecao == "" ){
				fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_AVISO, 'Id. Projeção não informado!'); 
				return;
			}
			
			finalizarAnimacaoAlterarAnaliseProjecao();
			iniciarAnimacaoAlterarAnaliseProjecao();
			
			var fVlrInvestIni   = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjVlrInvestIni').val() ) );
			var arDadosProjecao = [];

			// console.clear();
			
			$('#GridAnaliseEvoluProj > tbody > tr').each(function(){
				try {

					var iNroMes          = GetValorInteiro(     $(this).find("td").eq(0).html().trim() );
					var iAnoAtual        = GetValorInteiro(     $(this).find("td").eq(1).html().trim() );
					var iMesAtual        = arNomeMeses.indexOf( $(this).find("td").eq(2).html().trim() );
					var fVlrInvestMensal = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjVlrInvestMes'+iNroMes).val().trim()                   ) );
					var fVlrMesFinal     = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjVlrMesFinal'+iNroMes).html().trim().replace('R$', '') ) );
					var fPercLucroMes    = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjPercLucroMes'+iNroMes).html().trim().replace('%', '') ) ); 
					var sTipo            = $('#TxtGridEvoluProjTipo'+iNroMes).html().trim();

					arDadosProjecao.push({ NroMes: iNroMes, AnoAtual: iAnoAtual, MesAtual: iMesAtual, VlrInvestIni: fVlrInvestIni, VlrInvestMensal: fVlrInvestMensal, VlrInvestFim: fVlrMesFinal, TaxaMensal: fPercLucroMes, Tipo: sTipo });
				
					// console.log(
					// 	'iNroMes: ' + iNroMes 
					// 	+ ' // iAnoAtual: ' + iAnoAtual 
					// 	+ ' // iMesAtual: ' + iMesAtual 
					// 	+ ' // fVlrInvestIni: ' + fVlrInvestIni 
					// 	+ ' // fVlrInvestMensal: ' + fVlrInvestMensal 
					// 	+ ' // fVlrMesFinal: ' + fVlrMesFinal 
					// 	+ ' // fPercLucroMes: ' + fPercLucroMes 
					// 	+ ' // sTipo: ' + sTipo 
					// );

				} catch (e) {
					//console.log('Message = ' + e.message );
				} 
			}); //  $('#GridAnaliseEvoluProj > tbody > tr').each(function(){

			if ( arDadosProjecao.length <= 0 ){
				fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_AVISO, 'Lista de Projeção não informada!'); 
				return;
			}

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "Analise/alterarProjecao",
				data    : { IdProjecao: IdProjecao, DadosProjecao: arDadosProjecao },
				success: function(result) {  
				
					finalizarAnimacaoAlterarAnaliseProjecao();
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 

					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_ERRO, mensagem); 
						return;
					} else if (resultado == "OK") {
						fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					} else {
						fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
					finalizarAnimacaoAlterarAnaliseProjecao();
					fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);  // request.responseText //MSG_ALERTA_ERRO
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
			$("#PopModalGraficoEvolucaoProjecao").modal("hide");
			fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada",  TP_ALERTA_ERRO, 'Erro ao Montar Tabela da Projeção - ' + txt + ' - ' + MSG_ALERTA_ERRO); 
		});
	
	} catch (e) {
		finalizarAnimacaoAlterarAnaliseProjecao();
		fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

async function fAbrirModalGraficoProjecao( urlPadrao, sTipoGrafico = '', iMesLimite = 0, iAnoLimite = 0 ){
	try {
		
		fLimparAreaAlerta("AreaAlertaPrincAnaliseEvoluProjetada");	
		fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetada");	
		fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc");
		$('#DivGraficoEvolucaoProjecao').html('<i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i>');

		var TituloPop = 'Projeção até '+arNomeMeses[iMesLimite]+'/'+iAnoLimite; //Gráfico da Projeção
		if ( iMesLimite == 0 ) TituloPop = 'Projeção de '+iAnoLimite; //Gráfico da Projeção
		
		$('#TitModalGraficoEvolucaoProjecao').html(TituloPop);
		$("#PopModalGraficoEvolucaoProjecao").modal({backdrop: 'static'});
		
		 promise = new Promise( (resolve, reject) => {

			//var conteudoHtml          = '';
			var DataSetValorInvestido = []; 
			var DataSetValorAtual     = [];

			var iIndexArray = 0;
			$('#GridAnaliseEvoluProj > tbody > tr').each(function(){
				try {

					var iNroMes   = GetValorInteiro(     $(this).find("td").eq(0).html().trim() );
					var iAnoAtual = GetValorInteiro(     $(this).find("td").eq(1).html().trim() );
					var iMesAtual = arNomeMeses.indexOf( $(this).find("td").eq(2).html().trim() );

					if ( sTipoGrafico == 'A' && iAnoAtual  < iAnoLimite                           ) return true;  // continue;
					if ( sTipoGrafico == 'A' && iAnoAtual  > iAnoLimite                           ) return false; // break;
					if ( sTipoGrafico == 'A' && iAnoAtual == iAnoLimite && iMesAtual > iMesLimite ) return false; // break;
					if ( sTipoGrafico == 'G' && iAnoAtual  > iAnoLimite                           ) return false; // break; 
					if ( sTipoGrafico == 'G' && iAnoAtual == iAnoLimite && iMesAtual > iMesLimite ) return false; // break;

					var DataAtual     = new Date(iAnoAtual, iMesAtual, 0).toLocaleDateString("pt-BR");
					var fVlrMesFinal  = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjVlrMesFinal'+iNroMes).html().trim().replace('R$', '') ) );
					var fTotInvestMes = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjVlrInvestGeral'+iNroMes).html().trim().replace('R$', '') ) );

					// if ( sTipoGrafico == 'A' ) var fTotInvestMes = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjVlrInvestAno'+iNroMes).html().trim().replace('R$', '') ) );
					// if ( sTipoGrafico == 'G' ) var fTotInvestMes = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjVlrInvestGeral'+iNroMes).html().trim().replace('R$', '') ) );
					
					iIndexArray++;
					DataSetValorInvestido[ iIndexArray - 1 ] = [moment(colcarFormacataoDataXMLPadrao(DataAtual)).valueOf(), fTotInvestMes ];
					DataSetValorAtual[     iIndexArray - 1 ] = [moment(colcarFormacataoDataXMLPadrao(DataAtual)).valueOf(), fVlrMesFinal  ];

				} catch (e) {
					//console.log('Message = ' + e.message );
				} 
			}); //  $('#GridAnaliseEvoluProj > tbody > tr').each(function(){
			
			// $('#DivGraficoEvolucaoProjecao').html(conteudoHtml); 
			// resolve(true);
			// return;
			
			$('#DivGraficoEvolucaoProjecao').html('');

			Highcharts.setOptions({ global: { useUTC: false }, lang: { decimalPoint: ',', thousandsSep: '.' } });

			Highcharts.setOptions({
				lang: {
				months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
				shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
				weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
				loading: ['Atualizando o gráfico...aguarde'],
				contextButtonTitle: 'Exportar gráfico',
				decimalPoint: ',',
				thousandsSep: '.',
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
				}
			});

			Highcharts.stockChart('DivGraficoEvolucaoProjecao', {

				title: { 
					text: null ,
					// 	align: 'center',
					// 	useHTML: false,
					// 	text: '', // '<h6 class="font-weight-bold text-muted">Custo/Ação x Preço Médio</h6>',
				},

				chart: {
					//zoomType: 'xy' ,
					//zoomType: 'x',
					zoomType: null,
					//renderTo: 'container',
				},
				
				legend: {
					enabled: false
				},

				global: {
					useUTC: false
				},

				colors: ['#7798BF', '#55BF3B' ],

				lang: {
					months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
					shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
					weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
					loading: ['Atualizando o gráfico...aguarde'],
					contextButtonTitle: 'Exportar gráfico',
					decimalPoint: ',',
					thousandsSep: '.',
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

				rangeSelector: {
					enabled:false,
					selected: 5,
					allButtonsEnabled: false,
					inputEnabled: false,
					buttonTheme: { visibility: 'hidden' },
					labelStyle: { visibility: 'hidden' },
				},

				plotOptions: {
					series: {
						//compare: 'percent',
						//marker: {enabled: false },
						showInNavigator: false,
					},
					//line: { marker: {enabled: false }, turboThreshold: 2000, }
				},
				
				navigator: {
					enabled: false
				},

				tooltip: {
					valueDecimals: 2
				},

				xAxis: {
					// title: null,
					type: 'datetime',
					minTickInterval: 24 * 3600 * 1000,
					dateTimeLabelFormats: { month: "%b '%y", year: "%Y" },
					//labels: { formatter: function() { return moment(this.value).format("MM/YYYY"); }, },
					// crosshair: true,
				},

				yAxis: {
					labels: { formatter: function () { return 'R$ '+fMascaraValor(this.value); } },
					plotLines: [{value: 0,width: 2,color: 'silver'}]
				},
				
				// yAxis: [
				// 	{ title: { text: 'Total - R$',   style: { color: Highcharts.getOptions().colors[1] } }, labels: { format: 'R$ {value:.2f}', style: { color: Highcharts.getOptions().colors[1] } },                },// Primary yAxis
				// 	{ title: { text: 'Percentual - %', style: { color: Highcharts.getOptions().colors[0] } }, labels: { format: '{value:.2f}%',   style: { color: Highcharts.getOptions().colors[0] } }, opposite: true } // Secondary yAxis
				// ],
				
				// series: [
				// 	{ 
				// 			type: 'column', 
				// 			name: 'Total Proventos', 
				// 			yAxis: 1,
				// 			data: arVlrProv,
				// 			tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true }
				// 	} , 
				// 	{ 
				// 			type: 'spline', 
				// 			name: '% Evolução', 
				// 			data: arPercProv, 
				// 			marker: { lineWidth: 2, lineColor: Highcharts.getOptions().colors[3], fillColor: 'white' } ,
				// 			//tooltip: { headerFormat: '<b>{point.x}</b><br/>', pointFormat: '{series.name}: {point.y:.2f}%' }
				// 			tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>' + value + '%</b><br />'; }, shared: true }
				// 		}
				// ]

				tooltip: {
					split: true, 
					valueDecimals: 2, 
					//pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
					pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>R$ {point.y}</b><br/>',
				},

				series: [
					{
						name: 'Valor Investido',
						data: DataSetValorInvestido,
						//animation: false,
						dataGrouping: { groupPixelWidth: 5, },
						marker: { lineWidth: 2, lineColor: Highcharts.getOptions().colors[1], fillColor: 'white' } ,
						//pointStart: Date.UTC(2000, 0, 1),
						//pointInterval: 24 * 3600 * 1000,
					}, 

					{
						name: 'Valor Atual',
						data: DataSetValorAtual,
						//animation: false,
						dataGrouping: {groupPixelWidth: 5, },
						marker: { lineWidth: 2, lineColor: Highcharts.getOptions().colors[3], fillColor: 'white' } ,
						//pointStart: Date.UTC(2000, 0, 1),
						//pointInterval: 24 * 3600 * 1000,
					}
				]
			});		
	
			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			$("#PopModalGraficoEvolucaoProjecao").modal("hide");
			fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada",  TP_ALERTA_ERRO, 'Erro ao Montar Tabela da Projeção - ' + txt + ' - ' + MSG_ALERTA_ERRO); 
		});
	
	} catch (e) {
		$("#PopModalGraficoEvolucaoProjecao").modal("hide");
		fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function AbrirModalValorAtualProjecao( urlPadrao, iNroMes ){
	try {

		fLimparAreaAlerta("AreaAlertaPrincAnaliseEvoluProjetada");	
		fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetada");	
		fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc");
		fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetadaAjusteVlrAtual");
		
		$('#txtAnaliseEvoluProjetAjusteVlrAtualNroMes').val(      '' );
		$('#txtAnaliseEvoluProjetAjusteVlrAtualVlrMesFinal').val( '' );
		
		var fVlrMesFinal = parseFloat( GetValorDecimal( $('#TxtGridEvoluProjVlrMesFinal'+iNroMes).html().trim().replace('R$', '') ) ); 

		$('#txtAnaliseEvoluProjetAjusteVlrAtualNroMes').val(      iNroMes                     );
		$('#txtAnaliseEvoluProjetAjusteVlrAtualVlrMesFinal').val( fMascaraValor(fVlrMesFinal) );

		$("#PopModalAjustarVlrAtualEvolucaoProjecao").modal({backdrop: 'static'});
		$(document).on('shown.bs.modal', function (e) { $("#txtAnaliseEvoluProjetAjusteVlrAtualVlrMesFinal").focus(); });

	} catch (e) {
		$("#PopModalAjustarVlrAtualEvolucaoProjecao").modal("hide");
		fCriarAlerta("AreaAlertaPrincAnaliseEvoluProjetada", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function AjustarValorAtualProjecao( urlPadrao ){
	try {

		fLimparAreaAlerta("AreaAlertaPrincAnaliseEvoluProjetada");	
		fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetada");	
		fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetadaExc");
		fLimparAreaAlerta("AreaAlertaModalAnaliseEvoluProjetadaAjusteVlrAtual");
		
		var iNroMes      = $('#txtAnaliseEvoluProjetAjusteVlrAtualNroMes').val();
		var fVlrMesFinal = parseFloat( GetValorDecimal( $('#txtAnaliseEvoluProjetAjusteVlrAtualVlrMesFinal').val() ) ); 

		if ( iNroMes == '' || iNroMes == 0 ) {
			fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetadaAjusteVlrAtual", TP_ALERTA_AVISO, 'Nro Mês da Projeção não informado!'); 
			return;
		}

		$('#TxtGridEvoluProjTipo'+iNroMes).html('M'); // M-Modificado
		$('#TxtGridEvoluProjVlrMesFinal'+iNroMes).html( 'R$ '+fMascaraValor(fVlrMesFinal) );

		$("#PopModalAjustarVlrAtualEvolucaoProjecao").modal("hide");

		ReCalcularTabelaProjetada();

	} catch (e) {
		$("#PopModalAjustarVlrAtualEvolucaoProjecao").modal("hide");
		fCriarAlerta("AreaAlertaModalAnaliseEvoluProjetadaAjusteVlrAtual", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function fAbrirModalAddMaisProjecao( urlPadrao ){
	// alert('Fim');
}
