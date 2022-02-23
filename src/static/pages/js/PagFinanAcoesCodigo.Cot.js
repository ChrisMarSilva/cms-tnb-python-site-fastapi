
var template_app_cot = `
<div>
    <div class="row clearfix">
        <div class="col-xl-12 col-lg-12 col-md-12" style="padding-right: 4px; border: 0px solid red;">
            <div class="card border">
                <div class="header">
                    <div class="row clearfix align-items-end">
                        <div class="col-3">
                            <h2><strong>Cotações</strong></h2>
                        </div>
                        <div class="col-7">
                            <ul class="nav nav-tabs card-header-tabs font-weight-bold justify-content-center" style="margin: 0px; padding: 0px;">
                                <li class="nav-item"><a style="font-size: 13px; " class="nav-link active" data-toggle="tab" href="#TabCotDados">Dados</a></li>
                                <li class="nav-item"><a style="font-size: 13px; " class="nav-link" data-toggle="tab" href="#TabCotGraficos">Gráficos</a></li>
                            </ul>
                        </div>
                        <div class="col-2">
                        </div>
                    </div>
                </div>
                <div class="body">
                    <div class="tab-content">
                        <div role="tabpanel" class="tab-pane active" id="TabCotDados">

                            <div v-if="loading" class="text-center">
                                <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
                            </div>
                            <div v-else>
                                <div v-if="errored" class="text-cente">
                                    Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                                 </div>
                                <div v-else>

                                    <div v-if="cotacoes.length <= 0" class="text-cente">
                                        NENHUM RESULTADO ENCONTRADO
                                    </div>
                                    <div v-else>

                                        <!-- Div table-responsive -->
                                        <div class="table-responsive" id="AreaGrid">
                                            <table id="GridCot" name="GridCot" style="font-size: 12px" class="table table-sm table-hover table-condensed nowrap" cellspacing="0" width="100%">
                                                <thead>
                                                    <tr class="thead-dark font-weight-bold">
                                                        <th class="text-center" width="50px">ANO</th>
                                                        <th class="text-center" width="50px">JAN</th>
                                                        <th class="text-center" width="50px">FEV</th>
                                                        <th class="text-center" width="50px">MAR</th>
                                                        <th class="text-center" width="50px">ABR</th>
                                                        <th class="text-center" width="50px">MAI</th>
                                                        <th class="text-center" width="50px">JUN</th>
                                                        <th class="text-center" width="50px">JUL</th>
                                                        <th class="text-center" width="50px">AGO</th>
                                                        <th class="text-center" width="50px">SET</th>
                                                        <th class="text-center" width="50px">OUT</th>
                                                        <th class="text-center" width="50px">NOV</th>
                                                        <th class="text-center" width="50px">DEZ</th>
                                                        <th class="text-center" width="50px">ANUAL</th>
                                                        <th class="text-center" width="50px">Taxa Média de Crescimento Anual</th>
                                                    </tr>
                                                </thead>
                                                <tfoot>
                                                    <tr v-for="cot in TodasCotacoes">
                                                        <td>[[ cot.ano ]]</td>
                                                        <td>[[ cot.jan ]]</td>
                                                        <td>[[ cot.fev ]]</td>
                                                        <td>[[ cot.mar ]]</td>
                                                        <td>[[ cot.abr ]]</td>
                                                        <td>[[ cot.mai ]]</td>
                                                        <td>[[ cot.jun ]]</td>
                                                        <td>[[ cot.jul ]]</td>
                                                        <td>[[ cot.ago ]]</td>
                                                        <td>[[ cot.set ]]</td>
                                                        <td>[[ cot.out ]]</td>
                                                        <td>[[ cot.nov ]]</td>
                                                        <td>[[ cot.dez ]]</td>
                                                        <td>[[ cot.anual ]]</td>
                                                        <td>[[ cot.medio ]]</td>
                                                    </tr>
                                                </tfoot>
                                                <tbody>
                                                </tbody>
                                            </table>
                                        </div>
                                        <!-- Div table-responsive -->

                                    </div>

                                </div>
                            </div>

                        </div>

                        <div role="tabpanel" class="tab-pane in" id="TabCotGraficos">

                            <div v-if="loading" class="text-center">
                                <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
                            </div>
                            <div v-else>
                                <div v-if="errored" class="text-cente">
                                    Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                                 </div>
                                <div v-else>
                                    <highcharts :options="chartOptionsAno"></highcharts>
                                </div>
                            </div>

                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
</div>s
`;

var methods_app_cot = {

    getMascaraValor(value) {
        return value.toFixed(2).replace('.', ',').replace(/(\d)(?=(\d{3})+\,)/g, "$1.");
    },

    getPointCategoryName(point, dimension) {
        var series = point.series, isY = dimension === 'y', axis = series[isY ? 'yAxis' : 'xAxis'];
        return axis.categories[point[isY ? 'y' : 'x']];
    },

    async buscar_dados() {

        this.loading = true
        this.errored = false
        this.cotacoes = []

        axios({
          method: 'post',
          url: "/finan/acoes/grid_cot",
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify({ CodAtivo: codigo }),
        })
        .then( (response) => {
             let resultado = response.data.data.Resultado
             if (resultado == "OK") {
                 let lista = response.data.data.Lista
                 this.cotacoes = lista

                 let vm = this
                 let meses = ['JAN', 'FEV', 'MAI', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ', 'ANUAL', 'MÉDIO']
                 let anos = []
                 let data = []

                 let fLen = lista.length

                 for (i = 0; i < fLen; i++){
                    anos.push(lista[i].ano)
                 }

                 let minValue = 0.00
                 let maxValue = 0.00
                 for (i = 0; i < 12; i++) {
                    for (x = 0; x < fLen; x++){
                        let valor = 0.0
                        if ( i ==  0 ) valor = lista[x].jan
                        if ( i ==  1 ) valor = lista[x].fev
                        if ( i ==  2 ) valor = lista[x].mar
                        if ( i ==  3 ) valor = lista[x].abr
                        if ( i ==  4 ) valor = lista[x].mai
                        if ( i ==  5 ) valor = lista[x].jun
                        if ( i ==  6 ) valor = lista[x].jul
                        if ( i ==  7 ) valor = lista[x].ago
                        if ( i ==  8 ) valor = lista[x].set
                        if ( i ==  9 ) valor = lista[x].out
                        if ( i == 10 ) valor = lista[x].nov
                        if ( i == 11 ) valor = lista[x].dez
                        minValue = (valor < minValue) ? valor : minValue
                        maxValue = (valor > maxValue) ? valor : maxValue
                        if ( i == 12 ) valor = lista[x].anual
                        if ( i == 13 ) valor = lista[x].medio
                        data.push([i, x, valor])
                    }
                 }

                 this.chartOptionsAno = {
                    chart: { type: 'heatmap', marginTop: 40, marginBottom: 80, plotBorderWidth: 1,},
                    title: { text: 'Mapa de Calor - Valorição do Ativo - ' + codigo},
                    xAxis: { categories: meses, maxPadding: 0, minPadding: 0, },
                    yAxis: { categories: anos, title: null, reversed: true, lineWidth: 0, minorGridLineWidth: 0, lineColor: 'transparent', minorTickLength: 0, tickLength: 0  },
//                    accessibility: {
//                        point: {
//                            descriptionFormatter: function (point) {
//                                var ix = point.index + 1, xName = vm.getPointCategoryName(point, 'x'), yName =vm. getPointCategoryName(point, 'y'), val = point.value;
//                                return ix + '. ' + xName + ' sales ' + yName + ', ' + val + '.';
//                            }
//                        }
//                    },
                    // colorAxis: { minColor: '#FFFFFF', maxColor: Highcharts.getOptions().colors[0], },
                    colorAxis: { reversed: false, min: minValue, max: maxValue, endOnTick: false, startOnTick: false, tickInterval: 2, stops: [ [0, Highcharts.getOptions().colors[8]], [0.25, '#ffffff'], [1, Highcharts.getOptions().colors[7]] ] },
                    plotOptions: { heatmap: { borderWidth: 1 } },
                    legend: { align: 'right', layout: 'vertical', margin: 0, verticalAlign: 'top', y: 25, symbolHeight: 280 },
                    tooltip: { formatter: function () { return '' +  vm.getPointCategoryName(this.point, 'y') + '/'+ vm.getPointCategoryName(this.point, 'x')  +' <br/> <b>' + vm.getMascaraValor(this.point.value) + '%</b>'; } },
                    series: [{ borderWidth: 2, data: data, dataLabels: { enabled: true, color: '#ffffff' } }],
                    responsive: { rules: [{ condition: { maxWidth: 500 }, chartOptions: { yAxis: { labels: { formatter: function () { return this.value.charAt(0); } } } } }] }
                 }

                 return true
             } else {
                 this.errored = true
                 let mensagem = response.data.data.Mensagem
                 console.log('@TamoNaBolsa:Error',mensagem)
             }
        })
        .catch( (error) => {
            this.errored = true
            console.log('@TamoNaBolsa:Error',error)
        })
        .finally( () => {
            this.loading = false
        })

    },

};

var computeds_app_cot = {

    TodasCotacoes() {
        let vm = this
        let anoAtual = parseInt(moment().format('YYYY'))
        let mesAtual = parseInt(moment().format('MM'))
        return this.cotacoes.map(item => ({
            ...item,
            jan: vm.getMascaraValor(item.jan) + '%',
            fev: anoAtual == item.ano && mesAtual <  2 ? '' : vm.getMascaraValor(item.fev) + '%',
            mar: anoAtual == item.ano && mesAtual <  3 ? '' : vm.getMascaraValor(item.mar) + '%',
            abr: anoAtual == item.ano && mesAtual <  4 ? '' : vm.getMascaraValor(item.abr) + '%',
            mai: anoAtual == item.ano && mesAtual <  5 ? '' : vm.getMascaraValor(item.mai) + '%',
            jun: anoAtual == item.ano && mesAtual <  6 ? '' : vm.getMascaraValor(item.jun) + '%',
            jul: anoAtual == item.ano && mesAtual <  7 ? '' : vm.getMascaraValor(item.jul) + '%',
            ago: anoAtual == item.ano && mesAtual <  8 ? '' : vm.getMascaraValor(item.ago) + '%',
            set: anoAtual == item.ano && mesAtual <  9 ? '' : vm.getMascaraValor(item.set) + '%',
            out: anoAtual == item.ano && mesAtual < 10 ? '' : vm.getMascaraValor(item.out) + '%',
            nov: anoAtual == item.ano && mesAtual < 11 ? '' : vm.getMascaraValor(item.nov) + '%',
            dez: anoAtual == item.ano && mesAtual < 12 ? '' : vm.getMascaraValor(item.dez) + '%',
            anual: item.anual != 0.0 ? vm.getMascaraValor(item.anual) + '%' : '',
            medio: item.medio != 0.0 ? vm.getMascaraValor(item.medio) + '%' : '',
        }))
    },

}

var data_app_cot = {
    loading: true,
    errored: false,
    cotacoes: [],
    chartOptionsAno: null,
};

var app_cot = new Vue({
    el: '#AppCot',
    delimiters: ['[[',']]'],
    template: template_app_cot,
    data: data_app_cot,
    created () {
        // this.buscar_dados('A')
    },
    mounted() {
        // this.buscar_dados()
    },
    methods: methods_app_cot,
    computed: computeds_app_cot,
});
