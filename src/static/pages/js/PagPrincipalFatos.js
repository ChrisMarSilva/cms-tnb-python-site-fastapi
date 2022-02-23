
var appFatosTemplate = `
 <div class="row clearfix">
    <div class="col-lg-12">
        <div class="card border">
            <div class="header" style="padding: 0px; padding-top: 20px; padding-left: 20px;">
                <h2><strong><a href="/fatos">FATOS RELEVANTES</a></strong> NO MÊS</h2>
            </div>
            <div class="body" style="max-height: 410px; height: 410px; margin: 0px 0px 20px; padding: 0px;">

                <div class="row clearfix">
                    <div class="col-lg-12  d-flex justify-content-center">
                        <button style="width: 150px; " @click="idFatosSelected='ACAO'" v-bind:class="{ 'btn-simple btn-default': idFatosSelected != 'ACAO', 'btn-primary': idFatosSelected == 'ACAO' }" class="btn btn-sm btn-round waves-effect" id="change-view-today">AÇÕES ([[ listaACAO.length  ]])</button>&nbsp;
                        <button style="width: 150px; " @click="idFatosSelected='FII'"  v-bind:class="{ 'btn-simple btn-default': idFatosSelected != 'FII',  'btn-primary': idFatosSelected == 'FII'  }" class="btn btn-sm btn-round waves-effect" id="change-view-day">FIIs ([[ listaFII.length  ]])</button>&nbsp;
                        <button style="width: 150px; " @click="idFatosSelected='ETF'"  v-bind:class="{ 'btn-simple btn-default': idFatosSelected != 'ETF',  'btn-primary': idFatosSelected == 'ETF'  }" class="btn btn-sm btn-round waves-effect" id="change-view-week">ETFs ([[ listaETF.length  ]])</button>&nbsp;
                        <button style="width: 150px; " @click="idFatosSelected='BDR'"  v-bind:class="{ 'btn-simple btn-default': idFatosSelected != 'BDR',  'btn-primary': idFatosSelected == 'BDR'  }" class="btn btn-sm btn-round waves-effect" id="change-view-month">BDRs ([[ listaBDR.length  ]])</button>&nbsp;
                    </div>
                </div>

                <div class="row clearfix" style="max-height: 380px; height: 380px; overflow-y: auto; overflow-x: hidden; margin: 0px; padding: 0px;">
                   <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12" style="">

                        <div v-if="loading" class="text-center">
                            <div class="contentAnimated"> <div class="animated"> <div class="parent"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="description"></div> <div class="padding"></div> <div class="description"></div> </div> <div class="animated"> <div class="parent"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="description"></div> <div class="padding"></div> <div class="description"></div> </div> </div>
                        </div>
                        <div v-else>
                            <div v-if="errored" class="text-center" style="padding-top: 50px;">
                                Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                            </div>
                            <div v-else>

                                <div v-if="idEmpty" class="text-center"  style="padding-top: 50px;">
                                    <div class="text-center"><small style="font-size:14px; margin: 20px;" class="font-italic text-muted">Nenhum Fato Relevante comunicado...</small></div>
                                </div>
                                <div v-else>
                                    <ul :id="'ulFato-' + idFatosSelected" style="font-size:11px; padding: 0px; padding-left: 10px; padding-top: 5px; border: 0px solid green; " class="text-muted">
                                        <li v-for="(fato, indx) in TodosFatos" :id="'liFato-' + fato.tipoInvest + '-' + fato.id" style="list-style-type:circle; margin-bottom: 5px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 550px;" >
                                            <a class="text-danger" style="float: center; font-size:10px;" title="Remover Fato Relevante" href="javascript:void(0)" @click="removerFatoRelevante(indx, fato.id, fato.tipoInvest)"> <i class="fa fa-check fa-2x" aria-hidden="true"></i> </a>
                                            &nbsp;
                                            <a :class="fato.corTexto" data-html="true" data-toggle="tooltip" data-placement="bottom" title="Clique aqui para ver o conteúdo completo" :href="fato.link" target="_blank"> <span>[[ fato.datahora ]]</span> - <span>[[ fato.protocolo ]]</span> - <span class="font-weight-bold">[[ fato.empresa ]]</span> - <span>[[ fato.assunto ]]</span> </a>
                                        </li>
                                    </ul>
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

var appFatosMethods = {

    async buscarDados() {

        let logNome = '@TamoNaBolsa - PagPrincipalFatos'

        // console.log(logNome + ' - INI - ', moment().format())
        console.time(logNome + ' - TEMPO')

        this.listaACAO = []
        this.listaFII  = []
        this.listaETF  = []
        this.listaBDR  = []

        axios({
          method: 'post',
          url: '/principal/carregarfatosportipos',
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
        })
        .then( (response) => {
             let resultado = response.data.data.Resultado;
             if (resultado == "OK") {
                let dados = response.data.data.Dados
                this.listaACAO = dados.lista_acao
                this.listaFII  = dados.lista_fii
                this.listaETF  = dados.lista_etf
                this.listaBDR  = dados.lista_bdr
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


    async buscarDadosGrid( idFatos = '' ) {

        let logNome = '@TamoNaBolsa - PagPrincipalFatos - ' + idFatos

        // console.log(logNome + ' - INI - ', moment().format())
        console.time(logNome + ' - TEMPO')

        if ( idFatos == 'ACAO' ) this.listaACAO  = []
        if ( idFatos == 'FII'  ) this.listaFII   = []
        if ( idFatos == 'ETF'  ) this.listaETF   = []
        if ( idFatos == 'BDR'  ) this.listaBDR   = []

        let linkUrl = ""
        if ( idFatos == 'ACAO' ) linkUrl = '/principal/carregarFatosAcoes'
        if ( idFatos == 'FII'  ) linkUrl = '/principal/carregarFatosFiis'
        if ( idFatos == 'ETF'  ) linkUrl = '/principal/carregarFatosEtfs'
        if ( idFatos == 'BDR'  ) linkUrl = '/principal/carregarFatosBdrs'

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
                if ( idFatos == 'ACAO'  ) this.listaACAO = lista
                if ( idFatos == 'FII'   ) this.listaFII  = lista
                if ( idFatos == 'ETF'   ) this.listaETF  = lista
                if ( idFatos == 'BDR'   ) this.listaBDR  = lista
                if ( idFatos == 'ACAO'  ) this.idEmpty = this.listaACAO.length <= 0
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

    async removerFatoRelevante (indx, fatoId, fatoTipoInvest) {

        if ( fatoTipoInvest == 'ACAO'  ) this.listaACAO.splice(indx, 1)
        if ( fatoTipoInvest == 'FII'   ) this.listaFII.splice(indx, 1)
        if ( fatoTipoInvest == 'ETF'   ) this.listaETF.splice(indx, 1)
        if ( fatoTipoInvest == 'BDR'   ) this.listaBDR.splice(indx, 1)

        let logNome = '@TamoNaBolsa - removerFatoRelevante - ' + fatoTipoInvest

        console.clear()
        // console.log(logNome + ' - INI - ', moment().format())
        console.time(logNome + ' - TEMPO')

        axios({
          method: 'post',
          url: "/principal/removerFatoRelevante",
          timeout: 60000, // 60seg // 1Min
          responseType: 'json',
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify({ IdFato: fatoId, TipoInvest: fatoTipoInvest }),
        })
        .then( (response) => {
             let resultado = response.data.data.Resultado
             if (resultado == "OK") {
                 return true
             } else {
                 let mensagem = response.data.data.Mensagem
                 console.warn(logNome + ' - WANNING: ', mensagem)
             }
        })
        .catch( (error) => {
            console.error(logNome + ' - ERRO: ', error)
        })
        .finally( () => {
            this.loading = false
            // console.log(logNome + ' - FIM - ', moment().format())
            console.timeEnd(logNome + ' - TEMPO')
        })

    }, // removerFatoRelevante()

};

var appFatosComputeds = {

    TodosFatos() {
        try {

            let fatos = []
            if ( this.idFatosSelected == 'ACAO'  ) fatos = this.listaACAO
            if ( this.idFatosSelected == 'FII'   ) fatos = this.listaFII
            if ( this.idFatosSelected == 'ETF'   ) fatos = this.listaETF
            if ( this.idFatosSelected == 'BDR'   ) fatos = this.listaBDR

            let new_fatos = []
            let dataAtual = moment().format('YYYYMMDD').toString()

            _.forEach(fatos, function(value) {
                dataLocal = value[2].substring(0,8).toString()
                new_fatos.push({
                    id: value[0],
                    empresa: value[1],
                    datahora: moment(value[2], "YYYYMMDDHHmmss").format('DD/MM/YYYY HH:mm'),
                    link: value[3],
                    assunto: value[4],
                    protocolo: value[5],
                    tipoInvest: value[6],
                    corTexto: dataAtual == dataLocal ? 'text-primary' : 'text-muted'
               })
            })

            return new_fatos

        } catch (error) {
            console.error('@TamoNaBolsa - TodosFatos - Error:', this.idFatosSelected, error)
        }
    },

}

var appFatosWatch = {

    idFatosSelected: function(val) {
        if ( val == 'ACAO' ) this.idEmpty = this.listaACAO.length <= 0;
        if ( val == 'FII'  ) this.idEmpty = this.listaFII.length  <= 0;
        if ( val == 'ETF'  ) this.idEmpty = this.listaETF.length  <= 0;
        if ( val == 'BDR'  ) this.idEmpty = this.listaBDR.length  <= 0;
        //console.log('value changed from', val, this.idEmpty);
    },

}

var appFatosData = {
    loading: true,
    errored: false,
    idEmpty: true,
    idFatosSelected: 'ACAO',
    listaACAO: [],
    listaFII: [],
    listaETF: [],
    listaBDR: [],
}

var appFatos = new Vue({
    el: '#AppFatos',
    delimiters: ['[[',']]'],
    data: appFatosData,
    template: appFatosTemplate,
    created () {
        // this.buscarDadosGrid('ACAO')
        // this.buscarDadosGrid('FII')
        // this.buscarDadosGrid('ETF')
        // this.buscarDadosGrid('BDR')
        // this.buscarDados()
    },
    mounted () {
        // this.buscarDadosGrid('ACAO')
        // this.buscarDadosGrid('FII')
        // this.buscarDadosGrid('ETF')
        // this.buscarDadosGrid('BDR')
        let vm = this
        setTimeout(function(){ vm.buscarDados(); }, 1000);
    },
    methods: appFatosMethods,
    computed: appFatosComputeds,
    watch: appFatosWatch,
});
