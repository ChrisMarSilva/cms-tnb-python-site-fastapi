
var appOperacaoTemplate = `
<div class="card border info-box-2">
    <div class="header" style="padding: 5px; padding-top: 20px; padding-left: 20px;">
        <h2><strong><a href="/operacoes">OPERAÇÕES</a></strong> REALIZADAS NO MÊS</h2>
    </div>
    <div class="body" style="max-height: 400px; height: 400px; margin: 0px 0px 20px; padding: 0px;">

        <div class="row clearfix">
            <div class="col-lg-12  d-flex justify-content-center">
                <button style="width: 150px; " @click="idMensalSelected='ACAO'"    v-bind:class="{ 'btn-simple btn-default': idMensalSelected != 'ACAO',   'btn-primary': idMensalSelected == 'ACAO'   }" class="btn btn-sm btn-round waves-effect" id="change-view-today">AÇÕES ([[ listaACAO.length  ]])</button>&nbsp;
                <button style="width: 150px; " @click="idMensalSelected='FII'"     v-bind:class="{ 'btn-simple btn-default': idMensalSelected != 'FII',    'btn-primary': idMensalSelected == 'FII'    }" class="btn btn-sm btn-round waves-effect" id="change-view-day">FIIs ([[ listaFII.length  ]])</button>&nbsp;
                <button style="width: 150px; " @click="idMensalSelected='ETF'"     v-bind:class="{ 'btn-simple btn-default': idMensalSelected != 'ETF',    'btn-primary': idMensalSelected == 'ETF'    }" class="btn btn-sm btn-round waves-effect" id="change-view-week">ETFs ([[ listaETF.length  ]])</button>&nbsp;
                <button style="width: 150px; " @click="idMensalSelected='BDR'"     v-bind:class="{ 'btn-simple btn-default': idMensalSelected != 'BDR',    'btn-primary': idMensalSelected == 'BDR'    }" class="btn btn-sm btn-round waves-effect" id="change-view-month">BDRs ([[ listaBDR.length  ]])</button>&nbsp;
                <button style="width: 150px; " @click="idMensalSelected='CRIPTO'"  v-bind:class="{ 'btn-simple btn-default': idMensalSelected != 'CRIPTO', 'btn-primary': idMensalSelected == 'CRIPTO' }" class="btn btn-sm btn-round waves-effect" id="change-view-month">CRIPTOs ([[ listaCRIPTO.length  ]])</button>&nbsp;
            </div>
        </div>

        <br />

        <div class="row clearfix">

            <div class="col-sm-12 col-md-12 col-lg-6 col-xl-6" style="min-height: 350px; max-height: 350px; overflow-y:auto; -webkit-overflow-scrolling: touch; border: 0px solid green;">
                <div v-if="loading" class="text-center">
                    <div class="contentAnimated"> <div class="animated"> <div class="parent"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div>  </div>  </div>
                </div>
                <div v-else>

                    <div v-if="errored" class="text-cente">
                        Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                     </div>
                    <div v-else>
                        <div class="row clearfix item text-center" style="padding-left: 20px;">

                            <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12">
                                <small style="font-size:15px;" class="text-success font-weight-bold text-center">COMPRAS: R$ [[ getMascaraValor(total_compra) ]]</small> <br /> <br/>
                                 <table class="table table-sm table-hover table-condensed nowrap" border="0" cellspacing="0" width="100%" style="font-size: 11.5px; margin: 0px;">
                                    <thead>
                                        <tr class="font-weight-bold text-center">
                                            <th width="30px">Data</th>
                                            <th width="30px">Ativo</th>
                                            <th width="40px">Quant.</th>
                                            <th width="40px">Preço</th>
                                            <th width="50px">Total</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-if="total_compra == 0.0" style="font-size:14px;" class=" text-center font-italic text-muted font-weight-bold">
                                            <td colspan=5> Nenhuma Compra realizada... </td>
                                        </tr>
                                        <tr v-for="operacao in TodasOperacoesCompras" style="font-size:13px;" class=" text-center font-italic text-muted">
                                            <td>[[ operacao.data ]]</td>
                                            <td class="text-dark font-weight-bold">[[ operacao.ativo ]]</td>
                                            <td>[[ operacao.qtde ]]</td>
                                            <td>R$ [[ operacao.preco ]]</td>
                                            <td class="text-dark font-weight-bold">R$ [[ operacao.total ]]</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>

                        </div>
                    </div>
                </div>
            </div>

            <div class="col-sm-12 col-md-12 col-lg-6 col-xl-6" style="min-height: 350px; max-height: 350px; overflow-y:auto; -webkit-overflow-scrolling: touch; border: 0px solid red; ">
                <div v-if="loading" class="text-center">
                    <div class="contentAnimated"> <div class="animated"> <div class="parent"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div>  </div>  </div>
                </div>
                <div v-else>
                    <div v-if="errored" class="text-cente">
                        Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                     </div>
                    <div v-else>

                        <div class="row clearfix item text-center" style="padding-right: 20px;">
                            <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12">
                                <small style="font-size:15px;" class="text-danger font-weight-bold text-center">VENDAS: R$ [[ getMascaraValor(total_venda) ]]</small> <br/> <br />
                                 <table class="table table-sm table-hover table-condensed nowrap" border="0" cellspacing="0" width="100%" style="font-size: 11.5px; margin: 0px;">
                                    <thead>
                                        <tr class="font-weight-bold text-center">
                                            <th width="30px">Data</th>
                                            <th width="30px">Ativo</th>
                                            <th width="40px">Quant.</th>
                                            <th width="40px">Preço</th>
                                            <th width="50px">Total</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-if="total_venda == 0.0" style="font-size:14px;" class=" text-center font-italic text-muted font-weight-bold">
                                            <td colspan=5> Nenhuma Venda realizada... </td>
                                        </tr>
                                        <tr v-for="operacao in TodasOperacoesVendas" style="font-size:13px;" class=" text-center font-italic text-muted">
                                            <td>[[ operacao.data ]]</td>
                                            <td class="text-dark font-weight-bold">[[ operacao.ativo ]]</td>
                                            <td>[[ operacao.qtde ]]</td>
                                            <td>R$ [[ operacao.preco ]]</td>
                                            <td class="text-dark font-weight-bold">R$ [[ operacao.total ]]</td>
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
`;


var appOperacaoMethods = {

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

    getFormacataoInteiro(value) {
      return String(value).split('').reverse().join('').split(/(\d{3})/).filter(Boolean).join('.').split('').reverse().join('');
    },

    getMascaraValor(value) {
        return value.toFixed(2).replace('.', ',').replace(/(\d)(?=(\d{3})+\,)/g, "$1.");
    },

    getMascaraValorSemLimite(value) {
        return valor.toLocaleString('pt-br', {minimumFractionDigits: 2, maximumFractionDigits: 10}).replace(',00', '');
    },

    async buscarDados() {

        let logNome = '@TamoNaBolsa - PagPrincipalOperacao'

        // console.log(logNome + ' - INI - ', moment().format())
        console.time(logNome + ' - TEMPO')

        this.listaACAO   = []
        this.listaFII    = []
        this.listaETF    = []
        this.listaBDR    = []
        this.listaCRIPTO = []

        axios({
          method: 'post',
          url: '/principal/carregaroperacoesportipos',
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
        })
        .then( (response) => {
             let resultado = response.data.data.Resultado;
             if (resultado == "OK") {
                let dados = response.data.data.Dados
                this.listaACAO   = dados.lista_acao
                this.listaFII    = dados.lista_fii
                this.listaETF    = dados.lista_etf
                this.listaBDR    = dados.lista_bdr
                this.listaCRIPTO = dados.lista_cripto
                this.idEmpty = this.listaACAO.length <= 0
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

    async buscarDadosGrid( idMensal = '' ) {

        let logNome = '@TamoNaBolsa - PagPrincipalOperacao - ' + idMensal

        // console.log(logNome + ' - INI - ', moment().format())
        console.time(logNome + ' - TEMPO')

        if ( idMensal == 'ACAO'   ) this.listaACAO   = []
        if ( idMensal == 'FII'    ) this.listaFII    = []
        if ( idMensal == 'ETF'    ) this.listaETF    = []
        if ( idMensal == 'BDR'    ) this.listaBDR    = []
        if ( idMensal == 'CRIPTO' ) this.listaCRIPTO = []

        let linkUrl = ""
        if ( idMensal == 'ACAO'   ) linkUrl = '/principal/carregarOperacoesAcoes'
        if ( idMensal == 'FII'    ) linkUrl = '/principal/carregarOperacoesFiis'
        if ( idMensal == 'ETF'    ) linkUrl = '/principal/carregarOperacoesEtfs'
        if ( idMensal == 'BDR'    ) linkUrl = '/principal/carregarOperacoesBdrs'
        if ( idMensal == 'CRIPTO' ) linkUrl = '/principal/carregarOperacoesCriptos'

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
                if ( idMensal == 'ACAO'   ) this.listaACAO   = lista
                if ( idMensal == 'FII'    ) this.listaFII    = lista
                if ( idMensal == 'ETF'    ) this.listaETF    = lista
                if ( idMensal == 'BDR'    ) this.listaBDR    = lista
                if ( idMensal == 'CRIPTO' ) this.listaCRIPTO = lista
                if ( idMensal == 'ACAO'   ) this.idEmpty = this.listaACAO.length <= 0
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

var appOperacaoComputeds = {

    TodasOperacoesCompras() {
        try {

            this.total_compra = 0.0

            let operacoes = []
            if ( this.idMensalSelected == 'ACAO'   ) operacoes = this.listaACAO
            if ( this.idMensalSelected == 'FII'    ) operacoes = this.listaFII
            if ( this.idMensalSelected == 'ETF'    ) operacoes = this.listaETF
            if ( this.idMensalSelected == 'BDR'    ) operacoes = this.listaBDR
            if ( this.idMensalSelected == 'CRIPTO' ) operacoes = this.listaCRIPTO

            let vm = this
            let new_operacoes = []
            let total = 0.0
            let isCripto = this.idMensalSelected == 'CRIPTO'

            _.forEach(operacoes, function(value) {
                if ( value[1] == 'C' || value[1] == 'B' ){
                    total += parseFloat(vm.getValDecimal(value[5]))
                    new_operacoes.push({
                        data: moment(value[0], "YYYYMMDD").format('DD/MM/YYYY'),
                        tipo: value[1],
                        ativo: value[2],
                        qtde: isCripto ? value[3].toLocaleString('pt-br', {minimumFractionDigits: 2, maximumFractionDigits: 10}).replace(',00', '') : vm.getFormacataoInteiro(value[3]),
                        preco: value[4], //isCripto ? value[4] : value[4],
                        total: value[5],
                   })
                }
            })

            this.idEmpty = operacoes.length <= 0
            this.total_compra = parseFloat(total)

            return new_operacoes

        } catch (error) {
            console.error('@TamoNaBolsa - TodasOperacoesCompras - Error:', error)
        }
    }, // TodasOperacoesCompras()

    TodasOperacoesVendas() {
        try {

            this.total_venda = 0.0

            let operacoes = []
            if ( this.idMensalSelected == 'ACAO'   ) operacoes = this.listaACAO
            if ( this.idMensalSelected == 'FII'    ) operacoes = this.listaFII
            if ( this.idMensalSelected == 'ETF'    ) operacoes = this.listaETF
            if ( this.idMensalSelected == 'BDR'    ) operacoes = this.listaBDR
            if ( this.idMensalSelected == 'CRIPTO' ) operacoes = this.listaCRIPTO

            let vm = this
            let new_operacoes = []
            let total = 0
            let isCripto = this.idMensalSelected == 'CRIPTO'

            _.forEach(operacoes, function(value) {
                if ( value[1] == 'V' ){
                    total += parseFloat(vm.getValDecimal(value[5]))
                    new_operacoes.push({
                        data: moment(value[0], "YYYYMMDD").format('DD/MM/YYYY'),
                        tipo: value[1],
                        ativo: value[2],
                        qtde: isCripto ? value[3].toLocaleString('pt-br', {minimumFractionDigits: 2, maximumFractionDigits: 10}).replace(',00', '') : vm.getFormacataoInteiro(value[3]),
                        preco: value[4], //isCripto ? value[4] : value[4],
                        total: value[5],
                   })
                }
            })

            // this.idEmpty = operacoes.length <= 0
            this.total_venda = parseFloat(total)

            return new_operacoes

        } catch (error) {
            console.error('@TamoNaBolsa - TodasOperacoesVendas - Error:', error)
        }
    }, // TodasOperacoesVendas()

}

var appOperacaoData = {
    loading: true,
    errored: false,
    idEmpty: true,
    idMensalSelected: 'ACAO',
    listaACAO: [],
    listaFII: [],
    listaETF: [],
    listaBDR: [],
    listaCRIPTO: [],
    total_compra: 0.0,
    total_venda: 0.0,
}

var appOperacao = new Vue({
    el: '#AppOperacao',
    delimiters: ['[[',']]'],
    data: appOperacaoData,
    template: appOperacaoTemplate,
    created () {
        // this.buscarDadosGrid('ACAO')
        // this.buscarDadosGrid('FII')
        // this.buscarDadosGrid('ETF')
        // this.buscarDadosGrid('BDR')
        // this.buscarDadosGrid('CRIPTO')
        // this.buscarDados()
    },
    mounted () {
        // this.buscarDadosGrid('ACAO')
        // this.buscarDadosGrid('FII')
        // this.buscarDadosGrid('ETF')
        // this.buscarDadosGrid('BDR')
        // this.buscarDadosGrid('CRIPTO')
        let vm = this
        setTimeout(function(){ vm.buscarDados(); }, 1000);
    },
    methods: appOperacaoMethods,
    computed: appOperacaoComputeds,
});
