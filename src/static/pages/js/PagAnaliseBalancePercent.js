
async function fLimparGridBalancePercent( urlPadrao ){ 

     promise = new Promise( (resolve, reject) => {

        fLimparAreaAlerta("AreaAlertaPrincAnaliseBalance");
        $("#DivBalancePercentGrid").html("");

        var TxtBalancePercent_TotAtual  = 0.00;
        var TxtBalancePercent_TotAjuste = 0.00;

        var TxtBalancePercent_TotAtualAcao   = 0.00;
        var TxtBalancePercent_TotAjusteAcao  = 0.00;

        var TxtBalancePercent_TotAtualFII   = 0.00;
        var TxtBalancePercent_TotAjusteFII  = 0.00;

        var TxtBalancePercent_TotAtualETF   = 0.00;
        var TxtBalancePercent_TotAjusteETF  = 0.00;

        var TxtBalancePercent_TotAtualBDR   = 0.00;
        var TxtBalancePercent_TotAjusteBDR  = 0.00;

        var TxtBalancePercent_TotAtualCRIPTO   = 0.00;
        var TxtBalancePercent_TotAjusteCRIPTO  = 0.00;

        fAtualizarDadosTituloBalancePercent(
            TxtBalancePercent_TotAtual, TxtBalancePercent_TotAjuste,
            TxtBalancePercent_TotAtualAcao, TxtBalancePercent_TotAjusteAcao,
            TxtBalancePercent_TotAtualFII, TxtBalancePercent_TotAjusteFII,
            TxtBalancePercent_TotAtualETF, TxtBalancePercent_TotAjusteETF,
            TxtBalancePercent_TotAtualBDR, TxtBalancePercent_TotAjusteBDR,
            TxtBalancePercent_TotAtualCRIPTO, TxtBalancePercent_TotAjusteCRIPTO
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

async function fAtualizarDadosTituloBalancePercent( TxtBalancePercent_TotAtual, TxtBalancePercent_TotAjuste, 
                                              TxtBalancePercent_TotAtualAcao, TxtBalancePercent_TotAjusteAcao, 
                                              TxtBalancePercent_TotAtualFII, TxtBalancePercent_TotAjusteFII, 
                                              TxtBalancePercent_TotAtualETF, TxtBalancePercent_TotAjusteETF,
                                              TxtBalancePercent_TotAtualBDR, TxtBalancePercent_TotAjusteBDR,
                                              TxtBalancePercent_TotAtualCRIPTO, TxtBalancePercent_TotAjusteCRIPTO
                                            ){ 

     promise = new Promise( (resolve, reject) => {

        $("#TxtBalancePercent_TotAtual").html(  "R$ "+fMascaraValor(TxtBalancePercent_TotAtual) );
        $("#TxtBalancePercent_TotAjuste").html( "R$ "+fMascaraValor(TxtBalancePercent_TotAjuste) );    
    
        var TxtBalancePercent_PercAtualAcao  = 0.00;
        if ( TxtBalancePercent_TotAtual  > 0.00 && TxtBalancePercent_TotAtualAcao > 0.00  ) TxtBalancePercent_PercAtualAcao  = ( TxtBalancePercent_TotAtualAcao  / TxtBalancePercent_TotAtual  ) * 100;
        $("#TxtBalancePercent_TotAtualAcao").html(  "R$ "+fMascaraValor(TxtBalancePercent_TotAtualAcao)+" ("+fMascaraValor(TxtBalancePercent_PercAtualAcao)+"%)");
    
        var TxtBalancePercent_PercAjusteAcao = 0.00;
        if ( TxtBalancePercent_TotAjuste > 0.00 && TxtBalancePercent_TotAjusteAcao > 0.00 ) TxtBalancePercent_PercAjusteAcao = ( TxtBalancePercent_TotAjusteAcao / TxtBalancePercent_TotAjuste ) * 100;
        $("#TxtBalancePercent_TotAjusteAcao").html( "R$ "+fMascaraValor(TxtBalancePercent_TotAjusteAcao)+" ("+fMascaraValor(TxtBalancePercent_PercAjusteAcao)+"%)");   
    
        var TxtBalancePercent_PercAtualFII  = 0.00;
        if ( TxtBalancePercent_TotAtual  > 0.00 && TxtBalancePercent_TotAtualFII  > 0.00 ) TxtBalancePercent_PercAtualFII  = ( TxtBalancePercent_TotAtualFII   / TxtBalancePercent_TotAtual  ) * 100;
        $("#TxtBalancePercent_TotAtualFII").html(   "R$ "+fMascaraValor(TxtBalancePercent_TotAtualFII)+" ("+fMascaraValor(TxtBalancePercent_PercAtualFII)+"%)");
    
        var TxtBalancePercent_PercAjusteFII = 0.00;
        if ( TxtBalancePercent_TotAjuste > 0.00 && TxtBalancePercent_TotAjusteFII > 0.00 ) TxtBalancePercent_PercAjusteFII = ( TxtBalancePercent_TotAjusteFII / TxtBalancePercent_TotAjuste ) * 100;
        $("#TxtBalancePercent_TotAjusteFII").html(  "R$ "+fMascaraValor(TxtBalancePercent_TotAjusteFII)+" ("+fMascaraValor(TxtBalancePercent_PercAjusteFII)+"%)"); 

        var TxtBalancePercent_PercAtualETF  = 0.00;
        if ( TxtBalancePercent_TotAtual  > 0.00 && TxtBalancePercent_TotAtualETF  > 0.00 ) TxtBalancePercent_PercAtualETF  = ( TxtBalancePercent_TotAtualETF   / TxtBalancePercent_TotAtual  ) * 100;
        $("#TxtBalancePercent_TotAtualETF").html(   "R$ "+fMascaraValor(TxtBalancePercent_TotAtualETF)+" ("+fMascaraValor(TxtBalancePercent_PercAtualETF)+"%)");
    
        var TxtBalancePercent_PercAjusteETF = 0.00;
        if ( TxtBalancePercent_TotAjuste > 0.00 && TxtBalancePercent_TotAjusteETF > 0.00 ) TxtBalancePercent_PercAjusteETF = ( TxtBalancePercent_TotAjusteETF / TxtBalancePercent_TotAjuste ) * 100;
        $("#TxtBalancePercent_TotAjusteETF").html(  "R$ "+fMascaraValor(TxtBalancePercent_TotAjusteETF)+" ("+fMascaraValor(TxtBalancePercent_PercAjusteETF)+"%)");  

        var TxtBalancePercent_PercAtualBDR  = 0.00;
        if ( TxtBalancePercent_TotAtual  > 0.00 && TxtBalancePercent_TotAtualBDR  > 0.00 ) TxtBalancePercent_PercAtualBDR  = ( TxtBalancePercent_TotAtualBDR   / TxtBalancePercent_TotAtual  ) * 100;
        $("#TxtBalancePercent_TotAtualBDR").html(   "R$ "+fMascaraValor(TxtBalancePercent_TotAtualBDR)+" ("+fMascaraValor(TxtBalancePercent_PercAtualBDR)+"%)");

        var TxtBalancePercent_PercAjusteBDR = 0.00;
        if ( TxtBalancePercent_TotAjuste > 0.00 && TxtBalancePercent_TotAjusteBDR > 0.00 ) TxtBalancePercent_PercAjusteBDR = ( TxtBalancePercent_TotAjusteBDR / TxtBalancePercent_TotAjuste ) * 100;
        $("#TxtBalancePercent_TotAjusteBDR").html(  "R$ "+fMascaraValor(TxtBalancePercent_TotAjusteBDR)+" ("+fMascaraValor(TxtBalancePercent_PercAjusteBDR)+"%)");

        var TxtBalancePercent_PercAtualCRIPTO  = 0.00;
        if ( TxtBalancePercent_TotAtual  > 0.00 && TxtBalancePercent_TotAtualCRIPTO  > 0.00 ) TxtBalancePercent_PercAtualCRIPTO  = ( TxtBalancePercent_TotAtualCRIPTO   / TxtBalancePercent_TotAtual  ) * 100;
        $("#TxtBalancePercent_TotAtualCRIPTO").html(   "R$ "+fMascaraValor(TxtBalancePercent_TotAtualCRIPTO)+" ("+fMascaraValor(TxtBalancePercent_PercAtualCRIPTO)+"%)");

        var TxtBalancePercent_PercAjusteCRIPTO = 0.00;
        if ( TxtBalancePercent_TotAjuste > 0.00 && TxtBalancePercent_TotAjusteCRIPTO > 0.00 ) TxtBalancePercent_PercAjusteCRIPTO = ( TxtBalancePercent_TotAjusteCRIPTO / TxtBalancePercent_TotAjuste ) * 100;
        $("#TxtBalancePercent_TotAjusteCRIPTO").html(  "R$ "+fMascaraValor(TxtBalancePercent_TotAjusteCRIPTO)+" ("+fMascaraValor(TxtBalancePercent_PercAjusteCRIPTO)+"%)");

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

function iniciarAnimacaoPesquisarBalancePercent() {
	// $("#iRefreshBalancePercent").addClass("fa-spin");
    // $("#BtnBalancePercentPesquisar").addClass("disabled");
    $("#txtFiltroBalanceNotaPercent").attr("disabled","disabled");
    fDefinirPadraoSelect('txtFiltroBalanceNotaPercent');
}

function finalizarAnimacaoPesquisaBalancePercent() {
	// $("#iRefreshBalancePercent").removeClass("fa-spin");
	// $("#BtnBalancePercentPesquisar").removeClass("disabled");
    $("#txtFiltroBalanceNotaPercent").removeAttr("disabled");
    fDefinirPadraoSelect('txtFiltroBalanceNotaPercent');
}

async function fCarregarGridBalancePercent( urlPadrao ) {
    try {

         promise = new Promise( (resolve, reject) => {
    
            finalizarAnimacaoPesquisaBalancePercent();
            iniciarAnimacaoPesquisarBalancePercent();
            
            var DivBalancePercent = $("#DivBalancePercentGrid");
            DivBalancePercent.html(""); 
            
            var IdPortfolio = $("#txtFiltroBalanceNotaPercent").val();
    
            $.ajax({
                cache   : "false",
                dataType: "json",
                async   : true,
                type    : "POST",
                url     : urlPadrao + "Analise/gridBalancePercent",
                data: { IdPortfolio: IdPortfolio },
                success: function(result) {  
                    
                    var resultado = result.data.Resultado; 
                    var mensagem  = result.data.Mensagem; 
                    var lista     = result.data.Lista;
    
                    if (resultado == "NSESSAO") {
                        $(location).attr('href', urlPadrao + '/login');
                        return false;
                    } else if (resultado == "NOK") {
                        finalizarAnimacaoPesquisaBalancePercent();
                        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_AVISO, mensagem); 
                        return;
                    } else if (resultado == "FALHA") {
                        finalizarAnimacaoPesquisaBalancePercent();
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
                                var PercentA = parseFloat( GetValorDecimal(a[4])); // 4-PercentualSalvo  
                                var PercentB = parseFloat( GetValorDecimal(b[4])); // 4-PercentualSalvo
                                if(PercentA == PercentB) return 0;
                                return PercentA > PercentB? 1: -1;
                            });
    
                            content += '<div class="table-responsive" id="AreaGrid">';
                            content += '<table class="table table-sm table-hover" style="font-size: 12px" border="0" cellspacing="0" width="100%" style="margin: 0px;">';
                            content += '  <thead>';
                            content += '    <tr class="text-center bg-dark text-white" style="font-size: 12px"> ';
                            content += '      <th style="border: 0px; border: 1px solid black;" colspan="3">ATIVO</th>';
                            content += '      <th style="border: 0px;  " bgcolor="#FFFFFF" style="width:10px"> </th>';
                            content += '      <th style="border: 0px; border: 1px solid black;" colspan="3">PORTFÓLIO ATUAL</th>';
                            content += '      <th style="border: 0px;  " bgcolor="#FFFFFF" style="width:10px"> </th>';
                            content += '      <th style="border: 0px; border: 1px solid black;" colspan="3">PORTFÓLIO AJUSTADO</th>';
                            content += '      <th style="border: 0px;  " bgcolor="#FFFFFF" style="width:10px"> </th>';
                            content += '      <th style="border: 0px; border: 1px solid black;" colspan="3">RESULTADO</th>';
                            content += '    </tr>';  
                            content += '    <tr class="text-center bg-dark text-white"> ';
                            content += '      <th style="border: 0px; width:5px; border-left: 1px solid black; ">Tipo</th>';
                            content += '      <th style="border: 0px; width:5px; ">Código</th>';
                            content += '      <th style="border: 0px; width:5px; border-right: 1px solid black; ">Preço</th>';
                            content += '      <th style="border: 0px; width:5px;" bgcolor="#FFFFFF" > </th>';
                            content += '      <th style="border: 0px; width:5px; border-left: 1px solid black; "> Quant. </th>';
                            content += '      <th style="border: 0px; width:20px;"> Total</th>';
                            content += '      <th style="border: 0px; width:5px; border-right: 1px solid black; "> % Atual</th>';
                            content += '      <th style="border: 0px; width:5px;" bgcolor="#FFFFFF" > </th>';
                            content += '      <th style="border: 0px; width:15px; border-left: 1px solid black; "> % Definido</th>';
                            content += '      <th style="border: 0px; width:5px;"> Quant. </th>';
                            content += '      <th style="border: 0px; width:20px; border-right: 1px solid black; "> Total</th>';
                            content += '      <th style="border: 0px; width:5px;" bgcolor="#FFFFFF" > </th>';
                            content += '      <th style="border: 0px; width:30px; border-left: 1px solid black; "> Status </th>';
                            content += '      <th style="border: 0px; width:5px;"> Quant. </th>';
                            content += '      <th style="border: 0px; width:20px; border-right: 1px solid black; "> Total </th>';
                            content += '    </tr>';  
                            content += '  </thead>';
                            content += '  <tbody>';
    
                            var UltimaPercent = 0.00;
                            $.each(lista, function (index, value) {
    
                                var AtvCodigo     = value[0].replace("/", "-"); // 0-Codigo
                                var AtvCodigoOrig = value[0]; // 0-Codigo
                                var AtvQuant      = parseFloat( GetValorDecimal(value[1]) ); // 1-Quant
                                var AtvPreco      = parseFloat( GetValorDecimal(value[2]) ); // 2-Preco Atual
                                var AtvTotal      = parseFloat( GetValorDecimal(value[3]) ); // 3-Total Atual
                                var AtvPercent    = parseFloat( GetValorDecimal(value[4]) ); // 4-PercentualSalvo
                                var AtvId         = value[5]; // 5-Id'Ativo
                                var AtvTpInvest   = value[6]; // 6-TipoInvest
                                var PercentAtual  = 0.00;

                                if ( AtvTpInvest == 'CRIPTO' ) {
                                    AtvQuant = parseFloat( GetValorDecimalMaior(value[1]) ); // 1-Quant
                                    AtvPreco = parseFloat( GetValorDecimalMaior(value[2]) ); // 2-Preco Atual
                                }
                               
                                if ( (AtvTotal > 0.00) && (TotalInvest > 0.00) ) PercentAtual = ( AtvTotal / TotalInvest ) * 100;
                                if ( PercentAtual > 0.00 ) PercentAtual = Math.floor( PercentAtual * 100 ) / 100;
    
                                if ( UltimaPercent != AtvPercent ){
                                    UltimaPercent = AtvPercent;
                                    content += '    <tr class="bg-dark"> ';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;" class="font-weight-bold"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; "class="font-weight-bold"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;"> </td>';
                                    content += '      <td style="border: 0px; " bgcolor="#FFFFFF"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; "> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;"> </td>';
                                    content += '      <td style="border: 0px;  " bgcolor="#FFFFFF"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;" align="center"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; "> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;"> </td>';
                                    content += '      <td style="border: 0px; " bgcolor="#FFFFFF"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; "> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;"> </td>';
                                    content += '    </tr>';  
                                } //  if ( UltimaPercent != AtvPercent ){       
    
                                content += '    <tr class="text-center" id="LinhaPortfBalanc'+AtvCodigo+'"> ';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;" class="font-weight-bold">'+(AtvTpInvest == "ACAO" ? "AÇÃO": AtvTpInvest)+'</td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; "class="font-weight-bold">'+AtvCodigoOrig+'</td>';
                                if ( AtvTpInvest == 'CRIPTO' ){
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;">R$ '+fMascaraValorSemLimite(AtvPreco)+'</td>';
                                    content += '      <td style="border: 0px;  " bgcolor="#FFFFFF"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;">'+fMascaraValorSemLimite(AtvQuant)+'</td>';
                                } else {
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;">R$ '+fMascaraValor(AtvPreco)+'</td>';
                                    content += '      <td style="border: 0px;  " bgcolor="#FFFFFF"> </td>';
                                    content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;">'+colcarFormacataoInteiro(AtvQuant)+'</td>';
                                }
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; ">R$ '+fMascaraValor(AtvTotal)+'</td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;">'+fMascaraValor(PercentAtual)+'%</td>';
                                content += '      <td style="border: 0px;  " bgcolor="#FFFFFF"> </td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;" align="center">';
                                content += '          <input type="text" maxlength="6" min="0" max="100" step="0.50" required '+ 
                                                            ' id="txtPortfBalancPercent'+AtvCodigo+'" '+
                                                            ' name="txtPortfBalancPercent'+AtvCodigo+'" '+
                                                            ' onkeyup="fCalcularBalancePercent(\''+urlPadrao+'\')" '+
                                                            // ' onblur="fCalcularBalancePercent(\''+urlPadrao+'\')" '+
                                                            // ' onchange="fCalcularBalancePercent(\''+urlPadrao+'\')" '+
                                                            ' style="font-size:12px; width:80px; height:25px;" '+
                                                            ' class="DivPortfBalancPerct form-control text-right" '+
                                                            ' data-id="'+AtvId+'" '+
                                                            ' data-codigo="'+AtvCodigo+'" '+
                                                            ' data-tipoInvest="'+AtvTpInvest+'" '+
                                                            ' data-preco="'+AtvPreco+'" '+
                                                            ' data-quant="'+AtvQuant+'" '+
                                                            ' data-percent="'+PercentAtual+'" '+ //AtvPercent
                                                            ' data-total="'+AtvTotal+'" '+
                                                            ' data-totalinvest="'+TotalInvest+'" '+
                                                            ' value="'+fMascaraValor(AtvPercent)+'" '+
                                                            '> ';
                                content += '      </td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; "> <span id="txtPortfBalancQtde'+AtvCodigo+'">0</span> </td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;">R$ <span id="txtPortfBalancTot'+AtvCodigo+'">0,00</span></td>';
                                content += '      <td style="border: 0px; " bgcolor="#FFFFFF"> </td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-left: 1px solid black;"> <span id="txtPortfBalancStatus'+AtvCodigo+'"> </span></td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; "> <span id="txtPortfBalancQtdeDif'+AtvCodigo+'">0</span> </td>';
                                content += '      <td style="border: 0px; border-bottom: 1px solid gray; border-right: 1px solid black;">R$ <span id="txtPortfBalancDif'+AtvCodigo+'">0,00</span></td>';
                                content += '    </tr>';  
                            });
                            
                            
                            content += '    <tr class="text-center bg-dark text-white"> ';
                            content += '      <td style="border: 0px; border-left: 1px solid black; "> </td>';
                            content += '      <td style="border: 0px; "> </td>';
                            content += '      <td style="border: 0px; border-right: 1px solid black; "> </td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF" > </td>';
                            content += '      <td style="border: 0px; border-left: 1px solid black;  "> </td>';
                            content += '      <td style="border: 0px; font-size: 11px;" class="font-weight-bold" class="font-weight-bold">R$ '+fMascaraValor(TotalInvest)+'</td>';
                            content += '      <td style="border: 0px; border-right: 1px solid black; "> </td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF" > </td>';
                            content += '      <td style="border: 0px; border-left: 1px solid black; " class="font-weight-bold"> <span id="txtPortfBalancPerct" style="font-size: 10px;" >0,00</span>%</td>';
                            content += '      <td style="border: 0px; "> </td>';
                            content += '      <td style="border: 0px; border-right: 1px solid black; font-size: 11px;" class="font-weight-bold">R$ <span id="txtPortfBalancTot">0,00</span></td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF" > </td>';
                            content += '      <td style="border: 0px; border-left: 1px solid black; "> </td>';
                            content += '      <td style="border: 0px; "> </td>';
                            content += '      <td style="border: 0px; border-right: 1px solid black; "> </td>';
                            content += '    </tr>';  
                            
                            content += '    <tr class="text-center bg-dark text-white"> ';
                            content += '      <td style="border: 0px; border-top: 1px solid black; border-left: 1px solid black; " class="font-weight-bold">Tipo</th>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; " class="font-weight-bold">Código</td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; border-right: 1px solid black; " class="font-weight-bold">Preço</td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF" > </th>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; border-left: 1px solid black; " class="font-weight-bold"> Quant. </td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; " class="font-weight-bold"> Total</td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; border-right: 1px solid black; " class="font-weight-bold"> % Atual</td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF" > </th>';
                            content += '      <td style="border: 0px; border-top: 1px solid black;  border-left: 1px solid black; " class="font-weight-bold"> % Definido</td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; " class="font-weight-bold"> Quant. </td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; border-right: 1px solid black; " class="font-weight-bold"> Total</td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF" > </th>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; border-left: 1px solid black; " class="font-weight-bold"> Status </td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; ;" class="font-weight-bold"> Quant. </td>';
                            content += '      <td style="border: 0px; border-top: 1px solid black; border-right: 1px solid black; " class="font-weight-bold"> Total </td>';
                            content += '    </tr>';  
    
                            content += '    <tr class="text-center bg-dark text-white"> ';
                            content += '      <td style="border: 0px; border: 1px solid black;" colspan="3" class="font-weight-bold">ATIVO</td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF" > </th>';
                            content += '      <td style="border: 0px; border: 1px solid black;" colspan="3" class="font-weight-bold">PORTFÓLIO ATUAL</td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF" > </th>';
                            content += '      <td style="border: 0px; border: 1px solid black;" colspan="3" class="font-weight-bold">PORTFÓLIO AJUSTADO</td>';
                            content += '      <td style="border: 0px; " bgcolor="#FFFFFF" > </th>';
                            content += '      <td style="border: 0px; border: 1px solid black;" colspan="3" class="font-weight-bold">RESULTADO</td>';
                            content += '    </tr>'; 
                            
                            content += '  </tbody>';
                            content += '</table>';
                            content += '</div>';
                            
                            DivBalancePercent.html("");
                            DivBalancePercent.html( content );	
    
                            fCalcularBalancePercent( urlPadrao );
                            finalizarAnimacaoPesquisaBalancePercent();
                            return true;
                        }
    
                        finalizarAnimacaoPesquisaBalancePercent();
                        //fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_AVISO, 'Sem Dados para Exibir!'); 
                        return true;
                        
                    } else {
                        finalizarAnimacaoPesquisaBalancePercent();
                        fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, mensagem); 
                        return;
                    }
                    
                },
                error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
                    finalizarAnimacaoPesquisaBalancePercent();
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
        finalizarAnimacaoPesquisaBalancePercent();
		fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fCalcularBalancePercent( urlPadrao ) {
    try {

         promise = new Promise( (resolve, reject) => {
    
            fLimparAreaAlerta("AreaAlertaPrincAnaliseBalance");

            var BalancPercent = 0.00;
            var BalancTotal   = 0.00;
    
            var TxtBalancePercent_TotAtual  = 0.00;
            var TxtBalancePercent_TotAjuste = 0.00;
    
            var TxtBalancePercent_TotAtualAcao   = 0.00;
            var TxtBalancePercent_TotAjusteAcao  = 0.00;
    
            var TxtBalancePercent_TotAtualFII   = 0.00;
            var TxtBalancePercent_TotAjusteFII  = 0.00;
    
            var TxtBalancePercent_TotAtualETF   = 0.00;
            var TxtBalancePercent_TotAjusteETF  = 0.00;

            var TxtBalancePercent_TotAtualBDR   = 0.00;
            var TxtBalancePercent_TotAjusteBDR  = 0.00;

            var TxtBalancePercent_TotAtualCRIPTO   = 0.00;
            var TxtBalancePercent_TotAjusteCRIPTO  = 0.00;
    
            $.each( $(".DivPortfBalancPerct"), function() {

                //var AtvId             = $(this).data("id");
                var AtvCodigo         = $(this).data("codigo");
                var AtvTpInvest       = $(this).data("tipoinvest");
                var AtvPreco          = $(this).data("preco");
                var AtvQuantOr        = $(this).data("quant");
                var AtvPercentOr      = $(this).data("percent");
                var AtvTotal          = $(this).data("total");
                var TotalInvest       = $(this).data("totalinvest");
                var AtvPercentCalc    = parseFloat( GetValorDecimal( $("#txtPortfBalancPercent"+AtvCodigo).val() ) );
                var TotalCalcSugerido = 0.00;
                var AtvQuantCalc      = 0.00;
                var TotalCalcSReal    = 0.00;
                var AtvTotalDif       = 0.00;
                var AtvQuantDif       = 0.00;
                var AtvStatusDif      = "NDA";

                if ( (AtvPercentCalc > 0.00) && (TotalInvest > 0.00) )
                    TotalCalcSugerido = ( TotalInvest / 100 ) * AtvPercentCalc;

                if ( (TotalCalcSugerido > 0.00) && (AtvPreco > 0.00) ) {
                    if ( AtvTpInvest == 'CRIPTO' ){
                         AtvQuantCalc = TotalCalcSugerido / AtvPreco;
                    } else {
                         AtvQuantCalc = Math.floor( TotalCalcSugerido / AtvPreco );
                    }
                }

                if ( AtvQuantCalc > 0 )
                    TotalCalcSReal = AtvQuantCalc * AtvPreco;

                if ( AtvTotal > TotalCalcSReal ) {
                    AtvTotalDif  = AtvTotal - TotalCalcSReal;
                    if ( AtvTpInvest == 'CRIPTO' ){
                         AtvQuantDif = AtvTotalDif / AtvPreco;
                    } else {
                         AtvQuantDif  = Math.floor( AtvTotalDif / AtvPreco );
                    }
                    AtvStatusDif = "VENDER";
                }

                if ( AtvTotal < TotalCalcSReal ) {
                    AtvTotalDif  = TotalCalcSReal - AtvTotal;
                    if ( AtvTpInvest == 'CRIPTO' ){
                         AtvQuantDif = AtvTotalDif / AtvPreco;
                    } else {
                         AtvQuantDif  = Math.floor( AtvTotalDif / AtvPreco );
                    }
                    AtvStatusDif = "COMPRAR";
                }

                if ( (AtvQuantDif == 0.00)  || (AtvPercentOr == AtvPercentCalc) ) {
                    AtvQuantCalc   = AtvQuantOr;
                    TotalCalcSReal = AtvTotal;
                    AtvTotalDif    = 0.00;
                    AtvQuantDif    = 0.00;
                    AtvStatusDif   = "NDA";
                }

                $("#txtPortfBalancTot"+AtvCodigo).html(     fMascaraValor(TotalCalcSReal) );
                $("#txtPortfBalancDif"+AtvCodigo).html(     fMascaraValor(AtvTotalDif)    );
                $("#txtPortfBalancStatus"+AtvCodigo).html(  AtvStatusDif                  );
                if ( AtvTpInvest == 'CRIPTO' ){
                    $("#txtPortfBalancQtde"+AtvCodigo).html( fMascaraValorSemLimite(AtvQuantCalc) );
                    $("#txtPortfBalancQtdeDif"+AtvCodigo).html( fMascaraValorSemLimite(AtvQuantDif) );
                } else {
                    $("#txtPortfBalancQtde"+AtvCodigo).html( colcarFormacataoInteiro(AtvQuantCalc) );
                    $("#txtPortfBalancQtdeDif"+AtvCodigo).html( colcarFormacataoInteiro(AtvQuantDif) );
                }

                $("#txtPortfBalancStatus"+AtvCodigo).removeClass("text-muted");
                $("#txtPortfBalancStatus"+AtvCodigo).removeClass("text-success");
                $("#txtPortfBalancStatus"+AtvCodigo).removeClass("text-danger");
                if ( AtvStatusDif   == "NDA"     ) $("#txtPortfBalancStatus"+AtvCodigo).addClass('text-muted');
                if ( AtvStatusDif   == "COMPRAR" ) $("#txtPortfBalancStatus"+AtvCodigo).addClass('text-success');
                if ( AtvStatusDif   == "VENDER"  ) $("#txtPortfBalancStatus"+AtvCodigo).addClass('text-danger');

                BalancPercent += AtvPercentCalc;
                BalancTotal   += TotalCalcSReal;

                TxtBalancePercent_TotAtual += AtvTotal;
                if ( AtvTpInvest == "ACAO"   ) TxtBalancePercent_TotAtualAcao   += AtvTotal;
                if ( AtvTpInvest == "FII"    ) TxtBalancePercent_TotAtualFII    += AtvTotal;
                if ( AtvTpInvest == "ETF"    ) TxtBalancePercent_TotAtualETF    += AtvTotal;
                if ( AtvTpInvest == "BDR"    ) TxtBalancePercent_TotAtualBDR    += AtvTotal;
                if ( AtvTpInvest == "CRIPTO" ) TxtBalancePercent_TotAtualCRIPTO += AtvTotal;

                TxtBalancePercent_TotAjuste += TotalCalcSReal;
                if ( AtvTpInvest == "ACAO"   ) TxtBalancePercent_TotAjusteAcao   += TotalCalcSReal;
                if ( AtvTpInvest == "FII"    ) TxtBalancePercent_TotAjusteFII    += TotalCalcSReal;
                if ( AtvTpInvest == "ETF"    ) TxtBalancePercent_TotAjusteETF    += TotalCalcSReal;
                if ( AtvTpInvest == "BDR"    ) TxtBalancePercent_TotAjusteBDR    += TotalCalcSReal;
                if ( AtvTpInvest == "CRIPTO" ) TxtBalancePercent_TotAjusteCRIPTO += TotalCalcSReal;

            });
    
            $("#txtPortfBalancPerct").html( fMascaraValor(BalancPercent) ); 
            $("#txtPortfBalancTot").html(   fMascaraValor(BalancTotal)   ); 
    
            fAtualizarDadosTituloBalancePercent(
                TxtBalancePercent_TotAtual, TxtBalancePercent_TotAjuste,
                TxtBalancePercent_TotAtualAcao, TxtBalancePercent_TotAjusteAcao,
                TxtBalancePercent_TotAtualFII, TxtBalancePercent_TotAjusteFII,
                TxtBalancePercent_TotAtualETF, TxtBalancePercent_TotAjusteETF,
                TxtBalancePercent_TotAtualBDR, TxtBalancePercent_TotAjusteBDR,
                TxtBalancePercent_TotAtualCRIPTO, TxtBalancePercent_TotAjusteCRIPTO
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

async function fDividirValoresBalancePercent( urlPadrao ) {
    try {

         promise = new Promise( (resolve, reject) => {
    
            fLimparAreaAlerta("AreaAlertaPrincAnaliseBalance");

            qtdeAtv = 0;
            $.each( $( ".DivPortfBalancPerct" ), function() {
                qtdeAtv += 1;
            });
            
            if ( qtdeAtv      > 0    ) PercentIdeal = ( 100.00 / qtdeAtv);
            if ( PercentIdeal > 0.00 ) PercentIdeal = Math.floor( PercentIdeal * 100 ) / 100;
    
            $.each( $( ".DivPortfBalancPerct" ), function() {
                var AtvCodigo = $(this).data("codigo");
                $("#txtPortfBalancPercent"+AtvCodigo).val( fMascaraValor(PercentIdeal) );
    
            });
    
            fCalcularBalancePercent( urlPadrao ) ;
    
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

async function fResetarValoresBalancePercent( urlPadrao ) {
    try {

         promise = new Promise( (resolve, reject) => {

            fLimparAreaAlerta("AreaAlertaPrincAnaliseBalance");

            var BalancPercent = 100.00;
            var BalancTotal   = 0.00;
    
            var TxtBalancePercent_TotAtual  = 0.00;
            var TxtBalancePercent_TotAjuste = 0.00;
    
            var TxtBalancePercent_TotAtualAcao   = 0.00;
            var TxtBalancePercent_TotAjusteAcao  = 0.00;
    
            var TxtBalancePercent_TotAtualFII   = 0.00;
            var TxtBalancePercent_TotAjusteFII  = 0.00;
    
            var TxtBalancePercent_TotAtualETF   = 0.00;
            var TxtBalancePercent_TotAjusteETF  = 0.00;

            var TxtBalancePercent_TotAtualBDR   = 0.00;
            var TxtBalancePercent_TotAjusteBDR  = 0.00;

            var TxtBalancePercent_TotAtualCRIPTO   = 0.00;
            var TxtBalancePercent_TotAjusteCRIPTO  = 0.00;
    
            $.each( $( ".DivPortfBalancPerct" ), function() {

                var AtvCodigo    = $(this).data("codigo");
                var AtvTpInvest  = $(this).data("tipoinvest");
                var AtvQuantOr   = $(this).data("quant");
                var AtvPercentOr = $(this).data("percent");
                var AtvTotal     = $(this).data("total");
                var AtvTotalDif  = 0.00;
                var AtvQuantDif  = 0; 
                var AtvStatus    = "NDA";
                BalancTotal      = $(this).data("totalinvest");
    
                $("#txtPortfBalancPercent"+AtvCodigo).val(  fMascaraValor(AtvPercentOr)  );
                $("#txtPortfBalancTot"+AtvCodigo).html(     fMascaraValor(AtvTotal)      );
                
                $("#txtPortfBalancQtde"+AtvCodigo).html(    AtvQuantOr.toLocaleString()  ); 
                $("#txtPortfBalancDif"+AtvCodigo).html(     fMascaraValor(AtvTotalDif)   );  
                $("#txtPortfBalancQtdeDif"+AtvCodigo).html( AtvQuantDif.toLocaleString() ); 
                $("#txtPortfBalancStatus"+AtvCodigo).html(  AtvStatus                    );
                
                $("#txtPortfBalancStatus"+AtvCodigo).removeClass("text-success");	
                $("#txtPortfBalancStatus"+AtvCodigo).removeClass("text-danger");
                $("#txtPortfBalancStatus"+AtvCodigo).addClass('text-muted');            
    
                TxtBalancePercent_TotAtual += AtvTotal;
                if ( AtvTpInvest == "ACAO" ) TxtBalancePercent_TotAtualAcao += AtvTotal;
                if ( AtvTpInvest == "FII"  ) TxtBalancePercent_TotAtualFII  += AtvTotal;
                if ( AtvTpInvest == "ETF"  ) TxtBalancePercent_TotAtualETF  += AtvTotal;
                if ( AtvTpInvest == "BDR"  ) TxtBalancePercent_TotAtualBDR  += AtvTotal;
                if ( AtvTpInvest == "CRIPTO"  ) TxtBalancePercent_TotAtualCRIPTO  += AtvTotal;
    
                TxtBalancePercent_TotAjuste += AtvTotal;
                if ( AtvTpInvest == "ACAO" ) TxtBalancePercent_TotAjusteAcao += AtvTotal;
                if ( AtvTpInvest == "FII"  ) TxtBalancePercent_TotAjusteFII  += AtvTotal;
                if ( AtvTpInvest == "ETF"  ) TxtBalancePercent_TotAjusteETF  += AtvTotal;
                if ( AtvTpInvest == "BDR"  ) TxtBalancePercent_TotAjusteBDR  += AtvTotal;
                if ( AtvTpInvest == "CRIPTO"  ) TxtBalancePercent_TotAjusteCRIPTO  += AtvTotal;
    
            });

            $("#txtPortfBalancPerct").html( fMascaraValor(BalancPercent) ); 
            $("#txtPortfBalancTot").html(   fMascaraValor(BalancTotal)   ); 
            // fCalcularBalancePercent( urlPadrao ) ;
            
            fAtualizarDadosTituloBalancePercent( 
                    TxtBalancePercent_TotAtual, 
                    TxtBalancePercent_TotAjuste, 
                    TxtBalancePercent_TotAtualAcao, 
                    TxtBalancePercent_TotAjusteAcao, 
                    TxtBalancePercent_TotAtualFII, 
                    TxtBalancePercent_TotAjusteFII, 
                    TxtBalancePercent_TotAtualETF, 
                    TxtBalancePercent_TotAjusteETF,
                    TxtBalancePercent_TotAtualBDR,
                    TxtBalancePercent_TotAjusteBDR,
                    TxtBalancePercent_TotAtualCRIPTO,
                    TxtBalancePercent_TotAjusteCRIPTO
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

async function fLimparValoresBalancePercent( urlPadrao ) {
    try {

         promise = new Promise( (resolve, reject) => {
    
            fLimparAreaAlerta("AreaAlertaPrincAnaliseBalance");

            var BalancPercent = 0.00;
            var BalancTotal   = 0.00;
    
            $.each( $( ".DivPortfBalancPerct" ), function() {
                var AtvCodigo    = $(this).data("codigo");
                var AtvQuantOr   = 0;
                var AtvPercentOr = 0.00;
                var AtvTotal     = 0.00;
                var AtvTotalDif  = 0.00;
                var AtvQuantDif  = 0; 
                var AtvStatus    = "NDA";
    
                $("#txtPortfBalancPercent"+AtvCodigo).val(  fMascaraValor(AtvPercentOr)  );
                $("#txtPortfBalancTot"+AtvCodigo).html(     fMascaraValor(AtvTotal)      );
                
                $("#txtPortfBalancQtde"+AtvCodigo).html(    AtvQuantOr.toLocaleString()  ); 
                $("#txtPortfBalancDif"+AtvCodigo).html(     fMascaraValor(AtvTotalDif)   );  
                $("#txtPortfBalancQtdeDif"+AtvCodigo).html( AtvQuantDif.toLocaleString() ); 
                $("#txtPortfBalancStatus"+AtvCodigo).html(  AtvStatus                    );
                
                $("#txtPortfBalancStatus"+AtvCodigo).removeClass("text-success");	
                $("#txtPortfBalancStatus"+AtvCodigo).removeClass("text-danger");
                $("#txtPortfBalancStatus"+AtvCodigo).addClass('text-muted');
    
            });
    
            $("#txtPortfBalancPerct").html( fMascaraValor(BalancPercent) ); 
            $("#txtPortfBalancTot").html(   fMascaraValor(BalancTotal)   ); 
            
            fCalcularBalancePercent( urlPadrao ) ;
    
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

async function fSalvarValoresBalancePercent( urlPadrao ) {
    try {

         promise = new Promise( (resolve, reject) => {
    
            fLimparAreaAlerta("AreaAlertaPrincAnaliseBalance");

            var lista         = [];
            var BalancPercent = 0.00;
    
            $.each( $( ".DivPortfBalancPerct" ), function() {
                var AtvCodigo   = $(this).data("codigo");
                var AtvTpInvest = $(this).data("tipoinvest");
                var AtvPercent  = parseFloat( GetValorDecimal( $("#txtPortfBalancPercent"+AtvCodigo).val() ) );
                //if ( AtvPercent > 0.00 ) AtvPercent = Math.floor( AtvPercent * 100 ) / 100;
                BalancPercent  += AtvPercent;
                lista.push({ TipoInvest : AtvTpInvest, CodAtivo : AtvCodigo.replace("-", "/"), Percent : AtvPercent });
            });
            
            var iLen = lista.length;        
            if( iLen <= 0 ){
                fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_AVISO, 'Sem Dados para Salvar!'); 
                return false;
            }	
            
            if( BalancPercent > 100.00 ){
                fCriarAlerta("AreaAlertaPrincAnaliseBalance",TP_ALERTA_AVISO, 'Porcentagem Total maior que 100%.'); 
                return false;
            }	
            
            $.ajax({
                cache   : "false",
                dataType: "json",
                async   : true,
                type    : "POST",
                url     : urlPadrao + "Analise/salvarBalancePercent",
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
                        fCarregarGridBalancePercent( urlPadrao );
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