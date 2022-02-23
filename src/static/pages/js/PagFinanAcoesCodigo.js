
async function fCarregarGraficoTradingViewCodigo( urlPadrao, CodAtivo ) {
    try {

         promise = new Promise( (resolve, reject) => {

          if ( CodAtivo.includes('/BRL') ) {
               CodAtivo = "BINANCE:" + CodAtivo.replace('/BRL','BRL')
               new TradingView.widget({
                   "container_id": "DivGraficoTradingViewCodigo",
                   "width": "100%",
                   "height": "500px",
                   "symbol": CodAtivo,
                   "interval": "D", //"D"
                   "timezone": "America/Sao_Paulo",
                   "locale": "br",
                   "theme": "Light", // "dark", /  "Light",
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
                   "container_id": "DivGraficoTradingViewCodigo",
                   "customer": "bovespa",
                   "width": "100%",
                   "height": "500px",
                   "symbol": CodAtivo,
                   "interval": "D", //"D"
                   "timezone": "America/Sao_Paulo",
                   "locale": "br",
                   "theme": "Light", // "dark", /  "Light",
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
                   // "range": "YTD",
                   //"autosize": true,
                   //"noGraph": true,
                   // "show_popup_button": false,
                   // "popup_width": "1000",
                   // "popup_height": "650",
                   // "calendar": false,
                   // "hotlist": true,
               });
          }


          resolve(true);
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