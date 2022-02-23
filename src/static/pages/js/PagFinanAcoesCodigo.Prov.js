
var template_app_prov = `
<div>
    <div class="row clearfix">
        <div class="col-xl-12 col-lg-12 col-md-12" style="padding-right: 4px; border: 0px solid red;">
            <div class="card border">
                <div class="header">
                    <div class="row clearfix align-items-end">
                        <div class="col-3">
                            <h2><strong>Proventos</strong></h2>
                        </div>
                        <div class="col-7">
                            <ul class="nav nav-tabs card-header-tabs font-weight-bold justify-content-center" style="margin: 0px; padding: 0px;">
                                <li class="nav-item"><a style="font-size: 13px; " class="nav-link active" data-toggle="tab" href="#TabProvDados">Dados</a></li>
                                <!-- <li class="nav-item"><a style="font-size: 13px; " class="nav-link" data-toggle="tab" href="#TabProvDadosEx">Calendário Data Ex.</a></li> -->
                                <!-- <li class="nav-item"><a style="font-size: 13px; " class="nav-link" data-toggle="tab" href="#TabProvDadosPgt">Calendário Data Pagto</a></li> -->
                                <li class="nav-item"><a style="font-size: 13px; " class="nav-link" data-toggle="tab" href="#TabProvGraficos">Gráficos</a></li>
                            </ul>
                        </div>
                        <div class="col-2">
                        </div>
                    </div>
                </div>
                <div class="body">
                    <div class="tab-content">
                        <div role="tabpanel" class="tab-pane active" id="TabProvDados">

                            <div v-if="loading" class="text-center">
                                <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
                            </div>
                            <div v-else>
                                <div v-if="errored" class="text-cente">
                                    Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                                 </div>
                                <div v-else>

                                    <div v-if="proventos.length <= 0" class="text-cente">
                                        NENHUM RESULTADO ENCONTRADO
                                    </div>
                                    <div v-else>

                                        <!-- Div table-responsive -->
                                        <div class="table-responsive" id="AreaGrid">
                                            <table id="GridProv" name="GridProv" style="font-size: 12px" class="table table-sm table-hover table-condensed nowrap" cellspacing="0" width="100%">
                                                <thead>
                                                    <tr class="thead-dark font-weight-bold">
                                                        <th class="text-center" width="50px">TIPO</th>
                                                        <th class="text-center" width="50px">DATA APROV</th>
                                                        <th class="text-center" width="50px">DATA EX</th>
                                                        <th class="text-center" width="50px">DATA PAGTO</th>
                                                        <th class="text-center" width="50px">VALOR</th>
                                                    </tr>
                                                </thead>
                                                <tfoot>
                                                    <tr v-for="provento in TodosProventos">
                                                        <td>[[ provento.tipoFormat ]]</td>
                                                        <td>[[ provento.dataAprovFormat ]]</td>
                                                        <td>[[ provento.dataExFormat ]]</td>
                                                        <td>[[ provento.dataPagtoFormat ]]</td>
                                                        <td>[[ provento.vlrPrecoFormat ]]</td>
                                                    </tr>
                                                </tfoot>
                                                <tbody>
                                                </tbody>
                                            </table>
                                        </div>
                                        <!-- Div table-responsive -->

                                        <ul class="pagination pagination-primary m-b-0 justify-content-center" v-if="filtroPaginas.length > 1">
                                            <li class="page-item" :class="{'disabled' : (filtroPagAtual == 1)}"><a class="page-link text-muted" :class="{'disabled' : (filtroPagAtual == 1)}" href="javascript:void(0);" @click="filtroPagAtual--"><i class="zmdi zmdi-arrow-left"></i></a></li>
                                            <li class="page-item" v-if="filtroPagAtual > 3"><a class="page-link text-muted" href="javascript:void(0);" @click="filtroPagAtual = 1">[[ filtroPaginas[0] ]]</a></li>
                                            <li class="page-item disabled" v-if="filtroPagAtual > 3"> <a class="page-link text-muted disabled" href="javascript:void(0);"> ... </a></li>
                                            <li class="page-item" :class="{'active' : (filtroPagAtual === (pageNumber))}"  v-for="pageNumber in displayedPages"><a class="page-link text-muted" href="javascript:void(0);" @click="filtroPagAtual = pageNumber">[[ pageNumber ]]</a></li>
                                            <li class="page-item disabled" v-if="filtroPagAtual < filtroPaginas.length - 2"> <a class="page-link text-muted disabled" href="javascript:void(0);"> ... </a></li>
                                            <li class="page-item" v-if="filtroPagAtual < filtroPaginas.length - 2"><a class="page-link text-muted" href="javascript:void(0);" @click="filtroPagAtual = filtroPaginas.length">[[ filtroPaginas[filtroPaginas.length - 1] ]]</a></li>
                                            <li class="page-item" :class="{'disabled' : (filtroPagAtual == filtroPaginas.length)}"><a class="page-link text-muted" :class="{'disabled' : (filtroPagAtual == filtroPaginas.length)}" href="javascript:void(0);" @click="filtroPagAtual++"><i class="zmdi zmdi-arrow-right"></i></a></li>
                                        </ul>

                                    </div>

                                </div>
                            </div>

                        </div>

                        <div role="tabpanel" class="tab-pane in" id="TabProvDadosEx">

                            <div v-if="loading" class="text-center">
                                <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
                            </div>
                            <div v-else>
                                <div v-if="errored" class="text-cente">
                                    Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                                 </div>
                                <div v-else>

                                    <div v-if="proventos.length <= 0" class="text-cente">
                                        NENHUM RESULTADO ENCONTRADO
                                    </div>
                                    <div v-else>

                                        <!-- Div table-responsive -->
                                        <div class="table-responsive" id="AreaGrid">
                                            <table id="GridProvTabEx" name="GridProvTabEx" style="font-size: 12px" class="table table-sm table-hover table-condensed nowrap" cellspacing="0" width="100%">
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
                                                    </tr>
                                                </thead>
                                                <tfoot>
                                                    <tr v-for="provento in TodosProventosTabEx">
                                                        <td>[[ provento.ano ]]</td>
                                                        <td>[[ provento.jan ]]</td>
                                                        <td>[[ provento.fev ]]</td>
                                                        <td>[[ provento.mar ]]</td>
                                                        <td>[[ provento.abr ]]</td>
                                                        <td>[[ provento.mai ]]</td>
                                                        <td>[[ provento.jun ]]</td>
                                                        <td>[[ provento.jul ]]</td>
                                                        <td>[[ provento.ago ]]</td>
                                                        <td>[[ provento.set ]]</td>
                                                        <td>[[ provento.out ]]</td>
                                                        <td>[[ provento.nov ]]</td>
                                                        <td>[[ provento.dez ]]</td>
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

                        <div role="tabpanel" class="tab-pane in" id="TabProvDadosPgt">

                            <div v-if="loading" class="text-center">
                                <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
                            </div>
                            <div v-else>
                                <div v-if="errored" class="text-cente">
                                    Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                                 </div>
                                <div v-else>

                                    <div v-if="proventos.length <= 0" class="text-cente">
                                        NENHUM RESULTADO ENCONTRADO
                                    </div>
                                    <div v-else>

                                        <!-- Div table-responsive -->
                                        <div class="table-responsive" id="AreaGrid">
                                            <table id="GridProvTabPgto" name="GridProvTabPgto" style="font-size: 12px" class="table table-sm table-hover table-condensed nowrap" cellspacing="0" width="100%">
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
                                                    </tr>
                                                </thead>
                                                <tfoot>
                                                    <tr v-for="provento in TodosProventosTabPgt">
                                                        <td>[[ provento.ano ]]</td>
                                                        <td>[[ provento.jan ]]</td>
                                                        <td>[[ provento.fev ]]</td>
                                                        <td>[[ provento.mar ]]</td>
                                                        <td>[[ provento.abr ]]</td>
                                                        <td>[[ provento.mai ]]</td>
                                                        <td>[[ provento.jun ]]</td>
                                                        <td>[[ provento.jul ]]</td>
                                                        <td>[[ provento.ago ]]</td>
                                                        <td>[[ provento.set ]]</td>
                                                        <td>[[ provento.out ]]</td>
                                                        <td>[[ provento.nov ]]</td>
                                                        <td>[[ provento.dez ]]</td>
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

                        <div role="tabpanel" class="tab-pane in" id="TabProvGraficos">

                            <div v-if="loading" class="text-center">
                                <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
                            </div>
                            <div v-else>
                                <div v-if="errored" class="text-cente">
                                    Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                                 </div>
                                <div v-else>
                                    <highcharts :options="chartOptionsMes"></highcharts>
                                    <br/>
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

var methods_app_prov = {

    async setPaginacao () {
        this.filtroPaginas = []
        let numberOfPages = Math.ceil(this.proventos.length / this.filtroPagMax)  // N of items (100) / 10 items per page
        for (i = 1; i <= numberOfPages; i++) //generate 10 pages (100 / 10)
            this.filtroPaginas.push(i)
    },

    getMascaraValor(value) {
        return value.toFixed(10).replace('.', ',').replace(/(\d)(?=(\d{3})+\,)/g, "$1.");
    },

    async buscar_dados() {

        this.loading = true
        this.errored = false
        this.proventos = []

        axios({
          method: 'post',
          url: "/finan/acoes/grid_prov",
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify({ CodAtivo: codigo }),
        })
        .then( (response) => {
             let resultado = response.data.data.Resultado
             if (resultado == "OK") {

                 let lista = response.data.data.Lista

                 let fLen = lista.length
                 if (fLen <= 0){
                    return
                 }

                 this.proventos = lista

                 let arTitulo = []
                 let arValores = []

                for (i = 0; i < fLen; i++) {
                    arTitulo.push(lista[i].dataExFormat)
                    arValores.push(lista[i].vlrPreco)
                }

                this.chartOptionsMes = {
                    chart: { type: 'column' },
                    title: { text: 'Proventos por Data' },
                    xAxis: { categories: arTitulo, crosshair: true },
                    yAxis: [
                        { allowDecimals: true, min: 0, title: { text: null, style: { color: Highcharts.getOptions().colors[1] } }, labels: { format: 'R$ {value:.,2f}', style: { color: Highcharts.getOptions().colors[1] } },  },// Primary yAxis
                    ],
                    series: [
                        {yAxis: 0, showInLegend: false, data: arValores, tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<b>R$ ' + value + '</b><br /> '; }, shared: true } } ,
                    ]
                 }

                arTitulo = []
                arValores = []
                let ult_ano = ""
                let ult_valor = 0.0

                for (i = 0; i < fLen; i++) {
                    let atu_ano = lista[i].dataEx.substring(0,4)
                    let atu_valor = lista[i].vlrPreco
                    if (ult_ano == "")
                        ult_ano = atu_ano
                    if (ult_ano != atu_ano) {
                        arTitulo.push(ult_ano)
                        arValores.push(ult_valor)
                        ult_valor = 0.0
                        ult_ano = atu_ano
                    }
                    ult_valor += atu_valor

                }

                if (ult_ano != ''){
                    arTitulo.push(ult_ano)
                    arValores.push(ult_valor)
                }

                this.chartOptionsAno = {
                    chart: { type: 'column' },
                    title: { text: 'Proventos por Ano' },
                    xAxis: { categories: arTitulo, crosshair: true },
                    yAxis: [
                        { allowDecimals: true, min: 0, title: { text: null, style: { color: Highcharts.getOptions().colors[1] } }, labels: { format: 'R$ {value:.,2f}', style: { color: Highcharts.getOptions().colors[1] } },  },// Primary yAxis
                    ],
                    series: [
                        {yAxis: 0, showInLegend: false, color: '#BF0B23', data: arValores, tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<b>R$ ' + value + '</b><br /> '; }, shared: true } } ,
                    ]
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

    async buscar_tabela(TipoTab = 'E') {

        if (TipoTab == 'E') this.proventos_tab_ex  = []
        if (TipoTab == 'P') this.proventos_tab_pgt = []

        axios({
          method: 'post',
          url: "/finan/acoes/grid_prov_tab",
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify({ CodAtivo: codigo, TipoTabela: TipoTab }),
        })
        .then( (response) => {
             let resultado = response.data.data.Resultado
             if (resultado == "OK") {
                 let lista = response.data.data.Lista
                if (TipoTab == 'E') this.proventos_tab_ex  = lista
                if (TipoTab == 'P') this.proventos_tab_pgt = lista
                 return true
             } else {
                 let mensagem = response.data.data.Mensagem
                 console.log('@TamoNaBolsa:Error',mensagem)
             }
        })
        .catch( (error) => {
            console.log('@TamoNaBolsa:Error',error)
        })
    },

};

var computeds_app_prov = {

    TodosProventos() {

        let new_proventos = this.proventos

//        new_proventos = new_proventos.sort(function(a, b){
//            var ADataPagto = a.dataPagto;
//            var BDataPagto = b.dataPagto;
//            if (ADataPagto == BDataPagto) return 0;
//            return ADataPagto < BDataPagto? 1: -1;
//        })

        new_proventos = _.orderBy(new_proventos, ['dataPagto'], ['desc']);

        let start = (this.filtroPagAtual * this.filtroPagMax) - this.filtroPagMax
        let end = this.filtroPagAtual * this.filtroPagMax
        return new_proventos.slice(start, end)
    },

    TodosProventosTabEx() {
        let vm = this
        return this.proventos_tab_ex.map(item => ({
            ...item,
            jan: item.jan > 0.0 ? vm.getMascaraValor(item.jan) : '',
            fev: item.fev > 0.0 ? vm.getMascaraValor(item.fev) : '',
            mar: item.mar > 0.0 ? vm.getMascaraValor(item.mar) : '',
            abr: item.abr > 0.0 ? vm.getMascaraValor(item.abr) : '',
            mai: item.mai > 0.0 ? vm.getMascaraValor(item.mai) : '',
            jun: item.jun > 0.0 ? vm.getMascaraValor(item.jun) : '',
            jul: item.jul > 0.0 ? vm.getMascaraValor(item.jul) : '',
            ago: item.ago > 0.0 ? vm.getMascaraValor(item.ago) : '',
            set: item.set > 0.0 ? vm.getMascaraValor(item.set) : '',
            out: item.out > 0.0 ? vm.getMascaraValor(item.out) : '',
            nov: item.nov > 0.0 ? vm.getMascaraValor(item.nov) : '',
            dez: item.dez > 0.0 ? vm.getMascaraValor(item.dez) : '',
        }))
    },

    TodosProventosTabPgt() {
        let vm = this
        return this.proventos_tab_pgt.map(item => ({
            ...item,
            jan: item.jan > 0.0 ? vm.getMascaraValor(item.jan) : '',
            fev: item.fev > 0.0 ? vm.getMascaraValor(item.fev) : '',
            mar: item.mar > 0.0 ? vm.getMascaraValor(item.mar) : '',
            abr: item.abr > 0.0 ? vm.getMascaraValor(item.abr) : '',
            mai: item.mai > 0.0 ? vm.getMascaraValor(item.mai) : '',
            jun: item.jun > 0.0 ? vm.getMascaraValor(item.jun) : '',
            jul: item.jul > 0.0 ? vm.getMascaraValor(item.jul) : '',
            ago: item.ago > 0.0 ? vm.getMascaraValor(item.ago) : '',
            set: item.set > 0.0 ? vm.getMascaraValor(item.set) : '',
            out: item.out > 0.0 ? vm.getMascaraValor(item.out) : '',
            nov: item.nov > 0.0 ? vm.getMascaraValor(item.nov) : '',
            dez: item.dez > 0.0 ? vm.getMascaraValor(item.dez) : '',
        }))
    },

    displayedPages() {
        if (this.filtroPagAtual === 1)
            return this.filtroPaginas.slice(this.filtroPagAtual - 1, this.filtroPagAtual + 4)
        else if (this.filtroPagAtual === this.filtroPaginas.length)
            return this.filtroPaginas.slice(this.filtroPagAtual - 5, this.filtroPagAtual + 1)
        else if (this.filtroPagAtual >= 4 && this.filtroPagAtual <= 7)
            return this.filtroPaginas.slice(this.filtroPagAtual - 2, this.filtroPagAtual + 1)
        else if (this.filtroPagAtual > 7)
            return this.filtroPaginas.slice(this.filtroPagAtual - 2, this.filtroPagAtual + 1) // return this.filtroPaginas.slice(this.filtroPagAtual + 1, this.filtroPagAtual - 4)
        else
            return this.filtroPaginas.slice(this.filtroPagAtual - 2, this.filtroPagAtual + 3)
    },
};

var watchs_app_prov = {
    proventos () { this.setPaginacao() }
};

var data_app_prov = {
    loading: true,
    errored: false,
    proventos: [],
    proventos_tab_ex: [],
    proventos_tab_pgt: [],
    filtroPagMax: 10,
    filtroPagAtual: 1,
    filtroPaginas: [],
    chartOptionsMes: null,
    chartOptionsAno: null,
};

var app_prov = new Vue({
    el: '#AppProv',
    delimiters: ['[[',']]'],
    template: template_app_prov,
    data: data_app_prov,
    created () {
        // this.buscar_dados('A')
        // this.buscar_tabela('E') // E - Ex
        // this.buscar_tabela('P') // P - Pagt
    },
    mounted() {
        this.buscar_dados()
        // this.buscar_tabela('E') // E - Ex
        // this.buscar_tabela('P') // P - Pagt
    },
    methods: methods_app_prov,
    computed: computeds_app_prov,
	watch: watchs_app_prov,
});
