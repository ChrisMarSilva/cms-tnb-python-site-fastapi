
var template_app_dfc = `
<div>
    <div class="row clearfix">
        <div class="col-xl-12 col-lg-12 col-md-12" style="padding-right: 4px; border: 0px solid red;">
            <div class="card border">
                <div class="header">
                    <div class="row clearfix align-items-end">
                        <div class="col-3">
                            <h2><strong>Fluxo de Caixa</strong></h2>
                        </div>
                        <div class="col-7">
                            <ul class="nav nav-tabs card-header-tabs font-weight-bold justify-content-center" style="margin: 0px; padding: 0px;">
                                <li class="nav-item"><a style="font-size: 13px; " class="nav-link active" data-toggle="tab" href="#TabDFCDados">Dados</a></li>
                                <li class="nav-item"><a style="font-size: 13px; " class="nav-link" data-toggle="tab" href="#TabDFCGraficos">Gráficos</a></li>
                            </ul>
                        </div>
                        <div class="col-2">
                            <select v-on:change="changeTipoFinan($event)" style="font-size:12px;" class="form-control"> <option value="A">Anual</option> <option value="T" selected="selected">Trimestral</option> </select>
                        </div>
                    </div>
                </div>
                <div class="body">
                    <div class="tab-content">
                        <div role="tabpanel" class="tab-pane active" id="TabDFCDados">

                            <div v-if="loading" class="text-center">
                                <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
                            </div>
                            <div v-else>
                                <div v-if="errored" class="text-cente">
                                    Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                                 </div>
                                <div v-else>
                                    <div v-html="pagina"> </div>
                                </div>
                            </div>

                        </div>
                        <div role="tabpanel" class="tab-pane in" id="TabDFCGraficos">

                            <div v-if="chartLoading" class="text-center">
                                <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
                            </div>
                            <div v-else>
                                <div v-if="chartErrored" class="text-cente">
                                    Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                                 </div>
                                <div v-else>
                                    <highcharts :options="chartOptions"></highcharts>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
`;

var methods_app_dfc = {

    async changeTipoFinan(event) {
        this.buscar_dados( event.target.value )
        this.buscar_dados_grafico( event.target.value )
    },

    async buscar_dados(TipoFinan = 'T') {

        this.loading = true
        this.errored = false
        this.pagina = null

        axios({
          method: 'post',
          url: "/finan/acoes/grid_fluxo_caixa",
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify({ CodAtivo: codigo, TipoFinan : TipoFinan }),
        })
        .then( (response) => {
             this.pagina = response.data
        })
        .catch( (error) => {
            this.errored = true
            console.log('@TamoNaBolsa:Error',error)
        })
        .finally( () => {
            this.loading = false
        })

    },

    async buscar_dados_grafico(TipoFinan = 'T') {

        this.chartLoading = true
        this.chartErrored = false
        this.chartOptions = null

        axios({
          method: 'post',
          url: "/finan/acoes/grid_dfc",
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify({ CodAtivo: codigo, TipoFinan : TipoFinan }),
        })
        .then( (response) => {

            let resultado = response.data.data.Resultado

            if (resultado == "OK") {

                let dados = response.data.data.Dados

                let arTitulo = dados.listaTitulo
                let arCaixaLiquidoOperac = dados.listaCaixaLiquidoOperac //.map(Math.abs)
                let arCaixaLiquidoInvest = dados.listaCaixaLiquidoInvest //.map(Math.abs)
                let arCaixaLiquidoFinan = dados.listaCaixaLiquidoFinan //.map(Math.abs)
                let arCaixaTotal = dados.listaCaixaTotal //.map(Math.abs)
                let arCaixaLivre = dados.listaCaixaLivre //.map(Math.abs)

                this.chartOptions = {
                    chart: { zoomType: 'xy' },
                    title: { text: null },
                    xAxis: { categories: arTitulo, crosshair: true },
                    yAxis: [
                        { allowDecimals: false, title: { text: null, style: { color: Highcharts.getOptions().colors[1] } }, labels: { format: 'R$ {value:.,2f}', style: { color: Highcharts.getOptions().colors[1] } },                },// Primary yAxis
                    ],
                    plotOptions: {column: {stacking: 'normal'}, area: {stacking: 'normal'}, },
                    series: [
                        {stack: 'Valor', visible: true,  type: 'column', name: 'Fluco de Caixa Operacionais', yAxis: 0, data: arCaixaLiquidoOperac, tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br /> '; }, shared: true } } ,
                        {stack: 'Valor', visible: true,  type: 'column', name: 'Fluco de Caixa Investimento', yAxis: 0, data: arCaixaLiquidoInvest, tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true } } ,
                        {stack: 'Valor', visible: true, type: 'column', name: 'Fluco de Caixa Financiamento', yAxis: 0, data: arCaixaLiquidoFinan, tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true } } ,
                        {stack: 'Valor', visible: true, type: 'column', name: 'Fluco de Caixa Total', yAxis: 0, data: arCaixaTotal, tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true } } ,
                        {stack: 'Valor', visible: true,  type: 'column', name: 'Fluco de Caixa Livre', yAxis: 0, data: arCaixaLivre, tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true } } ,
                    ]
                  }

                return true;
            } else {
                this.chartErrored = true;
                let mensagem = response.data.data.Mensagem
                console.log('@TamoNaBolsa:Error',mensagem)
            }
        })
        .catch( (error) => {
            this.chartErrored = true
            console.log('@TamoNaBolsa:Error',error)
        })
        .finally( () => {
            this.chartLoading = false
        })
    },

};

var data_app_dfc = {
    loading: true,
    errored: false,
    pagina: null,
    chartLoading: true,
    chartErrored: false,
    chartOptions: null,
};

var app_dfc = new Vue({
    el: '#AppDFC',
    delimiters: ['[[',']]'],
    template: template_app_dfc,
    data: data_app_dfc,
    created () {
        this.buscar_dados('T')
        this.buscar_dados_grafico('T')
    },
    methods: methods_app_dfc,
});
