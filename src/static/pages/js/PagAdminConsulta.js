
$(document).ready(function() {

	//$(this).attr("title", ":: TnB - Consultas ::");

	$("#MnPrincAluguel").addClass("active open");	

	$("#TxtFiltroTabelas").on("keyup", function(e) {
		if(e.keyCode == 27) 
			$(this).val('');
		var value = $(this).val().toLowerCase();
		$("#DivListaTabelas li").filter(function() {  
			$(this).toggle( $(this).text().toLowerCase().indexOf(value) > -1 );
		});
	});

	$("#TxtFiltroTabelas").on("keypress", function(e) { 
		if(e.which == 13) {
			if ( $("#DivListaTabelas li:visible:first").html().trim() != "" ) {
				AdicionarTabelaNaConsulta( $("#DivListaTabelas li:visible:first").html().trim() ); 
			}
		}
	});
	
	$("#DivListaTabelas li").dblclick(function() { 
		AdicionarTabelaNaConsulta( $(this).html().trim() ); 
	});
	
	$("#DivConsultaSQL").on("keyup", function(e) {
		if(e.keyCode ==  27) {
			//$("#DivConsultaSQL").val('');
			$("#DivResultado").html("");
		}
		if(e.keyCode == 120) {
			ExecutarComandoSQL(); // F9
		}
	});

});

function AdicionarTabelaNaConsulta( NmTabela = "" ) {

	NmTabela = NmTabela.trim();

	if ( NmTabela == "" ) return;

	var ComandoSQLAntigo = $("#DivConsultaSQL").val();
  
	if ( ComandoSQLAntigo.trim() != '' ) 
		ComandoSQLAntigo += '\n';

	var ListaCamposSelect = "";
	var ListaCamposOrderBy = "";

	var lista = DataSetCamposTabela.data.Lista;

	if ( lista.length > 0 ){
		$.each(lista, function (index, value) {
			var TabelaAtual = value[0];
			var CampoAtual  = value[1];
			var KeyPriAtual = value[2];
			if ( NmTabela == TabelaAtual ){
				ListaCamposSelect += (ListaCamposSelect != '' ? ", " : "") + 'T.' + CampoAtual; // + '\n';
				if ( KeyPriAtual == 'PRI' ){
					ListaCamposOrderBy += (ListaCamposOrderBy != '' ? ", " : "") + 'T.' + CampoAtual; 
				} // if ( NmTabela == TabelaAtual  ){
			} // if ( NmTabela == TabelaAtual  ){
		});  //$.each(lista, function (index, value) {
	} // if ( lista.length > 0 ){
		
	if ( ListaCamposSelect.trim() == '' ) 
		ListaCamposSelect += ' T.* ';
		
	if ( ListaCamposOrderBy.trim() == '' ) 
		ListaCamposOrderBy += ' 1 ';

	var ComandoSQLNovo = 'SELECT '+ListaCamposSelect+'\nFROM '+NmTabela+' T \nORDER BY '+ListaCamposOrderBy;

	$("#DivConsultaSQL").val( ComandoSQLNovo + '\n\n' + ComandoSQLAntigo );
	ExecutarComandoSQL(       ComandoSQLNovo                    );

}

function ExecutarComandoSQL( ComandoSQL = ''  ) {
	try { 

		$("#DivResultado").html("");

		if ( ComandoSQL.trim() == "" )  
			ComandoSQL = document.getElementById("DivConsultaSQL").value.substring( document.getElementById("DivConsultaSQL").selectionStart,  document.getElementById("DivConsultaSQL").selectionEnd );
		
		if ( ComandoSQL.trim() == "" )  
			ComandoSQL = $("#DivConsultaSQL").val();

		if ( ComandoSQL.trim() == "" ) 
			return;

		$("#DivResultado").html(
			'<div class="row clearfix"> '+
			'  <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 text-center" style="padding-left: 5px; padding-right: 5px;" > '+
			'    <i class="fa fa-spinner fa-spin fa-5x fa-pulse fa-fw" aria-hidden="true"></i> '+
			'  </div> '+
			'</div> '
		);

		$.ajax({
			cache   : "false",
			dataType: "html",
			async   : true,
			type    : "POST",
			url: "/AdminConsulta/ComandoSQL",
			//url: "./AdminConsulta/ComandoSQL",
			data: { ComandoSQL: ComandoSQL },
			success: function(result) {
				$("#DivResultado").html("");
				$("#DivResultado").html(result);
			},
			error: function(data) {
				 $("#DivResultado").html(MSG_ALERTA_ERRO); 
				return false;
			}
		});	

	} catch (e) {
		if ( e.description != undefined ) $("#DivResultado").html(MSG_ALERTA_ERRO); 
	}
}





