//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

$(document).ready(function() {
  //$(this).attr("title", "Fundo Imob. - " + NOME_PROJETO);
  $("#MnPrincFiiFundoImob").addClass("active open");
  fLimparAreaAlertaPrinc();
  fLimparAreaAlertaModalCad();
});

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fLimparGrid(urlPadrao) {
  try {
    
    $("th").addClass("text-center");

    $("#Grid").dataTable().fnClearTable();
    $("#Grid").dataTable({ bDestroy: true }).fnDestroy();

    $("#Grid").DataTable({
      oLanguage: fTraduzirGrid(),
      aoColumns: [
        { bSortable: true, sWidth: "10px", targets: 0 }, // 0-Código
        { bSortable: true, sWidth: "20px", targets: 1 }, // 1-Nome
        { bSortable: true, sWidth: "40px", targets: 2 }, // 2-Razão Social
        { bSortable: true, sWidth: "40px", targets: 3 }, // 3-CNPJ
        { bSortable: true, sWidth: "40px", targets: 4 }, // 4-Situação
        { visible: false,                  targets: 5 }, // 5-Id
        { bSortable: true, sWidth: "20px", targets: 6 }  // 6-Ação
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
        { bSortable: true, sWidth: "10px", targets: 0 }, // 0-Código
        { bSortable: true, sWidth: "20px", targets: 1 }, // 1-Nome
        { bSortable: true, sWidth: "40px", targets: 2 }, // 2-Razão Social
        { bSortable: true, sWidth: "40px", targets: 3 }, // 3-CNPJ
        { bSortable: true, sWidth: "40px", targets: 4 }, // 4-Situação
        { visible: false,                  targets: 5 }, // 5-Id
        { bSortable: true, sWidth: "20px", targets: 6, // 6-Ação
          render: function(data, type, row) {
            var btnEdt = "";
            if (type == "display") {

              fiiFundoId = row[5];  // 5-Id

              btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar ' + fiiFundoId + '" href="javascript:void(0);" onclick="fAbrirModalDetalheFundoImob( \''+urlPadrao+'\', \''+fiiFundoId+'\', \'Alterar\' );">';
              btnEdt += '   <i class="fa fa-pencil fa-lg" aria-hidden="true"></i> ';
              btnEdt += "</a>";

            }
            return btnEdt;
          }
        } //  9-Acao
      ],
      createdRow: function(row, data, dataIndex) {
        $("td", row).addClass("text-center");
      }, //createdRow
      initComplete: function(settings, json) {
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

    $(document).ajaxError(function(event, request, settings, thrownError) { fLimparGrid(urlPadrao); });

  } catch (e) {
    fLimparGrid(urlPadrao);
    if (e.description != undefined)  fCriarAlertaPrinc(TP_ALERTA_ERRO, "fMontarGrid"+MSG_ALERTA_ERRO);
  }
}

function fCarregarGrid(urlPadrao) {
  try {

    fLimparAreaAlertaPrinc();
    $("#Grid").dataTable().fnClearTable();
    $("#Grid").dataTable({ bDestroy: true }).fnDestroy();

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "FiiFundoImob/grid",
      data: {},
      success: function(result) {

        var resultado = result.data.Resultado;
        var mensagem  = result.data.Mensagem;
        var lista     = result.data.Lista;

        if (resultado == "NSESSAO") {
          $(location).attr("href", urlPadrao + "/login");
          return false;
        } else if (resultado == "NOK") {
          fLimparGrid(urlPadrao);
          fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
          return;
        } else if (resultado == "FALHA") {
          fLimparGrid(urlPadrao);
          fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
          return;
        } else if (resultado == "OK") {
          fMontarGrid(urlPadrao, lista);
        } else {
          fLimparGrid(urlPadrao);
          fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
          return;
        }
      },
      error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
        fLimparGrid(urlPadrao);
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO );// request.responseText // MSG_ALERTA_ERRO
        return false;
      }
    });
  } catch (e) {
      fLimparGrid(urlPadrao);
      if (e.description != undefined) fCriarAlertaPrinc(TP_ALERTA_ERRO, "fCarregarGrid"+MSG_ALERTA_ERRO);
  }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fLimparDadosModalFundoImob( ) {

	  fLimparAreaAlertaModalCad();
	
    $("#txtCadFundoId").val("");   
    $("#txtCadFundoAdmin").val("");   
    $("#txtCadFundoTipo").val("");   
    $("#txtCadFundoNome").val("");   
    $("#txtCadFundoRazao").val(""); 
    $("#txtCadFundoCNPJ").val("");   
    $("#txtCadFundoCodigo").val(""); 
    $("#txtCadFundoIsin").val("");   
    $("#txtCadFundoSituacao").val("A");
  
    fDefinirPadraoSelect('txtCadFundoAdmin');
    fDefinirPadraoSelect('txtCadFundoTipo');

}

function fAbrirModalDetalheFundoImob( urlPadrao, fiiFundoId, TipoModal ) {
  try {

      fLimparDadosModalFundoImob();

      $("#PopModalDetalheFundoTit").html("");
      $("#PopModalDetalheFundoTit").html(" - "+TipoModal);

      if ( TipoModal == "Novo"                                 ) $('#PopModalDetalheFundo').modal({backdrop: 'static'});
      if ( TipoModal == "Alterar" || TipoModal == "Visualizar" ) fCarregarDadosModalDetalheFundoImob( urlPadrao, fiiFundoId, TipoModal );

      $("#txtCadFundoNome").focus();

  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, "fAbrirModalDetalheFundoImob"+MSG_ALERTA_ERRO); 
  }
}

function fCarregarDadosModalDetalheFundoImob(urlPadrao, fiiFundoId, TipoModal) {
  try {

    fLimparAreaAlertaModalCad();

    if (fiiFundoId == "") {
      fCriarAlertaPrinc(TP_ALERTA_AVISO, "Id. Fundo Imob. não informado!");
      return;
    }    

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "FiiFundoImob/carregar",
      data: { fiiFundoId: fiiFundoId },
      success: function(result) {

        var resultado = result.data.Resultado;
        var mensagem  = result.data.Mensagem;
        var Fundo     = result.data.Dados;

        if (resultado == "NSESSAO") {
          $(location).attr("href", urlPadrao + "/login");
          return false;
        } else if (resultado == "NOK") {
          fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
        } else if (resultado == "FALHA") {
          fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
        } else if (resultado == "OK") {

          if (Fundo.Id) {

            $("#txtCadFundoId").val(       Fundo.Id          );
            $("#txtCadFundoAdmin").val(    Fundo.AdminId     );
            $("#txtCadFundoTipo").val(     Fundo.TipoId      );
            $("#txtCadFundoNome").val(     Fundo.Nome        );
            $("#txtCadFundoRazao").val(    Fundo.RazaoSocial );
            $("#txtCadFundoCNPJ").val(     Fundo.CNPJ        );
            $("#txtCadFundoCodigo").val(   Fundo.Codigo      );
            $("#txtCadFundoIsin").val(     Fundo.Isin        );
            $("#txtCadFundoSituacao").val( Fundo.Situacao    );
            
            fDefinirPadraoSelect('txtCadFundoAdmin');
            fDefinirPadraoSelect('txtCadFundoTipo');
            
            $("#PopModalDetalheFundo").modal({ backdrop: "static" });
            
          } else {
            fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
          }

        } else {
          fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
        }
      },
      error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
        fCriarAlertaPrinc(TP_ALERTA_ERRO, MSG_ALERTA_ERRO ); // request.responseText // MSG_ALERTA_ERRO
      }
    });
  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, "fCarregarDadosModalDetalheFundoImob"+MSG_ALERTA_ERRO);
  }
}

function fValidarDadosFundoImob() {
  try {

    var fiiFundoId       = $("#txtCadFundoId").val().trim();     
    var fiiFundoAdmin    = $("#txtCadFundoAdmin").val();     
    var fiiFundoTipo     = $("#txtCadFundoTipo").val();     
    var fiiFundoNome     = $("#txtCadFundoNome").val().trim();        
    var fiiFundoRazao    = $("#txtCadFundoRazao").val().trim();     
    var fiiFundoCNPJ     = $("#txtCadFundoCNPJ").val().trim();     
    var fiiFundoCodigo   = $("#txtCadFundoCodigo").val().trim();     
    var fiiFundoIsin     = $("#txtCadFundoIsin").val().trim();     
    var fiiFundoSituacao = $("#txtCadFundoSituacao").val();  

    var ListaErros = "";
    if ( fiiFundoNome     == "" ) ListaErros = ListaErros + " - Nome<br/>";
    if ( fiiFundoRazao    == "" ) ListaErros = ListaErros + " - Razao<br/>";
    if ( fiiFundoCNPJ     == "" ) ListaErros = ListaErros + " - CNPJ<br/>";
    if ( fiiFundoCodigo   == "" ) ListaErros = ListaErros + " - Codigo<br/>";
    if ( fiiFundoSituacao == "" ) ListaErros = ListaErros + " - Situacao<br/>";

    if (ListaErros != "") {
      fCriarAlertaModalCad(TP_ALERTA_AVISO,"Os seguintes campos não estão preenchido: <br/>" + ListaErros);
      return false;
    }

    return true;

  } catch (e) {
    fCriarAlertaModalCad(TP_ALERTA_ERRO, "fValidarDadosFundoImob"+MSG_ALERTA_ERRO);
    return false;
  }
}

function fSalvarDadosFundoImob(urlPadrao) {
  try {

    fLimparAreaAlertaModalCad();
    
    if ( !fValidarDadosFundoImob() )  return false;

    iniciarAnimacaoSalvar();

    var fiiFundoId       = $("#txtCadFundoId").val().trim();     
    var fiiFundoAdmin    = $("#txtCadFundoAdmin").val();     
    var fiiFundoTipo     = $("#txtCadFundoTipo").val();     
    var fiiFundoNome     = $("#txtCadFundoNome").val().trim();        
    var fiiFundoRazao    = $("#txtCadFundoRazao").val().trim();     
    var fiiFundoCNPJ     = $("#txtCadFundoCNPJ").val().trim();     
    var fiiFundoCodigo   = $("#txtCadFundoCodigo").val().trim();     
    var fiiFundoIsin     = $("#txtCadFundoIsin").val().trim();     
    var fiiFundoSituacao = $("#txtCadFundoSituacao").val();  

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "FiiFundoImob/salvar",
      data: {
        fiiFundoId      : fiiFundoId,
        fiiFundoIdAdmin : fiiFundoAdmin,
        fiiFundoIdTipo  : fiiFundoTipo,
        fiiFundoNome    : fiiFundoNome,
        fiiFundoRazao   : fiiFundoRazao,
        fiiFundoCNPJ    : fiiFundoCNPJ,
        fiiFundoCodigo  : fiiFundoCodigo,
        fiiFundoIsin    : fiiFundoIsin,
        fiiFundoSituacao: fiiFundoSituacao,
      },
      success: function(result) {

        finalizarAnimacaoSalvar();

        var resultado = result.data.Resultado;
        var mensagem  = result.data.Mensagem;

        if (resultado == "NSESSAO") {
          $(location).attr("href", urlPadrao + "/login");
          return false;
        } else if (resultado == "NOK") {
          fCriarAlertaModalCad(TP_ALERTA_AVISO, mensagem);
          return;
        } else if (resultado == "FALHA") {
          fCriarAlertaModalCad(TP_ALERTA_ERRO, mensagem);
          return;
        } else if (resultado == "OK") {
          $("#PopModalDetalheFundo").modal("hide");
          fCarregarGrid(urlPadrao);
          fCriarAlertaPrinc(TP_ALERTA_SUCESSO, "Dados salvo com sucesso!");
        } else {
          fCriarAlertaModalCad(TP_ALERTA_ERRO, mensagem);
          return;
        }
      },
      error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
        finalizarAnimacaoSalvar();
        fCriarAlertaModalCad(TP_ALERTA_ERRO, MSG_ALERTA_ERRO);// request.responseText // MSG_ALERTA_ERRO
        return;
      }
    });
  } catch (e) {
    finalizarAnimacaoSalvar();
    CriarAlertaModal(TP_ALERTA_ERRO, "fSalvarDadosFundoImob"+MSG_ALERTA_ERRO);
    return;
  }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------