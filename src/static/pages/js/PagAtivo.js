
$(document).ready(function() {
	$("#MnPrincAtivos").addClass("active open");
	fLimparAreaAlertaPrinc();	
	fLimparAreaAlertaModalCad();
	fLimparAreaAlertaModalExc();
	$("#FormOper input[type=text]").bind("keyup change", function(){ fCalcularPrecoTotal();  fCalcularOperacao();  });
	//$("#txtDetOperTxLiquid" ).click(function(){                      fCalcularTaxaLiquid();  fCalcularOperacao();  });
	//$("#txtDetOperTxEmol" ).click(function(){                        fCalcularTaxaEmol();    fCalcularOperacao();  });
	//$("#txtDetOperTxIRRF" ).click(function(){                        fCalcularTaxaIRRF();    fCalcularOperacao();  });
});

function fCarregarListaGrupos( urlPadrao, IdGrupo ){
	try {
		
		$('#btnAdicionarAtivo').hide(); 
		$('#btnAlterarGrupo').hide(); 
		$('#btnRemoverGrupo').hide(); 		
		$('#btnAdicionarGrupo').show();
		
		$('#TabGrupos').empty(); // $("#TabGrupos").html('');
		if ( IdGrupo == "" ) 
			$("#TabGrupos").append( '<li class="nav-item"> <a class="nav-link active" id="TabPortfolio" data-toggle="tab" href="#Portfolio" aria-selected="true">Meu Portfólio <span id="TabQtdePortfolio">( 0 )</span> </a> </li>' )
		else
			$("#TabGrupos").append( '<li class="nav-item"> <a class="nav-link"        id="TabPortfolio" data-toggle="tab" href="#Portfolio"aria-selected="false">Meu Portfólio <span id="TabQtdePortfolio">( 0 )</span> </a> </li>' );
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "listas/lista_nomes_radar_user",
			// data    : {  },
			success: function(result) {  
			
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var lista     = result.data.Lista; 

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
					return false;
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					return false;
				} else if (resultado == "OK") {	

					 if ( lista.length > 0 )					 
						$.each(lista, function (index, value) {
							if ( IdGrupo == value[0] )
								$('<li class="nav-item"> <a class="nav-link active" id="Tab'+value[0]+'" data-toggle="tab" href="#'+value[0]+'" aria-selected="true" >'+value[1]+' <span id="TabQtde'+value[0]+'">( '+value[2]+' )</span></a> </li>').appendTo('#TabGrupos');
							else
								$('<li class="nav-item"> <a class="nav-link"        id="Tab'+value[0]+'" data-toggle="tab" href="#'+value[0]+'" aria-selected="false">'+value[1]+' <span id="TabQtde'+value[0]+'">( '+value[2]+' )</span></a> </li>').appendTo('#TabGrupos');
						});		
						
					$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
						e.target        // newly activated tab
						e.relatedTarget // previous active tab
						fCarregarGrid( urlPadrao ); 
					});
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
	
	} catch(e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	}
}

function fLimparGrid( urlPadrao ){
	try {	
		
		$("th").addClass('text-center');

		$('#Grid').dataTable().fnClearTable();
		$("#Grid").dataTable({ bDestroy: true }).fnDestroy();

		$('#Grid').DataTable( {
		    data: [],
			oLanguage: fTraduzirGrid(), 
			aoColumns: [
				{ bSortable: true, sWidth:  "50px", targets: 0 }, //  0-Setor
				{ bSortable: true, sWidth:  "50px", targets: 1 }, //  1-Sub-Setor
				{ bSortable: true, sWidth:  "50px", targets: 2 }, //  2-Segmento
				{ bSortable: true, sWidth:  "50px", targets: 3 }, //  3-Ativo
				{ bSortable: true, sWidth:  "50px", targets: 4 }, //  4-Empresa
				{ bSortable: true, sWidth:  "50px", targets: 5 }, //  5-Preço
				{ bSortable: true, sWidth:  "50px", targets: 6 }, //  6-Variação
				{ visible  : false,                 targets: 7 }, //  7-IdUserGrupo
				{ visible  : false,                 targets: 8 }, //  8-IdUserAtivo
				{ bSortable: false, sWidth: "10px", targets: 9 }  //  9-Acao
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

function fMontarGrid( urlPadrao, dataSet, IdGrupo ){
  try {   
  
        $('#Grid').DataTable( {
          processing: true,
          serverSide: false,
		  oLanguage: fTraduzirGrid(), 
		  data: dataSet,
          aoColumns: [
				{ bSortable: true, sWidth:  "50px", targets: 0 }, //  0-Setor
				{ bSortable: true, sWidth:  "50px", targets: 1 }, //  1-Sub-Setor
				{ bSortable: true, sWidth:  "50px", targets: 2 }, //  2-Segmento
				{ bSortable: true, sWidth:  "50px", targets: 3 }, //  3-Ativo
				{ bSortable: true, sWidth:  "50px", targets: 4 }, //  4-Empresa
				{ bSortable: true, sWidth:  "10px", targets: 5,   //  5-Preço
					render: function ( data, type, row ) { 
						if ( type == "display") return "R$ " + row[5]; //  5-Preço
						return data;
					} 				 
				}, //  5-Preço
				{ bSortable: true, sWidth:  "10px", targets: 6,   //  6-Variação
					render: function ( data, type, row ) { 
						if ( type == "display") return row[6]+"%";  //  6-Variação
						return data;
					} 				 
				}, //  6-Variação
				{ visible  : false,                 targets: 7 }, //  7-IdUserGrupo
				{ visible  : false,                 targets: 8 }, //  8-IdUserAtivo
				{ bSortable: false, sWidth:  "10px", targets: 9,   //  9-Acao
					render: function ( data, type, row ) {
						
						var btnDel = "";

						if ( type == "display") {
							
							var Quant       = 100;
							var TipoInvest  = row[0]; //  0-TipoInvest
							var CodAtivo    = row[3]; //  3-Ativo
							var Preco       = row[5]; //  5-Preço
							var IdUserGrupo = row[7]; //  7-IdUserGrupo
							var IdUserAtivo = row[8]; //  8-IdUserAtivo
								
							btnDel += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';


                            if ( TipoInvest == 'CRIPTO' ) {
                                btnDel += '<a class="btn btn-sm btn-success btn-icon btn-icon-mini btn-round btn-simple" style="font-size:9px;" title="Comprar Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAbrirModalDetalheOperCripto( \''+urlPadrao+'\', \'\', \'Novo\', \'C\', \''+CodAtivo+'\', \'100\', \''+Preco+'\' );"> ';
                                btnDel += '  <i class="fa fa-plus-square" aria-hidden="true"></i> ';
                                btnDel += '</a>';

                            } else {
                                btnDel += '<a class="btn btn-sm btn-success btn-icon btn-icon-mini btn-round btn-simple" style="font-size:9px;" title="Comprar Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAbrirModalDetalheOper( \''+urlPadrao+'\', \'\', \'Novo\', \'C\', \''+CodAtivo+'\', \'100\', \''+Preco+'\' );"> ';
                                btnDel += '  <i class="fa fa-plus-square" aria-hidden="true"></i> ';
                                btnDel += '</a>';;
                            }

							btnDel += '  &nbsp;';
							
							if ( IdGrupo != "" ){
								btnDel += '<a class="btn btn-sm btn-dark btn-icon btn-icon-mini btn-round btn-simple" style="font-size:9px;" title="Remover Ativo '+CodAtivo+' do Radar Personalizado" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fAbrirModalRemoverAtivo( \''+urlPadrao+'\', \''+IdUserGrupo+'\', \''+IdUserAtivo+'\', \''+CodAtivo+'\' );"> ';
								btnDel += '   <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ';
								btnDel += '</a>';
							} else{
                                if ( TipoInvest == 'CRIPTO' ) {
                                    btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:9px;" title="Vender Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fAbrirModalDetalheOperCripto( \''+urlPadrao+'\', \'\', \'Novo\', \'V\', \''+CodAtivo+'\', \''+Quant+'\', \''+Preco+'\' );">';
                                    btnDel += '  <i class="fa fa-minus-square" aria-hidden="true"></i> ';
                                    btnDel += '</a>';
                                } else {
                                    btnDel += '<a class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:9px;" title="Vender Ativo '+CodAtivo+'" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fAbrirModalDetalheOper( \''+urlPadrao+'\', \'\', \'Novo\', \'V\', \''+CodAtivo+'\', \''+Quant+'\', \''+Preco+'\' );">';
                                    btnDel += '  <i class="fa fa-minus-square" aria-hidden="true"></i> ';
                                    btnDel += '</a>';
                                }
							}
							
							btnDel += '</div>';
								
						}
						
						return  btnDel;
						
					} 
				} //  9-Acao
          ],
          createdRow : function(row,data,dataIndex) {	
            $('td', row).addClass('text-center');
			var PercValoriz = parseFloat(GetValorDecimal(data[6]));  //  6-Variação
			if ( PercValoriz > 0.00 )  $('td', row).addClass('text-success');
			if ( PercValoriz < 0.00 )  $('td', row).addClass('text-danger');
          }, //createdRow
          initComplete: function( settings, json ) {
				if ( IdGrupo == "" ) $("#TabQtdePortfolio").html("( "+dataSet.length+" )")
				else $("#TabQtde"+IdGrupo).html("( "+dataSet.length+" )");
          },
            order: [[ 3, "asc" ]], //  3-Ativo
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
		
		var IdGrupo = "";

		// $("#TabGrupos li a span").removeClass("text-dark");
		// $("#TabGrupos li a span").addClass("text-secondary");
		$("#TabGrupos li a").each(function () { 
			if ( $(this).hasClass( "active" ) == true ){
				IdGrupo = $(this).attr('id');
				// $(this).removeClass("text-secondary");
				// $(this).addClass("text-dark");
			}
		 });
		 
		IdGrupo = IdGrupo.replace("TabPortfolio", "");
		IdGrupo = IdGrupo.replace("Tab", "");
		
		if ( IdGrupo == "" ){
			$('#btnAdicionarAtivo').hide(); 
			$('#btnAlterarGrupo').hide(); 
			$('#btnRemoverGrupo').hide();	
		    $('#btnAdicionarGrupo').show();
		}
		else{
			$('#btnAdicionarAtivo').show(); 
			$('#btnAlterarGrupo').show(); 
			$('#btnRemoverGrupo').show(); 	
		    $('#btnAdicionarGrupo').hide();
		}	
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "ativo/grid",
			data    : { IdGrupo : IdGrupo },
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
					fMontarGrid( urlPadrao, lista, IdGrupo );
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

function fAbrirModalDetalheGrupo( urlPadrao, TipoModal ) {
    try {

		fLimparAreaAlertaModalCad();
		
		$("#txtCadGrupoId").val(   "" );
		$("#txtCadGrupoNome").val( "" );
    	$("#PopModalDetalheGrupoTit").html(" - "+TipoModal);
					
		if ( TipoModal == "Alterar" || TipoModal == "Visualizar" ){
				
			var IdGrupo = "";

			$("#TabGrupos li a").each(function () { 
				if ( $(this).hasClass( "active" ) == true )
				IdGrupo = $(this).attr('id');
			});

			IdGrupo = IdGrupo.replace("Tab", "");

			if ( IdGrupo == "" ){
				fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Grupo não informado!');
				return;
			}
			
			var NomeGrupo = $("#Tab"+IdGrupo).html();
			var iPos      = NomeGrupo.indexOf(" <span");
			if ( iPos > 0 );
				NomeGrupo = NomeGrupo.substring(0, iPos ).trim();
			
			$("#txtCadGrupoId").val(   IdGrupo   );
			$("#txtCadGrupoNome").val( NomeGrupo );
		}
		
		$('#PopModalDetalheGrupo').modal({backdrop: 'static'});
		
		$('#PopModalDetalheGrupo').on('shown.bs.modal', function() {
			$('#txtCadGrupoNome').focus();
		})
		

    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fValidarDadosGrupo() {	
	try {
		
		fLimparAreaAlertaModalCad();
		
		if( $("#txtCadGrupoNome").val() == "" ){
			fCriarAlertaModalCad(TP_ALERTA_AVISO, "Por favor, preencha o campo Nome!");
			return false;
		}	
		
		return true;
	
	} catch (e) {
		fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return false;
	} 
}

function fSalvarDadosGrupo( urlPadrao ){
	try {
		
		if ( !fValidarDadosGrupo() )
			return false;

		iniciarAnimacaoSalvar();

		var Id   = $("#txtCadGrupoId").val(); 
		var Nome = $("#txtCadGrupoNome").val(); 
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "ativo/salvargrupo",
			data    : { Id : Id, Nome : Nome },
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
					
					$("#PopModalDetalheGrupo").modal("hide");					
					fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					
					if ( Id == '' ){
						fCarregarListaGrupos( urlPadrao, Id );
						fCarregarGrid(        urlPadrao     );	
					}
					else{
						$("#Tab"+Id).html( Nome );
					}					
					
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

function fAbrirModalRemoverGrupo() {
    try {

       $("#txtDelGrupoId").val("");
	   
		var IdGrupo = "";

		$("#TabGrupos li a").each(function () { 
			if ( $(this).hasClass( "active" ) == true )
				IdGrupo = $(this).attr('id');
		 });
		 
		IdGrupo = IdGrupo.replace("Tab", "");
	   
       if ( IdGrupo  == "" ){
          fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Grupo não informado!'); 
          return;
        }
      
       $("#txtDelGrupoId").val( IdGrupo );
	   
       $("#PopModalDelGrupo").modal({backdrop: "static"});

    } catch (e) {
        $("#PopModalDelGrupo").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fExcluirDadosGrupo( urlPadrao ) {
    try {

		finalizarAnimacaoExcluir();

		var IdGrupo = $("#txtDelGrupoId").val();

		if ( IdGrupo == "" ){
			fCriarAlertaModalExc(TP_ALERTA_AVISO, 'Id. Grupo não informado!');
			return;
		}

		iniciarAnimacaoExcluir();
	  
		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "ativo/excluirgrupo",
			data: {  IdGrupo : IdGrupo },
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
					$("#txtDelGrupoId").val("");
					$("#PopModalDelGrupo").modal("hide");
					fCarregarListaGrupos( urlPadrao, '' );
					fCarregarGrid(        urlPadrao     );
					return true;
				} else {
					fCriarAlertaModalExc(TP_ALERTA_ERRO, mensagem); 
					return false;
				}
				
			},
			error: function (data) {
				$("#PopModalDelGrupo").modal("hide");
				finalizarAnimacaoExcluir();
				fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
			}
		});

    } catch (e) {
        $("#PopModalDelGrupo").modal("hide");
        finalizarAnimacaoExcluir();
		fCriarAlertaModalExc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fAbrirModalDetalheAtivo( urlPadrao ) {
    try {

		$("#AreaAlertaModalCadAtivo").html("");
		
		$("#txtCadAtivoCodigo").val("");
		fDefinirPadraoSelect('txtCadAtivoCodigo');
		
		$('#PopModalDetalheAtivo').modal({backdrop: 'static'});
		
		$('#PopModalDetalheAtivo').on('shown.bs.modal', function() {
			$('#txtCadAtivoCodigo').focus();
		})

    } catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}

function fCriarAlertaModalCadAtivo(Tipo, Mensagem){
	
	var DivAlerta = $("<div/>"); 
	DivAlerta.addClass( "alert "+Tipo+" alert-dismissible fade show" ); 
	DivAlerta.attr("id", 'DivAlerta'+fGerarNumeroAleatorio());
	DivAlerta.append( '<button type="button" class="close" data-dismiss="alert" aria-label="Close"> <span aria-hidden="true">&times;</span> </button>' );	
	if ( Tipo == TP_ALERTA_AVISO   ) DivAlerta.append( '<small> <strong>Aviso:</strong> '+Mensagem+'</small> ' );
	if ( Tipo == TP_ALERTA_SUCESSO ) DivAlerta.append( '<small> <strong>OK:</strong> '+Mensagem+'</small> ' );
	if ( Tipo == TP_ALERTA_ERRO    ) DivAlerta.append( '<small> <strong>Erro:</strong> '+Mensagem+'</small> ' );
	if ( Tipo == TP_ALERTA_ALERTA  ) DivAlerta.append( '<small> <strong>Alerta:</strong> '+Mensagem+'</small> ' );
	DivAlerta.delay(5000).fadeOut("slow", function () { $(this).remove(); });
	
	$("#AreaAlertaModalCadAtivo").append( DivAlerta );	
}

function fValidarDadosAtivo() {	
	try {
		
		$("#AreaAlertaModalCadAtivo").html("");
		
		if( $("#txtCadAtivoCodigo").val() == "" ){
			fCriarAlertaModalCadAtivo(TP_ALERTA_AVISO, 'Por favor, preencha o campo Cód Ativo!'); 
			return false;
		}	
		
		return true;
	
	} catch (e) {
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return false;
	} 
}

function fSalvarDadosAtivo( urlPadrao ){
	try {

		var IdGrupo = "";
		$("#TabGrupos li a").each(function () { 
			if ( $(this).hasClass( "active" ) == true )
				IdGrupo = $(this).attr('id');
		 });
		 
	   IdGrupo = IdGrupo.replace("Tab", "");
       if ( IdGrupo  == "" ){
          fCriarAlertaModalCadAtivo(TP_ALERTA_AVISO, 'Id. Grupo não informado!'); 
          return;
        }
		
		if ( !fValidarDadosAtivo() ) return false;

		iniciarAnimacaoSalvar();

		var CodAtivo = $("#txtCadAtivoCodigo").val(); 
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "ativo/salvarativo",
			data    : { IdGrupo : IdGrupo, CodAtivo: CodAtivo },
			success: function(result) {  
			
				finalizarAnimacaoSalvar();
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaModalCadAtivo(TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlertaModalCadAtivo(TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					$("#PopModalDetalheAtivo").modal("hide");					
					fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					fCarregarGrid( urlPadrao );	
				} else {
					fCriarAlertaModalCadAtivo(TP_ALERTA_ERRO, mensagem); 
					return;
				}
				
			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				finalizarAnimacaoSalvar();
				fCriarAlertaModalCadAtivo(TP_ALERTA_ERRO, MSG_ALERTA_ERRO );// request.responseText // MSG_ALERTA_ERRO
				return;
			}
		});
	
	
	} catch (e) {
		finalizarAnimacaoSalvar();
		fCriarAlertaModalCadAtivo(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function fAbrirModalRemoverAtivo( urlPadrao, IdUserGrupo, IdUserAtivo, CodAtivo ) {
    try {
		
		fLimparAreaAlertaPrinc();	

		if ( IdUserGrupo == "" ){
			fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Grupo não informado!');
			return;
		}

		if ( IdUserAtivo == "" ){
			fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Ativo não informado!');
			return;
		}

		if ( CodAtivo == "" ){
			fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Cód Ativo não informado!');
			return;
		}
	  
		$.ajax({
			dataType: "json",
			type: "post",
			url : urlPadrao + "ativo/excluirativo",
			data: {  IdUserGrupo: IdUserGrupo, IdUserAtivo: IdUserAtivo, CodAtivo: CodAtivo },
			success: function (result) {			
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
					return false;
				} else if (resultado == "FALHA") {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {					
				    fCriarAlertaPrinc(TP_ALERTA_SUCESSO, mensagem); 
					fCarregarGrid( urlPadrao );	
					return true;
				} else {
					fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
					return false;
				}
				
			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText // MSG_ALERTA_ERRO
			}
		});

    } catch (e) {
        $("#PopModalDelGrupo").modal("hide");
		fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    }
}
