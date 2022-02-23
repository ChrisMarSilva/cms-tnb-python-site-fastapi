
$(document).ready(function() {
	//$(this).attr("title", "Fundo Imob. Cotação - " + NOME_PROJETO);
	$("#MnPrincFiiFundoImobCotacao").addClass("active open");
	fLimparAreaAlertaPrinc();
	fLimparAreaAlertaModalCad();
});

function fLimparGrid( urlPadrao ){
	try {	
		
		$("th").addClass('text-center');

		$('#Grid').dataTable().fnClearTable();
		$("#Grid").dataTable({ bDestroy: true }).fnDestroy();

		$('#Grid').DataTable( {
			oLanguage: fTraduzirGrid(), 
			aoColumns: [
				{ bSortable: true, sWidth: "50px", targets: 0 }, //  0-FundoImobCodigo
				{ bSortable: true, sWidth: "50px", targets: 1 }, //  1-Fechamento
				{ bSortable: true, sWidth: "50px", targets: 2 }, //  2-Vlr. Anterior
				{ bSortable: true, sWidth: "50px", targets: 3 }, //  3-R$ Variação
				{ bSortable: true, sWidth: "50px", targets: 4 }, //  4-% Variação
				{ bSortable: true, sWidth: "50px", targets: 5 }, //  5-DtHr. Atualização
				{ bSortable: true, sWidth: "50px", targets: 6 } //  6-Acao
			],
			bFilter: true,
			searchable: true,
			orderable: true,
			bAutoWidth: false
		});

	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

function fMontarGrid( urlPadrao, dataSet ){
	try {   
	
		  $('#Grid').DataTable( {
			processing: true,
			serverSide: false,
			oLanguage: fTraduzirGrid(), 
			data: dataSet,
			aoColumns: [
			  { bSortable: true, sWidth: "50px", targets: 0 }, //  0-Ativo
			  {
				bSortable: true,
				sWidth: "50px",
				targets: 1, //  1-Fechamento
				render: function(data, type, row) {
				  if (type == "display") return "R$ " + row[1]; //  1-Fechamento
				  return data;
				}
			  }, //  1-Fechamento
			  {
				bSortable: true,
				sWidth: "50px",
				targets: 2, //  2-Vlr. Anterior
				render: function(data, type, row) {
				  if (type == "display") return "R$ " + row[2]; //  2-Vlr. Anterior
				  return data;
				}
			  }, //  3-Vlr. Anterior
			  {
				bSortable: true,
				sWidth: "50px",
				targets: 3, //  3-R$ Variação
				render: function(data, type, row) {
				  if (type == "display") return "R$ " + row[3]; //  3-R$ Variação
				  return data;
				}
			  }, //  3-R$ Variação
			  {
				  bSortable: true,
				  sWidth: "50px",
				  targets: 4, //  4-% Variação
				  render: function(data, type, row) {
					if (type == "display") return row[4]+"%"; //  4-% Variação
					return data;
				  }
			  }, //  4-% Variação
			  {
				bSortable: true,
				sWidth: "50px",
				targets: 5, //  5-Ult. Atualização
				render: function(data, type, row) {
				  if (type == "display") return colcarFormacataoDataHora(row[5]); //  5-Ult. Atualização
				  return data;
				}
			  }, //  5-Ult. Atualização
			  {
				bSortable: true,
				sWidth: "50px",
				targets: 6, //  6-Acao
				render: function(data, type, row) {
				  var btnEdt = "";
				  if (type == "display") {
					CodAtivo = row[0]; //  0-Ativo
	  
					btnEdt +='<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';
	  
					btnEdt +='<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar Cotação ' +CodAtivo +'" href="javascript:void(0);" onclick="fAbrirModalDetalheFundoImobCot( \'' +urlPadrao +"', '" +CodAtivo +"' );\">";
					btnEdt +='   <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> ';
					btnEdt += "</a>";
	  
					btnEdt += "&nbsp;&nbsp;&nbsp;";
	  
					btnEdt +='<a class="btn btn-sm btn-primary btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" id="BtnAtuCotacao'+CodAtivo+'" title="Atualizar Cotação ' +CodAtivo +'" href="javascript:void(0);" onclick="fAtualizarUnicaCotacao( \'' +urlPadrao +"', '" +CodAtivo +"', 0, 0 );\">";
					btnEdt +='   <i class="fa fa-refresh fa-sm" aria-hidden="true" id="iBtnAtuCotacao'+CodAtivo+'"></i> ';
					btnEdt += "</a>";
	  
					btnEdt += "</div>";
				  }
				  return btnEdt;
				}
			  } //  6-Acao
			],
			createdRow : function(row,data,dataIndex) {
				//$("td", row).addClass("text-center");
			}, //createdRow
			initComplete: function( settings, json ) {
			},
			bFilter: true,
			bInfo: true,
			bLengthChange: false,
			searchable: true,
			orderable: true,
			bOrdering: true,
			bSortable: true,
			sAutoWidth: false,
			bPaginate: false,
			bAutoWidth: false
		  });
		  
		  $( document ).ajaxError(function( event, request, settings, thrownError ) { fLimparGrid( urlPadrao ); });
  
	  } catch (e) {
		  fLimparGrid( urlPadrao );
		  if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	  }
}

function fCarregarGrid( urlPadrao ){
	try {   
		  
		  fLimparAreaAlertaPrinc();
		  
		  $('#Grid').dataTable().fnClearTable();
		  $("#Grid").dataTable({ bDestroy: true }).fnDestroy();		
	
		  $.ajax({
			  cache   : "false",
			  dataType: "json",
			  async   : true,
			  type    : "POST",
			  url     : urlPadrao + "FiiFundoImobCotacao/grid",
			  data    : { },
			  success: function(result) {
				  
				  var resultado = result.data.Resultado; 
				  var mensagem  = result.data.Mensagem; 
				  var lista     = result.data.Lista;
  
				  if (resultado == "NSESSAO") {
					  $(location).attr('href', urlPadrao + '/login');
					  return false;
				  } else if (resultado == "NOK") {
					  fLimparGrid( urlPadrao );
					  fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
					  return;
				  } else if (resultado == "FALHA") {
					  fLimparGrid( urlPadrao );
					  fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					  return;
				  }else if (resultado == "OK") {
					  fMontarGrid( urlPadrao, lista );
				  } else{
					  fLimparGrid( urlPadrao );
					  fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					  return;
				  }
				  
			  },
			  error: function(data) {
				  fLimparGrid( urlPadrao );
				  fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				  return false;
			  }
		  });		
		  
	  } catch (e) {
		  fLimparGrid( urlPadrao );
		  if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	  }
}

function fLimparDadosModalFundoImobCot( ) {
	fLimparAreaAlertaModalCad();	
	$("#txtCadCotFundo").val( "" );
	$("#txtCadCotFechamento").val( "" );
	$("#txtCadCotVlrAnterior").val( "" );
	$("#txtCadCotVariacao").val( "" );
}

function fAbrirModalDetalheFundoImobCot( urlPadrao, fiiFundoCodigo ) {
	fLimparDadosModalFundoImobCot();
	fCarregarDadosModalDetalheFundoImobCot( urlPadrao, fiiFundoCodigo );
}

function fCarregarDadosModalDetalheFundoImobCot( urlPadrao, fiiFundoCodigo ) {
    try {

       if ( fiiFundoCodigo == "" ){
		   fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Codigo do Fundo Imob. não informado!');
          return;
        }

         $.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "FiiFundoImobCotacao/carregar",
            data    : { fiiFundoCodigo : fiiFundoCodigo },
            success: function (result) {
			
				var resultado    = result.data.Resultado; 
				var mensagem     = result.data.Mensagem; 
				var FundoImobCot = result.data.Dados;
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
				} else if (resultado == "OK") {
				   if ( FundoImobCot.Fundo ) { 
						$("#txtCadCotFundo").val(       FundoImobCot.Fundo       );
						$("#txtCadCotFechamento").val(  FundoImobCot.Fechamento  );
						$("#txtCadCotVlrAnterior").val( FundoImobCot.VlrAnterior );
						$("#txtCadCotVariacao").val(    FundoImobCot.Variacao    );
						$('#PopModalDetalheFundoImobCotacao').modal({backdrop: 'static'});
					} else {
						fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					}
				} else {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
				}

            },
            error: function (data) {
               fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
            }
        });        

    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fValidarDadosFundoImobCot() {	
	try {
		
		fLimparAreaAlertaModalCad();

		var Fundo         = $("#txtCadCotFundo").val();
		var VlrFechamento = $("#txtCadCotFechamento").val(); 
		var VlrAnterior   = $("#txtCadCotVlrAnterior").val(); 
		var Variacao      = $("#txtCadCotVariacao").val(); 
		
		var ListaErros = "";
		if( Fundo         == "" ) ListaErros = ListaErros + " - Fundo<br/>";
		if( VlrFechamento == "" ) ListaErros = ListaErros + " - Fechamento<br/>";
		if( VlrAnterior   == "" ) ListaErros = ListaErros + " - Vlr. Anterior<br/>";
		if( Variacao      == "" ) ListaErros = ListaErros + " - Variação<br/>";
		if( ListaErros != "" ){
			fCriarAlertaModalCad(TP_ALERTA_AVISO, "Os seguintes campos não estão preenchido: <br/>"+ListaErros);
			return false;
		}	
		
		return true;
	
	} catch (e) {
		fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return false;
	} 
}
function iniciarAnimacaoAtualizacao( CodAtivo = "" ) {
	$("#BtnAtuCotacao"+CodAtivo).addClass("disabled");
	$("#BtnAtuCotacao"+CodAtivo).removeClass("btn-simple");
	
    $("#iBtnAtuCotacao"+CodAtivo).removeClass("fa-refresh");
    $("#iBtnAtuCotacao"+CodAtivo).addClass("fa-spinner");
    $("#iBtnAtuCotacao"+CodAtivo).addClass("fa-pulse");
}
  
function finalizarAnimacaoAtualizacao( CodAtivo = "" ) {
	$("#BtnAtuCotacao"+CodAtivo).removeClass("disabled");	
	$("#BtnAtuCotacao"+CodAtivo).addClass("btn-simple");
	
	$("#iBtnAtuCotacao"+CodAtivo).removeClass("fa-spinner");
	$("#iBtnAtuCotacao"+CodAtivo).removeClass("fa-pulse");
	$("#iBtnAtuCotacao"+CodAtivo).addClass("fa-refresh");
}

function fSalvarDadosFundoImobCot( urlPadrao ){
	try {
		
		if ( !fValidarDadosFundoImobCot() ) return false;

		finalizarAnimacaoSalvar();
		iniciarAnimacaoSalvar();

		var CodAtivo      = $("#txtCadCotFundo").val();
		var VlrFechamento = $("#txtCadCotFechamento").val(); 
		var VlrAnterior   = $("#txtCadCotVlrAnterior").val(); 
		var Variacao      = $("#txtCadCotVariacao").val(); 
		
		finalizarAnimacaoAtualizacao(Fundo);
		iniciarAnimacaoAtualizacao(Fundo);
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "FiiFundoImobCotacao/salvar",
			data    : { fiiFundoCodigo: CodAtivo, VlrFechamento: VlrFechamento, VlrAnterior: VlrAnterior, Variacao: Variacao },
			success: function(result) {  
			
				finalizarAnimacaoSalvar();
				finalizarAnimacaoAtualizacao(CodAtivo);
				
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
					fLimparDadosModalFundoImobCot();
					$("#PopModalDetalheFundoImobCotacao").modal("hide");	
					fCarregarGrid( urlPadrao );	
					//fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
				} else {
					fCriarAlertaModalCad(TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function(data) {
				finalizarAnimacaoSalvar();
				finalizarAnimacaoAtualizacao(CodAtivo);
				fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		finalizarAnimacaoAtualizacao(CodAtivo);
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function fAtualizarTodasCotacoes(urlPadrao) {
	try {

		finalizarAnimacaoAtualizacao("");
		iniciarAnimacaoAtualizacao("");

		var iNroLinha  =0;
		var iTotLinha = $('#Grid > tbody > tr').length;
		
        $('#Grid > tbody > tr').each(function() {
			iNroLinha++;
			var CodAtivo = $(this).find("td").eq(0).html();
			fAtualizarUnicaCotacao(urlPadrao, CodAtivo, iNroLinha, iTotLinha);
		});

		// finalizarAnimacaoAtualizacao("");
	
	} catch (e) {
		finalizarAnimacaoAtualizacao("");
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function fAtualizarUnicaCotacao(urlPadrao, CodAtivo = "", iNroLinha = 0, iTotLinha = 0) {
	try {			

		 promise = new Promise( (resolve, reject) => {

			if ( CodAtivo == "" ){
				fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Ativo não informado!');
			   return;
			 }
			 
			finalizarAnimacaoAtualizacao(CodAtivo);
			iniciarAnimacaoAtualizacao(CodAtivo);

			$('#Grid > tbody > tr').each(function() {
				if ( CodAtivo == $(this).find("td").eq(0).html() ) {					
					$(this).find("td").eq(1).html( "" ); // ("R$ 0,00"); 
					$(this).find("td").eq(2).html( "" ); // ("R$ 0,00"); 
					$(this).find("td").eq(3).html( "" ); // ("R$ 0,00"); 
					$(this).find("td").eq(4).html( "" ); // ("R$ 0,00");  
					$(this).find("td").eq(5).html( "" ); // ("0,00%")
					return false;
				}
			});
	 
			 $.ajax({
				 cache   : "false",
				 dataType: "json",
				 async   : true,
				 type    : "POST",
				 url     : urlPadrao + "FiiFundoImobCotacao/AtualizaCotacao",
				 data    : { fiiFundoCodigo : CodAtivo },
				 success: function (result) {			
					 var resultado    = result.data.Resultado; 
					 var mensagem     = result.data.Mensagem; 
           			 var FundoImobCot = result.data.Dados;	
          			 resolve(true);			
					 if (resultado == "NSESSAO") {
						 $(location).attr('href', urlPadrao + '/login');
						 return false;
					 } else if (resultado == "NOK") {
             				finalizarAnimacaoAtualizacao(CodAtivo);
						 fCriarAlertaPrinc(TP_ALERTA_AVISO, "Ativo: "+CodAtivo+" - " + mensagem); 
					 } else if (resultado == "FALHA") {
            			 finalizarAnimacaoAtualizacao(CodAtivo);
						 fCriarAlertaPrinc(TP_ALERTA_ERRO, "Ativo: "+CodAtivo+" - " + mensagem); 
					 } else if (resultado == "OK") {
						if ( FundoImobCot.Fundo ) { 											
							$('#Grid > tbody > tr').each(function() {
								if ( FundoImobCot.Fundo == $(this).find("td").eq(0).html() ) {
									$(this).find("td").eq(1).html("R$ " + FundoImobCot.Fechamento); 
									$(this).find("td").eq(2).html("R$ " + FundoImobCot.VlrAnterior); 
									$(this).find("td").eq(3).html("R$ " + FundoImobCot.VlrVariacao); 
									$(this).find("td").eq(4).html(FundoImobCot.PercVariacao + "%");
									$(this).find("td").eq(5).html( colcarFormacataoDataHora(FundoImobCot.DtHrAtualizacao) );
									return false;
								}
							});
						 } else {
               					finalizarAnimacaoAtualizacao(CodAtivo);
							 fCriarAlertaPrinc(TP_ALERTA_ERRO, "Fundo: "+CodAtivo+" - " + mensagem); 
						 }					
					 } else {
            			 finalizarAnimacaoAtualizacao(CodAtivo);
						 fCriarAlertaPrinc(TP_ALERTA_ERRO, "Fundo: "+CodAtivo+" - " + mensagem); 
					 }
				 },
				error: function (request, status, error) { // error: function(data) {  //error: function (request, status, error) {
						finalizarAnimacaoAtualizacao(CodAtivo);
						fCriarAlertaPrinc(TP_ALERTA_ERRO, "Fundo: "+CodAtivo+" - " + request.responseText); 
				 }
			 });   

			// resolve(true);
			// reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
		})
		.then( txt => {
			finalizarAnimacaoAtualizacao(CodAtivo);
			if ( iNroLinha == iTotLinha ) finalizarAnimacaoAtualizacao("");
		})
		.catch( txt => {
			finalizarAnimacaoAtualizacao(CodAtivo);
			if ( iNroLinha == iTotLinha ) finalizarAnimacaoAtualizacao("");
			fCriarAlertaPrinc(TP_ALERTA_ERRO, "Fundo: "+CodAtivo+" - " + MSG_ALERTA_ERRO); 
		});	
	
	} catch (e) {
    finalizarAnimacaoAtualizacao(CodAtivo);
		if ( iNroLinha==iTotLinha ) finalizarAnimacaoAtualizacao("");
		fCriarAlertaPrinc(TP_ALERTA_ERRO, "Fundo: "+CodAtivo+" - " + MSG_ALERTA_ERRO); 
		return;
	} 
}


//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------