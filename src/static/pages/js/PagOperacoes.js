
$(document).ready(function(){
	 promise = new Promise( (resolve, reject) => {

		//$(this).attr("title", ":: TnB - Operações ::");
		$("#MnPrincOperacoes").addClass("active open");
		
		fLimparAreaAlertaPrinc();
		fLimparAreaAlertaModalCad();
		fLimparAreaAlertaModalExc();

		$("#FormOper input[type=text]").bind("keyup change", function(){ fCalcularOperacao(); });
		$("#FormOperCripto input[type=text]").bind("keyup change", function(){ fCalcularOperacaoCripto(); });
		// $("#FormOperIncorporacao input[type=text]").bind("keyup change", function(){ fCalcularOperacaoIncorporacao();  });

		resolve(true);
		// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
	})
	.then( txt => {
		//console.log('Sucesso: ' + txt);
	})
	.catch( txt => {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	});
});

function iniciarAnimacaoPesquisar() {
	$("#iRefresh").addClass("fa-spin");
	$("#btnOperPesquisar").addClass("disabled");
	$("#btnOperLimpar").addClass("disabled");
}

function finalizarAnimacaoPesquisa() {
	$("#iRefresh").removeClass("fa-spin");
	$("#btnOperPesquisar").removeClass("disabled");
	$("#btnOperLimpar").removeClass("disabled");
}

function fLimparGrid( urlPadrao ){
	fLimparAreaAlertaPrinc();
	$("#txtOperDataIni").val(   fDataPrimeira()  );
	$("#txtOperDataFim").val(   fDataAnoUltima() );
	$("#selOperAtivo").val(     ""               );	
	$("#selOperCorretora").val( ""               );
	fLimparSomenteGrid( urlPadrao );
}

async function fLimparSomenteGrid( urlPadrao ){	
	try {	
		
		 promise = new Promise( (resolve, reject) => {

			finalizarAnimacaoPesquisa();
			
			$("th").addClass('text-center');
			$('#Grid').dataTable().fnClearTable();
			$("#Grid").dataTable({ bDestroy: true }).fnDestroy();

			$('#Grid').DataTable( {
			    data: [],
				oLanguage: fTraduzirGrid(), 
				aoColumns: [
					{ bSortable: true, sWidth: "10px", targets:  0 }, //  0-Data
					{ bSortable: true, sWidth: "10px", targets:  1 }, //  1-Tipo
					{ bSortable: true, sWidth: "10px", targets:  2 }, //  2-Ativo
					{ bSortable: true, sWidth: "15px", targets:  3 }, //  3-Quant
					{ bSortable: true, sWidth: "30px", targets:  4 }, //  4-Preco
					{ bSortable: true, sWidth: "30px", targets:  5 }, //  5-Corretora
					{ bSortable: true, sWidth: "30px", targets:  6 }, //  6-Tx. Corret
					{ bSortable: true, sWidth: "30px", targets:  7 }, //  7-Taxa Tot
					{ bSortable: true, sWidth: "30px", targets:  8 }, //  8-Total
					{ bSortable: true, sWidth: "30px", targets:  9 }, //  9-Custo/Acao		
					{ visible  : false,                targets: 10 }, // 10-IdOper
					{ visible  : false,                targets: 11 }, // 11-TipoInvest
					{ bSortable: false, sWidth: "30px",targets: 12 }  // 12-Acao
				],
				order: [[ 0, "desc" ], [ 10, "desc" ]],
	            iDisplayLength: 100,
				bLengthChange: false,
				bFilter: false,
				searchable: true,
				orderable: true,
				bAutoWidth: false
			});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
		
	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

async function fMontarGrid( urlPadrao, dataSet ){
  try {   
  
		 promise = new Promise( (resolve, reject) => {

		        $('#Grid').DataTable( {
		          processing: true,
		          serverSide: false,
				  oLanguage: fTraduzirGrid(), 
				  data: dataSet,
		          aoColumns: [
						{ bSortable: true, sWidth: "5px", targets:  0,  //  0-Data
							render: function ( data, type, row ) { 
								if ( type == "display") return colcarFormacataoData(row[0]); //  0-Data
								return data;
							} 
						}, //  0-Data
						{ bSortable: true, sWidth: "10px", targets:  1 }, //  1-Tipo
						{ bSortable: true, sWidth: "5px", targets:  2 }, //  2-Ativo
						{ bSortable: true, sWidth: "15px", targets:  3,   //  3-Quant
							render: function ( data, type, row ) { 
								if ( type == "display"){
								    var TipoInvest = row[11]; // 11-IdOper
								    if ( TipoInvest == 'CRIPTO') return fMascaraValorSemLimite(row[3]); //  3-Quant
								    return colcarFormacataoInteiro(row[3]); //  3-Quant
                                }
								return data;
							} 	
						}, //  3-Quant
						{ bSortable: true, sWidth: "10px", targets:  4,   //  4-Preco
							render: function ( data, type, row ) { 
								if ( type == "display") return "R$ " + row[4]; //  4-Preco
								return data;
							} 				 
						}, //  4-Preco
						{ bSortable: true, sWidth: "35px", targets:  5,}, //  5-Corretora
						{ bSortable: true, sWidth: "10px", targets:  6,   //  6-Tx. Corret
							render: function ( data, type, row ) { 
								if ( type == "display") return "R$ " + row[6];//  6-Tx. Corret
								return data;
							} 				 
						}, //  6-Tx. Corret
						{ bSortable: true, sWidth: "5px", targets:  7,   //  7-Taxa Tot
							render: function ( data, type, row ) { 
								if ( type == "display") return "R$ " + row[7]; //  7-Taxa Tot
								return data;
							} 				 
						}, //  7-Taxa Tot
						{ bSortable: true, sWidth: "25px", targets:  8,   //  8-Total
							render: function ( data, type, row ) { 
								if ( type == "display") return "R$ " + row[8]; //  8-Total
								return data;
							} 				 
						}, //  8-Total
						{ bSortable: true, sWidth: "15px", targets:  9,   //  9-Custo/Acao
							render: function ( data, type, row ) { 
								if ( type == "display") return "R$ " + row[9]; //  9-Custo/Acao
								return data;
							} 				 
						}, //  9-Custo/Acao
						{ visible  : false,                 targets: 10 },  // 10-IdOper
						{ visible  : false,                 targets: 11 },  // 11-TipoInvest
						{ bSortable: false, sWidth: "20px", targets: 12,   // 12-Acao
							render: function ( data, type, row ) {
								
								var btnVis = "";
								var btnEdt = "";
								var btnDel = "";
								var btnDis = '';

								if ( type == "display") {
									
									var Tipo       = row[1];  //  1-Tipo
									var CodAtivo   = row[2];  //  2-Ativo
									var IdOper     = row[10]; // 10-IdOper
									var TipoInvest = row[11]; // 11-IdOper

									Tipo = Tipo.substr(0, 1);

									btnVis += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';

                                    if ( TipoInvest == 'CRIPTO' ) {
                                        btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAbrirModalDetalheOperCripto( \''+urlPadrao+'\', \''+IdOper+'\', \'Alterar\', \''+Tipo+'\', \''+CodAtivo+'\' );"> <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> </a>';
                                    } else {
                                        btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAbrirModalDetalheOper( \''+urlPadrao+'\', \''+IdOper+'\', \'Alterar\', \''+Tipo+'\', \''+CodAtivo+'\' );"> <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> </a>';
                                    }
									
									btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;"  title="Excluir Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fChamarPagExclusaoOper( \''+IdOper+'\', \''+CodAtivo+'\' );">';
									btnDel += '   <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ';
									btnDel += '</a>';
									
									btnDel += '</div>';
								}

								return btnVis + '&nbsp;' + btnEdt + '&nbsp;' + btnDel;
							 
							} 
						} // 11-Acao
		          ],
		          createdRow : function(row,data,dataIndex) {	
                        $('td', row).addClass('text-center');
                        if ( data[1] == "Compra" || data[1] == "Compra/Troca" ) $('td', row).addClass('text-muted');  //  1-Tipo
                        if ( data[1] == "Venda"  || data[1] == "Venda/Troca"  ) $('td', row).addClass('text-danger'); //  1-Tipo
		          }, //createdRow
		          initComplete: function( settings, json ) {
					finalizarAnimacaoPesquisa();
		          },		  
					order: [[ 0, "desc" ], [ 10, "desc" ]],
					dom: 'frtBpi', //Bfrtip //frtBip  //frtBpi
					buttons: [  
						  {
							 extend:    'excelHtml5',
							 text:      '<i class="fa fa-file-excel-o"></i> Excel',
							 className: 'btn btn-outline-default btn-sm',
							 title: NOME_PROJETO + ' - Operações',
							 titleAttr: 'Excel',
							 exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ] },
							 customizeData: function (data) {
		                        for (var i = 0; i < data.body.length; i++) {
		                            for (var j = 0; j < data.body[i].length; j++) {
		                                if (j == 3) data.body[i][j] = '\u200C' + data.body[i][j]; // Formatando a Coluna = 3-Quant
		                            }
		                        }
							}
							//,modifier: { selected: true }
						  }, 
						  {
							extend: 'csvHtml5',
							charset: 'UTF-8',
							fieldSeparator: ';',
							titleAttr: 'CSV',
							text:      '<i class="fa fa-file-o"></i> CSV',
							className: 'btn btn-outline-default btn-sm',
							title: NOME_PROJETO + ' - Operações',
							bom: true,
							//filename: 'CsvTest',
							exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ] } //orthogonal: 'export',
						  },
						  {
							extend: 'pdfHtml5',
							text:      '<i class="fa fa-file-pdf-o"></i> PDF',
							className: 'btn btn-default btn-sm',
							titleAttr: 'PDF',
							title: NOME_PROJETO + ' - Operações', 
							//orientation: 'landscape',
							pageSize: 'A3',
							alignment: 'center',
							//styles: { header: { fontSize: 5},  body: { fontSize: 5}, anotherStyle: { fontSize: 5 } },
							exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ] }, //orthogonal: 'export',
							footer: true,
							customize: function (doc) { 
								doc.defaultStyle.fontSize = 12; 
								doc.styles.tableHeader.fontSize = 14; 
							}
						  },
						  {
							extend: 'print',
							text:      '<i class="fa fa-print"></i> Imprimir',
							title: NOME_PROJETO + ' - Operações',
							titleAttr: 'Imprimir',
							className: 'btn btn-default btn-sm',
							exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ] } //orthogonal: 'export',
						  }
					],			
					pageLength: 100, 
					bLengthChange: false,
					bFilter: false,
					searchable: true,
					orderable: true,
					bAutoWidth: false,
					bInfo: true,
					bSearchable: false,
					bOrderable: true,
					bSortable: true,
					bPaginate: true,
					bOrdering: true
		        });	
				
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
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
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
		
		 promise = new Promise( (resolve, reject) => {

			fLimparAreaAlertaPrinc();
			finalizarAnimacaoPesquisa();
			iniciarAnimacaoPesquisar();
			
			$('#Grid').dataTable().fnClearTable();
			$("#Grid").dataTable({ bDestroy: true }).fnDestroy();	
	  
			var DataIni   = $("#txtOperDataIni").val();
			var DataFim   = $("#txtOperDataFim").val();
			var CodAtivo  = $("#selOperAtivo").val();
			var Corretora = $("#selOperCorretora").val();
			
	        DataIni = tirarFormacataoData(DataIni);
	        DataFim = tirarFormacataoData(DataFim);
			
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "operacoes/grid",
				data    : { CodAtivo  : CodAtivo, Corretora : Corretora, DataIni   : DataIni, DataFim   : DataFim},
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
					finalizarAnimacaoPesquisa();
					fLimparSomenteGrid( urlPadrao );
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); // request.responseText //MSG_ALERTA_ERRO
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
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
		
    } catch (e) {
		finalizarAnimacaoPesquisa();
		fLimparSomenteGrid( urlPadrao );
		if ( e.description != undefined )fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fChamarPagExclusaoOper( IdOper, CodAtivo ) {
    try {

       $("#txtDetOperId").val("");
       $("#txtDetOperCod").val("");
	   
       if ( CodAtivo == "" ){
          fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Cód. Aitvo não informado!'); 
          return;
       }

       if ( IdOper == "" ){
          fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Oper. não informado!'); 
          return;
       }
      
       $("#PopModalDelOper").modal({backdrop: "static"}); // $("#PopModalDelOper").modal("show");
       $("#txtDetOperCod").val( CodAtivo );
       $("#txtDetOperId").val(  IdOper   );

    } catch (e) {
        $("#PopModalDelOper").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fExcluirDadosOperacao( urlPadrao, IdOperac, CodOperac ) {
    try {

		 promise = new Promise( (resolve, reject) => {

				fLimparAreaAlerta("AreaAlertaModalImportOper");
				fLimparAreaAlertaModalExc();
				finalizarAnimacaoExcluir();

				var IdOper   = $("#txtDetOperId").val();
				var CodAtivo = $("#txtDetOperCod").val();

				if ( IdOperac  ) IdOper   = IdOperac;
				if ( CodOperac ) CodAtivo = CodOperac;
				
				if ( CodAtivo == "" ){
					if ( !CodOperac ) fCriarAlertaModalExc(TP_ALERTA_AVISO, 'Cód. Ativo não informado!'); 
					if (  CodOperac ) fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_SUCESSO, 'Cód. Ativo não informado!');
					return;
				}

				if ( IdOper == "" ){
					if ( !IdOperac ) fCriarAlertaModalExc(TP_ALERTA_AVISO, 'Id. Oper. não informado!'); 
					if (  IdOperac ) fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_SUCESSO, 'Id. Oper. não informado!');
					return;
				}

				iniciarAnimacaoExcluir();
			  
				$.ajax({
					dataType: "json",
					type: "post",
					url : urlPadrao + "operacoes/excluir",
					data: { IdOper: IdOper, CodAtivo: CodAtivo },
					success: function (result) {
						
						finalizarAnimacaoExcluir();		
						
						var resultado = result.data.Resultado; 
						var mensagem  = result.data.Mensagem; 

						if (resultado == "NSESSAO") {
							$(location).attr('href', urlPadrao + '/login');
							return false;
						} else if (resultado == "NOK") {
							if ( !IdOperac ) fCriarAlertaModalExc(TP_ALERTA_AVISO, mensagem); 
							if (  IdOperac ) fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_AVISO, mensagem);
							return false;
						} else if (resultado == "FALHA") {
							if ( !IdOperac ) fCriarAlertaModalExc(TP_ALERTA_ERRO, mensagem); 
							if (  IdOperac ) fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_ERRO, mensagem);
							return;
						} else if (resultado == "OK") {				
							
							if ( !IdOperac ) {
								$("#txtDetOperId").val("");
								fCriarAlertaPrinc(TP_ALERTA_SUCESSO, mensagem); 
								$("#PopModalDelOper").modal("hide");
								fCarregarGrid( urlPadrao );
								fCarregarCodigoAtivos( urlPadrao );
							}

							if ( IdOperac ) {
								//fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_SUCESSO, mensagem);
								var tr = $('#TrImport'+IdOperac).closest('tr');	 //tr.fadeOut(400);
								tr.fadeOut(400, function() { 
									tr.remove(); 
									var rowCount = $('#GridImport tr').length;
									if ( rowCount <= 1 )  $("#AreaTableModalImportOper").html( "" ); //$("#GridImport").remove();
								});
							}

							return true;
						} else {
							if ( !IdOperac ) fCriarAlertaModalExc(TP_ALERTA_ERRO, mensagem); 
							if (  IdOperac ) fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_ERRO, mensagem);
							return false;
						}
					},
					error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
						$("#PopModalDelOper").modal("hide");
						finalizarAnimacaoExcluir();
						if ( !IdOperac ) fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText //MSG_ALERTA_ERRO
						if (  IdOperac ) fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_ERRO, MSG_ALERTA_ERRO );// request.responseText //MSG_ALERTA_ERRO
					}
				});

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

    } catch (e) {
        $("#PopModalDelOper").modal("hide");
        finalizarAnimacaoExcluir();
		if ( !IdOperac ) fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		if (  IdOperac ) fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }	
}

function fAbrirModalDetalheOperImportarOper(urlPadrao) {
	try {

		fLimparAreaAlerta("AreaAlertaModalImportOper");
		
		var DivListImport = $("#AreaTableModalImportOper");
		DivListImport.html( "" );

		$("#PopModalImportCSVOper").modal({backdrop: "static"});

    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }	
}

function iniciarAnimacaoImportar() {
    //$("#iImportar").removeClass("fa fa-upload");
    $("#iImportar").addClass("fa-spinner");
    $("#iImportar").addClass("fa-pulse");
    $("#iImportar").addClass("fa-pulse");
}

function finalizarAnimacaImportar() {
   $("#iImportar").removeClass("fa-spinner");
   $("#iImportar").removeClass("fa-pulse");
   $("#iImportar").addClass("fa fa-upload"); 
}

function fImportarCSVOper(urlPadrao) {
	try {

	 finalizarAnimacaImportar();
	 fLimparAreaAlerta("AreaAlertaModalImportOper");

	 var DivListImport = $("#AreaTableModalImportOper");
	 DivListImport.html( "" );
	  
	  var filePath = $("#arquivo");
	  
	  if ( filePath.val().trim() == '' ) {
		fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_AVISO, 'Nenhum arquivo selecionado para importação.');
		return false;
	  }

	  var fileType = ".csv";
	  var regex    = new RegExp("([a-zA-Z0-9\s_\\.\-:])+("+ fileType + ")$");
	  if ( !regex.test( filePath.val().toLowerCase() ) ) {
		fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_AVISO, 'Tipo de Arquivo inválido para importação.');
		return false;
	  }

	  iniciarAnimacaoImportar();
  
	  var formData = new FormData(); 
	  formData.append("arquivo", filePath[0].files[0] );
  
	  $.ajax({
		dataType: "json", 
		type: "POST",
		url: urlPadrao + "operacoes/importarcsv",
		data: formData,
		processData: false,
		contentType: false,
		cache: false,
		timeout: 600000,
		success: function(result) {

		 finalizarAnimacaImportar();

		  var resultado = result.data.Resultado;
		  var mensagem  = result.data.Mensagem;
		  var lista     = result.data.Lista; 
  
		  if (resultado == "NSESSAO") {
			$(location).attr("href", urlPadrao + "/login");
			return false;
		  } else if (resultado == "NOK") {
			fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_AVISO, mensagem);
			return false;
		  } else if (resultado == "FALHA") {
			fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_ERRO, mensagem);
			return;
		  } else if (resultado == "OK") {
			
			filePath.val('');
			fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_SUCESSO, mensagem);

			if ( lista.length > 0 ){

				var content = '';
				content += '<hr />';

				content += '<div class="form-group">';
				content += '  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">';
				content += '    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" ';
				content += '       onclick="fExcluirTodosDadosOperacao( \''+urlPadrao+'\', );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ';
				content += '    </a>';
				content += '  </div>';
				content += '</div>';

				content += '<div class="table-responsive">';
				content += '<table id="GridImport" border="0" style="font-size: 14px" class="table table-sm table-hover table-condensed" cellspacing="0" width="100%">';
				content += '    <col width="10">';//Linha
				content += '    <col width="15">';//Data
				content += '    <col width="15">';//Tipo
				content += '    <col width="15">';//Ativo
				content += '    <col width="15">';//Quant
				content += '    <col width="15">';//Preco
				content += '    <col width="10">'; //Corret
				content += '    <col width="10">'; //Liq
				content += '    <col width="10">'; //Emol
				content += '    <col width="10">'; //ISS
				content += '    <col width="10">'; //IRRF
				content += '    <col width="10">';//Outras
				content += '    <col width="15">';//Situação
				//content += '    <col width="10">';//IdLanc
				content += '    <col width="10">'; //Ação
				content += '  <thead>';
				content += '    <tr style="font-size: 13px" class="bg-secondary text-white text-center">';
				content += '      <th style="width:2px;">Linha</th>'; //0-Linha
				content += '      <th style="width:12px;">Data</th>'; //1-Data
				content += '      <th style="width:15px;">Tipo</th>'; //2-Tipo
				content += '      <th style="width:5px;">Ativo</th>';//3-Ativo
				content += '      <th style="width:5px;">Quant.</th>';//4-Quant
				content += '      <th style="width:5px;">Preco</th>';//5-Preco
				content += '      <th style="width:2px;">Corret.</th>';//6-Corret
				content += '      <th style="width:2px;">Liq.</th>';//7-Liq
				content += '      <th style="width:2px;">Emol.</th>';//8-Emol
				content += '      <th style="width:2px;">ISS</th>';//9-ISS
				content += '      <th style="width:2px;">IRRF</th>';//10-IRRF
				content += '      <th style="width:2px;">Outras</th>';//11-Outras
				content += '      <th style="width:12px;">Situação</th>';//12-Situação
				content += '      <th style="width:10px;display: none; ">IdLanc</th>';//13-IdLanc
				content += '      <th style="width:2px;">Ação</th>';//14-Ação
				content += '    </tr>';
				content += '  </thead>';

				content += '  <tbody>';
				$.each(lista, function (index, value) {
					
					var CodAtivo   = value[2];  //  2-Ativo
					var IdOper     = value[12]; // 12-IdLanc
					var TipoInvest = value[13]; // 13-TipoInvest

					var btnDel = "";
					var btnDis = ( (value[11] == 'Importado') ? '' : ' disabled');

					//btnDel += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
					btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple'+btnDis+'"'+btnDis+' style="font-size:0.5rem;" title="Excluir Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
					btnDel += '   onclick="fExcluirDadosOperacao( \''+urlPadrao+'\', \''+IdOper+'\', \''+CodAtivo+'\' );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ';
					btnDel += '</a>';
					//btnDel += '</div>';
		
					content += '    <tr style="font-size: 12px" id="TrImport'+IdOper+'" class="text-center text-dark font-weight-bold"> ';
					content += '      <td>'+colcarFormacataoInteiro(value[13])+'</td>';
					content += '      <td>'+colcarFormacataoData(value[0])+'</td>';
					content += '      <td>'+value[1]+'</td>';
					content += '      <td>'+value[2]+'</td>';
                    content += '      <td>'+value[3]+'</td>';
					content += '      <td>R$ '+value[4]+'</td>';
					content += '      <td>R$ '+value[5]+'</td>';
					content += '      <td>R$ '+value[6]+'</td>';
					content += '      <td>R$ '+value[7]+'</td>';
					content += '      <td>R$ '+value[8]+'</td>';
					content += '      <td>R$ '+value[9]+'</td>';
					content += '      <td>R$ '+value[10]+'</td>';
					content += '      <td class="text-center ' + ( (value[11] == 'Importado') ? 'text-success' : 'text-danger') +'">'+value[11]+'</td>'; //Situação
					content += '      <td style="display: none;">'+value[12]+'</td>'; //IdLanc
					content += '      <td>'+btnDel+'</td>'; //Ação
					content += '    </tr>';

				}); 

				content += '  </tbody>';
				content += '</table>';
				content += '</div>';

				//content += '<br />';

				content += '<div class="form-group">';
				content += '  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">';
				content += '    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" ';
				content += '       onclick="fExcluirTodosDadosOperacao( \''+urlPadrao+'\', );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ';
				content += '    </a>';
				content += '  </div>';
				content += '</div>';

				DivListImport.append( content );
			}

			return true;
		  } else {
			finalizarAnimacaImportar();
			fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_ERRO, mensagem);
			return false;
		  }
		},
		error: function (request, status, error) { //error: function(data) {  //error: function (request, status, error) {
			finalizarAnimacaImportar();
			fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText //MSG_ALERTA_ERRO
		}
	  });

	} catch (e) {
		finalizarAnimacaImportar();
		fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fExcluirTodosDadosOperacao(urlPadrao) {
	try {


		 promise = new Promise( (resolve, reject) => {

			fLimparAreaAlerta("AreaAlertaModalImportOper");

			$('#GridImport > tbody  > tr').each(function() {
				var CodAtivo = $(this).find("td").eq(3).html(); //3-Ativo
				var IdOper   = $(this).find("td").eq(13).html(); //13-IdLanc
				fExcluirDadosOperacao( urlPadrao, IdOper, CodAtivo );
				//fLimparAreaAlerta("AreaAlertaModalImportOper");
			});

			// fLimparAreaAlerta("AreaAlertaModalImportOper");

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

	} catch (e) {
		fCriarAlerta("AreaAlertaModalImportOper", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}  

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fAbrirModalDetalheOperImportarOperCEI(urlPadrao) {
	try {

		 fLimparAreaAlerta("AreaAlertaModalImportOperCEI");
		
		 $("#TxtDadosImportCEI").val( "" );
		 $("#AreaTableModalImportOperCEI").html( "" );

		$("#PopModalImportOperCEI").modal({backdrop: "static"});

    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }	
}

async function fExcluirTodosDadosOperacaoCEI(urlPadrao) {
	try {

		 promise = new Promise( (resolve, reject) => {

			fLimparAreaAlerta("AreaAlertaModalImportOperCEI");

			$('#GridImport > tbody  > tr').each(function() {
				var CodAtivo = $(this).find("td").eq(3).html();  //3-Ativo
				var IdOper   = $(this).find("td").eq(13).html(); //13-IdLanc
				fExcluirDadosOperacao( urlPadrao, IdOper, CodAtivo );
				// fLimparAreaAlerta("AreaAlertaModalImportOperCEI");
			});

			// fLimparAreaAlerta("AreaAlertaModalImportOperCEI");

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

	} catch (e) {
		fCriarAlerta("AreaAlertaModalImportOperCEI", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}  

function iniciarAnimacaoImportarCEI() {
    //$("#iImportarCEI").removeClass("fa fa-upload");
    $("#iImportarCEI").addClass("fa-spinner");
    $("#iImportarCEI").addClass("fa-pulse");
}

function finalizarAnimacaImportarCEI() {
   $("#iImportarCEI").removeClass("fa-spinner");
   $("#iImportarCEI").removeClass("fa-pulse");
   $("#iImportarCEI").addClass("fa fa-upload"); 
}

function fImportarOperCEI(urlPadrao) {
	try {

	 finalizarAnimacaImportarCEI();
	 fLimparAreaAlerta("AreaAlertaModalImportOperCEI");

	 var DivListImport = $("#AreaTableModalImportOperCEI");
	 DivListImport.html( "" );
	  
	  var TxtDadosImportCEI = $("#TxtDadosImportCEI").val().trim();
	  
	  if ( TxtDadosImportCEI == '' ) {
		fCriarAlerta("AreaAlertaModalImportOperCEI", TP_ALERTA_AVISO, 'Dados da CEI não informado');
		return false;
	  }

	  iniciarAnimacaoImportarCEI();

	  $.ajax({
		dataType: "json", 
		type: "POST",
		async   : true,
		url: urlPadrao + "operacoes/importarcei",
		data: { DadosCEI: TxtDadosImportCEI},
		cache: false,
		success: function(result) {

		 finalizarAnimacaImportarCEI();

		  var resultado = result.data.Resultado;
		  var mensagem  = result.data.Mensagem;
		  var lista     = result.data.Lista; 
  
		  if (resultado == "NSESSAO") {
			$(location).attr("href", urlPadrao + "/login");
			return false;
		  } else if (resultado == "NOK") {
			fCriarAlerta("AreaAlertaModalImportOperCEI", TP_ALERTA_AVISO, mensagem);
			return false;
		  } else if (resultado == "FALHA") {
			fCriarAlerta("AreaAlertaModalImportOperCEI", TP_ALERTA_ERRO, mensagem);
			return;
		  } else if (resultado == "OK") {
			
			fCriarAlerta("AreaAlertaModalImportOperCEI", TP_ALERTA_SUCESSO, mensagem);

			if ( lista.length > 0 ){

				var content = '';
				content += '<hr />';
				
				content += '<div class="form-group">';
				content += '  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">';
				content += '    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" ';
				content += '       onclick="fExcluirTodosDadosOperacaoCEI( \''+urlPadrao+'\', );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ';
				content += '    </a>';
				content += '  </div>';
				content += '</div>';
				
				content += '<div class="table-responsive">';
				content += '<table id="GridImport" border="0" style="font-size: 14px" class="table table-sm table-hover table-condensed" cellspacing="0" width="100%">';
				content += '    <col width="10">';//Linha
				content += '    <col width="15">';//Data
				content += '    <col width="15">';//Tipo
				content += '    <col width="15">';//Ativo
				content += '    <col width="15">';//Quant
				content += '    <col width="15">';//Preco
				// content += '    <col width="50">'; //Corret
				// content += '    <col width="50">'; //Liq
				// content += '    <col width="50">'; //Emol
				// content += '    <col width="50">'; //ISS
				// content += '    <col width="50">'; //IRRF
				// content += '    <col width="50">';//Outras
				content += '    <col width="15">';//Situação
				//content += '    <col width="50">';//IdLanc
				content += '    <col width="10">'; //Ação
				content += '  <thead>';
				content += '    <tr style="font-size: 14px" class="bg-secondary text-white text-center">';
				content += '      <th style="width:2px;">Linha</th>'; //0-Linha
				content += '      <th style="width:12px;">Data</th>'; //1-Data
				content += '      <th style="width:15px;">Tipo</th>'; //2-Tipo
				content += '      <th style="width:5px;">Ativo</th>';//3-Ativo
				content += '      <th style="width:5px;">Quant.</th>';//4-Quant
				content += '      <th style="width:5px;">Preco</th>';//5-Preco
				// content += '      <th style="width:2px;">Corret.</th>';//6-Corret
				// content += '      <th style="width:2px;">Liq.</th>';//7-Liq
				// content += '      <th style="width:2px;">Emol.</th>';//8-Emol
				// content += '      <th style="width:2px;">ISS</th>';//9-ISS
				// content += '      <th style="width:2px;">IRRF</th>';//10-IRRF
				// content += '      <th style="width:2px;">Outras</th>';//11-Outras
				content += '      <th style="width:12px;">Situação</th>';//12-Situação
				content += '      <th style="width:10px;display: none; ">IdLanc</th>';//13-IdLanc
				content += '      <th style="width:2px;">Ação</th>';//14-Ação
				content += '    </tr>';
				content += '  </thead>';

				content += '  <tbody>';
				$.each(lista, function (index, value) {
					
					CodAtivo = value[2];  //  2-Ativo
					IdOper   = value[12]; // 12-IdLanc

					var btnDel = "";
					var btnDis = ( (value[11] == 'Importado') ? '' : ' disabled');

					//btnDel += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
					btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple'+btnDis+'"'+btnDis+' style="font-size:0.5rem;" title="Excluir Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
					btnDel += '   onclick="fExcluirDadosOperacao( \''+urlPadrao+'\', \''+IdOper+'\', \''+CodAtivo+'\' );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ';
					btnDel += '</a>';
					//btnDel += '</div>';
	
					content += '    <tr style="font-size: 12px" id="TrImport'+IdOper+'" class="text-center font-weight-bold "> ';
					content += '      <td>'+colcarFormacataoInteiro(value[13])+'</td>'; //Linha
					content += '      <td>'+colcarFormacataoData(value[0])+'</td>'; //Data
					content += '      <td>'+value[1]+'</td>'; //Tipo
					content += '      <td>'+value[2]+'</td>';//Ativo
					content += '      <td>'+colcarFormacataoInteiro(value[3])+'</td>'; //Quant
					content += '      <td>R$ '+value[4]+'</td>'; //Preco
					content += '      <td style="display: none;">R$ '+value[5]+'</td>'; //Corret
					content += '      <td style="display: none;">R$ '+value[6]+'</td>'; //Liq
					content += '      <td style="display: none;">R$ '+value[7]+'</td>'; //Emol
					content += '      <td style="display: none;">R$ '+value[8]+'</td>'; //ISS
					content += '      <td style="display: none;">R$ '+value[9]+'</td>'; //IRRF
					content += '      <td style="display: none;">R$ '+value[10]+'</td>'; //Outras
					content += '      <td class="text-center ' + ( (value[11] == 'Importado') ? 'text-success' : 'text-danger') +'">'+value[11]+'</td>'; //Situação
					content += '      <td style="display: none;">'+value[12]+'</td>'; //IdLanc
					content += '      <td>'+btnDel+'</td>'; //Ação
					content += '    </tr>';

				}); 

				content += '  </tbody>';
				content += '</table>';
				content += '</div>';

				//content += '<br />';

				content += '<div class="form-group">';
				content += '  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">';
				content += '    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" ';
				content += '       onclick="fExcluirTodosDadosOperacaoCEI( \''+urlPadrao+'\', );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ';
				content += '    </a>';
				content += '  </div>';
				content += '</div>';

				DivListImport.append( content );
			}

			return true;
		  } else {
			finalizarAnimacaImportar();
			fCriarAlerta("AreaAlertaModalImportOperCEI", TP_ALERTA_ERRO, mensagem);
			return false;
		  }
		},
		error: function (request, status, error) { //error: function(data) {  //error: function (request, status, error) {
			finalizarAnimacaImportar();
			fCriarAlerta("AreaAlertaModalImportOperCEI", TP_ALERTA_ERRO, request.responseText ); // request.responseText //MSG_ALERTA_ERRO
		}
	  });

	} catch (e) {
		finalizarAnimacaImportar();
		fCriarAlerta("AreaAlertaModalImportOperCEI", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}


//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fAbrirModalDetalheOperImportarOperNotaCorretagem(urlPadrao) {
	try {

        $("#txtArquivoNota").val('');
        $("#txtCorretoraNota").val('');
        fLimparAreaAlerta("AreaAlertaModalImportOperNotaCorretagem");
        $("#AreaTableModalImportOperNotaCorretagem").html( "" );
        $("#PopModalImportOperNotaCorretagem").modal({backdrop: "static"});

    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fExcluirTodosDadosOperacaoNotaCorretagem(urlPadrao) {
	try {

		 promise = new Promise( (resolve, reject) => {

			fLimparAreaAlerta("AreaAlertaModalImportOperNotaCorretagem");

			$('#GridImport > tbody  > tr').each(function() {
				var CodAtivo = $(this).find("td").eq(3).html();  //3-Ativo
				var IdOper   = $(this).find("td").eq(13).html(); //13-IdLanc
				fExcluirDadosOperacao( urlPadrao, IdOper, CodAtivo );
				// fLimparAreaAlerta("AreaAlertaModalImportOperNotaCorretagem");
			});

			// fLimparAreaAlerta("AreaAlertaModalImportOperNotaCorretagem");

			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

	} catch (e) {
		fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

function iniciarAnimacaoImportarNotaCorretagem() {
    $("#BtnModalImportOperNotaCorretagemSalvar").addClass("disabled");
    //$("#iImportarNotaCorretagem").removeClass("fa fa-upload");
    $("#iImportarNotaCorretagem").addClass("fa-spinner");
    $("#iImportarNotaCorretagem").addClass("fa-pulse");
}

function finalizarAnimacaImportarNotaCorretagem() {
    $("#BtnModalImportOperNotaCorretagemSalvar").removeClass("disabled");
    $("#iImportarNotaCorretagem").removeClass("fa-spinner");
    $("#iImportarNotaCorretagem").removeClass("fa-pulse");
    $("#iImportarNotaCorretagem").addClass("fa fa-upload");
}

function fImportarOperNotaCorretagem(urlPadrao) {
	try {

	 finalizarAnimacaImportarNotaCorretagem();
	 fLimparAreaAlerta("AreaAlertaModalImportOperNotaCorretagem");

	 var DivListImport = $("#AreaTableModalImportOperNotaCorretagem");
	 DivListImport.html( "" );

	  var filePath = $("#txtArquivoNota");
	  var txtCorretoraNota = $("#txtCorretoraNota").val();

	  if ( filePath.val().trim() == '' ) {
		fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem", TP_ALERTA_AVISO, 'Nenhum arquivo selecionado para importação.');
		return false;
	  }

	  var fileType = ".pdf";
	  var regex    = new RegExp("([a-zA-Z0-9\s_\\.\-:])+("+ fileType + ")$");
	  if ( !regex.test( filePath.val().toLowerCase() ) ) {
		fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem", TP_ALERTA_AVISO, 'Tipo de Arquivo inválido para importação.');
		return false;
	  }

	  DivListImport.html( "<br><br><br> <h6 class='text-center font-weight-bold'>Aguarde, estamos importando a sua nota!!!</h6>" );

	  iniciarAnimacaoImportarNotaCorretagem();

	  var formData = new FormData();
	  formData.append("corretora", txtCorretoraNota.trim() );
	  formData.append("arquivo", filePath[0].files[0] );

	  $.ajax({
		dataType: "json",
		type: "POST",
		url: urlPadrao + "operacoes/importarnotacorretagem",
		data: formData,
		processData: false,
		contentType: false,
		cache: false,
		timeout: 600000,
		success: function(result) {

		 DivListImport.html( "" );

		 finalizarAnimacaImportarNotaCorretagem();

		  var resultado = result.data.Resultado;
		  var mensagem  = result.data.Mensagem;
		  var lista     = result.data.Lista;

		  if (resultado == "NSESSAO") {
			$(location).attr("href", urlPadrao + "/login");
			return false;
		  } else if (resultado == "NOK") {
			fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem", TP_ALERTA_AVISO, mensagem);
			return false;
		  } else if (resultado == "FALHA") {
			fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem", TP_ALERTA_ERRO, mensagem);
			return;
		  } else if (resultado == "OK") {

			fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem", TP_ALERTA_SUCESSO, mensagem);

			if ( lista.length > 0 ){

				var content = '';

				content += '<hr />';
				content += '<br />';

				content += '<div class="table-responsive">';
				content += '<table border="0" style="font-size: 13px" class="table table-sm table-hover table-condensed" cellspacing="0" width="100%">';
				content += '    <col width="15">';//Data
				content += '    <col width="15">';//TotalBruto
                content += '    <col width="15">'; //Liq
                content += '    <col width="15">'; //Emol
                content += '    <col width="15">'; //Corret
                content += '    <col width="15">'; //ISS
                content += '    <col width="15">'; //IRRF
                content += '    <col width="15">';//Outras
				content += '    <col width="15">';//TotalLiquido
				content += '  <thead>';
				content += '    <tr style="font-size: 13px" class="bg-secondary text-white text-center">';
				content += '      <th style="width:12px;">Data</th>';
				content += '      <th style="width:5px;">Tot. Bruto</th>';
				content += '      <th style="width:2px;">Liq.</th>';
				content += '      <th style="width:2px;">Emol.</th>';
				content += '      <th style="width:2px;">Corret.</th>';
				content += '      <th style="width:2px;">ISS</th>';
				content += '      <th style="width:2px;">IRRF</th>';
				content += '      <th style="width:2px;">Outras</th>';
				content += '      <th style="width:5px;">Tot. Líquido</th>';
				content += '    </tr>';
				content += '  </thead>';

				content += '  <tbody>';

				$.each(lista, function (index, value) {
				    if (value[0] == 'CALC') {
                        content += '    <tr style="font-size: 12px" class="text-center font-weight-bold"> ';
                        content += '      <td>'+colcarFormacataoData(value[1])+'</td>'; //Data
                        content += '      <td>R$ '+value[2]+'</td>'; //Tot.Bruto
                        content += '      <td>R$ '+value[3]+'</td>'; //Liq
                        content += '      <td>R$ '+value[4]+'</td>'; //Emol
                        content += '      <td>R$ '+value[5]+'</td>'; //Corret
                        content += '      <td>R$ '+value[6]+'</td>'; //ISS
                        content += '      <td>R$ '+value[7]+'</td>'; //IRRF
                        content += '      <td>R$ '+value[8]+'</td>'; //Outras
                        content += '      <td>R$ '+value[9]+'</td>'; //Tot.Líquido
                        content += '    </tr>';
				     }

				}); // $.each(lista, function (index, value) {

				content += '  </tbody>';
				content += '</table>';
				content += '</div>';

				content += '<hr />';

				content += '<div class="form-group">';
				content += '  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">';
				content += '    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" ';
				content += '       onclick="fExcluirTodosDadosOperacaoNotaCorretagem( \''+urlPadrao+'\', );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ';
				content += '    </a>';
				content += '  </div>';
				content += '</div>';

				content += '<div class="table-responsive">';
				content += '<table id="GridImport" border="0" style="font-size: 13px" class="table table-sm table-hover table-condensed" cellspacing="0" width="100%">';
				content += '    <col width="10">';//Linha
				content += '    <col width="15">';//Data
				content += '    <col width="15">';//Tipo
				content += '    <col width="15">';//Ativo
				content += '    <col width="15">';//Quant
				content += '    <col width="15">';//Preco
                content += '    <col width="15">'; //Corret
                content += '    <col width="15">'; //Liq
                content += '    <col width="15">'; //Emol
                content += '    <col width="15">'; //ISS
                content += '    <col width="15">'; //IRRF
                content += '    <col width="15">';//Outras
				content += '    <col width="15">';//Situação
				//content += '    <col width="50">';//IdLanc
				content += '    <col width="10">'; //Ação
				content += '  <thead>';
				content += '    <tr style="font-size: 13px" class="bg-secondary text-white text-center">';
				content += '      <th style="width:2px;">Linha</th>'; //0-Linha
				content += '      <th style="width:12px;">Data</th>'; //1-Data
				content += '      <th style="width:15px;">Tipo</th>'; //2-Tipo
				content += '      <th style="width:5px;">Ativo</th>';//3-Ativo
				content += '      <th style="width:5px;">Quant.</th>';//4-Quant
				content += '      <th style="width:5px;">Preco</th>';//5-Preco
				content += '      <th style="width:2px;">Corret.</th>';//6-Corret
				content += '      <th style="width:2px;">Liq.</th>';//7-Liq
				content += '      <th style="width:2px;">Emol.</th>';//8-Emol
				content += '      <th style="width:2px;">ISS</th>';//9-ISS
				content += '      <th style="width:2px;">IRRF</th>';//10-IRRF
				content += '      <th style="width:2px;">Outras</th>';//11-Outras
				content += '      <th style="width:12px;">Situação</th>';//12-Situação
				content += '      <th style="width:10px;display: none; ">IdLanc</th>';//13-IdLanc
				content += '      <th style="width:2px;">Ação</th>';//14-Ação
				content += '    </tr>';
				content += '  </thead>';

				content += '  <tbody>';
				$.each(lista, function (index, value) {
                    if (value[0] != 'CALC') {

                        CodAtivo = value[2];  //  2-Ativo
                        IdOper   = value[12]; // 12-IdLanc

                        var btnDel = "";
                        var btnDis = ( (value[11] == 'Importado') ? '' : ' disabled');

                        //btnDel += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
                        btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple'+btnDis+'"'+btnDis+' style="font-size:0.5rem;" title="Excluir Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
                        btnDel += '   onclick="fExcluirDadosOperacao( \''+urlPadrao+'\', \''+IdOper+'\', \''+CodAtivo+'\' );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ';
                        btnDel += '</a>';
                        //btnDel += '</div>';

                        //content += '    <tr style="font-size: 12px" id="TrImport'+IdOper+'" class="text-center ' + ( (value[11] == 'Importado') ? 'text-success' : 'text-danger') +'"> ';
                        content += '    <tr style="font-size: 12px" id="TrImport'+IdOper+'" class="text-center font-weight-bold "> ';
                        content += '      <td>'+colcarFormacataoInteiro(value[13])+'</td>'; //Linha
                        content += '      <td>'+colcarFormacataoData(value[0])+'</td>'; //Data
                        content += '      <td>'+value[1]+'</td>'; //Tipo
                        content += '      <td>'+value[2]+'</td>';//Ativo
                        content += '      <td>'+colcarFormacataoInteiro(value[3])+'</td>'; //Quant
                        content += '      <td>R$ '+value[4]+'</td>'; //Preco
                        content += '      <td>R$ '+value[5]+'</td>'; //Corret
                        content += '      <td>R$ '+value[6]+'</td>'; //Liq
                        content += '      <td>R$ '+value[7]+'</td>'; //Emol
                        content += '      <td>R$ '+value[8]+'</td>'; //ISS
                        content += '      <td>R$ '+value[9]+'</td>'; //IRRF
                        content += '      <td>R$ '+value[10]+'</td>'; //Outras
                        content += '      <td class="text-center ' + ( (value[11] == 'Importado') ? 'text-success' : 'text-danger') +'">'+value[11]+'</td>'; //Situação
                        content += '      <td style="display: none;">'+value[12]+'</td>'; //IdLanc
                        content += '      <td>'+btnDel+'</td>'; //Ação
                        content += '    </tr>';

                    }
				});

				content += '  </tbody>';
				content += '</table>';
				content += '</div>';

				//content += '<br />';

				content += '<div class="form-group">';
				content += '  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">';
				content += '    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" ';
				content += '       onclick="fExcluirTodosDadosOperacaoNotaCorretagem( \''+urlPadrao+'\', );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ';
				content += '    </a>';
				content += '  </div>';
				content += '</div>';

				DivListImport.append( content );
			}

			return true;
		  } else {
			finalizarAnimacaImportar();
			fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem", TP_ALERTA_ERRO, mensagem);
			DivListImport.html( "" );
			return false;
		  }
		},
		error: function (request, status, error) { //error: function(data) {  //error: function (request, status, error) {
			finalizarAnimacaImportar();
			fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem", TP_ALERTA_ERRO, request.responseText ); // request.responseText //MSG_ALERTA_ERRO
			DivListImport.html( "" );
		}
	  });

	} catch (e) {
		finalizarAnimacaImportar();
		fCriarAlerta("AreaAlertaModalImportOperNotaCorretagem", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		DivListImport.html( "" );
	}
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function iniciarAnimacaoExcluirTds() {
    $("#iExcluirTds").removeClass("fa-check");
    $("#iExcluirTds").addClass("fa-spinner");
    $("#iExcluirTds").addClass("fa-pulse");
	$("#BtnModalDelTdsOperSim").addClass("disabled");
}

function finalizarAnimacaoExcluirTds() {
	$("#iExcluirTds").removeClass("fa-spinner");
	$("#iExcluirTds").removeClass("fa-pulse");
	$("#iExcluirTds").addClass("fa-check"); //fa-check-square-o
	$("#BtnModalDelTdsOperSim").removeClass("disabled");
}

function fAbrirModalLimparTodasOper() {
    try {
	   
      fLimparAreaAlerta("AreaAlertaModalExcTds");
      $("#PopModalDelTdsOper").modal({backdrop: "static"}); 

    } catch (e) {
        $("#PopModalDelTdsOper").modal("hide");
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fExcluirTodasOperacao( urlPadrao ) {
    try {

		 promise = new Promise( (resolve, reject) => {

	        finalizarAnimacaoExcluirTds();
			iniciarAnimacaoExcluirTds();

			fLimparAreaAlerta("AreaAlertaModalExcTds");
		  
			$.ajax({
				dataType: "json",
				type: "post",
				url : urlPadrao + "operacoes/excluirtudo",
				data: {},
				success: function (result) {
						
					finalizarAnimacaoExcluirTds();
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 

					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fCriarAlerta("AreaAlertaModalExcTds", TP_ALERTA_AVISO, mensagem);
						return false;
					} else if (resultado == "FALHA") {
						fCriarAlerta("AreaAlertaModalExcTds", TP_ALERTA_ERRO, mensagem);
						return;
					} else if (resultado == "OK") {		
						$("#PopModalDelTdsOper").modal("hide");
						fCriarAlertaPrinc(TP_ALERTA_SUCESSO, mensagem); 
						fCarregarGrid( urlPadrao );
						fCarregarCodigoAtivos( urlPadrao );
						return true;
					} else {
						fCriarAlerta("AreaAlertaModalExcTds", TP_ALERTA_ERRO, mensagem);
						return false;
					}

				},
				error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
					finalizarAnimacaoExcluirTds();
					$("#PopModalDelTdsOper").modal("hide");
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);// request.responseText //MSG_ALERTA_ERRO
				}
			});
			
			resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			//console.log('Sucesso: ' + txt);
		})
		.catch( txt => {
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

    } catch (e) {
		finalizarAnimacaoExcluirTds();
		$("#PopModalDelTdsOper").modal("hide");
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }	
}

function fBuscarPrecoMedioOper( urlPadrao ) {
    try {

		$("#txtDetOperIncorporacaoPrecoMedioAtual").val( "0,00" );
		fCalcularOperacaoIncorporacao();

		var CodAtivo = $("#selDetOperIncorporacaoAtivoAtual").val().trim();

		if ( CodAtivo == "" ){
			//fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, 'Ativo não informado!');
			return;
		}

		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "operacoes/precomedio",
			data: { CodAtivo : CodAtivo },
			success: function (result) {

				var resultado = result.data.Resultado;
				var mensagem  = result.data.Mensagem;
				var Oper      = result.data.Dados;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, mensagem);
					return false;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
					return;
				} else if (resultado == "OK") {
					if ( Oper.PrecoMedio ){
						$("#txtDetOperIncorporacaoPrecoMedioAtual").val( Oper.PrecoMedio );
						fCalcularOperacaoIncorporacao();
					}
					return true;
				} else {
					fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
					return false;
				}
			},
			error: function (data) {
				fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			}
		});

    } catch (e) {
		fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

function fAbrirModalDetalheOperIncorporacao( urlPadrao ) {
    try {


        $("#txtDetOperIncorporacaoData").val( fDataAtual() );
        $("#txtDetOperIncorporacaoFator").val("1,0");
        //$("#selDetOperIncorporacaoCorretora").val("");
        $('#selDetOperIncorporacaoCorretora')[0].selectedIndex = 2; // Primeira Corretora
        fDefinirPadraoSelect('selDetOperIncorporacaoCorretora');

        $("#selDetOperIncorporacaoAtivoAtual").val("");
        fDefinirPadraoSelect('selDetOperIncorporacaoAtivoAtual');
        $("#txtDetOperIncorporacaoQuantAtual").val("0");
        $("#txtDetOperIncorporacaoPrecoMedioAtual").val("0,00");
        $("#txtDetOperIncorporacaoTotalAtual").val("0,00");

        $("#selDetOperIncorporacaoAtivoNovo").val("");
        fDefinirPadraoSelect('selDetOperIncorporacaoAtivoNovo');
        $("#txtDetOperIncorporacaoQuantNovo").val("0");
        $("#txtDetOperIncorporacaoPrecoMedioNovo").val("0,00");
        $("#txtDetOperIncorporacaoTotalNovo").val("0,00");

        fCalcularOperacaoIncorporacao();

        $('#PopModalDetalheOperIncorporacao').modal({backdrop: 'static'});
		$("#txtDetOperIncorporacaoFator").focus();

    } catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

function fCalcularOperacaoIncorporacao() {
    try {

        var Fator = 0;
        var QuantAtual = 0;
        var PrecoAtual = 0;
        var TotalAtual = 0;
        var QuantNovo = 0;
        var PrecoNovo = 0;
        var TotalNovo = 0;

        if ( $('#txtDetOperIncorporacaoFator').length           ) Fator      = GetValorDecimal( $('#txtDetOperIncorporacaoFator').val() );
        if ( $('#txtDetOperIncorporacaoQuantAtual').length      ) QuantAtual = GetValorInteiro( $('#txtDetOperIncorporacaoQuantAtual').val() );
        if ( $('#txtDetOperIncorporacaoPrecoMedioAtual').length ) PrecoAtual = GetValorDecimal( $('#txtDetOperIncorporacaoPrecoMedioAtual').val() );
        // if ( $('#txtDetOperIncorporacaoQuantNovo').length       ) QuantNovo  = GetValorInteiro( $('#txtDetOperIncorporacaoQuantNovo').val() );
        // if ( $('#txtDetOperIncorporacaoPrecoMedioNovo').length  ) PrecoNovo  = GetValorDecimal( $('#txtDetOperIncorporacaoPrecoMedioNovo').val() );

        if ( PrecoAtual > 0 && QuantAtual > 0 ) TotalAtual = parseFloat( parseFloat(PrecoAtual) * parseInt(QuantAtual) );
        if ( Fator      > 0 && QuantAtual > 0 ) QuantNovo  = parseInt(   parseInt(QuantAtual)   / parseFloat(Fator)    );
        if ( TotalAtual > 0 && QuantNovo  > 0 ) PrecoNovo  = parseFloat( parseFloat(TotalAtual) / parseInt(QuantNovo)  );
        if ( PrecoNovo  > 0 && QuantNovo  > 0 ) TotalNovo  = parseFloat( parseFloat(PrecoNovo)  * parseInt(QuantNovo)  );

        $("#txtDetOperIncorporacaoTotalAtual").val( fMascaraValor(TotalAtual) );
        $("#txtDetOperIncorporacaoQuantNovo").val( QuantNovo ); // colcarFormacataoInteiro(QuantNovo).replace('.', '')
        $("#txtDetOperIncorporacaoPrecoMedioNovo").val( fMascaraValor(PrecoNovo) );
        $("#txtDetOperIncorporacaoTotalNovo").val( fMascaraValor(TotalNovo) );

    } catch (e) {
        fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

function fValidarDadosOperIncorporacao() {
	try {

		var Data  = $("#txtDetOperIncorporacaoData").val();
		var Fator = $("#txtDetOperIncorporacaoFator").val();

		var AtivoAtual = $("#selDetOperIncorporacaoAtivoAtual").val();
		var QuantAtual = $("#txtDetOperIncorporacaoQuantAtual").val();
		var PrecoAtual = $("#txtDetOperIncorporacaoPrecoMedioAtual").val();

		var AtivoNovo = $("#selDetOperIncorporacaoAtivoNovo").val();
		var QuantNovo = $("#txtDetOperIncorporacaoQuantNovo").val();
		var PrecoNovo = $("#txtDetOperIncorporacaoPrecoMedioNovo").val();

		var ListaErros = "";
		if ( Data  == ""                                                       ) ListaErros = ListaErros + " - Data<br/>";
		if ( Fator == ""  || Fator == "0"                                      ) ListaErros = ListaErros + " - Fator<br/>";
		if ( AtivoAtual == ""                                                 ) ListaErros = ListaErros + " - Ativo Atual<br/>";
		if ( QuantAtual == ""  || QuantAtual == "0"                           ) ListaErros = ListaErros + " - Quant. Atual<br/>";
		if ( PrecoAtual == ""  || PrecoAtual == ",00" || PrecoAtual == "0,00" ) ListaErros = ListaErros + " - Preço Médio Atual<br/>";
		if ( AtivoNovo == ""                                                  ) ListaErros = ListaErros + " - Ativo Novo<br/>";
		if ( QuantNovo == ""  || QuantNovo == "0"                             ) ListaErros = ListaErros + " - Quant. Novo<br/>";
		if ( PrecoNovo == ""  || PrecoNovo == ",00" || PrecoNovo == "0,00"    ) ListaErros = ListaErros + " - Preço Médio Novo<br/>";

		if ( ListaErros != "" ){
			fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, "Os seguintes campos não estão preenchido: <br/>"+ListaErros);
			return false;
		}

		return true;

	} catch (e) {
		fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		return false;
	}
}

function iniciarAnimacaoSalvarIncorporacao() {
    $("#iSalvarIncorporacao").removeClass("fa-check");
    $("#iSalvarIncorporacao").addClass("fa-spinner");
    $("#iSalvarIncorporacao").addClass("fa-pulse");
    $("#BtnModalDetalheOperIncorporacaoSalvar").addClass("disabled");
}

function finalizarAnimacaoSalvarIncorporacao() {
   $("#iSalvarIncorporacao").removeClass("fa-spinner");
   $("#iSalvarIncorporacao").removeClass("fa-pulse");
   $("#iSalvarIncorporacao").addClass("fa-check");
   $("#BtnModalDetalheOperIncorporacaoSalvar").removeClass("disabled");
}

function fSalvarDadosOperIncorporacao( urlPadrao ){
	try {

		if ( !fValidarDadosOperIncorporacao() ) return;

		iniciarAnimacaoSalvarIncorporacao();

		var Data            = $("#txtDetOperIncorporacaoData").val();
		var Fator           = $("#txtDetOperIncorporacaoFator").val();
		var Corretora       = $("#selDetOperIncorporacaoCorretora").val();
		var CodAtivoAtual   = $("#selDetOperIncorporacaoAtivoAtual").val();
		var QuantAtual      = $("#txtDetOperIncorporacaoQuantAtual").val();
		var PrecoMedioAtual = '0' + $("#txtDetOperIncorporacaoPrecoMedioAtual").val();
		var CodAtivoNovo    = $("#selDetOperIncorporacaoAtivoNovo").val();
		var QuantNovo       = $("#txtDetOperIncorporacaoQuantNovo").val();
		var PrecoMedioNovo  = '0' + $("#txtDetOperIncorporacaoPrecoMedioNovo").val();

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "operacoes/salvarincorporacao",
			data    : {
			    Data            : Data,
			    Fator           : Fator,
			    Corretora       : Corretora,
			    CodAtivoAtual   : CodAtivoAtual,
			    QuantAtual      : QuantAtual,
			    PrecoMedioAtual : PrecoMedioAtual,
			    CodAtivoNovo    : CodAtivoNovo,
			    QuantNovo       : QuantNovo,
			    PrecoMedioNovo  : PrecoMedioNovo
			},
			success: function(result) {
                finalizarAnimacaoSalvarIncorporacao();
                var resultado = result.data.Resultado;
                var mensagem = result.data.Mensagem;
                if (resultado == "NSESSAO") {
                    $(location).attr('href', urlPadrao + '/login');
                    return false;
                } else if (resultado == "NOK") {
                    fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, mensagem);
                    return;
                } else if (resultado == "FALHA") {
                    fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
                    return;
                } else if (resultado == "OK") {
                    $("#PopModalDetalheOperIncorporacao").modal("hide");
                    fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
                    fCarregarGrid( urlPadrao );
                } else {
                    fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
                    return;
                }
			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				finalizarAnimacaoSalvarIncorporacao();
				fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText //MSG_ALERTA_ERRO
				return;
			}
		});

	} catch (e) {
		finalizarAnimacaoSalvarIncorporacao();
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		return;
	}
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------


function fAbrirModalDetalheOperTroca( urlPadrao ) {
    try {


        $("#selDetOperTrocaAtivoAtual").val("");
        fDefinirPadraoSelect('selDetOperTrocaAtivoAtual');

        $("#selDetOperTrocaAtivoNovo").val("");
        fDefinirPadraoSelect('selDetOperTrocaAtivoNovo');

        $('#PopModalDetalheOperTroca').modal({backdrop: 'static'});

    } catch (e) {
		fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

function fValidarDadosOperTroca() {
	try {

		var AtivoAtual = $("#selDetOperTrocaAtivoAtual").val();
		var AtivoNovo = $("#selDetOperTrocaAtivoNovo").val();

		var ListaErros = "";
		if ( AtivoAtual == "" ) ListaErros = ListaErros + " - Ativo Atual<br/>";
		if ( AtivoNovo == ""  ) ListaErros = ListaErros + " - Ativo Novo<br/>";

		if ( ListaErros != "" ){
			fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, "Os seguintes campos não estão preenchido: <br/>"+ListaErros);
			return false;
		}

		return true;

	} catch (e) {
		fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		return false;
	}
}

function iniciarAnimacaoSalvarTroca() {
    $("#iSalvarTroca").removeClass("fa-check");
    $("#iSalvarTroca").addClass("fa-spinner");
    $("#iSalvarTroca").addClass("fa-pulse");
    $("#BtnModalDetalheOperTrocaSalvar").addClass("disabled");
}

function finalizarAnimacaoSalvarTroca() {
   $("#iSalvarTroca").removeClass("fa-spinner");
   $("#iSalvarTroca").removeClass("fa-pulse");
   $("#iSalvarTroca").addClass("fa-check");
   $("#BtnModalDetalheOperTrocaSalvar").removeClass("disabled");
}

function fSalvarDadosOperTroca( urlPadrao ){
	try {

		if ( !fValidarDadosOperTroca() ) return;

		iniciarAnimacaoSalvarTroca();

		var CodAtivoAtual   = $("#selDetOperTrocaAtivoAtual").val();
		var CodAtivoNovo    = $("#selDetOperTrocaAtivoNovo").val();

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "operacoes/salvartroca",
			data    : { CodAtivoAtual : CodAtivoAtual, CodAtivoNovo : CodAtivoNovo, },
			success: function(result) {
                finalizarAnimacaoSalvarTroca();
                var resultado = result.data.Resultado;
                var mensagem = result.data.Mensagem;
                if (resultado == "NSESSAO") {
                    $(location).attr('href', urlPadrao + '/login');
                    return false;
                } else if (resultado == "NOK") {
                    fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_AVISO, mensagem);
                    return;
                } else if (resultado == "FALHA") {
                    fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
                    return;
                } else if (resultado == "OK") {
                    $("#PopModalDetalheOperTroca").modal("hide");
                    fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
                    fCarregarGrid( urlPadrao );
                } else {
                    fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, mensagem);
                    return;
                }
			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				finalizarAnimacaoSalvarTroca();
				fCriarAlerta("AreaAlertaModalCadOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText //MSG_ALERTA_ERRO
				return;
			}
		});

	} catch (e) {
		finalizarAnimacaoSalvarTroca();
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
		return;
	}
}