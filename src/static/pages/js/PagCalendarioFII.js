
function fBuscarListaProventosFII( urlPadrao ){
	try{

		 promise = new Promise( (resolve, reject) => {
	
			$("#DivListaCalendarioFII").html("");

			var CodAtivo  = $("#txtFiltroCalendFundo").val();
			if( !CodAtivo || CodAtivo == "" ) 	 return;
	
			$("#txtFiltroCalendFundo").prop('disabled', true );
			$("#DivListaCalendarioFII").html(
				'<i class="fa fa-spinner fa-spin fa-3x" aria-hidden="true"> </i> '+
				'<br/> '+
				'<br/> '+
				'<span style="font-size:12px;" class="txt-muted font-weight-bold">Carregando Proventos</span>'+
				'<br/> '+
				'<span style="font-size:14px;" class="txt-muted font-weight-bold">'+CodAtivo+'</span>'
			);
	
			$.ajax({
				cache   : "false",
				dataType: "json",
				async   : true,
				type    : "POST",
				url     : urlPadrao + "calendario/grid",
				data: { TipoInvest: 'FII', CodAtivo: CodAtivo },
				success: function(result) {
					
					var resultado = result.data.Resultado; 
					var mensagem  = result.data.Mensagem; 
					var lista     = result.data.Lista;
	
					if (resultado == "NSESSAO") {
						$("#DivListaCalendarioFII").html("");
						$("#txtFiltroCalendFundo").prop('disabled', false );
						$(location).attr('href', urlPadrao + '/login');
						return false;
					} else if (resultado == "NOK") {
						$("#DivListaCalendarioFII").html("");
						$("#txtFiltroCalendFundo").prop('disabled', false );
						fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
						return;
					} else if (resultado == "FALHA") {
						$("#DivListaCalendarioFII").html("");
						$("#txtFiltroCalendFundo").prop('disabled', false );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}else if (resultado == "OK") {
	
						var Conteudo = '';
	
						if ( lista && lista.length > 0 ){
							$.each(lista, function (index, value) {
								
								var EmprProvId      = value[0];
								var EmprProvAtivo   = value[1];
								var EmprProvTipo    = value[2]
								var EmprProvDtEx    = value[3];
								var EmprProvDtPagto = value[4];
								var EmprProvValor   = value[5];
	
								if ( EmprProvDtPagto != "" ) EmprProvDtPagto = colcarFormacataoData(EmprProvDtPagto);
								if ( EmprProvDtPagto == "" ) EmprProvDtPagto = 'SEM PREVISÃO';
	
								 var EmprProvTipoDescr = "";
								 if ( EmprProvTipo == 'R' ) EmprProvTipoDescr = 'RENDIMENTO';
								 if ( EmprProvTipo == 'E' ) EmprProvTipoDescr = 'DESDOBRAMENTO';
								 if ( EmprProvTipo == 'G' ) EmprProvTipoDescr = 'GRUPAMENTO';
								 if ( EmprProvTipo == 'B' ) EmprProvTipoDescr = 'BONIFICAÇÃO';
	
								 if ( EmprProvTipo == "R" ){
									Conteudo += ' <div class="text-center" style="border: 0px solid blue;">';
									Conteudo += ' <span class="font-weight-bold text-dark" style="font-size:14px;">'+EmprProvTipoDescr+'</span>';
									Conteudo += ' <br>';
									Conteudo += ' <span class="font-weight-bold text-secondary" style="font-size:12px;">Dt Ex: <span class="font-weight-normal text-muted" style="font-size:13px;">' + colcarFormacataoData(EmprProvDtEx)+ '</span></span>';
									Conteudo += ' <br>';
									Conteudo += ' <span class="font-weight-bold text-secondary" style="font-size:12px;">Dt Pagto: <span class="font-weight-normal text-muted" style="font-size:13px;">' + EmprProvDtPagto+ '</span></span>';
									Conteudo += ' <br>';
									Conteudo += ' <span class="font-weight-bold text-secondary" style="font-size:12px;">Valor: <span class="font-weight-normal text-muted" style="font-size:13px;">R$ ' + EmprProvValor.replace('.', ',') + '</span></span>';
									Conteudo += ' </div>';
									Conteudo += ' <hr style="margin-top: 5px; margin-bottom: 5px;">';
								 }
	
								if ( EmprProvTipo == "E" || EmprProvTipo == "G" || EmprProvTipo == "B" ){
	
									var EmprProvQtde = 0;
									if ( EmprProvTipo == 'E') EmprProvQtde = Math.round( (1 / EmprProvValor) * 100 );//Desdobro
									if ( EmprProvTipo == 'G') EmprProvQtde = Math.round(  1 / EmprProvValor); //Grupar
	
									var EmprProvQtdeDescr = "";
									if ( EmprProvTipo == 'E') EmprProvQtdeDescr = '1 para '+EmprProvQtde;//Desdobro
									if ( EmprProvTipo == 'G') EmprProvQtdeDescr = EmprProvQtde+' para 1';//Grupar
									if ( EmprProvTipo == 'B') EmprProvQtdeDescr = EmprProvValor+'%';//Grupar
	
									Conteudo += ' <div class="text-center" style="border: 0px solid blue;">';
									Conteudo += ' <span class="font-weight-bold text-dark" style="font-size:14px;">'+EmprProvTipoDescr+'</span>';
									Conteudo += ' <br>';
									Conteudo += ' <span class="font-weight-bold text-secondary" style="font-size:12px;">Dt Ex: <span class="font-weight-normal text-muted" style="font-size:13px;">' + colcarFormacataoData(EmprProvDtEx)+ '</span></span>';
									Conteudo += ' <br>';
									Conteudo += ' <span class="font-weight-bold text-secondary" style="font-size:12px;">Valor: <span class="font-weight-normal text-muted" style="font-size:13px;">' + EmprProvQtdeDescr + '</span></span>';
									Conteudo += ' </div>';
									Conteudo += ' <hr style="margin-top: 5px; margin-bottom: 5px;">';
								}
	
							});
						}else{
							Conteudo = '<small style="font-size:14px;" class="font-italic text-muted">Nenhum provento encontrado...</small><br/>';
						}
	
						$("#DivListaCalendarioFII").html(Conteudo);
						$("#txtFiltroCalendFundo").prop('disabled', false );
	
					} else{
						$("#DivListaCalendarioFII").html("");
						$("#txtFiltroCalendFundo").prop('disabled', false );
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
						return;
					}
					
				},
				error: function(data) {
					$("#DivListaCalendarioFII").html("");
					$("#txtFiltroCalendFundo").prop('disabled', false );
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
		$("#DivListaCalendarioFII").html("");
		$("#txtFiltroCalendFundo").prop('disabled', false );
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function fCarregarListaProventoFII( urlPadrao ){
	try {

		 promise = new Promise( (resolve, reject) => {

			$('#calendarFII').fullCalendar({
				defaultDate: fDataAtual(),
				displayEventTime : false,
				eventStartEditable : false,
				height: 600,
				contentHeight: 550,
				weekends: true, 
				footer: true,  
				ignoreTimezone: false,
				editable: false,
				businessHours: true,
				locale: 'pt-br',
				titleFormat: 'MMMM YYYY', 
				defaultView: 'month',
				monthNames: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
				monthNamesShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
				dayNames: ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabado'],
				dayNamesShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
				header: { 
					left: 'prev,next today', 
					center: 'title', 
					right: 'month,listWeek,listDay,listMonth',
					close: 'fa-times', prev: 'fa-chevron-left', next: 'fa-chevron-right', prevYear: 'fa-angle-double-left', nextYear: 'fa-angle-double-right', 
				}, 
				views: { 
				  month    : { titleFormat: 'MMMM YYYY',  }, 
				  week     : { titleFormat: "D MMMM YYYY", }, 
				  day      : { titleFormat: "ddd, d MMMM YYYY", },
				  listDay  : { buttonText: 'Dia' },
				  listWeek : { buttonText: 'Semana' },
				  listMonth: { buttonText: 'Lista' },
				 },
				 eventLimit: true,
				 themeSystem: 'standard',
				 navLinks: true, 
				 eventSources: [
	
				   // INICIO - LISTA DE DATA EX
				   {
					  textColor      : '#31708f', 
					  color          : '#d9edf7',
					  backgroundColor: '#b9def0', 
					  borderColor    : '#9acfea', 
					  events: function(start, end, timezone, callback) {
	
						$('.popover').popover('hide');
	
						$.ajax({
							url     : urlPadrao + "calendario/lista",
							dataType: 'json',
							cache   : "false",
							async   : true,
							type    : "POST",
							data    : { TipoInvest: 'FII', TpLista : 'DTEX', DataIni: start.format('YYYYMMDD'), DataFim: end.format('YYYYMMDD'), }, 
							error: function() {
								fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
								return false;
							},
							success: function(result) {
	
								var resultado = result.data.Resultado; 
								var mensagem  = result.data.Mensagem; 
								var lista     = result.data.Lista;
	
								if (resultado == "NSESSAO") {
									$(location).attr('href', urlPadrao + '/login');
									return false;
								} else if (resultado == "NOK") {
									fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
									return;
								} else if (resultado == "FALHA") {
									fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
									return;
								}else if (resultado == "OK") {
									var events = [];
									$.each(lista, function (index, value) {
	
										var CalId       = value[0];// 0-CalendarioId
										var CalTitle    = '';
										var CalDate     = ''; 
										var ProvCodigo  = value[1]; // 1-AtivoCodigo
										var ProvTipo    = value[2]; // 2-ProventoTipo
										var ProvDtEx    = value[3]; // 3-ProventoDtEx
										var ProvDtPagto = value[4]; // 4-ProventoDtPagto
										var ProvValor   = value[5]; // 5-ProventoValor
										
										if ( ProvTipo == 'R') CalTitle = ProvCodigo + ' Ex Rendimento';
										CalDate  = ProvDtEx;
										
										events.push({
											id           : CalId, 
											start        : CalDate,
											title        : CalTitle, 
											codigo       : ProvCodigo,
											provTipo     : ProvTipo,
											provDtEx     : ProvDtEx,
											provDtPagto  : ProvDtPagto,
											provValor    : ProvValor
										});
										
									});
									callback(events);
								} else{
									fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
									return;
								}
	
							}
						  });
					  },
				   },
				   // FIM - LISTA DE DATA EX
	
				   // INICIO - LISTA DE DATA PAGTO
				   {
						color          : '#dff0d8',    
						textColor      : '#3c763d', 
						backgroundColor: '#c8e5bc', 
						borderColor    : '#b2dba1', 
						events: function(start, end, timezone, callback) {
						$.ajax({
							url     : urlPadrao + "calendario/lista",
							dataType: 'json',
							cache   : "false",
							async   : true,
							type    : "POST",
							data    : { TipoInvest: 'FII', TpLista : 'DTPAGTO', DataIni: start.format('YYYYMMDD'), DataFim: end.format('YYYYMMDD'), }, 
							error: function() {
								fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
								return false;
							},
							success: function(result) {
	
								var resultado = result.data.Resultado; 
								var mensagem  = result.data.Mensagem; 
								var lista     = result.data.Lista;
	
								if (resultado == "NSESSAO") {
									$(location).attr('href', urlPadrao + '/login');
									return false;
								} else if (resultado == "NOK") {
									fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
									return;
								} else if (resultado == "FALHA") {
									fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
									return;
								}else if (resultado == "OK") {
									var events = [];
									$.each(lista, function (index, value) {
	
										var CalId       = value[0];// 0-CalendarioId
										var CalTitle    = '';
										var CalDate     = ''; 
										var ProvCodigo  = value[1]; // 1-AtivoCodigo
										var ProvTipo    = value[2]; // 2-ProventoTipo
										var ProvDtEx    = value[3]; // 3-ProventoDtEx
										var ProvDtPagto = value[4]; // 4-ProventoDtPagto
										var ProvValor   = value[5]; // 5-ProventoValor
										
										if ( ProvTipo == 'R') CalTitle = ProvCodigo + ' Pagto Rendimento';
										CalDate  = ProvDtPagto;
										
										events.push({
											id           : CalId, 
											start        : CalDate,
											title        : CalTitle, 
											codigo       : ProvCodigo,
											provTipo     : ProvTipo,
											provDtEx     : ProvDtEx,
											provDtPagto  : ProvDtPagto,
											provValor    : ProvValor
										});
	
									});
									callback(events);
								} else{
									fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
									return;
								}
	
							}
							});
						},
					},
					// FIM - LISTA DE DATA PAGTO
	
				   // INICIO - LISTA DE OPERACOES DE COMPRA
				   {
					color          : '#FFFFAA',    
					textColor      : '#555500', 
					backgroundColor: '#D4D46A', 
					borderColor    : '#808015', 
					events: function(start, end, timezone, callback) {
					$.ajax({
						url     : urlPadrao + "calendario/lista",
						dataType: 'json',
						cache   : "false",
						async   : true,
						type    : "POST",
						data    : { TipoInvest: 'FII', TpLista: 'COMPRA', DataIni: start.format('YYYYMMDD'), DataFim: end.format('YYYYMMDD'), }, 
						error: function() {
							fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
							return false;
						},
						success: function(result) {
	
							var resultado = result.data.Resultado; 
							var mensagem  = result.data.Mensagem; 
							var lista     = result.data.Lista;
	
							if (resultado == "NSESSAO") {
								$(location).attr('href', urlPadrao + '/login');
								return false;
							} else if (resultado == "NOK") {
								fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
								return;
							} else if (resultado == "FALHA") {
								fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
								return;
							}else if (resultado == "OK") {
								var events = [];
								$.each(lista, function (index, value) {
	
									var CalId      = value[0];// 0-OperacaoId
									var CalTitle   = '';
									var CalDate    = ''; 
									var OperCodigo = value[1]; // 1-AtivoCodigo
									var OperTipo   = value[2]; // 2-OperacaoTipo
									var OperData   = value[3]; // 3-OperacaoData
									var OperQuant  = value[4]; // 4-OperacaoQuant
									var OperPreco  = value[5]; // 5-OperacaoPreco
									var OperTotal  = value[6]; // 5-OperacaoTotal
									
									CalTitle = OperCodigo+ ' ' + OperTipo+ ' ' + colcarFormacataoInteiro(OperQuant);
									CalDate  = OperData;
									
									events.push({
										id         : CalId, 
										start      : CalDate,
										title      : CalTitle, 
										codigo     : OperCodigo,
										operTipo   : OperTipo,
										operData   : OperData,
										operQuant  : OperQuant,
										operPreco  : OperPreco,
										operTotal  : OperTotal
									});
	
								});
								callback(events);
							} else{
								fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
								return;
							}
	
						}
						});
					},
				},
				 // FIM - LISTA DE OPERACOES DE COMPRA
				 
	
				// INICIO - LISTA DE OPERACOES DE VENDA
				 {
					color          : '#E498AF',    
					textColor      : '#4C0017', 
					backgroundColor: '#BE5F7C', 
					borderColor    : '#4C0017', 
					events: function(start, end, timezone, callback) {
					$.ajax({
						url     : urlPadrao + "calendario/lista",
						dataType: 'json',
						cache   : "false",
						async   : true,
						type    : "POST",
						data    : { TipoInvest: 'FII', TpLista: 'VENDA', DataIni: start.format('YYYYMMDD'), DataFim: end.format('YYYYMMDD'), }, 
						error: function() {
							fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
							return false;
						},
						success: function(result) {
	
							var resultado = result.data.Resultado; 
							var mensagem  = result.data.Mensagem; 
							var lista     = result.data.Lista;
	
							if (resultado == "NSESSAO") {
								$(location).attr('href', urlPadrao + '/login');
								return false;
							} else if (resultado == "NOK") {
								fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
								return;
							} else if (resultado == "FALHA") {
								fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
								return;
							}else if (resultado == "OK") {
								var events = [];
								$.each(lista, function (index, value) {
	
									var CalId      = value[0];// 0-OperacaoId
									var CalTitle   = '';
									var CalDate    = ''; 
									var OperCodigo = value[1]; // 1-AtivoCodigo
									var OperTipo   = value[2]; // 2-OperacaoTipo
									var OperData   = value[3]; // 3-OperacaoData
									var OperQuant  = value[4]; // 4-OperacaoQuant
									var OperPreco  = value[5]; // 5-OperacaoPreco
									var OperTotal  = value[6]; // 5-OperacaoTotal
									
									CalTitle = OperCodigo+ ' ' + OperTipo+ ' ' + colcarFormacataoInteiro(OperQuant);
									CalDate  = OperData;
									
									events.push({
										id         : CalId, 
										start      : CalDate,
										title      : CalTitle, 
										codigo     : OperCodigo,
										operTipo   : OperTipo,
										operData   : OperData,
										operQuant  : OperQuant,
										operPreco  : OperPreco,
										operTotal  : OperTotal
									});
	
								});
								callback(events);
							} else{
								fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
								return;
							}
	
						}
						});
					},
				},
				 // FIM - LISTA DE OPERACOES DE VENDA
	
	
				// INICIO - LISTA DE GRUPAMENTO E DESDOBRAMENTO
				 {
					// color          : '#E498AF',    
					// textColor      : '#4C0017', 
					// backgroundColor: '#BE5F7C', 
					// borderColor    : '#4C0017', 
					events: function(start, end, timezone, callback) {
					$.ajax({
						url     : urlPadrao + "calendario/lista",
						dataType: 'json',
						cache   : "false",
						async   : true,
						type    : "POST",
						data    : { TipoInvest: 'FII', TpLista:'OUTROS', DataIni: start.format('YYYYMMDD'), DataFim:  end.format('YYYYMMDD'), }, 
						error: function() {
							fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
							return false;
						},
						success: function(result) {
	
							var resultado = result.data.Resultado; 
							var mensagem  = result.data.Mensagem; 
							var lista     = result.data.Lista;
	
							if (resultado == "NSESSAO") {
								$(location).attr('href', urlPadrao + '/login');
								return false;
							} else if (resultado == "NOK") {
								fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
								return;
							} else if (resultado == "FALHA") {
								fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
								return;
							}else if (resultado == "OK") {
								var events = [];
								$.each(lista, function (index, value) {
	
									var CalId       = value[0];// 0-CalendarioId
									var CalTitle    = '';
									var CalDate     = ''; 
									var ProvCodigo  = value[1]; // 1-AtivoCodigo
									var ProvTipo    = value[2]; // 2-ProventoTipo
									var ProvDtEx    = value[3]; // 3-ProventoDtEx
									var ProvDtPagto = value[4]; // 4-ProventoDtPagto
									var ProvValor   = value[5]; // 5-ProventoValor
									
									if ( ProvTipo == 'E') CalTitle = ProvCodigo + ' Desdobro';
									if ( ProvTipo == 'G') CalTitle = ProvCodigo + ' Grupar';
									if ( ProvTipo == 'B') CalTitle = ProvCodigo + ' Bonificar';
									CalDate  = ProvDtEx;
	
									var OperQtde = 0;
									if ( ProvTipo == 'E') OperQtde = Math.round( (1 / ProvValor) * 100 );//Desdobro
									if ( ProvTipo == 'G') OperQtde = Math.round(1 / ProvValor);//Grupar
	
									var OperQtdeDescr = "";
									if ( ProvTipo == 'E') OperQtdeDescr = '1 para '+OperQtde; //Desdobro
									if ( ProvTipo == 'G') OperQtdeDescr = OperQtde+' para 1'; //Grupar
									if ( ProvTipo == 'B') OperQtdeDescr = ProvValor+'%'; //Bonificar
									
									events.push({
										id           : CalId, 
										start        : CalDate,
										title        : CalTitle, 
										codigo       : ProvCodigo,
										provTipo     : ProvTipo,
										provDtEx     : ProvDtEx,
										provDtPagto  : ProvDtPagto,
										provValor    : OperQtdeDescr
									});
	
								});
								callback(events);
							} else{
								fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
								return;
							}
	
						}
						});
					},
				},
				 // FIM - LISTA DE GRUPAMENTO E DESDOBRAMENTO
	
				 ],  
				 eventRender: function (event, element, view) {
	
					  element.attr('href', 'javascript:void(0);');
					  
					  popoverElement = element.popover({
						html      : true,
						animation : true,
						title     : '<span class="text-muted">'+event.codigo+'</span> <button type="button" id="closepopover" class="close" onclick="fFecharPopoverFII();">&times;</button>',
						container : 'body',
						trigger   : 'click', //manual hover //click
						placement : 'top', //right
						content   : function() {
	
							$('.popover').popover('hide');
							setTimeout(function () {element.popover('hide');}, 10000); //10Seg
							
							if ( event.provDtPagto != "" ) event.provDtPagto = colcarFormacataoData(event.provDtPagto);
							if ( event.provDtPagto == "" ) event.provDtPagto = 'SEM PREVISÃO';
	
							if ( event.provTipo ){
								if ( event.provTipo == "R" ){
									var ProvTipo = '';
									if ( event.provTipo == 'R') ProvTipo = 'RENDIMENTO';
									return '<table border="0" >'+
										   '  <tr>'+ 
										   '    <td colspan="2" style="text-align:center;"> <span style="font-size:12px; color:gray; font-weight:bold;">' + ProvTipo + '</span> </td>'+
										   '  </tr>'+  
										   '  <tr>'+ 
										   '    <td style="text-align:right;"> <span style="font-size:12px; color:gray;">Data Ex:</span> </td>'+ 
										   '    <td> <span style="font-size : 12px; color:gray; font-weight:bold;">&nbsp;' + colcarFormacataoData(event.provDtEx)+ '</span> </td>'+ 
										   '  </tr>'+ 
										   '  <tr>'+ 
										   '    <td style="text-align:right;">  <span style="font-size:12px; color:gray;">Data Pagto:</span> </td>'+ 
										   '    <td> <span style="font-size:12px; color:gray; font-weight:bold;">&nbsp;' + event.provDtPagto+ '</span> </td>'+ 
										   '  </tr>'+ 
										   '  <tr>'+ 
										   '    <td style="text-align:right;"> <span style="font-size : 12px; color:gray;">Valor:</span> </td>'+ 
										   '    <td> <span style="font-size:12px; color:gray; font-weight:bold;">&nbsp;R$ ' + event.provValor.replace('.', ',') + '</span> </td>'+ 
										   '  </tr>'+ 
										   '  <tr>'+ 
										   '    <td colspan="2"> &nbsp; </td>'+
										   '  </tr>'+ 
										   '<table>';
								}
								if ( event.provTipo == "E" || event.provTipo == "G" || event.provTipo == "B" ){
									var ProvTipo = '';
									if ( event.provTipo == 'E') ProvTipo = 'DESDOBRAMENTO';
									if ( event.provTipo == 'G') ProvTipo = 'GRUPAMENTO';
									if ( event.provTipo == 'B') ProvTipo = 'BONIFICAÇÃO';
									return '<table border="0" >'+
										   '  <tr>'+ 
										   '    <td colspan="2" style="text-align:center;"> <span style="font-size:12px; color:gray; font-weight:bold;">' + ProvTipo + '</span> </td>'+
										   '  </tr>'+  
										   '  <tr>'+ 
										   '    <td style="text-align:right;"> <span style="font-size:12px; color:gray;">Data Ex:</span> </td>'+ 
										   '    <td> <span style="font-size : 12px; color:gray; font-weight:bold;">&nbsp;' + colcarFormacataoData(event.provDtEx)+ '</span> </td>'+ 
										   '  </tr>'+ 
										   '  <tr>'+ 
										   '    <td style="text-align:right;"> <span style="font-size : 12px; color:gray;">Valor:</span> </td>'+ 
										   '    <td> <span style="font-size:12px; color:gray; font-weight:bold;">&nbsp;' + event.provValor.replace('.', ',') + '</span> </td>'+ 
										   '  </tr>'+ 
										   '  <tr>'+ 
										   '    <td colspan="2"> &nbsp; </td>'+
										   '  </tr>'+ 
										   '<table>';
								}
								
							}
							
							if ( event.operTipo ){
								return '<table border="0" >'+
									   '  <tr>'+ 
									   '    <td colspan="2" style="text-align:center;"> <span style="font-size:12px; color:gray; font-weight:bold;">' + event.operTipo + '</span> </td>'+
									   '  </tr>'+  
									   '  <tr>'+ 
									   '    <td style="text-align:right;"> <span style="font-size:12px; color:gray;">Data:</span> </td>'+ 
									   '    <td> <span style="font-size : 12px; color:gray; font-weight:bold;">&nbsp;' + colcarFormacataoData(event.operData)+ '</span> </td>'+ 
									   '  </tr>'+ 
									   '  <tr>'+ 
									   '    <td style="text-align:right;">  <span style="font-size:12px; color:gray;">Quant:</span> </td>'+ 
									   '    <td> <span style="font-size:12px; color:gray; font-weight:bold;">&nbsp;R$ ' + colcarFormacataoInteiro(event.operQuant) + '</span> </td>'+ 
									   '  </tr>'+ 
									   '  <tr>'+ 
									   '    <td style="text-align:right;"> <span style="font-size : 12px; color:gray;">Preço:</span> </td>'+ 
									   '    <td> <span style="font-size:12px; color:gray; font-weight:bold;">&nbsp;R$ ' + event.operPreco + '</span> </td>'+ 
									   '  </tr>'+ 
									   '  <tr>'+ 
									   '    <td style="text-align:right;"> <span style="font-size : 12px; color:gray;">Total:</span> </td>'+ 
									   '    <td> <span style="font-size:12px; color:gray; font-weight:bold;">&nbsp;R$ ' + event.operTotal + '</span> </td>'+ 
									   '  </tr>'+ 
									   '  <tr>'+ 
									   '    <td colspan="2"> &nbsp; </td>'+
									   '  </tr>'+ 
									   '<table>';
							}
	
						}
					})
					.popover('show');
	
				},
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
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function fFecharPopoverFII(){
	$( ".popover" ).click(function() { $( this ).popover('hide'); });
}
