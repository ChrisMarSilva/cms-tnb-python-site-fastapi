
$(document).ready(function() {
  //$(this).attr("title", "CRIPTO. - " + NOME_PROJETO);
  $("#MnPrincCripto").addClass("active open");
  fLimparAreaAlertaPrinc();
  fLimparAreaAlertaModalCad();
});

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
        { bSortable: true, sWidth: "40px", targets: 2 }, // 2-Situação
        { visible: false,                  targets: 3 }, // 3-Id
        { bSortable: true, sWidth: "20px", targets: 4 }  // 4-Ação
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
        { bSortable: true, sWidth: "20px", targets: 1 }, // 1-Fundo
        { bSortable: true, sWidth: "40px", targets: 2 }, // 2-Situação
        { visible: false,                  targets: 3 }, // 3-Id
        { bSortable: true, sWidth: "20px", targets: 4,   // 4-Ação
          render: function(data, type, row) {
            var btnEdt = "";
            if (type == "display") {
              criptoId = row[3];  // 3-Id
              btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar ' + criptoId + '" href="javascript:void(0);" onclick="fAbrirModalDetalheCripto( \''+urlPadrao+'\', \''+criptoId+'\', \'Alterar\' );">';
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
      url: urlPadrao + "cripto/grid",
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

function fLimparDadosModalCripto() {
	fLimparAreaAlertaModalCad();
    $("#txtCadCriptoId").val("");
    $("#txtCadCriptoNome").val("");
    $("#txtCadCriptoCodigo").val("");
    $("#txtCadCriptoSituacao").val("A");
	fDefinirPadraoSelect('txtCadCriptoSituacao');
}

function fAbrirModalDetalheCripto( urlPadrao, criptoId, TipoModal ) {
  try {

      fLimparDadosModalCripto();
      $("#PopModalDetalheCriptoTit").html(" - "+TipoModal);

      if ( TipoModal == "Novo"                                 ) $('#PopModalDetalheCripto').modal({backdrop: 'static'});
      if ( TipoModal == "Alterar" || TipoModal == "Visualizar" ) fCarregarDadosModalDetalheCripto( urlPadrao, criptoId, TipoModal );

      $("#txtCadCriptoNome").focus();

  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, "fAbrirModalDetalheCripto"+MSG_ALERTA_ERRO);
  }
}

function fCarregarDadosModalDetalheCripto(urlPadrao, criptoId, TipoModal) {
  try {

    fLimparAreaAlertaModalCad();

    if (criptoId == "") {
      fCriarAlertaPrinc(TP_ALERTA_AVISO, "Id. não informado!");
      return;
    }    

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "cripto/carregar",
      data: { criptoId: criptoId },
      success: function(result) {

        var resultado = result.data.Resultado;
        var mensagem  = result.data.Mensagem;
        var Dados     = result.data.Dados;

        if (resultado == "NSESSAO") {
          $(location).attr("href", urlPadrao + "/login");
          return false;
        } else if (resultado == "NOK") {
          fCriarAlertaPrinc(TP_ALERTA_AVISO, mensagem);
        } else if (resultado == "FALHA") {
          fCriarAlertaPrinc(TP_ALERTA_ERRO, mensagem);
        } else if (resultado == "OK") {

          if (Dados.Id) {

            $("#txtCadCriptoId").val(       Dados.Id       );
            $("#txtCadCriptoNome").val(     Dados.Nome     );
            $("#txtCadCriptoCodigo").val(   Dados.Codigo   );
            $("#txtCadCriptoSituacao").val( Dados.Situacao );
	        fDefinirPadraoSelect('txtCadCriptoSituacao');
            
            $("#PopModalDetalheCripto").modal({ backdrop: "static" });
            
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
    fCriarAlertaPrinc(TP_ALERTA_ERRO, "fCarregarDadosModalDetalheCripto"+MSG_ALERTA_ERRO);
  }
}

function fValidarDadosCripto() {
  try {

    var criptoId       = $("#txtCadCriptoId").val().trim();
    var criptoNome     = $("#txtCadCriptoNome").val().trim();
    var criptoCodigo   = $("#txtCadCriptoCodigo").val().trim();
    var criptoSituacao = $("#txtCadCriptoSituacao").val();

    var ListaErros = "";
    if ( criptoNome     == "" ) ListaErros = ListaErros + " - Nome<br/>";
    if ( criptoCodigo   == "" ) ListaErros = ListaErros + " - Codigo<br/>";
    if ( criptoSituacao == "" ) ListaErros = ListaErros + " - Situacao<br/>";

    if (ListaErros != "") {
      fCriarAlertaModalCad(TP_ALERTA_AVISO,"Os seguintes campos não estão preenchido: <br/>" + ListaErros);
      return false;
    }

    return true;

  } catch (e) {
    fCriarAlertaModalCad(TP_ALERTA_ERRO, "fValidarDadosCripto"+MSG_ALERTA_ERRO);
    return false;
  }
}

function fSalvarDadosCripto(urlPadrao) {
  try {

    fLimparAreaAlertaModalCad();
    
    if ( !fValidarDadosCripto() )  return false;

    iniciarAnimacaoSalvar();

    var criptoId       = $("#txtCadCriptoId").val().trim();
    var criptoNome     = $("#txtCadCriptoNome").val().trim();
    var criptoCodigo   = $("#txtCadCriptoCodigo").val().trim();
    var criptoSituacao = $("#txtCadCriptoSituacao").val();

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "cripto/salvar",
      data: {
        criptoId      : criptoId,
        criptoNome    : criptoNome,
        criptoCodigo  : criptoCodigo,
        criptoSituacao: criptoSituacao,
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
          $("#PopModalDetalheCripto").modal("hide");
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
    CriarAlertaModal(TP_ALERTA_ERRO, "fSalvarDadosCripto"+MSG_ALERTA_ERRO);
    return;
  }
}