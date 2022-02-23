
$(document).ready(function () {
	fLimparAreaAlertaPrinc();
});

function iniciarAnimacaoPesquisar() {
	$("#iRefresh").addClass("fa-spin");
	$("#btnPesquisar").addClass("disabled");
}

function finalizarAnimacaoPesquisa() {
	$("#iRefresh").removeClass("fa-spin");
	$("#btnPesquisar").removeClass("disabled");
}

function fLimparGrid() {
	fLimparSomenteGrid( urlPadrao );
}

function fLimparSomenteGrid( urlPadrao ){
	try {

		finalizarAnimacaoPesquisa();

		$("th").addClass('text-center');

		$('#Grid').dataTable().fnClearTable();
		$("#Grid").dataTable({ bDestroy: true }).fnDestroy();

		$('#Grid').DataTable( {
		    data: [],
			oLanguage: fTraduzirGrid(),
			aoColumns: [
				{ bSortable: true, sWidth:  "50px",  targets: 0 },
				{ bSortable: true, sWidth:  "200px", targets: 1 },
				{ bSortable: true, sWidth:  "200px", targets: 2 }
			],
			order: [],
			bFilter: true,
			bInfo: true,
            iDisplayLength: 100,
			bLengthChange: false,
			bSearchable: true,
			bOrderable: true,
			bSortable: true,
			bAutoWidth: false,
			bPaginate: false,
			bOrdering: true,
			orderable: true
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}


function fMontarGrid( urlPadrao, dataSet ){
  try {

        $('#Grid').DataTable( {
          processing: true,
          responsive: true,
          serverSide: false,
		  oLanguage: fTraduzirGrid(),
		  data: dataSet,
          aoColumns: [
				{ bSortable: true, sWidth:  "50px",  targets: 0 },
				{ bSortable: true, sWidth:  "200px", targets: 1 },
				{ bSortable: true, sWidth:  "200px", targets: 2 }
          ],
          createdRow : function(row,data,dataIndex) {
            $('td', row).addClass('text-center');
          }, //createdRow
          initComplete: function( settings, json ) {
			finalizarAnimacaoPesquisa();
          },
			order: [[ 0, "asc" ]],
			bFilter: true,
			bInfo: true,
            iDisplayLength: 100,
			bLengthChange: false,
			bSearchable: true,
			bOrderable: true,
			bSortable: true,
			bAutoWidth: false,
			bPaginate: false,
			bOrdering: true,
			orderable: true
        });

    } catch (e) {
            fLimparGrid( urlPadrao );
            if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}


function fCarregarGrid( urlPadrao ){
  try {

		fLimparAreaAlertaPrinc();
		finalizarAnimacaoPesquisa();
		iniciarAnimacaoPesquisar();

		$('#Grid').dataTable().fnClearTable();
		$("#Grid").dataTable({ bDestroy: true }).fnDestroy();

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "admin/testes/grid",
			// data: { CodAtivo: CodAtivo },
			success: function(result) {

				var resultado = result.data.Resultado;
				var mensagem  = result.data.Mensagem;
				var lista     = result.data.Lista;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
					return;
				} else if (resultado == "FALHA") {
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
					return;
				}else if (resultado == "OK") {
					fMontarGrid( urlPadrao, lista );
				} else{
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
					return;
				}

			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				fLimparGrid( urlPadrao );
				fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
				return false;
			}
		});

    } catch (e) {
		fLimparGrid( urlPadrao );
		  if ( e.description != undefined ){
			fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		  }
    }
}



