

$(document).ready(function() {
		
	//$(this).attr("title", ":: TnB - Apuração ::");
	$("#MnPrincApuracao").addClass("active open");
	
	fLimparAreaAlertaPrinc();
	fLimparAreaAlertaModalCad();
	fLimparAreaAlertaModalExc();
	
});

async function fAbrirModalGerarPortfolio( urlPadrao ) {
    try {

        $("#PopModalGerarPortfolio").modal({backdrop: "static", keyboard: false});
        $("#iRefreshGerarPortfolio").addClass("fa-spin");

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "principal/gerarportifolio",
			success: function(result) {

				setTimeout(function(){
				    $("#iRefreshGerarPortfolio").removeClass("fa-spin");
				    $('#PopModalGerarPortfolio').modal('hide');
				}, 500);

                fCarregarAnoApuracao( urlPadrao );

			},
			error: function(data) {
				$("#iRefreshGerarPortfolio").removeClass("fa-spin");
				$('#PopModalGerarPortfolio').modal('hide');
				fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
				return;
			}
		});

    } catch (e) {
        $("#iRefreshGerarPortfolio").removeClass("fa-spin");
        $('#PopModalGerarPortfolio').modal('hide');
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fCarregarAnoApuracao( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {
	
			$('#selApuracAno').empty();
			$('#selApuracAno').append('<option value="" selected>Todos</option>');
			
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "apuracao/listaAno",
				success: function(result) {  
				
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista; 
	
					if (resultado == "NOK") {
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return false;
					} else if (resultado == "OK") {	
	
						$.each(lista, function (index, value) {
							$('#selApuracAno').append('<option value="'+ value +'" selected>'+value+'</option>');
						}); 
						fDefinirPadraoSelect('selApuracAno');
	
						return true;
					} else {
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return false;
					}
					
				},
				error: function(data) {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
					return false;
				}
			});
	
			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
		
	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fCarregarConfigApuracao( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {
	
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "apuracao/config",
				success: function(result) {  
				
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var Config    = result.data.Dados;
	
					if (resultado == "NOK") {
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return false;
					} else if (resultado == "OK") {	
						if ( Config.Valor == "S" ) $("#chkApuracVlrSuperior20Mil").attr( "checked", true )
						else 					   $("#chkApuracVlrSuperior20Mil").attr( "checked", false );
						return true;
					} else {
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return false;
					}
					
				},
				error: function(data) {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
					return false;
				}
			});
	
			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
		
	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function iniciarAnimacaoPesquisar() {

	 promise = new Promise( (resolve, reject) => {

		$("#iRefresh").addClass("fa-spin");
		$("#btnApuracPesquisar").addClass("disabled");
		$("#btnApuracLimpar").addClass("disabled");
		
		resolve(true);
		// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
	})
	.then( txt => {
		//console.log('Sucesso: ' + txt);
	})
	.catch( txt => {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	});

}

async function finalizarAnimacaoPesquisa() {

	 promise = new Promise( (resolve, reject) => {

		$("#iRefresh").removeClass("fa-spin");
		$("#btnApuracPesquisar").removeClass("disabled");
		$("#btnApuracLimpar").removeClass("disabled");

		resolve(true);
		// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
	})
	.then( txt => {
		//console.log('Sucesso: ' + txt);
	})
	.catch( txt => {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	});
  
}

async function fLimparGrid( urlPadrao ){	

	 promise = new Promise( (resolve, reject) => {

		$('#selApuracAno').val( "" );	
		$("#chkApuracVlrSuperior20Mil").attr( "checked", false );
		
		fLimparSomenteGrid( urlPadrao );

		resolve(true);
		// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
	})
	.then( txt => {
		//console.log('Sucesso: ' + txt);
	})
	.catch( txt => {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	});

}

async function fLimparSomenteGrid( urlPadrao ){
	try {	

		 promise = new Promise( (resolve, reject) => {
	
			$("th").addClass('text-center');

            fLimparSomenteGridComum( urlPadrao );
            fLimparSomenteGridDayTrade( urlPadrao );
            fLimparSomenteGridFII( urlPadrao );
            fLimparSomenteGridETFComum( urlPadrao );
            fLimparSomenteGridETFDayTrade( urlPadrao );
            fLimparSomenteGridBDRComum( urlPadrao );
            fLimparSomenteGridBDRDayTrade( urlPadrao );
            fLimparSomenteGridCRIPTO( urlPadrao );

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fLimparSomenteGridComum( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			$('#GridComum').dataTable().fnClearTable();
			$("#GridComum").dataTable({ bDestroy: true }).fnDestroy();

			$('#GridComum').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 1 }, //  1-Venda
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 2 }, //  2-Apurado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 3 }, //  3-A Compensar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 4 }, //  4-Resultado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 5 }, //  5-Imposto a Pagar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 6 }, //  6-Imposto Pago
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 7 }, //  7-Imposto Devido
					{ bSortable: false,                    sWidth: "5px",  targets: 8 }  //  8-Acao
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				bSearchable: false,
				bOrderable: false,
				bSortable: false,
				bAutoWidth: false,
				bPaginate: false,
				bOrdering: false
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fLimparSomenteGridDayTrade( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			$('#GridDayTrade').dataTable().fnClearTable();
			$("#GridDayTrade").dataTable({ bDestroy: true }).fnDestroy();

			$('#GridDayTrade').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 1 }, //  1-Venda
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 2 }, //  2-Apurado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 3 }, //  3-A Compensar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 4 }, //  4-Resultado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 5 }, //  5-Imposto a Pagar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 6 }, //  6-Imposto Pago
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 7 }, //  7-Imposto Devido
					{ bSortable: false,                    sWidth: "5px",  targets: 8 }  //  8-Acao
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				bSearchable: false,
				bOrderable: false,
				bSortable: false,
				bAutoWidth: false,
				bPaginate: false,
				bOrdering: false
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fLimparSomenteGridFII( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			$('#GridFII').dataTable().fnClearTable();
			$("#GridFII").dataTable({ bDestroy: true }).fnDestroy();

			$('#GridFII').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 1 }, //  1-Venda
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 2 }, //  2-Apurado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 3 }, //  3-A Compensar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 4 }, //  4-Resultado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 5 }, //  5-Imposto a Pagar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 6 }, //  6-Imposto Pago
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 7 }, //  7-Imposto Devido
					{ bSortable: false,                    sWidth: "5px",  targets: 8 }  //  8-Acao
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				bSearchable: false,
				bOrderable: false,
				bSortable: false,
				bAutoWidth: false,
				bPaginate: false,
				bOrdering: false
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fLimparSomenteGridETFComum( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			$('#GridETFComum').dataTable().fnClearTable();
			$("#GridETFComum").dataTable({ bDestroy: true }).fnDestroy();

			$('#GridETFComum').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 1 }, //  1-Venda
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 2 }, //  2-Apurado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 3 }, //  3-A Compensar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 4 }, //  4-Resultado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 5 }, //  5-Imposto a Pagar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 6 }, //  6-Imposto Pago
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 7 }, //  7-Imposto Devido
					{ bSortable: false,                    sWidth: "5px",  targets: 8 }  //  8-Acao
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				bSearchable: false,
				bOrderable: false,
				bSortable: false,
				bAutoWidth: false,
				bPaginate: false,
				bOrdering: false
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fLimparSomenteGridETFDayTrade( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			$('#GridETFDayTrade').dataTable().fnClearTable();
			$("#GridETFDayTrade").dataTable({ bDestroy: true }).fnDestroy();

			$('#GridETFDayTrade').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 1 }, //  1-Venda
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 2 }, //  2-Apurado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 3 }, //  3-A Compensar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 4 }, //  4-Resultado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 5 }, //  5-Imposto a Pagar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 6 }, //  6-Imposto Pago
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 7 }, //  7-Imposto Devido
					{ bSortable: false,                    sWidth: "5px",  targets: 8 }  //  8-Acao
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				bSearchable: false,
				bOrderable: false,
				bSortable: false,
				bAutoWidth: false,
				bPaginate: false,
				bOrdering: false
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fLimparSomenteGridBDRComum( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			$('#GridBDRComum').dataTable().fnClearTable();
			$("#GridBDRComum").dataTable({ bDestroy: true }).fnDestroy();

			$('#GridBDRComum').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 1 }, //  1-Venda
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 2 }, //  2-Apurado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 3 }, //  3-A Compensar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 4 }, //  4-Resultado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 5 }, //  5-Imposto a Pagar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 6 }, //  6-Imposto Pago
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 7 }, //  7-Imposto Devido
					{ bSortable: false,                    sWidth: "5px",  targets: 8 }  //  8-Acao
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				bSearchable: false,
				bOrderable: false,
				bSortable: false,
				bAutoWidth: false,
				bPaginate: false,
				bOrdering: false
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fLimparSomenteGridBDRDayTrade( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			$('#GridBDRDayTrade').dataTable().fnClearTable();
			$("#GridBDRDayTrade").dataTable({ bDestroy: true }).fnDestroy();

			$('#GridBDRDayTrade').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 1 }, //  1-Venda
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 2 }, //  2-Apurado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 3 }, //  3-A Compensar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 4 }, //  4-Resultado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 5 }, //  5-Imposto a Pagar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 6 }, //  6-Imposto Pago
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 7 }, //  7-Imposto Devido
					{ bSortable: false,                    sWidth: "5px",  targets: 8 }  //  8-Acao
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				bSearchable: false,
				bOrderable: false,
				bSortable: false,
				bAutoWidth: false,
				bPaginate: false,
				bOrdering: false
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fLimparSomenteGridCRIPTO( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			$('#GridCRIPTO').dataTable().fnClearTable();
			$("#GridCRIPTO").dataTable({ bDestroy: true }).fnDestroy();

			$('#GridCRIPTO').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 1 }, //  1-Venda
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 2 }, //  2-Apurado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 3 }, //  3-A Compensar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 4 }, //  4-Resultado
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 5 }, //  5-Imposto a Pagar
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 6 }, //  6-Imposto Pago
					{ bSortable: false, bOrderable: false, sWidth: "50px", targets: 7 }, //  7-Imposto Devido
					{ bSortable: false,                    sWidth: "5px",  targets: 8 }  //  8-Acao
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				bSearchable: false,
				bOrderable: false,
				bSortable: false,
				bAutoWidth: false,
				bPaginate: false,
				bOrdering: false
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fMontarGridComum( urlPadrao, dataSet ){
  try {   

		 promise = new Promise( (resolve, reject) => {

			$('#GridComum').DataTable( {
				processing: true,
				serverSide: false,
				oLanguage: fTraduzirGrid(), 
				data: dataSet,
				aoColumns: [
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 1,   //  1-Venda
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[1]; //  1-Venda
							  return data;
						  } 				 
					  }, //  1-Venda
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 2,   //  2-Apurado
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[2]; //  2-Apurado
							  return data;
						  } 				 
					  }, //  2-Apurado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 3, //  3-A Compensar
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[3]; //  3-A Compensar
							  return data;
						  } 				  
					  }, //  3-A Compensar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 4, //  4-Resultado
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[4]; //  4-Resultado
							  return data;
						  } 				  
					  }, //  4-Resultado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 5, //  5-Imposto a Pagar
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[5]; //  5-Imposto a Pagar
							  return data;
						  } 				  
					  }, // 5-Imposto a Pagar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 6, //  6-Imposto Pago
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[6]; //  6-Imposto Pago
							  return data;
						  } 				  
					  }, //  6-Imposto Pago
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 7, //  7-Imposto Devido
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[7]; //  7-Imposto Devido
							  return data;
						  } 				  
					  },  //  7-Imposto Devido		
					  { bSortable: false, sWidth: "10px", targets: 8,   // 8-Acao
						  render: function ( data, type, row ) {
							  
							  var btnVis = "";
							  var btnDis = '';
							  var btnCor = 'primary';
	  
							  if ( type == "display") {
								  
								  var MesAno       = row[0]; // 0-Mes/Ano
								  var VlrVenda     = row[2]; // 1-Venda
								  
								  if ( VlrVenda == '0,00' ) { btnDis = ' disabled'; btnCor = 'secondary'; }
								  
								  //btnVis += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
								  btnVis += '<a class="btn btn-sm btn-icon btn-icon-mini btn-round btn-simple btn-'+btnCor+btnDis+'"'+btnDis+' style="font-size:9px;" title="Visualizar Vendas do Mês '+MesAno+'" href="javascript:void(0);" onclick="fAbrirModalDetalheVendas( \''+urlPadrao+'\', \'C\', \''+MesAno+'\' );">';
								  btnVis += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
								  btnVis += '</a>';
								  //btnVis += '</div>';
							  }
	  
							  return btnVis;
						   
						  } 
					  } // 8-Acao
			 ],
				createdRow : function(row,data,dataIndex) {
					
					  $('td', row).addClass('text-center');
					  
					  //var MesAno        = data[0]; //  0-Mes/Ano
					  //var VlrVenda      = parseFloat( GetValorDecimal( data[1] ) ); //  1-Venda
					  var VlrApurado    = parseFloat( GetValorDecimal( data[2] ) ); //  2-Apurado
					  var VlrACompensar = parseFloat( GetValorDecimal( data[3] ) ); //  2-A Compensar
					  var VlrResultado  = parseFloat( GetValorDecimal( data[4] ) ); //  4-Resultado
					  var VlrImposto    = parseFloat( GetValorDecimal( data[7] ) ); //  7-Imposto Devido
					  
					  var ColMesAno     = $('td', row).eq(0); //  0-Mes/Ano
					  var ColApurado    = $('td', row).eq(2); //  2-Apurado
					  var ColACompensar = $('td', row).eq(3); //  3-A Compensar
					  var ColResultado  = $('td', row).eq(4); //  4-Resultado
					  var ColImposto    = $('td', row).eq(7); //  7-Imposto Devido
					  
					  if ( VlrApurado > 0){
						  ColMesAno.addClass('text-success font-weight-bold'); 
						  ColApurado.addClass('text-success font-weight-bold'); 
					  }
					  if ( VlrApurado < 0 ){
						  ColMesAno.addClass('text-danger font-weight-bold'); 
						  ColApurado.addClass('text-danger font-weight-bold'); 
					  } 
					  if ( VlrApurado == 0 ){
						  ColMesAno.addClass('text-muted'); //primary 
						  ColApurado.addClass('text-muted'); 
					  } 
					  
					  if ( VlrACompensar  > 0 ) ColACompensar.addClass('text-success font-weight-bold'); 
					  if ( VlrACompensar  < 0 ) ColACompensar.addClass('text-danger font-weight-bold');  
					  if ( VlrACompensar == 0 ) ColACompensar.addClass('text-muted');   //info 
					  
					  if ( VlrResultado  > 0 ) ColResultado.addClass('text-success font-weight-bold'); 
					  if ( VlrResultado  < 0 ) ColResultado.addClass('text-danger font-weight-bold');  
					  if ( VlrResultado == 0 ) ColResultado.addClass('text-muted');  //primary 
					  
					  if ( VlrImposto  > 0)  ColImposto.addClass('text-success font-weight-bold'); 
					  if ( VlrImposto  < 0 ) ColImposto.addClass('text-danger font-weight-bold');  
					  if ( VlrImposto == 0 ) ColImposto.addClass('text-muted'); //primary 
					  
				}, //createdRow
				initComplete: function( settings, json ) {
					  $("#iRefresh").removeClass("fa-spin");
					  $("#btnApuracPesquisar").removeClass("disabled");
					  $("#btnApuracLimpar").removeClass("disabled");
				}, //initComplete
				  order: [],		
				  dom: 'frtBpi',
				  buttons: [  
						{
						   extend:    'excelHtml5',
						   text:      '<i class="fa fa-file-excel-o"></i> Excel',
						   className: 'btn btn-outline-default btn-sm',
						   title: NOME_PROJETO + ' - Apuração das Operações Comuns com Ações',
						   titleAttr: 'Excel',
						   exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] } 
						}, 
						{
						  extend: 'csvHtml5',
						  charset: 'UTF-8',
						  fieldSeparator: ';',
						  titleAttr: 'CSV',
						  text:      '<i class="fa fa-file-o"></i> CSV',
						  className: 'btn btn-outline-default btn-sm',
						  title: NOME_PROJETO + ' - Apuração das Operações Comuns com Ações',
						  bom: true,
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] } 
						},
						{
						  extend: 'pdfHtml5',
						  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						  className: 'btn btn-default btn-sm',
						  titleAttr: 'PDF',
						  title: NOME_PROJETO + ' - Apuração das Operações Comuns com Ações', 
						  pageSize: 'A3',
						  alignment: 'center',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] },
						  footer: true,
						  customize: function (doc) { 
							  doc.defaultStyle.fontSize = 12; 
							  doc.styles.tableHeader.fontSize = 14; 
						  }
						},
						{
						  extend: 'print',
						  text:      '<i class="fa fa-print"></i> Imprimir',
						  title: NOME_PROJETO + ' - Apuração das Operações Comuns com Ações',
						  titleAttr: 'Imprimir',
						  className: 'btn btn-default btn-sm',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						}
				  ],
				  bFilter: false,
				  bInfo: false,
				  bLengthChange: false,
				  bSearchable: false,
				  bOrderable: false,
				  bSortable: false,
				  bAutoWidth: false,
				  bPaginate: false,
				  bOrdering: false
			  })
			 .on( 'error.dt', function ( e, settings, techNote, message ) {
				  finalizarAnimacaoPesquisa();
				  return true;
				} );
			 
			  
			  $( document ).ajaxError(function( event, request, settings, thrownError ) {
				  finalizarAnimacaoPesquisa();
			  });

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

    } catch (e) {
		fLimparSomenteGrid( urlPadrao );
		finalizarAnimacaoPesquisa();
      if ( e.description != undefined ){
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      }
    }
}

async function fMontarGridDayTrade( urlPadrao, dataSet ){
  try {   

		 promise = new Promise( (resolve, reject) => {
  
			$('#GridDayTrade').DataTable( {
				processing: true,
				serverSide: false,
				oLanguage: fTraduzirGrid(), 
				data: dataSet,
				aoColumns: [
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 1,   //  1-Venda
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[1]; //  1-Venda
							  return data;
						  } 				 
					  }, //  1-Venda
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 2,   //  2-Apurado
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[2]; //  2-Apurado
							  return data;
						  } 				 
					  }, //  2-Apurado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 3, //  3-A Compensar
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[3]; //  3-A Compensar
							  return data;
						  } 				  
					  }, //  3-A Compensar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 4, //  4-Resultado
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[4]; //  4-Resultado
							  return data;
						  } 				  
					  }, //  4-Resultado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 5, //  5-Imposto a Pagar
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[5]; //  5-Imposto a Pagar
							  return data;
						  } 				  
					  }, // 5-Imposto a Pagar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 6, //  6-Imposto Pago
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[6]; //  6-Imposto Pago
							  return data;
						  } 				  
					  }, //  6-Imposto Pago
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 7, //  7-Imposto Devido
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[7]; //  7-Imposto Devido
							  return data;
						  } 				  
					  },  //  7-Imposto Devido				
					  { bSortable: false, sWidth: "10px", targets: 8,   // 8-Acao
						  render: function ( data, type, row ) {
							  
							  var btnVis = "";
							  var btnDis = '';
							  var btnCor = 'primary';
	  
							  if ( type == "display") {
								  
								  var MesAno       = row[0]; // 0-Mes/Ano
								  var VlrVenda     = row[2]; // 1-Venda
								  
								  if ( VlrVenda == '0,00' ) { btnDis = ' disabled'; btnCor = 'secondary'; }
								  
								  //btnVis += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
								  btnVis += '<a class="btn btn-sm btn-icon btn-icon-mini btn-round btn-simple btn-'+btnCor+btnDis+'"'+btnDis+' style="font-size:9px;" title="Visualizar Vendas do Mês '+MesAno+'" href="javascript:void(0);" onclick="fAbrirModalDetalheVendas( \''+urlPadrao+'\', \'D\', \''+MesAno+'\' );">';
								  btnVis += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
								  btnVis += '</a>';
								  //btnVis += '</div>';
							  }
	  
							  return btnVis;
						   
						  } 
					  } // 8-Acao
				],
				createdRow : function(row,data,dataIndex) {
					
					  $('td', row).addClass('text-center');
					  
					  //var MesAno        = data[0]; //  0-Mes/Ano
					  var VlrVenda      = parseFloat( GetValorDecimal( data[1] ) ); //  1-Venda
					  var VlrApurado    = parseFloat( GetValorDecimal( data[2] ) ); //  2-Apurado
					  var VlrACompensar = parseFloat( GetValorDecimal( data[3] ) ); //  2-A Compensar
					  var VlrResultado  = parseFloat( GetValorDecimal( data[4] ) ); //  4-Resultado
					  var VlrImposto    = parseFloat( GetValorDecimal( data[7] ) ); //  7-Imposto Devido
					  
					  var ColMesAno     = $('td', row).eq(0); //  0-Mes/Ano
					  var ColApurado    = $('td', row).eq(2); //  2-Apurado
					  var ColACompensar = $('td', row).eq(3); //  3-A Compensar
					  var ColResultado  = $('td', row).eq(4); //  4-Resultado
					  var ColImposto    = $('td', row).eq(7); //  7-Imposto Devido
					  
					  if ( VlrApurado > 0){
						  ColMesAno.addClass('text-success font-weight-bold'); 
						  ColApurado.addClass('text-success font-weight-bold'); 
					  }
					  if ( VlrApurado < 0 ){
						  ColMesAno.addClass('text-danger font-weight-bold'); 
						  ColApurado.addClass('text-danger font-weight-bold'); 
					  } 
					  if ( VlrApurado == 0 ){
						  ColMesAno.addClass('text-muted'); //primary 
						  ColApurado.addClass('text-muted'); 
					  } 
					  
					  if ( VlrACompensar  > 0 ) ColACompensar.addClass('text-success font-weight-bold'); 
					  if ( VlrACompensar  < 0 ) ColACompensar.addClass('text-danger font-weight-bold');  
					  if ( VlrACompensar == 0 ) ColACompensar.addClass('text-muted');   //info 
					  
					  if ( VlrResultado  > 0 ) ColResultado.addClass('text-success font-weight-bold'); 
					  if ( VlrResultado  < 0 ) ColResultado.addClass('text-danger font-weight-bold');  
					  if ( VlrResultado == 0 ) ColResultado.addClass('text-muted');  //primary 
					  
					  if ( VlrImposto  > 0 ) ColImposto.addClass('text-success font-weight-bold'); 
					  if ( VlrImposto  < 0 ) ColImposto.addClass('text-danger font-weight-bold');  
					  if ( VlrImposto == 0 ) ColImposto.addClass('text-muted'); //primary 
					  
				}, //createdRow
				initComplete: function( settings, json ) {
					  $("#iRefresh").removeClass("fa-spin");
					  $("#btnApuracPesquisar").removeClass("disabled");
					  $("#btnApuracLimpar").removeClass("disabled");
				}, //initComplete
				  order: [],
				  dom: 'frtBpi',
				  buttons: [  
						{
						   extend:    'excelHtml5',
						   text:      '<i class="fa fa-file-excel-o"></i> Excel',
						   className: 'btn btn-outline-default btn-sm',
						   title: NOME_PROJETO + ' - Apuração das Operações Day Trade com Ações',
						   titleAttr: 'Excel',
						   exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] } 
						}, 
						{
						  extend: 'csvHtml5',
						  charset: 'UTF-8',
						  fieldSeparator: ';',
						  titleAttr: 'CSV',
						  text:      '<i class="fa fa-file-o"></i> CSV',
						  className: 'btn btn-outline-default btn-sm',
						  title: NOME_PROJETO + ' - Apuração das Operações Day Trade com Ações',
						  bom: true,
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] } 
						},
						{
						  extend: 'pdfHtml5',
						  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						  className: 'btn btn-default btn-sm',
						  titleAttr: 'PDF',
						  title: NOME_PROJETO + ' - Apuração das Operações Day Trade com Ações', 
						  pageSize: 'A3',
						  alignment: 'center',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] },
						  footer: true,
						  customize: function (doc) { 
							  doc.defaultStyle.fontSize = 12; 
							  doc.styles.tableHeader.fontSize = 14; 
						  }
						},
						{
						  extend: 'print',
						  text:      '<i class="fa fa-print"></i> Imprimir',
						  title: NOME_PROJETO + ' - Apuração das Operações Day Trade com Ações',
						  titleAttr: 'Imprimir',
						  className: 'btn btn-default btn-sm',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						}
				  ],
				  bFilter: false,
				  bInfo: false,
				  bLengthChange: false,
				  bSearchable: false,
				  bOrderable: false,
				  bSortable: false,
				  bAutoWidth: false,
				  bPaginate: false,
				  bOrdering: false
			  })
			 .on( 'error.dt', function ( e, settings, techNote, message ) {
				  finalizarAnimacaoPesquisa();
				  return true;
				} );
			 
			  
			  $( document ).ajaxError(function( event, request, settings, thrownError ) {
				  finalizarAnimacaoPesquisa();
			  });

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

    } catch (e) {
		fLimparSomenteGrid( urlPadrao );
		finalizarAnimacaoPesquisa();
      if ( e.description != undefined ){
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      }
    }
}

async function fMontarGridFII( urlPadrao, dataSet ){
  try {   
		
		 promise = new Promise( (resolve, reject) => {

			$('#GridFII').DataTable( {
				processing: true,
				serverSide: false,
				oLanguage: fTraduzirGrid(), 
				data: dataSet,
				aoColumns: [
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 1,   //  1-Venda
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[1]; //  1-Venda
							  return data;
						  } 				 
					  }, //  1-Venda
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 2,   //  2-Apurado
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[2]; //  2-Apurado
							  return data;
						  } 				 
					  }, //  2-Apurado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 3, //  3-A Compensar
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[3]; //  3-A Compensar
							  return data;
						  } 				  
					  }, //  3-A Compensar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 4, //  4-Resultado
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[4]; //  4-Resultado
							  return data;
						  } 				  
					  }, //  4-Resultado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 5, //  5-Imposto a Pagar
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[5]; //  5-Imposto a Pagar
							  return data;
						  } 				  
					  }, // 5-Imposto a Pagar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 6, //  6-Imposto Pago
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[6]; //  6-Imposto Pago
							  return data;
						  } 				  
					  }, //  6-Imposto Pago
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 7, //  7-Imposto Devido
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[7]; //  7-Imposto Devido
							  return data;
						  } 				  
					  },  //  7-Imposto Devido					
					  { bSortable: false, sWidth: "10px", targets: 8,   // 8-Acao
						  render: function ( data, type, row ) {
							  
							  var btnVis = "";
							  var btnDis = '';
							  var btnCor = 'primary';
	  
							  if ( type == "display") {
								  
								  var MesAno       = row[0]; // 0-Mes/Ano
								  var VlrVenda     = row[2]; // 1-Venda
								  
								  if ( VlrVenda == '0,00' ) { btnDis = ' disabled'; btnCor = 'secondary'; }
								  
								  //btnVis += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
								  btnVis += '<a class="btn btn-sm btn-icon btn-icon-mini btn-round btn-simple btn-'+btnCor+btnDis+'"'+btnDis+' style="font-size:9px;" title="Visualizar Vendas do Mês '+MesAno+'" href="javascript:void(0);" onclick="fAbrirModalDetalheVendas( \''+urlPadrao+'\', \'F\', \''+MesAno+'\' );">';
								  btnVis += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
								  btnVis += '</a>';
								  //btnVis += '</div>';
							  }
	  
							  return btnVis;
						   
						  } 
					  } // 8-Acao
				],
				createdRow : function(row,data,dataIndex) {
					
					  $('td', row).addClass('text-center');
					  
					  //var MesAno        = data[0]; //  0-Mes/Ano
					  var VlrVenda      = parseFloat( GetValorDecimal( data[1] ) ); //  1-Venda
					  var VlrApurado    = parseFloat( GetValorDecimal( data[2] ) ); //  2-Apurado
					  var VlrACompensar = parseFloat( GetValorDecimal( data[3] ) ); //  2-A Compensar
					  var VlrResultado  = parseFloat( GetValorDecimal( data[4] ) ); //  4-Resultado
					  var VlrImposto    = parseFloat( GetValorDecimal( data[7] ) ); // 7-Imposto Devido
					  
					  var ColMesAno     = $('td', row).eq(0); //  0-Mes/Ano
					  var ColApurado    = $('td', row).eq(2); //  2-Apurado
					  var ColACompensar = $('td', row).eq(3); //  3-A Compensar
					  var ColResultado  = $('td', row).eq(4); //  4-Resultado
					  var ColImposto    = $('td', row).eq(7); //  7-Imposto Devido
					  
					  if ( VlrApurado > 0){
						  ColMesAno.addClass('text-success font-weight-bold'); 
						  ColApurado.addClass('text-success font-weight-bold'); 
					  }
					  if ( VlrApurado < 0 ){
						  ColMesAno.addClass('text-danger font-weight-bold'); 
						  ColApurado.addClass('text-danger font-weight-bold'); 
					  } 
					  if ( VlrApurado == 0 ){
						  ColMesAno.addClass('text-muted'); //primary 
						  ColApurado.addClass('text-muted'); 
					  } 
					  
					  if ( VlrACompensar  > 0 ) ColACompensar.addClass('text-success font-weight-bold'); 
					  if ( VlrACompensar  < 0 ) ColACompensar.addClass('text-danger font-weight-bold');  
					  if ( VlrACompensar == 0 ) ColACompensar.addClass('text-muted');   //info 
					  
					  if ( VlrResultado  > 0 ) ColResultado.addClass('text-success font-weight-bold'); 
					  if ( VlrResultado  < 0 ) ColResultado.addClass('text-danger font-weight-bold');  
					  if ( VlrResultado == 0 ) ColResultado.addClass('text-muted');  //primary 
					  
					  if ( VlrImposto  > 0 ) ColImposto.addClass('text-success font-weight-bold'); 
					  if ( VlrImposto  < 0 ) ColImposto.addClass('text-danger font-weight-bold');  
					  if ( VlrImposto == 0 ) ColImposto.addClass('text-muted'); //primary 
					  
				}, //createdRow
				initComplete: function( settings, json ) {
					  $("#iRefresh").removeClass("fa-spin");
					  $("#btnApuracPesquisar").removeClass("disabled");
					  $("#btnApuracLimpar").removeClass("disabled");
				}, //initComplete
				  order: [],
				  dom: 'frtBpi',
				  buttons: [  
						{
						   extend:    'excelHtml5',
						   text:      '<i class="fa fa-file-excel-o"></i> Excel',
						   className: 'btn btn-outline-default btn-sm',
						   title: NOME_PROJETO + ' - Apuração das Operações com FIIs',
						   titleAttr: 'Excel',
						   exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] } 
						}, 
						{
						  extend: 'csvHtml5',
						  charset: 'UTF-8',
						  fieldSeparator: ';',
						  titleAttr: 'CSV',
						  text:      '<i class="fa fa-file-o"></i> CSV',
						  className: 'btn btn-outline-default btn-sm',
						  title: NOME_PROJETO + ' - Apuração das Operações com FIIs',
						  bom: true,
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] } 
						},
						{
						  extend: 'pdfHtml5',
						  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						  className: 'btn btn-default btn-sm',
						  titleAttr: 'PDF',
						  title: NOME_PROJETO + ' - Apuração das Operações com FIIs', 
						  pageSize: 'A3',
						  alignment: 'center',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] },
						  footer: true,
						  customize: function (doc) { 
							  doc.defaultStyle.fontSize = 12; 
							  doc.styles.tableHeader.fontSize = 14; 
						  }
						},
						{
						  extend: 'print',
						  text:      '<i class="fa fa-print"></i> Imprimir',
						  title: NOME_PROJETO + ' - Apuração das Operações com FIIs',
						  titleAttr: 'Imprimir',
						  className: 'btn btn-default btn-sm',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						}
				  ],
				  bFilter: false,
				  bInfo: false,
				  bLengthChange: false,
				  bSearchable: false,
				  bOrderable: false,
				  bSortable: false,
				  bAutoWidth: false,
				  bPaginate: false,
				  bOrdering: false
			  })
			 .on( 'error.dt', function ( e, settings, techNote, message ) {
				  finalizarAnimacaoPesquisa();
				  return true;
				} );
			 
			  
			  $( document ).ajaxError(function( event, request, settings, thrownError ) {
				  finalizarAnimacaoPesquisa();
			  });

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

    } catch (e) {
		fLimparSomenteGrid( urlPadrao );
		finalizarAnimacaoPesquisa();
      if ( e.description != undefined ){
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      }
    }
}

async function fMontarGridETFComum( urlPadrao, dataSet ){
  try {   
		
		 promise = new Promise( (resolve, reject) => {

			$('#GridETFComum').DataTable( {
				processing: true,
				serverSide: false,
				oLanguage: fTraduzirGrid(), 
				data: dataSet,
				aoColumns: [
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 1,   //  1-Venda
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[1]; //  1-Venda
							  return data;
						  } 				 
					  }, //  1-Venda
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 2,   //  2-Apurado
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[2]; //  2-Apurado
							  return data;
						  } 				 
					  }, //  2-Apurado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 3, //  3-A Compensar
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[3]; //  3-A Compensar
							  return data;
						  } 				  
					  }, //  3-A Compensar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 4, //  4-Resultado
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[4]; //  4-Resultado
							  return data;
						  } 				  
					  }, //  4-Resultado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 5, //  5-Imposto a Pagar
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[5]; //  5-Imposto a Pagar
							  return data;
						  } 				  
					  }, // 5-Imposto a Pagar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 6, //  6-Imposto Pago
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[6]; //  6-Imposto Pago
							  return data;
						  } 				  
					  }, //  6-Imposto Pago
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 7, //  7-Imposto Devido
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[7]; //  7-Imposto Devido
							  return data;
						  } 				  
					  },  //  7-Imposto Devido					
					  { bSortable: false, sWidth: "10px", targets: 8,   // 8-Acao
						  render: function ( data, type, row ) {
							  
							  var btnVis = "";
							  var btnDis = '';
							  var btnCor = 'primary';
	  
							  if ( type == "display") {
								  
								  var MesAno       = row[0]; // 0-Mes/Ano
								  var VlrVenda     = row[2]; // 1-Venda
								  
								  if ( VlrVenda == '0,00' ) { btnDis = ' disabled'; btnCor = 'secondary'; }
								  
								  //btnVis += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
								  btnVis += '<a class="btn btn-sm btn-icon btn-icon-mini btn-round btn-simple btn-'+btnCor+btnDis+'"'+btnDis+' style="font-size:9px;" title="Visualizar Vendas do Mês '+MesAno+'" href="javascript:void(0);" onclick="fAbrirModalDetalheVendas( \''+urlPadrao+'\', \'E\', \''+MesAno+'\' );">';
								  btnVis += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
								  btnVis += '</a>';
								  //btnVis += '</div>';
							  }
	  
							  return btnVis;
						   
						  } 
					  } // 8-Acao
				],
				createdRow : function(row,data,dataIndex) {
					
					  $('td', row).addClass('text-center');
					  
					  //var MesAno        = data[0]; //  0-Mes/Ano
					  var VlrVenda      = parseFloat( GetValorDecimal( data[1] ) ); //  1-Venda
					  var VlrApurado    = parseFloat( GetValorDecimal( data[2] ) ); //  2-Apurado
					  var VlrACompensar = parseFloat( GetValorDecimal( data[3] ) ); //  2-A Compensar
					  var VlrResultado  = parseFloat( GetValorDecimal( data[4] ) ); //  4-Resultado
					  var VlrImposto    = parseFloat( GetValorDecimal( data[7] ) ); // 7-Imposto Devido
					  
					  var ColMesAno     = $('td', row).eq(0); //  0-Mes/Ano
					  var ColApurado    = $('td', row).eq(2); //  2-Apurado
					  var ColACompensar = $('td', row).eq(3); //  3-A Compensar
					  var ColResultado  = $('td', row).eq(4); //  4-Resultado
					  var ColImposto    = $('td', row).eq(7); //  7-Imposto Devido
					  
					  if ( VlrApurado > 0){
						  ColMesAno.addClass('text-success font-weight-bold'); 
						  ColApurado.addClass('text-success font-weight-bold'); 
					  }
					  if ( VlrApurado < 0 ){
						  ColMesAno.addClass('text-danger font-weight-bold'); 
						  ColApurado.addClass('text-danger font-weight-bold'); 
					  } 
					  if ( VlrApurado == 0 ){
						  ColMesAno.addClass('text-muted'); //primary 
						  ColApurado.addClass('text-muted'); 
					  } 
					  
					  if ( VlrACompensar  > 0 ) ColACompensar.addClass('text-success font-weight-bold'); 
					  if ( VlrACompensar  < 0 ) ColACompensar.addClass('text-danger font-weight-bold');  
					  if ( VlrACompensar == 0 ) ColACompensar.addClass('text-muted');   //info 
					  
					  if ( VlrResultado  > 0 ) ColResultado.addClass('text-success font-weight-bold'); 
					  if ( VlrResultado  < 0 ) ColResultado.addClass('text-danger font-weight-bold');  
					  if ( VlrResultado == 0 ) ColResultado.addClass('text-muted');  //primary 
					  
					  if ( VlrImposto  > 0 ) ColImposto.addClass('text-success font-weight-bold'); 
					  if ( VlrImposto  < 0 ) ColImposto.addClass('text-danger font-weight-bold');  
					  if ( VlrImposto == 0 ) ColImposto.addClass('text-muted'); //primary 
					  
				}, //createdRow
				initComplete: function( settings, json ) {
					  $("#iRefresh").removeClass("fa-spin");
					  $("#btnApuracPesquisar").removeClass("disabled");
					  $("#btnApuracLimpar").removeClass("disabled");
				}, //initComplete
				  order: [],
				  dom: 'frtBpi',
				  buttons: [  
						{
						   extend:    'excelHtml5',
						   text:      '<i class="fa fa-file-excel-o"></i> Excel',
						   className: 'btn btn-outline-default btn-sm',
						   title: NOME_PROJETO + ' - Apuração das Operações Comum com ETFs', 
						   titleAttr: 'Excel',
						   exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] } 
						}, 
						{
						  extend: 'csvHtml5',
						  charset: 'UTF-8',
						  fieldSeparator: ';',
						  titleAttr: 'CSV',
						  text:      '<i class="fa fa-file-o"></i> CSV',
						  className: 'btn btn-outline-default btn-sm',
						  title: NOME_PROJETO + ' - Apuração das Operações Comum com ETFs', 
						  bom: true,
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] } 
						},
						{
						  extend: 'pdfHtml5',
						  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						  className: 'btn btn-default btn-sm',
						  titleAttr: 'PDF',
						  title: NOME_PROJETO + ' - Apuração das Operações Comum com ETFs', 
						  pageSize: 'A3',
						  alignment: 'center',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] },
						  footer: true,
						  customize: function (doc) { 
							  doc.defaultStyle.fontSize = 12; 
							  doc.styles.tableHeader.fontSize = 14; 
						  }
						},
						{
						  extend: 'print',
						  text:      '<i class="fa fa-print"></i> Imprimir',
						  title: NOME_PROJETO + ' - Apuração das Operações Comum com ETFs', 
						  titleAttr: 'Imprimir',
						  className: 'btn btn-default btn-sm',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						}
				  ],
				  bFilter: false,
				  bInfo: false,
				  bLengthChange: false,
				  bSearchable: false,
				  bOrderable: false,
				  bSortable: false,
				  bAutoWidth: false,
				  bPaginate: false,
				  bOrdering: false
			  })
			 .on( 'error.dt', function ( e, settings, techNote, message ) {
				  finalizarAnimacaoPesquisa();
				  return true;
				} );
			 
			  
			  $( document ).ajaxError(function( event, request, settings, thrownError ) {
				  finalizarAnimacaoPesquisa();
			  });

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

    } catch (e) {
		fLimparSomenteGrid( urlPadrao );
		finalizarAnimacaoPesquisa();
      if ( e.description != undefined ){
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      }
    }
}

async function fMontarGridETFDayTrade( urlPadrao, dataSet ){
  try {   
		
		 promise = new Promise( (resolve, reject) => {

			$('#GridETFDayTrade').DataTable( {
				processing: true,
				serverSide: false,
				oLanguage: fTraduzirGrid(), 
				data: dataSet,
				aoColumns: [
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 1,   //  1-Venda
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[1]; //  1-Venda
							  return data;
						  } 				 
					  }, //  1-Venda
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 2,   //  2-Apurado
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[2]; //  2-Apurado
							  return data;
						  } 				 
					  }, //  2-Apurado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 3, //  3-A Compensar
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[3]; //  3-A Compensar
							  return data;
						  } 				  
					  }, //  3-A Compensar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 4, //  4-Resultado
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[4]; //  4-Resultado
							  return data;
						  } 				  
					  }, //  4-Resultado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 5, //  5-Imposto a Pagar
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[5]; //  5-Imposto a Pagar
							  return data;
						  } 				  
					  }, // 5-Imposto a Pagar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 6, //  6-Imposto Pago
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[6]; //  6-Imposto Pago
							  return data;
						  } 				  
					  }, //  6-Imposto Pago
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 7, //  7-Imposto Devido
						  render: function ( data, type, row ) { 
							  if ( type == "display") return "R$ " + row[7]; //  7-Imposto Devido
							  return data;
						  } 				  
					  },  //  7-Imposto Devido					
					  { bSortable: false, sWidth: "10px", targets: 8,   // 8-Acao
						  render: function ( data, type, row ) {
							  
							  var btnVis = "";
							  var btnDis = '';
							  var btnCor = 'primary';
	  
							  if ( type == "display") {
								  
								  var MesAno       = row[0]; // 0-Mes/Ano
								  var VlrVenda     = row[2]; // 1-Venda
								  
								  if ( VlrVenda == '0,00' ) { btnDis = ' disabled'; btnCor = 'secondary'; }
								  
								  //btnVis += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
								  btnVis += '<a class="btn btn-sm btn-icon btn-icon-mini btn-round btn-simple btn-'+btnCor+btnDis+'"'+btnDis+' style="font-size:9px;" title="Visualizar Vendas do Mês '+MesAno+'" href="javascript:void(0);" onclick="fAbrirModalDetalheVendas( \''+urlPadrao+'\', \'G\', \''+MesAno+'\' );">';
								  btnVis += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
								  btnVis += '</a>';
								  //btnVis += '</div>';
							  }
	  
							  return btnVis;
						   
						  } 
					  } // 8-Acao
				],
				createdRow : function(row,data,dataIndex) {
					
					  $('td', row).addClass('text-center');
					  
					  //var MesAno        = data[0]; //  0-Mes/Ano
					  var VlrVenda      = parseFloat( GetValorDecimal( data[1] ) ); //  1-Venda
					  var VlrApurado    = parseFloat( GetValorDecimal( data[2] ) ); //  2-Apurado
					  var VlrACompensar = parseFloat( GetValorDecimal( data[3] ) ); //  2-A Compensar
					  var VlrResultado  = parseFloat( GetValorDecimal( data[4] ) ); //  4-Resultado
					  var VlrImposto    = parseFloat( GetValorDecimal( data[7] ) ); // 7-Imposto Devido
					  
					  var ColMesAno     = $('td', row).eq(0); //  0-Mes/Ano
					  var ColApurado    = $('td', row).eq(2); //  2-Apurado
					  var ColACompensar = $('td', row).eq(3); //  3-A Compensar
					  var ColResultado  = $('td', row).eq(4); //  4-Resultado
					  var ColImposto    = $('td', row).eq(7); //  7-Imposto Devido
					  
					  if ( VlrApurado > 0){
						  ColMesAno.addClass('text-success font-weight-bold'); 
						  ColApurado.addClass('text-success font-weight-bold'); 
					  }
					  if ( VlrApurado < 0 ){
						  ColMesAno.addClass('text-danger font-weight-bold'); 
						  ColApurado.addClass('text-danger font-weight-bold'); 
					  } 
					  if ( VlrApurado == 0 ){
						  ColMesAno.addClass('text-muted'); //primary 
						  ColApurado.addClass('text-muted'); 
					  } 
					  
					  if ( VlrACompensar  > 0 ) ColACompensar.addClass('text-success font-weight-bold'); 
					  if ( VlrACompensar  < 0 ) ColACompensar.addClass('text-danger font-weight-bold');  
					  if ( VlrACompensar == 0 ) ColACompensar.addClass('text-muted');   //info 
					  
					  if ( VlrResultado  > 0 ) ColResultado.addClass('text-success font-weight-bold'); 
					  if ( VlrResultado  < 0 ) ColResultado.addClass('text-danger font-weight-bold');  
					  if ( VlrResultado == 0 ) ColResultado.addClass('text-muted');  //primary 
					  
					  if ( VlrImposto  > 0 ) ColImposto.addClass('text-success font-weight-bold'); 
					  if ( VlrImposto  < 0 ) ColImposto.addClass('text-danger font-weight-bold');  
					  if ( VlrImposto == 0 ) ColImposto.addClass('text-muted'); //primary 
					  
				}, //createdRow
				initComplete: function( settings, json ) {
					  $("#iRefresh").removeClass("fa-spin");
					  $("#btnApuracPesquisar").removeClass("disabled");
					  $("#btnApuracLimpar").removeClass("disabled");
				}, //initComplete
				  order: [],
				  dom: 'frtBpi',
				  buttons: [  
						{
						   extend:    'excelHtml5',
						   text:      '<i class="fa fa-file-excel-o"></i> Excel',
						   className: 'btn btn-outline-default btn-sm',
						   title: NOME_PROJETO + ' - Apuração das Operações Day Trade com ETFs', 
						   titleAttr: 'Excel',
						   exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] } 
						}, 
						{
						  extend: 'csvHtml5',
						  charset: 'UTF-8',
						  fieldSeparator: ';',
						  titleAttr: 'CSV',
						  text:      '<i class="fa fa-file-o"></i> CSV',
						  className: 'btn btn-outline-default btn-sm',
						  title: NOME_PROJETO + ' - Apuração das Operações Day Trade com ETFs', 
						  bom: true,
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] } 
						},
						{
						  extend: 'pdfHtml5',
						  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						  className: 'btn btn-default btn-sm',
						  titleAttr: 'PDF',
						  title: NOME_PROJETO + ' - Apuração das Operações Day Trade com ETFs', 
						  pageSize: 'A3',
						  alignment: 'center',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] },
						  footer: true,
						  customize: function (doc) { 
							  doc.defaultStyle.fontSize = 12; 
							  doc.styles.tableHeader.fontSize = 14; 
						  }
						},
						{
						  extend: 'print',
						  text:      '<i class="fa fa-print"></i> Imprimir',
						  title: NOME_PROJETO + ' - Apuração das Operações Day Trade com ETFs', 
						  titleAttr: 'Imprimir',
						  className: 'btn btn-default btn-sm',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						}
				  ],
				  bFilter: false,
				  bInfo: false,
				  bLengthChange: false,
				  bSearchable: false,
				  bOrderable: false,
				  bSortable: false,
				  bAutoWidth: false,
				  bPaginate: false,
				  bOrdering: false
			  })
			 .on( 'error.dt', function ( e, settings, techNote, message ) {
				  finalizarAnimacaoPesquisa();
				  return true;
				} );
			 
			  
			  $( document ).ajaxError(function( event, request, settings, thrownError ) {
				  finalizarAnimacaoPesquisa();
			  });

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

    } catch (e) {
		fLimparSomenteGrid( urlPadrao );
		finalizarAnimacaoPesquisa();
      if ( e.description != undefined ){
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      }
    }
}

async function fMontarGridBDRComum( urlPadrao, dataSet ){
  try {

		 promise = new Promise( (resolve, reject) => {

			$('#GridBDRComum').DataTable( {
				processing: true,
				serverSide: false,
				oLanguage: fTraduzirGrid(),
				data: dataSet,
				aoColumns: [
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 1,   //  1-Venda
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[1]; //  1-Venda
							  return data;
						  }
					  }, //  1-Venda
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 2,   //  2-Apurado
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[2]; //  2-Apurado
							  return data;
						  }
					  }, //  2-Apurado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 3, //  3-A Compensar
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[3]; //  3-A Compensar
							  return data;
						  }
					  }, //  3-A Compensar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 4, //  4-Resultado
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[4]; //  4-Resultado
							  return data;
						  }
					  }, //  4-Resultado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 5, //  5-Imposto a Pagar
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[5]; //  5-Imposto a Pagar
							  return data;
						  }
					  }, // 5-Imposto a Pagar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 6, //  6-Imposto Pago
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[6]; //  6-Imposto Pago
							  return data;
						  }
					  }, //  6-Imposto Pago
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 7, //  7-Imposto Devido
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[7]; //  7-Imposto Devido
							  return data;
						  }
					  },  //  7-Imposto Devido
					  { bSortable: false, sWidth: "10px", targets: 8,   // 8-Acao
						  render: function ( data, type, row ) {

							  var btnVis = "";
							  var btnDis = '';
							  var btnCor = 'primary';

							  if ( type == "display") {

								  var MesAno       = row[0]; // 0-Mes/Ano
								  var VlrVenda     = row[2]; // 1-Venda

								  if ( VlrVenda == '0,00' ) { btnDis = ' disabled'; btnCor = 'secondary'; }

								  //btnVis += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
								  btnVis += '<a class="btn btn-sm btn-icon btn-icon-mini btn-round btn-simple btn-'+btnCor+btnDis+'"'+btnDis+' style="font-size:9px;" title="Visualizar Vendas do Mês '+MesAno+'" href="javascript:void(0);" onclick="fAbrirModalDetalheVendas( \''+urlPadrao+'\', \'E\', \''+MesAno+'\' );">';
								  btnVis += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
								  btnVis += '</a>';
								  //btnVis += '</div>';
							  }

							  return btnVis;

						  }
					  } // 8-Acao
				],
				createdRow : function(row,data,dataIndex) {

					  $('td', row).addClass('text-center');

					  //var MesAno        = data[0]; //  0-Mes/Ano
					  var VlrVenda      = parseFloat( GetValorDecimal( data[1] ) ); //  1-Venda
					  var VlrApurado    = parseFloat( GetValorDecimal( data[2] ) ); //  2-Apurado
					  var VlrACompensar = parseFloat( GetValorDecimal( data[3] ) ); //  2-A Compensar
					  var VlrResultado  = parseFloat( GetValorDecimal( data[4] ) ); //  4-Resultado
					  var VlrImposto    = parseFloat( GetValorDecimal( data[7] ) ); // 7-Imposto Devido

					  var ColMesAno     = $('td', row).eq(0); //  0-Mes/Ano
					  var ColApurado    = $('td', row).eq(2); //  2-Apurado
					  var ColACompensar = $('td', row).eq(3); //  3-A Compensar
					  var ColResultado  = $('td', row).eq(4); //  4-Resultado
					  var ColImposto    = $('td', row).eq(7); //  7-Imposto Devido

					  if ( VlrApurado > 0){
						  ColMesAno.addClass('text-success font-weight-bold');
						  ColApurado.addClass('text-success font-weight-bold');
					  }
					  if ( VlrApurado < 0 ){
						  ColMesAno.addClass('text-danger font-weight-bold');
						  ColApurado.addClass('text-danger font-weight-bold');
					  }
					  if ( VlrApurado == 0 ){
						  ColMesAno.addClass('text-muted'); //primary
						  ColApurado.addClass('text-muted');
					  }

					  if ( VlrACompensar  > 0 ) ColACompensar.addClass('text-success font-weight-bold');
					  if ( VlrACompensar  < 0 ) ColACompensar.addClass('text-danger font-weight-bold');
					  if ( VlrACompensar == 0 ) ColACompensar.addClass('text-muted');   //info

					  if ( VlrResultado  > 0 ) ColResultado.addClass('text-success font-weight-bold');
					  if ( VlrResultado  < 0 ) ColResultado.addClass('text-danger font-weight-bold');
					  if ( VlrResultado == 0 ) ColResultado.addClass('text-muted');  //primary

					  if ( VlrImposto  > 0 ) ColImposto.addClass('text-success font-weight-bold');
					  if ( VlrImposto  < 0 ) ColImposto.addClass('text-danger font-weight-bold');
					  if ( VlrImposto == 0 ) ColImposto.addClass('text-muted'); //primary

				}, //createdRow
				initComplete: function( settings, json ) {
					  $("#iRefresh").removeClass("fa-spin");
					  $("#btnApuracPesquisar").removeClass("disabled");
					  $("#btnApuracLimpar").removeClass("disabled");
				}, //initComplete
				  order: [],
				  dom: 'frtBpi',
				  buttons: [
						{
						   extend:    'excelHtml5',
						   text:      '<i class="fa fa-file-excel-o"></i> Excel',
						   className: 'btn btn-outline-default btn-sm',
						   title: NOME_PROJETO + ' - Apuração das Operações Comum com BDRs',
						   titleAttr: 'Excel',
						   exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						},
						{
						  extend: 'csvHtml5',
						  charset: 'UTF-8',
						  fieldSeparator: ';',
						  titleAttr: 'CSV',
						  text:      '<i class="fa fa-file-o"></i> CSV',
						  className: 'btn btn-outline-default btn-sm',
						  title: NOME_PROJETO + ' - Apuração das Operações Comum com BDRs',
						  bom: true,
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						},
						{
						  extend: 'pdfHtml5',
						  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						  className: 'btn btn-default btn-sm',
						  titleAttr: 'PDF',
						  title: NOME_PROJETO + ' - Apuração das Operações Comum com BDRs',
						  pageSize: 'A3',
						  alignment: 'center',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] },
						  footer: true,
						  customize: function (doc) {
							  doc.defaultStyle.fontSize = 12;
							  doc.styles.tableHeader.fontSize = 14;
						  }
						},
						{
						  extend: 'print',
						  text:      '<i class="fa fa-print"></i> Imprimir',
						  title: NOME_PROJETO + ' - Apuração das Operações Comum com BDRs',
						  titleAttr: 'Imprimir',
						  className: 'btn btn-default btn-sm',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						}
				  ],
				  bFilter: false,
				  bInfo: false,
				  bLengthChange: false,
				  bSearchable: false,
				  bOrderable: false,
				  bSortable: false,
				  bAutoWidth: false,
				  bPaginate: false,
				  bOrdering: false
			  })
			 .on( 'error.dt', function ( e, settings, techNote, message ) {
				  finalizarAnimacaoPesquisa();
				  return true;
				} );


			  $( document ).ajaxError(function( event, request, settings, thrownError ) {
				  finalizarAnimacaoPesquisa();
			  });

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

    } catch (e) {
		fLimparSomenteGrid( urlPadrao );
		finalizarAnimacaoPesquisa();
      if ( e.description != undefined ){
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      }
    }
}

async function fMontarGridBDRDayTrade( urlPadrao, dataSet ){
  try {

		 promise = new Promise( (resolve, reject) => {

			$('#GridBDRDayTrade').DataTable( {
				processing: true,
				serverSide: false,
				oLanguage: fTraduzirGrid(),
				data: dataSet,
				aoColumns: [
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 1,   //  1-Venda
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[1]; //  1-Venda
							  return data;
						  }
					  }, //  1-Venda
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 2,   //  2-Apurado
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[2]; //  2-Apurado
							  return data;
						  }
					  }, //  2-Apurado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 3, //  3-A Compensar
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[3]; //  3-A Compensar
							  return data;
						  }
					  }, //  3-A Compensar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 4, //  4-Resultado
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[4]; //  4-Resultado
							  return data;
						  }
					  }, //  4-Resultado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 5, //  5-Imposto a Pagar
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[5]; //  5-Imposto a Pagar
							  return data;
						  }
					  }, // 5-Imposto a Pagar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 6, //  6-Imposto Pago
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[6]; //  6-Imposto Pago
							  return data;
						  }
					  }, //  6-Imposto Pago
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 7, //  7-Imposto Devido
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[7]; //  7-Imposto Devido
							  return data;
						  }
					  },  //  7-Imposto Devido
					  { bSortable: false, sWidth: "10px", targets: 8,   // 8-Acao
						  render: function ( data, type, row ) {

							  var btnVis = "";
							  var btnDis = '';
							  var btnCor = 'primary';

							  if ( type == "display") {

								  var MesAno       = row[0]; // 0-Mes/Ano
								  var VlrVenda     = row[2]; // 1-Venda

								  if ( VlrVenda == '0,00' ) { btnDis = ' disabled'; btnCor = 'secondary'; }

								  //btnVis += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
								  btnVis += '<a class="btn btn-sm btn-icon btn-icon-mini btn-round btn-simple btn-'+btnCor+btnDis+'"'+btnDis+' style="font-size:9px;" title="Visualizar Vendas do Mês '+MesAno+'" href="javascript:void(0);" onclick="fAbrirModalDetalheVendas( \''+urlPadrao+'\', \'G\', \''+MesAno+'\' );">';
								  btnVis += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
								  btnVis += '</a>';
								  //btnVis += '</div>';
							  }

							  return btnVis;

						  }
					  } // 8-Acao
				],
				createdRow : function(row,data,dataIndex) {

					  $('td', row).addClass('text-center');

					  //var MesAno        = data[0]; //  0-Mes/Ano
					  var VlrVenda      = parseFloat( GetValorDecimal( data[1] ) ); //  1-Venda
					  var VlrApurado    = parseFloat( GetValorDecimal( data[2] ) ); //  2-Apurado
					  var VlrACompensar = parseFloat( GetValorDecimal( data[3] ) ); //  2-A Compensar
					  var VlrResultado  = parseFloat( GetValorDecimal( data[4] ) ); //  4-Resultado
					  var VlrImposto    = parseFloat( GetValorDecimal( data[7] ) ); // 7-Imposto Devido

					  var ColMesAno     = $('td', row).eq(0); //  0-Mes/Ano
					  var ColApurado    = $('td', row).eq(2); //  2-Apurado
					  var ColACompensar = $('td', row).eq(3); //  3-A Compensar
					  var ColResultado  = $('td', row).eq(4); //  4-Resultado
					  var ColImposto    = $('td', row).eq(7); //  7-Imposto Devido

					  if ( VlrApurado > 0){
						  ColMesAno.addClass('text-success font-weight-bold');
						  ColApurado.addClass('text-success font-weight-bold');
					  }
					  if ( VlrApurado < 0 ){
						  ColMesAno.addClass('text-danger font-weight-bold');
						  ColApurado.addClass('text-danger font-weight-bold');
					  }
					  if ( VlrApurado == 0 ){
						  ColMesAno.addClass('text-muted'); //primary
						  ColApurado.addClass('text-muted');
					  }

					  if ( VlrACompensar  > 0 ) ColACompensar.addClass('text-success font-weight-bold');
					  if ( VlrACompensar  < 0 ) ColACompensar.addClass('text-danger font-weight-bold');
					  if ( VlrACompensar == 0 ) ColACompensar.addClass('text-muted');   //info

					  if ( VlrResultado  > 0 ) ColResultado.addClass('text-success font-weight-bold');
					  if ( VlrResultado  < 0 ) ColResultado.addClass('text-danger font-weight-bold');
					  if ( VlrResultado == 0 ) ColResultado.addClass('text-muted');  //primary

					  if ( VlrImposto  > 0 ) ColImposto.addClass('text-success font-weight-bold');
					  if ( VlrImposto  < 0 ) ColImposto.addClass('text-danger font-weight-bold');
					  if ( VlrImposto == 0 ) ColImposto.addClass('text-muted'); //primary

				}, //createdRow
				initComplete: function( settings, json ) {
					  $("#iRefresh").removeClass("fa-spin");
					  $("#btnApuracPesquisar").removeClass("disabled");
					  $("#btnApuracLimpar").removeClass("disabled");
				}, //initComplete
				  order: [],
				  dom: 'frtBpi',
				  buttons: [
						{
						   extend:    'excelHtml5',
						   text:      '<i class="fa fa-file-excel-o"></i> Excel',
						   className: 'btn btn-outline-default btn-sm',
						   title: NOME_PROJETO + ' - Apuração das Operações Day Trade com BDRs',
						   titleAttr: 'Excel',
						   exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						},
						{
						  extend: 'csvHtml5',
						  charset: 'UTF-8',
						  fieldSeparator: ';',
						  titleAttr: 'CSV',
						  text:      '<i class="fa fa-file-o"></i> CSV',
						  className: 'btn btn-outline-default btn-sm',
						  title: NOME_PROJETO + ' - Apuração das Operações Day Trade com BDRs',
						  bom: true,
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						},
						{
						  extend: 'pdfHtml5',
						  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						  className: 'btn btn-default btn-sm',
						  titleAttr: 'PDF',
						  title: NOME_PROJETO + ' - Apuração das Operações Day Trade com BDRs',
						  pageSize: 'A3',
						  alignment: 'center',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] },
						  footer: true,
						  customize: function (doc) {
							  doc.defaultStyle.fontSize = 12;
							  doc.styles.tableHeader.fontSize = 14;
						  }
						},
						{
						  extend: 'print',
						  text:      '<i class="fa fa-print"></i> Imprimir',
						  title: NOME_PROJETO + ' - Apuração das Operações Day Trade com BDRs',
						  titleAttr: 'Imprimir',
						  className: 'btn btn-default btn-sm',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						}
				  ],
				  bFilter: false,
				  bInfo: false,
				  bLengthChange: false,
				  bSearchable: false,
				  bOrderable: false,
				  bSortable: false,
				  bAutoWidth: false,
				  bPaginate: false,
				  bOrdering: false
			  })
			 .on( 'error.dt', function ( e, settings, techNote, message ) {
				  finalizarAnimacaoPesquisa();
				  return true;
				} );


			  $( document ).ajaxError(function( event, request, settings, thrownError ) {
				  finalizarAnimacaoPesquisa();
			  });

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

    } catch (e) {
		fLimparSomenteGrid( urlPadrao );
		finalizarAnimacaoPesquisa();
      if ( e.description != undefined ){
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      }
    }
}

async function fMontarGridCRIPTO( urlPadrao, dataSet ){
  try {

		 promise = new Promise( (resolve, reject) => {

			$('#GridCRIPTO').DataTable( {
				processing: true,
				serverSide: false,
				oLanguage: fTraduzirGrid(),
				data: dataSet,
				aoColumns: [
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 0 }, //  0-Mes/Ano
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 1,   //  1-Venda
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[1]; //  1-Venda
							  return data;
						  }
					  }, //  1-Venda
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 2,   //  2-Apurado
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[2]; //  2-Apurado
							  return data;
						  }
					  }, //  2-Apurado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 3, //  3-A Compensar
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[3]; //  3-A Compensar
							  return data;
						  }
					  }, //  3-A Compensar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 4, //  4-Resultado
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[4]; //  4-Resultado
							  return data;
						  }
					  }, //  4-Resultado
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 5, //  5-Imposto a Pagar
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[5]; //  5-Imposto a Pagar
							  return data;
						  }
					  }, // 5-Imposto a Pagar
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 6, //  6-Imposto Pago
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[6]; //  6-Imposto Pago
							  return data;
						  }
					  }, //  6-Imposto Pago
					  { bSortable: false, bOrderable: false, sWidth: "50px", targets: 7, //  7-Imposto Devido
						  render: function ( data, type, row ) {
							  if ( type == "display") return "R$ " + row[7]; //  7-Imposto Devido
							  return data;
						  }
					  },  //  7-Imposto Devido
					  { bSortable: false, sWidth: "10px", targets: 8,   // 8-Acao
						  render: function ( data, type, row ) {

							  var btnVis = "";
							  var btnDis = '';
							  var btnCor = 'primary';

							  if ( type == "display") {

								  var MesAno   = row[0]; // 0-Mes/Ano
								  var VlrVenda = row[2]; // 1-Venda

								  if ( VlrVenda == '0,00' ) { btnDis = ' disabled'; btnCor = 'secondary'; }

								  //btnVis += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
								  btnVis += '<a class="btn btn-sm btn-icon btn-icon-mini btn-round btn-simple btn-'+btnCor+btnDis+'"'+btnDis+' style="font-size:9px;" title="Visualizar Vendas do Mês '+MesAno+'" href="javascript:void(0);" onclick="fAbrirModalDetalheVendas( \''+urlPadrao+'\', \'K\', \''+MesAno+'\' );">';
								  btnVis += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
								  btnVis += '</a>';
								  //btnVis += '</div>';
							  }

							  return btnVis;

						  }
					  } // 8-Acao
				],
				createdRow : function(row,data,dataIndex) {

					  $('td', row).addClass('text-center');

					  //var MesAno        = data[0]; //  0-Mes/Ano
					  var VlrVenda      = parseFloat( GetValorDecimal( data[1] ) ); //  1-Venda
					  var VlrApurado    = parseFloat( GetValorDecimal( data[2] ) ); //  2-Apurado
					  var VlrACompensar = parseFloat( GetValorDecimal( data[3] ) ); //  2-A Compensar
					  var VlrResultado  = parseFloat( GetValorDecimal( data[4] ) ); //  4-Resultado
					  var VlrImposto    = parseFloat( GetValorDecimal( data[7] ) ); // 7-Imposto Devido

					  var ColMesAno     = $('td', row).eq(0); //  0-Mes/Ano
					  var ColApurado    = $('td', row).eq(2); //  2-Apurado
					  var ColACompensar = $('td', row).eq(3); //  3-A Compensar
					  var ColResultado  = $('td', row).eq(4); //  4-Resultado
					  var ColImposto    = $('td', row).eq(7); //  7-Imposto Devido

					  if ( VlrApurado > 0){
						  ColMesAno.addClass('text-success font-weight-bold');
						  ColApurado.addClass('text-success font-weight-bold');
					  }
					  if ( VlrApurado < 0 ){
						  ColMesAno.addClass('text-danger font-weight-bold');
						  ColApurado.addClass('text-danger font-weight-bold');
					  }
					  if ( VlrApurado == 0 ){
						  ColMesAno.addClass('text-muted'); //primary
						  ColApurado.addClass('text-muted');
					  }

					  if ( VlrACompensar  > 0 ) ColACompensar.addClass('text-success font-weight-bold');
					  if ( VlrACompensar  < 0 ) ColACompensar.addClass('text-danger font-weight-bold');
					  if ( VlrACompensar == 0 ) ColACompensar.addClass('text-muted');   //info

					  if ( VlrResultado  > 0 ) ColResultado.addClass('text-success font-weight-bold');
					  if ( VlrResultado  < 0 ) ColResultado.addClass('text-danger font-weight-bold');
					  if ( VlrResultado == 0 ) ColResultado.addClass('text-muted');  //primary

					  if ( VlrImposto  > 0 ) ColImposto.addClass('text-success font-weight-bold');
					  if ( VlrImposto  < 0 ) ColImposto.addClass('text-danger font-weight-bold');
					  if ( VlrImposto == 0 ) ColImposto.addClass('text-muted'); //primary

				}, //createdRow
				initComplete: function( settings, json ) {
					  $("#iRefresh").removeClass("fa-spin");
					  $("#btnApuracPesquisar").removeClass("disabled");
					  $("#btnApuracLimpar").removeClass("disabled");
				}, //initComplete
				  order: [],
				  dom: 'frtBpi',
				  buttons: [
						{
						   extend:    'excelHtml5',
						   text:      '<i class="fa fa-file-excel-o"></i> Excel',
						   className: 'btn btn-outline-default btn-sm',
						   title: NOME_PROJETO + ' - Apuração das Operações com CRIPTOs',
						   titleAttr: 'Excel',
						   exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						},
						{
						  extend: 'csvHtml5',
						  charset: 'UTF-8',
						  fieldSeparator: ';',
						  titleAttr: 'CSV',
						  text:      '<i class="fa fa-file-o"></i> CSV',
						  className: 'btn btn-outline-default btn-sm',
						  title: NOME_PROJETO + ' - Apuração das Operações com CRIPTOs',
						  bom: true,
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						},
						{
						  extend: 'pdfHtml5',
						  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						  className: 'btn btn-default btn-sm',
						  titleAttr: 'PDF',
						  title: NOME_PROJETO + ' - Apuração das Operações com CRIPTOs',
						  pageSize: 'A3',
						  alignment: 'center',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] },
						  footer: true,
						  customize: function (doc) {
							  doc.defaultStyle.fontSize = 12;
							  doc.styles.tableHeader.fontSize = 14;
						  }
						},
						{
						  extend: 'print',
						  text:      '<i class="fa fa-print"></i> Imprimir',
						  title: NOME_PROJETO + ' - Apuração das Operações com CRIPTOs',
						  titleAttr: 'Imprimir',
						  className: 'btn btn-default btn-sm',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ] }
						}
				  ],
				  bFilter: false,
				  bInfo: false,
				  bLengthChange: false,
				  bSearchable: false,
				  bOrderable: false,
				  bSortable: false,
				  bAutoWidth: false,
				  bPaginate: false,
				  bOrdering: false
			  })
			 .on( 'error.dt', function ( e, settings, techNote, message ) {
				  finalizarAnimacaoPesquisa();
				  return true;
				} );


			  $( document ).ajaxError(function( event, request, settings, thrownError ) {
				  finalizarAnimacaoPesquisa();
			  });

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

    } catch (e) {
		fLimparSomenteGrid( urlPadrao );
		finalizarAnimacaoPesquisa();
      if ( e.description != undefined ){
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      }
    }
}

async function fCarregarGrid( urlPadrao ){
  try {   
			
		$('#GridComum').dataTable().fnClearTable();
		$('#GridDayTrade').dataTable().fnClearTable();
		$('#GridFII').dataTable().fnClearTable();
		$('#GridETFComum').dataTable().fnClearTable();
		$('#GridETFDayTrade').dataTable().fnClearTable();
		$('#GridBDRComum').dataTable().fnClearTable();
		$('#GridBDRDayTrade').dataTable().fnClearTable();
		$('#GridCRIPTO').dataTable().fnClearTable();

		$("#GridComum").dataTable({ bDestroy: true }).fnDestroy();
		$("#GridDayTrade").dataTable({ bDestroy: true }).fnDestroy();
		$("#GridFII").dataTable({ bDestroy: true }).fnDestroy();
		$("#GridETFComum").dataTable({ bDestroy: true }).fnDestroy();
		$("#GridETFDayTrade").dataTable({ bDestroy: true }).fnDestroy();
		$("#GridBDRComum").dataTable({ bDestroy: true }).fnDestroy();
		$("#GridBDRDayTrade").dataTable({ bDestroy: true }).fnDestroy();
		$("#GridCRIPTO").dataTable({ bDestroy: true }).fnDestroy();
		
		finalizarAnimacaoPesquisa();
		iniciarAnimacaoPesquisar();
		
		var AnoApuracao = $("#selApuracAno").val();
		if ( AnoApuracao == "T") AnoApuracao = "";

		var CalcVlrSuperior = "N";
		if ( $("#chkApuracVlrSuperior20Mil").is(":checked") ) CalcVlrSuperior = "S";
	
		promiseComum = new Promise( (resolve, reject) => {

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "apuracao/grid",
				data    : { AnoApuracao : AnoApuracao, CalcVlrSuperior: CalcVlrSuperior, TpApuracao : 'C' },
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
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridComum( urlPadrao, lista );
					} else{
						finalizarAnimacaoPesquisa();
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
					return false;
				}
			});		

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});	
		
		promiseDayTrade = new Promise( (resolve, reject) => {
		
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "apuracao/grid",
				data    : { AnoApuracao : AnoApuracao, CalcVlrSuperior: "N", TpApuracao : 'D' },
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
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridDayTrade( urlPadrao, lista );
					} else{
						finalizarAnimacaoPesquisa();
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
					return false;
				}
			});			

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
		
		promiseFII = new Promise( (resolve, reject) => {
		
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "apuracao/grid",
				data    : { AnoApuracao : AnoApuracao, CalcVlrSuperior: "N", TpApuracao : 'F' },
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
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridFII( urlPadrao, lista );
					} else{
						finalizarAnimacaoPesquisa();
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
					return false;
				}
			});			

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
		
		promiseETFComum = new Promise( (resolve, reject) => {
		
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "apuracao/grid",
				data    : { AnoApuracao : AnoApuracao, CalcVlrSuperior: "N", TpApuracao : 'E' },
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
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridETFComum( urlPadrao, lista );
					} else{
						finalizarAnimacaoPesquisa();
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
					return false;
				}
			});			

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
		
		promiseETFDayTrade = new Promise( (resolve, reject) => {
		
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "apuracao/grid",
				data    : { AnoApuracao : AnoApuracao, CalcVlrSuperior: "N", TpApuracao : 'G' },
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
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridETFDayTrade( urlPadrao, lista );
					} else{
						finalizarAnimacaoPesquisa();
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
					return false;
				}
			});			

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

		promiseBDRComum = new Promise( (resolve, reject) => {

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "apuracao/grid",
				data    : { AnoApuracao : AnoApuracao, CalcVlrSuperior: "N", TpApuracao : 'I' },
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
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return;
					}else if (resultado == "OK") {
						fMontarGridBDRComum( urlPadrao, lista );
					} else{
						finalizarAnimacaoPesquisa();
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return;
					}

				},
				error: function(data) {
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
					return false;
				}
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

		promiseBDRDayTrade = new Promise( (resolve, reject) => {

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "apuracao/grid",
				data    : { AnoApuracao : AnoApuracao, CalcVlrSuperior: "N", TpApuracao : 'J' },
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
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return;
					}else if (resultado == "OK") {
						fMontarGridBDRDayTrade( urlPadrao, lista );
					} else{
						finalizarAnimacaoPesquisa();
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return;
					}

				},
				error: function(data) {
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
					return false;
				}
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

		promiseCRIPTO= new Promise( (resolve, reject) => {

			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "apuracao/grid",
				data    : { AnoApuracao : AnoApuracao, CalcVlrSuperior: "N", TpApuracao : 'k' },
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
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return;
					}else if (resultado == "OK") {
						fMontarGridCRIPTO( urlPadrao, lista );
					} else{
						finalizarAnimacaoPesquisa();
						fLimparSomenteGrid( urlPadrao );( urlPadrao );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
						return;
					}

				},
				error: function(data) {
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
					return false;
				}
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

    } catch (e) {
		finalizarAnimacaoPesquisa();
		fLimparSomenteGrid( urlPadrao );( urlPadrao );
        if ( e.description != undefined )
		   fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

function fAbrirModalAjusteApuracao( urlPadrao ) {
    try {
	   
       fLimparAreaAlertaModalCad();	 

		var data = new Date();
	   $("#txtCadApurAno").val( data.getFullYear() );
	   $("#txtCadApurTipo").val("C");   
	   
	   $("#PopModalDetalheAjusteApur").modal({backdrop: "static"});	   
	   
	   fCarregarGridAjusteApuracao( urlPadrao );

    } catch (e) {
        $("#PopModalDetalheAjusteApur").modal("hide");
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fCarregarGridAjusteApuracao( urlPadrao ) {
    try {
		   
		fLimparAreaAlertaModalCad();	
		   
		$("#iRefreshBuscar").removeClass("fa-spin");
		$("#btnApuracBuscar").removeClass("disabled");
	   
		$("#txtCadApurVlrJAN").val( "0,00" );
		$("#txtCadApurVlrFEV").val( "0,00" );
		$("#txtCadApurVlrMAR").val( "0,00" );
		$("#txtCadApurVlrABR").val( "0,00" );
		$("#txtCadApurVlrMAI").val( "0,00" );
		$("#txtCadApurVlrJUN").val( "0,00" );
		$("#txtCadApurVlrJUL").val( "0,00" );
		$("#txtCadApurVlrAGO").val( "0,00" );
		$("#txtCadApurVlrSET").val( "0,00" );
		$("#txtCadApurVlrOUT").val( "0,00" );
		$("#txtCadApurVlrNOV").val( "0,00" );
		$("#txtCadApurVlrDEZ").val( "0,00" );	

	   var Ano       = $("#txtCadApurAno").val().trim();
	   var Categoria = $("#txtCadApurTipo").val().trim();
	   
		if( Categoria == "" ){
			fCriarAlertaModalCad(TP_ALERTA_AVISO, "Por favor, preencha o campo Tipo!");
			return false;
		}	
	   
		if( Ano == "" ){
			fCriarAlertaModalCad(TP_ALERTA_AVISO, "Por favor, preencha o campo Ano!");
			return false;
		}	
		
		if( Ano.length != 4 ){
			fCriarAlertaModalCad(TP_ALERTA_AVISO, "Ano inválido!");
			return false;
		}		
		
		var data = new Date();
		if( Ano > data.getFullYear() ){
			fCriarAlertaModalCad(TP_ALERTA_AVISO, "Ano maior que Ano Atual!");
			return false;
		}	
		
		$("#iRefreshBuscar").addClass("fa-spin");
		$("#btnApuracBuscar").addClass("disabled");

		 promise = new Promise( (resolve, reject) => {
	
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "apuracao/carregar",
				data    : { Ano : Ano, Categoria : Categoria },
				success: function (result) {
							   
					$("#iRefreshBuscar").removeClass("fa-spin");
					$("#btnApuracBuscar").removeClass("disabled");
				
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var Apur      = result.data.Dados;
					
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
					} else if (resultado == "FALHA") {
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					} else if (resultado == "OK") {
						
					   if ( Apur.JAN ) { 
					   
						   $("#txtCadApurVlrJAN").val( Apur.JAN );
						   $("#txtCadApurVlrFEV").val( Apur.FEV );
						   $("#txtCadApurVlrMAR").val( Apur.MAR );
						   $("#txtCadApurVlrABR").val( Apur.ABR );
						   $("#txtCadApurVlrMAI").val( Apur.MAI );
						   $("#txtCadApurVlrJUN").val( Apur.JUN );
						   $("#txtCadApurVlrJUL").val( Apur.JUL );
						   $("#txtCadApurVlrAGO").val( Apur.AGO );
						   $("#txtCadApurVlrSET").val( Apur.SET );
						   $("#txtCadApurVlrOUT").val( Apur.OUT );
						   $("#txtCadApurVlrNOV").val( Apur.NOV );
						   $("#txtCadApurVlrDEZ").val( Apur.DEZ );	
	
						} else {
							fCriarAlertaModalCad(TP_ALERTA_ERRO, mensagem); 
						}
						
					} else {
						fCriarAlertaModalCad(TP_ALERTA_ERRO, mensagem); 
					}
	
				},
				error: function (data) {
					$("#iRefreshBuscar").removeClass("fa-spin");
					$("#btnApuracBuscar").removeClass("disabled");
				   fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				}
			});  
	
			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

    } catch (e) {
		$("#iRefreshBuscar").removeClass("fa-spin");
		$("#btnApuracBuscar").removeClass("disabled");
		fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fSalvarDadosAjusteApur( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {
	
			iniciarAnimacaoSalvar();
		
			var Ano       = $("#txtCadApurAno").val().trim();
			var Categoria = $("#txtCadApurTipo").val().trim();
			var VlrJAN    = $("#txtCadApurVlrJAN").val().trim();
			var VlrFEV    = $("#txtCadApurVlrFEV").val().trim();
			var VlrMAR    = $("#txtCadApurVlrMAR").val().trim();
			var VlrABR    = $("#txtCadApurVlrABR").val().trim();
			var VlrMAI    = $("#txtCadApurVlrMAI").val().trim();
			var VlrJUN    = $("#txtCadApurVlrJUN").val().trim();
			var VlrJUL    = $("#txtCadApurVlrJUL").val().trim();
			var VlrAGO    = $("#txtCadApurVlrAGO").val().trim();
			var VlrSET    = $("#txtCadApurVlrSET").val().trim();
			var VlrOUT    = $("#txtCadApurVlrOUT").val().trim();
			var VlrNOV    = $("#txtCadApurVlrNOV").val().trim();
			var VlrDEZ    = $("#txtCadApurVlrDEZ").val().trim();
			
			VlrJAN = parseFloat(GetValorDecimal(VlrJAN));
			VlrFEV = parseFloat(GetValorDecimal(VlrFEV));
			VlrMAR = parseFloat(GetValorDecimal(VlrMAR));
			VlrABR = parseFloat(GetValorDecimal(VlrABR));
			VlrMAI = parseFloat(GetValorDecimal(VlrMAI));
			VlrJUN = parseFloat(GetValorDecimal(VlrJUN));
			VlrJUL = parseFloat(GetValorDecimal(VlrJUL));
			VlrAGO = parseFloat(GetValorDecimal(VlrAGO));
			VlrSET = parseFloat(GetValorDecimal(VlrSET));
			VlrOUT = parseFloat(GetValorDecimal(VlrOUT));
			VlrNOV = parseFloat(GetValorDecimal(VlrNOV));
			VlrDEZ = parseFloat(GetValorDecimal(VlrDEZ));
			 
			 $.ajax({
				 cache   : "false",
				 dataType: "json",
				 async   : true,
				 type    : "POST",
				 url     : urlPadrao + "apuracao/salvar",
				 data    : { Ano       : Ano, 
							 Categoria : Categoria, 
							 VlrJAN    : VlrJAN, 
							 VlrFEV    : VlrFEV, 
							 VlrMAR    : VlrMAR, 
							 VlrABR    : VlrABR, 
							 VlrMAI    : VlrMAI, 
							 VlrJUN    : VlrJUN, 
							 VlrJUL    : VlrJUL, 
							 VlrAGO    : VlrAGO, 
							 VlrSET    : VlrSET, 
							 VlrOUT    : VlrOUT, 
							 VlrNOV    : VlrNOV, 
							 VlrDEZ    : VlrDEZ 
				 },
				 success: function(result) {  
				 
					 finalizarAnimacaoSalvar();
					 
					 var resultado = result.data.Resultado; 
					 var mensagem  = result.data.Mensagem; 
					 
					 if (resultado == "NSESSAO") {
						 $(location).attr('href', urlPadrao + '/login');
						 return false;
					 } else if (resultado == "NOK") {
						 fCriarAlertaModalCad(TP_ALERTA_AVISO, mensagem); 
						 return;
					 } else if (resultado == "FALHA") {
						 fCriarAlertaModalCad(TP_ALERTA_ERRO, mensagem); 
						 return;
					 } else if (resultado == "OK") {
						 $("#PopModalDetalheAjusteApur").modal("hide");					
						 fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
						 fCarregarAnoApuracao( urlPadrao );
						 fCarregarGrid(        urlPadrao );
					 } else {
						 fCriarAlertaModalCad(TP_ALERTA_ERRO, mensagem); 
						 return;
					 }
					 
				 },
				 error: function(data) {
					 finalizarAnimacaoSalvar();
					 fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
					 return;
				 }
			 });
	
			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

async function fAbrirModalDetalheVendas( urlPadrao, TpApuracao, MesAno ){
	try {  

		 promise = new Promise( (resolve, reject) => {
	
			fLimparAreaAlertaPrinc();
		
			var DivGridApuracVendas = $("#DivGridApuracVendas");
			DivGridApuracVendas.html("");
	
			var AnoMesApuracao = MesAno;
			AnoMesApuracao = AnoMesApuracao.replace("/", "");
			AnoMesApuracao = AnoMesApuracao.substring(2, 6) + AnoMesApuracao.substring(0, 2);
	
			if( (TpApuracao=="") || (MesAno=="") || (AnoMesApuracao=="") ){
				fCriarAlertaPrinc(TP_ALERTA_AVISO, "Dados da pesquisa inválido!");
				return false;
			}	
			  
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "apuracao/gridVendas",
				data    : { TpApuracao: TpApuracao, AnoMesApuracao: AnoMesApuracao },
				success: function(result) {  
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
					
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						$("#PopModalDetalheApuracVendas").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						$("#PopModalDetalheApuracVendas").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					} else if (resultado == "OK") {
	
						if ( lista.length > 0 ){
							
							var VendaVlrTotal   = 0.00;
							var VendaVlrValoriz = 0.00;
							var content         = '';
	
							content += '<table class="table table-sm table-hover" style="font-size: 12px;" border="0" cellspacing="0" width="100%" style="margin: 0px;">';
							content += '  <thead>';
							content += '    <tr style="font-size: 12px;" class="thead-dark font-weight-bold"> ';
							content += '      <th>Data</th>';
							content += '      <th>Ativo</th>';
							content += '      <th>Quant.</th>';
							content += '      <th>Preço Médio</th>';
							content += '      <th>Custo/Ação</th>';
							content += '      <th>Total</th>';
							content += '      <th>Valorização</th>';
							content += '      <th>%</th>';
							content += '    </tr>';  
							content += '  </thead>';
							content += '  <tbody>';
							
							$.each(lista, function (index, value) {
	
									var AtvData       = value[0]; // 0-Data
									var AtvCodigo     = value[1]; // 1-CodAtivo
									var AtvQuant      = value[2]; // 2-Quant
									var AtvPreco      = parseFloat( GetValorDecimal(value[3]) ); // 3-Preco/Custo
									var AtvPrecoMedio = parseFloat( GetValorDecimal(value[4]) ); // 4-Preco Medio
									var AtvTotal      = parseFloat( GetValorDecimal(value[5]) ); // 5-Total 
									var AtvValoriz    = parseFloat( GetValorDecimal(value[6]) ); // 6-Vlr Valorizacao 
									var AtvPercent    = parseFloat( GetValorDecimal(value[7]) ); // 7-Perc Valorizacao

									if ( AtvCodigo.includes('/BRL') ) {
									    // AtvQuant      = parseFloat( GetValorDecimalMaior(value[2]) ); // 2-Quant
                                        AtvPreco      = parseFloat( GetValorDecimalMaior(value[3]) ); // 3-Preco/Custo
                                        AtvPrecoMedio = parseFloat( GetValorDecimalMaior(value[4]) ); // 4-Preco Medio
									}
	
									var CorTexto = 'text-muted';
									if ( AtvValoriz > 0 ) CorTexto = 'text-success'; //font-weight-bold 
									if ( AtvValoriz < 0 ) CorTexto = 'text-danger';  //font-weight-bold
	
									VendaVlrTotal   += AtvTotal;
									VendaVlrValoriz += AtvValoriz;
	
									content += '    <tr class="text-center '+CorTexto+'" > ';
									content += '      <td style="width:5px;">'+AtvData+'</td>';
									content += '      <td style="width:5px;">'+AtvCodigo+'</td>';
									content += '      <td style="width:10px;">'+AtvQuant+'</td>';
									if ( AtvCodigo.includes('/BRL') ) {
                                        content += '      <td style="width:15px;">R$ '+fMascaraValorSemLimite(AtvPrecoMedio)+'</td>';
                                        content += '      <td style="width:15px;">R$ '+fMascaraValorSemLimite(AtvPreco)+'</td>';
									} else{
                                        content += '      <td style="width:15px;">R$ '+fMascaraValor(AtvPrecoMedio)+'</td>';
                                        content += '      <td style="width:15px;">R$ '+fMascaraValor(AtvPreco)+'</td>';
                                    }
									content += '      <td style="width:20px;">R$ '+fMascaraValor(AtvTotal)+'</td>';
									content += '      <td style="width:20px;">R$ '+fMascaraValor(AtvValoriz)+'</td>';
									content += '      <td style="width:5px;">'+fMascaraValor(AtvPercent)+'%</td>';
									content += '    </tr>'; 
	
							}); //$.each(lista, function (index, value) {
							
							content += '    <tr style="font-size: 12px;" class="text-dark font-weight-bold" > ';
							content += '      <td> </td>';
							content += '      <td> </td>';
							content += '      <td> </td>';
							content += '      <td> </td>';
							content += '      <td> </td>';
							content += '      <td>R$ '+fMascaraValor(VendaVlrTotal)+'</td>';
							content += '      <td>R$ '+fMascaraValor(VendaVlrValoriz)+'</td>';
							content += '      <td> </td>';
							content += '    </tr>'; 
							
							content += '  </tbody>';
							content += '</table>';
	
							DivGridApuracVendas.html("");
							DivGridApuracVendas.append( content );	
							
							$("#PopModalDetalheApuracVendas").modal({backdrop: "static"});
							return true;
						}// if ( lista.length > 0 ){
	
						fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Sem Dados para Exibir!'); 
						return true;
		   
					} else {
						$("#PopModalDetalheApuracVendas").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					$("#PopModalDetalheApuracVendas").modal("hide");	
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
					return;
				}
			});
	
			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
	
	} catch (e) {
		$("#PopModalDetalheApuracVendas").modal("hide");	
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	}  
}

async function fSalvarConfigApuracao( urlPadrao, cb ){
	try {

		 promise = new Promise( (resolve, reject) => {

            var CalcVlrSuperior = cb.checked ? "S" : "N";

			 $.ajax({
				 cache   : "false",
				 dataType: "json",
				 async   : true,
				 type    : "POST",
				 url     : urlPadrao + "apuracao/salvarconfig",
				 data    : { CalcVlrSuperior : CalcVlrSuperior },
				 success: function(result) {

				 },
				 error: function(data) {
					 fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
				 }
			 });

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			//fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		});

	} catch (e) {
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		return;
	}
}