
//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

$(document).ready(function() {

	 promise = new Promise( (resolve, reject) => {
		
		//$(this).attr("title", ":: TnB - Proventos ::");
		$("#MnPrincRedimentos").addClass("active open");		
		
		fLimparAreaAlertaPrinc();
		fLimparAreaAlertaModalCad();
		fLimparAreaAlertaModalExc();
		fLimparAreaAlerta("AreaAlertaModalCadProv");
			
		$("#txtDivQuant").bind("keyup change",      function(){ fCalcularDividendo(); } );
		$("#txtDivPreco").bind("keyup change",      function(){ fCalcularDividendo(); } );
		$("#selDivTipo").bind("change",             function(){ fMostrarCalcVlrLiq(); fMostrarValorBruto(); fCalcularDividendo(); } );
		$("#txtDivCalcVlrLiq").bind("change",       function(){ fMostrarValorBruto(); fCalcularDividendo(); } );
		$("#txtDivPrecoBruto" ).unbind( "keyup"  );
		$("#txtDivPrecoBruto" ).unbind( "change" );

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

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

async function iniciarAnimacaoPesquisar() {

	 promise = new Promise( (resolve, reject) => {

		$("#iRefresh").addClass("fa-spin");
		$("#btnRendPesquisar").addClass("disabled");

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
			$("#btnRendPesquisar").removeClass("disabled");

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

			$("#txtIdRendDel").val(     ""               );
			$("#selRendAtivo").val(     ""               );
			$("#selRendTipo").val(      ""               );
			$("#txtRendDataIni").val(   fDataPrimeira()  );
			$("#txtRendDataFim").val(   ""               ); 
			fLimparSomenteGrid(         urlPadrao        );	

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

			finalizarAnimacaoPesquisa();
			
			$("th").addClass('text-center');

			$('#Grid').dataTable().fnClearTable();
			$("#Grid").dataTable({ bDestroy: true }).fnDestroy();

			$('#Grid').DataTable( {
			    data: [],
				oLanguage: fTraduzirGrid(), 
				aoColumns: [
					{ bSortable: true, sWidth: "50px", targets: 0 }, //  0-DataEx
					{ bSortable: true, sWidth: "50px", targets: 1 }, //  1-DataPagto
					{ bSortable: true, sWidth: "50px", targets: 2 }, //  2-Ativo
					{ bSortable: true, sWidth: "50px", targets: 3 }, //  3-Tipo
					{ bSortable: true, sWidth: "50px", targets: 4 }, //  4-Corretora
					{ bSortable: true, sWidth: "50px", targets: 5 }, //  5-Quant
					{ bSortable: true, sWidth: "50px", targets: 6 }, //  6-Preco 
					{ bSortable: true, sWidth: "50px", targets: 7 }, //  7-Total
					{ visible  : false,                targets: 8 }, //  8-IdRend
					{ visible  : false,                targets: 9 }, //  9-SitRend
					{ bSortable: true, sWidth: "50px", targets:10 }  // 10-Acao
				],
	            order: [[ 1, "desc" ], [ 2, "desc" ]],
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
						{ bSortable: true, sWidth: "20px", targets: 0 ,  //  0-DataEx
							render: function ( data, type, row ) { 
								if ( type == "display") return colcarFormacataoData(row[0]);//  0-DataEx
								return data;
							} 
						}, //  0-DataEx
						{ bSortable: true, sWidth: "20px", targets: 1 , //  1-DataPagtoa
							render: function ( data, type, row ) { 
								if ( type == "display") return colcarFormacataoData(row[1]); //  1-DataPagto
								return data;
							} 
						}, //  1-DataPagto
						{ bSortable: true, sWidth: "10px", targets: 2 }, //  2-Ativo
						{ bSortable: true, sWidth: "40px", targets: 3 ,  //  3-Tipo
							render: function ( data, type, row ) { 
								if ( type == "display") {
									Tipo   = row[3]; //  3-Tipo
									     if ( Tipo == "DIVIDENDOS"     ) return '<span style="font-size:12px;" class="badge badge-success">'+Tipo+'</span>'
									else if ( Tipo == "JRS CAP PRÓPRIO") return '<span style="font-size:12px;" class="badge badge-primary">'+Tipo+'</span>'; 
									else if ( Tipo == "REST CAP DIN"   ) return '<span style="font-size:12px;" class="badge badge-danger">'+Tipo+'</span>'; 
									else if ( Tipo == "RENDIMENTO"     ) return '<span style="font-size:12px;" class="badge badge-warning">'+Tipo+'</span>'; 
									else                                 return '<span style="font-size:12px;" class="badge badge-default">'+Tipo+'</span>'; 
								}
								return data;
							}
						}, //  3-Tipo
						{ bSortable: true, sWidth: "80px", targets: 4 }, //  4-Corretora
						{ bSortable: true, sWidth: "15px", targets: 5 ,  //  5-Quant
							render: function ( data, type, row ) { 
								if ( type == "display") return colcarFormacataoInteiro(row[5]); //  5-Quant
								return data;
							} 	
						}, //  5-Quant
						{ bSortable: true, sWidth: "30px", targets: 6,   //  6-Preco
							render: function ( data, type, row ) { 
								if ( type == "display") return "R$ " + row[6]; //  6-Preco 
								return data;
							} 				 
						}, //  6-Preco 
						{ bSortable: true, sWidth: "30px", targets: 7 ,   //  7-Total
							render: function ( data, type, row ) { 
								if ( type == "display") return "R$ " + row[7]; //  7-Total
								return data;
							} 				 
						}, //  7-Total
						{ visible  : false,                targets: 8 }, //  8-IdRend
						{ visible  : false,                targets: 9 }, //  9-SitRend
						{ bSortable: true, sWidth: "30px", targets:10,   //  10-Acao
							render: function ( data, type, row ) {
								
								var btnApv = "";
								var btnEdt = "";
								var btnDel = "";
								var btnDis = '';

								if ( type == "display") {
									
									IdRend   = row[8]; // 8-IdRend
									CodAtivo = row[2]; // 2-Ativo
									SitRend  = row[9]; // 9-SitRend

									if ( SitRend != 'B'  ) btnDis = ' disabled';
									
									btnApv += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';

									btnApv += '<a class="btn btn-sm btn-success btn-icon btn-icon-mini btn-round btn-simple'+btnDis+'"'+btnDis+' style="font-size:0.5rem; " title="Aprovar Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAprovarProventos( \''+urlPadrao+'\', \''+IdRend+'\', \''+CodAtivo+'\' );">';
									btnApv += '   <i class="fa fa-check fa-lg" aria-hidden="true"></i> ';
									btnApv += '</a>';

									btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAbrirModalDetalheRend( \''+urlPadrao+'\', \''+IdRend+'\', \''+CodAtivo+'\', \'Alterar\' );">';
									btnEdt += '   <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> ';
									btnEdt += '</a>';
									
									btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Excluir Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fChamarPagExclusaoRend( \''+IdRend+'\', \''+CodAtivo+'\' );">';
									btnDel += '   <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ';
									btnDel += '</a>';
									
									btnDel += '</div>';

								}
								
								return btnApv + '&nbsp;' + btnEdt + '&nbsp;' + btnDel;
								
							} 
						} //  10-Acao
		          ],
		          createdRow : function(row,data,dataIndex) {
		            $('td', row).addClass('text-center');
		          }, //createdRow
		          initComplete: function( settings, json ) {
					finalizarAnimacaoPesquisa();
		          },
		            order: [[ 1, "desc" ], [ 2, "desc" ]],
					dom: 'frtBpi', //Bfrtip //frtBip  //frtBpi
					buttons: [  
						  {
							 extend:    'excelHtml5',
							 text:      '<i class="fa fa-file-excel-o"></i> Excel',
							 className: 'btn btn-outline-default btn-sm',
							 title: NOME_PROJETO + ' - Proventos',
							 titleAttr: 'Excel',
							 exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ] },
							 customizeData: function (data) {
		                        for (var i = 0; i < data.body.length; i++) {
		                            for (var j = 0; j < data.body[i].length; j++) {
		                                if (j == 5) data.body[i][j] = '\u200C' + data.body[i][j]; // Formatando a Coluna = 5-Quant
		                            }
		                        }
		                    } 
						  }, 
						  {
							extend: 'csvHtml5',
							charset: 'UTF-8',
							fieldSeparator: ';',
							titleAttr: 'CSV',
							text:      '<i class="fa fa-file-o"></i> CSV',
							className: 'btn btn-outline-default btn-sm',
							title: NOME_PROJETO + ' - Proventos',
							bom: true,
							exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ] } //orthogonal: 'export',
						  },
						  {
							extend: 'pdfHtml5',
							text:      '<i class="fa fa-file-pdf-o"></i> PDF',
							className: 'btn btn-default btn-sm',
							titleAttr: 'PDF',
							title: NOME_PROJETO + ' - Proventos', 
							pageSize: 'A3',
							alignment: 'center',
							exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ] }, //orthogonal: 'export',
							footer: true,
							customize: function (doc) { 
								doc.defaultStyle.fontSize = 12; 
								doc.styles.tableHeader.fontSize = 14; 
							}
						  },
						  {
							extend: 'print',
							text:      '<i class="fa fa-print"></i> Imprimir',
							title: NOME_PROJETO + ' - Proventos',
							titleAttr: 'Imprimir',
							className: 'btn btn-default btn-sm',
							exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ] } //orthogonal: 'export',
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
					fLimparSomenteGrid( urlPadrao );
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
		if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fCarregarGrid( urlPadrao ){
  try {   

		 promise = new Promise( (resolve, reject) => {


            fLimparAreaAlertaPrinc();

            $('#Grid').dataTable().fnClearTable();
            $("#Grid").dataTable({ bDestroy: true }).fnDestroy();

            finalizarAnimacaoPesquisa();
            iniciarAnimacaoPesquisar();

            var CodAtivo  = $("#selRendAtivo").val().trim();
            var TipoRend  = $("#selRendTipo").val().trim();
            var DataIni   = $("#txtRendDataIni").val().trim();
            var DataFim   = $("#txtRendDataFim").val().trim();
            var Corretora = ""; //$("#selRendCorretora").val().trim();

            DataIni = tirarFormacataoData(DataIni);
            DataFim = tirarFormacataoData(DataFim);

            $.ajax({
                cache   : "false",
                dataType: "json",
                async   : true,
                type    : "POST",
                url     : urlPadrao + "proventos/grid",
                data: {
                    CodAtivo  : CodAtivo,
                    TipoRend  : TipoRend,
                    Corretora : Corretora,
                    DataIni   : DataIni,
                    DataFim   : DataFim
                },
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
                error: function(data) {
                    finalizarAnimacaoPesquisa();
                    fLimparSomenteGrid( urlPadrao );
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
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});
		
    } catch (e) {
		finalizarAnimacaoPesquisa();
		fLimparSomenteGrid( urlPadrao );
		if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fAbrirModalDetalheRendImportarProv(urlPadrao) {
	try {

		fLimparAreaAlerta("AreaAlertaModalImportProv");
		
		var DivListImport = $("#AreaTableModalImportProv");
		DivListImport.html( "" );

		$("#PopModalImportCSVProv").modal({backdrop: "static"});

    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }	
}

async function iniciarAnimacaoImportar() {

		 promise = new Promise( (resolve, reject) => {

		    //$("#iImportar").removeClass("fa fa-upload");
		    $("#iImportar").addClass("fa-spinner");
		    $("#iImportar").addClass("fa-pulse");

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

async function finalizarAnimacaImportar() {

		 promise = new Promise( (resolve, reject) => {

		   $("#iImportar").removeClass("fa-spinner");
		   $("#iImportar").removeClass("fa-pulse");
		   $("#iImportar").addClass("fa fa-upload"); 
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

function fImportarCSVProv(urlPadrao) {
	try {

	 finalizarAnimacaImportar();
	 fLimparAreaAlerta("AreaAlertaModalImportProv");

	 var DivListImport = $("#AreaTableModalImportProv");
	 DivListImport.html( "" );
	  
	  var filePath = $("#arquivo");
	  
	  if ( filePath.val().trim() == '' ) {
		fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_AVISO, 'Nenhum arquivo selecionado para importação.');
		return false;
	  }

	  var fileType = ".csv";
	  var regex    = new RegExp("([a-zA-Z0-9\s_\\.\-:])+("+ fileType + ")$");
	  if ( !regex.test( filePath.val().toLowerCase() ) ) {
		fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_AVISO, 'Tipo de Arquivo inválido para importação.');
		return false;
	  }

	  iniciarAnimacaoImportar();
  
	  var formData = new FormData(); 
	  formData.append("arquivo", filePath[0].files[0] );
  
	  $.ajax({
		dataType: "json", 
		type: "POST",
		url: urlPadrao + "proventos/importarcsv",
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
			fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_AVISO, mensagem);
			return false;
		  } else if (resultado == "FALHA") {
			fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_ERRO, mensagem);
			return;
		  } else if (resultado == "OK") {
			
			filePath.val('');
			fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_SUCESSO, mensagem);

			if ( lista.length > 0 ){

				var content = '';
				content += '<hr />';

				content += '<div class="form-group">';
				content += '  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">';
				content += '    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fExcluirTodosDadosRendimento( \''+urlPadrao+'\', );"> ';
				content += '       <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ';
				content += '    </a>';
				content += '  </div>';
				content += '</div>';

				content += '<div class="table-responsive">';
				content += '<table id="GridImport" border="0" style="font-size: 11px" class="table table-sm table-hover table-condensed" cellspacing="0" width="100%">';
				content += '  <thead>';
				content += '    <tr style="font-size: 11px" class="bg-secondary text-white text-center">';
				content += '      <th style="width:2px;">Linha</th>'; //0-Linha
				content += '      <th style="width:12px;">Data Ex</th>';//  1-Data Ex
				content += '      <th style="width:12px;">Data Pagto</th>';//  2-Data Pagto
				content += '      <th style="width:15px;">Tipo</th>';//  3-Tipo
				content += '      <th style="width:5px;">Ativo</th>';//  4-Ativo
				content += '      <th style="width:5px;">Quant.</th>';//  5-Quant
				content += '      <th style="width:15px;">Preço Bruto</th>';// 6-Preco Bruto
				content += '      <th style="width:15px;">Preço Líquido</th>';//  7-Preco Líquido
				content += '      <th style="width:12px;">Situação</th>';// 8-Situação
				content += '      <th style="width:10px;display: none; ">IdProv</th>';// 9-IdProv
				content += '      <th style="width:2px;">Ação</th>';// 10-Situação
				content += '    </tr>';
				content += '  </thead>';

				content += '  <tbody>';
				$.each(lista, function (index, value) {

					CodAtivo = value[3]; //  3-Ativo
					IdProv   = value[8]; // 8-IdProv

					var btnDel = "";
					var btnDis = ( (value[7] == 'Importado') ? '' : ' disabled');

					btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple'+btnDis+'"'+btnDis+' style="font-size:0.5rem;" title="Excluir Provento '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
					btnDel += '   onclick="fExcluirDadosRendimento( \''+urlPadrao+'\', \''+IdProv+'\', \''+CodAtivo+'\' );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ';
					btnDel += '</a>';
					
					content += '    <tr style="font-size: 10px" id="TrImport'+IdProv+'" class="text-center ' + ( (value[7] == 'Importado') ? 'text-success' : 'text-danger') +'"> ';
					content += '      <td>'+colcarFormacataoInteiro(value[9].trim())+'</td>'; // 9-NumLinha
					content += '      <td>'+colcarFormacataoData( value[0] )+'</td>'; //  0-Data Ex
					content += '      <td>'+colcarFormacataoData( value[1] )+'</td>'; //  1-Data Pagto
					content += '      <td>'+value[2]+'</td>'; //  2-Tipo
					content += '      <td>'+value[3]+'</td>'; //  3-Ativo
					content += '      <td>'+colcarFormacataoInteiro(value[4])+'</td>';//  4-Quant
					content += '      <td>R$ '+value[5]+'</td>'; //  5-Preco Bruto
					content += '      <td>R$ '+value[6]+'</td>'; //  6-Preco Líquido
					content += '      <td>'+value[7]+'</td>'; // 7-Situação
					content += '      <td style="display: none;">'+value[8]+'</td>'; // 8-IdProv
					content += '      <td>'+btnDel+'</td>'; //Ação
					content += '    </tr>';

				}); 

				content += '  </tbody>';
				content += '</table>';
				content += '</div>';

				content += '<div class="form-group">';
				content += '  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">';
				content += '    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fExcluirTodosDadosRendimento( \''+urlPadrao+'\', );"> ';
				content += '       <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ';
				content += '    </a>';
				content += '  </div>';
				content += '</div>';

				DivListImport.append( content );
				buscar_todos_codigos_proventos(urlPadrao, 'selRendAtivo', false, true, false, true);
				buscar_todos_codigos_comprados_para_proventos(urlPadrao, 'selDivAtivo', false, false, true, false);
			}

			return true;
		  } else {
			finalizarAnimacaImportar();
			fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_ERRO, mensagem);
			return false;
		  }
		},
		error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
			finalizarAnimacaImportar();
			fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); // request.responseText //MSG_ALERTA_ERRO
		}
	  });

	} catch (e) {
		finalizarAnimacaImportar();
		fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}

async function fExcluirTodosDadosRendimento(urlPadrao) {
	try {

		 promise = new Promise( (resolve, reject) => {

			fLimparAreaAlerta("AreaAlertaModalImportProv");

			$('#GridImport > tbody  > tr').each(function() {
				var CodAtivo = $(this).find("td").eq(4).html(); // 4-Ativo
				var IdProv   = $(this).find("td").eq(9).html(); // 9-IdProv
				fExcluirDadosRendimento( urlPadrao, IdProv, CodAtivo );
				//fLimparAreaAlerta("AreaAlertaModalImportProv");
			});
			
			buscar_todos_codigos_proventos(urlPadrao, 'selRendAtivo', false, true, false, true);
			buscar_todos_codigos_comprados_para_proventos(urlPadrao, 'selDivAtivo', false, false, true, false);

			//fLimparAreaAlerta("AreaAlertaModalImportProv");

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
		fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}  

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------
 
function fAbrirModalDetalheRendImportarProvCEI(urlPadrao) {
	try {

		fLimparAreaAlerta("AreaAlertaModalImportProvCEI");
		
		$("#TxtDadosImportCEI").val( "" );
		$("#AreaTableModalImportProvCEI").html( "" );

		$("#PopModalImportProvCEI").modal({backdrop: "static"});

    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }	
}

async function fExcluirTodosDadosRendimentoCEI(urlPadrao) {
	try {

		 promise = new Promise( (resolve, reject) => {


			fLimparAreaAlerta("AreaAlertaModalImportProvCEI");

			$('#GridImport > tbody  > tr').each(function() {
				var CodAtivo = $(this).find("td").eq(4).html(); // 4-Ativo
				var IdProv   = $(this).find("td").eq(9).html(); // 9-IdProv
				fExcluirDadosRendimento( urlPadrao, IdProv, CodAtivo );
				//fLimparAreaAlerta("AreaAlertaModalImportProvCEI");
			});
			
			buscar_todos_codigos_proventos(urlPadrao, 'selRendAtivo', false, true, false, true);
			buscar_todos_codigos_comprados_para_proventos(urlPadrao, 'selDivAtivo', false, false, true, false);

			//fLimparAreaAlerta("AreaAlertaModalImportProvCEI");

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
		fCriarAlerta("AreaAlertaModalImportProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
} 

async function iniciarAnimacaoImportarCEI() {

		 promise = new Promise( (resolve, reject) => {

		    //$("#iImportarCEI").removeClass("fa fa-upload");
		    $("#iImportarCEI").addClass("fa-spinner");
		    $("#iImportarCEI").addClass("fa-pulse");

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

async function finalizarAnimacaImportarCEI() {

		 promise = new Promise( (resolve, reject) => {

			   $("#iImportarCEI").removeClass("fa-spinner");
			   $("#iImportarCEI").removeClass("fa-pulse");
			   $("#iImportarCEI").addClass("fa fa-upload"); 

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

function fImportarProvCEI(urlPadrao) {
	try {

	 finalizarAnimacaImportarCEI();
	 fLimparAreaAlerta("AreaAlertaModalImportProvCEI");

	 var DivListImport = $("#AreaTableModalImportProvCEI");
	 DivListImport.html( "" );
	  
	 var TxtDadosImportCEI = $("#TxtDadosImportCEI").val().trim();
	  
	 if ( TxtDadosImportCEI == '' ) {
	   fCriarAlerta("AreaAlertaModalImportProvCEI", TP_ALERTA_AVISO, 'Dados da CEI não informado');
	   return false;
	 }

	  iniciarAnimacaoImportarCEI();
  
	  $.ajax({
		dataType: "json", 
		type: "POST",
		async   : true,
		url: urlPadrao + "proventos/importarcei",
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
			fCriarAlerta("AreaAlertaModalImportProvCEI", TP_ALERTA_AVISO, mensagem);
			return false;
		  } else if (resultado == "FALHA") {
			fCriarAlerta("AreaAlertaModalImportProvCEI", TP_ALERTA_ERRO, mensagem);
			return;
		  } else if (resultado == "OK") {
			
			fCriarAlerta("AreaAlertaModalImportProvCEI", TP_ALERTA_SUCESSO, mensagem);

			if ( lista.length > 0 ){

				var content = '';
				content += '<hr />';

				content += '<div class="form-group">';
				content += '  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">';
				content += '    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fExcluirTodosDadosRendimentoCEI( \''+urlPadrao+'\', );"> ';
				content += '       <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ';
				content += '    </a>';
				content += '  </div>';
				content += '</div>';
				
				content += '<div class="table-responsive">';
				content += '<table id="GridImport" border="0" style="font-size: 11px" class="table table-sm table-hover table-condensed" cellspacing="0" width="100%">';
				content += '    <col width="10">';//Linha
				content += '  <thead>';
				content += '    <tr style="font-size: 11px" class="bg-secondary text-white text-center">';
				content += '      <th style="width:2px;">Linha</th>'; //0-Linha
				content += '      <th style="width:12px;">Data Ex</th>';//  1-Data Ex
				content += '      <th style="width:12px;">Data Pagto</th>';//  2-Data Pagto
				content += '      <th style="width:15px;">Tipo</th>';//  3-Tipo
				content += '      <th style="width:5px;">Ativo</th>';//  4-Ativo
				content += '      <th style="width:5px;">Quant.</th>';//  5-Quant
				content += '      <th style="width:15px;">Preço Bruto</th>';// 6-Preco Bruto
				content += '      <th style="width:15px;">Preço Líquido</th>';//  7-Preco Líquido
				content += '      <th style="width:12px;">Situação</th>';// 8-Situação
				content += '      <th style="width:10px;display: none; ">IdProv</th>';// 9-IdProv
				content += '      <th style="width:2px;">Ação</th>';// 10-Situação
				content += '    </tr>';
				content += '  </thead>';

				content += '  <tbody>';
				$.each(lista, function (index, value) {

					CodAtivo = value[3]; //  3-Ativo
					IdProv   = value[8]; // 8-IdProv

					var btnDel = "";
					var btnDis = ( (value[7] == 'Importado') ? '' : ' disabled');

					btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple'+btnDis+'"'+btnDis+' style="font-size:9px;" title="Excluir Provento '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" ';
					btnDel += '   onclick="fExcluirDadosRendimento( \''+urlPadrao+'\', \''+IdProv+'\', \''+CodAtivo+'\' );"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ';
					btnDel += '</a>';
					
					content += '    <tr style="font-size: 10px" id="TrImport'+IdProv+'" class="text-center ' + ( (value[7] == 'Importado') ? 'text-success' : 'text-danger') +'"> ';
					content += '      <td>'+colcarFormacataoInteiro(value[9].trim())+'</td>'; // 9-NumLinha
					content += '      <td>'+colcarFormacataoData( value[0] )+'</td>'; //  0-Data Ex
					content += '      <td>'+colcarFormacataoData( value[1] )+'</td>'; //  1-Data Pagto
					content += '      <td>'+value[2]+'</td>'; //  2-Tipo
					content += '      <td>'+value[3]+'</td>'; //  3-Ativo
					content += '      <td>'+colcarFormacataoInteiro(value[4])+'</td>';//  4-Quant
					content += '      <td>R$ '+value[5]+'</td>'; //  5-Preco Bruto
					content += '      <td>R$ '+value[6]+'</td>'; //  6-Preco Líquido
					content += '      <td>'+value[7]+'</td>'; // 7-Situação
					content += '      <td style="display: none;">'+value[8]+'</td>'; // 8-IdProv
					content += '      <td>'+btnDel+'</td>'; //Ação
					content += '    </tr>';

				}); 

				content += '  </tbody>';
				content += '</table>';
				content += '</div>';

				content += '<div class="form-group">';
				content += '  <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 text-right">';
				content += '    <a class="btn btn-sm btn-danger btn-round btn-simple text-center" style="font-size:14px;" title="Excluir Todos os Ativo Importados" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fExcluirTodosDadosRendimentoCEI( \''+urlPadrao+'\', );"> ';
				content += '       <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> Excluir Todos ';
				content += '    </a>';
				content += '  </div>';
				content += '</div>';

				DivListImport.append( content );
				buscar_todos_codigos_proventos(urlPadrao, 'selRendAtivo', false, true, false, true);
				buscar_todos_codigos_comprados_para_proventos(urlPadrao, 'selDivAtivo', false, false, true, false);
			}

			return true;
		  } else {
			finalizarAnimacaImportar();
			fCriarAlerta("AreaAlertaModalImportProvCEI", TP_ALERTA_ERRO, mensagem);
			return false;
		  }
		},
		error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
			finalizarAnimacaImportar();
			fCriarAlerta("AreaAlertaModalImportProvCEI", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); // request.responseText //MSG_ALERTA_ERRO
		}
	  });

	} catch (e) {
		finalizarAnimacaImportar();
		fCriarAlerta("AreaAlertaModalImportProvCEI", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
	}
}


//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fAbrirModalLimparTodasRend() {
    try {

      fLimparAreaAlerta("AreaAlertaModalExcTds");
      $("#PopModalDelTdsRend").modal({backdrop: "static"}); 

    } catch (e) {
        $("#PopModalDelTdsRend").modal("hide");
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

async function fExcluirTodosRendimento( urlPadrao ) {
    try {

		 promise = new Promise( (resolve, reject) => {

			fLimparAreaAlerta("AreaAlertaModalExcTds");
		  
			$.ajax({
				dataType: "json",
				type: "post",
				url : urlPadrao + "proventos/excluirtudo",
				data: {},
				success: function (result) {
					
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
						$("#PopModalDelTdsRend").modal("hide");
						fCriarAlertaPrinc(TP_ALERTA_SUCESSO, mensagem); 
						fCarregarGrid( urlPadrao );
						fCarregarCodigoAtivos( urlPadrao );
						buscar_todos_codigos_proventos(urlPadrao, 'selRendAtivo', false, true, false, true);
						buscar_todos_codigos_comprados_para_proventos(urlPadrao, 'selDivAtivo', false, false, true, false);
						return true;
					} else {
						fCriarAlerta("AreaAlertaModalExcTds", TP_ALERTA_ERRO, mensagem);
						return false;
					}
					
				},
				error: function (data) {
					$("#PopModalDelTdsRend").modal("hide");
					fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
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
        $("#PopModalDelTdsRend").modal("hide");
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }	
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------