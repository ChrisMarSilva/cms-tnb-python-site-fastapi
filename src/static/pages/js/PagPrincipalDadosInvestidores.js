
var template_app_dados_invest = `
<div>

    <div v-if="loading" class="text-center">
        <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
    </div>

    <div v-else>

        <div v-if="errored" class="text-cente">
            Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
         </div>

        <div v-else>

            <!-- Div Dados Para o Admin -->
            <div class="row clearfix">
                <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="card border info-box-2" style="height: 200px;">
                        <div class="header" style="padding: 0px; padding-top: 20px; padding-left: 20px;">
                            <h2><strong><a class="" href="/investidor">Usuários</a></strong></h2>
                        </div>
                        <div class="body">
                            <div class="mr-5" id="DivQtdeInvest" style="font-size: 12px; ">
                                [[ dados.QtdeInvest ]] Usuários no Total <br/>
                                [[ dados.QtdeInvestAguarde ]] Usuários Aguardando <br/>
                                <br/>
                                [[ dados.QtdeInvestCriado ]] Usuários Criados Hoje <br/>
                                [[ dados.QtdeUserLogSite ]] Usuários Logados pelo Site Hoje <br/>
                                [[ dados.QtdeUserLogApp ]] Usuários Logados pelo App Hoje <br/>
                                <br/>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="card border info-box-2" style="height: 200px;">
                        <div class="header" style="padding: 0px; padding-top: 20px; padding-left: 20px;">
                            <h2><strong>Operações</strong></h2>
                        </div>
                        <div class="body">
                            <div class="mr-5" id="DivQtdeOper" style="font-size: 12px; ">
                                AÇÔES &nbsp;&nbsp;- Operações Cadastrados =  [[ dados.QtdeACAOOper ]] <br/>
                                FII &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Operações Cadastrados =  [[ dados.QtdeFIIOper ]] <br/>
                                ETF &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Operações Cadastrados =  [[ dados.QtdeETFOper ]] <br/>
                                BDR &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Operações Cadastrados =  [[ dados.QtdeBDROper ]] <br/>
                                CRIPTO &nbsp;- Operações Cadastrados =  [[ dados.QtdeCRIPTOOper ]] <br/>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6 col-sm-12">
                    <div class="card border info-box-2" style="height: 200px;">
                        <div class="header" style="padding: 0px; padding-top: 20px; padding-left: 20px;">
                            <h2><strong>Proventos</strong></h2>
                        </div>
                        <div class="body">
                            <div class="mr-5" id="DivQtdeProv" style="font-size: 12px; ">
                                AÇÔES - Proventos Cadastrados =  [[ dados.QtdeACAOProv ]] <br/>
                                FII &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Proventos Cadastrados =  [[ dados.QtdeFIIProv ]] <br/>
                                BDR &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Proventos Cadastrados =  [[ dados.QtdeBDRProv ]] <br/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Div Dados Para o Admin -->

        </div>

    </div>

</div>
`;


var app_dados_invest = new Vue({

    el: '#AppDadosInvestidores',

    delimiters: ['[[',']]'],

    template: template_app_dados_invest,

    data: {
        loading: true,
        errored: false,
        dados: null,
    },

    methods: {

        async buscarDados() {

            this.loading = true
            this.errored = false
            this.dados = null

            let logNome = '@TamoNaBolsa - PagPrincipalDadosInvestidores'

            // console.log(logNome + ' - INI - ', moment().format())
            console.time(logNome + ' - TEMPO')

            axios({
              method: 'post',
              url: "/principal/carregar",
              timeout: 60000, // 60seg // 1Min
              responseType: 'json',
              headers: { 'Content-Type': 'application/json' },
            })
            .then( (response) => {
                 let resultado = response.data.data.Resultado
                 if (resultado == "OK") {
                     let dados = response.data.data.Dados
                     this.dados = dados;
                     return true;
                 } else {
                     this.errored = true;
                     let mensagem = response.data.data.Mensagem
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
        },

    },

    created () {
        // this.buscarDados()
    },

    mounted () {
        let vm = this
        setTimeout(function(){ vm.buscarDados(); }, 1000);
    },

});
