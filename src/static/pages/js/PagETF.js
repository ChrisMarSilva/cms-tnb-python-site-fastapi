
$(document).ready(function() {
  //$(this).attr("title", "ETF. - " + NOME_PROJETO);
  $("#MnPrincEtf").addClass("active open");
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
        { bSortable: true, sWidth: "20px", targets: 1 }, // 1-Fundo
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
        { bSortable: true, sWidth: "20px", targets: 1 }, // 1-Fundo
        { bSortable: true, sWidth: "40px", targets: 2 }, // 2-Razão Social
        { bSortable: true, sWidth: "40px", targets: 3 }, // 3-CNPJ
        { bSortable: true, sWidth: "40px", targets: 4 }, // 4-Situação
        { visible: false,                  targets: 5 }, // 5-Id
        { bSortable: true, sWidth: "20px", targets: 6, // 6-Ação
          render: function(data, type, row) {
            var btnEdt = "";
            if (type == "display") {
              etfId = row[5];  // 5-Id
              btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar ' + etfId + '" href="javascript:void(0);" onclick="fAbrirModalDetalheEtf( \''+urlPadrao+'\', \''+etfId+'\', \'Alterar\' );">';
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
      url: urlPadrao + "etf/grid",
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

function fLimparDadosModalEtf( ) {
	fLimparAreaAlertaModalCad();
    $("#txtCadEtfId").val("");
    $("#txtCadEtfFundo").val("");
    $("#txtCadEtfRazao").val("");
    $("#txtCadEtfIndice").val("");
    $("#txtCadEtfNome").val("");
    $("#txtCadEtfCNPJ").val("");
    $("#txtCadEtfCodigo").val("");
    $("#txtCadEtfIsin").val("");
    $("#txtCadEtfSituacao").val("A");
	fDefinirPadraoSelect('txtCadEtfSituacao');
}

function fAbrirModalDetalheEtf( urlPadrao, etfId, TipoModal ) {
  try {

      fLimparDadosModalEtf();
      $("#PopModalDetalheEtfTit").html(" - "+TipoModal);

      if ( TipoModal == "Novo"                                 ) $('#PopModalDetalheEtf').modal({backdrop: 'static'});
      if ( TipoModal == "Alterar" || TipoModal == "Visualizar" ) fCarregarDadosModalDetalheEtf( urlPadrao, etfId, TipoModal );

      $("#txtCadEtfFundo").focus();

  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, "fAbrirModalDetalheEtf"+MSG_ALERTA_ERRO);
  }
}

function fCarregarDadosModalDetalheEtf(urlPadrao, etfId, TipoModal) {
  try {

    fLimparAreaAlertaModalCad();

    if (etfId == "") {
      fCriarAlertaPrinc(TP_ALERTA_AVISO, "Id. não informado!");
      return;
    }    

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "etf/carregar",
      data: { etfId: etfId },
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

            $("#txtCadEtfId").val(       Dados.Id          );
            $("#txtCadEtfFundo").val(    Dados.Fundo       );
            $("#txtCadEtfRazao").val(    Dados.RazaoSocial );
            $("#txtCadEtfIndice").val(   Dados.Indice      );
            $("#txtCadEtfNome").val(     Dados.Nome        );
            $("#txtCadEtfCNPJ").val(     Dados.CNPJ        );
            $("#txtCadEtfCodigo").val(   Dados.Codigo      );
            $("#txtCadEtfIsin").val(     Dados.Isin        );
            $("#txtCadEtfSituacao").val( Dados.Situacao    );
	        fDefinirPadraoSelect('txtCadEtfSituacao');
            
            $("#PopModalDetalheEtf").modal({ backdrop: "static" });
            
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
    fCriarAlertaPrinc(TP_ALERTA_ERRO, "fCarregarDadosModalDetalheEtf"+MSG_ALERTA_ERRO);
  }
}

function fValidarDadosEtf() {
  try {

    var etfId       = $("#txtCadEtfId").val().trim();
    var etfFundo    = $("#txtCadEtfFundo").val().trim();
    var etfRazao    = $("#txtCadEtfRazao").val().trim();
    var etfIndice   = $("#txtCadEtfIndice").val().trim();
    var etfNome     = $("#txtCadEtfNome").val().trim();
    var etfCNPJ     = $("#txtCadEtfCNPJ").val().trim();
    var etfCodigo   = $("#txtCadEtfCodigo").val().trim();
    var etfIsin     = $("#txtCadEtfIsin").val().trim();
    var etfSituacao = $("#txtCadEtfSituacao").val();

    var ListaErros = "";
    if ( etfFundo    == "" ) ListaErros = ListaErros + " - Fundo<br/>";
    if ( etfRazao    == "" ) ListaErros = ListaErros + " - Razao<br/>";
    if ( etfCNPJ     == "" ) ListaErros = ListaErros + " - CNPJ<br/>";
    if ( etfCodigo   == "" ) ListaErros = ListaErros + " - Codigo<br/>";
    if ( etfSituacao == "" ) ListaErros = ListaErros + " - Situacao<br/>";

    if (ListaErros != "") {
      fCriarAlertaModalCad(TP_ALERTA_AVISO,"Os seguintes campos não estão preenchido: <br/>" + ListaErros);
      return false;
    }

    return true;

  } catch (e) {
    fCriarAlertaModalCad(TP_ALERTA_ERRO, "fValidarDadosEtf"+MSG_ALERTA_ERRO);
    return false;
  }
}

function fSalvarDadosEtf(urlPadrao) {
  try {

    fLimparAreaAlertaModalCad();
    
    if ( !fValidarDadosEtf() )  return false;

    iniciarAnimacaoSalvar();

    var etfId       = $("#txtCadEtfId").val().trim();
    var etfFundo    = $("#txtCadEtfFundo").val().trim();
    var etfRazao    = $("#txtCadEtfRazao").val().trim();
    var etfIndice   = $("#txtCadEtfIndice").val().trim();
    var etfNome     = $("#txtCadEtfNome").val().trim();
    var etfCNPJ     = $("#txtCadEtfCNPJ").val().trim();
    var etfCodigo   = $("#txtCadEtfCodigo").val().trim();
    var etfIsin     = $("#txtCadEtfIsin").val().trim();
    var etfSituacao = $("#txtCadEtfSituacao").val();

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "etf/salvar",
      data: {
        etfId      : etfId,
        etfFundo   : etfFundo,
        etfRazao   : etfRazao,
        etfIndice  : etfIndice,
        etfNome    : etfNome,
        etfCNPJ    : etfCNPJ,
        etfCodigo  : etfCodigo,
        etfIsin    : etfIsin,
        etfSituacao: etfSituacao,
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
          $("#PopModalDetalheEtf").modal("hide");
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
    CriarAlertaModal(TP_ALERTA_ERRO, "fSalvarDadosEtf"+MSG_ALERTA_ERRO);
    return;
  }
}