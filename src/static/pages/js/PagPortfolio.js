
$(document).ready(function() {
   // $(this).attr("title", ":: TnB - Portfolio ::");
    $("#MnPrincPortfolio").addClass("active open");           
    $("#FormOper input[type=text]").bind("keyup change", function(){ fCalcularPrecoTotal();  fCalcularOperacao();  });
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

                fMontarPagina( urlPadrao );

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

function fMostrarEsconderValores(){
  $(".DivTextValor").toggle();
  $(".DivIconeValor").toggle();
}

async function iniciarAnimacaoPesquisar() {
                
     promise = new Promise( (resolve, reject) => {
                       
       resolve(true);

       $("#iRefresh").addClass("fa-spin");
       $("#btnPortAtualizarPag").addClass("disabled");
       //$("#btnOperLimpar").addClass("disabled");

       // resolve(true);
       // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
    })
    .then( txt => {
        //console.log('Sucesso: ' + txt);
    })
    .catch( txt => {
        fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    });

}

async function finalizarAnimacaoPesquisa() {
                
     promise = new Promise( (resolve, reject) => {
                                   
         resolve(true);

         $("#iRefresh").removeClass("fa-spin");
         $("#btnPortAtualizarPag").removeClass("disabled");
         //$("#btnOperLimpar").removeClass("disabled");

         // resolve(true);
         // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
    })
    .then( txt => {
                   //console.log('Sucesso: ' + txt);
    })
    .catch( txt => {
                   fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    });

}

function fGetAbaIdPortfolio() {
                
    var IdPortfolio = "";

    $("#TabPortfolios li a").each(function () { 
         if ( $(this).hasClass( "active" ) == true ){
             IdPortfolio = $(this).attr('id');
             //$(this).removeClass("text-secondary");
             //$(this).addClass("text-dark");
         }
         else{
             //$(this).removeClass("text-dark");
             //$(this).addClass("text-secondary");
         }
    });

    IdPortfolio = IdPortfolio.replace("AbaPortfolioAcoes",   "");
    IdPortfolio = IdPortfolio.replace("AbaPortfolioFundos",  "");
    IdPortfolio = IdPortfolio.replace("AbaPortfolioIndices", "");
    IdPortfolio = IdPortfolio.replace("AbaPortfolioBdrs",    "");
    IdPortfolio = IdPortfolio.replace("AbaPortfolioCriptos", "");
    IdPortfolio = IdPortfolio.replace("AbaPortfolio",        "");
    IdPortfolio = IdPortfolio.replace("Aba",                 "");
    
    return IdPortfolio;          
}

function fGetAbaTipoPortfolio() {
                
    var TipoPortfolio = "";

    $("#TabPortfolios li a").each(function () { 
         if ( $(this).hasClass( "active" ) == true ){
             TipoPortfolio = $(this).attr('id');
             //$(this).removeClass("text-secondary");
             //$(this).addClass("text-dark");
         }
         else{
             //$(this).removeClass("text-dark");
             //$(this).addClass("text-secondary");
         }
    });

    if ( TipoPortfolio == "AbaPortfolioAcoes"   ) return "ACAO";
    if ( TipoPortfolio == "AbaPortfolioFundos"  ) return "FII";
    if ( TipoPortfolio == "AbaPortfolioIndices" ) return "ETF";
    if ( TipoPortfolio == "AbaPortfolioBdrs"    ) return "BDR";
    if ( TipoPortfolio == "AbaPortfolioCriptos" ) return "CRIPTO";
    return "";
                
}

async function fAbrirModalGraficoPortfolio( urlPadrao, CodAtivo ) {
    try {

         promise = new Promise( (resolve, reject) => {

          if ( CodAtivo.includes('/BRL') ) {
               CodAtivo = "BINANCE:" + CodAtivo.replace('/BRL','BRL')
               new TradingView.widget({
                               "container_id": "DivGraficoProtfTradingView",
                               "width": "100%",
                               "height": "500px",
                               "symbol": CodAtivo,
                               "interval": "D",
                               "timezone": "America/Sao_Paulo",
                               "locale": "br",
                               "theme": "Light",
                               "style": "1",
                               "toolbar_bg": "#f1f3f6",
                               "enable_publishing": false,
                               "allow_symbol_change": true,
                               "gridLineColor": "#E9E9EA",
                               "fontColor": "#83888D",
                               "underLineColor": "#dbeffb",
                               "trendLineColor": "#4bafe9",
                               "activeTickerBackgroundColor": "#EDF0F3",
                               "details": false,
                               "withdateranges": true,
                               "hide_side_toolbar": true,
                               "withdateranges": true,
               });
          } else{
               new TradingView.widget({
                               "container_id": "DivGraficoProtfTradingView",
                               "customer": "bovespa",
                               "width": "100%",
                               "height": "500px",
                               "symbol": CodAtivo,
                               "interval": "D", //"D"
                               "timezone": "America/Sao_Paulo",
                               "locale": "br",
                               "theme": "Light",
                               "style": "1",
                               "toolbar_bg": "#f1f3f6",
                               "enable_publishing": false,
                               "allow_symbol_change": true,
                               "gridLineColor": "#E9E9EA",
                               "fontColor": "#83888D",
                               "underLineColor": "#dbeffb",
                               "trendLineColor": "#4bafe9",
                               "activeTickerBackgroundColor": "#EDF0F3",
                               "details": false,
                               "withdateranges": true,
                               "hide_side_toolbar": true,
                               "withdateranges": true,
                               //"noGraph": true,
                               // "show_popup_button": false,
                               // "popup_width": "1000",
                               // "popup_height": "650",
                               // "calendar": false,
                               // "hotlist": true,
               });
          }
                           
           $('#PopModalGraficoPortfolio').modal({backdrop: 'static'});

          resolve(true);
          // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
        })
        .then( txt => {
          //console.log('Sucesso: ' + txt);
        })
        .catch( txt => {
          fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
        });

    } catch (e) {
         fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fLimparSomenteGrid( urlPadrao ){          
    try {       

            promise = new Promise( (resolve, reject) => {

                 resolve(true);

                 $("th").addClass('text-center');               

                 $('#Grid').dataTable().fnClearTable();
                 $("#Grid").dataTable({ bDestroy: true }).fnDestroy();

                 $('#Grid').DataTable( {                                 
                   oLanguage: fTraduzirGrid(), 
                   aoColumns: [
                                   { bSortable: true, bOrderable: true, sWidth: "40px",  targets:  0 }, //  0-Ativo
                                   { bSortable: true, bOrderable: true, sWidth: "100px", targets:  1 }, //  1-Quant
                                   { bSortable: true, bOrderable: true, sWidth: "100px", targets:  2 }, //  2-Preco Medio
                                   { bSortable: true, bOrderable: true, sWidth: "100px", targets:  3 }, //  3-Preco Atual
                                   { bSortable: true, bOrderable: true, sWidth: "100px", targets:  4 }, //  4-Preco Teto
                                   { bSortable: true, bOrderable: true, sWidth: "120px", targets:  5 }, //  5-Total Invest 
                                   { bSortable: true, bOrderable: true, sWidth: "120px", targets:  6 }, //  6-Total Atual
                                   { bSortable: true, bOrderable: true, sWidth: "120px", targets:  7 }, //  7-Valorização(R$)
                                   { bSortable: true, bOrderable: true, sWidth: "50px",  targets:  8 }, //  8-Valorização(%)
                                   { bSortable: true, bOrderable: true, sWidth: "120px", targets:  9 }, //  9-Total Rendimento
                                   { bSortable: true, bOrderable: true, sWidth: "20px",  targets: 10 }, // 10-Yield on Cost
                                   { visible  : false,                                     targets: 11 }, // 11-Total Aluguel
                                   { visible  : false,                                     targets: 12 }, // 12-IdAtivo
                                   { visible  : false,                                     targets: 13 }, // 13-TipoInvest
                                   { bSortable: false, bOrderable: false, sWidth: "10px",  targets: 14 }  // 14-Acao
                   ],
                   order: [],
                   bFilter: false,
                   bInfo: false,
                   bLengthChange: false,
                   bSearchable: false,
                   bOrderable: true,
                   bSortable: true,
                   bAutoWidth: false,
                   bPaginate: false,
                   bOrdering: true
                 });

                 // resolve(true);
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

async function fLimparPagina( urlPadrao ){        
      
       promise = new Promise( (resolve, reject) => {
                                     
           resolve(true);

           fLimparAreaAlerta("AreaAlertaPrinc");
           fLimparAreaAlerta("AreaAlertaModalCad"); 
           fLimparAreaAlerta("AreaAlertaModalExc");

           $('#btnPortAddAtivo').hide(); 
           $('#btnPortAltPortfolio').hide(); 
           $('#btnPortExcPortfolio').hide();             
           $('#btnPortAddPortfolio').show(); 

           // fLimparTotalizadores( urlPadrao );
           $("#DivPortTotInvest").html(   "R$ 0,00" );
           $("#DivPortTotAtual").html(    "R$ 0,00" );
           $("#DivPortValorizacao").html( "R$ 0,00 <small><em>( 0,00% )</em></small>" );
           $("#DivPortRendimento").html(  "R$ 0,00" );
           $("#DivPortAluguel").html(  "R$ 0,00" );
           $("#DivPortGanhoPerda").html(  "R$ 0,00 <small><em>( 0,00% )</em></small>" );
           $("#DivPortIbovPreco").html(  "0,00 pts" );
           $("#DivPortIbovValoriz").html(  "0,00 <em>( 0,00% )</em></small>" );

           $("#DivPortValorizacao").addClass("text-muted");
           $("#DivPortValorizacao").removeClass("text-success");
           $("#DivPortValorizacao").removeClass("text-danger");               
           $("#DivPortGanhoPerda").addClass("text-muted");                     
           $("#DivPortGanhoPerda").removeClass("text-success");
           $("#DivPortGanhoPerda").removeClass("text-danger");            
           $("#DivPortIbovValoriz").addClass("text-muted");                        
           $("#DivPortIbovValoriz").removeClass("text-success");
           $("#DivPortIbovValoriz").removeClass("text-danger");

           $("#DivGraficoPortGeral").html("");
           $("#DivGridPortfPercent").html("");
           $("#ListaValDia").html("");
           $("#ListaValDiaTotal").html("");
           // $("#ListaIndice").html("");
           // $("#ListaRadar").html("");
           $("#DivGraficoPortCarteira").html("");
           $("#DivGraficoPortValorLucroPrejuizo").html("");
           $("#DivGraficoPortPercLucroPrejuizo").html("");
           $("#DivGraficoPortProventos").html("");
           $("#DivGraficoAtivos").html("");
           $("#DivGraficoSetores").html("");
           $("#DivGraficoSubSetores").html("");
           $("#DivGraficoSegmentos").html("");
           $("#DivGridAtivoSetor").html("");

           fLimparSomenteGrid( urlPadrao );

           // resolve(true);
           // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
                     //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
                     fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
}

async function fMontarTotalizadores( urlPadrao, TotInvest, TotAtual, TotValorizacao, PercValorizacao, TotRend, TotAlug, TotGanhoPerda, PercGanhoPerda ){  
    try {   

              promise = new Promise( (resolve, reject) => {
                     
                     resolve(true);

                     // var start = new Date().getTime();
                     // console.log('fMontarTotalizadores - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
     
                     $("#DivPortTotInvest").html(   "R$ " + fMascaraValor(TotInvest) );
                     $("#DivPortTotAtual").html(    "R$ " + fMascaraValor(TotAtual) );
                     $("#DivPortValorizacao").html( "R$ " + fMascaraValor(TotValorizacao) + " <small><em>( "+ fMascaraValor(PercValorizacao) +"% )</em></small>");
                     $("#DivPortRendimento").html(  "R$ " + fMascaraValor(TotRend) );
                     $("#DivPortAluguel").html(     "R$ " + fMascaraValor(TotAlug) );
                     $("#DivPortGanhoPerda").html(  "R$ " + fMascaraValor(TotGanhoPerda) + " <small><em>( "+ fMascaraValor(PercGanhoPerda) +"% )</em></small>");

                     $("#DivPortValorizacao").removeClass("text-muted");               
                     if ( TotValorizacao  > 0.00 ) $("#DivPortValorizacao").addClass("text-success");
                     if ( TotValorizacao  < 0.00 ) $("#DivPortValorizacao").addClass("text-danger");
                     if ( TotValorizacao == 0.00 ) $("#DivPortValorizacao").addClass("text-muted");

                     $("#DivPortGanhoPerda").removeClass("text-muted");             
                     if ( TotGanhoPerda > 0 ) $("#DivPortGanhoPerda").addClass("text-success");
                     if ( TotGanhoPerda < 0 ) $("#DivPortGanhoPerda").addClass("text-danger");  
                     if ( TotGanhoPerda == 0 ) $("#DivPortGanhoPerda").addClass("text-muted");

                     // var end = new Date().getTime();
                     // var time = end - start;
                     // sec = Math.floor((time/1000) % 60);
                     // console.log('fMontarTotalizadores - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");
                             
                             // resolve(true);
               // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
             })
             .then( txt => {
               //console.log('Sucesso: ' + txt);
             })
             .catch( txt => {
               fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
             });
    
    } catch (e) {
      if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fMontarGridPercentualAtivos( urlPadrao, arCodAtivos, arValInvest, arValAtual ) {
    try {    

          promise = new Promise( (resolve, reject) => {
                         
               resolve(true);
                               
               // var start = new Date().getTime();
               // console.log('fMontarGridPercentualAtivos - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                               
               var DivGridPortfPercent = $("#DivGridPortfPercent");                               
               DivGridPortfPercent.html("");

               var fLen = arCodAtivos.length;
               
               var arProftfolio = [];
               var TotalInvest  = 0.00;
               var TotalAtual   = 0.00;
               for (i = 0; i < fLen; i++) {
                   TotalInvest += parseFloat(arValInvest[i]);
                   TotalAtual  += parseFloat(arValAtual[i]); 
                   arProftfolio.push({ Codigo: arCodAtivos[i], ValorInvest: arValInvest[i], PercentInvest: 0.00, ValorAtual: arValAtual[i], PercentAtual: 0.00, TipoInvest: '' });
               }
               
               for (i = 0; i < fLen; i++) {
                   var ValorInvest   = parseFloat(arProftfolio[i].ValorInvest); 
                   var PercentInvest = parseFloat(arProftfolio[i].PercentInvest); 
                   var ValorAtual    = parseFloat(arProftfolio[i].ValorAtual); 
                   var PercentAtual  = parseFloat(arProftfolio[i].PercentAtual); 
                   if ( (ValorInvest > 0.00) && (TotalInvest > 0.00) ) PercentInvest = ( ValorInvest / TotalInvest ) * 100;
                   if ( (ValorAtual  > 0.00) && (TotalAtual  > 0.00) ) PercentAtual  = ( ValorAtual  / TotalAtual  ) * 100;
                   arProftfolio[i].PercentInvest = PercentInvest;
                   arProftfolio[i].PercentAtual  = PercentAtual;
               }

               arProftfolio.sort(function(a, b){
                 var APercentAtual  = parseFloat(a.PercentAtual); 
                 var BPercentAtual  = parseFloat(b.PercentAtual); 
                 if (APercentAtual == BPercentAtual) return 0;
                 return APercentAtual > BPercentAtual? 1: -1;
               });
               
               arProftfolio.reverse();

               var content = '';
               content     += '<table style="font-size: 12px;" class="table table-sm table-hover table-bord ered table-condensed nowrap" cellspacing="0" width="100%">';
               content     += '  <thead>';
               content     += '    <tr class="thead-dark font-weight-bold text-center"> ';
               content     += '      <th title="Código do Ativo">Ativo</th> ';
               //content     += '      <th title="Percentual Investido no Ativo do Portfólio">% Invest.</th> ';
               content     += '      <th title="Percentual Atual do Ativo no Portfólio">% Carteira</th> '; 
               content     += '    </tr>';
               content     += '   </thead>';
               content     += '  <tbody>';

               for (i = 0; i < fLen; i++) {
                     var Codigo        = arProftfolio[i].Codigo;
                     //var ValorInvest   = parseFloat(arProftfolio[i].ValorInvest); 
                     var PercentInvest = parseFloat(arProftfolio[i].PercentInvest); 
                     //var ValorAtual    = parseFloat(arProftfolio[i].ValorAtual); 
                     var PercentAtual  = parseFloat(arProftfolio[i].PercentAtual); 
                     content += '    <tr class="text-center"> ';
                     content += '      <td> <a href="https://www.google.com.br/search?q='+Codigo+'" target="_blank"> <span class="text-dark font-weight-bold">'+Codigo + '</span></a> </td>';
                     //content += '      <td> <span class="text-muted"> '+fMascaraValor(PercentInvest)+'% </span> </td>';
                     content += '      <td> <span class="text-dark font-weight-bold"> '+fMascaraValor(PercentAtual)+'% </span> </td>';
                     content += '    </tr>';
               }
               
               content += '  </tbody>';
               content += '  <tfoot> </tfoot>';
               content += '</table>';

               DivGridPortfPercent.html("");
               DivGridPortfPercent.append( content ); 

               // var end = new Date().getTime();
               // var time = end - start;
               // sec = Math.floor((time/1000) % 60);
               // console.log('fMontarGridPercentualAtivos - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

               // resolve(true);
               // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));

         })
         .then( txt => {
                         //console.log('Sucesso: ' + txt);
         })
         .catch( txt => {
                         fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
         });
                   
    } catch (e) {
                   if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fMontarGraficoCarteiraGeral( urlPadrao, TotInvest, TotAtual, TotRend, TotAlug ){ 
  try {   
          promise = new Promise( (resolve, reject) => {
                         
               resolve(true);

               // var start = new Date().getTime();
               // console.log('fMontarGraficoCarteiraGeral - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                               
               Highcharts.setOptions({ global: { useUTC: false }, lang: { decimalPoint: ',', thousandsSep: '.' } });

               Highcharts.chart('DivGraficoPortGeral', {
                   lang: {
                            months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
                            shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                            weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                            loading: ['Atualizando o gráfico...aguarde'],
                            contextButtonTitle: 'Exportar gráfico',
                            decimalPoint: ',',
                            thousandsSep: '.',
                            viewFullscreen: 'Exibir em tela cheia',
                            openInCloud: 'Abri em Highcharts Cloud',
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
                   exporting: { enabled: false },
                   data: { table: 'datatable' },
                   chart: { type: 'column' },
                   title: { text: null },
                   //legend: { enabled: true, align: 'center', verticalAlign: 'top', },                 
                   legend: { enabled: false },                                                                                                                                                                        
                   //xAxis: { categories: ['Carteira'], labels: { style: { fontSize: '8.5px' } } },
                   xAxis: { categories: [''], title: { text: null }, labels: {enabled:true,y : 20, rotation: -45, align: 'right' } },
                   yAxis: {allowDecimals: false, title: { text: null } },
                   colors: ['#2f7ed8', '#8bbc21',  '#492970', '#f28f43'],
                   credits: { enabled: false },
                   tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true },
                   series: [{ name: 'Tot. Investido', data: [TotInvest] }, { name: 'Tot. Atual', data: [TotAtual] }, { name: 'Total Valorização', data: [ TotAtual - TotInvest]  }, { name: 'Tot. Proventos', data: [TotRend+TotAlug] }]
               });
                               
               // var end = new Date().getTime();
               // var time = end - start;
               // sec = Math.floor((time/1000) % 60);
               // console.log('fMontarGraficoCarteiraGeral - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

               // resolve(true);
               // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
         })
         .then( txt => {
                         //console.log('Sucesso: ' + txt);
         })
         .catch( txt => {
                         fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
         });
  
    } catch (e) {
      if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fMontarGraficoCarteiraAtivos( urlPadrao, arCodAtivos, arValInvest, arValAtual, arValValoriz, arValRenb ){
  try {    

          promise = new Promise( (resolve, reject) => {
                         
               resolve(true);

               // var start = new Date().getTime();
               // console.log('fMontarGraficoCarteiraAtivos - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                                                              
               var fLen = arCodAtivos.length;
               
               var arProftfolio  = [];
               for (i = 0; i < fLen; i++) {
                    arProftfolio.push({ Codigo: arCodAtivos[i], ValInvest: arValInvest[i], ValAtual: arValAtual[i], ValValoriz: arValValoriz[i], ValRenb: arValRenb[i], TipoInvest: '' });
               }

               arProftfolio.sort(function(a, b){
                   var ACodigo = a.Codigo;
                   var BCodigo = b.Codigo;
                   if (ACodigo == BCodigo) return 0;
                   return ACodigo > BCodigo? 1: -1;
               });

               // arProftfolio.reverse();

               var arNewCodAtivos  = [];
               var arNewValInvest  = [];
               var arNewValAtual   = [];
               var arNewValValoriz = [];
               var arNewValRenb    = [];
               for (i = 0; i < fLen; i++) {
                   arNewCodAtivos[i]  =  arProftfolio[i].Codigo;
                   arNewValInvest[i]  =  arProftfolio[i].ValInvest;
                   arNewValAtual[i]   =  arProftfolio[i].ValAtual;
                   arNewValValoriz[i] =  arProftfolio[i].ValValoriz;
                   arNewValRenb[i]    =  arProftfolio[i].ValRenb;
               }

               Highcharts.chart('DivGraficoPortCarteira', {
                   lang: {
                            months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
                            shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                            weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                            loading: ['Atualizando o gráfico...aguarde'],
                            contextButtonTitle: 'Exportar gráfico',
                            decimalPoint: ',',
                            thousandsSep: '.',
                            viewFullscreen: 'Exibir em tela cheia',
                            openInCloud: 'Abri em Highcharts Cloud',
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
                   data: { table: 'datatable' },
                   chart: { type: 'column' },
                   title: { text: null },
                   legend: { enabled: true, align: 'center', verticalAlign: 'top', floating: true, backgroundColor: Highcharts.defaultOptions.legend.backgroundColor || 'white',borderColor: '#CCC', borderWidth: 1, shadow: false },
                   xAxis: { categories: arNewCodAtivos },
                   colors: ['#2f7ed8', '#8bbc21',  '#492970', '#f28f43'],
                   yAxis: {allowDecimals: false, title: { text: null } },
                   credits: { enabled: false },
                   tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true },
                   series: [{ name: 'Total Investido', data: arNewValInvest }, { name: 'Total Atual', data: arNewValAtual }, { name: 'Total Valorização', data: arNewValValoriz }, { name: 'Total Proventos', data: arNewValRenb }]
               });
                               
               // var end = new Date().getTime();
               // var time = end - start;
               // sec = Math.floor((time/1000) % 60);
               // console.log('fMontarGraficoCarteiraAtivos - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

               // resolve(true);
               // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
         })
         .then( txt => {
                         //console.log('Sucesso: ' + txt);
         })
         .catch( txt => {
                         fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
         });
  
    } catch (e) {
      if ( e.description != undefined ){
                               fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      }
    }
}

async function fMontarGraficoTotalValorizacao( urlPadrao, arCodAtivos, arValValoriz ){
  try {    

          promise = new Promise( (resolve, reject) => {
             
             resolve(true);

             // var start = new Date().getTime();
             // console.log('fMontarGraficoTotalValorizacao - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                             
             var fLen = arCodAtivos.length;

             var arProftfolio = [];
             for (i = 0; i < fLen; i++) {
                arProftfolio.push({ Codigo: arCodAtivos[i], ValValoriz: arValValoriz[i] });
             }

             arProftfolio.sort(function(a, b){
                 var AValValoriz = parseFloat(a.ValValoriz);
                 var BValValoriz = parseFloat(b.ValValoriz);
                 if (AValValoriz == BValValoriz) return 0;
                 return AValValoriz > BValValoriz? 1: -1;
             });
             
             arProftfolio.reverse();
             
             var arCodAtivosOrdenado     = [];
             var arValValorizOrdenado    = [];
             var arValDesvalorizOrdenado = [];
             for (i = 0; i < fLen; i++) {
                 arCodAtivosOrdenado[i]     = arProftfolio[i].Codigo;
                 arValValorizOrdenado[i]    = ( arProftfolio[i].ValValoriz > 0 ) ? arProftfolio[i].ValValoriz : 0.00;
                 arValDesvalorizOrdenado[i] = ( arProftfolio[i].ValValoriz < 0 ) ? arProftfolio[i].ValValoriz : 0.00;
             }

             Highcharts.chart('DivGraficoPortValorLucroPrejuizo', {
                 lang: {
                        months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
                        shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                        weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                        loading: ['Atualizando o gráfico...aguarde'],
                        contextButtonTitle: 'Exportar gráfico',
                        decimalPoint: ',',
                        thousandsSep: '.',
                        viewFullscreen: 'Exibir em tela cheia',
                        openInCloud: 'Abri em Highcharts Cloud',
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
                 data: { table: 'datatable' },
                 chart: { type: 'column' },
                 title: { text: null },
                 legend: { enabled: true, align: 'center', verticalAlign: 'top', floating: true, backgroundColor: Highcharts.defaultOptions.legend.backgroundColor || 'white',borderColor: '#CCC', borderWidth: 1, shadow: false },
                 xAxis: { categories: arCodAtivosOrdenado },
                 yAxis: {allowDecimals: false, title: { text: null } },
                 credits: { enabled: false },
                 tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: false },
                 series: [{ name: 'Total Valorização', data: arValValorizOrdenado, color: '#8bbc21' }, { name: 'Total Desvalorização', data: arValDesvalorizOrdenado, color: '#c42525' }] 
             });

             // var end = new Date().getTime();
             // var time = end - start;
             // sec = Math.floor((time/1000) % 60);
             // console.log('fMontarGraficoTotalValorizacao - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

             // resolve(true);
             // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
         })
         .then( txt => {
                         //console.log('Sucesso: ' + txt);
         })
         .catch( txt => {
                         fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
         });

    } catch (e) {
      if ( e.description != undefined ){
                               fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      }
    }
}

async function fMontarGraficoPercentualValorizacao( urlPadrao, arCodAtivos, arPercValoriz ){
  try {    

          promise = new Promise( (resolve, reject) => {
                         
               resolve(true);

               // var start = new Date().getTime();
               // console.log('fMontarGraficoPercentualValorizacao - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                               
               var fLen = arCodAtivos.length;

               var arProftfolio = [];
               for (i = 0; i < fLen; i++) {
                 arProftfolio.push({ Codigo: arCodAtivos[i], PercValoriz: arPercValoriz[i] });
               }

               arProftfolio.sort(function(a, b){
                   var APercValoriz = parseFloat(a.PercValoriz);
                   var BPercValoriz = parseFloat(b.PercValoriz);
                   if (APercValoriz == BPercValoriz) return 0;
                   return APercValoriz > BPercValoriz? 1: -1;
               });
               
               arProftfolio.reverse();
               
               var arCodAtivosOrdenado      = [];
               var arPercValorizOrdenado    = [];
               var arPercDesvalorizOrdenado = [];
               for (i = 0; i < fLen; i++) {
                   arCodAtivosOrdenado[i]      = arProftfolio[i].Codigo;
                   arPercValorizOrdenado[i]    = ( arProftfolio[i].PercValoriz > 0 ) ? arProftfolio[i].PercValoriz : 0.00;
                   arPercDesvalorizOrdenado[i] = ( arProftfolio[i].PercValoriz < 0 ) ? arProftfolio[i].PercValoriz : 0.00;
               }

               Highcharts.chart('DivGraficoPortPercLucroPrejuizo', {
                   lang: {
                            months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
                            shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                            weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                            loading: ['Atualizando o gráfico...aguarde'],
                            contextButtonTitle: 'Exportar gráfico',
                            decimalPoint: ',',
                            thousandsSep: '.',
                            viewFullscreen: 'Exibir em tela cheia',
                            openInCloud: 'Abri em Highcharts Cloud',
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
                   data: { table: 'datatable' },
                   chart: { type: 'column' },
                   title: { text: null },
                   legend: { enabled: true, align: 'center', verticalAlign: 'top', floating: true, backgroundColor: Highcharts.defaultOptions.legend.backgroundColor || 'white',borderColor: '#CCC', borderWidth: 1, shadow: false },
                   xAxis: { categories: arCodAtivosOrdenado },
                   yAxis: {allowDecimals: false, title: { text: null } },
                   credits: { enabled: false },
                   tooltip: { headerFormat: '<b>{point.x}</b><br/>', pointFormat: '{series.name}: {point.y:.2f}%' }, 
                   series: [{ name: '% Valorização', data: arPercValorizOrdenado, color: '#8bbc21' }, { name: '% Desvalorização', data: arPercDesvalorizOrdenado, color: '#c42525' }] 
               });

               // var end = new Date().getTime();
               // var time = end - start;
               // sec = Math.floor((time/1000) % 60);
               // console.log('fMontarGraficoPercentualValorizacao - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

               // resolve(true);
               // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
         })
         .then( txt => {
                         //console.log('Sucesso: ' + txt);
         })
         .catch( txt => {
                         fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
         });

    } catch (e) {
      if ( e.description != undefined ){
        fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      }
    }
}

async function fMontarGraficoTotalProventos( urlPadrao, arCodAtivos, arValRenb ){
  try {    

            promise = new Promise( (resolve, reject) => {
                           
                 resolve(true);

                 // var start = new Date().getTime();
                 // console.log('fMontarGraficoTotalProventos - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                                                                
                 var fLen = arCodAtivos.length;

                 var arProftfolio = [];
                 for (i = 0; i < fLen; i++) {
                    arProftfolio.push({ Codigo: arCodAtivos[i], ValProvento: arValRenb[i] });
                 }

                 arProftfolio.sort(function(a, b){
                     var AValProvento = parseFloat(a.ValProvento); 
                     var BValProvento = parseFloat(b.ValProvento); 
                     if (AValProvento == BValProvento) return 0;
                     return AValProvento > BValProvento? 1: -1;
                 });

                 arProftfolio.reverse();
                 
                 var arCodAtivosOrdenado   = [];
                 var arValProventoOrdenado = [];
                 for (i = 0; i < fLen; i++) {
                     arCodAtivosOrdenado[i]   = arProftfolio[i].Codigo;
                     arValProventoOrdenado[i] = arProftfolio[i].ValProvento;
                 }

                 Highcharts.chart('DivGraficoPortProventos', {
                       lang: {
                                months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
                                shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                                weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                                loading: ['Atualizando o gráfico...aguarde'],
                                contextButtonTitle: 'Exportar gráfico',
                                decimalPoint: ',',
                                thousandsSep: '.',
                                viewFullscreen: 'Exibir em tela cheia',
                                openInCloud: 'Abri em Highcharts Cloud',
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
                       data: { table: 'datatable' },
                       chart: { type: 'column' },
                       title: { text: null },
                       legend: { enabled: true, align: 'center', verticalAlign: 'top', floating: true, backgroundColor: Highcharts.defaultOptions.legend.backgroundColor || 'white',borderColor: '#CCC', borderWidth: 1, shadow: false },
                       xAxis: { categories: arCodAtivosOrdenado },
                       yAxis: {allowDecimals: false, title: { text: null } },
                       credits: { enabled: false },
                       tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true },
                       series: [{ name: 'Total Proventos', data: arValProventoOrdenado }] 
                 });

                 // var end = new Date().getTime();
                 // var time = end - start;
                 // sec = Math.floor((time/1000) % 60);
                 // console.log('fMontarGraficoTotalProventos - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

                 // resolve(true);
                 // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
           })
           .then( txt => {
                           //console.log('Sucesso: ' + txt);
           })
           .catch( txt => {
                           fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
           });

    } catch (e) {
      if ( e.description != undefined ){
                               fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      }
    }
}

async function fMontarGraficoPesoAtivos( urlPadrao, arCodAtivos, arValAtual ) {
    try {    

          promise = new Promise( (resolve, reject) => {
                         
               resolve(true);

               // var start = new Date().getTime();
               // console.log('fMontarGraficoPesoAtivos - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                               
               var fLen = arCodAtivos.length;
               
               var arProftfolio = [];
               var TotalAtual   = 0.00;
               for (i = 0; i < fLen; i++) {
                   TotalAtual += parseFloat(arValAtual[i]);
                   arProftfolio.push({ Codigo: arCodAtivos[i], ValorAtual: arValAtual[i] });
               }

               arProftfolio.sort(function(a, b){
                   var APercentAtual  = parseFloat(a.ValorAtual); 
                   var BPercentAtual  = parseFloat(b.ValorAtual); 
                   if (APercentAtual == BPercentAtual) return 0;
                   return APercentAtual > BPercentAtual? 1: -1;
               });
               
               arProftfolio.reverse();
               
               var DataSetAtivos = []; 
               for (i = 0; i < fLen; i++) {
                    DataSetAtivos[i] = { name: arProftfolio[i].Codigo, y: parseFloat(arProftfolio[i].ValorAtual), sliced: ( i == 0 ) , selected: ( i == 0 )  };
               }

               Highcharts.chart('DivGraficoAtivos', {
                   lang: {
                                  months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
                                  shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                                  weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                                  loading: ['Atualizando o gráfico...aguarde'],
                                  contextButtonTitle: 'Exportar gráfico',
                                  decimalPoint: ',',
                                  thousandsSep: '.',
                                  viewFullscreen: 'Exibir em tela cheia',
                                  openInCloud: 'Abri em Highcharts Cloud',
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
                   chart: { plotBackgroundColor: null, plotBorderWidth: null, plotShadow: false,type: 'pie' },
                   title: { text: 'Ativos' },
                   //tooltip: { pointFormat: '{series.name}: <b>{point.percentage:.2f}%</b>' },
                   //tooltip: { pointFormat: 'R$ {point.y:.2f} <b>{point.percentage:.2f}%</b>' },
                   tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return 'Total: <b>R$ ' + value + '</b> <br> Percent.: <b>'+ Number(this.percentage).toFixed(2) +'%</b> '; }, shared: true },
                   plotOptions: { pie: { allowPointSelect: true, cursor: 'pointer', dataLabels: { enabled: true, format: '<b>{point.name}</b>: {point.percentage:.2f} %' } } },
                   series: [{ name: 'Ativos', colorByPoint: true, data: DataSetAtivos }]
               });           
                               
               // var end = new Date().getTime();
               // var time = end - start;
               // sec = Math.floor((time/1000) % 60);
               // console.log('fMontarGraficoPesoAtivos - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

               // resolve(true);
               // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
         })
         .then( txt => {
                         //console.log('Sucesso: ' + txt);
         })
         .catch( txt => {
                         fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
         });
                   
    } catch (e) {
                   if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fMontarGraficoPesoSetores( urlPadrao, arSetorNome, arSetorTotal ) { 
      try {    

            promise = new Promise( (resolve, reject) => {
                           
               resolve(true);

               // var start = new Date().getTime();
               // console.log('fMontarGraficoPesoSetores - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );

               var arProftfolio = [];
               var TotalAtual   = 0.00;
               for (var key in arSetorTotal) {
                   TotalAtual += parseFloat( arSetorTotal[key] );
                   arProftfolio.push({ Codigo: arSetorNome[key], ValorAtual: arSetorTotal[key] });
               }

               arProftfolio.sort(function(a, b){
                     var APercentAtual  = parseFloat(a.ValorAtual);
                     var BPercentAtual  = parseFloat(b.ValorAtual);
                     if (APercentAtual == BPercentAtual) return 0;
                     return APercentAtual > BPercentAtual? 1: -1;
               });

               arProftfolio.reverse();

               var fLen = arProftfolio.length;
               var DataSetSetores = [];
               for (i = 0; i < fLen; i++) {
                               DataSetSetores[i] = { name: arProftfolio[i].Codigo, y: parseFloat(arProftfolio[i].ValorAtual), sliced: ( i == 0 ) , selected: ( i == 0 )  };
               }

               Highcharts.chart('DivGraficoSetores', {
                   lang: {
                            months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
                            shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                            weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                            loading: ['Atualizando o gráfico...aguarde'],
                            contextButtonTitle: 'Exportar gráfico',
                            decimalPoint: ',',
                            thousandsSep: '.',
                            viewFullscreen: 'Exibir em tela cheia',
                            openInCloud: 'Abri em Highcharts Cloud',
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
                   chart: { plotBackgroundColor: null, plotBorderWidth: null, plotShadow: false,type: 'pie' },
                   title: { text: 'Setores' },
                   //tooltip: { pointFormat: '{series.name}: <b>{point.percentage:.2f}%</b>' },
                   //tooltip: { pointFormat: 'R$ {point.y:.2f} <b>{point.percentage:.2f}%</b>' },
                   tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return 'Total: <b>R$ ' + value + '</b> <br> Percent.: <b>'+ Number(this.percentage).toFixed(2) +'%</b> '; }, shared: true },
                   plotOptions: { pie: { allowPointSelect: true, cursor: 'pointer', dataLabels: { enabled: true, format: '<b>{point.name}</b>: {point.percentage:.2f} %' } } },
                   series: [{ name: 'Setores', colorByPoint: true, data: DataSetSetores }]
               });

               // var end = new Date().getTime();
               // var time = end - start;
               // sec = Math.floor((time/1000) % 60);
               // console.log('fMontarGraficoPesoSetores - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

               // resolve(true);
               // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
           })
           .then( txt => {
                           //console.log('Sucesso: ' + txt);
           })
           .catch( txt => {
                           fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
            });
                     
      } catch (e) {
                     if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      }
}

async function fMontarGraficoPesoSubSetores( urlPadrao, arSubSetorNome, arSubSetorTotal ) { 
    try {    

          promise = new Promise( (resolve, reject) => {
               
               resolve(true);

               // var start = new Date().getTime();
               // console.log('fMontarGraficoPesoSubSetores - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                               
               var arProftfolio = [];
               var TotalAtual   = 0.00;
               for (var key in arSubSetorTotal) {
                   TotalAtual += parseFloat( arSubSetorTotal[key] );
                   arProftfolio.push({ Codigo: arSubSetorNome[key], ValorAtual: arSubSetorTotal[key] });
               }
               
               arProftfolio.sort(function(a, b){
                   var APercentAtual  = parseFloat(a.ValorAtual);
                   var BPercentAtual  = parseFloat(b.ValorAtual);
                   if (APercentAtual == BPercentAtual) return 0;
                   return APercentAtual > BPercentAtual? 1: -1;
               });
               
               arProftfolio.reverse();
               
               var fLen = arProftfolio.length;
               var DataSetSubSetores = []; 
               for (i = 0; i < fLen; i++) {
                    DataSetSubSetores[i] = { name: arProftfolio[i].Codigo, y: parseFloat(arProftfolio[i].ValorAtual), sliced: ( i == 0 ) , selected: ( i == 0 )  };
               }

               Highcharts.chart('DivGraficoSubSetores', {
                   lang: {
                          months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
                          shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                          weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                          loading: ['Atualizando o gráfico...aguarde'],
                          contextButtonTitle: 'Exportar gráfico',
                          decimalPoint: ',',
                          thousandsSep: '.',
                          viewFullscreen: 'Exibir em tela cheia',
                          openInCloud: 'Abri em Highcharts Cloud',
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
                   chart: { plotBackgroundColor: null, plotBorderWidth: null, plotShadow: false,type: 'pie' },
                   title: { text: 'Sub-Setores' },
                   //tooltip: { pointFormat: '{series.name}: <b>{point.percentage:.2f}%</b>' },
                   //tooltip: { pointFormat: 'R$ {point.y:.2f} <b>{point.percentage:.2f}%</b>' },
                   tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return 'Total: <b>R$ ' + value + '</b> <br> Percent.: <b>'+ Number(this.percentage).toFixed(2) +'%</b> '; }, shared: true },
                   plotOptions: { pie: { allowPointSelect: true, cursor: 'pointer', dataLabels: { enabled: true, format: '<b>{point.name}</b>: {point.percentage:.2f} %' } } },
                   series: [{ name: 'SubSetores', colorByPoint: true, data: DataSetSubSetores }]
               });           

               // var end = new Date().getTime();
               // var time = end - start;
               // sec = Math.floor((time/1000) % 60);
               // console.log('fMontarGraficoPesoSubSetores - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

               // resolve(true);
               // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
         })
         .then( txt => {
                         //console.log('Sucesso: ' + txt);
         })
         .catch( txt => {
            fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
         });
                   
    } catch (e) {
        if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fMontarGraficoPesoSegmentos( urlPadrao, arSegmentoNome, arSegmentoTotal ) { 
    try {    

            promise = new Promise( (resolve, reject) => {
                           
               resolve(true);
                               
               // var start = new Date().getTime();
               // console.log('fMontarGraficoPesoSegmentos - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                               
               var arProftfolio = [];
               var TotalAtual   = 0.00;
               for (var key in arSegmentoTotal) {
                   TotalAtual += parseFloat( arSegmentoTotal[key] );
                   arProftfolio.push({ Codigo: arSegmentoNome[key], ValorAtual: arSegmentoTotal[key] });
               }
               
               arProftfolio.sort(function(a, b){
                   var APercentAtual  = parseFloat(a.ValorAtual);
                   var BPercentAtual  = parseFloat(b.ValorAtual);
                   if (APercentAtual == BPercentAtual) return 0;
                   return APercentAtual > BPercentAtual? 1: -1;
               });
               
               arProftfolio.reverse();
               
               var fLen = arProftfolio.length;
               var DataSetSegmento = []; 
               for (i = 0; i < fLen; i++) {
                    DataSetSegmento[i] = { name: arProftfolio[i].Codigo, y: parseFloat(arProftfolio[i].ValorAtual), sliced: ( i == 0 ) , selected: ( i == 0 )  };
               }

               Highcharts.chart('DivGraficoSegmentos', {
                   lang: {
                            months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
                          shortMonths: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                          weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
                          loading: ['Atualizando o gráfico...aguarde'],
                          contextButtonTitle: 'Exportar gráfico',
                          decimalPoint: ',',
                          thousandsSep: '.',
                          viewFullscreen: 'Exibir em tela cheia',
                          openInCloud: 'Abri em Highcharts Cloud',
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
                   chart: { plotBackgroundColor: null, plotBorderWidth: null, plotShadow: false,type: 'pie' },
                   title: { text: 'Segmentos' },
                   //tooltip: { pointFormat: '{series.name}: <b>{point.percentage:.2f}%</b>' },
                   //tooltip: { pointFormat: 'R$ {point.y:.2f} <b>{point.percentage:.2f}%</b>' },
                   tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return 'Total: <b>R$ ' + value + '</b> <br> Percent.: <b>'+ Number(this.percentage).toFixed(2) +'%</b> '; }, shared: true },
                   plotOptions: { pie: { allowPointSelect: true, cursor: 'pointer', dataLabels: { enabled: true, format: '<b>{point.name}</b>: {point.percentage:.2f} %' } } },
                   series: [{ name: 'Segmentos', colorByPoint: true, data: DataSetSegmento }]
               });           

               // var end = new Date().getTime();
               // var time = end - start;
               // sec = Math.floor((time/1000) % 60);
               // console.log('fMontarGraficoPesoSegmentos - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

               // resolve(true);
               // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
           })
           .then( txt => {
                           //console.log('Sucesso: ' + txt);
           })
           .catch( txt => {
                fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
           });
                   
    } catch (e) {
        if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fMontarGridSetores( urlPadrao, TotAtual, arSetorQtde, arSetorTotal, arSubSetorQtde, arSubSetorTotal, arSegmentoQtde, arSegmentoTotal ) {
    try {    

          promise = new Promise( (resolve, reject) => {
                         
             resolve(true);

             // var start = new Date().getTime();
             // console.log('fMontarGridSetores - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                             
             var DivGridAtivoSetor = $("#DivGridAtivoSetor");                               
             DivGridAtivoSetor.html("");

             var content = '';
             content    += '<table border="0" class="table table-sm table-b ordered table-h over table-s triped " style="font-size: 13px;">';
             content    += '<thead class="thead-dark"> ';
             content    += '<tr style="width: 5px;" class="text-center"> ';
             content    += '<th style="width: 5px;">Setor</th>';
             content    += '<th style="width: 5px;">Total</th>';
             content    += '<th style="width: 5px;">%</th> ';
             content    += '<th style="width: 5px;">Sub-Setor</th>';
             content    += '<th style="width: 5px;">Total</th>';
             content    += '<th style="width: 5px;">%</th> ';
             content    += '<th style="width: 5px;">Segmento</th>';
             content    += '<th style="width: 5px;">Total</th>';
             content    += '<th style="width: 5px;">%</th> ';
             content    += '<th style="width: 5px;">Ativo</th> ';
             content    += '<th style="width: 5px;">Total</th>';
             content    += '<th style="width: 5px;">%</th> ';
             content    += '</tr> ';
             content    += '</thead>';
             content    += '<tbody class="text-center">';

             var contentLinhas = "";

             if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){

                   var lista = DataSetPagina.data.Lista;       

                   if ( lista.length > 0 ){

                      var IdPortfolio = fGetAbaIdPortfolio();
                       var TipoInvest  = fGetAbaTipoPortfolio();

                      var UltimoSetor    = "";
                      var UltimoSubSetor = "";
                      var UltimoSegmetno = "";
                      $.each(lista, function (index, value) {

                          var CartId        = value.CartId;
                          var AtvTipoInvest = value.AtvTipoInvest;
                          
                          if ( (IdPortfolio == "") || (IdPortfolio == CartId ) ){
                              if ( (TipoInvest=="" || TipoInvest=="ACAO") && (AtvTipoInvest == "ACAO") ){ // if ( (TipoInvest == "") || (TipoInvest == AtvTipoInvest) ){

                                   var SetorId     = value.SetorId;
                                   var SubSetorId  = value.SubSetorId;
                                   var SegmentoId  = value.SegmentoId;
                                   var AtvCodigo   = value.AtvCodigo;
                                   var AtvTotAtual = parseFloat(GetValorDecimal( value.AtvTotAtual )); 

                                   if ( UltimoSetor != SetorId ) {
                                         contentLinhas    += '<tr class="bg-light"> ';
                                         contentLinhas    += '<td style="border-top: 1px solid black;" colspan="12"> </td> ';
                                         contentLinhas    += '</tr>';
                                   }

                                   contentLinhas    += '<tr style="border: 1px solid black; font-size: 11px;"> ';

                                   if ( UltimoSetor == "" || UltimoSetor != SetorId ){
                                       var SetQtde      = arSetorQtde[SetorId];
                                       var SetTotal     = arSetorTotal[SetorId];
                                       var SetPercent   = ( (TotAtual > 0.00 && SetTotal > 0.00) ? ( SetTotal / TotAtual ) * 100 : 0.00 );   
                                       contentLinhas    += '<td style="border-top: 1px solid black; border-left: 1px solid black;" rowspan="'+SetQtde+'" class="font-weight-bold">'+value.SetorNome+'</td>  ';
                                       contentLinhas    += '<td style="border-bottom: 1px solid black;" rowspan="'+SetQtde+'">R$ '+fMascaraValor(parseFloat(SetTotal)) +'</td> ';
                                       contentLinhas    += '<td style="border-bottom: 1px solid black;" rowspan="'+SetQtde+'" class="font-weight-bold">'+fMascaraValor(parseFloat(SetPercent))+'%</td>';
                                       UltimoSetor       = SetorId;
                                       //UltimoSubSetor    = '';
                                       //UltimoSegmetno    = '';
                                   }
                                   
                                   if ( UltimoSubSetor == "" || UltimoSubSetor != SubSetorId ){
                                       var SubQtde      = arSubSetorQtde[SetorId+'-'+SubSetorId];
                                       var SubTotal     = arSubSetorTotal[SetorId+'-'+SubSetorId];
                                       var SubPercent   = ( (TotAtual > 0.00 && SubTotal > 0.00) ? ( SubTotal / TotAtual ) * 100 : 0.00 ); 
                                       contentLinhas    += '<td rowspan="'+SubQtde+'" class="font-weight-bold">'+value.SubSetorNome+'</td>';
                                       contentLinhas    += '<td rowspan="'+SubQtde+'">R$ '+fMascaraValor(parseFloat(SubTotal)) +'</td> ';
                                       contentLinhas    += '<td rowspan="'+SubQtde+'" class="font-weight-bold">'+fMascaraValor(parseFloat(SubPercent))+'%</td>';
                                       UltimoSubSetor    = SubSetorId;
                                       //UltimoSegmetno    = '';
                                   }

                                   if ( UltimoSegmetno == "" || UltimoSegmetno != SegmentoId ){
                                       var SegQtde      = arSegmentoQtde[SetorId+'-'+SubSetorId+'-'+SegmentoId];
                                       var SegTotal     = arSegmentoTotal[SetorId+'-'+SubSetorId+'-'+SegmentoId];
                                       var SegPercent   = ( (TotAtual > 0.00 && SegTotal > 0.00) ? ( SegTotal / TotAtual ) * 100 : 0.00 );                  
                                       contentLinhas    += '<td rowspan="'+SegQtde+'" class="font-weight-bold">'+value.SegmentoNome+'</td>';
                                       contentLinhas    += '<td rowspan="'+SegQtde+'">R$ '+fMascaraValor(parseFloat(SegTotal)) +'</td> ';
                                       contentLinhas    += '<td rowspan="'+SegQtde+'" class="font-weight-bold">'+fMascaraValor(parseFloat(SegPercent))+'%</td>';
                                       UltimoSegmetno    = SegmentoId;
                                   }

                                   var AtvQtde      = 1;
                                   var AtvPercent   = ( (TotAtual > 0.00 && AtvTotAtual > 0.00) ? ( AtvTotAtual / TotAtual ) * 100 : 0.00 ); 
                                   contentLinhas    += '<td rowspan="'+AtvQtde+'" class="font-weight-bold">'+AtvCodigo+'</td>  ';
                                   contentLinhas    += '<td rowspan="'+AtvQtde+'">R$ '+fMascaraValor(parseFloat(AtvTotAtual)) +'</td> ';
                                   contentLinhas    += '<td rowspan="'+AtvQtde+'" class="font-weight-bold">'+fMascaraValor(parseFloat(AtvPercent))+'%</td>';

                                   // console.log(
                                   //            'Cod: '         + AtvCodigo  + ' - Qrde: '+AtvQtde+
                                   //            ' - Setor: '    +SetorId     + ' - Setor: '+value.SetorNome + 
                                   //            ' - SubSetor: ' +SubSetorId  + ' - SubSetor: '+value.SubSetorNome + 
                                   //            ' - Segment: '  +SegmentoId  +' - Segmento: ' + value.SubSetorNome
                                   // );
                                   
                                   contentLinhas    += '</tr>';

                              } // if ( (TipoInvest == "") || (TipoInvest == value.AtvTipoInvest) ){
                          } // if ( (IdPortfolio == "") || (IdPortfolio == value.CartId) ){

                      }); // $.each(lista, function (index, value) {

                   } // if ( lista.length > 0 ){

             } //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){

             if ( contentLinhas !="" ){
                   content    += contentLinhas;
                   content    += '<tr class="bg-light"> ';
                   content    += '<td style="border-top: 1px solid black;" colspan="12"> </td> ';
                   content    += '</tr>';
                   content    += '</tbody>';
                   content    += '<tfoot class="thead-dark" style="font-size: 13px;"> ';
                   content    += '<tr class="text-center"> ';
                   content    += '<th>Setor</th>';
                   content    += '<th colspan="2">R$ '+fMascaraValor(parseFloat(TotAtual)) +'</th>';
                   content    += '<th>Sub-Setor</th>';
                   content    += '<th colspan="2">R$ '+fMascaraValor(parseFloat(TotAtual)) +'</th>';
                   content    += '<th>Segmento</th>';
                   content    += '<th colspan="2">R$ '+fMascaraValor(parseFloat(TotAtual)) +'</th>';
                   content    += '<th>Ativo</th> ';
                   content    += '<th colspan="2">R$ '+fMascaraValor(parseFloat(TotAtual)) +'</th>';
                   content    += '</tr> ';
                   content    += '</tfoot>';
                   content    += '</table>';
             }else{
                             content = "";
             }

             DivGridAtivoSetor.html("");
             DivGridAtivoSetor.append( content );   

             // var end = new Date().getTime();
             // var time = end - start;
             // sec = Math.floor((time/1000) % 60);
             // console.log('fMontarGridSetores - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

             // resolve(true);
             // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
         })
         .then( txt => {
                         //console.log('Sucesso: ' + txt);
         })
         .catch( txt => {
                         fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
         });
                                                                    
    } catch (e) {
                   if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fMontarGridValorizacaoDia( urlPadrao, lista ) {
  try {    

        promise = new Promise( (resolve, reject) => {
                       
         resolve(true);

         // var start = new Date().getTime();
         // console.log('fMontarGridValorizacaoDia - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                                                        
       var DivListValDia      = $("#ListaValDia");
       var DivListValDiaTotal = $("#ListaValDiaTotal");
                   
        DivListValDia.html(      "" );
         DivListValDiaTotal.html( "" );

         var Total = 0.00;

         var content = '';
         content     += '<table id="GridValDia" border="0" class="table table-sm table-hover table-condensed nowrap" cellspacing="0" width="100%">';
         //content     += '  <thead><tr class="bg-secondary text-white text-center"> <th>Ativo</th> <th>Preço</th> <th>Valorização</th> <th>Total</th> <th>Grafico</th> </tr></thead>';
         content     += '  <tbody>';

         if ( lista.length > 0 ){

               lista.sort(function(a, b){

                  var ValValorizA  = parseFloat( GetValorDecimal( a.VlrValorizDia  ) ); 
                  var PercValorizA = parseFloat( GetValorDecimal( a.PercValorizDia ) ); 

                  var ValValorizB  = parseFloat( GetValorDecimal( b.VlrValorizDia  ) ); 
                  var PercValorizB = parseFloat( GetValorDecimal( b.PercValorizDia ) ); 

                  if ( ValValorizA < 0.00 && PercValorizA > 0.00 ) PercValorizA = PercValorizA * -1;
                  if ( ValValorizB < 0.00 && PercValorizB > 0.00 ) PercValorizB = PercValorizB * -1;

                  if(PercValorizA== PercValorizB) return 0;
                  return PercValorizA> PercValorizB? 1: -1;
               });

               lista.reverse();

               $.each(lista, function (index, value) {
     
                    var CodAtivo    = value.Codigo;                      
                    var TipoInvest  = value.TipoInvest;       
                    
                    if ( TipoInvest == 'CRIPTO' ) {
                        var Qtde = parseFloat( GetValorDecimalMaior( value.Quant ) ); 
                    } else {
                        var Qtde = parseFloat( GetValorInteiro( value.Quant ) ); 
                    }    

                    var ValAtual    = parseFloat( GetValorDecimal( value.PrecoAtual     ) );
                    var ValValoriz  = parseFloat( GetValorDecimal( value.VlrValorizDia  ) );
                    var PercValoriz = parseFloat( GetValorDecimal( value.PercValorizDia ) );
                                    
                    var Valor = 0.00; 
                    if( ValValoriz != 0.00 ) Valor = Qtde * ValValoriz; 
                    Total = Total + Valor;
                    
                    content += '    <tr class="text-center"> ';
                    
                    if( Valor >  0.00 ) content += '      <td style="width:40px"> <i class="fa fa-arrow-up faa-bounce ani mated text-success">  </i> <a href="https://www.google.com.br/search?q='+CodAtivo+'" target="_blank"> <span class="text-success font-weight-bold" style="font-size: 12px;" >'+CodAtivo + '</span></a> </td>';
                    if( Valor == 0.00 ) content += '      <td style="width:40px"> <i class="fa fa-arrow-right faa-flash ani mated text-primary"></i> <a href="https://www.google.com.br/search?q='+CodAtivo+'" target="_blank"> <span class="text-primary font-weight-bold" style="font-size: 12px;" >'+CodAtivo + '</span></a> </td>';
                    if( Valor <  0.00 ) content += '      <td style="width:40px"> <i class="fa fa-arrow-down faa-bounce ani mated text-danger" ></i> <a href="https://www.google.com.br/search?q='+CodAtivo+'" target="_blank"> <span class="text-danger  font-weight-bold" style="font-size: 12px;" >'+CodAtivo + '</span></a> </td>';
                    content += '      <td style="width:50px"> <span class="text-dark  font-weigh t-bold" style="font-size: 12px;">  R$ '+fMascaraValor(ValAtual) +'</span></td>';
                    if( Valor >  0.00 ){ 
                        //content += '      <td style="width:80px"> <span class="text-success" style="font-size: 12px;"> +'+fMascaraValor(ValValoriz)+'</span> <span class="text-success font-weight-bold" style="font-size: 12px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
                        content += '      <td style="width:80px"> <span class="text-success font-weight-bold" style="font-size: 12px;"> '+fMascaraValor(PercValoriz)+'% </span> </td>';
                        content += '      <td style="width:80px"> <span class="badge badge-success badge-pill font-weight-bold" style="font-size: 12px;"> +'+ fMascaraValor(Valor) +' </span> </td>';
                    }
                    if( Valor == 0.00 ){
                        //content += '      <td style="width:80px"> <span class="text-primary" style="font-size: 12px;"> '+fMascaraValor(ValValoriz)+'</span> <span class="text-primary font-weight-bold" style="font-size: 12px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
                        content += '      <td style="width:80px"> <span class="text-primary font-weight-bold" style="font-size: 12px;"> '+fMascaraValor(PercValoriz)+'% </span> </td>';
                        content += '      <td style="width:80px"> <span class="badge badge-primary badge-pill font-weight-bold" style="font-size: 12px;"> ' + fMascaraValor(Valor) +' </span> </td>';
                    }
                    if( Valor <  0.00 ){
                        //content += '      <td style="width:80px"> <span class="text-danger" style="font-size: 12px;"> '+fMascaraValor(ValValoriz)+'</span> <span class="text-danger font-weight-bold" style="font-size: 12px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
                        content += '      <td style="width:80px"> <span class="text-danger font-weight-bold" style="font-size: 12px;"> '+fMascaraValor(PercValoriz)+'% </span> </td>';
                        content += '      <td style="width:80px"> <span class="badge badge-danger  badge-pill font-weight-bold" style="font-size: 12px;"> ' + fMascaraValor(Valor) +' </span> </td>';
                    }

                    content += '      <td style="width:10px">';
                    if ( TipoInvest == 'CRIPTO' ) {
                        content += '         <a class="btn btn-sm btn-success btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.6rem; min-width: 1.6rem; width: 1.6rem; margin: 1px 1px; font-size:0.3rem; " title="Comprar Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
                        content += '            onclick="fAbrirModalDetalheOperCripto( \''+urlPadrao+'\', \'\', \'Novo\', \'C\', \''+CodAtivo+'\', \'1\', \''+fMascaraValor(ValAtual)+'\' );"> <i class="fa fa-plus-square" aria-hidden="true"></i> ';
                        content += '         </a>';
                        content += '         <a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.6rem; min-width: 1.6rem; width: 1.6rem; margin: 1px 1px; font-size:0.3rem; " title="Vender Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
                        content += '            onclick="fAbrirModalDetalheOperCripto( \''+urlPadrao+'\', \'\', \'Novo\', \'V\', \''+CodAtivo+'\', \''+Qtde+'\', \''+fMascaraValor(ValAtual)+'\' );"> <i class="fa fa-minus-square" aria-hidden="true"></i> ';
                        content += '         </a>';
                    } else {
                        content += '         <a class="btn btn-sm btn-success btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.6rem; min-width: 1.6rem; width: 1.6rem; margin: 1px 1px; font-size:0.3rem; " title="Comprar Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
                        content += '            onclick="fAbrirModalDetalheOper( \''+urlPadrao+'\', \'\', \'Novo\', \'C\', \''+CodAtivo+'\', \'100\', \''+fMascaraValor(ValAtual)+'\' );"> <i class="fa fa-plus-square" aria-hidden="true"></i> ';
                        content += '         </a>';
                        content += '         <a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.6rem; min-width: 1.6rem; width: 1.6rem; margin: 1px 1px; font-size:0.3rem; " title="Vender Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
                        content += '            onclick="fAbrirModalDetalheOper( \''+urlPadrao+'\', \'\', \'Novo\', \'V\', \''+CodAtivo+'\', \''+Qtde+'\', \''+fMascaraValor(ValAtual)+'\' );"> <i class="fa fa-minus-square" aria-hidden="true"></i> ';
                        content += '         </a>';
                    }
                    content += '         <a class="btn btn-sm btn-dark btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.6rem; min-width: 1.6rem; width: 1.6rem; margin: 1px 1px; font-size:0.3rem; " title="Gráfico do Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
                    content += '            onclick="fAbrirModalGraficoPortfolio( \''+urlPadrao+'\',\''+CodAtivo+'\' );"> <i class="fa fa-area-chart" aria-hidden="true"></i> ';
                    content += '         </a>';
                    content += '      </td>';
                                    
                    content += '    </tr>';
                              
               }); // $.each(listaGrid, function (index, value) {

                         
         } // if ( lista.length > 0 ){

         content += '  </tbody>';
         content += '</table>';
         
         DivListValDia.html(      "" );
         DivListValDia.append( content );
         
         content  = '';
         content += '<table border="0" style="border: 0px solid black;  font-size: 14px" class="table table-sm table-condensed nowrap" cellspacing="0" width="100%">';
         //content += '  <thead><tr class="bg-secondary text-white text-center"> <th style="width:1px"></th> <th>Ativo</th> <th>Preço</th> <th>Valorização</th> <th>Total</th> </tr></thead>';
         //content += '  <tfoot> </tfoot>';
         content += '  <tbody style="border: 0px solid black; ">'; 
         content += '    <tr bgcolor="#e9ecef" style="border: 0px solid black; " class="text-white text-center"> ';
         content += '      <td style="border: 0px solid black; width:20px">&nbsp;<span class="text-dark font-weight-bold" style="font-size: 14px;" >TOTAL</span> </td>';
         content += '      <td style="border: 0px solid black; width:50px">&nbsp;</td>';
         content += '      <td style="border: 0px solid black; width:50px">&nbsp;</td>';
         if( Total >  0.00 ) content += '      <td style="border: 0px solid black; width:70px"> <span class="badge badge-success badge-pill font-weight-bold" style="font-size: 14px;"> +'+ fMascaraValor(Total) +'</span> </td>';
         if( Total == 0.00 ) content += '      <td style="border: 0px solid black; width:70px"> <span class="badge badge-primary badge-pill font-weight-bold" style="font-size: 14px;">  '+ fMascaraValor(Total) +'</span> </td>';
         if( Total <  0.00 ) content += '      <td style="border: 0px solid black; width:70px"> <span class="badge badge-danger  badge-pill font-weight-bold" style="font-size: 14px;">  '+ fMascaraValor(Total) +'</span> </td>';
         content += '      <td style="border: 0px solid black; width:80px">&nbsp;</td>';
         content += '    </tr>';
         content += '  </tbody>';
         content += '</table>';
         
         DivListValDiaTotal.html( "" );
         DivListValDiaTotal.append( content );

         // var end = new Date().getTime();
         // var time = end - start;
         // sec = Math.floor((time/1000) % 60);
         // console.log('fMontarGridValorizacaoDia - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

         // resolve(true);
         // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
       })
       .then( txt => {
                       //console.log('Sucesso: ' + txt);
       })
       .catch( txt => {
            fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
       });
                                                                    
    } catch (e) {
                   if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fMontarGridIndices( urlPadrao ) {
    try {    

          promise = new Promise( (resolve, reject) => {
             
             resolve(true);
             
             // var start = new Date().getTime();
             // console.log('fMontarGridIndices - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                             
             var DivListIndice = $("#ListaIndice");
             DivListIndice.html("");

             var contentIndice     = '';
             contentIndice     += '<table class="table table-sm table-hover table-condensed nowrap" border="0" cellspacing="0" width="100%" style="margin: 0px;">';
             contentIndice     += '  <tbody>';

             var contentIndiceIBOV = '';
             var contentIndiceIBXX = '';
             var contentIndiceIDIV = '';
             var contentIndiceSMLL = '';
             
             if ( (DataSetRadar) && (DataSetRadar.data) && ( DataSetRadar.data.Lista) ){

                   var lista = DataSetRadar.data.Lista;                                                        
                                  
                   if ( lista.length > 0 ){

                        $.each(lista, function (index, value) {

                            var CodAtivo    = value[0];                                  // 0-CODIGO
                            var Valor       = parseFloat( GetValorDecimal( value[1] ) ); // 1-PRECO
                            var ValValoriz  = parseFloat( GetValorDecimal( value[2] ) ); // 2-Valorização(R$)
                            var PercValoriz = parseFloat( GetValorDecimal( value[3] ) ); // 3-Valorização(%)

                            if ( CodAtivo == 'IBOV' ){
                                  contentIndiceIBOV += '    <tr class="text-center"> ';
                                  if( ValValoriz >  0.00 ) contentIndiceIBOV += '      <td style="width:80px;"> <!-- <i class="fa fa-arrow-up faa-bounce ani mated text-success">  </i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" title="Índice Bovespa" target="_blank"> <span class="text-success font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                  if( ValValoriz == 0.00 ) contentIndiceIBOV += '      <td style="width:80px;"> <!-- <i class="fa fa-arrow-right faa-flash ani mated text-primary"></i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" title="Índice Bovespa" target="_blank"> <span class="text-primary font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                  if( ValValoriz <  0.00 ) contentIndiceIBOV += '      <td style="width:80px;"> <!-- <i class="fa fa-arrow-down faa-bounce ani mated text-danger" ></i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" title="Índice Bovespa" target="_blank"> <span class="text-danger  font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                  contentIndiceIBOV += '      <td> <span class="text-dark  font-weight-bold" style="width:10px; font-size: 11px;">  '+fMascaraValor(Valor) +' pts</span></td>';
//                                  if( ValValoriz >  0.00 ) contentIndiceIBOV += '      <td> <span class="font-weight-normal text-success" style="width:10px; font-size: 11px;"> +'+fMascaraValor(ValValoriz)+'</span> <span class="font-weight-normal text-success font-weight-bold" style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span></td>';
//                                  if( ValValoriz == 0.00 ) contentIndiceIBOV += '      <td> <span class="font-weight-normal text-primary" style="width:10px; font-size: 11px;"> '+fMascaraValor(ValValoriz)+' </span> <span class="font-weight-normal text-primary font-weight-bold" style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
//                                  if( ValValoriz <  0.00 ) contentIndiceIBOV += '      <td> <span class="font-weight-normal text-danger"  style="width:10px; font-size: 11px;"> '+fMascaraValor(ValValoriz)+' </span> <span class="font-weight-normal text-danger font-weight-bold"  style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
                                  if( ValValoriz >  0.00 ) contentIndiceIBOV += '      <td> <span class="font-weight-normal text-success font-weight-bold" style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'% </span></td>';
                                  if( ValValoriz == 0.00 ) contentIndiceIBOV += '      <td> <span class="font-weight-normal text-primary font-weight-bold" style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'% </span> </td>';
                                  if( ValValoriz <  0.00 ) contentIndiceIBOV += '      <td> <span class="font-weight-normal text-danger font-weight-bold"  style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'% </span> </td>';
                                  contentIndiceIBOV += '      <td style="width:10px">';
                                  contentIndiceIBOV += '         <a class="btn btn-sm btn-dark btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.2rem; min-width: 1.2rem; width: 1.2rem; margin: 1px 1px; font-size:0.3rem; " title="Gráfico do Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
                                  contentIndiceIBOV += '            onclick="fAbrirModalGraficoPortfolio( \''+urlPadrao+'\',\''+CodAtivo+'\' );"> <i class="fa fa-area-chart" aria-hidden="true"></i> ';
                                  contentIndiceIBOV += '         </a>';
                                  contentIndiceIBOV += '      </td>';
                                  contentIndiceIBOV += '    </tr>';

                            }else if ( CodAtivo == 'IBXX' ){
                                  contentIndiceIBXX += '    <tr class="text-center"> ';
                                  if( ValValoriz >  0.00 ) contentIndiceIBXX += '      <td style="width:80px;"> <!-- <i class="fa fa-arrow-up faa-bounce ani mated text-success">  </i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" title="Índice Brasil 100" target="_blank"> <span class="text-success font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                  if( ValValoriz == 0.00 ) contentIndiceIBXX += '      <td style="width:80px;"> <!-- <i class="fa fa-arrow-right faa-flash ani mated text-primary"></i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" title="Índice Brasil 100" target="_blank"> <span class="text-primary font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                  if( ValValoriz <  0.00 ) contentIndiceIBXX += '      <td style="width:80px;"> <!-- <i class="fa fa-arrow-down faa-bounce ani mated text-danger" ></i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" title="Índice Brasil 100" target="_blank"> <span class="text-danger  font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                  contentIndiceIBXX += '      <td> <span class="text-dark  font-weight-bold" style="width:10px; font-size: 11px;">  '+fMascaraValor(Valor) +' pts</span></td>';
//                                  if( ValValoriz >  0.00 ) contentIndiceIBXX += '      <td> <span class="font-weight-normal text-success" style="width:10px; font-size: 11px;"> +'+fMascaraValor(ValValoriz)+'</span> <span class="font-weight-normal text-success font-weight-bold" style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span></td>';
//                                  if( ValValoriz == 0.00 ) contentIndiceIBXX += '      <td> <span class="font-weight-normal text-primary" style="width:10px; font-size: 11px;"> '+fMascaraValor(ValValoriz)+' </span> <span class="font-weight-normal text-primary font-weight-bold" style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
//                                  if( ValValoriz <  0.00 ) contentIndiceIBXX += '      <td> <span class="font-weight-normal text-danger"  style="width:10px; font-size: 11px;"> '+fMascaraValor(ValValoriz)+' </span> <span class="font-weight-normal text-danger font-weight-bold"  style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
                                  if( ValValoriz >  0.00 ) contentIndiceIBXX += '      <td> <span class="font-weight-normal text-success font-weight-bold" style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'%'+'</span></td>';
                                  if( ValValoriz == 0.00 ) contentIndiceIBXX += '      <td> <span class="font-weight-normal text-primary font-weight-bold" style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'%'+'</span> </td>';
                                  if( ValValoriz <  0.00 ) contentIndiceIBXX += '      <td> <span class="font-weight-normal text-danger font-weight-bold"  style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'%'+'</span> </td>';
                                  contentIndiceIBXX += '      <td style="width:10px">';
                                  contentIndiceIBXX += '         <a class="btn btn-sm btn-dark btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.2rem; min-width: 1.2rem; width: 1.2rem; margin: 1px 1px; font-size:0.3rem; " title="Gráfico do Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
                                  contentIndiceIBXX += '            onclick="fAbrirModalGraficoPortfolio( \''+urlPadrao+'\',\''+CodAtivo+'\' );"> <i class="fa fa-area-chart" aria-hidden="true"></i> ';
                                  contentIndiceIBXX += '         </a>';
                                  contentIndiceIBXX += '      </td>';
                                  contentIndiceIBXX += '    </tr>';

                            }else if ( CodAtivo == 'IDIV' ){
                                    contentIndiceIDIV += '    <tr class="text-center"> ';
                                    if( ValValoriz >  0.00 ) contentIndiceIDIV += '      <td style="width:80px;"> <!-- <i class="fa fa-arrow-up faa-bounce ani mated text-success">  </i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" title="Índice Dividendos" target="_blank"> <span class="text-success font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                    if( ValValoriz == 0.00 ) contentIndiceIDIV += '      <td style="width:80px;"> <!-- <i class="fa fa-arrow-right faa-flash ani mated text-primary"></i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" title="Índice Dividendos" target="_blank"> <span class="text-primary font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                    if( ValValoriz <  0.00 ) contentIndiceIDIV += '      <td style="width:80px;"> <!-- <i class="fa fa-arrow-down faa-bounce ani mated text-danger" ></i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" title="Índice Dividendos" target="_blank"> <span class="text-danger  font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                    contentIndiceIDIV += '      <td> <span class="text-dark  font-weight-bold" style="width:10px; font-size: 11px;">  '+fMascaraValor(Valor) +' pts</span></td>';
//                                    if( ValValoriz >  0.00 ) contentIndiceIDIV += '      <td> <span class="font-weight-normal text-success" style="width:10px; font-size: 11px;"> +'+fMascaraValor(ValValoriz)+'</span> <span class="font-weight-normal text-success font-weight-bold" style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span></td>';
//                                    if( ValValoriz == 0.00 ) contentIndiceIDIV += '      <td> <span class="font-weight-normal text-primary" style="width:10px; font-size: 11px;"> '+fMascaraValor(ValValoriz)+' </span> <span class="font-weight-normal text-primary font-weight-bold" style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
//                                    if( ValValoriz <  0.00 ) contentIndiceIDIV += '      <td> <span class="font-weight-normal text-danger"  style="width:10px; font-size: 11px;"> '+fMascaraValor(ValValoriz)+' </span> <span class="font-weight-normal text-danger font-weight-bold"  style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
                                    if( ValValoriz >  0.00 ) contentIndiceIDIV += '      <td> <span class="font-weight-normal text-success font-weight-bold" style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'%'+'</span></td>';
                                    if( ValValoriz == 0.00 ) contentIndiceIDIV += '      <td> <span class="font-weight-normal text-primary font-weight-bold" style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'%'+'</span> </td>';
                                    if( ValValoriz <  0.00 ) contentIndiceIDIV += '      <td> <span class="font-weight-normal text-danger font-weight-bold"  style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'%'+'</span> </td>';
                                    contentIndiceIDIV += '      <td style="width:10px">';
                                    contentIndiceIDIV += '         <a class="btn btn-sm btn-dark btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.2rem; min-width: 1.2rem; width: 1.2rem; margin: 1px 1px; font-size:0.3rem; " title="Gráfico do Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
                                    contentIndiceIDIV += '            onclick="fAbrirModalGraficoPortfolio( \''+urlPadrao+'\',\''+CodAtivo+'\' );"> <i class="fa fa-area-chart" aria-hidden="true"></i> ';
                                    contentIndiceIDIV += '         </a>';
                                    contentIndiceIDIV += '      </td>';
                                    contentIndiceIDIV += '    </tr>';

                            }else if ( CodAtivo == 'SMLL' ){
                                contentIndiceSMLL += '    <tr class="text-center"> ';
                                if( ValValoriz >  0.00 ) contentIndiceSMLL += '      <td style="width:80px;"> <!-- <i class="fa fa-arrow-up faa-bounce ani mated text-success">  </i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" title="Índice Small Cap" target="_blank"> <span class="text-success font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                if( ValValoriz == 0.00 ) contentIndiceSMLL += '      <td style="width:80px;"> <!-- <i class="fa fa-arrow-right faa-flash ani mated text-primary"></i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" title="Índice Small Cap" target="_blank"> <span class="text-primary font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                if( ValValoriz <  0.00 ) contentIndiceSMLL += '      <td style="width:80px;"> <!-- <i class="fa fa-arrow-down faa-bounce ani mated text-danger" ></i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" title="Índice Small Cap" target="_blank"> <span class="text-danger  font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                contentIndiceSMLL += '      <td> <span class="text-dark  font-weight-bold" style="width:10px; font-size: 11px;">  '+fMascaraValor(Valor) +' pts</span></td>';
//                                if( ValValoriz >  0.00 ) contentIndiceSMLL += '      <td> <span class="font-weight-normal text-success" style="width:10px; font-size: 11px;"> +'+fMascaraValor(ValValoriz)+'</span> <span class="font-weight-normal text-success font-weight-bold" style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span></td>';
//                                if( ValValoriz == 0.00 ) contentIndiceSMLL += '      <td> <span class="font-weight-normal text-primary" style="width:10px; font-size: 11px;"> '+fMascaraValor(ValValoriz)+' </span> <span class="font-weight-normal text-primary font-weight-bold" style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
//                                if( ValValoriz <  0.00 ) contentIndiceSMLL += '      <td> <span class="font-weight-normal text-danger"  style="width:10px; font-size: 11px;"> '+fMascaraValor(ValValoriz)+' </span> <span class="font-weight-normal text-danger font-weight-bold"  style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
                                if( ValValoriz >  0.00 ) contentIndiceSMLL += '      <td> <span class="font-weight-normal text-success font-weight-bold" style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'%'+'</span></td>';
                                if( ValValoriz == 0.00 ) contentIndiceSMLL += '      <td> <span class="font-weight-normal text-primary font-weight-bold" style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'%'+'</span> </td>';
                                if( ValValoriz <  0.00 ) contentIndiceSMLL += '      <td> <span class="font-weight-normal text-danger font-weight-bold"  style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'%'+'</span> </td>';
                                contentIndiceSMLL += '      <td style="width:10px">';
                                contentIndiceSMLL += '         <a class="btn btn-sm btn-dark btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.2rem; min-width: 1.2rem; width: 1.2rem; margin: 1px 1px; font-size:0.3rem; " title="Gráfico do Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
                                contentIndiceSMLL += '            onclick="fAbrirModalGraficoPortfolio( \''+urlPadrao+'\',\''+CodAtivo+'\' );"> <i class="fa fa-area-chart" aria-hidden="true"></i> ';
                                contentIndiceSMLL += '         </a>';
                                contentIndiceSMLL += '      </td>';
                                contentIndiceSMLL += '    </tr>';

                            }
                                        
                        });
                   } //if ( lista.length > 0 ){

             } // if ( (DataSetRadar) && (DataSetRadar.data) && ( DataSetRadar.data.Lista) ){

             contentIndice += contentIndiceIBOV;
             contentIndice += contentIndiceIBXX;
             contentIndice += contentIndiceIDIV;
             contentIndice += contentIndiceSMLL;
             contentIndice += '  </tbody>';
             contentIndice += '</table>';
             DivListIndice.html("");
             DivListIndice.append( contentIndice );  
                             
             // var end = new Date().getTime();
             // var time = end - start;
             // sec = Math.floor((time/1000) % 60);
             // console.log('fMontarGridIndices - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

             // resolve(true);
             // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
         })
         .then( txt => {
                         //console.log('Sucesso: ' + txt);
         })
         .catch( txt => {
                         fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
         });
                                                                    
    } catch (e) {
                   if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fMontarGridRadar( urlPadrao ) {
    try {    

            promise = new Promise( (resolve, reject) => {
               
               resolve(true);

               // var start = new Date().getTime();
               // console.log('fMontarGridRadar - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
               
               var DivListRadar = $("#ListaRadar");
               DivListRadar.html("");

               var content = '';
               content     += '<table class="table table-sm table-hover table-condensed nowrap" border="0" cellspacing="0" width="100%" style="margin: 0px;">';
               content     += '  <tbody>';
               
               if ( (DataSetRadar) && (DataSetRadar.data) && ( DataSetRadar.data.Lista) ){

                   var lista = DataSetRadar.data.Lista;         

                   if ( lista.length > 0 ){

                      lista.sort(function(a, b){

                          var CodAtivoA    = a[0]; // 0-CODIGO  
                          var ValValorizA  = parseFloat( GetValorDecimal( a[2] ) ); // 2-Valorização(R$)
                          var PercValorizA = parseFloat( GetValorDecimal( a[3] ) ); // 3-Valorização(%)
                          
                          var CodAtivoB    = b[0];   // 0-CODIGO
                          var ValValorizB  = parseFloat( GetValorDecimal( b[2] ) ); // 2-Valorização(R$)
                          var PercValorizB = parseFloat( GetValorDecimal( b[3] ) ); // 3-Valorização(%)
                          
                          if ( ValValorizA < 0.00 && PercValorizA > 0.00 ) PercValorizA = PercValorizA * -1;
                          if ( ValValorizB < 0.00 && PercValorizB > 0.00 ) PercValorizB = PercValorizB * -1;

                          if(PercValorizA == PercValorizB) return 0;
                          return PercValorizA > PercValorizB? 1: -1;
                      });

                      lista.reverse();

                      $.each(lista, function (index, value) {

                          var CodAtivo    = value[0];                                  // 0-CODIGO
                          var Valor       = parseFloat( GetValorDecimal( value[1] ) ); // 1-PRECO
                          var ValValoriz  = parseFloat( GetValorDecimal( value[2] ) ); // 2-Valorização(R$)
                          var PercValoriz = parseFloat( GetValorDecimal( value[3] ) ); // 3-Valorização(%)

                          if ( (CodAtivo != 'IBOV') && (CodAtivo != 'IDIV') && (CodAtivo != 'SMLL') && (CodAtivo != 'IBXX') ){
                                content += '    <tr class="text-center"> ';
                                if( ValValoriz >  0.00 ) content += '      <td style="width:10px;"> <!-- <i class="fa fa-arrow-up faa-bounce ani mated text-success">  </i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" target="_blank"> <span class="text-success font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                if( ValValoriz == 0.00 ) content += '      <td style="width:10px;"> <!-- <i class="fa fa-arrow-right faa-flash ani mated text-primary"></i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" target="_blank"> <span class="text-primary font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                if( ValValoriz <  0.00 ) content += '      <td style="width:10px;"> <!-- <i class="fa fa-arrow-down faa-bounce ani mated text-danger" ></i> --> <a href="https://www.google.com.br/search?q='+CodAtivo+'" target="_blank"> <span class="text-danger  font-weight-bold" style="font-size: 11px;" >'+CodAtivo + '</span></a> </td>';
                                content += '      <td style="width:40px;"> <span class="text-dark  font-weight-bold" style="font-size: 11px;">  R$ '+fMascaraValor(Valor) +'</span></td>';
//                                if( ValValoriz >  0.00 ) content += '      <td style="width:50px;"> <span class="font-weight-normal text-success" style="font-size: 11px;"> +'+fMascaraValor(ValValoriz)+'</span> <span class="font-weight-normal text-success font-weight-bold" style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span></td>';
//                                if( ValValoriz == 0.00 ) content += '      <td style="width:50px;"> <span class="font-weight-normal text-primary" style="font-size: 11px;"> '+fMascaraValor(ValValoriz)+' </span> <span class="font-weight-normal text-primary font-weight-bold" style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
//                                if( ValValoriz <  0.00 ) content += '      <td style="width:50px;"> <span class="font-weight-normal text-danger"  style="font-size: 11px;"> '+fMascaraValor(ValValoriz)+' </span> <span class="font-weight-normal text-danger font-weight-bold"  style="font-size: 11px;"> ('+fMascaraValor(PercValoriz)+'%)'+'</span> </td>';
                                if( ValValoriz >  0.00 ) content += '      <td style="width:50px;"> <span class="font-weight-normal text-success font-weight-bold" style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'% </span> </td>';
                                if( ValValoriz == 0.00 ) content += '      <td style="width:50px;"> <span class="font-weight-normal text-primary font-weight-bold" style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'% </span> </td>';
                                if( ValValoriz <  0.00 ) content += '      <td style="width:50px;"> <span class="font-weight-normal text-danger font-weight-bold"  style="font-size: 11px;"> '+fMascaraValor(PercValoriz)+'% </span> </td>';
                                content += '      <td style="width:30px">';

                                if ( CodAtivo.includes('/BRL') ) {
                                    content += '         <a class="btn btn-sm btn-success btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.4rem; min-width: 1.4rem; width: 1.4rem; margin: 1px 1px; font-size:0.3rem; " title="Comprar Ativo '+CodAtivo+'" href="javascript:void(0);" ';
                                    content += '            onclick="fAbrirModalDetalheOperCripto( \''+urlPadrao+'\', \'\', \'Novo\', \'C\', \''+CodAtivo+'\', \'1\', \''+fMascaraValor(Valor)+'\' );"> <i class="fa fa-plus-square" aria-hidden="true"></i> ';
                                    content += '         </a>';
                                } else {
                                    content += '         <a class="btn btn-sm btn-success btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.4rem; min-width: 1.4rem; width: 1.4rem; margin: 1px 1px; font-size:0.3rem; " title="Comprar Ativo '+CodAtivo+'" href="javascript:void(0);" ';
                                    content += '            onclick="fAbrirModalDetalheOper( \''+urlPadrao+'\', \'\', \'Novo\', \'C\', \''+CodAtivo+'\', \'100\', \''+fMascaraValor(Valor)+'\' );"> <i class="fa fa-plus-square" aria-hidden="true"></i> ';
                                    content += '         </a>';
                                }

                                content += '         <a class="btn btn-sm btn-dark btn-icon btn-icon-mini btn-round btn-simple" style="height: 1.4rem; min-width: 1.4rem; width: 1.4rem; margin: 1px 1px; font-size:0.3rem; " title="Gráfico do Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
                                content += '            onclick="fAbrirModalGraficoPortfolio( \''+urlPadrao+'\',\''+CodAtivo+'\' );"> <i class="fa fa-area-chart" aria-hidden="true"></i> ';
                                content += '         </a>';
                                content += '      </td>';
                                content += '    </tr>';
                          }// if ( CodAtivo == 'IBOV' && CodAtivo == 'IDIV' && CodAtivo == 'SMLL' ){
                                      
                      });

                   } //if ( lista.length > 0 ){

               } // if ( (DataSetRadar) && (DataSetRadar.data) && ( DataSetRadar.data.Lista) ){

               content += '  </tbody>';
               content += '</table>';
               DivListRadar.html("");
               DivListRadar.append( content );              
               
               // var end = new Date().getTime();
               // var time = end - start;
               // sec = Math.floor((time/1000) % 60);
               // console.log('fMontarGridRadar - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");

               // resolve(true);
               // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
           })
           .then( txt => {
                           //console.log('Sucesso: ' + txt);
           })
           .catch( txt => {
                           fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
           });
                                                                    
    } catch (e) {
                   if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fMontarGridCarteira( urlPadrao, dataSet, IdPortfolio, TipoInvest ) {
 try {    

        promise = new Promise( (resolve, reject) => {
                       
           resolve(true);
           
           // var start = new Date().getTime();
           // console.log('fMontarGridCarteira - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                           
           $('#Grid').dataTable().fnClearTable();
           $("#Grid").dataTable({ bDestroy: true }).fnDestroy();

           $('#Grid').DataTable( {
               processing: true,
               serverSide: false,
               oLanguage: fTraduzirGrid(), 
               data: dataSet,
               aoColumns: [
                 { bSortable: true, bOrderable: true, sWidth: "10px",  targets:  0,  //  0-Ativo
                    render: function ( data, type, row ) {
                        if ( type == "display"){
                           var VlrValoriz = parseFloat(GetValorDecimal(row[7]));  // 7-Valorização(R$)
                           if( VlrValoriz >  0.00 ) return '<a style="text-deco ration:none;" href="https://www.google.com.br/search?q='+row[0]+'" target="_blank"> <span class="text-success font-weight-bold" style="font-size: 14px;" >'+row[0] + '</span></a>';
                           if( VlrValoriz == 0.00 ) return '<a style="text-deco ration:none;" href="https://www.google.com.br/search?q='+row[0]+'" target="_blank"> <span class="text-primary font-weight-bold" style="font-size: 14px;" >'+row[0] + '</span></a>';
                           if( VlrValoriz <  0.00 ) return '<a style="text-deco ration:none;" href="https://www.google.com.br/search?q='+row[0]+'" target="_blank"> <span class="text-danger  font-weight-bold" style="font-size: 14px;" >'+row[0] + '</span></a>';
                        }
                        return data;
                    }
                 }, //  0-Ativo
                 { bSortable: true, bOrderable: true, sWidth: "10px", targets:  1,   //  1-Quant
                    render: function ( data, type, row ) {
                        if ( type == "display") {
                            var TipoInvest = row[13]; // 13-TipoInvest
                            if ( TipoInvest == 'CRIPTO') return fMascaraValorSemLimite(parseFloat(GetValorDecimalMaior(row[1]))); //  1-Quant
                            return row[1];
                        }
                        return parseFloat(GetValorDecimalMaior(data));
                    }
                 }, //  1-Quant
                 { bSortable: true, bOrderable: true, sWidth: "10px", targets:  2,   // 2-Preco Medio
                    render: function ( data, type, row ) {
                        if ( type == "display") return "R$ " + row[2];
                        return parseFloat(GetValorDecimal(data));
                    }
                 }, // 2-Preco Medio
                 { bSortable: true, bOrderable: true, sWidth: "10px", targets:  3,   // 3-Preco Atual
                    render: function ( data, type, row ) {
                        if ( type == "display") return "R$ " + row[3];// 3-Preco Atual
                        return parseFloat(GetValorDecimal(data));
                    }
                 }, // 3-Preco Atual
                 { bSortable: true, bOrderable: true, sWidth: "10px", targets:  4,   // 4-Preco Teto
                    render: function ( data, type, row ) {
                        if ( type == "display"){

                            var CodAtivo = row[0];  //  0-CodAtivo
                            var Texto    = "DEFINIR";
                            var Preco    = '0,00';
                            var CorTexto = 'text-muted';

                            var PrecoAtual = parseFloat(GetValorDecimal(row[3])); // 3-Preco Atual
                            var PrecoTeto  = parseFloat(GetValorDecimal(row[4])); // 4-Preco Teto

                            if (  PrecoTeto > 0.00 ) {
                               Texto = "R$ " + row[4]; // 4-Preco Teto
                               Preco = row[4]; // 4-Preco Teto
                               if ( PrecoTeto  < PrecoAtual ) CorTexto = 'text-danger';
                               if ( PrecoTeto >= PrecoAtual ) CorTexto = 'text-success';
                            }

                            return '  <a class="font-weight-bold '+CorTexto+'" style="text-deco ration:none;" title="Clique Aqui para Definir o Preço Teto do Ativo '+CodAtivo+'" href="javascript:void(0);" '+
                                   '     onclick="fAbrirModalPrecoTetoAtivo( \''+urlPadrao+'\', \''+CodAtivo+'\', \''+Preco+'\' );"> '+Texto+' </i> '+
                                   '  </a>';
                        }
                        return parseFloat(GetValorDecimal(data));
                    }
                 }, // 4-Preco Teto
                 { bSortable: true, bOrderable: true, sWidth: "10px", targets:  5, // 5-Total Invest
                    render: function ( data, type, row ) {
                        if ( type == "display") return "R$ " + row[5];// 5-Total Invest
                        return parseFloat(GetValorDecimal(data));
                    }
                 }, // 5-Total Invest
                 { bSortable: true, bOrderable: true, sWidth: "10px", targets:  6, // 6-Total Atual
                    render: function ( data, type, row ) {
                        if ( type == "display") return "R$ " + row[6];// 6-Total Atual
                        return parseFloat(GetValorDecimal(data));
                    }
                 }, // 6-Total Atual
                 { bSortable: true, bOrderable: true, sWidth: "10px", targets:  7, // 7-Valorização(R$)
                    render: function ( data, type, row ) {
                        if ( type == "display") return "R$ " + row[7];// 7-Valorização(R$)
                        return parseFloat(GetValorDecimal(data));
                    }
                 },// 7-Valorização(R$)
                 { bSortable: true, bOrderable: true, sWidth: "10px",  targets: 8, // 8-Valorização(%)
                    render: function ( data, type, row ) {
                        if ( type == "display") return row[8]+"%";// 8-Valorização(%)
                        return parseFloat(GetValorDecimal(data));
                    }
                 }, // 8-Valorização(%)
                 { bSortable: true, bOrderable: true, sWidth: "10px", targets:  9, // 9-Total Proventos
                    render: function ( data, type, row ) {
                        if ( type == "display") return "R$ " + row[9];// 9-Total Rendimento
                        return parseFloat(GetValorDecimal(data));
                    }
                 }, // 9-Total Rendimento
                 { bSortable: true, bOrderable: true, sWidth: "10px", targets: 10, //  10-Yield on Cost
                    render: function ( data, type, row ) {
                        if ( type == "display") return row[10]+"%"; //  10-Yield on Cost
                        return parseFloat(GetValorDecimal(data));
                    }
                 }, //  10-Yield on Cost
                 { visible  : false,                                     targets: 11},  // 11-Total Aluguel
                 { visible  : false,                                     targets: 12},  // 12-IdAtivo
                 { visible  : false,                                     targets: 13 }, // 13-TipoInvest
                 { bSortable: false, bOrderable: false, sWidth:  "5px", targets:  14,   // 14-Acao
                    render: function ( data, type, row ) {

                        var btnDel = "";

                        if ( type == "display") {

                            var CodAtivo = row[0];  //  0-CodAtivo
                            var Quant    = row[1];  //  1-Quant
                            var Preco    = row[3];  //  3-Preco Atual
                            var IdAtivo  = row[12]; // 12-IdAtivo
                            var TipoInvest = row[13]; // 13-TipoInvest

                            if ( TipoInvest == 'CRIPTO' ) {
                                btnDel += '<a class="btn btn-sm btn-success btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem; " title="Comprar Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAbrirModalDetalheOperCripto( \''+urlPadrao+'\', \'\', \'Novo\', \'C\', \''+CodAtivo+'\', \'1\', \''+Preco+'\' );"> <i class="fa fa-plus-square" aria-hidden="true"></i></a>';
                                btnDel += '&nbsp;';
                                btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Vender Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fAbrirModalDetalheOperCripto( \''+urlPadrao+'\', \'\', \'Novo\', \'V\', \''+CodAtivo+'\', \''+Quant+'\', \''+Preco+'\' );"> <i class="fa fa-minus-square" aria-hidden="true"></i></a>';
                            } else {
                                btnDel += '<a class="btn btn-sm btn-success btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem; " title="Comprar Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAbrirModalDetalheOper( \''+urlPadrao+'\', \'\', \'Novo\', \'C\', \''+CodAtivo+'\', \'100\', \''+Preco+'\' );"> <i class="fa fa-plus-square" aria-hidden="true"></i> </a>';
                                btnDel += '&nbsp;';
                                btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Vender Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fAbrirModalDetalheOper( \''+urlPadrao+'\', \'\', \'Novo\', \'V\', \''+CodAtivo+'\', \''+Quant+'\', \''+Preco+'\' );"> <i class="fa fa-minus-square" aria-hidden="true"></i> </a>';
                            }

                            btnDel += '&nbsp;';
                            btnDel += '<a class="btn btn-sm btn-dark btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem; " title="Gráfico do Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fAbrirModalGraficoPortfolio( \''+urlPadrao+'\',\''+CodAtivo+'\' );"> <i class="fa fa-area-chart" aria-hidden="true"></i> </a>';

                            if ( IdPortfolio != "" ){
                               btnDel += '&nbsp;';
                               btnDel += '<a class="btn btn-sm btn-dark btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem; " title="Remover Ativo '+CodAtivo+' do Portfólio Personalizado" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fAbrirModalRemoverAtivo( \''+urlPadrao+'\', \''+IdPortfolio+'\', \''+IdAtivo+'\', \''+CodAtivo+'\' );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> </a>';
                            }
                        }

                        return  btnDel;
                    }
                 } //  14-Acao
           ],
           createdRow : function(row,data,dataIndex) {   
                                                                                          
               var VlrValoriz = parseFloat(GetValorDecimal( data[7] ));  // 7-Valorização(R$)
               
               $('td', row).addClass('text-center');
               
               $('td', row).eq(0).addClass('font-weight-bold'); // 0-Ativo
               $('td', row).eq(7).addClass('font-weight-bold'); // 7-Valorização(R$)
               $('td', row).eq(8).addClass('font-weight-bold'); // 8-Valorização(%)
               $('td', row).eq(9).addClass('font-weight-bold'); // 9-Total Proventos
                              
               if      ( VlrValoriz == 0 ) $('td', row).eq(0).addClass('table-muted')
               else if ( VlrValoriz > 0  ) $('td', row).eq(0).addClass('text-success')
               else if ( VlrValoriz < 0  ) $('td', row).eq(0).addClass('text-danger');
                              
               if      ( VlrValoriz == 0 ) $('td', row).eq(7).addClass('table-muted')  // 7-Valorização(R$)
               else if ( VlrValoriz > 0  ) $('td', row).eq(7).addClass('text-success') // 7-Valorização(R$)
               else if ( VlrValoriz < 0  ) $('td', row).eq(7).addClass('text-danger'); // 7-Valorização(R$)
                              
               if      ( VlrValoriz == 0 ) $('td', row).eq(8).addClass('table-muted')  // 8-Valorização(%)
               else if ( VlrValoriz > 0  ) $('td', row).eq(8).addClass('text-success') // 8-Valorização(%)
               else if ( VlrValoriz < 0  ) $('td', row).eq(8).addClass('text-danger'); // 8-Valorização(%)
                                                                            
           }, //createdRow
           initComplete: function( settings, json ) {
              finalizarAnimacaoPesquisa();
                 // var end = new Date().getTime();
                 // var time = end - start;
                 // sec = Math.floor((time/1000) % 60);
                 // console.log('fMontarGridCarteira - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");
                           
           }, //initComplete
             order: [[ 8, "desc" ]], // 0, "asc" 0-Ativo                                             
             dom: 'frtBpi', 
             buttons: [  
                          {
                             extend:    'excelHtml5',
                             text:      '<i class="fa fa-file-excel-o"></i> Excel',
                             className: 'btn btn-outline-default btn-sm',
                             title: NOME_PROJETO + ' - Portfólio',
                             titleAttr: 'Excel',
                             exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10 ] },
                             customizeData: function (data) {
                                for (var i = 0; i < data.body.length; i++) {
                                    for (var j = 0; j < data.body[i].length; j++) {
                                           if (j == 1) data.body[i][j] = '\u200C' + data.body[i][j]; // Formatando a Coluna = 1-Quant
                                    }
                                }
                            } 
                          }, 
                          {
                            extend: 'csvHtml5',
                            charset: 'UTF-8',
                            fieldSeparator: ';',
                            titleAttr: 'CSV',
                            text:      '<i class="fa fa-file-o"></i> CSV',
                            className: 'btn btn-outline-default btn-sm',
                            title: NOME_PROJETO + ' - Portfólio',
                            bom: true,
                            exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10 ] } 
                          },
                          {
                            extend: 'pdfHtml5',
                             text:      '<i class="fa fa-file-pdf-o"></i> PDF',
                            className: 'btn btn-default btn-sm',
                            titleAttr: 'PDF',
                            title: NOME_PROJETO + ' - Portfólio', 
                            //messageTop: 'xxxx',
                            orientation: 'landscape',
                            pageSize: 'A3',
                            alignment: 'center',
                            exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10 ] },
                            footer: true,
                            customize: function (doc) { 
                                            doc.defaultStyle.fontSize = 12; 
                                            doc.styles.tableHeader.fontSize = 14; 
                                            doc.styles.tableHeader.alignment = 'center';
                                            doc.styles.title.bold = true;
                                            doc.styles.tableHeader.bold = true;
                                            // doc.styles.tableHeader.color = '#ffffff';
                                            // doc.styles.tableHeader.fillColor = '#666666';
                                            // doc.styles.tableBodyOdd.fillColor = '#ffffff';
                                            // doc.styles.tableBodyEven.fillColor = '#e9e9e9';
                                            doc.styles.tableHeader.noWrap = true;
                            }
                          },
                          {
                            extend: 'print',
                            text:      '<i class="fa fa-print"></i> Imprimir',
                            title: NOME_PROJETO + ' - Portfólio',
                            titleAttr: 'Imprimir',
                            className: 'btn btn-default btn-sm',
                            exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10 ] }
                          }
             ],
             bFilter: false,
             bInfo: false,
             bLengthChange: false,
             bSearchable: false,
             bOrderable: true,
             bSortable: true,
             bAutoWidth: false,
             sAutoWidth: false,
             bPaginate: false,
             bOrdering: true
           });           

           // resolve(true);
           // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
       })
       .then( txt => {
                       //console.log('Sucesso: ' + txt);
       })
       .catch( txt => {
                       fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
       });
                                                                    
    } catch (e) {
         finalizarAnimacaoPesquisa();
         fLimparSomenteGrid( urlPadrao );
         if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fMontarPagina( urlPadrao ){
                
     promise = new Promise( (resolve, reject) => {
                         
         resolve(true);

         // var start = new Date().getTime();
         // console.log('fMontarPagina - INICIO - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) );
                         
         fLimparPagina( urlPadrao );
         finalizarAnimacaoPesquisa();
         iniciarAnimacaoPesquisar();

         var IdPortfolio = fGetAbaIdPortfolio();
         var TipoInvest  = fGetAbaTipoPortfolio();

         if ( IdPortfolio == "" ){
             //Portfolio Default
             $('#btnPortAddAtivo').hide();
             $('#btnPortAltPortfolio').hide();
             $('#btnPortExcPortfolio').hide();
             $('#btnPortAddPortfolio').show();
         }else{
             //Portfolio Personalizado
             $('#btnPortAddAtivo').show();
             $('#btnPortAltPortfolio').show();
             $('#btnPortExcPortfolio').show();
             $('#btnPortAddPortfolio').hide();
         }              

         if ( TipoInvest == "ACAO" || TipoInvest == "FII" || TipoInvest == "ETF" || TipoInvest == "BDR" || TipoInvest == "CRIPTO" ) $('#btnPortEmailInfo').hide();
         if ( TipoInvest != "ACAO" && TipoInvest != "FII" && TipoInvest != "ETF" && TipoInvest != "BDR" && TipoInvest != "CRIPTO" ) $('#btnPortEmailInfo').show();

         var TotInvest       = 0.00;
         var TotAtual        = 0.00;
         var TotAtualAtivos  = 0.00; 
         var TotValorizacao  = 0.00;
         var PercValorizacao = 0.00;         
         var TotRend         = 0.00;                               
         var TotAlug         = 0.00;
         var TotGanhoPerda   = 0.00;
         var PercGanhoPerda  = 0.00;

         var arCodAtivos     = [];
         var arValInvest     = [];
         var arValAtual      = [];
         var arValRenb       = [];
         var arValValoriz    = [];
         var arPercValoriz   = [];
         var arSetorNome     = [];
         var arSetorQtde     = [];
         var arSetorTotal    = [];
         var arSubSetorNome  = [];
         var arSubSetorQtde  = [];
         var arSubSetorTotal = [];
         var arSegmentoNome  = [];
         var arSegmentoQtde  = [];
         var arSegmentoTotal = [];
         var arProftfolio    = [];
         var arDataSet       = [];

          $.ajax({
                 cache   : "false",
                 dataType: "json",
                 async   : true,
                 type    : "POST",
                 url     : urlPadrao + "portfolio/DataSetPagina",
                 data    : { },
                 success: function(result) {

                    var resultado = result.data.Resultado;
                    var mensagem  = result.data.Mensagem;
                    var lista     = result.data.Lista;

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

                        DataSetPagina = result;

                         if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){

                           var lista = DataSetPagina.data.Lista;

                           if ( lista.length > 0 ){

                               var idx = -1;
                               $.each(lista, function (index, value) {

                                  var CartId        = value.CartId;
                                  var AtvTipoInvest = value.AtvTipoInvest;

                                  if ( (IdPortfolio == "") || (IdPortfolio == CartId ) ){
                                        if ( (TipoInvest == "") || (TipoInvest == AtvTipoInvest) ){

                                            // var CartId = value.CartId;
                                            // var CartNome = value.CartNome;
                                            var SetorId           = value.SetorId;
                                            var SetorNome         = value.SetorNome;
                                            var SubSetorId        = value.SubSetorId;
                                            var SubSetorNome      = value.SubSetorNome;
                                            var SegmentoId        = value.SegmentoId;
                                            var SegmentoNome      = value.SegmentoNome;
                                            var AtvId             = value.AtvId;
                                            var AtvTipoInvest     = value.AtvTipoInvest;
                                            var AtvCodigo         = value.AtvCodigo;
                                            var AtvQtde           = value.AtvQtde;
                                            var AtvPrecoMedio     = value.AtvPrecoMedio; //parseFloat(GetValorDecimal( value.AtvPrecoMedio ));
                                            var AtvPrecoAtual     = value.AtvPrecoAtual; //parseFloat(GetValorDecimal( value.AtvPrecoAtual ));
                                            var AtvPrecoTeto      = value.AtvPrecoTeto; //parseFloat(GetValorDecimal( value.AtvPrecoTeto ));
                                            var AtvVlrValorizDia  = value.AtvVlrValorizDia; //parseFloat(GetValorDecimal(  ));
                                            var AtvPercValorizDia = value.AtvPercValorizDia; // parseFloat(GetValorDecimal(  ));
                                            var AtvTotInvest      = value.AtvTotInvest; // parseFloat(GetValorDecimal( ));
                                            var AtvTotAtual       = value.AtvTotAtual; // parseFloat(GetValorDecimal(  ));
                                            var AtvTotValoriz     = value.AtvTotValoriz; // parseFloat(GetValorDecimal(  ));
                                            var AtvPercValoriz    = value.AtvPercValoriz; // parseFloat(GetValorDecimal(  ));
                                            var AtvTotProv        = value.AtvTotProv; // parseFloat(GetValorDecimal(  ));
                                            var AtvTotAlug        = value.AtvTotAlug; // parseFloat(GetValorDecimal( value.AtvTotAlug ));
                                            var AtvYieldOnCost    = value.AtvYieldOnCost;

                                            TotInvest      += parseFloat(GetValorDecimal( AtvTotInvest  ));
                                            TotAtual       += parseFloat(GetValorDecimal( AtvTotAtual   ));
                                            TotValorizacao += parseFloat(GetValorDecimal( AtvTotValoriz ));
                                            TotRend        += parseFloat(GetValorDecimal( AtvTotProv    ));
                                            TotAlug        += parseFloat(GetValorDecimal( AtvTotAlug    ));

                                            arProftfolio.push({ Codigo: AtvCodigo, Quant: AtvQtde, PrecoAtual: AtvPrecoAtual, VlrValorizDia: AtvVlrValorizDia, PercValorizDia: AtvPercValorizDia, TipoInvest: AtvTipoInvest });
                                            arDataSet.push([ AtvCodigo, AtvQtde, AtvPrecoMedio, AtvPrecoAtual, AtvPrecoTeto, AtvTotInvest, AtvTotAtual, AtvTotValoriz, AtvPercValoriz, AtvTotProv, AtvYieldOnCost, AtvTotAlug, AtvId, AtvTipoInvest ]);

                                            AtvTotInvest  = parseFloat(GetValorDecimal( AtvTotInvest ));
                                            AtvTotValoriz = parseFloat(GetValorDecimal( AtvTotValoriz ));
                                            AtvTotAtual   = parseFloat(GetValorDecimal( AtvTotAtual ));
                                            AtvTotProv    = parseFloat(GetValorDecimal( AtvTotProv ));
                                            AtvTotAlug    = parseFloat(GetValorDecimal( AtvTotAlug ));

                                            idx += 1;
                                            arCodAtivos[idx]   = AtvCodigo;
                                            arValInvest[idx]   = AtvTotInvest;
                                            arValAtual[idx]    = AtvTotAtual;
                                            arValRenb[idx]     = AtvTotProv + AtvTotAlug;
                                            arValValoriz[idx]  = AtvTotValoriz;
                                            arPercValoriz[idx] = ( ( AtvTotValoriz != 0 && AtvTotInvest > 0 ) ? (( AtvTotValoriz / AtvTotInvest ) * 100) : 0.00 );

                                            if ( AtvTipoInvest == "ACAO" ){
                                                   //console.log('Cod: ' + AtvCodigo + ' - Vlr: ' + AtvTotAtual);
                                                   TotAtualAtivos += AtvTotAtual;
                                                   if ( !arSetorQtde[SetorId]                                   ) arSetorQtde[SetorId]                                   = 0;
                                                   if ( !arSetorTotal[SetorId]                                  ) arSetorTotal[SetorId]                                  = 0.00;
                                                   if ( !arSubSetorQtde[SetorId+'-'+SubSetorId]                 ) arSubSetorQtde[SetorId+'-'+SubSetorId]                 = 0;
                                                   if ( !arSubSetorTotal[SetorId+'-'+SubSetorId]                ) arSubSetorTotal[SetorId+'-'+SubSetorId]                = 0.00;
                                                   if ( !arSegmentoQtde[SetorId+'-'+SubSetorId+'-'+SegmentoId]  ) arSegmentoQtde[SetorId+'-'+SubSetorId+'-'+SegmentoId]  = 0;
                                                   if ( !arSegmentoTotal[SetorId+'-'+SubSetorId+'-'+SegmentoId] ) arSegmentoTotal[SetorId+'-'+SubSetorId+'-'+SegmentoId] = 0.00;
                                                   arSetorNome[SetorId]                                    = SetorNome;
                                                   arSetorQtde[SetorId]                                   += 1;
                                                   arSetorTotal[SetorId]                                  += AtvTotAtual;
                                                   arSubSetorNome[SetorId+'-'+SubSetorId]                  = SubSetorNome;
                                                   arSubSetorQtde[SetorId+'-'+SubSetorId]                 += 1;
                                                   arSubSetorTotal[SetorId+'-'+SubSetorId]                += AtvTotAtual;
                                                   arSegmentoNome[SetorId+'-'+SubSetorId+'-'+SegmentoId]   = SegmentoNome;
                                                   arSegmentoQtde[SetorId+'-'+SubSetorId+'-'+SegmentoId]  += 1;
                                                   arSegmentoTotal[SetorId+'-'+SubSetorId+'-'+SegmentoId] += AtvTotAtual;
                                            } // if ( AtvTipoInvest == "ACAO" ){

                                        } // if ( (TipoInvest == "") || (TipoInvest == value.AtvTipoInvest) ){
                                  } // if ( (IdPortfolio == "") || (IdPortfolio == value.CartId) ){

                               }); // $.each(lista, function (index, value) {

                               if ( TotValorizacao != 0 && TotInvest > 0 ) PercValorizacao = ( TotValorizacao / TotInvest ) * 100;
                               TotGanhoPerda = TotValorizacao + TotRend + TotAlug;
                               if ( TotGanhoPerda != 0 && TotInvest > 0 ) PercGanhoPerda = ( TotGanhoPerda / TotInvest ) * 100;

                           } // if ( lista.length > 0 ){

                         } //if ( (DataSetPagina) && (DataSetPagina.data) && ( DataSetPagina.data.Lista) ){

                         setTimeout(() => { fMontarTotalizadores( urlPadrao, TotInvest, TotAtual, TotValorizacao, PercValorizacao, TotRend, TotAlug, TotGanhoPerda, PercGanhoPerda ); }, 1);
                         setTimeout(() => { fMontarGraficoCarteiraGeral( urlPadrao, TotInvest, TotAtual, TotRend, TotAlug ); }, 1);

                         setTimeout(() => { fMontarGridValorizacaoDia( urlPadrao, arProftfolio ); }, 100);
                         setTimeout(() => { fMontarGridPercentualAtivos( urlPadrao, arCodAtivos, arValInvest, arValAtual ); }, 100);

                         setTimeout(() => { fMontarGraficoCarteiraAtivos( urlPadrao, arCodAtivos, arValInvest, arValAtual, arValValoriz, arValRenb ); }, 200);
                         setTimeout(() => { fMontarGridCarteira( urlPadrao, arDataSet, IdPortfolio, TipoInvest ); }, 200);
                         setTimeout(() => { fMontarGraficoTotalValorizacao( urlPadrao, arCodAtivos, arValValoriz ); }, 200);
                         setTimeout(() => { fMontarGraficoPercentualValorizacao( urlPadrao, arCodAtivos, arPercValoriz ); }, 200);
                         setTimeout(() => { fMontarGraficoTotalProventos( urlPadrao, arCodAtivos, arValRenb ); }, 200);

                         setTimeout(() => { fMontarGraficoPesoAtivos( urlPadrao, arCodAtivos, arValAtual ); }, 500);
                         setTimeout(() => { fMontarGraficoPesoSetores( urlPadrao, arSetorNome, arSetorTotal ); }, 500);
                         setTimeout(() => { fMontarGraficoPesoSubSetores( urlPadrao, arSubSetorNome, arSubSetorTotal ); }, 500);
                         setTimeout(() => { fMontarGraficoPesoSegmentos( urlPadrao, arSegmentoNome, arSegmentoTotal ); }, 500);

                         //console.log('Total: ' + TotAtualAtivos);
                         setTimeout(() => { fMontarGridSetores( urlPadrao, TotAtualAtivos, arSetorQtde, arSetorTotal, arSubSetorQtde, arSubSetorTotal, arSegmentoQtde, arSegmentoTotal ); }, 500);

                         finalizarAnimacaoPesquisa();

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

          fCarregarPaginaIndiceRadar( urlPadrao );
         // setTimeout(() => { fMontarGridIndices( urlPadrao ); }, 100);
         // setTimeout(() => { fMontarGridRadar( urlPadrao ); }, 100);

         // var end = new Date().getTime();
         // var time = end - start;
         // sec = Math.floor((time/1000) % 60);
         // console.log('fMontarPagina - FIM - ' + new Intl.DateTimeFormat('pt-BR', {year: 'numeric', month: 'numeric', day: 'numeric',hour: 'numeric', minute: 'numeric', second: 'numeric',hour12: false,timeZone: 'America/Sao_Paulo' }).format(new Date()) + " - TEMPO - " + time + " milliseconds / in " + sec + " seconds");
         
         // resolve(true);
         // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
    })
    .then( txt => {
                   //console.log('Sucesso: ' + txt);
    })
    .catch( txt => {
                   fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    });

}

async function fCarregarPaginaIndiceRadar( urlPadrao ){
    try {

          promise = new Promise( (resolve, reject) => {

               $("#ListaIndice").html("");
               $("#ListaRadar").html("");

                $.ajax({
                   cache   : "false",
                   dataType: "json",
                   async   : true,
                   type    : "POST",
                   url     : urlPadrao + "portfolio/ativosNoRadar",
                   data    : { },
                   success: function(result) {

                       var resultado = result.data.Resultado;
                       var mensagem  = result.data.Mensagem;
                       var lista     = result.data.Lista;

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
                           DataSetRadar = result;
                           fMontarGridIndices( urlPadrao );
                           fMontarGridRadar( urlPadrao );
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

async function fRecarregarPagina( urlPadrao, Id ){
    try {   

          promise = new Promise( (resolve, reject) => {
               
               resolve(true);

               fLimparPagina( urlPadrao );

               finalizarAnimacaoPesquisa();
               iniciarAnimacaoPesquisar();
               
               // DataSetPagina = [];
               // DataSetRadar  = [];

               // fCarregarListaPortfolios( urlPadrao );

               var IdPortfolio = fGetAbaIdPortfolio();
               var TipoInvest  = fGetAbaTipoPortfolio();


               var ActiveCriptos = ( ( IdPortfolio == "" && TipoInvest == "CRIPTO" ) ? " active" : "" );
               var ActiveBdrs    = ( ( IdPortfolio == "" && TipoInvest == "BDR"    ) ? " active" : "" );
               var ActiveIndices = ( ( IdPortfolio == "" && TipoInvest == "ETF"    ) ? " active" : "" );
               var ActiveFundos  = ( ( IdPortfolio == "" && TipoInvest == "FII"    ) ? " active" : "" );
               var ActiveAcoes   = ( ( IdPortfolio == "" && TipoInvest == "ACAO"   ) ? " active" : "" );
               var ActivePortf   = ( ( IdPortfolio == "" && TipoInvest == ""       ) ? " active" : "" );
               
               var SelectedCriptos = ( ( IdPortfolio == "" && TipoInvest == "CRIPTO" ) ? "true" : "false" );
               var SelectedBdrs    = ( ( IdPortfolio == "" && TipoInvest == "BDR"    ) ? "true" : "false" );
               var SelectedIndices = ( ( IdPortfolio == "" && TipoInvest == "ETF"    ) ? "true" : "false" );
               var SelectedFundos  = ( ( IdPortfolio == "" && TipoInvest == "FII"    ) ? "true" : "false" );
               var SelectedAcoes   = ( ( IdPortfolio == "" && TipoInvest == "ACAO"   ) ? "true" : "false" );
               var SelectedPortf   = ( ( IdPortfolio == "" && TipoInvest == ""       ) ? "true" : "false" );

               $('#TabPortfolios').empty(); 
               $("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActiveCriptos+'" id="AbaPortfolioCriptos" data-toggle="tab" href="#PortfolioCriptos" role="tab" aria-controls="PortfolioCriptos" aria-selected="'+SelectedCriptos+'" title="Portfólio CRIPTOs - Todos os Criptos da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; CRIPTOs   </a> </li>' );
               $("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActiveBdrs+'"    id="AbaPortfolioBdrs"    data-toggle="tab" href="#PortfolioBdrs"    role="tab" aria-controls="PortfolioBdrs"    aria-selected="'+SelectedBdrs+'"    title="Portfólio BDRs - Todos os Bdrs da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; BDRs   </a> </li>' );
               $("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActiveIndices+'" id="AbaPortfolioIndices" data-toggle="tab" href="#PortfolioIndices" role="tab" aria-controls="PortfolioIndices" aria-selected="'+SelectedIndices+'" title="Portfólio ETFs - Todos os Etfs da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; ETFs  </a> </li>' );
               $("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActiveFundos+'"  id="AbaPortfolioFundos"  data-toggle="tab" href="#PortfolioFundos"  role="tab" aria-controls="PortfolioFundos"  aria-selected="'+SelectedFundos+'"  title="Portfólio FIIs - Todos os Fiis da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; FIIs    </a> </li>' );
               $("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActiveAcoes+'"   id="AbaPortfolioAcoes"   data-toggle="tab" href="#PortfolioAcoes"   role="tab" aria-controls="PortfolioAcoes"   aria-selected="'+SelectedAcoes+'"   title="Portfólio Ações - Todos as Ações da Carteira">    <i class="fa fa-bar-chart"></i>&nbsp; AÇÕES  </a> </li>' );
               $("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActivePortf+'"   id="AbaPortfolio"        data-toggle="tab" href="#Portfolio"        role="tab" aria-controls="Portfolio"        aria-selected="'+SelectedPortf+'"   title="Portfólio Completo - Todos os Ativos da Carteira"><i class="fa fa-bar-chart"></i>&nbsp; Portfólio </a> </li>' );

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
                            fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_AVISO, mensagem);
                            return false;
                         } else if (resultado == "FALHA") {
                            fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, mensagem);
                            return false;
                        } else if (resultado == "OK") {    
                                                        
                            $('#TabPortfolios').empty();

                            if ( lista.length > 0 ){
                                lista.reverse();
                                $.each(lista, function (index, value) {
                                   var ActivePerson   = ( ( IdPortfolio != "" && IdPortfolio == value[0] && TipoInvest == "" ) ? " active" : "" );
                                   var SelectedPerson = ( ( IdPortfolio != "" && IdPortfolio == value[0] && TipoInvest == "" ) ? "true" : "false" );
                                   $('<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActivePerson+'" id="Aba'+value[0]+'" data-toggle="tab" href="#'+value[0]+'" role="tab" aria-controls="'+value[0]+'" aria-selected="'+SelectedPerson+'" title="Portfólio Personalizado - Ativos Selecionados da Carteira"><i class="fa fa-sliders"></i>&nbsp; '+value[1]+'</a> </li>').appendTo('#TabPortfolios');
                                });
                            }

                            $("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActiveCriptos+'" id="AbaPortfolioCriptos" data-toggle="tab" href="#PortfolioCriptos" role="tab" aria-controls="PortfolioCriptos" aria-selected="'+SelectedCriptos+'"  title="Portfólio CRIPTOs - Todos os Criptos da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; CRIPTOs     </a> </li>' );
                            $("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActiveBdrs+'"    id="AbaPortfolioBdrs"    data-toggle="tab" href="#PortfolioBdrs"    role="tab" aria-controls="PortfolioBdrs"    aria-selected="'+SelectedBdrs+'"    title="Portfólio BDRs - Todos os Bdrs da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; BDRs     </a> </li>' );
                            $("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActiveIndices+'" id="AbaPortfolioIndices" data-toggle="tab" href="#PortfolioIndices" role="tab" aria-controls="PortfolioIndices" aria-selected="'+SelectedIndices+'" title="Portfólio ETFs - Todos os Etfs da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; ETFs     </a> </li>' );
                            $("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActiveFundos+'"  id="AbaPortfolioFundos"  data-toggle="tab" href="#PortfolioFundos"  role="tab" aria-controls="PortfolioFundos"  aria-selected="'+SelectedFundos+'"  title="Portfólio FIIs - Todos os Fiis da Carteira">    <i class="fa fa-bar-chart"></i>&nbsp; FIIs     </a> </li>' );
                            $("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActiveAcoes+'"   id="AbaPortfolioAcoes"   data-toggle="tab" href="#PortfolioAcoes"   role="tab" aria-controls="PortfolioAcoes"   aria-selected="'+SelectedAcoes+'"   title="Portfólio Ações - Todos as Ações da Carteira">      <i class="fa fa-bar-chart"></i>&nbsp; AÇÕES  </a> </li>' );
                            $("#TabPortfolios").append( '<li class="nav-item"> <a style="font-size: 10px; " class="border border-secondary nav-link'+ActivePortf+'"   id="AbaPortfolio"        data-toggle="tab" href="#Portfolio"        role="tab" aria-controls="Portfolio"        aria-selected="'+SelectedPortf+'"   title="Portfólio Completo - Todos os Ativos da Carteira">  <i class="fa fa-bar-chart"></i>&nbsp; Portfólio </a> </li>' );

                            $('#TabPortfolios a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
                                //e.target        // newly activated tab
                                //e.relatedTarget // previous active tab
                                fMontarPagina( urlPadrao );
                            });

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

               fMontarPagina( urlPadrao );

               // fCarregarPaginaIndiceRadar( urlPadrao );

               // resolve(true);
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
