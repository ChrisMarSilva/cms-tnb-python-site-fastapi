
var template_app_fatos = `
<div>
    <div class="row clearfix">
        <div class="col-xl-12 col-lg-12 col-md-12" style="padding-right: 4px; border: 0px solid red;">
            <div class="card border">
                <div class="header">
                    <h2><strong>Fatos Relevantes</strong></h2>
                </div>
                <div class="body" style="margin: 0px; padding: 0px; height: 300px;">
                   
                    <div v-if="loading" class="text-center">
                        <br/> <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> <br/> <br/> <br/>
                    </div>
                    <div v-else>
                        <div v-if="errored" class="text-cente">
                            Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                        </div>
                        <div v-else style="margin: 0px; padding: 0px; padding-top: 10px; padding-bottom: 10px; max-height: 280px; height: 280px; overflow-y:auto; -webkit-overflow-scrolling: touch;">

                            <div v-if="fatos.length <= 0" class="text-center">
                                NENHUM RESULTADO ENCONTRADO
                            </div>
                            <div v-else>
                                <ul style="margin-right: 5px;">
                                    <li style="list-style-type:circle; margin-bottom: 5px;" v-for="fato in TodosFatos">
                                        <a title="Clique aqui para ver o conteúdo oficial" style="font-size: 13px; " :href="fato.link" target="_blank" class="text-dark"> <span class="font-weight-bold">[[ fato.dataFormat ]]</span> - <span class="font-weight-normal">Protocolo: [[ fato.protocolo ]]</span> - <span class="text-primary font-weight-bold">[[ fato.empresa ]]</span> - <span class="font-text-muted weight-normal">[[ fato.assunto ]]</span> </a>
                                    </li>
                                </ul>
                            </div>

                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</div>s
`;

var methods_app_fatos = {

    async buscar_dados() {

        this.loading = true
        this.errored = false
        this.fatos = []

        axios({
          method: 'post',
          url: "/finan/acoes/grid_fatos",
          timeout: 60000,
          responseType: 'json',
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify({ CodAtivo: codigo }),
        })
        .then( (response) => {
             let resultado = response.data.data.Resultado
             if (resultado == "OK") {
                 let lista = response.data.data.Lista
                 this.fatos = lista
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
            // console.log(error.toJSON());
            //            if (error.response) {
            //                console.log('@TamoNaBolsa:Error', error.response.data);
            //                console.log('@TamoNaBolsa:Error', error.response.status);
            //                console.log('@TamoNaBolsa:Error', error.response.headers);
            //            } else if (error.request) {
            //                console.log('@TamoNaBolsa:Error', error.request);
            //            } else {
            //                console.log('@TamoNaBolsa:Error', error.message);
            //            }
            //            console.log('@TamoNaBolsa:Error', error.config);
        })
        .finally( () => {
            this.loading = false
        })

    },

};

var computeds_app_fatos = {

    TodosFatos() {
        // let new_fatos = this.fatos.sort(function(a, b){
        //     var AData = a.data;
        //     var BData = b.data;
        //     if (AData == BData) return 0;
        //     return AData < BData? 1: -1;
        // })
        return this.fatos
    },

};

var data_app_fatos = {
    loading: true,
    errored: false,
    fatos: [],
};

var app_fatos = new Vue({
    el: '#AppFatos',
    delimiters: ['[[',']]'],
    template: template_app_fatos,
    data: data_app_fatos,
    created () { this.buscar_dados('T') },
    methods: methods_app_fatos,
    computed: computeds_app_fatos,
});
