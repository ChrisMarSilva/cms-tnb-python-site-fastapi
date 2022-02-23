
async function fLimparGridResumoOper( urlPadrao ){	

     promise = new Promise( (resolve, reject) => {

		fLimparAreaAlerta("AreaAlertaPrincAnaliseResumoOper");

		$("#DivAnaliseResumoOperTotCompra").text(      "R$ 0,00" );
		$("#DivAnaliseResumoOperTotVenda").text(       "R$ 0,00" );
		$("#DivAnaliseResumoOperTotValorizacao").text( "R$ 0,00 (0,00%)" );
		$("#DivAnaliseResumoOperTotProvento").text(    "R$ 0,00" );
		$("#DivAnaliseResumoOperTotGanhoPerda").text(  "R$ 0,00 (0,00%)" );
	
		fLimparSomenteGridResumoOper( urlPadrao );

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

async function fLimparSomenteGridResumoOper( urlPadrao ){
	try {	

		 promise = new Promise( (resolve, reject) => {
	    
			$("th").addClass('text-center');
			
			$('#GridAnaliseResumoOper').dataTable().fnClearTable();
			$("#GridAnaliseResumoOper").dataTable({ bDestroy: true }).fnDestroy();
			
			$('#GridAnaliseResumoOper').DataTable( {
				oLanguage: fTraduzirGrid(),
				aoColumns: [
					{ bSortable: true, sWidth: "50px", targets:  0 }, //  0-Tipo
					{ bSortable: true, sWidth: "50px", targets:  1 }, //  1-Ativo
					{ bSortable: true, sWidth: "50px", targets:  2 }, //  2-Tot. Compra
					{ bSortable: true, sWidth: "50px", targets:  3 }, //  3-Tot. Bonus
					{ bSortable: true, sWidth: "50px", targets:  4 }, //  4-Tot. Venda
					{ bSortable: true, sWidth: "50px", targets:  5 }, //  5-Tot. Valorização
					{ bSortable: true, sWidth: "50px", targets:  6 }, //  6-Tot. Proventos
					{ bSortable: true, sWidth: "50px", targets:  7 }, //  7-Tot. Ganhos/Perda
					{ bSortable: true, sWidth: "50px", targets:  8 }, //  8-Situação
					{ bSortable: true, sWidth: "50px", targets:  9 }  //  9-Acao
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
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});

	} catch(e) {
		fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",  TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

async function fMontarGridAnaliseResumoOper( urlPadrao, dataSet ){	
	try { 

		 promise = new Promise( (resolve, reject) => {

			  var TotCompra       = 0.00;
			  var TotVenda        = 0.00;
			  var TotValorizacao  = 0.00;
			  var PercValorizacao = 0.00;
			  var TotProvento     = 0.00;
			  var TotGanhoPerda   = 0.00;
			  var PercGanhoPerda  = 0.00;

			  $('#GridAnaliseResumoOper').dataTable().fnClearTable();
			  $("#GridAnaliseResumoOper").dataTable({ bDestroy: true }).fnDestroy();

			  $('#GridAnaliseResumoOper').DataTable( {
				processing: true,
				serverSide: false,
				iDisplayLength: 10,
				oLanguage: fTraduzirGrid(), 
				data: dataSet,
				aoColumns: [
					  { bSortable: true, sWidth: "50px", targets:  0, //  0-Tipo
						  render: function ( data, type, row ) {  if ( type == "display" && row[0] == 'ACAO' ) return 'AçÃO';  return data;  }
					  }, //  0-Tipo
					  { bSortable: true, sWidth: "50px", targets:  1 }, //  1-Ativo
					  { bSortable: true, sWidth: "50px", targets:  2,   //  2-Tot. Compra
						  render: function ( data, type, row ) { if ( type == "display") return "R$ " + row[2]; return parseFloat(GetValorDecimal(data)); } 				
					  },  //  2-Tot. Compra
					  { bSortable: true, sWidth: "50px", targets:  3,   //  3-Tot. Bonus
						  render: function ( data, type, row ) { if ( type == "display") return "R$ " + row[3]; return parseFloat(GetValorDecimal(data)); } 				
					  },  //  3-Tot. Compra
					  { bSortable: true, sWidth: "50px", targets:  4,   //  4-Tot. Venda
						  render: function ( data, type, row ) { if ( type == "display") return "R$ " + row[4]; return parseFloat(GetValorDecimal(data)); } 	
					  }, //  4-Tot. Venda
					  { bSortable: true, sWidth: "50px", targets:  5,   //  5-Tot. Valorização
						  render: function ( data, type, row ) { if ( type == "display") return "R$ " + row[5]; return parseFloat(GetValorDecimal(data)); } 	
					  }, //  5-Tot. Valorização
					  { bSortable: true, sWidth: "50px", targets:  6,  //  6-Tot. Proventos
						  render: function ( data, type, row ) { if ( type == "display") return "R$ " + row[6]; return parseFloat(GetValorDecimal(data)); } 	
					  },  //  6-Tot. Proventos
					  { bSortable: true, sWidth: "50px", targets:  7,   //  7-Tot. Ganhos/Perda
						  render: function ( data, type, row ) { if ( type == "display") return "R$ " + row[7]; return parseFloat(GetValorDecimal(data)); } 	
					  },//  7-Tot. Ganhos/Perda
					  { bSortable: true, sWidth: "50px", targets: 8 }, // 8-Situação
					  { bSortable: true, sWidth: "40px", targets: 9,   // 9-Acao
						render: function ( data, type, row ) {
							var btnViz = "";
							if ( type == "display") {
								CodAtivo  = row[1]; //  1-Ativo
								btnViz += '<a class="btn btn-sm btn-primary btn-icon btn-icon-mini btn-round btn-simple" style="font-size:9px;" title="Visualizar Operações do Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAbrirModalDetalheAnaliseOperResumo( \''+urlPadrao+'\', \''+CodAtivo+'\' );">';
								btnViz += '   <i class="fa fa-eye fa-lg" aria-hidden="true"></i> ';
								btnViz += '</a>';
							}
							return btnViz;
						} 
					} // 9-Acao
				],
				createdRow : function(row,data,dataIndex) {

				  $('td', row).addClass('text-center'); //font-weight-bold

				  var Tipo           = data[0];                               //  0-Tipo
				  var Ativo          = data[1];                               //  1-Ativo
			  	  var VlrCompra      = parseFloat(GetValorDecimal(data[2]));  //  2-Tot. Compra
			  	  var VlrBonus       = parseFloat(GetValorDecimal(data[3]));  //  3-Tot. Bonus
				  var VlrVenda       = parseFloat(GetValorDecimal(data[4]));  //  4-Tot. Venda
				  var VlrValorizacao = parseFloat(GetValorDecimal(data[5]));  //  5-Tot. Valorização
				  var VlrProvento    = parseFloat(GetValorDecimal(data[6]));  //  6-Tot. Proventos
				  var VlrGanhoPerda  = parseFloat(GetValorDecimal(data[7]));  //  7-Tot. Ganhos/Perda
				  var Situacao       = data[8];                               //  8-Situação

				  TotCompra       += VlrCompra + VlrBonus;
				  TotVenda        += VlrVenda;
				  TotValorizacao  += VlrValorizacao;
				  TotProvento     += VlrProvento;
				  TotGanhoPerda   += VlrGanhoPerda;
				  
				  // if ( VlrGanhoPerda  > 0.00 ) $('td', row).addClass('text-success');
				  // if ( VlrGanhoPerda  < 0.00 ) $('td', row).addClass('text-danger'); //table
				  // if ( VlrGanhoPerda == 0.00 ) $('td', row).addClass('text-primary');
				  				  
				  $('td', row).eq(1).addClass('font-weight-bold'); //  1-Ativo
				  $('td', row).eq(5).addClass('font-weight-bold'); //  5-Tot. Valorização
				  $('td', row).eq(7).addClass('font-weight-bold'); //  7-Tot. Ganhos/Perda
				  $('td', row).eq(8).addClass('font-weight-bold'); //  8-Situação

				  if ( Situacao.indexOf("ENCERRADA") != -1 )  $('td', row).css('text-decoration','line-through').addClass('font-italic'); 

				  if ( VlrValorizacao == 0.00 ){ 
				  	$('td', row).eq(5).addClass('text-primary'); //  5-Tot. Valorização
				  }
				  else if ( VlrValorizacao  > 0.00 ){
				  	$('td', row).eq(5).addClass('col-teal'); //  5-Tot. Valorização
				  }
				  else if ( VlrValorizacao  < 0.00 ){
				  	$('td', row).eq(5).addClass('col-red'); //  5-Tot. Valorização
				  }

				  if ( VlrGanhoPerda == 0.00 ){ 
				  	$('td', row).eq(1).addClass('table-primary'); //  1-Ativo
				  	$('td', row).eq(7).addClass('text-primary'); //  7-Tot. Ganhos/Perda
				  	$('td', row).eq(8).addClass('table-primary'); //  8-Situação
				  }
				  else if ( VlrGanhoPerda  > 0.00 ){
				  	$('td', row).eq(1).addClass('table-success'); //  1-Ativo
				  	$('td', row).eq(7).addClass('col-teal'); //  7-Tot. Ganhos/Perda
				  	$('td', row).eq(8).addClass('table-success'); //  8-Situação
				  }
				  else if ( VlrGanhoPerda  < 0.00 ){
				  	$('td', row).eq(1).addClass('table-danger'); //  1-Ativo
				  	$('td', row).eq(7).addClass('col-red'); //  7-Tot. Ganhos/Perda
				  	$('td', row).eq(8).addClass('table-danger'); //  8-Situação
				  }

				}, //createdRow
				initComplete: function( settings, json ) {

					PercValorizacao = 0.00;
				  	if ( TotCompra != 0.00 && TotValorizacao != 0.00 ) PercValorizacao = ( TotValorizacao / TotCompra ) * 100;

					PercGanhoPerda = 0.00;
				  	if ( TotCompra != 0.00 && TotGanhoPerda != 0.00 ) PercGanhoPerda = ( TotGanhoPerda / TotCompra ) * 100;

					$("#DivAnaliseResumoOperTotCompra").text(      "R$ " + fMascaraValor(TotCompra));
					$("#DivAnaliseResumoOperTotVenda").text(       "R$ " + fMascaraValor(TotVenda) );
					$("#DivAnaliseResumoOperTotValorizacao").text( "R$ " + fMascaraValor(TotValorizacao) + " ("+fMascaraValor(PercValorizacao)+"%)" );					
					$("#DivAnaliseResumoOperTotProvento").text(    "R$ " + fMascaraValor(TotProvento) );
					$("#DivAnaliseResumoOperTotGanhoPerda").text(  "R$ " + fMascaraValor(TotGanhoPerda) + " ("+fMascaraValor(PercGanhoPerda)+"%)" );

					if ( parseFloat(TotValorizacao)  > 0.00 ) $("#DivAnaliseResumoOperTotValorizacao").addClass("col-teal");
					if ( parseFloat(TotValorizacao)  < 0.00 ) $("#DivAnaliseResumoOperTotValorizacao").addClass("col-red");

					if ( parseFloat(TotGanhoPerda)  > 0.00 ) $("#DivAnaliseResumoOperTotGanhoPerda").addClass("col-teal");
					if ( parseFloat(TotGanhoPerda)  < 0.00 ) $("#DivAnaliseResumoOperTotGanhoPerda").addClass("col-red");

					finalizarAnimacaoPesquisaResumoOper();

				}, //initComplete
				  order: [[ 1, "asc" ]],// order: [[ 0, "asc" ], [ 1, "asc" ]],	
				  dom: 'frtBpi',
				  buttons: [  
						{
						   extend:    'excelHtml5',
						   text:      '<i class="fa fa-file-excel-o"></i> Excel',
						   className: 'btn btn-outline-default btn-sm',
						   title: NOME_PROJETO + ' - Análise - Resumo Operacoes',
						   titleAttr: 'Excel',
						   exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6, 7, 8 ] }
						}, 
						{
						  extend: 'csvHtml5',
						  charset: 'UTF-8',
						  fieldSeparator: ';',
						  titleAttr: 'CSV',
						  text:      '<i class="fa fa-file-o"></i> CSV',
						  className: 'btn btn-outline-default btn-sm',
						  title: NOME_PROJETO + ' - Análise - Resumo Operacoes',
						  bom: true,
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6, 7, 8 ] } 
						},
						{
						  extend: 'pdfHtml5',
						  text:      '<i class="fa fa-file-pdf-o"></i> PDF',
						  className: 'btn btn-default btn-sm',
						  titleAttr: 'PDF',
						  title: NOME_PROJETO + ' - Análise - Resumo Operacoes',
						  pageSize: 'A3',
						  alignment: 'center',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6, 7, 8 ] },
						  footer: true,
						  customize: function (doc) { 
							  doc.defaultStyle.fontSize = 12; 
							  doc.styles.tableHeader.fontSize = 14; 
						  }
						},
						{
						  extend: 'print',
						  text:      '<i class="fa fa-print"></i> Imprimir',
						  title: NOME_PROJETO + ' - Análise - Resumo Operacoes',
						  titleAttr: 'Imprimir',
						  className: 'btn btn-default btn-sm',
						  exportOptions: {  columns: [ 0, 1, 2, 3, 4 ,5 ,6, 7, 8 ] }
						}
				  ],
				  bFilter: false,
				  bInfo: false,
				  bLengthChange: false,
				  searchable: false,
				  orderable: true,
				  bAutoWidth: false,
				  bPaginate: false,
				  ordering: true
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
		fLimparSomenteGridResumoOper( urlPadrao );
		if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrincAnaliseResumoOper", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}  


function iniciarAnimacaoPesquisarResumoOper() {
	// $("#iRefreshResumo").addClass("fa-spin");
    // $("#btnAnaliseResumoPesquisar").addClass("disabled");
    $("#txtFiltroResumoPortfolio").attr("disabled","disabled");
    fDefinirPadraoSelect('txtFiltroResumoPortfolio');
}

function finalizarAnimacaoPesquisaResumoOper() {
	// $("#iRefreshResumo").removeClass("fa-spin");
	// $("#btnAnaliseResumoPesquisar").removeClass("disabled");
    $("#txtFiltroResumoPortfolio").removeAttr("disabled");
    fDefinirPadraoSelect('txtFiltroResumoPortfolio');
}

async function fCarregarGridResumoOper( urlPadrao ){
	try {   

		 promise = new Promise( (resolve, reject) => {

			  fLimparAreaAlerta("AreaAlertaPrincAnaliseResumoOper");
			  // fLimparGridResumoOper(urlPadrao);

			  finalizarAnimacaoPesquisaResumoOper();
			  iniciarAnimacaoPesquisarResumoOper();
	  
			  // $('#GridAnaliseResumoOper').dataTable().fnClearTable();
			  // $("#GridAnaliseResumoOper").dataTable({ bDestroy: true }).fnDestroy();

			  var IdPortfolio = $("#txtFiltroResumoPortfolio").val();
			  
			  $.ajax({
				  cache   : "false",
				  dataType: "json",
				  async   : true,
				  type    : "POST",
				  url: urlPadrao + "Analise/gridResumoOper",
				  data: { IdPortfolio: IdPortfolio },
				  success: function(result) {
					  
					  var resultado = result.data.Resultado; 
					  var mensagem  = result.data.Mensagem; 
					  var lista     = result.data.Lista;
	  
					  if (resultado == "NSESSAO") {
						  $(location).attr('href', urlPadrao + '/login');
						  return false;
					  } else if (resultado == "NOK") {
					  	  finalizarAnimacaoPesquisaResumoOper();
						  fLimparSomenteGridResumoOper( urlPadrao );
						  fCriarAlerta("AreaAlertaPrincAnaliseResumoOper", TP_ALERTA_AVISO, mensagem); 
						  return;
					  } else if (resultado == "FALHA") {
					  	  finalizarAnimacaoPesquisaResumoOper();
						  fLimparSomenteGridResumoOper( urlPadrao );
						  fCriarAlerta("AreaAlertaPrincAnaliseResumoOper", TP_ALERTA_AVISO, mensagem); 
						  return;
					  }else if (resultado == "OK") {
						  fMontarGridAnaliseResumoOper( urlPadrao, lista );
					  } else{
					  	  finalizarAnimacaoPesquisaResumoOper();
						  fLimparSomenteGridResumoOper( urlPadrao );
						  fCriarAlerta("AreaAlertaPrincAnaliseResumoOper", TP_ALERTA_AVISO, mensagem); 
						  return;
					  }
					  
				  },
				  error: function(data) {
					  finalizarAnimacaoPesquisaResumoOper();
					  fLimparSomenteGridResumoOper( urlPadrao );
					  fCriarAlerta("AreaAlertaPrincAnaliseResumoOper", TP_ALERTA_AVISO, MSG_ALERTA_ERRO); 
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
			finalizarAnimacaoPesquisaResumoOper();
			fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		});		
  
	 } catch (e) {
		finalizarAnimacaoPesquisaResumoOper();
		fLimparSomenteGridResumoOper( urlPadrao );
		if ( e.description != undefined ) fCriarAlerta("AreaAlertaPrincAnaliseResumoOper", TP_ALERTA_AVISO, MSG_ALERTA_ERRO); 
	  }
}
  
async function fAbrirModalDetalheAnaliseOperResumo( urlPadrao, CodAtivo ){
	try {  

		 promise = new Promise( (resolve, reject) => {
	
			fLimparAreaAlerta("AreaAlertaPrincAnaliseResumoOper");

			$("#PopModalDetalheAnaliseOperResumoTit").html(CodAtivo);
			$('.nav-tabs a[href="#AbaDetalheOperResumoOperac"]').tab('show')
	
			var DivGridModalDetalheAnaliseOperResumoOperac = $("#DivGridModalDetalheAnaliseOperResumoOperac");
			DivGridModalDetalheAnaliseOperResumoOperac.html("");
			
			var DivGridModalDetalheAnaliseOperResumoProvent = $("#DivGridModalDetalheAnaliseOperResumoProvent");
			DivGridModalDetalheAnaliseOperResumoProvent.html("");
			
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "Analise/gridOper",
				data: { CodAtivo: CodAtivo },
				success: function(result) {  
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
					
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						$("#PopModalDetalheAnaliseOperResumo").modal("hide");	
						fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						$("#PopModalDetalheAnaliseOperResumo").modal("hide");	
						fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_ERRO, mensagem); 
						return;
					} else if (resultado == "OK") {
	
						var content = '';
						
						if ( lista.length > 0 ){
							
							content += '<table class="table table-sm table-hover table-condensed nowrap" style="font-size: 12px;" border="0" cellspacing="0" width="100%" style="margin: 0px;">';
							content += '  <thead>';
							content += '    <tr style="font-size: 12px;" class="thead-dark font-weight-bold"> ';
							content += '      <th>Tipo</th>';
							content += '      <th>Categoria</th>';
							content += '      <th>Data</th>';
							content += '      <th>Quant.</th>';
							content += '      <th>Custo/Ação</th>';
							content += '      <th>Preço Médio</th>';
							content += '      <th>Total</th>';
							content += '      <th>Valorização</th>';
							content += '    </tr>';  
							content += '  </thead>';
							content += '  <tbody>';
							
							var TotInvest = 0.00;
							var TotAtual  = 0.00;
							
							$.each(lista, function (index, value) {
	
								var OperTipo        = value[0]; // 0-Tipo
								var OperCategoria   = value[1]; // 1-Categoria
								//var OperCorretorta  = value[2]; // 2-Corretorta
								var OperData        = value[3]; // 3-Data
								var OperQuant       = value[4]; // 4-Quant
								var OperPrecoCusto  = value[5]; //parseFloat( GetValorDecimal(value[5]) ); //  5-Preco Custo
								var OperPrecoMedio  = value[6]; // parseFloat( GetValorDecimal(value[6]) ); //  6-Preco Medio
								var OperTotal       = value[7]; // parseFloat( GetValorDecimal(value[7]) ); //  7-Total 
								var OperValorizacao = parseFloat( GetValorDecimal(value[8]) ); //  8-Valorizacao
								
								if ( OperTipo == "Compra" || OperTipo == "Compra/Troca" || OperTipo == "Bonificação" ) TotInvest += parseFloat( GetValorDecimal(OperTotal) );
								if ( OperTipo == "Venda"  || OperTipo == "Venda/Troca"  || OperTipo == "Projetado"   ) TotAtual  += parseFloat( GetValorDecimal(OperTotal) );
	
								var textCor = "text-dark";
								if ( OperTipo == "Venda" || OperTipo == "Venda/Troca" || OperTipo == "Projetado" ){
									if ( OperValorizacao > 0 ) textCor = "col-teal";
									if ( OperValorizacao < 0 ) textCor = "col-red"; 
								}
	
								content += '    <tr class="text-center '+textCor+'" > ';
								content += '      <td style="width:auto;">'+OperTipo+'</td>';
								content += '      <td style="width:auto;">'+OperCategoria+'</td>';
								content += '      <td style="width:auto;">'+OperData+'</td>';
								content += '      <td style="width:auto;">'+OperQuant+'</td>'; 
								content += '      <td style="width:auto;">R$ '+OperPrecoCusto+'</td>';
								content += '      <td style="width:auto;">R$ '+OperPrecoMedio+'</td>';
								content += '      <td style="width:auto;">R$ '+OperTotal+'</td>';
								content += '      <td class="font-weight-bold" style="width:auto;">'+( OperValorizacao != 0.00 ? "R$ " + value[8] : "" ) + '</td>';
								content += '    </tr>'; 
	
							}); //$.each(lista, function (index, value) {
								
							var TotValorizacao  = TotAtual - TotInvest;
							var PercValorizacao = 0.00;
							if ( TotInvest != 0.00 && TotValorizacao != 0.00 ) PercValorizacao = ( TotValorizacao / TotInvest ) * 100;
							
							textCor = "text-dark";
							if ( TotValorizacao > 0 ) textCor = "col-teal";
							if ( TotValorizacao < 0 ) textCor = "col-red"; 
	
							content += '    <tr style="font-size: 12px;" class="text-center '+textCor+' font-weight-bold" > ';
							content += '      <td> TOTAL </td>'; //OperTipo
							content += '      <td> </td>'; //OperCategoria
							content += '      <td> </td>'; //OperData
							content += '      <td> </td>'; //OperQuant
							content += '      <td> </td>'; //OperPrecoCusto
							content += '      <td> </td>'; //OperPrecoMedio
							content += '      <td> </td>'; // OperTotal
							content += '      <td class="font-weight-bold" >R$ '+fMascaraValor(TotValorizacao) + " ("+ fMascaraValor(PercValorizacao) +"%)"+'</td>'; //OperValorizacao
							content += '    </tr>'; 
													
							content += '  </tbody>';
							content += '</table>';
	
						} // if ( lista.length > 0 ){
						else{
							content = 'Nenhuma Operaçãp encontrada para o Ativo...';
						}
						
						DivGridModalDetalheAnaliseOperResumoOperac.html("");
						// DivGridModalDetalheAnaliseOperResumoOperac.append( "<h6 class='text-center font-weight-bold'> Operações do Ativo: "+CodAtivo+"</h6> " );	
						DivGridModalDetalheAnaliseOperResumoOperac.append( content );	
	
						$("#PopModalDetalheAnaliseOperResumo").modal({backdrop: "static"});
						return true;
		   
					} else {
						$("#PopModalDetalheAnaliseOperResumo").modal("hide");	
						fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					$("#PopModalDetalheAnaliseOperResumo").modal("hide");	
					fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
					return;
				}
			});
			
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "proventos/grid",
				data: { CodAtivo: CodAtivo, TipoRend: "", DataIni: "", DataFim: tirarFormacataoData(fDataAtual()), Corretora: "" },
				success: function(result) {  
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
					
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						$("#PopModalDetalheAnaliseOperResumo").modal("hide");	
						fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						$("#PopModalDetalheAnaliseOperResumo").modal("hide");	
						fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_ERRO, mensagem); 
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
						
						DivGridModalDetalheAnaliseOperResumoProvent.html("");
						//DivGridModalDetalheAnaliseOperResumoProvent.append( "<h6 class='text-center font-weight-bold'> Proventos do Ativo: "+CodAtivo+"</h6> " );	
						DivGridModalDetalheAnaliseOperResumoProvent.append( content );	
	
						$("#PopModalDetalheAnaliseOperResumo").modal({backdrop: "static"});
						return true;
		   
					} else {
						$("#PopModalDetalheAnaliseOperResumo").modal("hide");	
						fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					$("#PopModalDetalheAnaliseOperResumo").modal("hide");	
					fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
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
		$("#PopModalDetalheAnaliseOperResumo").modal("hide");	
		fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	}  
}	

async function fCarregarListaPortfolioResumoOper( urlPadrao ){
	try {	

		 promise = new Promise( (resolve, reject) => {

			$('#txtFiltroResumoPortfolio').empty(); 
			$('#txtFiltroResumoPortfolio').append('<option value="" selected>Meu Portfólio</option>');
			$('#txtFiltroResumoPortfolio').append('<option value="ACAO">Minhas Ações</option>');
			$('#txtFiltroResumoPortfolio').append('<option value="FII">Meus FIIs</option>');
			$('#txtFiltroResumoPortfolio').append('<option value="ETF">Meus ETFs</option>');
			$('#txtFiltroResumoPortfolio').append('<option value="BDR">Minhas BDRs</option>');
			$('#txtFiltroResumoPortfolio').append('<option value="CRIPTO">Minhas CRIPTOs</option>');
	
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "listas/lista_nomes_carteira_user",
				// data    : {  },
				success: function(result) {  
				
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista; 
	
					if (resultado == "NSESSAO") {
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_AVISO, mensagem); 
						return false;
					} else if (resultado == "FALHA") {
						fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_ERRO, mensagem); 
						return false;
					} else if (resultado == "OK") {

						$.each(lista, function (index, value) {
							$('#txtFiltroResumoPortfolio').append('<option value="'+value[0]+'">'+value[1]+'</option>');
						});

						fDefinirPadraoSelect('txtFiltroResumoPortfolio');
						return true;
					} else {
						fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_ERRO, mensagem); 
						return false;
					}
					
				},
				error: function(data) {
					fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
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
		fCriarAlerta("AreaAlertaPrincAnaliseResumoOper",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}
