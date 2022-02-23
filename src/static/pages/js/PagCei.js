
var PagCeiSitLanc   = '';
var PagCeiLstIdxTr  = [];
var PagCeiLstIdOper = [];
var PagCeiLstIdProv = [];

$(document).ready(function(){

	//$(this).attr("title", ":: TnB - CEI ::");
	$("#MnPrincCei").addClass("active open");

	fLimparAreaAlertaPrinc();
	fLimparAreaAlertaModalCad();
	fLimparAreaAlertaModalExc();
  fLimparAreaAlerta("AlertaModalDadosCei");

  // Operações
  idxGridSel      = 0;
  idxGridData     = 1;
  idxGridTipo     = 2;
  idxGridAtivo    = 3;
  idxGridQuant    = 4;
  idxGridPreco    = 5;
  idxGridTotal    = 6;
  idxGridCorret   = 7;
  idxGridSitDescr = 8;
  idxGridIdOper   = 9;
  idxGridIdSit    =10;
  idxGridAcao     =11;

  // Operações
  widthGridSel      = "15px";
  widthGridData     = "40px";
  widthGridTipo     = "50px";
  widthGridAtivo    = "40px";
  widthGridQuant    = "50px";
  widthGridPreco    = "50px";
  widthGridTotal    = "70px";
  widthGridCorret   = "90px";
  widthGridSitDescr = "50px";
  widthGridIdOper   = "";
  widthGridIdSit    = "";
  widthGridAcao     = "30px";

  // Proventos
  idxGridProvSel        = 0;
  idxGridProvDataPagto  = 1;
  idxGridProvTipo       = 2;
  idxGridProvAtivo      = 3;
  idxGridProvQuant      = 4;
  idxGridProvTotBruto   = 5;
  idxGridProvTotLiquido = 6;
  idxGridProvCorret     = 7;
  idxGridProvSitDescr   = 8;
  idxGridProvIdProv     = 9;
  idxGridProvIdSit      =10;
  idxGridProvAcao       =11;

  // Proventos
  widthGridProvSel        = "15px";
  widthGridProvDataPagto  = "40px";
  widthGridProvTipo       = "50px";
  widthGridProvAtivo      = "40px";
  widthGridProvQuant      = "50px";
  widthGridProvTotBruto   = "70px";
  widthGridProvTotLiquido = "70px";
  widthGridProvCorret     = "90px";
  widthGridProvSitDescr   = "50px";
  widthGridProvIdProv     = "";
  widthGridProvIdSit      = "";
  widthGridProvAcao       = "30px";

  $('#ckTodos').click(function()     { var check = $(this).is(':checked'); $('.check-cei-oper').each(function() { $(this).prop("checked", check); }); });
  $('#ckTodosProv').click(function() { var check = $(this).is(':checked'); $('.check-cei-prov').each(function() { $(this).prop("checked", check); }); });

  $("#FormOper input[type=text]").bind("keyup change", function(){ fCalcularPrecoTotal();  fCalcularOperacao();  });
  //$("#txtDetOperTxLiquid" ).click(function(){                      fCalcularTaxaLiquid();  fCalcularOperacao();  });
  //$("#txtDetOperTxEmol" ).click(function(){                        fCalcularTaxaEmol();    fCalcularOperacao();  });
  //$("#txtDetOperTxIRRF" ).click(function(){                        fCalcularTaxaIRRF();    fCalcularOperacao();  });

  $("#txtDivQuant").bind("keyup change",      function(){ fCalcularDividendo(); } );
  $("#txtDivPreco").bind("keyup change",      function(){ fCalcularDividendo(); } );
  $("#selDivTipo").bind("change",             function(){ fMostrarCalcVlrLiq(); fMostrarValorBruto(); fCalcularDividendo(); } );
  $("#txtDivCalcVlrLiq").bind("change",       function(){ fMostrarValorBruto(); fCalcularDividendo(); } );
  $("#txtDivPrecoBruto" ).unbind( "keyup"  );
  $("#txtDivPrecoBruto" ).unbind( "change" );

});

function fAbrirModalDadosCei() {
  try {

        fLimparAreaAlerta("AlertaModalDadosCei");

        $("#txtDetCeiCpf").val(        FormatarCPFCNPJ(CeiCpf) );
        $("#txtDetCeiSenha").val(      ""                      );
        $("#txtDetCeiDtHrDescr").html( CeiDtHrDescr            );

        $("#txtDetCeiSitDescr").removeClass("text-muted"); 
        $("#txtDetCeiSitDescr").removeClass("text-success");
        $("#txtDetCeiSitDescr").removeClass("text-danger"); 

        if(CeiSit == "A"){
          $("#txtDetCeiSitDescr").html('Habilitada');
          $("#txtDetCeiSitDescr").addClass('text-success');
        } else if(CeiSit == "I"){
          $("#txtDetCeiSitDescr").html('Desabilitada');
          $("#txtDetCeiSitDescr").addClass('text-danger');
        } else{
          $("#txtDetCeiSitDescr").html('Desconhedida');
          $("#txtDetCeiSitDescr").addClass('table-muted');
        }                                                         

        $('#PopModalDadosCEI').modal({backdrop: 'static'});  

        $("#txtDetCeiCpf").focus();

  } catch (e) {
    fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}

function iniciarAnimacaoSalvarCei() {
  $("#iDadosCeiSalvar").removeClass("fa-check");
  $("#iDadosCeiSalvar").addClass("fa-spinner");
  $("#iDadosCeiSalvar").addClass("fa-pulse");
  $("#BtnModalDadosCeiSalvar").addClass("disabled");
}

function finalizarAnimacaoSalvarCei() {
  $("#iDadosCeiSalvar").removeClass("fa-spinner");
  $("#iDadosCeiSalvar").removeClass("fa-pulse");
  $("#iDadosCeiSalvar").addClass("fa-check");
  $("#BtnModalDadosCeiSalvar").removeClass("disabled");
}

async function fSalvarDadosCei( urlPadrao ){
  try {

       promise = new Promise( (resolve, reject) => {

          fLimparAreaAlertaPrinc();
          finalizarAnimacaoSalvarCei();
          iniciarAnimacaoSalvarCei();
          
          var txtCPF   = tirarFormacataoCPFCNPJ( $("#txtDetCeiCpf").val().trim() ); 
          var txtSenha = $("#txtDetCeiSenha").val().trim(); 

          if( txtCPF != ""){
             
             if( !ValidarCPF( document.getElementById('txtDetCeiCpf') ) ){
                finalizarAnimacaoSalvarCei();
                fCriarAlerta("AlertaModalDadosCei", TP_ALERTA_AVISO, 'CPF inválido!'); 
                return;
             }

             if( txtSenha == "" ){
                finalizarAnimacaoSalvarCei();
                fCriarAlerta("AlertaModalDadosCei", TP_ALERTA_AVISO, 'Senha não informada!'); 
                return;
             }

          }

           if( txtSenha != "" ){
                if( txtCPF == ""){
                  finalizarAnimacaoSalvarCei();
                  fCriarAlerta("AlertaModalDadosCei", TP_ALERTA_AVISO, 'CPF não informado!'); 
                  return;
                } 
           }

          $.ajax({
            cache   : "false",
            dataType: "json",
            async   : true,
            type    : "POST",
            url     : urlPadrao + "cei/salvar",
            data    : { txtCPF: txtCPF, txtSenha: txtSenha },
            success: function(result) {  

              finalizarAnimacaoSalvarCei();

              var resultado = result.data.Resultado; 
              var mensagem  = result.data.Mensagem; 
              var Dados     = result.data.Dados; 

              if (resultado == "NSESSAO") {
                  $(location).attr('href', urlPadrao + '/login');
                  return false;
               } else if (resultado == "NOK") {
                  fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
                  return;
              } else if (resultado == "OK") {
                  CeiCpf = FormatarCPFCNPJ(Dados.Cpf);
                  CeiSit = Dados.Sit;
                  $("#PopModalDadosCEI").modal("hide");
                  if(CeiSit == "A"){
                    fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Importação Habilitada com Sucesso!'); 
                  } else{
                    fCriarAlertaPrinc(TP_ALERTA_SUCESSO, 'Importação Desabilitada com Sucesso!'); 
                  }   
              } else {
                fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                return;
              }
          
            },
            error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
              finalizarAnimacaoSalvarCei();
              fCriarAlerta("AlertaModalDadosCei", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);   // request.responseText //MSG_ALERTA_ERRO
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
        finalizarAnimacaoSalvarCei();
        fCriarAlerta("AlertaModalDadosCei", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    finalizarAnimacaoSalvarCei();
    fCriarAlerta("AlertaModalDadosCei", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  return;
  }
}

function iniciarAnimacaoPesquisar() {
  $("#iRefresh").addClass("fa-spin");
  $("#btnCeiPesquisar").addClass("disabled");
}

function finalizarAnimacaoPesquisa() {
  $("#iRefresh").removeClass("fa-spin");
  $("#btnCeiPesquisar").removeClass("disabled");
}

function fLimparGrid( urlPadrao ){    
  $("#selCeiAtivo").val(   ""              );
  $("#txtCeiDataIni").val( fDataPrimeira() );
  $("#txtCeiDataFim").val( fDataUltima()   ); 
  fLimparSomenteGrid(      urlPadrao       ); 
}

async function fLimparSomenteGrid( urlPadrao ){
  try { 

     promise = new Promise( (resolve, reject) => {

      
        finalizarAnimacaoPesquisa();
        
        if ( $("#Grid").length <= 0 ) {
            return;
        }
        
        $("th").addClass('text-center');

        $('#Grid').dataTable().fnClearTable();
        $("#Grid").dataTable({ bDestroy: true }).fnDestroy();

        $('#Grid').DataTable( {
            data: [],
            oLanguage: fTraduzirGrid(), 
            aoColumns: [
              { bSortable: false, sWidth: widthGridSel,      targets: idxGridSel      }, 
              { bSortable: false, sWidth: widthGridData,     targets: idxGridData     },
              { bSortable: false, sWidth: widthGridTipo,     targets: idxGridTipo     },
              { bSortable: false, sWidth: widthGridAtivo,    targets: idxGridAtivo    },
              { bSortable: false, sWidth: widthGridQuant,    targets: idxGridQuant    },
              { bSortable: false, sWidth: widthGridPreco,    targets: idxGridPreco    },
              { bSortable: false, sWidth: widthGridTotal,    targets: idxGridTotal    },
              { bSortable: false, sWidth: widthGridCorret,   targets: idxGridCorret   },
              { bSortable: false, sWidth: widthGridSitDescr, targets: idxGridSitDescr },
              { visible  : false,                            targets: idxGridIdOper   },
              { visible  : false,                            targets: idxGridIdSit    },
              { bSortable: false,  sWidth: widthGridAcao,    targets: idxGridAcao     }
            ],
            // order          : [[ idxGridIdOper, "asc" ], [ idxGridData, "desc" ], [ idxGridAtivo, "desc" ], [ idxGridTipo, "desc" ]],
            bLengthChange  : false,
            bFilter        : false,
            searchable     : true,
            orderable      : false,
            bAutoWidth     : false
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

          var indexTr = -1;
        
            var table = $('#Grid').DataTable( {
                processing: true,
                serverSide: false,
                oLanguage: fTraduzirGrid(), 
                data: dataSet,
                aoColumns: [
                    { bSortable: false, sWidth: widthGridSel,       targets: idxGridSel,      render: function ( data, type, row ) { if ( type == "display") var SitRend = row[idxGridIdSit]; if ( SitRend == "I") return "<input class='check-cei-oper' type='checkbox' id='ckSelOper-"+row[idxGridIdOper]+"'/>"; return data; } },
                    { bSortable: false, sWidth: widthGridData,      targets: idxGridData,     render: function ( data, type, row ) { if ( type == "display") return colcarFormacataoData(row[idxGridData]); return data; }  }, 
                    { bSortable: false, sWidth: widthGridTipo,      targets: idxGridTipo,     render: function ( data, type, row ) { if ( type == "display") return row[idxGridTipo]; return data; } }, 
                    { bSortable: false, sWidth: widthGridAtivo,     targets: idxGridAtivo,    render: function ( data, type, row ) { if ( type == "display") return row[idxGridAtivo]; return data; } }, 
                    { bSortable: false, sWidth: widthGridQuant,     targets: idxGridQuant,    render: function ( data, type, row ) { if ( type == "display") return colcarFormacataoInteiro(row[idxGridQuant]); return data; } }, 
                    { bSortable: false, sWidth: widthGridPreco,     targets: idxGridPreco,    render: function ( data, type, row ) { if ( type == "display") return "R$ " + row[idxGridPreco]; return data; } }, 
                    { bSortable: false, sWidth: widthGridTotal,     targets: idxGridTotal,    render: function ( data, type, row ) { if ( type == "display") return "R$ " + row[idxGridTotal]; return data; } }, 
                    { bSortable: false, sWidth: widthGridCorret,    targets: idxGridCorret,   render: function ( data, type, row ) { if ( type == "display") return row[idxGridCorret]; return data; } }, 
                    { bSortable: false, sWidth: widthGridSitDescr,  targets: idxGridSitDescr, render: function ( data, type, row ) { if ( type == "display") return row[idxGridSitDescr]; return data; } }, 
                    { visible  : false,                             targets: idxGridIdOper,   render: function ( data, type, row ) { if ( type == "display") return row[idxGridIdOper]; return data; } }, 
                    { visible  : false,                             targets: idxGridIdSit,    render: function ( data, type, row ) { if ( type == "display") return row[idxGridIdSit]; return data; } }, 
                    { bSortable: false, sWidth: widthGridAcao,      targets: idxGridAcao, 
                      render: function ( data, type, row ) {

                        var btnAdd = "";
                        var btnIgn = "";
                        var btnDis = '';
                        var btnCor = '';

                        if ( type == "display") {

                          indexTr      += 1;
                          var Data      = colcarFormacataoDataXML(row[idxGridData]); 
                          var TipoOper  = row[idxGridTipo].toUpperCase().substring(0, 1); 
                          var CodAtivo  = row[idxGridAtivo]; 
                          var Qtde      = parseFloat( GetValorInteiro( row[idxGridQuant] ) ); 
                          var Preco     = parseFloat( GetValorDecimal( row[idxGridPreco] ) );
                          var IdOper    = row[idxGridIdOper];
                          var SitRend   = row[idxGridIdSit];  // I-Importada // L-Lançada // C-Conferida

                          btnDis = '';
                          btnCor = 'success';
                          if ( (SitRend == 'L') || (SitRend == 'C') ){ // L-Lançada // C-Conferida
                            btnDis = ' disabled';
                            btnCor = 'muted';
                          }  
                          
                          btnAdd += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';

                          btnAdd += '<a id="BtnAddOper-'+indexTr+'" class="btn btn-sm btn-'+btnCor+' btn-icon btn-icon-mini btn-round btn-simple'+btnDis+'"'+btnDis+' style="font-size:0.5rem; " title="Adicionar Operação Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAbrirModalDetalheOperLocal( \''+urlPadrao+'\', \'\', \'Novo\', \''+TipoOper+'\', \''+CodAtivo+'\', \''+Qtde+'\', \''+fMascaraValor(Preco)+'\', \''+Data+'\', \''+indexTr+'\', \''+IdOper+'\' );">';
                          btnAdd += '   <i class="fa fa-plus-square fa-lg" aria-hidden="true"></i> ';
                          btnAdd += '</a>';

                          btnDis = '';
                          btnCor = 'info';
                          if ( (SitRend == 'L') || (SitRend == 'C') ){ // L-Lançada // C-Conferida
                            btnDis = ' disabled';
                            btnCor = 'muted';
                          }  

                          btnIgn += '<a id="BtnConfOper-'+indexTr+'" class="btn btn-sm btn-'+btnCor+' btn-icon btn-icon-mini btn-round btn-simple'+btnDis+'"'+btnDis+' style="font-size:0.5rem;" title="Marcar como Conferida Operação Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAlterarSitOperCei( \''+urlPadrao+'\', \'\', \''+IdOper+'\', \'C\', \''+indexTr+'\' );">'; // C-Conferida
                          btnIgn += '   <i class="fa fa-check fa-lg" aria-hidden="true"></i> ';
                          btnIgn += '</a>';
                          
                          btnIgn += '</div>';

                        }
                        
                        return btnAdd + '&nbsp;' + btnIgn;
                        
                      } 
                    }
                ],
                createdRow : function(row,data,dataIndex) {

                    var SitRend = data[idxGridIdSit];  // I-Importada // L-Lançada // C-Conferida

                    $('td', row).addClass('text-center');
                         if ( SitRend == "I" ) $('td', row).addClass('text-dark')   // $('td', row).eq(idxGridSitDescr).addClass('text-dark')  
                    else if ( SitRend == "L" ) $('td', row).addClass('text-success')
                    else if ( SitRend == "C" ) $('td', row).addClass('text-primary');

                }, //createdRow
                initComplete: function( settings, json ) {
                  finalizarAnimacaoPesquisa();
                },
                // order: [[ idxGridIdOper, "asc" ], [ idxGridData, "desc" ], [ idxGridAtivo, "desc" ], [ idxGridTipo, "desc" ]],
                dom: 'frtBpi', //Bfrtip //frtBip  //frtBpi
                buttons: [  
                      {
                         extend:    'excelHtml5',
                         text:      '<i class="fa fa-file-excel-o"></i> Excel',
                         className: 'btn btn-outline-default btn-sm',
                         title: NOME_PROJETO + ' - CEI - Operações',
                         titleAttr: 'Excel',
                         exportOptions: {  columns: [ idxGridData, idxGridTipo, idxGridAtivo, idxGridQuant, idxGridPreco, idxGridTotal, idxGridCorret, idxGridSitDescr ] },
                         customizeData: function (data) {
                                      for (var i = 0; i < data.body.length; i++) {
                                          for (var j = 0; j < data.body[i].length; j++) {
                                              if (j == idxGridQuant) data.body[i][j] = '\u200C' + data.body[i][j]; // Formatando a Coluna = 5-Quant == idxGridQuant
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
                          title: NOME_PROJETO + ' - CEI - Operações',
                          bom: true,
                          exportOptions: {  columns: [ idxGridData, idxGridTipo, idxGridAtivo, idxGridQuant, idxGridPreco, idxGridTotal, idxGridCorret, idxGridSitDescr ] } //orthogonal: 'export',
                      },
                      {
                      extend:    'pdfHtml5',
                          text:      '<i class="fa fa-file-pdf-o"></i> PDF',
                          className: 'btn btn-default btn-sm',
                          titleAttr: 'PDF',
                          title: NOME_PROJETO + ' - CEI - Operações', 
                          pageSize: 'A3',
                          alignment: 'center',
                          exportOptions: {  columns: [ idxGridData, idxGridTipo, idxGridAtivo, idxGridQuant, idxGridPreco, idxGridTotal, idxGridCorret, idxGridSitDescr ] }, //orthogonal: 'export',
                          footer: true,
                          customize: function (doc) { 
                            doc.defaultStyle.fontSize = 12; 
                            doc.styles.tableHeader.fontSize = 14; 
                          }
                      },
                      {
                          extend: 'print',
                          text:      '<i class="fa fa-print"></i> Imprimir',
                          title: NOME_PROJETO + ' - CEI - Operações',
                          titleAttr: 'Imprimir',
                          className: 'btn btn-default btn-sm',
                          exportOptions: {  columns: [ idxGridData, idxGridTipo, idxGridAtivo, idxGridQuant, idxGridPreco, idxGridTotal, idxGridCorret, idxGridSitDescr ] } //orthogonal: 'export',
                      }
                  ],      
                 //iDisplayLength : 100,
                  bPaginate: false,
                  bLengthChange: false,
                  bFilter: false,
                  searchable: false,
                  bAutoWidth: false,
                  bInfo: true,
                  bSearchable: false,
                  bSortable: false,
                  orderable: false,
                  bOrderable: false,
                  bOrdering: false
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

          finalizarAnimacaoPesquisa();
          iniciarAnimacaoPesquisar();

          fLimparAreaAlertaPrinc();

          if ( $("#Grid").length <= 0 ) {
              resolve(true);
              return;
          }

          $('#Grid').dataTable().fnClearTable();
          $("#Grid").dataTable({ bDestroy: true }).fnDestroy();  

          $('#ckTodos').prop("checked", false); 
                    
          var DataIni   = tirarFormacataoData($("#txtCeiDataIni").val().trim());
          var DataFim   = tirarFormacataoData($("#txtCeiDataFim").val().trim());
          var CodAtivo  = $("#selCeiAtivo").val();
          
          $.ajax({
            cache   : "false",
            dataType: "json",
            async   : true,
            type    : "POST",
            url     : urlPadrao + "cei/grid",
            data    : { DataIni: DataIni, DataFim: DataFim, CodAtivo: CodAtivo, },
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
              fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);   // request.responseText //MSG_ALERTA_ERRO
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
        finalizarAnimacaoPesquisa();
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });

    } catch (e) {
      finalizarAnimacaoPesquisa();
      fLimparSomenteGrid( urlPadrao );
      if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fProcurarAlterarLinhaGridOper( urlPadrao, lstIdxTr, sitLanc ){
  try {

       promise = new Promise( (resolve, reject) => {

            $('#Grid > tbody > tr').each(function(index, tr) { 
                if ( lstIdxTr.indexOf( index.toString() ) >= 0 ){ 
                  fAlterarLinhaGridOper( urlPadrao, $(this), index, sitLanc );   
                }
            });

            PagCeiSitLanc   = '';
            PagCeiLstIdxTr  = [];
            PagCeiLstIdOper = [];
            PagCeiLstIdProv = [];

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        finalizarAnimacaoSalvarCei();
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    finalizarAnimacaoSalvarCei();
    fCriarAlertaPrinc( TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  return;
  }
}

async function fAlterarLinhaGridOper( urlPadrao, trOper, indexTr, sitLanc ){
  try {

       promise = new Promise( (resolve, reject) => {

          $(trOper).find("td:eq("+idxGridSel+")").text('');

          $("#BtnAddOper-"+indexTr).removeClass('btn-success');
          $("#BtnAddOper-"+indexTr).addClass('btn-muted');
          $("#BtnAddOper-"+indexTr).addClass('disabled');

          $("#BtnConfOper-"+indexTr).removeClass('btn-info');
          $("#BtnConfOper-"+indexTr).addClass('btn-muted');
          $("#BtnConfOper-"+indexTr).addClass('disabled');

          $(trOper).children('td').removeClass('text-muted');
          
          if ( sitLanc == 'C'){
             $(trOper).find("td:eq("+idxGridSitDescr+")").text('Conferida');
             $(trOper).children('td').addClass('text-info');
          }
          
          if ( sitLanc == 'L'){
             $(trOper).find("td:eq("+idxGridSitDescr+")").text('Lançada');
             $(trOper).children('td').addClass('text-success');
          }

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        finalizarAnimacaoSalvarCei();
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    finalizarAnimacaoSalvarCei();
    fCriarAlertaPrinc( TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  return;
  }
}

async function fAlterarSitOperCei( urlPadrao, LstIdOper, IdOper, IdSit, indexTr, alterar = true ){
  try {

       promise = new Promise( (resolve, reject) => {
  
            if( IdOper != "" ) {
                LstIdOper = [];
                LstIdOper.push(IdOper);
            }

            if( LstIdOper.length <= 0 ){
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. não informado.');
              return;
            } 

            if( IdSit == "" ) {
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Situação não informada.');
              return;
            } 

            $.ajax({
              cache   : "false",
              dataType: "json",
              async   : true,
              type    : "POST",
              url     : urlPadrao + "cei/alterarlistasituacao",
              data    : { LstIdOper: LstIdOper, IdSit: IdSit },
              success: function(result) {  
                var resultado = result.data.Resultado; 
                var mensagem  = result.data.Mensagem; 
                if (resultado == "NSESSAO") {
                    $(location).attr('href', urlPadrao + '/login');
                    return false;
                 } else if (resultado == "NOK") {
                    fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
                    return;
                } else if (resultado == "OK") {
                    if ( alterar ) {
                        lstIdxTr = [];
                        lstIdxTr.push( indexTr.toString() );
                        fProcurarAlterarLinhaGridOper( urlPadrao, lstIdxTr, IdSit );
                    } // if ( alterar ) {
                } else {
                  fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                  return;
                }
              },
              error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
                fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);   // request.responseText //MSG_ALERTA_ERRO
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
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  return;
  }
}

function fAbrirModalDetalheOperLocal( urlPadrao, IdOper, TipoModal, TipoOper, CodAtivo, Quant, Preco, Data, pgCeiIndexTr, pgCeiIdOper ) {

  PagCeiSitLanc = 'L';

  PagCeiLstIdxTr = [];
  PagCeiLstIdxTr.push( pgCeiIndexTr.toString() );

  PagCeiLstIdOper = [];
  PagCeiLstIdProv = [];
  PagCeiLstIdOper.push(pgCeiIdOper);

  fAbrirModalDetalheOper(     urlPadrao, IdOper, TipoModal, TipoOper, CodAtivo, Quant, Preco, Data );
  // fCarregarModalCodigoAtivos( urlPadrao, TipoModal, 'C', CodAtivo );

}

async function fConferirLancOper( urlPadrao ) {
  try {

       promise = new Promise( (resolve, reject) => {

            var lanc_select   = false;
            var lanc_lst_oper = [];
            var lanc_sit      = 'C';

            $('#Grid > tbody > tr').each(function(index, tr) { 

                 var chkOper = $(this).find("td:eq("+idxGridSel+")").find("input:checked");

                 if( $(chkOper).length > 0 ){

                    lanc_select = true;

                    var IdOper = $(chkOper).attr('id').replace('ckSelOper-','');
                    lanc_lst_oper.push(IdOper);

                    fAlterarLinhaGridOper( urlPadrao, $(this), index, lanc_sit );

                }
            });

            if( lanc_select ) {
                fAlterarSitOperCei( urlPadrao, lanc_lst_oper, '', lanc_sit, 0, false );
                $('#ckTodos').prop("checked", false);
            }else{
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Nenhum item selecionado!'); 
            }

            resolve(true);
            // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    return;
  }
}

async function fAgruparLancOper( urlPadrao ) {
  try {

       promise = new Promise( (resolve, reject) => {

            var lanc_select   = false;
            var lanc_ok       = true;
            var lanc_data     = "";
            var lanc_tipo     = "";
            var lanc_ativo    = "";
            var lanc_qtde     = 0.00;
            var lanc_preco    = 0.00;
            var lanc_total    = 0.00;

            PagCeiSitLanc     = 'L';
            PagCeiLstIdxTr    = [];
            PagCeiLstIdOper   = [];
            PagCeiLstIdProv   = [];

            $('#Grid > tbody > tr').each(function(index, tr) { 

                 var chkOper = $(this).find("td:eq("+idxGridSel+")").find("input:checked");

                 if( $(chkOper).length > 0 ){

                      lanc_select = true;

                      var IdOper = $(chkOper).attr('id').replace('ckSelOper-','');
                      var data   = colcarFormacataoDataXMLPadrao( $(this).find("td:eq("+idxGridData+")").text().trim() );
                      var tipo   = $(this).find("td:eq("+idxGridTipo+")").text().trim().substr(0, 1);
                      var ativo  = $(this).find("td:eq("+idxGridAtivo+")").text().trim();
                      var qtde   = $(this).find("td:eq("+idxGridQuant+")").text().trim();
                      var total  = $(this).find("td:eq("+idxGridTotal+")").text().trim();

                      if ( lanc_data  == "" ) lanc_data  = data;
                      if ( lanc_tipo  == "" ) lanc_tipo  = tipo;
                      if ( lanc_ativo == "" ) lanc_ativo = ativo;

                      if ( lanc_data  != data  ) lanc_ok = false;
                      if ( lanc_tipo  != tipo  ) lanc_ok = false;
                      if ( lanc_ativo != ativo ) lanc_ok = false;

                      if ( !lanc_ok ) return false;

                      PagCeiLstIdxTr.push( index.toString() );
                      PagCeiLstIdOper.push(IdOper);

                      lanc_qtde  += parseInt( GetValorInteiro( qtde.replace('.', '').replace(',', '') ));
                      lanc_total += parseFloat( GetValorDecimal( total.replace('R$', '') ));

                } //if( $(chkOper).length > 0 ){

            });// $('#Grid > tbody > tr').each(function(index, tr) { 

            if( !lanc_select ){
              PagCeiSitLanc     = '';
              PagCeiLstIdxTr    = [];
              PagCeiLstIdOper   = [];
              PagCeiLstIdProv   = [];
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Nenhum item selecionado!');
            } else if( !lanc_ok ){
              PagCeiSitLanc     = '';
              PagCeiLstIdxTr    = [];
              PagCeiLstIdOper   = [];
              PagCeiLstIdProv   = [];
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Para Agrupar os Lançamentos em uma única Operação, somente é permitido a mesma Data, Tipo e Ativo...');
            } else{
                 $('#ckTodos').prop("checked", false); 
                 if ( (lanc_qtde > 0.00) && (lanc_total > 0.00) ) 
                     lanc_preco = (lanc_total / lanc_qtde );
                 fAbrirModalDetalheOper( urlPadrao, '', 'Novo', lanc_tipo, lanc_ativo, lanc_qtde.toString(), fMascaraValor(lanc_preco), lanc_data );
                 //fCarregarModalCodigoAtivos( urlPadrao, 'Novo', 'C', lanc_ativo );
            }; 

            resolve(true);
            // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      });
  
  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);  
    return;
  }
}

function iniciarAnimacaoPesquisarProv() {
  $("#iProvRefresh").addClass("fa-spin");
  $("#btnCeiProvPesquisar").addClass("disabled");
}

function finalizarAnimacaoPesquisaProv() {
  $("#iProvRefresh").removeClass("fa-spin");
  $("#btnCeiProvPesquisar").removeClass("disabled");
}

function fLimparGridProv( urlPadrao ){    
  $("#selCeiProvAtivo").val(   ""              );
  $("#txtCeiProvDataIni").val( fDataPrimeira() );
  $("#txtCeiProvDataFim").val( ""              );  // fDataUltima()
  fLimparSomenteGridProv(      urlPadrao       ); 
}

function fLimparSomenteGridProv( urlPadrao ){
  try { 
  
    finalizarAnimacaoPesquisaProv();
    
    $("th").addClass('text-center');
    
    if ( $("#GridProv").length <= 0 ) {
        return;
    }

    $('#GridProv').dataTable().fnClearTable();
    $("#GridProv").dataTable({ bDestroy: true }).fnDestroy();

    $('#GridProv').DataTable( {
        data: [],
        oLanguage: fTraduzirGrid(), 
        aoColumns: [
          { bSortable: false, sWidth: widthGridProvSel,        targets: idxGridProvSel        }, 
          { bSortable: false, sWidth: widthGridProvDataPagto,  targets: idxGridProvDataPagto  },
          { bSortable: false, sWidth: widthGridProvTipo,       targets: idxGridProvTipo       },
          { bSortable: false, sWidth: widthGridProvAtivo,      targets: idxGridProvAtivo      },
          { bSortable: false, sWidth: widthGridProvQuant,      targets: idxGridProvQuant      },
          { bSortable: false, sWidth: widthGridProvTotBruto,   targets: idxGridProvTotBruto   },
          { bSortable: false, sWidth: widthGridProvTotLiquido, targets: idxGridProvTotLiquido },
          { bSortable: false, sWidth: widthGridProvCorret,     targets: idxGridProvCorret     },
          { bSortable: false, sWidth: widthGridProvSitDescr,   targets: idxGridProvSitDescr   },
          { visible  : false,                                  targets: idxGridProvIdProv     },
          { visible  : false,                                  targets: idxGridProvIdSit      },
          { bSortable: false,  sWidth: widthGridProvAcao,      targets: idxGridProvAcao       }
        ],
        // order          : [[ idxGridProvDataPagto, "asc" ], [ idxGridProvIdProv, "asc" ], [ idxGridProvAtivo, "asc" ], [ idxGridProvTipo, "asc" ]],
        bLengthChange  : false,
        bFilter        : false,
        searchable     : true,
        orderable      : false,
        bAutoWidth     : false
    });

  } catch(e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}

async function fMontarGridProv( urlPadrao, dataSet ){
  try {  

       promise = new Promise( (resolve, reject) => {


          var indexTr = -1;
      
          var table = $('#GridProv').DataTable( {
              processing: true,
              serverSide: false,
              oLanguage: fTraduzirGrid(), 
              data: dataSet,
              aoColumns: [
                  { bSortable: false, sWidth: widthGridProvSel,        targets: idxGridProvSel,        render: function ( data, type, row ) { if ( type == "display") var SitRend = row[idxGridProvIdSit]; if ( SitRend == "I") return "<input class='check-cei-prov' type='checkbox' id='ckSelProv-"+row[idxGridProvIdProv]+"'/>"; return data; } },
                  { bSortable: false, sWidth: widthGridProvDataPagto,  targets: idxGridProvDataPagto,  render: function ( data, type, row ) { if ( type == "display") return colcarFormacataoData(row[idxGridProvDataPagto]); return data; }  }, 
                  { bSortable: false, sWidth: widthGridProvTipo,       targets: idxGridProvTipo,       render: function ( data, type, row ) { if ( type == "display") return row[idxGridProvTipo]; return data; } }, 
                  { bSortable: false, sWidth: widthGridProvAtivo,      targets: idxGridProvAtivo,      render: function ( data, type, row ) { if ( type == "display") return row[idxGridProvAtivo]; return data; } }, 
                  { bSortable: false, sWidth: widthGridProvQuant,      targets: idxGridProvQuant,      render: function ( data, type, row ) { if ( type == "display") return colcarFormacataoInteiro(row[idxGridProvQuant]); return data; } }, 
                  { bSortable: false, sWidth: widthGridProvTotBruto,   targets: idxGridProvTotBruto,   render: function ( data, type, row ) { if ( type == "display") return "R$ " + row[idxGridProvTotBruto]; return data; } }, 
                  { bSortable: false, sWidth: widthGridProvTotLiquido, targets: idxGridProvTotLiquido, render: function ( data, type, row ) { if ( type == "display") return "R$ " + row[idxGridProvTotLiquido]; return data; } }, 
                  { bSortable: false, sWidth: widthGridProvCorret,     targets: idxGridProvCorret,     render: function ( data, type, row ) { if ( type == "display") return row[idxGridProvCorret]; return data; } }, 
                  { bSortable: false, sWidth: widthGridProvSitDescr,   targets: idxGridProvSitDescr,   render: function ( data, type, row ) { if ( type == "display") return row[idxGridProvSitDescr]; return data; } }, 
                  { visible  : false,                                  targets: idxGridProvIdProv,     render: function ( data, type, row ) { if ( type == "display") return row[idxGridProvIdProv]; return data; } }, 
                  { visible  : false,                                  targets: idxGridProvIdSit,      render: function ( data, type, row ) { if ( type == "display") return row[idxGridProvIdSit]; return data; } }, 
                  { bSortable: false, sWidth: widthGridProvAcao,       targets: idxGridProvAcao, 
                    render: function ( data, type, row ) {

                      var btnAdd = "";
                      var btnIgn = "";
                      var btnDis = '';
                      var btnCor = '';

                      if ( type == "display") {

                        indexTr       += 1;
                        var DtEx       = ''; 
                        var DtPagto    = colcarFormacataoDataXML(row[idxGridProvDataPagto]); 
                        var TipoProv   = row[idxGridProvTipo].toUpperCase().substring(0, 1); 
                        var CodAtivo   = row[idxGridProvAtivo]; 
                        var Qtde       = parseFloat( GetValorInteiro( row[idxGridProvQuant] ) ); 
                        var TotBruto   = parseFloat( GetValorDecimal( row[idxGridProvTotBruto] ) );
                        var TotLiquido = parseFloat( GetValorDecimal( row[idxGridProvTotLiquido] ) );
                        var Preco      = 0.00;
                        var IdProv     = row[idxGridProvIdProv];
                        var SitRend    = row[idxGridProvIdSit];  // I-Importado // L-Lançado // C-Conferido

                        if ( (Qtde > 0.00) && (TotBruto > 0.00) ) Preco = (TotBruto / Qtde );
                        //if ( (Qtde > 0.00) && (TotLiquido > 0.00) ) Preco = (TotLiquido / Qtde );

                        btnDis = '';
                        btnCor = 'success';
                        if ( (SitRend == 'L') || (SitRend == 'C') ){ // L-Lançado // C-Conferido
                          btnDis = ' disabled';
                          btnCor = 'muted';
                        }  
                        
                        btnAdd += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';

                        btnAdd += '<a id="BtnAddProv-'+indexTr+'" class="btn btn-sm btn-'+btnCor+' btn-icon btn-icon-mini btn-round btn-simple'+btnDis+'"'+btnDis+' style="font-size:0.5rem; " title="Adicionar Provento Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAbrirModalDetalheRendCalendLocal( \''+urlPadrao+'\', \''+TipoProv+'\', \''+CodAtivo+'\', \''+DtEx+'\', \''+DtPagto+'\', \''+fMascaraValorMaior(Preco)+'\', \'Novo\', \''+Qtde+'\', \''+indexTr+'\', \''+IdProv+'\' );">';
                        btnAdd += '   <i class="fa fa-plus-square fa-lg" aria-hidden="true"></i> ';
                        btnAdd += '</a>';

                        btnDis = '';
                        btnCor = 'info';
                        if ( (SitRend == 'L') || (SitRend == 'C') ){ // L-Lançado // C-Conferido
                          btnDis = ' disabled';
                          btnCor = 'muted';
                        }  

                        btnIgn += '<a id="BtnConfProv-'+indexTr+'" class="btn btn-sm btn-'+btnCor+' btn-icon btn-icon-mini btn-round btn-simple'+btnDis+'"'+btnDis+' style="font-size:0.5rem;" title="Marcar como Conferido Provento Ativo '+CodAtivo+'" href="javascript:void(0);" onclick="fAlterarSitProvCei( \''+urlPadrao+'\', \'\', \''+IdProv+'\', \'C\', \''+indexTr+'\' );">'; // C-Conferida
                        btnIgn += '   <i class="fa fa-check fa-lg" aria-hidden="true"></i> ';
                        btnIgn += '</a>';
                        
                        btnIgn += '</div>';

                      }
                      
                      return btnAdd + '&nbsp;' + btnIgn;
                      
                    } 
                  }
              ],
              createdRow : function(row,data,dataIndex) {
                  var SitRend = data[idxGridProvIdSit];  // I-Importada // L-Lançada // C-Conferida
                  $('td', row).addClass('text-center');
                       if ( SitRend == "I" ) $('td', row).addClass('text-dark')   // $('td', row).eq(idxGridProvSitDescr).addClass('text-dark')  
                  else if ( SitRend == "L" ) $('td', row).addClass('text-success')
                  else if ( SitRend == "C" ) $('td', row).addClass('text-primary');

              }, //createdRow
              initComplete: function( settings, json ) {
                finalizarAnimacaoPesquisaProv();
              },
              // order: [[ idxGridProvDataPagto, "asc" ], [ idxGridProvIdProv, "asc" ], [ idxGridProvAtivo, "asc" ], [ idxGridProvTipo, "asc" ]],
              dom: 'frtBpi', //Bfrtip //frtBip  //frtBpi
              buttons: [  
                    {
                       extend:    'excelHtml5',
                       text:      '<i class="fa fa-file-excel-o"></i> Excel',
                       className: 'btn btn-outline-default btn-sm',
                       title: NOME_PROJETO + ' - CEI - Proventos',
                       titleAttr: 'Excel',
                       exportOptions: {  columns: [ idxGridProvDataPagto, idxGridProvTipo, idxGridProvAtivo, idxGridProvQuant, idxGridProvTotLiquido, idxGridProvTotBruto, idxGridProvCorret, idxGridProvSitDescr ] },
                       customizeData: function (data) {
                                    for (var i = 0; i < data.body.length; i++) {
                                        for (var j = 0; j < data.body[i].length; j++) {
                                            if (j == idxGridProvQuant) data.body[i][j] = '\u200C' + data.body[i][j]; // Formatando a Coluna = 5-Quant == idxGridProvQuant
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
                        title: NOME_PROJETO + ' - CEI - Proventos',
                        bom: true,
                        exportOptions: {  columns: [ idxGridProvDataPagto, idxGridProvTipo, idxGridProvAtivo, idxGridProvQuant, idxGridProvTotLiquido, idxGridProvTotBruto, idxGridProvCorret, idxGridProvSitDescr ] } //orthogonal: 'export',
                    },
                    {
                    extend:    'pdfHtml5',
                        text:      '<i class="fa fa-file-pdf-o"></i> PDF',
                        className: 'btn btn-default btn-sm',
                        titleAttr: 'PDF',
                        title: NOME_PROJETO + ' - CEI - Proventos', 
                        pageSize: 'A3',
                        alignment: 'center',
                        exportOptions: {  columns: [ idxGridProvDataPagto, idxGridProvTipo, idxGridProvAtivo, idxGridProvQuant, idxGridProvTotLiquido, idxGridProvTotBruto, idxGridProvCorret, idxGridProvSitDescr ] }, //orthogonal: 'export',
                        footer: true,
                        customize: function (doc) { 
                          doc.defaultStyle.fontSize = 12; 
                          doc.styles.tableHeader.fontSize = 14; 
                        }
                    },
                    {
                        extend: 'print',
                        text:      '<i class="fa fa-print"></i> Imprimir',
                        title: NOME_PROJETO + ' - CEI - Proventos',
                        titleAttr: 'Imprimir',
                        className: 'btn btn-default btn-sm',
                        exportOptions: {  columns: [ idxGridProvDataPagto, idxGridProvTipo, idxGridProvAtivo, idxGridProvQuant, idxGridProvTotLiquido, idxGridProvTotBruto, idxGridProvCorret, idxGridProvSitDescr ] } //orthogonal: 'export',
                    }
                ],      
               //iDisplayLength : 100,
                bPaginate: false,
                bLengthChange: false,
                bFilter: false,
                searchable: true,
                orderable: false,
                bAutoWidth: false,
                bInfo: true,
                bSearchable: false,
                bOrderable: false,
                bSortable: true,
                bOrdering: false
          });
        
          $( document ).ajaxError(function( event, request, settings, thrownError ) {
            fLimparSomenteGrid( urlPadrao );
            finalizarAnimacaoPesquisaProv();
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
        finalizarAnimacaoPesquisaProv();
        if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      }
}

async function fCarregarGridProv( urlPadrao ){
  try {   

       promise = new Promise( (resolve, reject) => {

          finalizarAnimacaoPesquisaProv();
          iniciarAnimacaoPesquisarProv();
          
          fLimparAreaAlertaPrinc();

          if ( $("#GridProv").length <= 0 ) {
              resolve(true);
              return;
          }
          
          $('#GridProv').dataTable().fnClearTable();
          $("#GridProv").dataTable({ bDestroy: true }).fnDestroy();  

          $('#ckTodosProv').prop("checked", false); 
          
          var DataIni   = tirarFormacataoData($("#txtCeiProvDataIni").val().trim());
          var DataFim   = tirarFormacataoData($("#txtCeiProvDataFim").val().trim());
          var CodAtivo  = $("#selCeiProvAtivo").val();

          $.ajax({
            cache   : "false",
            dataType: "json",
            async   : true,
            type    : "POST",
            url     : urlPadrao + "cei/gridprov",
            data    : { DataIni: DataIni, DataFim: DataFim, CodAtivo: CodAtivo, },
            success: function(result) {
              
                var resultado = result.data.Resultado; 
                var mensagem  = result.data.Mensagem; 
                var lista     = result.data.Lista;

                if (resultado == "NSESSAO") {
                  $(location).attr('href', urlPadrao + '/login');
                  return false;
                } else if (resultado == "NOK") {
                  finalizarAnimacaoPesquisaProv();
                  fLimparSomenteGridProv( urlPadrao );
                  fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
                  return;
                } else if (resultado == "FALHA") {
                  finalizarAnimacaoPesquisaProv();
                  fLimparSomenteGridProv( urlPadrao );
                  fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                  return;
                }else if (resultado == "OK") {
                  fMontarGridProv( urlPadrao, lista );
                } else{
                  finalizarAnimacaoPesquisaProv();
                  fLimparSomenteGridProv( urlPadrao );
                  fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                  return;
                }
              
            },
            error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
              finalizarAnimacaoPesquisaProv();
              fLimparSomenteGridProv( urlPadrao );
              fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);   // request.responseText //MSG_ALERTA_ERRO
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
        finalizarAnimacaoPesquisaProv();
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
    } catch (e) {
      finalizarAnimacaoPesquisaProv();
      fLimparSomenteGridProv( urlPadrao );
      if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    }
}

async function fProcurarAlterarLinhaGridProv( urlPadrao, lstIdxTr, sitLanc ){
  try {

       promise = new Promise( (resolve, reject) => {

            $('#GridProv > tbody > tr').each(function(index, tr) { 
                if ( lstIdxTr.indexOf( index.toString() ) >= 0 ){ 
                  fAlterarLinhaGridProv( urlPadrao, $(this), index, sitLanc );   
                }
            });

            PagCeiSitLanc   = '';
            PagCeiLstIdxTr  = [];
            PagCeiLstIdOper = [];
            PagCeiLstIdProv = [];

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        finalizarAnimacaoSalvarCei();
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    finalizarAnimacaoSalvarCei();
    fCriarAlertaPrinc( TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  return;
  }
}

async function fAlterarLinhaGridProv( urlPadrao, trProv, indexTr, sitLanc ){
  try {

       promise = new Promise( (resolve, reject) => {

          $(trProv).find("td:eq("+idxGridProvSel+")").text('');

          $("#BtnAddProv-"+indexTr).removeClass('btn-success');
          $("#BtnAddProv-"+indexTr).addClass('btn-muted');
          $("#BtnAddProv-"+indexTr).addClass('disabled');

          $("#BtnConfProv-"+indexTr).removeClass('btn-info');
          $("#BtnConfProv-"+indexTr).addClass('btn-muted');
          $("#BtnConfProv-"+indexTr).addClass('disabled');

          $(trProv).children('td').removeClass('text-muted');
          
          if ( sitLanc == 'C'){
             $(trProv).find("td:eq("+idxGridProvSitDescr+")").text('Conferido');
             $(trProv).children('td').addClass('text-info');
          }
          
          if ( sitLanc == 'L'){
             $(trProv).find("td:eq("+idxGridProvSitDescr+")").text('Lançado');
             $(trProv).children('td').addClass('text-success');
          }

        resolve(true);
        // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        finalizarAnimacaoSalvarCei();
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    finalizarAnimacaoSalvarCei();
    fCriarAlertaPrinc( TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  return;
  }
}

async function fAlterarSitProvCei( urlPadrao, LstIdProv, IdProv, IdSit, indexTr, alterar = true ){
  try {

       promise = new Promise( (resolve, reject) => {
  
            if( IdProv != "" ) {
                LstIdProv = [];
                LstIdProv.push(IdProv);
            } 

            if( LstIdProv.length <= 0 ){
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. não informado!'); 
              return;
            } 

            if( IdSit == "" ) {
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Situação não informada!'); 
              return;
            } 

            $.ajax({
              cache   : "false",
              dataType: "json",
              async   : true,
              type    : "POST",
              url     : urlPadrao + "cei/alterarlistasituacaoprov",
              data    : { LstIdProv: LstIdProv, IdSit: IdSit },
              success: function(result) {  
                var resultado = result.data.Resultado; 
                var mensagem  = result.data.Mensagem; 
                if (resultado == "NSESSAO") {
                    $(location).attr('href', urlPadrao + '/login');
                    return false;
                 } else if (resultado == "NOK") {
                    fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
                    return;
                } else if (resultado == "OK") {
                    if ( alterar ) {
                        lstIdxTr = [];
                        lstIdxTr.push( indexTr.toString() );
                        fProcurarAlterarLinhaGridProv( urlPadrao, lstIdxTr, IdSit );
                    } // if ( alterar ) {
                } else {
                  fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                  return;
                }
              },
              error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
                fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);   // request.responseText //MSG_ALERTA_ERRO
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
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  return;
  }
}

function fAbrirModalDetalheRendCalendLocal( urlPadrao, ProvTipo, ProvCodigo, ProvDtEx, ProvDtPagto, ProvValor, TipoInvest, ProvQuant, pgCeiIndexTr, pgCeiIdProv ) {

  PagCeiSitLanc = 'L';

  PagCeiLstIdxTr = [];
  PagCeiLstIdxTr.push( pgCeiIndexTr.toString() );

  PagCeiLstIdOper = [];
  PagCeiLstIdProv = [];
  PagCeiLstIdProv.push(pgCeiIdProv);

  fAbrirModalDetalheRendCalend( urlPadrao, ProvTipo, ProvCodigo, ProvDtEx, ProvDtPagto, ProvValor, TipoInvest, ProvQuant.toString() );

}

async function fConferirLancProv( urlPadrao ) {
  try {

       promise = new Promise( (resolve, reject) => {

            var lanc_select   = false;
            var lanc_lst_prov = [];
            var lanc_sit      = 'C';

            $('#GridProv > tbody > tr').each(function(index, tr) { 

                 var chkProv = $(this).find("td:eq("+idxGridProvSel+")").find("input:checked");

                 if( $(chkProv).length > 0 ){

                    lanc_select = true;

                    var IdProv = $(chkProv).attr('id').replace('ckSelProv-','');
                    lanc_lst_prov.push(IdProv);

                    fAlterarLinhaGridProv( urlPadrao, $(this), index, lanc_sit );

                }
            });

            if( lanc_select ) {
                fAlterarSitProvCei( urlPadrao, lanc_lst_prov, '', lanc_sit, 0, false );
                $('#ckTodosProv').prop("checked", false);
            }else{
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Nenhum item selecionado!'); 
            }

            resolve(true);
            // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
    return;
  }
}

async function fAgruparLancProv( urlPadrao ) {
  try {

       promise = new Promise( (resolve, reject) => {

            var lanc_select      = false;
            var lanc_ok          = true;
            var lanc_data_ex     = "";
            var lanc_data_pagto  = "";
            var lanc_tipo        = "";
            var lanc_ativo       = "";
            var lanc_qtde        = 0.00;
            var lanc_preco       = 0.00;
            var lanc_tot_bruto   = 0.00;
            var lanc_tot_liquido = 0.00;

            PagCeiSitLanc     = 'L';
            PagCeiLstIdxTr    = [];
            PagCeiLstIdOper   = [];
            PagCeiLstIdProv   = [];

            $('#GridProv > tbody > tr').each(function(index, tr) { 

                 var chkProv = $(this).find("td:eq("+idxGridProvSel+")").find("input:checked");

                 if( $(chkProv).length > 0 ){

                      lanc_select = true;

                      var IdProv     = $(chkProv).attr('id').replace('ckSelProv-','');
                      var data_pagto = colcarFormacataoDataXMLPadrao( $(this).find("td:eq("+idxGridProvDataPagto+")").text().trim() );
                      var tipo       = $(this).find("td:eq("+idxGridProvTipo+")").text().trim().substr(0, 1);
                      var ativo      = $(this).find("td:eq("+idxGridProvAtivo+")").text().trim();
                      var qtde       = $(this).find("td:eq("+idxGridProvQuant+")").text().trim();
                      var tot_bruto  = $(this).find("td:eq("+idxGridProvTotLiquido+")").text().trim();
                      var tot_liqudo = $(this).find("td:eq("+idxGridProvTotBruto+")").text().trim();

                      if ( lanc_data_pagto == "" ) lanc_data_pagto  = data_pagto;
                      if ( lanc_tipo       == "" ) lanc_tipo        = tipo;
                      if ( lanc_ativo      == "" ) lanc_ativo       = ativo;

                      if ( lanc_data_pagto != data_pagto ) lanc_ok = false;
                      if ( lanc_tipo       != tipo       ) lanc_ok = false;
                      if ( lanc_ativo      != ativo      ) lanc_ok = false;

                      if ( !lanc_ok ) return false;

                      PagCeiLstIdxTr.push( index.toString() );
                      PagCeiLstIdProv.push(IdProv);

                      lanc_qtde        += parseInt( GetValorInteiro( qtde.replace('.', '').replace(',', '') ));
                      lanc_tot_bruto   += parseFloat( GetValorDecimal( tot_bruto.replace('R$', '') ));
                      lanc_tot_liquido += parseFloat( GetValorDecimal( tot_liqudo.replace('R$', '') ));

                } //if( $(chkProv).length > 0 ){

            });// $('#Grid > tbody > tr').each(function(index, tr) { 

            if( !lanc_select ){
              PagCeiSitLanc     = '';
              PagCeiLstIdxTr    = [];
              PagCeiLstIdOper   = [];
              PagCeiLstIdProv   = [];
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Nenhum item selecionado!');
            } else if( !lanc_ok ){
              PagCeiSitLanc     = '';
              PagCeiLstIdxTr    = [];
              PagCeiLstIdOper   = [];
              PagCeiLstIdProv   = [];
              fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Para Agrupar os Lançamentos em um único Provento, somente é permitido a mensam Data, Tipo e Ativo...');
            } else{
                 $('#ckTodosProv').prop("checked", false); 
                 if ( (lanc_qtde > 0.00) && (lanc_tot_bruto > 0.00) ) lanc_preco = (lanc_tot_bruto / lanc_qtde );
                 // if ( (lanc_qtde > 0.00) && (lanc_tot_liquido > 0.00) ) lanc_preco = (lanc_tot_liquido / lanc_qtde );
                 fAbrirModalDetalheRendCalend( urlPadrao, lanc_tipo, lanc_ativo, lanc_data_ex, lanc_data_pagto, fMascaraValorMaior(lanc_preco), 'Novo', lanc_qtde.toString() );
            }; 

            resolve(true);
            // reject("aaaaaaaaaaaa") // reject(new Error("aaaaaaaaaaaa!"));
      })
      .then( txt => {
        //console.log('Sucesso: ' + txt);
      })
      .catch( txt => {
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      });
  
  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);  
    return;
  }
}
