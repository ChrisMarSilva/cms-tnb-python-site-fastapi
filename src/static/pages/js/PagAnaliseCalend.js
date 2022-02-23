
function iniciarAnimacaoPesquisarAnaliseCalProv() {
	$("#iRefreshCalProv").addClass("fa-spin");
	$("#btnAnaliseCalProvPesquisar").addClass("disabled");
	//$("#btnAnaliseCalProvLimpar").addClass("disabled");
}

function finalizarAnimacaoPesquisaAnaliseCalProv() {
	$("#iRefreshCalProv").removeClass("fa-spin");
	$("#btnAnaliseCalProvPesquisar").removeClass("disabled");
	//$("#btnAnaliseCalProvLimpar").removeClass("disabled");
}

function fLimparGridAnaliseCalProv( urlPadrao ){	
		
	fLimparAreaAlerta("AreaAlertaPrincAnaliseCalProv");
	fLimparSomenteGridAnaliseCalProv( urlPadrao );
	
}

async function fLimparSomenteGridAnaliseCalProv( urlPadrao ){
	try {	

		 promise = new Promise( (resolve, reject) => {
	
			finalizarAnimacaoPesquisaAnaliseCalProv();
  
			$("th").addClass('text-center');
			
			$('#GridAnaliseCalProv').dataTable().fnClearTable();
			$("#GridAnaliseCalProv").dataTable({ bDestroy: true }).fnDestroy();

			
			$('#GridAnaliseCalProv').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: true, sWidth: "50px", targets:  0 }, //  0-Ativo
					{ bSortable: true, sWidth: "50px", targets:  1 }, //  1-JAN
					{ bSortable: true, sWidth: "50px", targets:  2 }, //  2-FEV
					{ bSortable: true, sWidth: "50px", targets:  3 }, //  3-MAR
					{ bSortable: true, sWidth: "50px", targets:  4 }, //  4-ABR
					{ bSortable: true, sWidth: "50px", targets:  5 }, //  5-MAI
					{ bSortable: true, sWidth: "50px", targets:  6 }, //  6-JUN
					{ bSortable: true, sWidth: "50px", targets:  7 }, //  7-JUL
					{ bSortable: true, sWidth: "50px", targets:  8 }, //  8-AGO
					{ bSortable: true, sWidth: "50px", targets:  9 }, //  9-SET
					{ bSortable: true, sWidth: "50px", targets: 10 }, // 10-OUT
					{ bSortable: true, sWidth: "50px", targets: 11 }, // 11-NOV
					{ bSortable: true, sWidth: "50px", targets: 12 }, // 12-DEZ
					{ bSortable: true, sWidth: "50px", targets: 13 }, // 13-TOTAL
					{ bSortable: true, sWidth: "50px", targets: 14 }  // 14-MEDIA
				],
				order: [],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				searchable: false,
				orderable: false,
				bAutoWidth: false,
				bPaginate: false,
				ordering: false
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
		fCriarAlerta("AreaAlertaPrincAnaliseCalProv",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

async function fMontarGridAnaliseCalProv( urlPadrao, dataSet, ano ){	
	try { 

		 promise = new Promise( (resolve, reject) => {
	
			$('#GridAnaliseCalProv').dataTable().fnClearTable();
			$("#GridAnaliseCalProv").dataTable({ bDestroy: true }).fnDestroy();	
	
			$('#GridAnaliseCalProv').DataTable( {
			  processing: true,
			  serverSide: false,
			  iDisplayLength: 10,
			  oLanguage: fTraduzirGrid(), 
			  data: dataSet,
			  aoColumns: [
				  { bSortable: true, sWidth: "50px", targets:  0 }, //  0-CodAtivo
				  { bSortable: true, sWidth: "50px", targets:  1,   //  1-JAN
					  render: function ( data, type, row ) {
						  var IdCampo = 1;  //  1-JAN
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 				
				  }, //  1-JAN
				  { bSortable: true, sWidth: "50px", targets:  2,  //  2-FEV
					  render: function ( data, type, row ) {
						  var IdCampo = 2;  //  2-FEV
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 				
				  }, //  2-FEV
				  { bSortable: true, sWidth: "50px", targets:  3,  //  3-MAR
					  render: function ( data, type, row ) {
						  var IdCampo = 3; //  3-MAR
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 				
				  }, //  3-MAR
				  { bSortable: true, sWidth: "50px", targets:  4,  //  4-ABR
					  render: function ( data, type, row ) {
						  var IdCampo = 4; //  4-ABR
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 				
				  }, //  4-ABR
				  { bSortable: true, sWidth: "50px", targets:  5,  //  5-MAI
					  render: function ( data, type, row ) {
						  var IdCampo = 5; //  5-MAI
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 				
				  }, //  5-MAI
				  { bSortable: true, sWidth: "50px", targets:  6, //  6-JUN  
					  render: function ( data, type, row ) {
						  var IdCampo = 6; //  6-JUN 
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 				
				  }, //  6-JUN
				  { bSortable: true, sWidth: "50px", targets:  7, //  7-JUL 
					  render: function ( data, type, row ) {
						  var IdCampo = 7; //  7-JUL 
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 				
				  }, //  7-JUL
				  { bSortable: true, sWidth: "50px", targets:  8, //  8-AGO 
					  render: function ( data, type, row ) {
						  var IdCampo = 8; //  8-AGO
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 				
				  }, //  8-AGO
				  { bSortable: true, sWidth: "50px", targets:  9,  //  9-SET
					  render: function ( data, type, row ) {
						  var IdCampo = 9; //  9-SET
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 				
				  }, //  9-SET
				  { bSortable: true, sWidth: "50px", targets: 10,  // 10-OUT
					  render: function ( data, type, row ) {
						  var IdCampo = 10; // 10-OUT
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 				
				  }, // 10-OUT
				  { bSortable: true, sWidth: "50px", targets: 11,  // 11-NOV
					  render: function ( data, type, row ) {
						  var IdCampo = 11; // 11-NOV
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 				
				  }, // 11-NOV
				  { bSortable: true, sWidth: "50px", targets: 12,   // 12-DEZ
					  render: function ( data, type, row ) {
						  var IdCampo = 12; // 12-DEZ
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 				
				  }, // 12-DEZ
				  { bSortable: true, sWidth: "50px", targets: 13,  // 13-TOTAL
					  render: function ( data, type, row ) {
						  var IdCampo = 13; // 13-TOTAL
						  if ( type == "display") {
							  if ( row[IdCampo] != "0,00")  return '<a class="text-dark font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+row[0]+'\', \''+ano+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
							  return row[IdCampo]; 
						  }
						  return data;
					  } 			
				  }, // 13-TOTAL
				  { bSortable: true, sWidth: "50px", targets: 14,  // 14-MEDIA
					  render: function ( data, type, row ) {
						  var IdCampo = 14; // 14-MEDIA
						  if ( type == "display") return row[IdCampo]; 
						  return data;
					  } 			
				  } // 14-MEDIA
			  ],
			  createdRow : function(row,data,dataIndex) {
  
				$('td', row).addClass('text-center');
  
				var CodAtivo = data[0]; //  0-CodAtivo
  
				if ( CodAtivo == "TOTAL" ){
					  $(row).addClass("table-secondary text-dark font-weight-bold");
					  $(row).css("height", "35");
				}else{
					  $('td', row).eq( 0).addClass('table-secondary text-dark font-weight-bold'); // 0-CodAtivo
					  $('td', row).eq(13).addClass('table-secondary text-dark font-weight-bold'); // 13-TOTAL
					  $('td', row).eq(14).addClass('table-secondary text-dark font-weight-bold'); // 14-MEDIA
					  //$(row).css("height", "30");
					  if ( data[ 1] != "0,00") $('td', row).eq( 1).addClass('text-success font-weight-bold'); 
					  if ( data[ 2] != "0,00") $('td', row).eq( 2).addClass('text-success font-weight-bold'); 
					  if ( data[ 3] != "0,00") $('td', row).eq( 3).addClass('text-success font-weight-bold'); 
					  if ( data[ 4] != "0,00") $('td', row).eq( 4).addClass('text-success font-weight-bold'); 
					  if ( data[ 5] != "0,00") $('td', row).eq( 5).addClass('text-success font-weight-bold'); 
					  if ( data[ 6] != "0,00") $('td', row).eq( 6).addClass('text-success font-weight-bold'); 
					  if ( data[ 7] != "0,00") $('td', row).eq( 7).addClass('text-success font-weight-bold'); 
					  if ( data[ 8] != "0,00") $('td', row).eq( 8).addClass('text-success font-weight-bold'); 
					  if ( data[ 9] != "0,00") $('td', row).eq( 9).addClass('text-success font-weight-bold'); 
					  if ( data[10] != "0,00") $('td', row).eq(10).addClass('text-success font-weight-bold'); 
					  if ( data[11] != "0,00") $('td', row).eq(11).addClass('text-success font-weight-bold'); 
					  if ( data[12] != "0,00") $('td', row).eq(12).addClass('text-success font-weight-bold'); 
				}
			  }, //createdRow
			  initComplete: function( settings, json ) {
				  finalizarAnimacaoPesquisaAnaliseCalProv();
			  }, //initComplete
				order: [],	
				dom: 'frtBpi',
				buttons: [  
					  {
						 extend:    'excelHtml5',
						 text:      '<i class="fa fa-file-excel-o"></i> Excel',
						 className: 'btn btn-outline-default btn-sm',
						 title: NOME_PROJETO + ' - Análise do Calendário de Proventos - Ano '+ano,
						 titleAttr: 'Excel',
						 exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ] } 
					  }, 
					  {
						extend: 'csvHtml5',
						charset: 'UTF-8',
						fieldSeparator: ';',
						titleAttr: 'CSV',
						text:      '<i class="fa fa-file-o"></i> CSV',
						className: 'btn btn-outline-default btn-sm',
						title: NOME_PROJETO + ' - Análise do Calendário de Proventos - Ano '+ano,
						bom: true,
						exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ] } 
					  },
					  {
						extend: 'pdfHtml5',
						text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						className: 'btn btn-default btn-sm',
						titleAttr: 'PDF',
						title: NOME_PROJETO + ' - Análise do Calendário de Proventos - Ano '+ano, 
						pageSize: 'A3',
						alignment: 'center',
						exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ] },
						footer: true,
						customize: function (doc) { 
							doc.defaultStyle.fontSize = 12; 
							doc.styles.tableHeader.fontSize = 14; 
						}
					  },
					  {
						extend: 'print',
						text:      '<i class="fa fa-print"></i> Imprimir',
						title: NOME_PROJETO + ' - Análise do Calendário de Proventos - Ano '+ano,
						titleAttr: 'Imprimir',
						className: 'btn btn-default btn-sm',
						exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ] }
					  }
				],
				bFilter: false,
				bInfo: false,
				bLengthChange: false,
				searchable: false,
				orderable: false,
				bAutoWidth: false,
				bPaginate: false,
				ordering: false
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
		  fLimparSomenteGridAnaliseCalProv( urlPadrao );
		  finalizarAnimacaoPesquisaAnaliseCalProv();
		if ( e.description != undefined ){ fCriarAlerta("AreaAlertaPrincAnaliseCalProv", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);  }
	  }
}  
  
async function fCarregarGridAnaliseCalProv( urlPadrao ){
	try {   

		 promise = new Promise( (resolve, reject) => {
	
			fLimparAreaAlerta("AreaAlertaPrincAnaliseCalProv");
  
			// $('#GridAnaliseCalProv').dataTable().fnClearTable();
			// $("#GridAnaliseCalProv").dataTable({ bDestroy: true }).fnDestroy();	
			
			finalizarAnimacaoPesquisaAnaliseCalProv();
			iniciarAnimacaoPesquisarAnaliseCalProv();
			
			var Ano = GetAnoAtual(); 
  
			if ( Ano == "" ){
			  fLimparSomenteGridAnaliseCalProv( urlPadrao );
			  fCriarAlerta("AreaAlertaPrincAnaliseCalProv", TP_ALERTA_AVISO, "Ano não Informado"); 
			  return false;
			}
			
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url: urlPadrao + "Analise/gridCalProv",
				data: { Ano : Ano },
				success: function(result) {
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
	
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fLimparSomenteGridAnaliseCalProv( urlPadrao );
						fCriarAlerta("AreaAlertaPrincAnaliseCalProv", TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						fLimparSomenteGridAnaliseCalProv( urlPadrao );
						fCriarAlerta("AreaAlertaPrincAnaliseCalProv", TP_ALERTA_AVISO, mensagem); 
						return;
					}else if (resultado == "OK") {
						fMontarGridAnaliseCalProv( urlPadrao, lista, Ano );
					} else{
						fLimparSomenteGridAnaliseCalProv( urlPadrao );
						fCriarAlerta("AreaAlertaPrincAnaliseCalProv", TP_ALERTA_AVISO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					fLimparSomenteGridAnaliseCalProv( urlPadrao );
					fCriarAlerta("AreaAlertaPrincAnaliseCalProv", TP_ALERTA_AVISO, MSG_ALERTA_ERRO); 
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
		fLimparSomenteGridAnaliseCalProv( urlPadrao );
		if ( e.description != undefined ){
		  fCriarAlerta("AreaAlertaPrincAnaliseCalProv", TP_ALERTA_AVISO, MSG_ALERTA_ERRO); 
		}
	  }
}
  
async function fAbrirModalDetalheAnaliseCalProv( urlPadrao, CodAtivo, Ano, Mes ){
	try {  

		 promise = new Promise( (resolve, reject) => {
	
			fLimparAreaAlertaPrinc();

			var DivGridModalDetalheAnaliseCalProv = $("#DivGridModalDetalheAnaliseCalProv");
			DivGridModalDetalheAnaliseCalProv.html("");
	
			if ( CodAtivo == "TOTAL" ) CodAtivo = "";
			if ( CodAtivo == "ACAO"  ) CodAtivo = "";
			if ( CodAtivo == "FII"   ) CodAtivo = "";
			if ( CodAtivo == "ETF"   ) CodAtivo = "";
			
			if ( Ano == ""      ) Ano = "9999";
			if ( Ano == "TOTAL" ) Ano = "9999";
	
			var DataIni = "";
			var DataFim = "";
			if ( Ano != "" && Ano != "TOTAL" && Mes == "13"  ){
				DataIni = Ano+"0101";
				DataFim = Ano+"1231";
			}
			if (  Ano != "" && Ano != "TOTAL" && Mes != "" && Mes != "13"  ){
				DataIni = Ano+("00" + Mes).slice(-2)+"01";
				DataFim = Ano+("00" + Mes).slice(-2)+"31";
			}
			
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "proventos/grid",
				data: { CodAtivo: CodAtivo, TipoRend: "", Corretora: "", DataIni: DataIni, DataFim: DataFim },
				success: function(result) {  
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
					
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						$("#PopModalDetalheAnaliseCalProv").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						$("#PopModalDetalheAnaliseCalProv").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					} else if (resultado == "OK") {
	
						var content = '';
						
						if ( lista.length > 0 ){
							
							content += '<table class="table table-sm table-hover table-condensed nowrap" style="font-size: 12px;" border="0" cellspacing="0" width="100%" style="margin: 0px;">';
							content += '  <thead>';
							content += '    <tr style="font-size: 12px;" class="thead-dark font-weight-bold"> ';
							content += '      <th>Data Ex.</th>';
							content += '      <th>Data Pagto</th>';
							content += '      <th>Código</th>';
							content += '      <th>Tipo</th>';
							content += '      <th>Quant.</th>';
							content += '      <th>Preço</th>';
							content += '      <th>Total</th>';
							content += '    </tr>';  
							content += '  </thead>';
							content += '  <tbody>';
							
							var ProvVlrTotal = 0.00;
							
							$.each(lista, function (index, value) {
	
								var ProvDataEx    = value[0]; // 0-DataEx
								var ProvDataPagto = value[1]; // 1-DataPagto
								var ProvCodAtivo  = value[2]; // 2-CodAtivo
								var ProvTipo      = value[3]; // 3-Tipo
								var ProvCorretora = value[4]; //  4-Corretora
								var ProvQuant     = value[5]; // 5-Quant
								var ProvPreco     = parseFloat( GetValorDecimal(value[6]) ); // 6-Preco
								var ProvTotal     = parseFloat( GetValorDecimal(value[7]) ); // 7-Total 
								var ProvId        = value[8]; //  8-IdRend
								var ProvSituacao  = value[8]; //  9-SitRend
								ProvVlrTotal     += ProvTotal;
	
								content += '    <tr class="text-center text-dark" > ';
								content += '      <td style="width:auto;">'+colcarFormacataoData(ProvDataEx)+'</td>';
								content += '      <td style="width:auto;">'+colcarFormacataoData(ProvDataPagto)+'</td>';
								content += '      <td class="font-weight-bold" style="width:auto;">'+ProvCodAtivo+'</td>';
								content += '      <td style="width:auto;">'+ProvTipo+'</td>';
								content += '      <td style="width:auto;">'+colcarFormacataoInteiro(ProvQuant)+'</td>';
								content += '      <td style="width:auto;">R$ '+fMascaraValor(ProvPreco)+'</td>';
								content += '      <td class="font-weight-bold" style="width:auto;">R$ '+fMascaraValor(ProvTotal)+'</td>';
								content += '    </tr>'; 
	
							}); //$.each(lista, function (index, value) {
													
							content += '    <tr style="font-size: 12px;" class="text-center text-dark font-weight-bold" > ';
							content += '      <td> </td>';
							content += '      <td> </td>';
							content += '      <td class="font-weight-bold" style="width:auto;">TOTAL</td>';
							content += '      <td> </td>';
							content += '      <td> </td>';
							content += '      <td> </td>';
							content += '      <td class="font-weight-bold" >R$ '+fMascaraValor(ProvVlrTotal)+'</td>';
							content += '    </tr>'; 
													
							content += '  </tbody>';
							content += '</table>';
	
						} // if ( lista.length > 0 ){
						else{
							content = 'Nenhum Provento encontrado para o Ativo no Período...';
						}
						
						DivGridModalDetalheAnaliseCalProv.html("");
						DivGridModalDetalheAnaliseCalProv.append( content );	
	
						$("#PopModalDetalheAnaliseCalProv").modal({backdrop: "static"});
						return true;
		   
					} else {
						$("#PopModalDetalheAnaliseCalProv").modal("hide");	
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					$("#PopModalDetalheAnaliseCalProv").modal("hide");	
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
		$("#PopModalDetalheAnaliseCalProv").modal("hide");	
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	}  
}	
