
var appInvestiorTemplate = `
<div>

    <div class="row clearfix">
        <div class="col-lg-12">

            <div class="card">
                <ul class="row profile_state list-unstyled">
                    <li class="col-lg-3 col-md-3 col-6">
                        <div class="body">
                            <i class="zmdi zmdi-account col-amber"></i>
                            <h4>[[ numTotalInvestidores ]]</h4>
                            <b><span>TOTAL</span></b>
                        </div>
                    </li>
                    <li class="col-lg-3 col-md-3 col-6">
                        <div class="body">
                            <i class="zmdi zmdi-eye col-blue"></i>
                            <h4>[[ numLogadosInvestidores ]]</h4>
                            <b><span>LOGADOS</span></b>
                        </div>
                    </li>
                    <li class="col-lg-3 col-md-3 col-6">
                        <div class="body">
                            <i class="zmdi zmdi-thumb-up text-success"></i>
                            <h4>[[ numAtivosInvestidores ]]</h4>
                            <b><span>ATIVOS</span></b>
                        </div>
                    </li>
                    <li class="col-lg-3 col-md-3 col-6">
                        <div class="body">
                            <i class="zmdi zmdi-thumb-down col-red"></i>
                            <h4>[[ numInativosInvestidores ]]</h4>
                            <b><span>INATIVOS</span></b>
                        </div>
                    </li>
                </ul>
            </div>

        </div>
    </div>

    <div class="row clearfix text-right">
        <div class="col">
            <button type="button" class="btn btn-round btn-simple btn-sm btn-default btn-filter" @click="filtarInvestidores('T')">Todos</button>
            <button type="button" class="btn btn-round btn-simple btn-sm btn-warning btn-filter" @click="filtarInvestidores('L')">Logados</button>
            <button type="button" class="btn btn-round btn-simple btn-sm btn-success btn-filter" @click="filtarInvestidores('A')">Ativos</button>
            <button type="button" class="btn btn-round btn-simple btn-sm btn-info    btn-filter" @click="filtarInvestidores('P')">Pendentes</button>
            <button type="button" class="btn btn-round btn-simple btn-sm btn-danger  btn-filter" @click="filtarInvestidores('I')">Inativos</button>
        </div>
    </div>

    <br/>

    <div class="row clearfix">
        <div class="col-lg-12">
            <div class="card border">
                <div class="header"> <h2><strong>Investidor</strong></h2> </div>
                <div class="body">

                    <div class="row clearfix">
                        <div class="col">

                            <div v-if="loading" class="text-center">

                                <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>

                            </div>
                            <div v-else>

                                <div v-if="errored" class="text-cente">
                                    Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                                 </div>
                                <div v-else>

                                    <div class="row clearfix">
                                        <div class="col-8">
                                        </div>
                                        <div class="col-4">
                                            <input type="text" v-model="filtroInvestidor" placeholder="Buscar por Investidor..." class="form-control" style="background-color: white;">
                                        </div>
                                    </div>

                                    <br/>

                                    <div class="table-responsive" id="AreaGrid">
                                        <table ref="gridInvestidores" style="font-size: 12px" class="table table-sm table-hover table-condensed table-bo rdered nowrap m-b-0" cellspacing="0" width="100%">
                                            <thead>
                                                <tr class="thead-dark font-weight-bold">
                                                    <th>Foto</th>
                                                    <th>Nome</th>
                                                    <th>Email</th>
                                                    <th>DtCriação</th>
                                                    <th>A-Lanc</th>
                                                    <th>A-Prov</th>
                                                    <th>F-FII</th>
                                                    <th>F-Rend</th>
                                                    <th>E-ETF</th>
                                                    <th>B-Lanc</th>
                                                    <th>B-Prov</th>
                                                    <th>C-Lanc</th>
                                                    <th>Site</th>
                                                    <th>App</th>
                                                    <th>Sit.</th>
                                                    <th style="display: none;">IdUsuario</th>
                                                    <th>Ação</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr  class="text-center" v-for="(investidor, indx) in TodosInvestidores" :key="investidor.id">
                                                    <td> <img :src="investidor.foto" onerror="this.onerror=null;this.src=\'/static/pages/img/pessoa-icon.png\';" alt="" width="25" height="25" class="rounded-circle" /> </td>
                                                    <td>[[ investidor.nome ]]</td>
                                                    <td>[[ investidor.email ]]</td>
                                                    <td class="text-center">[[ investidor.dtCriacao ]]</td>
                                                    <td class="text-center">[[ investidor.acaoLanc ]]</td>
                                                    <td class="text-center">[[ investidor.acaoProv ]]</td>
                                                    <td class="text-center">[[ investidor.fiiLanc ]]</td>
                                                    <td class="text-center">[[ investidor.fiiProv ]]</td>
                                                    <td class="text-center">[[ investidor.etfLanc ]]</td>
                                                    <td class="text-center">[[ investidor.bdrLanc ]]</td>
                                                    <td class="text-center">[[ investidor.bdrProv ]]</td>
                                                    <td class="text-center">[[ investidor.criptoLanc ]]</td>
                                                    <td class="text-center">[[ investidor.dtHrLogSite ]]</td>
                                                    <td class="text-center">[[ investidor.dtHrLogApp ]]</td>
                                                    <td :class="investidor.corTexto" class="font-weight-bold text-center">[[ investidor.situacao ]]</td>
                                                    <td style="display: none;">[[ investidor.id ]]</td>
                                                    <td>
                                                        <div class="btn-group btn-group-sm">
<a @click="alterarNomeInvestidor(indx, investidor.id, investidor.nome)" class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:9px;" title="Alterar Nome" href="javascript:void(0);"> <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> </a>
&nbsp;
<a @click="alterarSituacaoInvestidor(indx, investidor.id, 'A')" :class="{'disabled' : (investidor.situacao == 'Ativo')}" class="btn btn-sm btn-success btn-icon btn-icon-mini btn-round btn-simple" style="font-size:8px;" title="Ativar" href="javascript:void(0);"> <i class="fa fa-thumbs-up text-success" aria-hidden="true"></i> </a>
&nbsp;
<a @click="alterarSituacaoInvestidor(indx, investidor.id, 'I')" :class="{'disabled' : (investidor.situacao == 'Inativo')}" class="btn btn-sm btn-muted btn-icon btn-icon-mini btn-round btn-simple" style="font-size:8px;" title="Inativar" href="javascript:void(0);" > <i class="fa fa-thumbs-down text-muted" aria-hidden="true"></i> </a>
&nbsp;
<a @click="alterarSituacaoInvestidor(indx, investidor.id, 'X')" :class="{'disabled' : (investidor.situacao == 'Bloqueado')}" class="btn btn-sm btn-dark btn-icon btn-icon-mini btn-round btn-simple" style="font-size:8px;" title="Bloquar" href="javascript:void(0);" > <i class="fa fa-lock text-secondary" aria-hidden="true"></i> </a>
&nbsp;
<a @click="gerarCarteiraInvestidor(indx, investidor.id)" class="btn btn-sm btn-primary btn-icon btn-icon-mini btn-round btn-simple" style="font-size:8px;" title="Gerar" href="javascript:void(0);" > <i class="fa fa-calculator text-primary" aria-hidden="true"></i>  </a>
&nbsp;
<a @click="excluirInvestidor(indx, investidor.id)" class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:8px;" title="Excluir" href="javascript:void(0);" role="button" aria-pressed="true"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> </a>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>

                                </div>

                            </div>

                        </div>
                    </div>

                    <br/>

                </div>
            </div>
        </div>
    </div>

</div>
`;

var appInvestior = new Vue({
    el: '#AppInvestiores',
    delimiters: ['[[',']]'],
    template: appInvestiorTemplate,
    data: {
        loading: true,
        errored: false,
        investidores: [],
        numTotalInvestidores: 0,
        numLogadosInvestidores: 0,
        numAtivosInvestidores: 0,
        numInativosInvestidores: 0,
        filtroInvestidor: '',
        filtroSituacao: '',
        filtroDataIni: moment().format('DD/MM/YYYY'),
        filtroDataFim: '',
    },
    methods: {

        filtarInvestidores(tipo) {
            if ( tipo == 'T'){
                this.filtroSituacao = ''
                this.filtroDataIni = ''
            } else if ( tipo == 'L'){
                this.filtroSituacao = ''
                this.filtroDataIni = moment().format('DD/MM/YYYY')
            } else if ( tipo == 'A'){
                this.filtroSituacao = 'Ativo'
                this.filtroDataIni = ''
            } else if ( tipo == 'P'){
                this.filtroSituacao = 'Aguardando Confirmação de Email'
                this.filtroDataIni = ''
            } else if ( tipo == 'I'){
                this.filtroSituacao = 'Inativo'
                this.filtroDataIni = ''
            }
        },

        getFormacataoInteiro(value) {
          return String(value).split('').reverse().join('').split(/(\d{3})/).filter(Boolean).join('.').split('').reverse().join('');
        },

        buscarDados() {

            this.loading = true
            this.errored = false
            this.investidores = []
            this.numTotalInvestidores = 0
            this.numLogadosInvestidores = 0
            this.numAtivosInvestidores = 0
            this.numInativosInvestidores = 0

            let logNome = '@TamoNaBolsa - PagInvestiores'

            // console.log(logNome + ' - INI - ', moment().format())
            console.time(logNome + ' - TEMPO')

            axios({
                method: 'post',
                url: '/investidor/grid',
                timeout: 60000, // 60seg // 1Min
                responseType: 'json',
                headers: { 'Content-Type': 'application/json' },
                // data: JSON.stringify({ DataIni : this.filtroDataIni, DataFim : this.filtroDataFim, Situacao : this.filtroSituacao, }),
                data: JSON.stringify({ DataIni : '', DataFim : '', Situacao : '', }),
            })
            .then( (response) => {
                 let resultado = response.data.data.Resultado
                 if (resultado == "OK") {
                     let lista = response.data.data.Lista
                     this.investidores = lista
                     return true
                 } else {
                     this.errored = true
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

        alterarNomeInvestidor(indx, IdUsuario, NomeUsuario) {

            let logNome = '@TamoNaBolsa - PagInvestiores - AlterarNomeInvestidor'

            if ( NomeUsuario.indexOf(")") > 0 )
                NomeUsuario = NomeUsuario.substring( NomeUsuario.indexOf(")")+2, NomeUsuario.length)

            var NomeUsuario = prompt("Nome Investidor", NomeUsuario);

            if (NomeUsuario == null || NomeUsuario == "")
                return

            axios({
                method: 'post',
                url: '/investidor/alterarnome',
                timeout: 60000, // 60seg // 1Min
                responseType: 'json',
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify({ IdUsuario: IdUsuario, NomeUsuario: NomeUsuario, }),
            })
            .then( (response) => {
                 let resultado = response.data.data.Resultado
                 if (resultado == "OK") {
                     let investidor = this.investidores[indx]
                     investidor[1] = NomeUsuario
                     Vue.set(this.investidores, indx, investidor)
                     return true
                 } else {
                     let mensagem = response.data.data.Mensagem
                     console.warn(logNome + ' - WANNING: ', mensagem)
                 }
            })
            .catch( (error) => {
                console.error(logNome + ' - ERRO: ', error)
            })


        },

        excluirInvestidor(indx, IdUsuario) {

            let logNome = '@TamoNaBolsa - PagInvestiores - ExcluirInvestidor'

            var resp = confirm("Você realmente deseja excluir o Investidor?")

            if (resp != true)
                return

            axios({
                method: 'post',
                url: '/investidor/excluir',
                timeout: 60000, // 60seg // 1Min
                responseType: 'json',
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify({ IdUsuario : IdUsuario, }),
            })
            .then( (response) => {
                 let resultado = response.data.data.Resultado
                 if (resultado == "OK") {
                     this.investidores.splice(indx, 1)
                     return true
                 } else {
                     let mensagem = response.data.data.Mensagem
                     console.warn(logNome + ' - WANNING: ', mensagem)
                 }
            })
            .catch( (error) => {
                console.error(logNome + ' - ERRO: ', error)
            })

        },

        alterarSituacaoInvestidor(indx, IdUsuario, Situacao) {

            let logNome = '@TamoNaBolsa - PagInvestiores - AlterarSituacaoInvestidor'

            axios({
                method: 'post',
                url: '/investidor/alterarsituacao',
                timeout: 60000, // 60seg // 1Min
                responseType: 'json',
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify({ IdUsuario : IdUsuario, Situacao : Situacao, }),
            })
            .then( (response) => {
                 let resultado = response.data.data.Resultado
                 if (resultado == "OK") {
                     let investidor = this.investidores[indx]
                     if (Situacao == "A"){
                        investidor[14] = 'Ativo'
                     } else if (Situacao == "I"){
                        investidor[14]  = 'Inativo'
                     } else { // if (Situacao == "X"){
                        investidor[14] = 'Bloqueado'
                     }
                     Vue.set(this.investidores, indx, investidor)
                     return true
                 } else {
                     let mensagem = response.data.data.Mensagem
                     console.warn(logNome + ' - WANNING: ', mensagem)
                 }
            })
            .catch( (error) => {
                console.error(logNome + ' - ERRO: ', error)
            })

        },

        gerarCarteiraInvestidor(indx, IdUsuario) {

            let logNome = '@TamoNaBolsa - PagInvestiores - GerarCarteiraInvestidor'

            axios({
                method: 'post',
                url: '/investidor/gerarcarteira',
                timeout: 600000, // 600seg // 10Min
                responseType: 'json',
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify({ IdUsuario : IdUsuario, }),
            })
            .then( (response) => {
                 let resultado = response.data.data.Resultado
                 if (resultado == "OK") {
                     alert('OK - '+ IdUsuario)
                     console.log(logNome + ' - SUCCESS: ', IdUsuario)
                     return true
                 } else {
                     let mensagem = response.data.data.Mensagem
                     console.warn(logNome + ' - WANNING: ', mensagem)
                 }
            })
            .catch( (error) => {
                console.error(logNome + ' - ERRO: ', error)
            })

        },

    },
    computed: {

        TodosInvestidores() {
            try{

                let vm = this
                vm.numTotalInvestidores = 0
                vm.numLogadosInvestidores = 0
                vm.numAtivosInvestidores = 0
                vm.numInativosInvestidores = 0
                let dataAtual = moment().format('YYYYMMDD')

                let new_investidores = []

                _.forEach(this.investidores, function(value) {

                    vm.numTotalInvestidores += 1
                    if ( value[12].substr(0, 8) == dataAtual || value[13].substr(0, 8) == dataAtual )
                        vm.numLogadosInvestidores += 1
                    if ( value[14] == 'Ativo')
                        vm.numAtivosInvestidores += 1
                    else
                        vm.numInativosInvestidores += 1

                    new_investidores.push({
                        foto: value[0],
                        nome: value[1],
                        email: value[2],
                        dtCriacao: moment(value[3], "YYYYMMDD").format('DD/MM/YYYY'),
                        acaoLanc: vm.getFormacataoInteiro(value[4]),
                        acaoProv: vm.getFormacataoInteiro(value[5]),
                        fiiLanc: vm.getFormacataoInteiro(value[6]),
                        fiiProv: vm.getFormacataoInteiro(value[7]),
                        etfLanc: vm.getFormacataoInteiro(value[8]),
                        bdrLanc: vm.getFormacataoInteiro(value[9]),
                        bdrProv: vm.getFormacataoInteiro(value[10]),
                        criptoLanc: vm.getFormacataoInteiro(value[11]),
                        dtHrLogSite: value[12] == '' ? '' : moment(value[12], "YYYYMMDDHHmmss").format('DD/MM/YYYY HH:mm:ss'),
                        dtHrLogApp: value[13] == '' ? '' : moment(value[13], "YYYYMMDDHHmmss").format('DD/MM/YYYY HH:mm:ss'),
                        situacao: value[14],
                        id: value[15],
                        corTexto: 'text-' + (value[14] == 'Ativo' ? 'success' : 'danger'),
                    })
                })

                if (vm.filtroSituacao != "" || vm.filtroDataIni == ""){
                    if (vm.filtroSituacao == "Inativo")
                        new_investidores = _.filter(new_investidores, function(investior) { return investior.situacao.includes('I') || investior.situacao.includes('X') || investior.situacao.includes('B'); })
                    else
                        new_investidores = _.filter(new_investidores, function(investior) { return investior.situacao.includes(vm.filtroSituacao); })
                }

                if (vm.filtroSituacao == "" || vm.filtroDataIni != ""){
                    new_investidores = _.filter(new_investidores, function(investior) { return investior.dtHrLogSite.substr(0, 10).includes(vm.filtroDataIni) || investior.dtHrLogApp.substr(0, 10).includes(vm.filtroDataIni); });
                }

                if (vm.filtroInvestidor != ""){
                   new_investidores = _.filter(new_investidores, function(investior) {
                       return vm.filtroInvestidor.toLowerCase().split(' ').every( filtro =>
                            investior.nome.toLowerCase().includes(filtro) ||
                            investior.email.toLowerCase().includes(filtro) ||
                            investior.situacao.toLowerCase().includes(filtro) ||
                            investior.dtCriacao.toLowerCase().includes(filtro) ||
                            investior.dtHrLogSite.toLowerCase().includes(filtro) ||
                            investior.dtHrLogApp.toLowerCase().includes(filtro)
                        )
                   })
                }

                return new_investidores

            } catch (error) {
                console.error('@TamoNaBolsa - Error:', error)
            }
        },

    },
    mounted () {
        this.buscarDados()
    },
});
