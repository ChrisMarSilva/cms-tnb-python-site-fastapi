
function iniciarAnimacaoPesquisarAnaliseCalProvAtivo() {
	$("#iRefreshCalendProvAtivo").addClass("fa-spin");
	$("#btnAnaliseCalendProvAtivoPesquisar").addClass("disabled");
    $("#txtFiltroAnaliseCalendProvAtivoAtivo").attr("disabled","disabled");
    fDefinirPadraoSelect('txtFiltroAnaliseCalendProvAtivoAtivo');
}

function finalizarAnimacaoPesquisaAnaliseCalProvAtivo() {
	$("#iRefreshCalendProvAtivo").removeClass("fa-spin");
	$("#btnAnaliseCalendProvAtivoPesquisar").removeClass("disabled");
    $("#txtFiltroAnaliseCalendProvAtivoAtivo").removeAttr("disabled");
    fDefinirPadraoSelect('txtFiltroAnaliseCalendProvAtivoAtivo');
}

function fLimparGridAnaliseCalendProvAtivo( urlPadrao ){	
		
	$("#txtFiltroAnaliseCalendProvAtivoAtivo").val("");
	fDefinirPadraoSelect('txtFiltroAnaliseCalendProvAtivoAtivo');
	
	fLimparAreaAlerta("AreaAlertaPrincAnaliseCalProvAtivo");
	fLimparSomenteGridAnaliseCalendProvAtivo( urlPadrao );
	
}

async function fLimparSomenteGridAnaliseCalendProvAtivo( urlPadrao ){
	try {	

		 promise = new Promise( (resolve, reject) => {
	
			finalizarAnimacaoPesquisaAnaliseCalProvAtivo();
  
			$("th").addClass('text-center');
			
			$('#GridAnaliseCalProvAtivo').dataTable().fnClearTable();
			$("#GridAnaliseCalProvAtivo").dataTable({ bDestroy: true }).fnDestroy();
			
			$('#GridAnaliseCalProvAtivo').DataTable( {
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
		fCriarAlerta("AreaAlertaPrincAnaliseCalProvAtivo",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

async function fMontarGridAnaliseCalProvAtivo( urlPadrao, dataSet, CodAtivoSel ){	
	try { 

		 promise = new Promise( (resolve, reject) => {

			var arAnos  = [];
			var arJAN   = [];
			var arFEV   = [];
			var arMAR   = [];
			var arABR   = [];
			var arMAI   = [];
			var arJUN   = [];
			var arJUL   = [];
			var arAGO   = [];
			var arSET   = [];
			var arOUT   = [];
			var arNOV   = [];
			var arDEZ   = [];
			var arTOTAL = [];
			var arMEDIA = [];
	
			  $('#GridAnaliseCalProvAtivo').DataTable( {
				processing: true,
				serverSide: false,
				iDisplayLength: 10,
				oLanguage: fTraduzirGrid(), 
				data: dataSet,
				aoColumns: [
					{ bSortable: true, sWidth: "50px", targets:  0 }, //  0-Ano
					{ bSortable: true, sWidth: "50px", targets:  1,   //  1-JAN
						render: function ( data, type, row ) {
							var IdCampo = 1;  //  1-JAN
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
								return row[IdCampo]; 
							}
							return data;
						} 				
					}, //  1-JAN
					{ bSortable: true, sWidth: "50px", targets:  2,  //  2-FEV
						render: function ( data, type, row ) {
							var IdCampo = 2;  //  2-FEV
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
								return row[IdCampo]; 
							}
							return data;
						} 				
					}, //  2-FEV
					{ bSortable: true, sWidth: "50px", targets:  3,  //  3-MAR
						render: function ( data, type, row ) {
							var IdCampo = 3; //  3-MAR
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
								return row[IdCampo]; 
							}
							return data;
						} 				
					}, //  3-MAR
					{ bSortable: true, sWidth: "50px", targets:  4,  //  4-ABR
						render: function ( data, type, row ) {
							var IdCampo = 4; //  4-ABR
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
								return row[IdCampo]; 
							}
							return data;
						} 				
					}, //  4-ABR
					{ bSortable: true, sWidth: "50px", targets:  5,  //  5-MAI
						render: function ( data, type, row ) {
							var IdCampo = 5; //  5-MAI
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
								return row[IdCampo]; 
							}
							return data;
						} 				
					}, //  5-MAI
					{ bSortable: true, sWidth: "50px", targets:  6, //  6-JUN  
						render: function ( data, type, row ) {
							var IdCampo = 6; //  6-JUN 
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
								return row[IdCampo]; 
							}
							return data;
						} 				
					}, //  6-JUN
					{ bSortable: true, sWidth: "50px", targets:  7, //  7-JUL 
						render: function ( data, type, row ) {
							var IdCampo = 7; //  7-JUL 
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
								return row[IdCampo]; 
							}
							return data;
						} 				
					}, //  7-JUL
					{ bSortable: true, sWidth: "50px", targets:  8, //  8-AGO 
						render: function ( data, type, row ) {
							var IdCampo = 8; //  8-AGO
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
								return row[IdCampo]; 
							}
							return data;
						} 				
					}, //  8-AGO
					{ bSortable: true, sWidth: "50px", targets:  9,  //  9-SET
						render: function ( data, type, row ) {
							var IdCampo = 9; //  9-SET
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
								return row[IdCampo]; 
							}
							return data;
						} 				
					}, //  9-SET
					{ bSortable: true, sWidth: "50px", targets: 10,  // 10-OUT
						render: function ( data, type, row ) {
							var IdCampo = 10; // 10-OUT
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
								return row[IdCampo]; 
							}
							return data;
						} 				
					}, // 10-OUT
					{ bSortable: true, sWidth: "50px", targets: 11,  // 11-NOV
						render: function ( data, type, row ) {
							var IdCampo = 11; // 11-NOV
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
								return row[IdCampo]; 
							}
							return data;
						} 				
					}, // 11-NOV
					{ bSortable: true, sWidth: "50px", targets: 12,   // 12-DEZ
						render: function ( data, type, row ) {
							var IdCampo = 12; // 12-DEZ
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-success font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
								return row[IdCampo]; 
							}
							return data;
						} 				
					}, // 12-DEZ
					{ bSortable: true, sWidth: "50px", targets: 13,  // 13-TOTAL
						render: function ( data, type, row ) {
							var IdCampo = 13; // 13-TOTAL
							if ( type == "display" && row[0] != "TOTAL" && row[0] != "MÉDIA" && row[0] != "RANKING") {
								if ( row[IdCampo] != "0,00")  return '<a class="text-dark font-weight-bold" style="text-decoration:none;" title="Clique Aqui para Detalhar os Proventos" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseCalProv( \''+urlPadrao+'\', \''+CodAtivoSel+'\', \''+row[0]+'\', \''+IdCampo+'\' );"> '+row[IdCampo]+' </i> </a>';
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
	
					var Ano = data[0]; //  0-Ano
	
					if ( Ano == "TOTAL" ){
						$(row).addClass("bg-light text-dark font-weight-bold");
						$(row).css("height", "35");
				  }else if ( Ano == "MÉDIA" ){
						$(row).addClass("bg-light text-muted font-weight-bold");
						$(row).css("height", "35");
						$(row).css("font-size", "12px");
				  }else if ( Ano == "RANKING" ){
						$(row).addClass("bg-light text-muted font-weight-bold");
						$(row).css("height", "35");
						$(row).css("font-size", "10px");
				  }else{
					
					arAnos[dataIndex] = Ano;
					arJAN[dataIndex] = parseFloat(GetValorDecimal(data[1])); 
					arFEV[dataIndex] = parseFloat(GetValorDecimal(data[2])); 
					arMAR[dataIndex] = parseFloat(GetValorDecimal(data[3])); 
					arABR[dataIndex] = parseFloat(GetValorDecimal(data[4])); 
					arMAI[dataIndex] = parseFloat(GetValorDecimal(data[5])); 
					arJUN[dataIndex] = parseFloat(GetValorDecimal(data[6])); 
					arJUL[dataIndex] = parseFloat(GetValorDecimal(data[7])); 
					arAGO[dataIndex] = parseFloat(GetValorDecimal(data[8])); 
					arSET[dataIndex] = parseFloat(GetValorDecimal(data[9])); 
					arOUT[dataIndex] = parseFloat(GetValorDecimal(data[10])); 
					arNOV[dataIndex] = parseFloat(GetValorDecimal(data[11])); 
					arDEZ[dataIndex] = parseFloat(GetValorDecimal(data[12])); 
					arTOTAL[dataIndex] = parseFloat(GetValorDecimal(data[13])); 
					arMEDIA[dataIndex] = parseFloat(GetValorDecimal(data[14])); 

					$('td', row).eq( 0).addClass('text-dark font-weight-bold'); // 0-Ano
					$('td', row).eq(13).addClass('text-dark font-weight-bold'); // 13-TOTAL
					$('td', row).eq(14).addClass('text-dark font-weight-bold'); // 14-MEDIA
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
					fDrawChartGraficoAnaliseCalProvAtivo( arAnos, arJAN, arFEV, arMAR, arABR, arMAI, arJUN, arJUL, arAGO, arSET, arOUT, arNOV, arDEZ, arTOTAL, arMEDIA );
					finalizarAnimacaoPesquisaAnaliseCalProvAtivo();
				}, //initComplete
				  order: [],	
				  dom: 'frtBpi',
				  buttons: [  
						{
						   extend:    'excelHtml5',
						   text:      '<i class="fa fa-file-excel-o"></i> Excel',
						   className: 'btn btn-outline-default btn-sm',
						   title: NOME_PROJETO + ' - Análise do Calendário de Proventos - Ativo '+CodAtivoSel,
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
						  title: NOME_PROJETO + ' - Análise do Calendário de Proventos - Ativo '+CodAtivoSel,
						  bom: true,
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ] } 
						},
						{
						  extend: 'pdfHtml5',
						  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						  className: 'btn btn-default btn-sm',
						  titleAttr: 'PDF',
						  title: NOME_PROJETO + ' - Análise do Calendário de Proventos - Ativo '+CodAtivoSel, 
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
						  title: NOME_PROJETO + ' - Análise do Calendário de Proventos - Ativo '+CodAtivoSel,
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
		  fLimparSomenteGridAnaliseCalendProvAtivo( urlPadrao );
		  finalizarAnimacaoPesquisaAnaliseCalProvAtivo();
		if ( e.description != undefined ){
		  fCriarAlerta("AreaAlertaPrincAnaliseCalProvAtivo", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		}
	  }
}  

async function fDrawChartGraficoAnaliseCalProvAtivo( arAnos, arJAN, arFEV, arMAR, arABR, arMAI, arJUN, arJUL, arAGO, arSET, arOUT, arNOV, arDEZ, arTOTAL, arMEDIA ){

     promise = new Promise( (resolve, reject) => {

		$('#DivGraficoAnaliseCalProvAtivo').show();
		$("#DivGraficoAnaliseCalProvAtivo").css("display", "block");
		
		var fLen = arAnos.length;
		
		var DataSetSeries = [];
		for (i = 0; i < fLen; i++) {
			DataSetSeries[i] = {name: arAnos[i], data: [ arJAN[i], arFEV[i], arMAR[i], arABR[i], arMAI[i], arJUN[i], arJUL[i], arAGO[i], arSET[i], arOUT[i], arNOV[i], arDEZ[i], arTOTAL[i], arMEDIA[i]] };
		}
	
		Highcharts.chart('DivGraficoAnaliseCalProvAtivo', {
			chart: { type: 'column' },
			title: { text: null },
			legend: { enabled: true, align: 'center', verticalAlign: 'top', floating: true, backgroundColor: Highcharts.defaultOptions.legend.backgroundColor || 'white',borderColor: '#CCC', borderWidth: 1, shadow: false },
			xAxis: { categories: [ 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT','NOV', 'DEZ', 'TOTAL', 'MÉDIA' ], crosshair: true },
			yAxis: { min: 0, title: { text: 'Rainfall (mm)' } },
			//tooltip: { headerFormat: '<span style="font-size:10px">{point.key}</span><table>', pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' + '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>', footerFormat: '</table>', shared: true, useHTML: true },
			tooltip: { pointFormatter: function() { var value = Number(this.y).toFixed(2).replace(/./g, function(c, i, a) {  return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "X" + c : c; }).replace('.',',').replace(/X/g,'.'); return '<span style="color:' + this.series.color + '">' + this.series.name + '</span>: <b>R$ ' + value + '</b><br />'; }, shared: true },
			plotOptions: { column: { pointPadding: 0.2, borderWidth: 0 } },
			series: DataSetSeries
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
		
}
  
async function fCarregarGridAnaliseCalendProvAtivo( urlPadrao ){
	try {   

		 promise = new Promise( (resolve, reject) => {

			$('#DivGraficoAnaliseCalProvAtivo').hide();
			$("#DivGraficoAnaliseCalProvAtivo").css("display", "none");
			 fLimparAreaAlerta("AreaAlertaPrincAnaliseCalProvAtivo");
	  
			  $('#GridAnaliseCalProvAtivo').dataTable().fnClearTable();
			  $("#GridAnaliseCalProvAtivo").dataTable({ bDestroy: true }).fnDestroy();	
			  
			  finalizarAnimacaoPesquisaAnaliseCalProvAtivo();
			  iniciarAnimacaoPesquisarAnaliseCalProvAtivo();
			  
			  var CodAtivo  = $("#txtFiltroAnaliseCalendProvAtivoAtivo").val();
	
			//   if ( CodAtivo == "" ){
			// 	fLimparSomenteGridAnaliseCalendProvAtivo( urlPadrao );
			// 	fCriarAlerta("AreaAlertaPrincAnaliseCalProvAtivo", TP_ALERTA_AVISO, "Ano não Informado"); 
			// 	return false;
			//   }
			  
			  $.ajax({
				  cache   : "false",
				  dataType: "json",
				  async   : true,
				  type    : "POST",
				  url: urlPadrao + "Analise/gridCalProvAtivo",
				  data: { CodAtivo  : CodAtivo },
				  success: function(result) {
					  
					  var resultado = result.data.Resultado; 
					  var mensagem  = result.data.Mensagem; 
					  var lista     = result.data.Lista;
	  
					  if (resultado == "NSESSAO") {
						  $(location).attr('href', urlPadrao + '/login');
						  return false;
					  } else if (resultado == "NOK") {
						  fLimparSomenteGridAnaliseCalendProvAtivo( urlPadrao );
						  fCriarAlerta("AreaAlertaPrincAnaliseCalProvAtivo", TP_ALERTA_AVISO, mensagem); 
						  return;
					  } else if (resultado == "FALHA") {
						  fLimparSomenteGridAnaliseCalendProvAtivo( urlPadrao );
						  fCriarAlerta("AreaAlertaPrincAnaliseCalProvAtivo", TP_ALERTA_AVISO, mensagem); 
						  return;
					  }else if (resultado == "OK") {
						  fMontarGridAnaliseCalProvAtivo( urlPadrao, lista, CodAtivo );
					  } else{
						  fLimparSomenteGridAnaliseCalendProvAtivo( urlPadrao );
						  fCriarAlerta("AreaAlertaPrincAnaliseCalProvAtivo", TP_ALERTA_AVISO, mensagem); 
						  return;
					  }
					  
				  },
				  error: function(data) {
					  fLimparSomenteGridAnaliseCalendProvAtivo( urlPadrao );
					  fCriarAlerta("AreaAlertaPrincAnaliseCalProvAtivo", TP_ALERTA_AVISO, MSG_ALERTA_ERRO); 
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
		fLimparSomenteGridAnaliseCalendProvAtivo( urlPadrao );
		if ( e.description != undefined ){ fCriarAlerta("AreaAlertaPrincAnaliseCalProvAtivo", TP_ALERTA_AVISO, MSG_ALERTA_ERRO);  }
	  }
  }
  
