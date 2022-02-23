
$(document).ready(function() {

	//$(this).attr("title", "Corretora - " + NOME_PROJETO);
	
	$("#MnPrincCorretora").addClass("active open");		
	
	fLimparAreaAlertaPrinc();	
	fLimparAreaAlertaModalCad();
	fLimparAreaAlertaModalExc();

});

function fLimparGrid( urlPadrao ){
	try {	
		
		$("th").addClass('text-center');

		$('#Grid').dataTable().fnClearTable();
		$("#Grid").dataTable({ bDestroy: true }).fnDestroy();

		$('#Grid').DataTable( {
		    data: [],
			oLanguage: fTraduzirGrid(), 
			aoColumns: [
				{ bSortable: true, sWidth: "150px", targets: 0 }, //  0-Nome
				{ bSortable: true, sWidth:  "50px", targets: 1 }, //  1-CNPJ
				{ bSortable: true, sWidth:  "50px", targets: 2 }, //  2-Corretagem
				{ visible  : false,                 targets: 3 }, //  3-IdCorret
				{ bSortable: true, sWidth:  "50px", targets: 4 }  //  4-Acao
			],
			order: [],
			bFilter: false,
			bInfo: false,
            iDisplayLength: 100,
			bLengthChange: false,
			bSearchable: false,
			bOrderable: false,
			bSortable: false,
			bAutoWidth: false,
			bPaginate: false,
			bOrdering: false
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
				{ bSortable: true, sWidth: "150px", targets: 0 }, //  1-Nome
				{ bSortable: true, sWidth:  "50px", targets: 1,   //  1-CNPJ
					render: function ( data, type, row ) { 
						if ( type == "display" )
							if ( row[1] != "" ) return FormatarCPFCNPJ(row[1]); //  1-CNPJ
						return data;
					} 				 
				}, //  1-CNPJ
				{ bSortable: true, sWidth:  "50px", targets: 2,   //  2-Corretagem
					render: function ( data, type, row ) { 
						if ( type == "display") return "R$ " + row[2]; //  2-Valor
						return data;
					} 				 
				}, //  2-Valor
				{ visible  : false,                 targets: 3 }, //  3-IdCorret
				{ bSortable: true, sWidth: "50px", targets:   4,  //  4-Acao
					render: function ( data, type, row ) {
						
						var btnEdt = "";
						var btnDel = "";
						var btnDis = '';

						if ( type == "display") {
							
							IdCorret = row[3]; //  3-IdCorret
							//if ( TpSitPagdr=='1'  ) btnDis = ' disabled';
							
							btnEdt += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';

							btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar Corretora" href="javascript:void(0);" onclick="fAbrirModalDetalheCorret( \''+urlPadrao+'\', \''+IdCorret+'\', \'Alterar\' );">';
							btnEdt += '   <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> ';
							btnEdt += '</a>';
							
							btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple '+btnDis+'"'+btnDis+' style="font-size:0.5rem;" title="Excluir Corretora" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fChamarPagExclusaoCorret( \''+IdCorret+'\' );">';
							btnDel += '   <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ';
							btnDel += '</a>';
							
							btnDel += '</div>';
						}
						
						return btnEdt + '&nbsp;' + btnDel;
						
					} 
				} //  9-Acao
          ],
          createdRow : function(row,data,dataIndex) {
            $('td', row).addClass('text-center');
          }, //createdRow
          initComplete: function( settings, json ) {
          },
            order: [[ 0, "asc" ]],
            iDisplayLength: 100,
			bLengthChange: false,
			bFilter: false,
			bInfo: false,
			bSearchable: false,
			bPaginate: false,
			bOrderable: true,
			bSortable: true,
			bOrdering: true,
			searchable: true,
			orderable: true,
			bAutoWidth: false
			
        });
		
		$( document ).ajaxError(function( event, request, settings, thrownError ) {
			fLimparGrid( urlPadrao );
		});

    } catch (e) {
		fLimparGrid( urlPadrao );
		  if ( e.description != undefined ){
			fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		  }
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
			url     : urlPadrao + "corretora/grid",
			data    : {},
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
		  if ( e.description != undefined ){
			fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		  }
    }
}

function fLimparDadosModalCorret( ) {
	fLimparAreaAlertaModalCad();
	$("#txtCadCorretId").val("");
	$("#txtCadCorretoraLista").val("");
	$('#txtCadCorretoraLista')[0].selectedIndex = 0;
	$("#txtCadCorretCNPJ").val("");
	$("#txtCadCorretNome").val("");
	$("#txtCadCorretValor").val("0,00");
	fDefinirPadraoSelect('txtCadCorretoraLista');
}

function fAbrirModalDetalheCorret( urlPadrao, IdCorret, TipoModal ) {
    try {

    	fLimparDadosModalCorret();

    	$("#PopModalDetalheCorretTit").html(" - "+TipoModal);

//		$("#txtCadCorretCNPJ").removeAttr("readonly");
//		$("#txtCadCorretNome").removeAttr("readonly");
//		$("#txtCadCorretValor").removeAttr("readonly");
		$("#BtnModalDetalheCorretSalvar").removeAttr("disabled");
		$("#BtnModalDetalheCorretSalvar").removeClass("disabled");
					
		if ( TipoModal == "Nova" || TipoModal == "Novo" ){
	    	$('#PopModalDetalheCorret').modal({backdrop: 'static'})  ;
		}

		if ( TipoModal == "Alterar" || TipoModal == "Visualizar" ){
	        fCarregarDadosModalDetalheCorret( urlPadrao, IdCorret, TipoModal );
		}

		//$("#txtCadCorretCNPJ").focus();

    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fCarregarDadosModalDetalheCorret( urlPadrao, IdCorret, TipoModal ) {
    try {
		
       if ( IdCorret == "" ){
		   fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Corretora não informado!');
          return;
        }
         $.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "corretora/carregar",
            data    : { IdCorret : IdCorret  },
            success: function (result) {
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var Corret    = result.data.Dados;
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
				} else if (resultado == "OK") {
				   if ( Corret.Id ) {
						$("#txtCadCorretId").val( Corret.Id );
						$("#txtCadCorretNome").val( Corret.Nome );
	                    if ( Corret.IdCorretoraLista ){
	                        $("#txtCadCorretoraLista").val( Corret.IdCorretoraLista );
	                        fDefinirPadraoSelect('txtCadCorretoraLista');
	                    }
						if ( Corret.CNPJ ) $("#txtCadCorretCNPJ").val( FormatarCPFCNPJ(Corret.CNPJ) );
						$("#txtCadCorretValor").val( Corret.Valor );
						$('#PopModalDetalheCorret').modal({backdrop: 'static'});
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

		var Nome  = $("#txtCadCorretNome").val(); 
		var CNPJ  = tirarFormacataoCPFCNPJ( $("#txtCadCorretCNPJ").val() ); 
		var Valor = $("#txtCadCorretValor").val(); 
		
		var ListaErros = "";
		if( Nome == "" ) ListaErros = ListaErros + " - Nome<br/>";
		//if( (CNPJ != "") && !ValidarCNPJ( $("#txtCadCorretCNPJ", FMT_CNPJ) ) )  
		//  ListaErros = ListaErros + " - CNPJ Invalido<br/>";
		//if( Valor == "" || Valor == ",00" || Valor == "0,00" )
		//	ListaErros = ListaErros + " - Corretagem<br/>";	
  
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


function fSalvarDadosCorret( urlPadrao ){
	try {
		
		if ( !fValidarDados() )
			return false;

		iniciarAnimacaoSalvar();

		var Id = $("#txtCadCorretId").val();
		var IdCorretoraLista = $("#txtCadCorretoraLista").val();
		var CNPJ  = $("#txtCadCorretCNPJ").val(); 
		var Nome  = $("#txtCadCorretNome").val(); 
		var Valor = $("#txtCadCorretValor").val(); 
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "corretora/salvar",
			data    : { Id: Id, IdCorretoraLista: IdCorretoraLista, CNPJ: tirarFormacataoCPFCNPJ( CNPJ ), Nome  : Nome, Valor : Valor },
			success: function(result) {  
			
				finalizarAnimacaoSalvar();
				
				var resultado = result.data.Resultado; 
				var mensagem = result.data.Mensagem; 
				
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
					fLimparDadosModalCorret();
					$("#PopModalDetalheCorret").modal("hide");					
					fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					fCarregarGrid( urlPadrao );	
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
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		CriarAlertaModal(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function fChamarPagExclusaoCorret( IdCorret ) {
    try {

       $("#txtDelCorretId").val("");
	   
       if (  IdCorret  == "" ){
          fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Corretora não informado!'); 
          return;
        }
		
       // $("#PopModalDelCorret").modal("show");
       $("#PopModalDelCorret").modal({backdrop: "static"});

       $("#txtDelCorretId").val( IdCorret );

    } catch (e) {
        $("#PopModalDelCorret").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fExcluirDadosCorret( urlPadrao ) {
    try {

		finalizarAnimacaoExcluir();

		var IdCorret = $("#txtDelCorretId").val();

		if ( IdCorret == "" ){
			fCriarAlertaModalExc(TP_ALERTA_AVISO, 'Id. Corretora não informado!');
			return;
		}

		iniciarAnimacaoExcluir();
	  
		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "corretora/excluir",
			data: {  IdCorret : IdCorret },
			success: function (result) {
				
				finalizarAnimacaoExcluir();				
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaModalExc(TP_ALERTA_AVISO, mensagem); 
					return false;
				} else if (resultado == "FALHA") {
					fCriarAlertaModalExc(TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {					
				    fCriarAlertaPrinc(TP_ALERTA_SUCESSO, mensagem); 
					$("#txtDelCorretId").val("");
					$("#PopModalDelCorret").modal("hide");
					fCarregarGrid( urlPadrao );
					return true;
				} else {
					fCriarAlertaModalExc(TP_ALERTA_ERRO, mensagem); 
					return false;
				}
				
			},
			error: function (data) {
				$("#PopModalDelCorret").modal("hide");
				finalizarAnimacaoExcluir();
				fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
			}
		});

    } catch (e) {
        $("#PopModalDelCorret").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fBuscarDadosCorretoraLista( urlPadrao ) {
    try {

		fLimparAreaAlerta("AreaAlertaModalCad");

        $("#txtCadCorretCNPJ").val("");
        $("#txtCadCorretNome").val("");

		var corretora = $("#txtCadCorretoraLista").val().trim();

		if ( corretora == "" ){
			//fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_AVISO, 'Ativo não informado!');
			return;
		}

		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "corretora/carregarcorretorageral",
			data: { corretora : corretora },
			success: function (result) {

				var resultado = result.data.Resultado;
				var mensagem  = result.data.Mensagem;
				var dados     = result.data.Dados;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_AVISO, mensagem);
					return false;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_ERRO, mensagem);
					return;
				} else if (resultado == "OK") {
                    if ( dados.CNPJ ) $("#txtCadCorretCNPJ").val( FormatarCPFCNPJ(dados.CNPJ) );
                    if ( dados.Nome ) $("#txtCadCorretNome").val( dados.Nome );
					return true;
				} else {
					fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_ERRO, mensagem);
					return false;
				}
			},
			error: function (data) {
				fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
			}
		});

    } catch (e) {
		fCriarAlerta("AreaAlertaModalCad",TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}