
Vue.use(HighchartsVue.default)

var template_app_dados = `
<div>

    <div v-if="loading" class="text-center">
        <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
    </div>

    <div v-else>

        <div v-if="errored" class="text-cente">
            Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
         </div>

        <div v-else>

            <h6 class="text-center">[[ dados.nomeRazaoSocial ]]</h6>
            <br/>

            <div class="table-responsive">
                <table class="table table-hover m-b-0">
                    <tbody>
                        <tr> <td> <small class="text-muted" style="font-size: 11px;">Nome: <b style="font-size: 13px;">[[ dados.nome ]]</b> </small></td>  </tr>
                        <tr> <td> <small class="text-muted" style="font-size: 11px;">Códigos: </small><a v-for="codigo in dados.codigos" target="_blank" style="text-deco ration:none;" :href="'/finan/acoes/' + codigo"><span class="badge badge-info bg-info text-white font-weight-bold">[[ codigo ]]</span></a></td> </tr>
                        <tr> <td> <small class="text-muted" style="font-size: 11px;">CNPJ: <b style="font-size: 13px;">[[ dados.cnpj ]]</b> </small> </td>  </tr>
                        <tr> <td> <small class="text-muted" style="font-size: 11px;">Setor: <b style="font-size: 13px;">[[ dados.setor ]]</b> </small> </td>  </tr>
                        <tr> <td> <small class="text-muted" style="font-size: 11px;">SubSetor: <b style="font-size: 13px;">[[ dados.subsetor ]]</b> </small> </td> </tr>
                        <tr> <td> <small class="text-muted" style="font-size: 11px;">Segmento: <b style="font-size: 13px;">[[ dados.segmeto ]]</b> </small> </td> </tr>
                        <tr> <td> <small class="text-muted" style="font-size: 11px;">Site: <a target='_blank' style="font-size: 13px;" :href="dados.siteRI"> [[ dados.siteRI ]] </small> </td> </tr>
                        <tr> <td> <small class="text-muted" style="font-size: 11px;">Governança: <b style="font-size: 13px;">[[ dados.governanca ]]</b> </small> </td> </tr>
                        <tr> <td> <small class="text-muted" style="font-size: 11px;">Últ. Balanço: <b style="font-size: 13px;">[[ dados.ultBalanco ]]</b> </small> </td> </tr>
                    </tbody>
                </table>
            </div>

        </div>

    </div>

</div>
`;

var methods_app_dados = {

    async buscar_dados() {

        this.loading = true
        this.errored = false
        this.dados = null

        axios({
          method: 'post',
          url: "/finan/acoes/carregar",
          timeout: 60000, // 60seg // 1Min
          responseType: 'text',
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify({ CodAtivo: codigo }),
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

var data_app_dados = {
    loading: true,
    errored: false,
    dados: null,
};

var app_dados = new Vue({
    el: '#AppDados',
    delimiters: ['[[',']]'],
    template: template_app_dados,
    data: data_app_dados,
    created () {
        this.buscar_dados()
    },
    methods: methods_app_dados,
});
