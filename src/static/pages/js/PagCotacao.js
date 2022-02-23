
$(document).ready(function() {
  //$(this).attr("title", "Cotação - " + NOME_PROJETO);
  $("#MnPrincCotacao").addClass("active open");
  fLimparAreaAlertaPrinc();
  fLimparAreaAlertaModalCad();
});

function iniciarAnimacaoPesquisar() {
  $("#iRefresh").addClass("fa-spin");
  $("#btnCotPesquisar").addClass("disabled");
  $("#btnCotLimpar").addClass("disabled");
}

function finalizarAnimacaoPesquisa() {
  $("#iRefresh").removeClass("fa-spin");
  $("#btnCotPesquisar").removeClass("disabled");
  $("#btnCotLimpar").removeClass("disabled");
}

function fLimparGrid(urlPadrao) {
  $("#selFiltroSetor").val("");
  $("#selFiltroSubSetor").val("");
  $("#selFiltroSegmento").val("");
  $("#selFiltroAtivo").val("");
  //$("#selFiltroTipo").val("");
  fLimparSomenteGrid(urlPadrao);
}

function fLimparSomenteGrid(urlPadrao) {
  try {
    finalizarAnimacaoPesquisa();
    $("th").addClass("text-center");

    $("#Grid")
      .dataTable()
      .fnClearTable();

    $("#Grid")
      .dataTable({ bDestroy: true })
      .fnDestroy();

    $("#Grid").DataTable({
      oLanguage: fTraduzirGrid(),
      aoColumns: [
        { bSortable: true, sWidth: "50px", targets: 0 }, //  0-Ativo
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
  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
  }
}

function fMontarGrid(urlPadrao, dataSet) {
  try {
    $("#Grid").DataTable({
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

              btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar Cotação ' + CodAtivo + '" href="javascript:void(0);" onclick="fAbrirModalDetalheCot( \'' +urlPadrao +"', '" +CodAtivo +"' );\">";
              btnEdt += '   <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> ';
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
      createdRow: function(row, data, dataIndex) {
        //$("td", row).addClass("text-center");
      }, //createdRow
      initComplete: function(settings, json) {
        finalizarAnimacaoPesquisa();
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

    $(document).ajaxError(function(event, request, settings, thrownError) {
      fLimparSomenteGrid(urlPadrao);
      finalizarAnimacaoPesquisa();
    });
  } catch (e) {
    fLimparSomenteGrid(urlPadrao);
    finalizarAnimacaoPesquisa();
    if (e.description != undefined) {
      fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
  }
}

function fCarregarGrid(urlPadrao) {
  try {
    fLimparAreaAlertaPrinc();

    $("#Grid")
      .dataTable()
      .fnClearTable();
    $("#Grid")
      .dataTable({ bDestroy: true })
      .fnDestroy();

    finalizarAnimacaoPesquisa();
    iniciarAnimacaoPesquisar();

    var Setor = $("#selFiltroSetor")
      .val()
      .trim();
    var SubSetor = $("#selFiltroSubSetor")
      .val()
      .trim();
    var Segmento = $("#selFiltroSegmento")
      .val()
      .trim();
    var CodAtivo = $("#selFiltroAtivo")
      .val()
      .trim();
    var Tipo = $("#selFiltroTipo")
      .val()
      .trim();

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "cotacao/grid",
      data: {
        Setor: Setor,
        SubSetor: SubSetor,
        Segmento: Segmento,
        CodAtivo: CodAtivo,
        Tipo: Tipo
      },
      success: function(result) {
        var resultado = result.data.Resultado;
        var mensagem = result.data.Mensagem;
        var lista = result.data.Lista;

        if (resultado == "NSESSAO") {
          $(location).attr("href", urlPadrao + "/login");
          return false;
        } else if (resultado == "NOK") {
          finalizarAnimacaoPesquisa();
          fLimparSomenteGrid(urlPadrao);
          fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
          return;
        } else if (resultado == "FALHA") {
          finalizarAnimacaoPesquisa();
          fLimparSomenteGrid(urlPadrao);
          fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
          return;
        } else if (resultado == "OK") {
          fMontarGrid(urlPadrao, lista);
        } else {
          finalizarAnimacaoPesquisa();
          fLimparSomenteGrid(urlPadrao);
          fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
          return;
        }
      },
      error: function(data) {
        finalizarAnimacaoPesquisa();
        fLimparSomenteGrid(urlPadrao);
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
        return false;
      }
    });
  } catch (e) {
    finalizarAnimacaoPesquisa();
    fLimparSomenteGrid(urlPadrao);
    if (e.description != undefined) {
      fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
  }
}

function fLimparDadosModalCot( ) {
	fLimparAreaAlertaModalCad();	
	$("#txtCadCotAtivo").val( "" );
	$("#txtCadCotFechamento").val( "" );
	$("#txtCadCotVlrAnterior").val( "" );
	$("#txtCadCotVariacao").val( "" );
}

function fAbrirModalDetalheCot( urlPadrao, CodAtivo ) {
	fLimparDadosModalCot();
    fCarregarDadosModalDetalheCot( urlPadrao, CodAtivo );
}

function fCarregarDadosModalDetalheCot( urlPadrao, CodAtivo ) {
    try {
       if ( CodAtivo == "" ){
		   fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Ativo não informado!');
          return;
		}

         $.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "cotacao/carregar",
            data    : { CodAtivo : CodAtivo },
            success: function (result) {			
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var Cot        = result.data.Dados;				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
				} else if (resultado == "OK") {
				   if ( Cot.Ativo ) { 
						$("#txtCadCotAtivo").val(       Cot.Ativo       );
						$("#txtCadCotFechamento").val(  Cot.Fechamento  );
						$("#txtCadCotVlrAnterior").val( Cot.VlrAnterior );
						$("#txtCadCotVariacao").val(    Cot.Variacao    );
						$('#PopModalDetalheCotacao').modal({backdrop: 'static'});
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

function fValidarDados() {	
	try {
		
		fLimparAreaAlertaModalCad();

		var CodAtivo      = $("#txtCadCotAtivo").val();
		var VlrFechamento = $("#txtCadCotFechamento").val(); 
		var VlrAnterior   = $("#txtCadCotVlrAnterior").val(); 
		var Variacao      = $("#txtCadCotVariacao").val(); 
		
		var ListaErros = "";
		if( CodAtivo      == "" ) ListaErros = ListaErros + " - Ativo<br/>";
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

function fSalvarDadosCot( urlPadrao ){
	try {
		
		if ( !fValidarDados() ) return false;
		
		finalizarAnimacaoSalvar();
		iniciarAnimacaoSalvar();

		var CodAtivo      = $("#txtCadCotAtivo").val();
		var VlrFechamento = $("#txtCadCotFechamento").val(); 
		var VlrAnterior   = $("#txtCadCotVlrAnterior").val(); 
		var Variacao      = $("#txtCadCotVariacao").val(); 

		finalizarAnimacaoAtualizacao(CodAtivo);
		iniciarAnimacaoAtualizacao(CodAtivo);
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "cotacao/salvar",
			data    : { CodAtivo: CodAtivo, VlrFechamento: VlrFechamento, VlrAnterior: VlrAnterior, Variacao: Variacao },
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
					fLimparDadosModalCot();
					$("#PopModalDetalheCotacao").modal("hide");	
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
				 url     : urlPadrao + "cotacao/AtualizaCotacao",
				 data    : { CodAtivo : CodAtivo },
				 success: function (result) {			
					 var resultado = result.data.Resultado; 
					 var mensagem  = result.data.Mensagem; 
           var Cot        = result.data.Dados;	
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
						if ( Cot.Ativo ) { 											
							$('#Grid > tbody > tr').each(function() {
								if ( Cot.Ativo == $(this).find("td").eq(0).html() ) {
									$(this).find("td").eq(1).html("R$ " + Cot.Fechamento); 
									$(this).find("td").eq(2).html("R$ " + Cot.VlrAnterior); 
									$(this).find("td").eq(3).html("R$ " + Cot.VlrVariacao); 
									$(this).find("td").eq(4).html(Cot.PercVariacao + "%");
									$(this).find("td").eq(5).html( colcarFormacataoDataHora(Cot.DtHrAtualizacao) );
									return false;
								}
							});
						 } else {
               finalizarAnimacaoAtualizacao(CodAtivo);
							 fCriarAlertaPrinc(TP_ALERTA_ERRO, "Ativo: "+CodAtivo+" - " + mensagem); 
						 }					
					 } else {
             finalizarAnimacaoAtualizacao(CodAtivo);
						 fCriarAlertaPrinc(TP_ALERTA_ERRO, "Ativo: "+CodAtivo+" - " + mensagem); 
					 }
				 },
         error: function (request, status, error) { // error: function(data) {  //error: function (request, status, error) {
           finalizarAnimacaoAtualizacao(CodAtivo);
					fCriarAlertaPrinc(TP_ALERTA_ERRO, "Ativo: "+CodAtivo+" - " + request.responseText); 
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
			fCriarAlertaPrinc(TP_ALERTA_ERRO, "Ativo: "+CodAtivo+" - " + MSG_ALERTA_ERRO); 
		});	
	
	} catch (e) {
    finalizarAnimacaoAtualizacao(CodAtivo);
		if ( iNroLinha==iTotLinha ) finalizarAnimacaoAtualizacao("");
		fCriarAlertaPrinc(TP_ALERTA_ERRO, "Ativo: "+CodAtivo+" - " + MSG_ALERTA_ERRO); 
		return;
	} 
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------


