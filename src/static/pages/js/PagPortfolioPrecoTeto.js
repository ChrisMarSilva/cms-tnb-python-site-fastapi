
function fAbrirModalPrecoTetoAtivo( urlPadrao, CodAtivo, Preco ) {
    try {

		fLimparAreaAlerta("AreaAlertaModalCadAtivoPrecoTeto"); 
		
		$("#txtCadAtivoTetoCodigo").val( CodAtivo );
		$("#txtCadAtivoTetoPreco").val(  Preco    );

		$('#PopModalDetalheAtivoPrecoTeto').modal({backdrop: 'static'});

		$('#PopModalDetalheAtivoPrecoTeto').on('shown.bs.modal', function() {
			$('#txtCadAtivoPrecoTetoPreco').focus();
		})

    } catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fSalvarDadosAtivoPrecoTeto( urlPadrao ){
	try {
		
		fLimparAreaAlerta("AreaAlertaModalCadAtivoPrecoTeto"); 
		
		var CodAtivo = $("#txtCadAtivoTetoCodigo").val(); 
		var Preco    = $("#txtCadAtivoTetoPreco").val();

		var IdPortfolio = fGetAbaIdPortfolio();
		var TipoInvest  = fGetAbaTipoPortfolio();
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "portfolio/salvarAtivoPrecoTeto",
			data    : { CodAtivo: CodAtivo, Preco: Preco },
			success: function(result) {  
			
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaModalCadAtivoPrecoTeto",TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaModalCadAtivoPrecoTeto",TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					$("#PopModalDetalheAtivoPrecoTeto").modal("hide");					
					// fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					fRecarregarPagina( urlPadrao, IdPortfolio );
				} else {
					fCriarAlerta("AreaAlertaModalCadAtivoPrecoTeto",TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				fCriarAlerta("AreaAlertaModalCadAtivoPrecoTeto",TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText //MSG_ALERTA_ERRO
				return;
			}
		});	
	
	} catch (e) {
		fCriarAlerta("AreaAlertaModalCadAtivoPrecoTeto",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}
