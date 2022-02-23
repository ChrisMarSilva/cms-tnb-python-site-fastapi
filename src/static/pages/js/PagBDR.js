
$(document).ready(function() {
  //$(this).attr("title", "BDR. - " + NOME_PROJETO);
  $("#MnPrincBdr").addClass("active open");
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
              bdrId = row[5];  // 5-Id
              btnEdt += '<a class="btn btn-sm btn-warning btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" title="Alterar ' + bdrId + '" href="javascript:void(0);" onclick="fAbrirModalDetalheBdr( \''+urlPadrao+'\', \''+bdrId+'\', \'Alterar\' );">';
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
      url: urlPadrao + "bdr/grid",
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

function fLimparDadosModalBdr( ) {
	fLimparAreaAlertaModalCad();

    $("#txtCadBdrId").val("");
    $("#txtCadBdrSetor").val("11"); // 11 - Não Classificados
    $("#txtCadBdrSubSetor").val("42"); // 42 - Não Classificados
    $("#txtCadBdrSegmento").val("81"); // 81 - Não Classificados
    $("#txtCadBdrNome").val("");
    $("#txtCadBdrRazao").val("");
    $("#txtCadBdrCNPJ").val("");
    $("#txtCadBdrCodigo").val("");
    $("#txtCadBdrIsin").val("");
    $("#txtCadBdrCodCVM").val("");
    $("#txtCadBdrTipo").val("DRN");
    $("#txtCadBdrSituacao").val("A");

    fDefinirPadraoSelect('txtCadBdrSetor');
    fDefinirPadraoSelect('txtCadBdrSubSetor');
    fDefinirPadraoSelect('txtCadBdrSegmento');
    fDefinirPadraoSelect('txtCadBdrTipo');
    fDefinirPadraoSelect('txtCadBdrSituacao');
}

function fAbrirModalDetalheBdr( urlPadrao, bdrId, TipoModal ) {
  try {

      fLimparDadosModalBdr();
      $("#PopModalDetalheBdrTit").html(" - "+TipoModal);

      if ( TipoModal == "Novo"                                 ) $('#PopModalDetalheBdr').modal({backdrop: 'static'});
      if ( TipoModal == "Alterar" || TipoModal == "Visualizar" ) fCarregarDadosModalDetalheBdr( urlPadrao, bdrId, TipoModal );

      $("#txtCadBdrNome").focus();

  } catch (e) {
    fCriarAlertaPrinc(TP_ALERTA_ERRO, "fAbrirModalDetalheBdr"+MSG_ALERTA_ERRO);
  }
}

function fCarregarDadosModalDetalheBdr(urlPadrao, bdrId, TipoModal) {
  try {

    fLimparAreaAlertaModalCad();

    if (bdrId == "") {
      fCriarAlertaPrinc(TP_ALERTA_AVISO, "Id. não informado!");
      return;
    }    

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "bdr/carregar",
      data: { bdrId: bdrId },
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

            $("#txtCadBdrId").val(       Dados.Id          );
            $("#txtCadBdrSetor").val(    Dados.SetorId     );
            $("#txtCadBdrSubSetor").val( Dados.SubSetorId  );
            $("#txtCadBdrSegmento").val( Dados.SegmentoId  );
            $("#txtCadBdrNome").val(     Dados.Nome        );
            $("#txtCadBdrRazao").val(    Dados.RazaoSocial );
            $("#txtCadBdrCNPJ").val(     Dados.CNPJ        );
            $("#txtCadBdrCodigo").val(   Dados.Codigo      );
            $("#txtCadBdrIsin").val(     Dados.Isin        );
            $("#txtCadBdrCodCVM").val(   Dados.CodCVM      );
            $("#txtCadBdrTipo").val(     Dados.Tipo        );
            $("#txtCadBdrSituacao").val( Dados.Situacao    );

	        fDefinirPadraoSelect('txtCadBdrSetor');
	        fDefinirPadraoSelect('txtCadBdrSubSetor');
	        fDefinirPadraoSelect('txtCadBdrSegmento');
	        fDefinirPadraoSelect('txtCadBdrTipo');
	        fDefinirPadraoSelect('txtCadBdrSituacao');
            
            $("#PopModalDetalheBdr").modal({ backdrop: "static" });
            
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
    fCriarAlertaPrinc(TP_ALERTA_ERRO, "fCarregarDadosModalDetalheBdr"+MSG_ALERTA_ERRO);
  }
}

function fValidarDadosBdr() {
  try {

    var bdrId       = $("#txtCadBdrId").val().trim();
    var bdrSetor    = $("#txtCadBdrSetor").val();
    var bdrSubSetor = $("#txtCadBdrSubSetor").val();
    var bdrSegmento = $("#txtCadBdrSegmento").val();
    var bdrNome     = $("#txtCadBdrNome").val().trim();
    var bdrRazao    = $("#txtCadBdrRazao").val().trim();
    var bdrCNPJ     = $("#txtCadBdrCNPJ").val().trim();
    var bdrCodigo   = $("#txtCadBdrCodigo").val().trim();
    var bdrIsin     = $("#txtCadBdrIsin").val().trim();
    var bdrCodCVM   = $("#txtCadBdrCodCVM").val().trim();
    var bdrTipo     = $("#txtCadBdrTipo").val();
    var bdrSituacao = $("#txtCadBdrSituacao").val();

    var ListaErros = "";
    if ( bdrNome     == "" ) ListaErros = ListaErros + " - Nome<br/>";
    if ( bdrRazao    == "" ) ListaErros = ListaErros + " - Razao<br/>";
    if ( bdrCNPJ     == "" ) ListaErros = ListaErros + " - CNPJ<br/>";
    if ( bdrCodigo   == "" ) ListaErros = ListaErros + " - Codigo<br/>";
    if ( bdrSituacao == "" ) ListaErros = ListaErros + " - Situacao<br/>";

    if (ListaErros != "") {
      fCriarAlertaModalCad(TP_ALERTA_AVISO,"Os seguintes campos não estão preenchido: <br/>" + ListaErros);
      return false;
    }

    return true;

  } catch (e) {
    fCriarAlertaModalCad(TP_ALERTA_ERRO, "fValidarDadosBdr"+MSG_ALERTA_ERRO);
    return false;
  }
}

function fSalvarDadosBdr(urlPadrao) {
  try {

    fLimparAreaAlertaModalCad();
    
    if ( !fValidarDadosBdr() )
        return false;

    iniciarAnimacaoSalvar();

    var bdrId       = $("#txtCadBdrId").val().trim();
    var bdrSetor    = $("#txtCadBdrSetor").val();
    var bdrSubSetor = $("#txtCadBdrSubSetor").val();
    var bdrSegmento = $("#txtCadBdrSegmento").val();
    var bdrNome     = $("#txtCadBdrNome").val().trim();
    var bdrRazao    = $("#txtCadBdrRazao").val().trim();
    var bdrCNPJ     = $("#txtCadBdrCNPJ").val().trim();
    var bdrCodigo   = $("#txtCadBdrCodigo").val().trim();
    var bdrIsin     = $("#txtCadBdrIsin").val().trim();
    var bdrCodCVM   = $("#txtCadBdrCodCVM").val().trim();
    var bdrTipo     = $("#txtCadBdrTipo").val();
    var bdrSituacao = $("#txtCadBdrSituacao").val();

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "bdr/salvar",
      data: {
        bdrId: bdrId,
        bdrSetor: bdrSetor,
        bdrSubSetor: bdrSubSetor,
        bdrSegmento: bdrSegmento,
        bdrNome: bdrNome,
        bdrRazao: bdrRazao,
        bdrCNPJ: bdrCNPJ,
        bdrCodigo: bdrCodigo,
        bdrIsin: bdrIsin,
        bdrCodCVM: bdrCodCVM,
        bdrTipo: bdrTipo,
        bdrSituacao: bdrSituacao,
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
          $("#PopModalDetalheBdr").modal("hide");
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
    CriarAlertaModal(TP_ALERTA_ERRO, "fSalvarDadosBdr"+MSG_ALERTA_ERRO);
    return;
  }
}