

$(document).ready(function(){

	//$(this).attr("title", ":: TnB - Alertas ::");
	// $("#MnPrincCei").addClass("active open");

	fLimparAreaAlertaPrinc();
	fLimparAreaAlertaModalCad();
	fLimparAreaAlertaModalExc();

  // Grid Alertas
  idxGridDtHr        = 0;
  idxGridDtEnvio     = 1;
  idxGridNmUsuario   = 2;
  idxGridTipo        = 3;
  idxGridMensagem    = 4;
  idxGridSitTelegram = 5;
  idxGridSitEmail    = 6;
  idxGridIdUsuario   = 7;
  idxGridIdAlerta    = 8;
  idxGridAcao        = 9;

  // Grid Alertas
  widthGridDtHr        = "20px";
  widthGridDtEnvio     = "10px";
  widthGridNmUsuario   = "70px";
  widthGridTipo        = "60px";
  widthGridMensagem    = "120px";
  widthGridSitTelegram = "10px";
  widthGridSitEmail    = "10px";
  widthGridIdUsuario   = "";
  widthGridIdAlerta    = "";
  widthGridAcao        = "5px";

  // Grid User Alertas
  idxGridUserNmUsuario    = 0;
  idxGridUserTpAlerta     = 1;
  idxGridUserTpAssinatura = 2;
  idxGridUserIdUsuario    = 3;
  idxGridUserIdAssinatura = 4;
  idxGridUserSituacao     = 5;
  idxGridUserAcao         = 6;

  // Grid User Alertas
  widthGridUserNmUsuario    = "100px";
  widthGridUserTpAlerta     = "80px";
  widthGridUserTpAssinatura = "30px";
  widthGridUserIdUsuario    = "";
  widthGridUserIdAssinatura = "";
  widthGridUserSituacao     = "";
  widthGridUserAcao         = "10px";

});

function iniciarAnimacaoPesquisar() {
  $("#iRefresh").addClass("fa-spin");
  $("#btnPesquisar").addClass("disabled");
}

function finalizarAnimacaoPesquisa() {
  $("#iRefresh").removeClass("fa-spin");
  $("#btnPesquisar").removeClass("disabled");
}

function fLimparGrid( urlPadrao ){    
  $("#txtDataIni").val( fDataPrimeira() );
  $("#txtDataFim").val( fDataUltima()   ); 
  fLimparSomenteGrid(   urlPadrao       ); 
}

function fLimparSomenteGrid( urlPadrao ){
  try { 
  
    finalizarAnimacaoPesquisa();
    
    $("th").addClass('text-center');

    $('#Grid').dataTable().fnClearTable();
    $("#Grid").dataTable({ bDestroy: true }).fnDestroy();

    $('#Grid').DataTable( {
        data: [],
        oLanguage: fTraduzirGrid(), 
        aoColumns: [
          { bSortable: true,  sWidth: widthGridDtHr,        targets: idxGridDtHr        }, 
          { bSortable: true,  sWidth: widthGridDtEnvio,     targets: idxGridDtEnvio     },
          { bSortable: true,  sWidth: widthGridNmUsuario,   targets: idxGridNmUsuario   },
          { bSortable: true,  sWidth: widthGridTipo,        targets: idxGridTipo        },
          { bSortable: true,  sWidth: widthGridMensagem,    targets: idxGridMensagem    },
          { bSortable: true,  sWidth: widthGridSitTelegram, targets: idxGridSitTelegram },
          { bSortable: true,  sWidth: widthGridSitEmail,    targets: idxGridSitEmail    },
          { visible  : false,                               targets: idxGridIdUsuario   },
          { visible  : false,                               targets: idxGridIdAlerta    },
          { bSortable: false, sWidth: widthGridAcao,        targets: idxGridAcao        }
        ],
        // order          : [[ idxGridIdOper, "asc" ], [ idxGridData, "desc" ], [ idxGridAtivo, "desc" ], [ idxGridTipo, "desc" ]],
        bLengthChange  : false,
        bFilter        : true,
        searchable     : true,
        orderable      : true,
        bAutoWidth     : false
    });

  } catch(e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}

function fMontarGrid( urlPadrao, dataSet ){
  try {   

      var indexTr = -1;
  
      var table = $('#Grid').DataTable( {
          processing: true,
          serverSide: false,
          oLanguage: fTraduzirGrid(), 
          data: dataSet,
          aoColumns: [
              { bSortable: true,  sWidth: widthGridDtHr,        targets: idxGridDtHr,        render: function ( data, type, row ) { if ( type == "display") return colcarFormacataoDataHora(row[idxGridDtHr]); return data; }  }, 
              { bSortable: true,  sWidth: widthGridDtEnvio,     targets: idxGridDtEnvio,     render: function ( data, type, row ) { if ( type == "display") return colcarFormacataoData(row[idxGridDtEnvio]); return data; }  }, 
              { bSortable: true,  sWidth: widthGridNmUsuario,   targets: idxGridNmUsuario,   render: function ( data, type, row ) { if ( type == "display") return row[idxGridIdUsuario] + ' - ' + row[idxGridNmUsuario]; return data; } }, 
              { bSortable: true,  sWidth: widthGridTipo,        targets: idxGridTipo,        render: function ( data, type, row ) { if ( type == "display") return row[idxGridTipo]; return data; } }, 
              { bSortable: true,  sWidth: widthGridMensagem,    targets: idxGridMensagem,    render: function ( data, type, row ) { if ( type == "display") return trocar_tag_br(row[idxGridMensagem]); return data; } }, 
              { bSortable: true,  sWidth: widthGridSitTelegram, targets: idxGridSitTelegram, render: function ( data, type, row ) { if ( type == "display") return row[idxGridSitTelegram]; return data; } }, 
              { bSortable: true,  sWidth: widthGridSitEmail,    targets: idxGridSitEmail,    render: function ( data, type, row ) { if ( type == "display") return row[idxGridSitEmail]; return data; } }, 
              { visible  : false,                               targets: idxGridIdUsuario,   render: function ( data, type, row ) { if ( type == "display") return row[idxGridIdUsuario]; return data; } }, 
              { visible  : false,                               targets: idxGridIdAlerta,    render: function ( data, type, row ) { if ( type == "display") return row[idxGridIdAlerta]; return data; } }, 
              { bSortable: false, sWidth: widthGridAcao,        targets: idxGridAcao, 
                render: function ( data, type, row ) {

                  var btnGrid = "";

                  if ( type == "display") {

                    indexTr      += 1;
                    var IdUsuario = row[idxGridIdUsuario];
                    var IdAlerta  = row[idxGridIdAlerta];    

                    btnGrid += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';

                    btnGrid += '<a id="BtnExclAlerta-'+indexTr+'" class="btn btn-sm btn-danger btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Excluir Alerta('+IdAlerta+')" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fExcluirAlerta( \''+urlPadrao+'\', \''+IdAlerta+'\', \''+indexTr+'\' );">';
                    btnGrid += '   <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> ';
                    btnGrid += '</a>';

                    btnGrid += '</div>';
                  }
                  
                  return btnGrid; // + '&nbsp;' + btnIgn;
                  
                } 
              }
          ],
          createdRow : function(row,data,dataIndex) {
              var sit_telegram = data[idxGridSitTelegram]
              var sit_email    = data[idxGridSitEmail]
              
              $(row).attr('id', 'GridTr-'+dataIndex);
              //$('td', row).addClass('text-center');
             
              $('td', row).eq(idxGridNmUsuario).addClass('text-left');
              $('td', row).eq(idxGridTipo).addClass('text-left');
              $('td', row).eq(idxGridMensagem).addClass('text-left');  

              if ( sit_telegram == "Pendente"     ) $('td', row).eq(idxGridSitTelegram).addClass('text-muted'); 
              if ( sit_telegram == "Enviado"      ) $('td', row).eq(idxGridSitTelegram).addClass('text-success'); 
              if ( sit_telegram == "Erro"         ) $('td', row).eq(idxGridSitTelegram).addClass('text-danger');
              if ( sit_telegram == "Desconhecido" ) $('td', row).eq(idxGridSitTelegram).addClass('text-primary');

              if ( sit_email == "Pendente"     ) $('td', row).eq(idxGridSitEmail).addClass('text-muted'); 
              if ( sit_email == "Enviado"      ) $('td', row).eq(idxGridSitEmail).addClass('text-success'); 
              if ( sit_email == "Erro"         ) $('td', row).eq(idxGridSitEmail).addClass('text-danger');
              if ( sit_email == "Desconhecido" ) $('td', row).eq(idxGridSitEmail).addClass('text-primary');

          }, //createdRow
          initComplete: function( settings, json ) {
            finalizarAnimacaoPesquisa();
          },
          // order: [[ idxGridIdOper, "asc" ], [ idxGridData, "desc" ], [ idxGridAtivo, "desc" ], [ idxGridTipo, "desc" ]],
          //dom: 'frtBpi', //Bfrtip //frtBip  //frtBpi
           //iDisplayLength : 100,
            bPaginate: false,
            bLengthChange: false,
            bFilter: true,
            searchable: true,
            bAutoWidth: false,
            bInfo: true,
            bSearchable: true,
            bSortable: true,
            orderable: true,
            bOrderable: true,
            bOrdering: true
      });
    
      $( document ).ajaxError(function( event, request, settings, thrownError ) {
        fLimparSomenteGrid( urlPadrao );
        finalizarAnimacaoPesquisa();
      });

      } catch (e) {
        fLimparSomenteGrid( urlPadrao );
        finalizarAnimacaoPesquisa();
        if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      }
}

function fCarregarGrid( urlPadrao ){
  try {   

       promise = new Promise( (resolve, reject) => {

          fLimparAreaAlertaPrinc();

          finalizarAnimacaoPesquisa();
          iniciarAnimacaoPesquisar();

          $('#Grid').dataTable().fnClearTable();
          $("#Grid").dataTable({ bDestroy: true }).fnDestroy(); 
                    
          var DataIni = tirarFormacataoData($("#txtDataIni").val().trim());
          var DataFim = tirarFormacataoData($("#txtDataFim").val().trim());
          
          $.ajax({
            cache   : "false",
            dataType: "json",
            async   : true,
            type    : "POST",
            url     : urlPadrao + "alerta/grid",
            data    : { DataIni: DataIni, DataFim: DataFim, },
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

function fExcluirAlerta( urlPadrao, IdAlerta, indexTr ) {
    try {

      promise = new Promise( (resolve, reject) => {

           if ( IdAlerta == '' ) {
            fCriarAlertaPrinc(TP_ALERTA_AVISO, 'Id. Alerta não informado');
             return false;
           }

          $.ajax({
            dataType: "json",
            type: "post",
            url : urlPadrao + "alerta/excluir",
            data : { IdAlerta: IdAlerta, },
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
                // fCriarAlertaPrinc(TP_ALERTA_SUCESSO, mensagem); 
                fAlterarLinhaGridAlerta( urlPadrao, indexTr.toString() )
                return true;
              } else {
                fCriarAlerta("AreaAlertaModalExcTds", TP_ALERTA_ERRO, mensagem);
                return false;
              }
              
            },
            error: function (data) {
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
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });

    } catch (e) {
      if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    } 
}

function fAlterarLinhaGridAlerta( urlPadrao, indexTr ){
  try {

      promise = new Promise( (resolve, reject) => {

          $("#BtnExclAlerta-"+indexTr).removeClass('btn-danger');
          $("#BtnExclAlerta-"+indexTr).addClass('btn-muted');
          $("#BtnExclAlerta-"+indexTr).addClass('disabled');

          $("#GridTr-"+indexTr).children('td').addClass('text-danger');

          var tr =$("#GridTr-"+indexTr).closest('tr');  
          tr.fadeOut(400);
          //tr.fadeOut(400, function() { tr.remove(); });

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

function fAbrirModalCriarAlerta() {
  try {

        fLimparAreaAlertaPrinc();
        fLimparAreaAlerta("AlertaModalDadosAlerta");

        $("#txtDetAlertaTipo").val( "" );
        $("#txtDetAlertaUser").val( "" );
        $("#txtDetAlertaMsg").val( "" );    
                             
        fDefinirPadraoSelect('txtDetAlertaTipo');                 
        fDefinirPadraoSelect('txtDetAlertaUser');

        $('#PopModalDadosAlerta').modal({backdrop: 'static'});  

        $("#txtDetAlertaMsg").focus();

  } catch (e) {
    fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}

function iniciarAnimacaoSalvarAlerta() {
  $("#iDadosAlertaSalvar").removeClass("fa-check");
  $("#iDadosAlertaSalvar").addClass("fa-spinner");
  $("#iDadosAlertaSalvar").addClass("fa-pulse");
  $("#BtnModalDadosAlertaSalvar").addClass("disabled");
}

function finalizarAnimacaoSalvarAlerta() {
  $("#iDadosAlertaSalvar").removeClass("fa-spinner");
  $("#iDadosAlertaSalvar").removeClass("fa-pulse");
  $("#iDadosAlertaSalvar").addClass("fa-check");
  $("#BtnModalDadosAlertaSalvar").removeClass("disabled");
}

function fSalvarDadosAlerta( urlPadrao ){
  try {

      promise = new Promise( (resolve, reject) => {

          fLimparAreaAlertaPrinc();

          finalizarAnimacaoSalvarAlerta();
          iniciarAnimacaoSalvarAlerta();
          
          var txtTipo = $("#txtDetAlertaTipo").val().trim(); 
          var txtUser = $("#txtDetAlertaUser").val().trim(); 
          var txtMsg  = $("#txtDetAlertaMsg").val().trim(); 
          
          if( txtTipo == ""){
            finalizarAnimacaoSalvarAlerta();
            fCriarAlerta("AlertaModalDadosAlerta", TP_ALERTA_AVISO, 'Tipo não informado!'); 
            return;
          } 

          if ( txtTipo == 'ADMIN-01') 
            txtUser = "";

          if ( txtTipo == 'ADMIN-02' && txtUser == ""){
            finalizarAnimacaoSalvarAlerta();
            fCriarAlerta("AlertaModalDadosAlerta", TP_ALERTA_AVISO, 'Usuario não informado!'); 
            return;
          } 
          
          if( txtMsg == ""){
            finalizarAnimacaoSalvarAlerta();
            fCriarAlerta("AlertaModalDadosAlerta", TP_ALERTA_AVISO, 'Msg não informado!'); 
            return;
          } 

          $.ajax({
            cache   : "false",
            dataType: "json",
            async   : true,
            type    : "POST",
            url     : urlPadrao + "alerta/salvar",
            data    : { txtTipo: txtTipo, txtUser: txtUser, txtMsg: txtMsg },
            success: function(result) {  

              finalizarAnimacaoSalvarAlerta();

              var resultado = result.data.Resultado; 
              var mensagem  = result.data.Mensagem;

              if (resultado == "NSESSAO") {
                  $(location).attr('href', urlPadrao + '/login');
                  return false;
               } else if (resultado == "NOK") {
                  fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
                  return;
              } else if (resultado == "OK") {
                  $("#PopModalDadosAlerta").modal("hide");
                  fCarregarGrid( urlPadrao );
              } else {
                fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                return;
              }
          
            },
            error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
              finalizarAnimacaoSalvarAlerta();
              fCriarAlerta("AlertaModalDadosAlerta", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);   // request.responseText //MSG_ALERTA_ERRO
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
        finalizarAnimacaoSalvarAlerta();
        fCriarAlerta("AlertaModalDadosAlerta", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });
  
  } catch (e) {
    finalizarAnimacaoSalvarAlerta();
    fCriarAlerta("AlertaModalDadosAlerta", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  return;
  }
}

function fLimparSomenteGridUser( urlPadrao ){
  try { 
    
    $("#GridUser > thead > th").addClass('text-left');
    $("#GridUser > thead > tr").addClass('text-left');

    $('#GridUser').dataTable().fnClearTable();
    $("#GridUser").dataTable({ bDestroy: true }).fnDestroy();

    $('#GridUser').DataTable( {
        data: [],
        oLanguage: fTraduzirGrid(), 
        aoColumns: [
          { bSortable: true,  sWidth: widthGridUserNmUsuario,    targets: idxGridUserNmUsuario    }, 
          { bSortable: true,  sWidth: widthGridUserTpAlerta,     targets: idxGridUserTpAlerta     },
          { bSortable: true,  sWidth: widthGridUserTpAssinatura, targets: idxGridUserTpAssinatura },
          { visible  : false,                                    targets: idxGridUserIdUsuario    },
          { visible  : false,                                    targets: idxGridUserIdAssinatura },
          { visible  : false,                                    targets: idxGridUserSituacao     },
          { bSortable: false, sWidth: widthGridUserAcao,         targets: idxGridUserAcao         }
        ],
        // order          : [[ idxGridIdOper, "asc" ], [ idxGridData, "desc" ], [ idxGridAtivo, "desc" ], [ idxGridTipo, "desc" ]],
        bLengthChange  : false,
        bFilter        : true,
        searchable     : true,
        orderable      : true,
        bAutoWidth     : false
    });

  } catch(e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}

function fMontarGridUser( urlPadrao, dataSet ){
  try {   


     $("#GridUser > thead > th").addClass('text-left');
     $("#GridUser > thead > tr").addClass('text-left');
  
      var indexTr = -1;

      var table = $('#GridUser').DataTable( {
          processing: true,
          serverSide: false,
          oLanguage: fTraduzirGrid(), 
          data: dataSet,
          aoColumns: [
              { bSortable: true,  sWidth: widthGridUserNmUsuario,    targets: idxGridUserNmUsuario,    render: function ( data, type, row ) { if ( type == "display") return row[idxGridUserIdUsuario] + ' - ' + row[idxGridUserNmUsuario]; return data; } }, 
              { bSortable: true,  sWidth: widthGridUserTpAlerta,     targets: idxGridUserTpAlerta,     render: function ( data, type, row ) { if ( type == "display") return row[idxGridUserTpAlerta]; return data; } }, 
              { bSortable: true,  sWidth: widthGridUserTpAssinatura, targets: idxGridUserTpAssinatura, render: function ( data, type, row ) { if ( type == "display") return row[idxGridUserTpAssinatura]; return data; } }, 
              { visible  : false,                                    targets: idxGridUserIdUsuario,    render: function ( data, type, row ) { if ( type == "display") return row[idxGridUserIdUsuario]; return data; } }, 
              { visible  : false,                                    targets: idxGridUserIdAssinatura, render: function ( data, type, row ) { if ( type == "display") return row[idxGridUserIdAssinatura]; return data; } }, 
              { visible  : false,                                    targets: idxGridUserSituacao,     render: function ( data, type, row ) { if ( type == "display") return row[idxGridUserSituacao]; return data; } }, 
              { bSortable: false, sWidth: widthGridUserAcao,         targets: idxGridUserAcao, 
                render: function ( data, type, row ) {

                  var btnGrid = "";
                  var btnDis  = "";
                  var btnCor  = "";

                  if ( type == "display") {

                    indexTr         += 1;
                    var IdUsuario    = row[idxGridUserIdUsuario];
                    var IdAssinatura = row[idxGridUserIdAssinatura];
                    var Situacao     = row[idxGridUserSituacao];
                    

                    btnGrid += '<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">';

                    btnDis  = ( Situacao == 'I' ? ''      : ' disabled');
                    btnCor  = ( Situacao == 'I' ? 'success' : 'muted' );
                    btnGrid += '<a id="BtnAtivaAssinatura-'+indexTr+'" class="btn btn-sm btn-'+btnCor+' btn-icon btn-icon-mini btn-round btn-simple'+btnDis+'" style="font-size:0.5rem;" title="Inativar Assinatura('+IdAssinatura+')" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fAlterarAssinatura( \''+urlPadrao+'\', \''+IdAssinatura+'\', \'A\', \''+indexTr+'\' );">';
                    btnGrid += '   <i class="fa fa-thumbs-up fa-lg" aria-hidden="true"></i> ';
                    btnGrid += '</a>';

                    btnGrid += '&nbsp;';

                    btnDis  = ( Situacao == 'A' ? ''      : ' disabled');
                    btnCor  = ( Situacao == 'A' ? 'danger' : 'muted' );
                    btnGrid += '<a id="BtnInativaAssinatura-'+indexTr+'" class="btn btn-sm btn-'+btnCor+' btn-icon btn-icon-mini btn-round btn-simple'+btnDis+'" style="font-size:0.5rem;" title="Inativar Assinatura('+IdAssinatura+')" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fAlterarAssinatura( \''+urlPadrao+'\', \''+IdAssinatura+'\', \'I\', \''+indexTr+'\' );">';
                    btnGrid += '   <i class="fa fa-thumbs-down fa-lg" aria-hidden="true"></i> ';
                    btnGrid += '</a>';

                    btnGrid += '</div>';
                  }
                  
                  return btnGrid; 
                  
                } 
              }
          ],
          createdRow : function(row,data,dataIndex) {
              $(row).addClass('text-left font-weight-bold');
              $(row).attr('id', 'GridUserTr-'+dataIndex);
              // $('td', row).eq(idxGridUserNmUsuario).addClass('text-left  font-weight-bold'); 
              // $('td', row).eq(idxGridUserTpAlerta).addClass('text-left  font-weight-bold');
              // $('td', row).eq(idxGridUserTpAssinatura).addClass('text-left  font-weight-bold'); 
              var Situacao = data[idxGridUserSituacao];
              if ( Situacao == "A" ) $('td', row).addClass('text-success');  
              if ( Situacao == "I" ) $('td', row).addClass('text-danger'); 
          }, //createdRow
          initComplete: function( settings, json ) {
            
          },
          // order: [[ idxGridIdOper, "asc" ], [ idxGridData, "desc" ], [ idxGridAtivo, "desc" ], [ idxGridTipo, "desc" ]],
          //dom: 'frtBpi', //Bfrtip //frtBip  //frtBpi
           //iDisplayLength : 100,
            bPaginate: false,
            bLengthChange: false,
            bFilter: true,
            searchable: true,
            bAutoWidth: false,
            bInfo: true,
            bSearchable: true,
            bSortable: true,
            orderable: true,
            bOrderable: true,
            bOrdering: true
      });
    
      $( document ).ajaxError(function( event, request, settings, thrownError ) {
        fLimparSomenteGridUser( urlPadrao );
      });

      } catch (e) {
        fLimparSomenteGridUser( urlPadrao );
        if ( e.description != undefined ) fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      }
}

function fAbrirModalUserAlerta( urlPadrao ) {
  try {

         promise = new Promise( (resolve, reject) => {

          fLimparAreaAlertaPrinc();
          fLimparAreaAlerta("AlertaModalDadosUserAlerta");

          $('#GridUser').dataTable().fnClearTable();
          $("#GridUser").dataTable({ bDestroy: true }).fnDestroy(); 
          
          $.ajax({
            cache   : "false",
            dataType: "json",
            async   : true,
            type    : "POST",
            url     : urlPadrao + "alerta/griduserassinatura",
            success: function(result) {
              
                var resultado = result.data.Resultado; 
                var mensagem  = result.data.Mensagem; 
                var lista     = result.data.Lista;

                if (resultado == "NSESSAO") {
                  $(location).attr('href', urlPadrao + '/login');
                  return false;
                } else if (resultado == "NOK") {
                  fLimparSomenteGridUser( urlPadrao );
                  fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem); 
                  return;
                } else if (resultado == "FALHA") {
                  fLimparSomenteGridUser( urlPadrao );
                  fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                  return;
                }else if (resultado == "OK") {
                  $('#PopModalDadosUserAlerta').modal({backdrop: 'static'});  
                  fMontarGridUser( urlPadrao, lista );
                } else{
                  fLimparSomenteGridUser( urlPadrao );
                  fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem); 
                  return;
                }
              
            },
            error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
              fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);   // request.responseText //MSG_ALERTA_ERRO
              fLimparSomenteGridUser( urlPadrao );
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
        fLimparSomenteGridUser( urlPadrao );
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });


  } catch (e) {
    fCriarAlerta("AreaAlertaPrinc",TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
  }
}

function fAlterarAssinatura( urlPadrao, id_assinatura, situacao, indexTr ) {
    try {

      promise = new Promise( (resolve, reject) => {

           if ( id_assinatura.toString() == '' ) {
            fCriarAlerta("AlertaModalDadosUserAlerta", 'Id. Assinatura não informado');
             return false;
           }

           if ( situacao == '' ) {
            fCriarAlerta("AlertaModalDadosUserAlerta", 'Situação não informada');
             return false;
           }

          $.ajax({
            dataType: "json",
            type: "post",
            url : urlPadrao + "alerta/alterarassinatura",
            data : { id_assinatura: id_assinatura, situacao: situacao, },
            success: function (result) {
              
              var resultado = result.data.Resultado; 
              var mensagem  = result.data.Mensagem; 

              if (resultado == "NSESSAO") {
                $(location).attr('href', urlPadrao + '/login');
                return false;
              } else if (resultado == "NOK") {
                fCriarAlerta("AlertaModalDadosUserAlerta", TP_ALERTA_AVISO, mensagem);
                return false;
              } else if (resultado == "FALHA") {
                fCriarAlerta("AlertaModalDadosUserAlerta", TP_ALERTA_ERRO, mensagem);
                return;
              } else if (resultado == "OK") {   
                // fCriarAlerta("AlertaModalDadosUserAlerta", TP_ALERTA_SUCESSO, mensagem); 
                fAlterarLinhaGridUserAlerta( urlPadrao, indexTr.toString() , situacao );
                return true;
              } else {
                fCriarAlerta("AlertaModalDadosUserAlerta", TP_ALERTA_ERRO, mensagem);
                return false;
              }
              
            },
            error: function (data) {
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
        fCriarAlerta("AlertaModalDadosUserAlerta", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
      });

    } catch (e) {
      if ( e.description != undefined ) fCriarAlerta("AlertaModalDadosUserAlerta", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
    } 
}

function fAlterarLinhaGridUserAlerta( urlPadrao, indexTr, situacao ){
  try {

      promise = new Promise( (resolve, reject) => {

          if ( situacao == 'A' ){

            $("#GridUserTr-"+indexTr).children('td').removeClass('text-danger')
            $("#GridUserTr-"+indexTr).children('td').addClass('text-success');

            $("#BtnAtivaAssinatura-"+indexTr).addClass('disabled');
            $("#BtnAtivaAssinatura-"+indexTr).removeClass('btn-success');
            $("#BtnAtivaAssinatura-"+indexTr).addClass('btn-muted');

            $("#BtnInativaAssinatura-"+indexTr).removeClass('disabled');
            $("#BtnInativaAssinatura-"+indexTr).removeClass('btn-muted');
            $("#BtnInativaAssinatura-"+indexTr).addClass('btn-danger');

          }

          if ( situacao == 'I' ){

            $("#GridUserTr-"+indexTr).children('td').removeClass('text-success')
            $("#GridUserTr-"+indexTr).children('td').addClass('text-danger');

            $("#BtnAtivaAssinatura-"+indexTr).removeClass('disabled');
            $("#BtnAtivaAssinatura-"+indexTr).removeClass('btn-muted');
            $("#BtnAtivaAssinatura-"+indexTr).addClass('btn-success');

            $("#BtnInativaAssinatura-"+indexTr).addClass('disabled');
            $("#BtnInativaAssinatura-"+indexTr).removeClass('btn-danger');
            $("#BtnInativaAssinatura-"+indexTr).addClass('btn-muted');

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