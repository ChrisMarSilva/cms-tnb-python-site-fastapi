
var template_app_valorizacao = `
<div>

    <!-- DivTabCateg -->
    <ul class="nav nav-tabs d-flex nav-justified font-weight-bold" role="tablist" style="font-size: 13px; ">
        <li class="nav-item"> <a class="nav-link" @click=" idCategoriaSelected = 'ACAO'   " v-bind:class="{ 'active': idCategoriaSelected == 'ACAO'   }" data-toggle="tab" v-bind:aria-selected="idCategoriaSelected == 'ACAO'   ? true : false"> AÇÕES   ( [[ listaACAO.length   ]] ) </a> </li>
        <li class="nav-item"> <a class="nav-link" @click=" idCategoriaSelected = 'FII'    " v-bind:class="{ 'active': idCategoriaSelected == 'FII'    }" data-toggle="tab" v-bind:aria-selected="idCategoriaSelected == 'FII'    ? true : false"> FIIs    ( [[ listaFII.length    ]] ) </a> </li>
        <li class="nav-item"> <a class="nav-link" @click=" idCategoriaSelected = 'ETF'    " v-bind:class="{ 'active': idCategoriaSelected == 'ETF'    }" data-toggle="tab" v-bind:aria-selected="idCategoriaSelected == 'ETF'    ? true : false"> ETFs    ( [[ listaETF.length    ]] ) </a> </li>
        <li class="nav-item"> <a class="nav-link" @click=" idCategoriaSelected = 'BDR'    " v-bind:class="{ 'active': idCategoriaSelected == 'BDR'    }" data-toggle="tab" v-bind:aria-selected="idCategoriaSelected == 'BDR'    ? true : false"> BDRs    ( [[ listaBDR.length    ]] ) </a> </li>
        <li class="nav-item"> <a class="nav-link" @click=" idCategoriaSelected = 'CRIPTO' " v-bind:class="{ 'active': idCategoriaSelected == 'CRIPTO' }" data-toggle="tab" v-bind:aria-selected="idCategoriaSelected == 'CRIPTO' ? true : false"> CRIPTOs ( [[ listaCRIPTO.length ]] ) </a> </li>
        <li class="nav-item"> <a class="nav-link" @click=" idCategoriaSelected = 'RADAR'  " v-bind:class="{ 'active': idCategoriaSelected == 'RADAR'  }" data-toggle="tab" v-bind:aria-selected="idCategoriaSelected == 'RADAR'  ? true : false"> RADAR   ( [[ listaRADAR.length  ]] ) </a> </li>
    </ul>
    <!-- DivTabCateg -->

    <!-- Div Conteudo Pag -->
    <div class="row clearfix">
        <div class="col-lg-12">
            <div class="card border">
                <div class="body">

					<br />
					<br />

                    <!-- Div Table Responsive -->
                    <div class="table-responsive" id="AreaGrid">
                        <table style="font-size: 14px" class="table table-sm table-hover table-condensed table-bo rdered nowrap m-b-0" cellspacing="0" width="100%">
                            <thead>
                                <tr class="thead-dark font-weight-bold">
                                    <th>Codigo</th>
                                    <th>Nome</th>
                                    <th>Cotação</th>
                                    <th>% Dia</th>
                                    <th>% Semana</th>
                                    <th>% Mês</th>
                                    <th>% Ano</th>
                                    <th>% 12 Meses</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="line-height:2.3;" class="text-center" v-for="(item, indx) in TodosAtivos" :key="item[0]">
                                    <td> <a target="_blank" style="text-deco ration:none;" :href="'/finan/acoes/' + item[0]"><span class="text-primary font-weight-bold">[[ item[0] ]]</span></a> </td>
                                    <td>[[ item[1] ]]</td>
                                    <td>R$ [[ idCategoriaSelected == 'CRIPTO' ? formatPriceCripto(parseFloat(item[2])) : formatPrice(item[2]) ]]</td>
                                    <td class="font-weight-bold" :class=" item[3] == 0.0 ? 'text-primary' : item[3] > 0.0 ? 'text-success' : 'text-danger' ">[[ formatPrice(item[3]) ]]%</td>
                                    <td class="font-weight-bold" :class=" item[4] == 0.0 ? 'text-primary' : item[4] > 0.0 ? 'text-success' : 'text-danger' ">[[ formatPrice(item[4]) ]]%</td>
                                    <td class="font-weight-bold" :class=" item[5] == 0.0 ? 'text-primary' : item[5] > 0.0 ? 'text-success' : 'text-danger' ">[[ formatPrice(item[5]) ]]%</td>
                                    <td class="font-weight-bold" :class=" item[6] == 0.0 ? 'text-primary' : item[6] > 0.0 ? 'text-success' : 'text-danger' ">[[ formatPrice(item[6]) ]]%</td>
                                    <td class="font-weight-bold" :class=" item[7] == 0.0 ? 'text-primary' : item[7] > 0.0 ? 'text-success' : 'text-danger' ">[[ formatPrice(item[7]) ]]%</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <!-- Div Table Responsive -->

					<br />
					<br />

                </div>
            </div>
        </div>
    </div>
    <!-- Div Conteudo Pag -->

</div>
`;

var methods_app_valorizacao = {

    formatPrice(value) {
        let val = (value/1).toFixed(2).replace('.', ',')
        return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    },

    formatPriceCripto(value) {
       	return value.toFixed(10).replace('.', ',').replace(/(\d)(?=(\d{3})+\,)/g, "$1.");
    },

    async buscarDadosGrid( idCategoria = '' ) {

        if ( idCategoria == 'ACAO'   ) this.listaACAO   = []
        if ( idCategoria == 'FII'    ) this.listaFII    = []
        if ( idCategoria == 'ETF'    ) this.listaETF    = []
        if ( idCategoria == 'BDR'    ) this.listaBDR    = []
        if ( idCategoria == 'CRIPTO' ) this.listaCRIPTO = []
        if ( idCategoria == 'RADAR'  ) this.listaRADAR  = []

        axios({
          method: 'post',
          url: "/valorizacao/grid",
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify({ Categ: idCategoria  }),
        })
        .then( (response) => {
             let resultado = response.data.data.Resultado;
             if (resultado == "OK") {
                let lista = response.data.data.Lista
                if ( idCategoria == 'ACAO'   ) this.listaACAO   = lista
                if ( idCategoria == 'FII'    ) this.listaFII    = lista
                if ( idCategoria == 'ETF'    ) this.listaETF    = lista
                if ( idCategoria == 'BDR'    ) this.listaBDR    = lista
                if ( idCategoria == 'CRIPTO' ) this.listaCRIPTO = lista
                if ( idCategoria == 'RADAR'  ) this.listaRADAR  = lista
                 return true;
             } else {
                 this.errored = true;
                 let mensagem = response.data.data.Mensagem;
                 console.log('@TamoNaBolsa:Mensagem',mensagem)
             }
        })
        .catch( (error) => {
            this.errored = true
            console.log('@TamoNaBolsa:Error',error)
        })
        .finally( () => {
            this.loading = false
        })

    }, // buscarDadosGrid()

};

var computeds_app_valorizacao = {

    TodosAtivos() {
        if ( this.idCategoriaSelected == 'ACAO'   ) return this.listaACAO
        if ( this.idCategoriaSelected == 'FII'    ) return this.listaFII
        if ( this.idCategoriaSelected == 'ETF'    ) return this.listaETF
        if ( this.idCategoriaSelected == 'BDR'    ) return this.listaBDR
        if ( this.idCategoriaSelected == 'CRIPTO' ) return this.listaCRIPTO
        if ( this.idCategoriaSelected == 'RADAR'  ) return this.listaRADAR
        return []
    },

}

var data_app_valorizacao = {
    loading: true,
    errored: false,
    idCategoriaSelected: 'ACAO',
    listaACAO: [],
    listaFII: [],
    listaETF: [],
    listaBDR: [],
    listaCRIPTO: [],
    listaRADAR: [],
}

var app_valorizacao = new Vue({
    el: '#AppValorizacao',
    delimiters: ['[[',']]'],
    data: data_app_valorizacao,
    template: template_app_valorizacao,
    async created () {
        this.buscarDadosGrid('ACAO')
        this.buscarDadosGrid('FII')
        this.buscarDadosGrid('ETF')
        this.buscarDadosGrid('BDR')
        this.buscarDadosGrid('CRIPTO')
        this.buscarDadosGrid('RADAR')
    },
    methods: methods_app_valorizacao,
    computed: computeds_app_valorizacao,
//    beforeUpdate() { console.time() },
//    updated() { console.log("Time for render ("+this.idCategoriaSelected+"):"); console.timeEnd(); },
});
