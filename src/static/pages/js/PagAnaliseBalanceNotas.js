
async function fLimparGridBalanceNotas( urlPadrao ){ 

     promise = new Promise( (resolve, reject) => {

        fLimparAreaAlerta("AreaAlertaPrincAnaliseBalance");
        $("#DivBalanceNotasGrid").html("");

        var TxtBalanceNotas_TotAtual  = 0.00;
        var TxtBalanceNotas_TotAjuste = 0.00;

        var TxtBalanceNotas_TotAtualAcao  = 0.00;
        var TxtBalanceNotas_TotAjusteAcao = 0.00;

        var TxtBalanceNotas_TotAtualFII  = 0.00;
        var TxtBalanceNotas_TotAjusteFII = 0.00;

        var TxtBalanceNotas_TotAtualETF  = 0.00;
        var TxtBalanceNotas_TotAjusteETF = 0.00;

        var TxtBalanceNotas_TotAtualBDR  = 0.00;
        var TxtBalanceNotas_TotAjusteBDR = 0.00;

        var TxtBalanceNotas_TotAtualCRIPTO  = 0.00;
        var TxtBalanceNotas_TotAjusteCRIPTO = 0.00;

        fAtualizarDadosTituloBalanceNotas(
            TxtBalanceNotas_TotAtual, TxtBalanceNotas_TotAjuste,
            TxtBalanceNotas_TotAtualAcao, TxtBalanceNotas_TotAjusteAcao,
            TxtBalanceNotas_TotAtualFII, TxtBalanceNotas_TotAjusteFII,
            TxtBalanceNotas_TotAtualETF, TxtBalanceNotas_TotAjusteETF,
            TxtBalanceNotas_TotAtualBDR, TxtBalanceNotas_TotAjusteBDR,
            TxtBalanceNotas_TotAtualCRIPTO, TxtBalanceNotas_TotAjusteCRIPTO
        );

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
    
async function fCarregarListaPortfolioBalanc( urlPadrao ){
	try {	
            
         promise = new Promise( (resolve, reject) => {

            $('#txtFiltroBalanceNotaPortfolio').empty(); 
            $('#txtFiltroBalanceNotaPortfolio').append('<option value=""  selected>Meu Portfólio</option>');
            $('#txtFiltroBalanceNotaPortfolio').append('<option value="ACAO">Minhas Ações </option>');
            $('#txtFiltroBalanceNotaPortfolio').append('<option value="FII">Meus FIIs    </option>');
            $('#txtFiltroBalanceNotaPortfolio').append('<option value="ETF">Meus ETFs    </option>');
            $('#txtFiltroBalanceNotaPortfolio').append('<option value="BDR">Minhas BDRs </option>');
            $('#txtFiltroBalanceNotaPortfolio').append('<option value="CRIPTO">Minhas CRIPTOs </option>');
            
            $('#txtFiltroBalanceNotaPercent').empty(); 
            $('#txtFiltroBalanceNotaPercent').append('<option value=""  selected>Meu Portfólio</option>');
            $('#txtFiltroBalanceNotaPercent').append('<option value="ACAO">Minhas Ações </option>');
            $('#txtFiltroBalanceNotaPercent').append('<option value="FII">Meus FIIs    </option>');
            $('#txtFiltroBalanceNotaPercent').append('<option value="ETF">Meus ETFs    </option>');
            $('#txtFiltroBalanceNotaPercent').append('<option value="BDR">Minhas BDRs </option>');
            $('#txtFiltroBalanceNotaPercent').append('<option value="CRIPTO">Minhas CRIPTOs </option>');
    
            $.ajax({
                cache   : "false",
                dataType: "json",
                async   : true,
                type    : "POST",
                url     : urlPadrao + "listas/lista_nomes_carteira_user",
                // data    : {  },
                success: function(result) {  
                
                    var resultado = result.data.Resultado; 
                    var mensagem  = result.data.Mensagem; 
                    var lista     = result.data.Lista; 
    
                    if (resultado == "NSESSAO") {
                        $(location).attr('href', urlPadrao + '/login');
                        return false;
                    } else if (resultado == "NOK") {
                        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_AVISO, mensagem); 
                        return false;
                    } else if (resultado == "FALHA") {
                        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, mensagem); 
                        return false;
                    } else if (resultado == "OK") {	
                        $.each(lista, function (index, value) {
                            $('#txtFiltroBalanceNotaPortfolio').append('<option value="'+value[0]+'">'+value[1]+'</option>');
                            $('#txtFiltroBalanceNotaPercent').append('<option value="'+value[0]+'">'+value[1]+'</option>');
                        });
                        fDefinirPadraoSelect('txtFiltroBalanceNotaPortfolio');
                        fDefinirPadraoSelect('txtFiltroBalanceNotaPercent');
                        return true;
                    } else {
                        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, mensagem); 
                        return false;
                    }
                    
                },
                error: function(data) {
                    fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
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
	
	} catch(e) {
		fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

async function fAtualizarDadosTituloBalanceNotas( TxtBalanceNotas_TotAtual, TxtBalanceNotas_TotAjuste, 
                                            TxtBalanceNotas_TotAtualAcao, TxtBalanceNotas_TotAjusteAcao, 
                                            TxtBalanceNotas_TotAtualFII, TxtBalanceNotas_TotAjusteFII, 
                                            TxtBalanceNotas_TotAtualETF, TxtBalanceNotas_TotAjusteETF,
                                            TxtBalanceNotas_TotAtualBDR, TxtBalanceNotas_TotAjusteBDR,
                                            TxtBalanceNotas_TotAtualCRIPTO, TxtBalanceNotas_TotAjusteCRIPTO
                                           ){

     promise = new Promise( (resolve, reject) => {

        $("#TxtBalanceNotas_TotAtual").html(  "R$ "+fMascaraValor(TxtBalanceNotas_TotAtual) );
        $("#TxtBalanceNotas_TotAjuste").html( "R$ "+fMascaraValor(TxtBalanceNotas_TotAjuste) );    
    
        var TxtBalanceNotas_PercAtualAcao  = 0.00;
        if ( TxtBalanceNotas_TotAtual  > 0.00 && TxtBalanceNotas_TotAtualAcao > 0.00  ) TxtBalanceNotas_PercAtualAcao  = ( TxtBalanceNotas_TotAtualAcao  / TxtBalanceNotas_TotAtual  ) * 100;
        $("#TxtBalanceNotas_TotAtualAcao").html(  "R$ "+fMascaraValor(TxtBalanceNotas_TotAtualAcao)+" ("+fMascaraValor(TxtBalanceNotas_PercAtualAcao)+"%)");
    
        var TxtBalanceNotas_PercAjusteAcao = 0.00;
        if ( TxtBalanceNotas_TotAjuste > 0.00 && TxtBalanceNotas_TotAjusteAcao > 0.00 ) TxtBalanceNotas_PercAjusteAcao = ( TxtBalanceNotas_TotAjusteAcao / TxtBalanceNotas_TotAjuste ) * 100;
        $("#TxtBalanceNotas_TotAjusteAcao").html( "R$ "+fMascaraValor(TxtBalanceNotas_TotAjusteAcao)+" ("+fMascaraValor(TxtBalanceNotas_PercAjusteAcao)+"%)");   
    
        var TxtBalanceNotas_PercAtualFII  = 0.00;
        if ( TxtBalanceNotas_TotAtual  > 0.00 && TxtBalanceNotas_TotAtualFII  > 0.00 ) TxtBalanceNotas_PercAtualFII  = ( TxtBalanceNotas_TotAtualFII   / TxtBalanceNotas_TotAtual  ) * 100;
        $("#TxtBalanceNotas_TotAtualFII").html(   "R$ "+fMascaraValor(TxtBalanceNotas_TotAtualFII)+" ("+fMascaraValor(TxtBalanceNotas_PercAtualFII)+"%)");
    
        var TxtBalanceNotas_PercAjusteFII = 0.00;
        if ( TxtBalanceNotas_TotAjuste > 0.00 && TxtBalanceNotas_TotAjusteFII > 0.00 ) TxtBalanceNotas_PercAjusteFII = ( TxtBalanceNotas_TotAjusteFII / TxtBalanceNotas_TotAjuste ) * 100;
        $("#TxtBalanceNotas_TotAjusteFII").html(  "R$ "+fMascaraValor(TxtBalanceNotas_TotAjusteFII)+" ("+fMascaraValor(TxtBalanceNotas_PercAjusteFII)+"%)"); 
    
        var TxtBalanceNotas_PercAtualETF  = 0.00;
        if ( TxtBalanceNotas_TotAtual  > 0.00 && TxtBalanceNotas_TotAtualETF  > 0.00 ) TxtBalanceNotas_PercAtualETF  = ( TxtBalanceNotas_TotAtualETF   / TxtBalanceNotas_TotAtual  ) * 100;
        $("#TxtBalanceNotas_TotAtualETF").html(   "R$ "+fMascaraValor(TxtBalanceNotas_TotAtualETF)+" ("+fMascaraValor(TxtBalanceNotas_PercAtualETF)+"%)");
    
        var TxtBalanceNotas_PercAjusteETF = 0.00;
        if ( TxtBalanceNotas_TotAjuste > 0.00 && TxtBalanceNotas_TotAjusteETF > 0.00 ) TxtBalanceNotas_PercAjusteETF = ( TxtBalanceNotas_TotAjusteETF / TxtBalanceNotas_TotAjuste ) * 100;
        $("#TxtBalanceNotas_TotAjusteETF").html(  "R$ "+fMascaraValor(TxtBalanceNotas_TotAjusteETF)+" ("+fMascaraValor(TxtBalanceNotas_PercAjusteETF)+"%)");  

        var TxtBalanceNotas_PercAtualBDR  = 0.00;
        if ( TxtBalanceNotas_TotAtual  > 0.00 && TxtBalanceNotas_TotAtualBDR  > 0.00 ) TxtBalanceNotas_PercAtualBDR  = ( TxtBalanceNotas_TotAtualBDR   / TxtBalanceNotas_TotAtual  ) * 100;
        $("#TxtBalanceNotas_TotAtualBDR").html(   "R$ "+fMascaraValor(TxtBalanceNotas_TotAtualBDR)+" ("+fMascaraValor(TxtBalanceNotas_PercAtualBDR)+"%)");

        var TxtBalanceNotas_PercAjusteBDR = 0.00;
        if ( TxtBalanceNotas_TotAjuste > 0.00 && TxtBalanceNotas_TotAjusteBDR > 0.00 ) TxtBalanceNotas_PercAjusteBDR = ( TxtBalanceNotas_TotAjusteBDR / TxtBalanceNotas_TotAjuste ) * 100;
        $("#TxtBalanceNotas_TotAjusteBDR").html(  "R$ "+fMascaraValor(TxtBalanceNotas_TotAjusteBDR)+" ("+fMascaraValor(TxtBalanceNotas_PercAjusteBDR)+"%)");

        var TxtBalanceNotas_PercAtualCRIPTO  = 0.00;
        if ( TxtBalanceNotas_TotAtual  > 0.00 && TxtBalanceNotas_TotAtualCRIPTO  > 0.00 ) TxtBalanceNotas_PercAtualCRIPTO  = ( TxtBalanceNotas_TotAtualCRIPTO   / TxtBalanceNotas_TotAtual  ) * 100;
        $("#TxtBalanceNotas_TotAtualCRIPTO").html(   "R$ "+fMascaraValor(TxtBalanceNotas_TotAtualCRIPTO)+" ("+fMascaraValor(TxtBalanceNotas_PercAtualCRIPTO)+"%)");

        var TxtBalanceNotas_PercAjusteCRIPTO = 0.00;
        if ( TxtBalanceNotas_TotAjuste > 0.00 && TxtBalanceNotas_TotAjusteCRIPTO > 0.00 ) TxtBalanceNotas_PercAjusteCRIPTO = ( TxtBalanceNotas_TotAjusteCRIPTO / TxtBalanceNotas_TotAjuste ) * 100;
        $("#TxtBalanceNotas_TotAjusteCRIPTO").html(  "R$ "+fMascaraValor(TxtBalanceNotas_TotAjusteCRIPTO)+" ("+fMascaraValor(TxtBalanceNotas_PercAjusteCRIPTO)+"%)");

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

function fDimunuirNota( urlPadrao, AtvCodigo ){ 
    var nota = "";
    nota = $('#txtPortfBalancNotasPercent'+AtvCodigo).val();
    if ( nota == "" ) nota = 0;
    nota = parseInt(nota) - 1;
    if ( nota <= 0) nota = 0;
    $('#txtPortfBalancNotasPercent'+AtvCodigo).val( nota );
    fCalcularBalanceNotas( urlPadrao );
}    

function fAumentarNota( urlPadrao, AtvCodigo ){ 
    var nota = "";
    nota = $('#txtPortfBalancNotasPercent'+AtvCodigo).val();
    if ( nota == "" ) nota = 0;
    nota = parseInt(nota) + 1;
    if ( nota >= 100) nota = 100;
    $('#txtPortfBalancNotasPercent'+AtvCodigo).val( nota );
    fCalcularBalanceNotas( urlPadrao );
}     

function iniciarAnimacaoPesquisarBalanceNotas() {
	//$("#iRefreshBalanceNotas").addClass("fa-spin");
	//$("#BtnBalanceNotasPesquisar").addClass("disabled");
    $("#txtFiltroBalanceNotaPortfolio").attr("disabled","disabled");
    fDefinirPadraoSelect('txtFiltroBalanceNotaPortfolio');
}

function finalizarAnimacaoPesquisaBalanceNotas() {
	// $("#iRefreshBalanceNotas").removeClass("fa-spin");
    // $("#BtnBalanceNotasPesquisar").removeClass("disabled");
    $("#txtFiltroBalanceNotaPortfolio").removeAttr("disabled");
    fDefinirPadraoSelect('txtFiltroBalanceNotaPortfolio');
}

async function fCarregarGridBalanceNotas( urlPadrao ) {
    try {

         promise = new Promise( (resolve, reject) => {
    
            finalizarAnimacaoPesquisaBalanceNotas();
            iniciarAnimacaoPesquisarBalanceNotas();
            
            var DivBalanceNotas = $("#DivBalanceNotasGrid");
            DivBalanceNotas.html(""); 
    
            var IdPortfolio = $("#txtFiltroBalanceNotaPortfolio").val();
    
            $.ajax({
                cache   : "false",
                dataType: "json",
                async   : true,
                type    : "POST",
                url     : urlPadrao + "Analise/gridBalanceNotas",
                data: { IdPortfolio: IdPortfolio },
                success: function(result) {  
                    
                    var resultado = result.data.Resultado; 
                    var mensagem  = result.data.Mensagem; 
                    var lista     = result.data.Lista;
    
                    if (resultado == "NSESSAO") {
                        $(location).attr('href', urlPadrao + '/login');
                        return false;
                    } else if (resultado == "NOK") {
                        finalizarAnimacaoPesquisaBalanceNotas();
                        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_AVISO, mensagem); 
                        return;
                    } else if (resultado == "FALHA") {
                        finalizarAnimacaoPesquisaBalanceNotas();
                        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, mensagem); 
                        return;
                    } else if (resultado == "OK") {
    
                        if ( lista.length > 0 ){
                            
                            var content = '';
                            
                            var TotalInvest = 0.00;
                            $.each(lista, function (index, value) {
                                TotalInvest += parseFloat( GetValorDecimal(value[3]) ); // 3-Total Atual
                            });
    
                            lista.sort(function(a, b){
                                var NotaA = parseFloat( GetValorDecimal(a[4])); // 4-Nota Salva  
                                var NotaB = parseFloat( GetValorDecimal(b[4])); // 4-Nota Salva 
                                if(NotaA == NotaB) return 0;
                                return NotaA > NotaB? 1: -1;
                            });
                            
                            content += '<div class="table-responsive" id="AreaGrid">';
                            content += '<table class="table table-sm table-hover" style="font-size: 12px" border="0" cellspacing="0" width="100%" style="margin: 0px;">';
                            content += '  <thead>';
                            content += '    <tr class="text-center bg-dark text-white" style="font-size: 12px"> ';
                            content += '      <th style="border: 0px; border: 1px solid black;" colspan="3">ATIVO</th>';
                            content += '      <th style="border: 0px" bgcolor="#FFFFFF" style="width:10px"> </th>';
                            content += '      <th style="border: 0px; border: 1px solid black;" colspan="3">PORTFÓLIO ATUAL</th>';
                            content += '      <th style="border: 0px" bgcolor="#FFFFFF" style="width:10px"> </th>';
                            content += '      <th style="border: 0px; border: 1px solid black;" colspan="4">PORTFÓLIO AJUSTADO</th>';
                            content += '      <th style="border: 0px" bgcolor="#FFFFFF" style="width:10px"> </th>';
                            content += '      <th style="border: 0px; border: 1px solid black;" colspan="3">RESULTADO</th>';
                            content += '    </tr>';  
                            content += '    <tr class="text-center bg-dark text-white"> ';
                            content += '      <th style="border: 0px; width:5px; border-left: 1px solid black; ">Tipo</th>';
                            content += '      <th style="border: 0px; width:5px; ">Código</th>';
                            content += '      <th style="border: 0px; width:5px; border-right: 1px solid black; ">Preço</th>';
                            content += '      <th style="border: 0px; width:5px; border: 0px" bgcolor="#FFFFFF" > </th>';
                            content += '      <th style="border: 0px; width:5px; border-left: 1px solid black; "> Quant. </th>';
                            content += '      <th style="border: 0px; width:20px;"> Total</th>';
                            content += '      <th style="border: 0px; width:5px; border-right: 1px solid black; "> % Atual</th>';
                            content += '      <th style="border: 0px; width:5px; border: 0px" bgcolor="#FFFFFF" > </th>';
                            content += '      <th style="border: 0px; width:5px; border-left: 1px solid black; "> Nota</th>';
                            content += '      <th style="border: 0px; width:10px;"> Quant. </th>';
                            content += '      <th style="border: 0px; width:10px;"> Total </th>';
                            content += '      <th style="border: 0px; width:30px; border-right: 1px solid black; "> % Definido</th>';
                            content += '      <th style="border: 0px; width:5px; border: 0px" bgcolor="#FFFFFF" > </th>';
                            content += '      <th style="border: 0px; width:30px; border-left: 1px solid black; "> Status </th>';
                            content += '      <th style="border: 0px; width:5px;"> Quant. </th>';
                            content += '      <th style="border: 0px; width:20px; border-right: 1px solid black; "> Total </th>';
                            content += '    </tr>';  
                            content += '  </thead>';
                            content += '  <tbody>';
    
                            var UltimaNota = 0.00;
                            $.each(lista, function (index, value) {
    
                                var AtvCodigo     = value[0].replace("/", "-"); // 0-Codigo
                                var AtvCodigoOrig = value[0]; // 0-Codigo
                                var AtvQuant      = parseFloat( GetValorDecimal(value[1]) ); // 1-Quant
                                var AtvPreco      = parseFloat( GetValorDecimal(value[2]) ); // 2-Preco Atual
                                var AtvTotal      = parseFloat( GetValorDecimal(value[3]) ); // 3-Total Atual
                                var AtvNota       = parseFloat( GetValorDecimal(value[4]) ); // 4-Nota Salva
                                var AtvId         = value[5]; // 5-Id'Ativo
                                var AtvTpInvest   = value[6]; // 6-TipoInvest
                                var PercentAtual  = 0.00;

                                if ( AtvTpInvest == 'CRIPTO' ) {
                                    AtvQuant = parseFloat( GetValorDecimalMaior(value[1]) ); // 1-Quant
                                    AtvPreco = parseFloat( GetValorDecimalMaior(value[2]) ); // 2-Preco Atual
                                }
    
                                if ( AtvNota == "" ) AtvNota = "0";
                                if ( (AtvTotal > 0.00) && (TotalInvest > 0.00) ) PercentAtual = ( AtvTotal / TotalInvest ) * 100;
                                if ( PercentAtual > 0.00 ) PercentAtual = Math.floor( PercentAtual * 100 ) / 100;     
                                
                                if ( UltimaNota != AtvNota ){
                                    UltimaNota = AtvNota;
                                    content += '    <tr class="bg-dark"> ';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;" class="font-weight-bold"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; " class="border: 0px; font-weight-bold"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;"> </td>';
                                    content += '      <td style="border: 0px; " bgcolor="#FFFFFF"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; "> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;"> </td>';
                                    content += '      <td style="border: 0px;" bgcolor="#FFFFFF"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;" align="center"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; "> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; "> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;"> </td>';
                                    content += '      <td style="border: 0px" bgcolor="#FFFFFF"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; "> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;"> </td>';
                                    content += '    </tr>';  
                                } //  if ( UltimaNota != AtvNota ){                           
    
                                content += '    <tr class="text-center" id="LinhaPortfBalanc'+AtvCodigo+'"> ';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;" class="font-weight-bold">'+(AtvTpInvest == "ACAO" ? "AÇÃO": AtvTpInvest)+'</td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; " class="border: 0px; font-weight-bold">'+AtvCodigoOrig+'</td>';
                                if ( AtvTpInvest == 'CRIPTO' ){
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;">R$ '+fMascaraValorSemLimite(AtvPreco)+'</td>';
                                    content += '      <td style="border: 0px; " bgcolor="#FFFFFF"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;">'+fMascaraValorSemLimite(AtvQuant)+'</td>';
                                } else {
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;">R$ '+fMascaraValor(AtvPreco)+'</td>';
                                    content += '      <td style="border: 0px; " bgcolor="#FFFFFF"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;">'+colcarFormacataoInteiro(AtvQuant)+'</td>';
                                }
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; ">R$ '+fMascaraValor(AtvTotal)+'</td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;">'+fMascaraValor(PercentAtual)+'%</td>';
                                content += '      <td style="border: 0px;" bgcolor="#FFFFFF"> </td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;" align="center">';
                                //content += '          <div class="input-group number-spinner" > ';
                                //content += '            <div class="input-group-prepend"> <a class="btn btn-sm btn-danger btn-simple" title="" href="javascript:void(0);" onclick="fDimunuirNota(\''+urlPadrao+'\', \''+AtvCodigo+'\');"> <i class="fa fa-minus fa-lg"></i></a></div> ';
                               // content += '            <a style="font-size:8px; width:5px; height:5px;" class="btn btn-primary btn-icon  btn-icon-mini btn-round" title="" href="javascript:void(0);" onclick="fDimunuirNota(\''+urlPadrao+'\', \''+AtvCodigo+'\');"> <i class="fa fa-minus fa-lg"></i> </a> ';
                                //content += '            <span class="badge badge-danger"> <i class="fa fa-minus fa-lg"></i> </span>';
                                content += '            <input type="number" min="0" max="100" step="1" maxlength="6" required '+ //required
                                                            ' id="txtPortfBalancNotasPercent'+AtvCodigo+'" '+
                                                            ' name="txtPortfBalancNotasPercent'+AtvCodigo+'" '+
                                                            //' onkeyup="fCalcularBalanceNotas(\''+urlPadrao+'\')" '+
                                                            // ' onblur="fCalcularBalanceNotas(\''+urlPadrao+'\')" '+
                                                            ' onchange="fCalcularBalanceNotas(\''+urlPadrao+'\')" '+
                                                            ' style="font-size:12px; width:80px; height:25px;" '+
                                                            ' class="DivPortfBalancNotas form-control text-center" '+ 
                                                            ' data-id="'+AtvId+'" '+
                                                            ' data-codigo="'+AtvCodigo+'" '+
                                                            ' data-tipoInvest="'+AtvTpInvest+'" '+
                                                            ' data-preco="'+AtvPreco+'" '+
                                                            ' data-quant="'+AtvQuant+'" '+
                                                            ' data-percent="'+PercentAtual+'" '+ 
                                                            ' data-nota="'+AtvNota+'" '+ 
                                                            ' data-total="'+AtvTotal+'" '+
                                                            ' data-totalinvest="'+TotalInvest+'" '+
                                                            ' value="'+AtvNota+'" '+
                                                            '> ';
                                //content += '            <div class="input-group-prepend"> <a class="btn btn-sm btn-success btn-simple" title="" href="javascript:void(0);" onclick="fAumentarNota(\''+urlPadrao+'\',\''+AtvCodigo+'\');"> <i class="fa fa-plus fa-lg"></i> </a> </div> ';
                                //content += '          </div> ';
                                content += '      </td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; "> <span id="txtPortfBalancNotasQtde'+AtvCodigo+'">0</span> </td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; ">R$ <span id="txtPortfBalancNotasTot'+AtvCodigo+'">0,00</span></td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;"><span id="txtPortfBalancNotasPrct'+AtvCodigo+'">0,00</span>%</td>';
                                content += '      <td style="border: 0px" bgcolor="#FFFFFF"> </td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;"> <span id="txtPortfBalancNotasStatus'+AtvCodigo+'"> </span></td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; "> <span id="txtPortfBalancNotasQtdeDif'+AtvCodigo+'">0</span> </td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;">R$ <span id="txtPortfBalancNotasDif'+AtvCodigo+'">0,00</span></td>';
                                content += '    </tr>';  
                            });                        
    
                            content += '    <tr class="text-center bg-dark text-white"> ';
                            content += '      <td style="border: 0px; border-left: 1px solid black; "></td>';
                            content += '      <td style="border: 0px;"> </td>';
                            content += '      <td style="border: 0px; border-right: 1px solid black; "> </td>';
                            content += '      <td style="border: 0px;" bgcolor="#FFFFFF" > </td>';
                            content += '      <td style="border: 0px; border-left: 1px solid black; "> </td>';
                            content += '      <td style="border: 0px;"  class="font-weight-bold"> R$ '+fMascaraValor(TotalInvest)+'</td>';
                            content += '      <td style="border: 0px; border-right: 1px solid black; "> </td>';
                            content += '      <td style="border: 0px;" bgcolor="#FFFFFF" > </td>';
                            content += '      <td style="border: 0px; border-left: 1px solid black; "  class="font-weight-bold"> <span id="txtPortfBalancNotasNota">0</span> </td>';
                            content += '      <td style="border: 0px;"> </td>';
                            content += '      <td style="border: 0px;"  class="font-weight-bold"> R$ <span id="txtPortfBalancNotasTot">0,00</span> </td>';
                            content += '      <td style="border: 0px; border-right: 1px solid black; "  class="font-weight-bold"> <span id="txtPortfBalancNotasPerct" style="font-size: 10px;" >0,00</span>% </td>';
                            content += '      <td style="border: 0px;" bgcolor="#FFFFFF" > </td>';
                            content += '      <td style="border: 0px; width:30px; border-left: 1px solid black; ">  </td>';
                            content += '      <td style="border: 0px;"> </td>';
                            content += '      <td style="border: 0px; border-right: 1px solid black; "> </td>';
                            content += '    </tr>'; 
    
                            content += '    <tr class="text-center bg-dark text-white"> ';
                            content += '      <td style="border: 0px; border-top: 1px solid black; border-left: 1px solid black; " class="font-weight-bold">Tipo</td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black;" class="font-weight-bold">Código</td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; border-right: 1px solid black; " class="font-weight-bold">Preço</td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF" > </td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; border-left: 1px solid black; " class="font-weight-bold"> Quant. </td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black;" class="font-weight-bold"> Total</td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black;border-right: 1px solid black; " class="font-weight-bold"> % Atual</td>';
                            content += '      <td style="border: 0px; "  bgcolor="#FFFFFF" > </td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black;border-left: 1px solid black; " class="font-weight-bold"> Nota</td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black;" class="font-weight-bold"> Quant. </td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black;" class="font-weight-bold"> Total </td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black;border-right: 1px solid black; " class="font-weight-bold"> % Definido</td>';
                            content += '      <td style="border: 0px; "  bgcolor="#FFFFFF" > </td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; width:30px; border-left: 1px solid black; " class="font-weight-bold"> Status </td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black;" class="font-weight-bold"> Quant. </td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; border-right: 1px solid black; " class="font-weight-bold"> Total </td>';
                            content += '    </tr>';   
    
                            content += '    <tr class="text-center bg-dark text-white"> ';
                            content += '      <td style="border: 0px; border: 1px solid black;" colspan="3" class="font-weight-bold">ATIVO</td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF" > </td>';
                            content += '      <td style="border: 0px; border: 1px solid black;" colspan="3" class="font-weight-bold">PORTFÓLIO ATUAL</td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF"> </td>';
                            content += '      <td style="border: 0px; border: 1px solid black;" colspan="4" class="font-weight-bold">PORTFÓLIO AJUSTADO</td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF" > </td>';
                            content += '      <td style="border: 0px; border: 1px solid black;" colspan="3" class="font-weight-bold">RESULTADO</td>';
                            content += '    </tr>';   
                            
                            content += '  </tbody>';
                            content += '</table>';
                            content += '</div>';
                            
                            DivBalanceNotas.html("");
                            DivBalanceNotas.html( content );	
    
                            fCalcularBalanceNotas( urlPadrao );
                            finalizarAnimacaoPesquisaBalanceNotas();
                            return true;
                        }
    
                        finalizarAnimacaoPesquisaBalanceNotas();
                        //fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_AVISO, 'Sem Dados para Exibir!'); 
                        return true;
                        
                    } else {
                        finalizarAnimacaoPesquisaBalanceNotas();
                        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, mensagem); 
                        return;
                    }
                    
                },
                error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
                    finalizarAnimacaoPesquisaBalanceNotas();
                    fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText //MSG_ALERTA_ERRO
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
            //fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
        });

    } catch (e) {
        finalizarAnimacaoPesquisaBalanceNotas();
		fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fCalcularBalanceNotas( urlPadrao ) {
    try {

         promise = new Promise( (resolve, reject) => {
    
            fLimparAreaAlerta("AreaAlertaPrincAnaliseBalance");

            var BalancPercent   = 0.00;
            var BalancTotal     = 0.00;
            var BalancTotalNota = 0.00;
    
            var TxtBalanceNotas_TotAtual  = 0.00;
            var TxtBalanceNotas_TotAjuste = 0.00;
    
            var TxtBalanceNotas_TotAtualAcao   = 0.00;
            var TxtBalanceNotas_TotAjusteAcao  = 0.00;
    
            var TxtBalanceNotas_TotAtualFII   = 0.00;
            var TxtBalanceNotas_TotAjusteFII  = 0.00;
    
            var TxtBalanceNotas_TotAtualETF   = 0.00;
            var TxtBalanceNotas_TotAjusteETF  = 0.00;

            var TxtBalanceNotas_TotAtualBDR   = 0.00;
            var TxtBalanceNotas_TotAjusteBDR  = 0.00;

            var TxtBalanceNotas_TotAtualCRIPTO   = 0.00;
            var TxtBalanceNotas_TotAjusteCRIPTO  = 0.00;
    
            $.each( $( ".DivPortfBalancNotas" ), function() {
                var AtvCodigo    = $(this).data("codigo");
                var AtvNotaCalc  = parseFloat( GetValorDecimal( $("#txtPortfBalancNotasPercent"+AtvCodigo).val() ) );
                BalancTotalNota += AtvNotaCalc; 
            });
    
            $.each( $( ".DivPortfBalancNotas" ), function() {
                
                // //var AtvId             = $(this).data("id");
                var AtvCodigo         = $(this).data("codigo");
                var AtvTpInvest       = $(this).data("tipoinvest");
                var AtvPreco          = $(this).data("preco");
                var AtvQuantOr        = $(this).data("quant");
                var AtvNotaOr         = $(this).data("nota");
                var AtvTotal          = $(this).data("total");
                var TotalInvest       = $(this).data("totalinvest");
                var AtvNotaCalc       = parseInt( $("#txtPortfBalancNotasPercent"+AtvCodigo).val() );
                var AtvQuantCalc      = 0.00;
                var TotalCalcSReal    = 0.00;
                var PercntCalcSReal   = 0.00;
                var AtvTotalDif       = 0.00;
                var AtvQuantDif       = 0.00;
                var AtvStatusDif      = "NDA";
    
                if ( (AtvNotaCalc > 0) && (TotalInvest > 0.00) ) 
                    TotalCalcSReal = ( TotalInvest / BalancTotalNota ) * AtvNotaCalc
    
                 if ( (TotalCalcSReal > 0.00) && (AtvPreco > 0.00) ) {
                    if ( AtvTpInvest == 'CRIPTO' ){
                         AtvQuantCalc = TotalCalcSReal / AtvPreco;
                    } else {
                         AtvQuantCalc = Math.floor( TotalCalcSReal / AtvPreco );
                    }
                 }
    
                if ( AtvQuantCalc > 0 ) 
                    TotalCalcSReal = AtvQuantCalc * AtvPreco;
    
                if ( (TotalCalcSReal > 0.00) && (TotalInvest > 0.00) ) 
                    PercntCalcSReal = ( TotalCalcSReal / TotalInvest ) * 100;
    
                if ( AtvTotal > TotalCalcSReal ) { 
                    AtvTotalDif  = AtvTotal - TotalCalcSReal; 
                    AtvQuantDif  = AtvQuantOr - AtvQuantCalc;
                    AtvStatusDif = "VENDER";  
                 }
    
                if ( AtvTotal < TotalCalcSReal ) { 
                     AtvTotalDif  = TotalCalcSReal - AtvTotal; 
                     AtvQuantDif  = AtvQuantCalc - AtvQuantOr;
                     AtvStatusDif = "COMPRAR"; 
                }
    
                if ( (AtvQuantDif == 0.0) || (AtvQuantOr == AtvQuantDif) ) {
                    AtvQuantCalc   = AtvQuantOr; 
                    TotalCalcSReal = AtvTotal; 
                    AtvTotalDif    = 0.00;
                    AtvQuantDif    = 0.00;
                    AtvStatusDif   = "NDA";
               }
               
               if ( AtvNotaCalc == 0.00)  {
                    AtvQuantCalc   = 0.00;
                    TotalCalcSReal = 0.00;
                    AtvTotalDif    = 0.00;
                    AtvQuantDif    = 0.00;
                    AtvStatusDif   = "NDA";
               }

                $("#txtPortfBalancNotasTot"+AtvCodigo).html( fMascaraValor(TotalCalcSReal) );
                $("#txtPortfBalancNotasPrct"+AtvCodigo).html( fMascaraValor(PercntCalcSReal) );
                if ( AtvTpInvest == 'CRIPTO' ){
                    $("#txtPortfBalancNotasQtde"+AtvCodigo).html( fMascaraValorSemLimite(AtvQuantCalc) );
                } else {
                    $("#txtPortfBalancNotasQtde"+AtvCodigo).html( colcarFormacataoInteiro(AtvQuantCalc) );
                }
                
                $("#txtPortfBalancNotasDif"+AtvCodigo).html( fMascaraValor(AtvTotalDif) );
                $("#txtPortfBalancNotasStatus"+AtvCodigo).html( AtvStatusDif );
                if ( AtvTpInvest == 'CRIPTO' ){
                    $("#txtPortfBalancNotasQtdeDif"+AtvCodigo).html( fMascaraValorSemLimite(AtvQuantDif) );
                } else {
                    $("#txtPortfBalancNotasQtdeDif"+AtvCodigo).html( colcarFormacataoInteiro(AtvQuantDif) );
                }
                
                $("#txtPortfBalancNotasStatus"+AtvCodigo).removeClass("text-muted");	
                $("#txtPortfBalancNotasStatus"+AtvCodigo).removeClass("text-success");	
                $("#txtPortfBalancNotasStatus"+AtvCodigo).removeClass("text-danger");	
                if ( AtvStatusDif   == "NDA"     ) $("#txtPortfBalancNotasStatus"+AtvCodigo).addClass('text-muted');
                if ( AtvStatusDif   == "COMPRAR" ) $("#txtPortfBalancNotasStatus"+AtvCodigo).addClass('text-success');
                if ( AtvStatusDif   == "VENDER"  ) $("#txtPortfBalancNotasStatus"+AtvCodigo).addClass('text-danger');
    
                BalancPercent   += PercntCalcSReal;
                BalancTotal     += TotalCalcSReal;    
    
                TxtBalanceNotas_TotAtual += AtvTotal;
                if ( AtvTpInvest == "ACAO"   ) TxtBalanceNotas_TotAtualAcao   += AtvTotal;
                if ( AtvTpInvest == "FII"    ) TxtBalanceNotas_TotAtualFII    += AtvTotal;
                if ( AtvTpInvest == "ETF"    ) TxtBalanceNotas_TotAtualETF    += AtvTotal;
                if ( AtvTpInvest == "BDR"    ) TxtBalanceNotas_TotAtualBDR    += AtvTotal;
                if ( AtvTpInvest == "CRIPTO" ) TxtBalanceNotas_TotAtualCRIPTO += AtvTotal;
    
                TxtBalanceNotas_TotAjuste += TotalCalcSReal;
                if ( AtvTpInvest == "ACAO"   ) TxtBalanceNotas_TotAjusteAcao   += TotalCalcSReal;
                if ( AtvTpInvest == "FII"    ) TxtBalanceNotas_TotAjusteFII    += TotalCalcSReal;
                if ( AtvTpInvest == "ETF"    ) TxtBalanceNotas_TotAjusteETF    += TotalCalcSReal;
                if ( AtvTpInvest == "BDR"    ) TxtBalanceNotas_TotAjusteBDR    += TotalCalcSReal;
                if ( AtvTpInvest == "CRIPTO" ) TxtBalanceNotas_TotAjusteCRIPTO += TotalCalcSReal;
    
            });
    
            $("#txtPortfBalancNotasPerct").html( fMascaraValor(BalancPercent) ); 
            $("#txtPortfBalancNotasTot").html(   fMascaraValor(BalancTotal)   ); 
            $("#txtPortfBalancNotasNota").html(  BalancTotalNota              ); 
            
            fAtualizarDadosTituloBalanceNotas( 
                TxtBalanceNotas_TotAtual, TxtBalanceNotas_TotAjuste, 
                TxtBalanceNotas_TotAtualAcao, TxtBalanceNotas_TotAjusteAcao, 
                TxtBalanceNotas_TotAtualFII, TxtBalanceNotas_TotAjusteFII, 
                TxtBalanceNotas_TotAtualETF, TxtBalanceNotas_TotAjusteETF,
                TxtBalanceNotas_TotAtualBDR, TxtBalanceNotas_TotAjusteBDR,
                TxtBalanceNotas_TotAtualCRIPTO, TxtBalanceNotas_TotAjusteCRIPTO
            );
    
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
        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fDividirValoresBalanceNotas( urlPadrao ) {
    try {

        fLimparAreaAlerta("AreaAlertaPrincAnaliseBalance");
     
        $.each( $( ".DivPortfBalancNotas" ), function() {
            var AtvCodigo = $(this).data("codigo");
            $("#txtPortfBalancNotasPercent"+AtvCodigo).val("1");
        });

        fCalcularBalanceNotas( urlPadrao ) ;

    } catch (e) {
        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fResetarValoresBalanceNotas( urlPadrao ) {
    try {

         promise = new Promise( (resolve, reject) => {

            fLimparAreaAlerta("AreaAlertaPrincAnaliseBalance");

            $.each( $( ".DivPortfBalancNotas" ), function() {
                var AtvCodigo = $(this).data("codigo");
                var AtvNotaOr = $(this).data("nota");
                $("#txtPortfBalancNotasPercent"+AtvCodigo).val(AtvNotaOr);
            });
    
            fCalcularBalanceNotas( urlPadrao ) ;

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
        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fLimparValoresBalanceNotas( urlPadrao ) {
    try {
            
         promise = new Promise( (resolve, reject) => {

            fLimparAreaAlerta("AreaAlertaPrincAnaliseBalance");

            $.each( $( ".DivPortfBalancNotas" ), function() {
                var AtvCodigo = $(this).data("codigo");
                $("#txtPortfBalancNotasPercent"+AtvCodigo).val("0");
            });
            
            fCalcularBalanceNotas( urlPadrao ) ;

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
        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fSalvarValoresBalanceNotas( urlPadrao ) {
    try {
            
         promise = new Promise( (resolve, reject) => {

            fLimparAreaAlerta("AreaAlertaPrincAnaliseBalance");

            var lista = [];
            $.each( $( ".DivPortfBalancNotas" ), function() {
                var AtvCodigo   = $(this).data("codigo");
                var AtvTpInvest = $(this).data("tipoinvest");
                var AtvNota     = $("#txtPortfBalancNotasPercent"+AtvCodigo).val();
                lista.push({ TipoInvest : AtvTpInvest, CodAtivo : AtvCodigo.replace("-", "/"), Nota : AtvNota });
            });
            
            var iLen = lista.length;        
            if( iLen <= 0 ){
                fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_AVISO, 'Sem Dados para Salvar!'); 
                return false;
            }	
            
            $.ajax({
                cache   : "false",
                dataType: "json",
                async   : true,
                type    : "POST",
                url     : urlPadrao + "Analise/salvarBalanceNotas", 
                data    : { lista: lista },
                success: function(result) {  
                
                    var resultado = result.data.Resultado; 
                    var mensagem  = result.data.Mensagem; 
                    
                    if (resultado == "NSESSAO") {
                        $(location).attr('href', urlPadrao + '/login');
                        return false;
                    } else if (resultado == "NOK") {
                        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_AVISO, mensagem); 
                        return;
                    } else if (resultado == "FALHA") {
                        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, mensagem); 
                        return;
                    } else if (resultado == "OK") {
                        fCarregarGridBalanceNotas( urlPadrao );
                        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
                    } else {
                        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, mensagem); 
                        return;
                    }
                    
                },
                error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
                    fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText //MSG_ALERTA_ERRO
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
            //fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
        });

    } catch (e) {
        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}