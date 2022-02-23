
// ---------------------------------------------------------------------------------------------------------
// ---------------------------------------------------------------------------------------------------------

var template_app_minhas_acoes = `
<div>

    <div v-if="loading" class="text-center">
        <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
    </div>

    <div v-else>

        <div v-if="errored" class="text-cente">
            Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
         </div>

        <div v-else>

            <div v-if="empty" class="text-center">
                NENHUM RESULTADO ENCONTRADO
            </div>

            <div v-else>

                <div class="table-responsive">
                    <table class="table table-hover m-b-0" border="0">
                        <tbody>
                            <tr v-for="(ativo, indx) in TodosAtivos">
                                <td style="width: 80px;">
                                    <a target="_blank" style="text-deco ration:none;" :href="'/finan/acoes/' + ativo.codigos[0]">
                                        <img :src="ativo.logo" alt="" width="48" height="48" class="lozad rounded -circle img-raised" onerror="this.onerror=null;this.src=\'/static/pages/ativos/SEMLOGO.gif\';" />
                                    </a>
                                </td>
                                <td>
                                    <h6 style="margin-bottom: 10px; ">[[ ativo.nome ]]</h6>
                                    <a v-for="codigo in ativo.codigos" target="_blank" style="text-deco ration:none;" :href="'/finan/acoes/' + codigo"><span class="badge badge-info bg-info text-white font-weight-bold">[[ codigo ]]</span></a>
                                </td>
                                <td class="text-right">
                                    <div class="mb-0 margin-0"> <h6 style="font-size: 18px;" >R$ [[ formatPrice(ativo.cotacao) ]]</h6> </div>
                                    <div> <small style="font-size: 10px;" :class='[[ ativo.variacao_color ]]'> <i style="font-size: 12px;"  :class='[[ ativo.variacao_icon ]]'> [[ formatPrice(ativo.variacao_percent) ]]% </small> </div>
                                    <div style="font-size: 12px;" class="text-muted">R$ [[ formatPrice(ativo.variacao_valor) ]]</div><!--  -->
                                </td>
                            </tr>
                    </table>
                </div>

            </div>

        </div>

    </div>

</div>
`;

var methods_app_minhas_acoes = {

    formatPrice(value) {
        let val = (value/1).toFixed(2).replace('.', ',')
        return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    },

    buscar_dados() {

        this.loading = true
        this.errored = false
        this.empty = false
        this.ativos = []

        axios({
          method: 'post',
          url: "/finan/acoes/grid",
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify({ FiltroTipo: 'M', FiltroEmpresa: "" }),
        })
        .then( (response) => {
             let resultado = response.data.data.Resultado
             if (resultado == "OK") {
                 let lista = response.data.data.Lista
                 this.ativos = lista;
                 this.empty =  lista.length <= 0
                 return true;
             } else {
                 this.errored = true;
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

var computeds_app_minhas_acoes = {
    TodosAtivos() {
        return this.ativos.map(ativo => ({
         ...ativo,
         variacao_icon: 'zmdi zmdi-trending-' + (ativo.variacao_valor == 0.0 ? 'flat' : ativo.variacao_valor > 0.0 ? 'up' : 'down'),
         variacao_color: 'text-' + (ativo.variacao_valor == 0.0 ? 'primary' : ativo.variacao_valor > 0.0 ? 'success' : 'danger'),
        }))
    },
};

var data_app_minhas_acoes = {
    loading: true,
    errored: false,
    empty: false,
    ativos: [],
};

var app_minhas_acoes = new Vue({
    el: '#AppMinhaAcoes',
    delimiters: ['[[',']]'],
    template: template_app_minhas_acoes,
    data: data_app_minhas_acoes,
    created () { this.buscar_dados() },
    mounted() { },
    methods: methods_app_minhas_acoes,
    computed: computeds_app_minhas_acoes,
});

// ---------------------------------------------------------------------------------------------------------
// ---------------------------------------------------------------------------------------------------------

var template_app_demais_acoes = `
<div>

    <div class="form-group">
        <input type="text" class="form-control" v-model="filtroEmpresa" @keyup="keyPressFiltroEmpresa($event)" @keyup.enter="enterClickedFiltroEmpresa()"  name="TxtFiltroEmpresa" placeholder="Buscar por Empresa..." style="background-color: white;">
    </div>

    <div v-if="loading" class="text-center">
        <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
    </div>

    <div v-else>

        <div v-if="errored" class="text-cente">
            Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
         </div>

        <div v-else>

            <div v-if="empty" class="text-center">
                NENHUM RESULTADO ENCONTRADO
            </div>

            <div v-else>

                <div class="row clearfix">
                    <div class="col-lg-4 col-md-6 col-sm-12" v-for="(ativo, indx) in TodosAtivos">
                        <div class="card" style="min-height: 280px; max-height: 280px;">
                            <div class="body text-center">
                                <div class="chart"> <img :src="ativo.logo" alt="" width="90" height="90" class="lozad rounded -circle img-raised" onerror="this.onerror=null;this.src=\'/static/pages/ativos/SEMLOGO.gif\';" /> </div>
                                <h6>[[ ativo.nome ]]</h6>
                                <a v-for="codigo in ativo.codigos" target="_blank" style="text-deco ration:none;" :href="'/finan/acoes/' + codigo"><span class="badge badge-info bg-info text-white font-weight-bold">[[ codigo ]]</span></a>
                                <br>
                                <small class="text-muted"> [[ ativo.setor ]] <b>/</b> [[ ativo.subsetor ]] <b>/</b> [[ ativo.segmento ]]</small>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card" v-if="filtroPaginas.length > 1">
                    <div class="body">
                        <ul class="pagination pagination-primary m-b-0 justify-content-center">
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

    </div>

</div>
`;

var methods_app_demais_acoes = {

    formatPrice(value) {
        let val = (value/1).toFixed(2).replace('.', ',')
        return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    },

    enterClickedFiltroEmpresa() {
        // this.buscar_dados(1)
        // let filtro = this.filtroEmpresa.toLowerCase()
        this.ativos = this.todos_ativos.filter( (ativo) => {

//           return ativo.nome.toLowerCase().includes(filtro) ||
//                  ativo.setor.toLowerCase().includes(filtro)  ||
//                  ativo.subsetor.toLowerCase().includes(filtro) ||
//                  ativo.segmento.toLowerCase().includes(filtro) ||
//                  ativo.codigos.some( (codigo) => { return codigo.toLowerCase().includes(filtro) })

           return this.filtroEmpresa.toLowerCase().split(' ').every( filtro => // every // some
                ativo.nome.toLowerCase().includes(filtro) ||
                ativo.setor.toLowerCase().includes(filtro) ||
                ativo.subsetor.toLowerCase().includes(filtro) ||
                ativo.segmento.toLowerCase().includes(filtro) ||
                ativo.codigos.some( (codigo) => { return codigo.toLowerCase().includes(filtro) })
            )

        })
    },

    keyPressFiltroEmpresa: function($event) {
        if (this.filtroEmpresa.trim() === '')
           this.ativos = this.todos_ativos // this.buscar_dados(1)
         else
            this.enterClickedFiltroEmpresa()
    },

    setPaginacao () {
        this.filtroPaginas = []
        let numberOfPages = Math.ceil(this.ativos.length / this.filtroPagMax)  // N of items (100) / 10 items per page
        for (i = 1; i <= numberOfPages; i++) //generate 10 pages (100 / 10)
            this.filtroPaginas.push(i)
    },

    buscar_dados( pag_atual = 1 ) {

        this.loading = true
        this.errored = false
        this.empty = false
        // this.todos_ativos = []
        // this.ativos = []

        axios({
          method: 'post',
          url: "/finan/acoes/grid",
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify({ FiltroTipo: '', FiltroEmpresa: this.filtroEmpresa, FiltroPagAtual: pag_atual }),
        })
        .then( (response) => {
             let resultado = response.data.data.Resultado;
             if (resultado == "OK") {
                 let lista = response.data.data.Lista
                 this.todos_ativos = lista
                 this.ativos = lista
                 this.empty =  lista.length <= 0
                 return true;
             } else {
                 this.ativos = []
                 this.errored = true;
                 let mensagem = response.data.data.Mensagem;
                 console.log('@TamoNaBolsa:Mensagem',mensagem)
             }
        })
        .catch( (error) => {
            this.todos_ativos = []
            this.ativos = []
            this.errored = true
            console.log('@TamoNaBolsa:Error',error)
        })
        .finally( () => {
            this.loading = false
        })

    },

};

var computeds_app_demais_acoes = {

    TodosAtivos() {
        let start = (this.filtroPagAtual * this.filtroPagMax) - this.filtroPagMax
        let end = this.filtroPagAtual * this.filtroPagMax
        let new_ativos = this.ativos.slice(start, end)
        return new_ativos.map(ativo => ({
            ...ativo,
            variacao_icon: 'zmdi zmdi-trending-' + (ativo.variacao_valor == 0.0 ? 'flat' : ativo.variacao_valor > 0.0 ? 'up' : 'down'),
            variacao_color: 'text-' + (ativo.variacao_valor == 0.0 ? 'primary' : ativo.variacao_valor > 0.0 ? 'success' : 'danger'),
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

var watchs_app_demais_acoes = {
    ativos () { this.setPaginacao() }
};

var data_app_demais_acoes = {
    loading: true,
    errored: false,
    empty: false,
    todos_ativos: [],
    ativos: [],
    filtroPagMax: 9,
    filtroPagAtual: 1,
    filtroPaginas: [],
    filtroEmpresa: '',
};

var app_demais_acoes = new Vue({
    el: '#AppDemaisAcoes',
    delimiters: ['[[',']]'],
    template: template_app_demais_acoes,
    created () { this.buscar_dados() },
    mounted() { },
    data: data_app_demais_acoes,
    methods: methods_app_demais_acoes,
    computed: computeds_app_demais_acoes,
	watch: watchs_app_demais_acoes,
});

// ---------------------------------------------------------------------------------------------------------
// ---------------------------------------------------------------------------------------------------------
