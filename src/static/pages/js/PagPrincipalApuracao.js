
var appApuracaoTemplate = `
 <div class="row clearfix">
    <div class="col-lg-12">
        <div class="card border">
            <div class="header" style="padding: 0px; padding-top: 20px; padding-left: 20px;">
                <h2><strong><a href="/apuracao">APURAÇÃO</a></strong> SOBRE OPERAÇÕES MENSAIS</h2>  </a></strong>
            </div>
            <div class="body" style="max-height: 170px; height: 170px; margin: 0px 0px 20px; padding: 10px;">

                <div class="row clearfix">
                    <div class="col-lg-12 d-flex justify-content-center" style="padding-top: 20px;">
                        <button style="width: 140px; " @click="idApuracaoSelected='ACAOC'"  v-bind:class="{ 'btn-simple btn-default': idApuracaoSelected != 'ACAOC',  'btn-primary': idApuracaoSelected == 'ACAOC'  }" class="btn btn-sm btn-round waves-effect" id="change-view-today">AÇÕES COMUM</button>&nbsp;
                        <button style="width: 170px; " @click="idApuracaoSelected='ACAOD'"  v-bind:class="{ 'btn-simple btn-default': idApuracaoSelected != 'ACAOD',  'btn-primary': idApuracaoSelected == 'ACAOD'  }" class="btn btn-sm btn-round waves-effect" id="change-view-today">AÇÕES DAY TRADE</button>&nbsp;
                        <button style="width: 110px; " @click="idApuracaoSelected='FII'"    v-bind:class="{ 'btn-simple btn-default': idApuracaoSelected != 'FII',    'btn-primary': idApuracaoSelected == 'FII'    }" class="btn btn-sm btn-round waves-effect" id="change-view-day">FIIs</button>&nbsp;
                        <button style="width: 140px; " @click="idApuracaoSelected='ETFC'"   v-bind:class="{ 'btn-simple btn-default': idApuracaoSelected != 'ETFC',   'btn-primary': idApuracaoSelected == 'ETFC'   }" class="btn btn-sm btn-round waves-effect" id="change-view-week">ETFs COMUM</button>&nbsp;
                        <button style="width: 170px; " @click="idApuracaoSelected='ETFD'"   v-bind:class="{ 'btn-simple btn-default': idApuracaoSelected != 'ETFD',   'btn-primary': idApuracaoSelected == 'ETFD'   }" class="btn btn-sm btn-round waves-effect" id="change-view-week">ETFs DAY TRADE</button>&nbsp;
                        <button style="width: 140px; " @click="idApuracaoSelected='BDRC'"   v-bind:class="{ 'btn-simple btn-default': idApuracaoSelected != 'BDRC',   'btn-primary': idApuracaoSelected == 'BDRC'   }" class="btn btn-sm btn-round waves-effect" id="change-view-month">BDRs COMUM</button>&nbsp;
                        <button style="width: 170px; " @click="idApuracaoSelected='BDRD'"   v-bind:class="{ 'btn-simple btn-default': idApuracaoSelected != 'BDRD',   'btn-primary': idApuracaoSelected == 'BDRD'   }" class="btn btn-sm btn-round waves-effect" id="change-view-month">BDRs DAY TRADE</button>&nbsp;
                        <button style="width: 110px; " @click="idApuracaoSelected='CRIPTO'" v-bind:class="{ 'btn-simple btn-default': idApuracaoSelected != 'CRIPTO', 'btn-primary': idApuracaoSelected == 'CRIPTO' }" class="btn btn-sm btn-round waves-effect" id="change-view-day">CRIPTOs</button>&nbsp;
                    </div>
                </div>

                <div class="row clearfix" style="max-height: 170px; height: 170px; overflow-y: auto; overflow-x: hidden; margin: 0px; padding: 0px;">
                   <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12" style="">

                        <div v-if="loading" class="text-center">
                            <div class="contentAnimated"> <div class="animated"> <div class="description"></div> <div class="padding"></div> <div class="description"></div> </div> </div>
                        </div>
                        <div v-else>
                            <div v-if="errored" class="text-center" style="padding-top: 50px;">
                                Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                            </div>
                            <div v-else>

                                <div class="table-responsive-sm"  style="padding-top: 20px;">
                                    <table class="table table-sm table-hover table-condensed nowrap" border="0" cellspacing="0" width="100%" style="font-size: 13px; margin: 0px;">
                                        <thead>
                                            <tr class="thead-dark font-weight-bold text-center">
                                                <th width="30px">Mês/Ano</th>
                                                <th width="80px">Venda</th>
                                                <th width="100px">Lucro Apurado</th>
                                                <th width="120px">Prejuízo a Compensar</th>
                                                <th width="120px">Base de Cálculo IR</th>
                                                <th width="80px">IR Devido</th>
                                                <th width="80px">IR Pago</th>
                                                <th width="80px">IR a Pagar</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="apuracao in TodosApuracoes" class="text-center">
                                                <td :class="apuracao.corVlrApurado">[[ apuracao.mesAno ]]</td>
                                                <td class="text-muted">R$ [[ apuracao.vlrVenda ]]</td>
                                                <td :class="apuracao.corVlrApurado">R$ [[ apuracao.vlrApurado ]]</td>
                                                <td :class="apuracao.corVlrCompensar">R$ [[ apuracao.vlrCompensar ]]</td>
                                                <td :class="apuracao.corVlrResultado">R$ [[ apuracao.vlrResultado ]]</td>
                                                <td class="text-muted">R$ [[ apuracao.vlrImpostoAPagar ]]</td>
                                                <td class="text-muted">R$ [[ apuracao.vlrImpostoPago ]]</td>
                                                <td :class="apuracao.corVlrImpostoDevido">R$ [[ apuracao.vlrImpostoDevido ]]</td>
                                            </tr>
                                        </tbody>
                                    </table>
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


var appApuracaoMethods = {

    getValDecimal(value){
        try {
            value = value.replace(/\./g, '').replace(',', '.')
            value = parseFloat(value).toFixed(2) || 0
            if( !isNumber(value) )
                return 0
            return value
        } catch (error) {
            return 0
            console.error('@TamoNaBolsa - Error:', error)
        }
    },

    async buscarDados() {

        let logNome = '@TamoNaBolsa - PagPrincipalApuracao'

        // console.log(logNome + ' - INI - ', moment().format())
        console.time(logNome + ' - TEMPO')

        this.listaACAOC  = []
        this.listaACAOD  = []
        this.listaFII    = []
        this.listaETFC   = []
        this.listaETFD   = []
        this.listaBDRC   = []
        this.listaBDRD   = []
        this.listaCRIPTO = []

        axios({
          method: 'post',
          url: '/apuracao/gridresumidaportipo',
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
        })
        .then( (response) => {
             let resultado = response.data.data.Resultado;
             if (resultado == "OK") {
                let dados = response.data.data.Dados
                this.listaACAOC  = dados.lista_acao_c
                this.listaACAOD  = dados.lista_acao_d
                this.listaFII    = dados.lista_fii
                this.listaETFC   = dados.lista_etf_c
                this.listaETFD   = dados.lista_etf_d
                this.listaBDRC   = dados.lista_bdr_c
                this.listaBDRD   = dados.lista_bdr_d
                this.listaCRIPTO = dados.lista_cripto
                return true;
             } else {
                 this.errored = true;
                 let mensagem = response.data.data.Mensagem;
                 console.warn(logNome + ' - WANNING: ', mensagem)
             }
        })
        .catch( (error) => {
            this.errored = true
            console.error(logNome + ' - ERRO: ', error)
        })
        .finally( () => {
            this.loading = false
            // console.log(logNome + ' - FIM - ', moment().format())
            console.timeEnd(logNome + ' - TEMPO')
        })

    }, // buscarDadosGrid()

    async buscarDadosGrid( idApuracao = '' ) {

        let logNome = '@TamoNaBolsa - PagPrincipalApuracao - ' + idApuracao

        // console.log(logNome + ' - INI - ', moment().format())
        console.time(logNome + ' - TEMPO')

        if ( idApuracao == 'ACAOC'  ) this.listaACAOC  = []
        if ( idApuracao == 'ACAOD'  ) this.listaACAOD  = []
        if ( idApuracao == 'FII'    ) this.listaFII    = []
        if ( idApuracao == 'ETFC'   ) this.listaETFC   = []
        if ( idApuracao == 'ETFD'   ) this.listaETFD   = []
        if ( idApuracao == 'BDRC'   ) this.listaBDRC   = []
        if ( idApuracao == 'BDRD'   ) this.listaBDRD   = []
        if ( idApuracao == 'CRIPTO' ) this.listaCRIPTO = []

        let linkUrl = ""
        if ( idApuracao == 'ACAOC'  ) linkUrl = '/apuracao/gridResumidaAcaoComum'
        if ( idApuracao == 'ACAOD'  ) linkUrl = '/apuracao/gridResumidaAcaoDayTrade'
        if ( idApuracao == 'FII'    ) linkUrl = '/apuracao/gridResumidaFii'
        if ( idApuracao == 'ETFC'   ) linkUrl = '/apuracao/gridResumidaEtfComum'
        if ( idApuracao == 'ETFD'   ) linkUrl = '/apuracao/gridResumidaEtfDayTrade'
        if ( idApuracao == 'BDRC'   ) linkUrl = '/apuracao/gridResumidaBdrComum'
        if ( idApuracao == 'BDRD'   ) linkUrl = '/apuracao/gridResumidaBdrDayTrade'
        if ( idApuracao == 'CRIPTO' ) linkUrl = '/apuracao/gridResumidaCripto'

        axios({
          method: 'post',
          url: linkUrl,
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
        })
        .then( (response) => {
             let resultado = response.data.data.Resultado;
             if (resultado == "OK") {
                let lista = response.data.data.Lista
                if ( idApuracao == 'ACAOC'  ) this.listaACAOC  = lista
                if ( idApuracao == 'ACAOD'  ) this.listaACAOD  = lista
                if ( idApuracao == 'FII'    ) this.listaFII    = lista
                if ( idApuracao == 'ETFC'   ) this.listaETFC   = lista
                if ( idApuracao == 'ETFD'   ) this.listaETFD   = lista
                if ( idApuracao == 'BDRC'   ) this.listaBDRC   = lista
                if ( idApuracao == 'BDRD'   ) this.listaBDRD   = lista
                if ( idApuracao == 'CRIPTO' ) this.listaCRIPTO = lista
                return true;
             } else {
                 this.errored = true;
                 let mensagem = response.data.data.Mensagem;
                 console.warn(logNome + ' - WANNING: ', mensagem)
             }
        })
        .catch( (error) => {
            this.errored = true
            console.error(logNome + ' - ERRO: ', error)
        })
        .finally( () => {
            this.loading = false
            // console.log(logNome + ' - FIM - ', moment().format())
            console.timeEnd(logNome + ' - TEMPO')
        })

    }, // buscarDadosGrid()

};

var appApuracaoComputeds = {

    TodosApuracoes() {
        try {

            let apuracoes = []
            if ( this.idApuracaoSelected == 'ACAOC'  ) apuracoes = this.listaACAOC
            if ( this.idApuracaoSelected == 'ACAOD'  ) apuracoes = this.listaACAOD
            if ( this.idApuracaoSelected == 'FII'    ) apuracoes = this.listaFII
            if ( this.idApuracaoSelected == 'ETFC'   ) apuracoes = this.listaETFC
            if ( this.idApuracaoSelected == 'ETFD'   ) apuracoes = this.listaETFD
            if ( this.idApuracaoSelected == 'BDRC'   ) apuracoes = this.listaBDRC
            if ( this.idApuracaoSelected == 'BDRD'   ) apuracoes = this.listaBDRD
            if ( this.idApuracaoSelected == 'CRIPTO' ) apuracoes = this.listaCRIPTO

            let new_apuracoes = []
            let vm = this

             _.forEach(apuracoes, function(value) {
                let vlrApurado = parseFloat(vm.getValDecimal(value[2]))
                let vlrCompensar = parseFloat(vm.getValDecimal(value[3]))
                let vlrResultado = parseFloat(vm.getValDecimal(value[4]))
                let vlrImpostoDevido = parseFloat(vm.getValDecimal(value[7]))
                new_apuracoes.push({
                    mesAno: value[0],
                    vlrVenda: value[1],
                    vlrApurado: value[2],
                    vlrCompensar: value[3],
                    vlrResultado: value[4],
                    vlrImpostoAPagar: value[5],
                    vlrImpostoPago: value[6],
                    vlrImpostoDevido: value[7],
                    corVlrApurado: vlrApurado > 0 ? 'text-success font-weight-bold' :vlrApurado < 0 ? 'text-danger font-weight-bold' : 'text-muted',
                    corVlrCompensar: vlrCompensar > 0 ? 'text-success font-weight-bold' : vlrCompensar < 0 ? 'text-danger font-weight-bold' : 'text-muted',
                    corVlrResultado:  vlrResultado > 0 ? 'text-success font-weight-bold' : vlrResultado < 0 ? 'text-danger font-weight-bold' : 'text-muted',
                    corVlrImpostoDevido: vlrImpostoDevido > 0 ? 'text-success font-weight-bold' : vlrImpostoDevido < 0 ? 'text-danger font-weight-bold' : 'text-muted',
               })
            })

            return new_apuracoes

        } catch (error) {
            console.error('@TamoNaBolsa - TodosApuracoes - Error:', this.idApuracaoSelected, error)
        }
    },

}

var appApuracaoData = {
    loading: true,
    errored: false,
    idEmpty: true,
    idApuracaoSelected: 'ACAOC',
    listaACAOC: [],
    listaACAOD: [],
    listaFII: [],
    listaETFC: [],
    listaETFD: [],
    listaBDRC: [],
    listaBDRD: [],
    listaCRIPTO: [],
}

var appApuracao = new Vue({
    el: '#AppApuracao',
    delimiters: ['[[',']]'],
    data: appApuracaoData,
    template: appApuracaoTemplate,
    created () {
        // this.buscarDadosGrid('ACAOC')
        // this.buscarDadosGrid('ACAOD')
        // this.buscarDadosGrid('FII')
        // this.buscarDadosGrid('ETFC')
        // this.buscarDadosGrid('ETFD')
        // this.buscarDadosGrid('BDRC')
        // this.buscarDadosGrid('BDRD')
        // this.buscarDadosGrid('CRIPTO')
        // this.buscarDados()
    },
    mounted() {
        // this.buscarDadosGrid('ACAOC')
        // this.buscarDadosGrid('ACAOD')
        // this.buscarDadosGrid('FII')
        // this.buscarDadosGrid('ETFC')
        // this.buscarDadosGrid('ETFD')
        // this.buscarDadosGrid('BDRC')
        // this.buscarDadosGrid('BDRD')
        // this.buscarDadosGrid('CRIPTO')
        let vm = this
        setTimeout(function(){ vm.buscarDados(); }, 500);
    },
    methods: appApuracaoMethods,
    computed: appApuracaoComputeds,
});
