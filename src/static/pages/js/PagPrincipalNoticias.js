
var template_app_noticias = `
<div class="row clearfix" style="dis-play: none;">
    <div class="col-lg-12">
        <div class="card border">
            <div class="header" style="padding: 0px; padding-top: 20px; padding-left: 20px;">
                <h2><strong><a href="javascript:void(0);">NOTÍCIAS</a></strong> DO DIA</h2>
            </div>
            <div class="body" style="margin: 0px; padding: 0px; margin-bottom: 20px; ">

                <div id="DivConteudoNoticias" style="max-height: 410px; height: 410px; overflow-y:auto; -webkit-overflow-scrolling: touch; border: 0px solid red;">

                    <div v-if="loading" class="text-center">

                        <div class="contentAnimated"> <div class="animated"> <div class="parent"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="description"></div> <div class="padding"></div> <div class="description"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="title"></div> <div class="padding"></div> <div class="description"></div> <div class="padding"></div> <div class="description"></div> <div class="padding"></div> <div class="title"></div> </div> </div>

                    </div>
                    <div v-else>

                        <div v-if="errored" class="text-cente">
                            Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!
                        </div>
                        <div v-else>

                            <div v-if="noticias.length <= 0" class="text-center">

                                <div class="text-center"><small style="font-size:14px; margin: 20px; " class="font-italic text-muted">Nenhuma Notícia no Dia...</small></div>

                            </div>
                            <div v-else>

                                <ul id="ulAlertaNoticia" style="font-size:12px; padding: 0px; padding-left: 25px; padding-top: 10px; border: 0px solid green; " class="text-muted">
                                    <li v-for="noticia in TodosNoticias" :id="'liAlertaNoticia-'+noticia.id" style="list-style-type:circle; margin-bottom: 5px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 5500px;" >
                                        <a class="text-muted" data-html="true" data-toggle="tooltip" data-placement="bottom" title="Clique aqui para ver o conteúdo completo" :href="noticia.link" target="_blank"> <span>[[ noticia.datahora ]]</span> - <span class="font-weight-bold text-info">[[ noticia.site ]]</span> - <span>#[[ noticia.tipo ]]</span> - <span class="font-weight-bold text-primary">[[ noticia.titulo ]]</span> </a>
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
`;


var app_noticias = new Vue({

    el: '#AppNoticias',

    delimiters: ['[[',']]'],

    template: template_app_noticias,

    data: {
        loading: true,
        errored: false,
        noticias: [],
    },

    methods: {

        async buscarDados() {

            this.loading = true
            this.errored = false
            this.noticias = []

            let logNome = '@TamoNaBolsa - PagPrincipalNoticias'

            // console.log(logNome + ' - INI - ', moment().format())
            console.time(logNome + ' - TEMPO')

            axios({
              method: 'post',
              url: "/principal/carregarNoticias",
              timeout: 60000, // 60seg // 1Min
              responseType: 'text',
              headers: { 'Content-Type': 'application/json' },
            })
            .then( (response) => {
                 let resultado = response.data.data.Resultado
                 if (resultado == "OK") {
                     let lista = response.data.data.Lista
                     this.noticias = lista
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

    },

    computed: {

        TodosNoticias() {
            try {
                let new_noticias = []
                _.forEach(this.noticias, function(value) {
                    new_noticias.push({
                        id: value[0],
                        site: value[1],
                        datahora: moment(value[2], "YYYYMMDDHHmmss").format('DD/MM/YYYY HH:mm'),
                        tipo: value[3],
                        titulo: value[4],
                        link: value[5]
                    })
                })
                return new_noticias
            } catch (error) {
                console.error('@TamoNaBolsa - Error:', error)
            }
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
