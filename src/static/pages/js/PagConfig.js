//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

$(document).ready(function () {

  //$(this).attr("title", "Config. - " + NOME_PROJETO);

  $("#MnPrincConfig").addClass("active open");

  fLimparAreaAlerta("AreaAlertaPrincConfigCotacao");
  fLimparAreaAlerta("AreaAlertaPrincConfigIndicador");
  fLimparAreaAlerta("AreaAlertaPrincConfigEmail");
  fLimparAreaAlerta("AreaAlertaPrincConfigLimpeza");

});

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fCarregarConfigCotacao(urlPadrao) {
  try {

    fLimparAreaAlerta("AreaAlertaPrincConfigCotacao");

    $("#txtConfigCotacaoProc").attr("checked", false);
    $("#txtConfigCotacaoDOM").attr("checked", false);
    $("#txtConfigCotacaoSEG").attr("checked", false);
    $("#txtConfigCotacaoTER").attr("checked", false);
    $("#txtConfigCotacaoQUA").attr("checked", false);
    $("#txtConfigCotacaoQUI").attr("checked", false);
    $("#txtConfigCotacaoSEX").attr("checked", false);
    $("#txtConfigCotacaoSAB").attr("checked", false);
    $("#txtConfigCotacaoLogErr").attr("checked", false);
    $("#txtConfigCotacaoArqv").attr("checked", false);
    $("#txtConfigCotacaoHrInicio").val("00:00:00");
    $("#txtConfigCotacaoHrFim").val("00:00:00");
    $("#txtConfigCotacaoHrIntervalo").val("00:00:00");
    $("#txtConfigCotacaoTpLista").val("");

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "config/carregar",
      data: { Tipo: "Cotacao" },
      success: function (result) {

        var resultado = result.data.Resultado;
        var mensagem = result.data.Mensagem;
        var Config = result.data.Dados;

        if (resultado == "NSESSAO") {
          $(location).attr('href', urlPadrao + '/login');
          return false;
        } else if (resultado == "NOK") {
          fCriarAlerta("AreaAlertaPrincConfigCotacao", TP_ALERTA_AVISO, mensagem);
        } else if (resultado == "FALHA") {
          fCriarAlerta("AreaAlertaPrincConfigCotacao", TP_ALERTA_ERRO, mensagem);
        } else if (resultado == "OK") {
          if (Config.HrInicio) {
            $("#txtConfigCotacaoProc").attr("checked", (Config.Proc == "S"));
            $("#txtConfigCotacaoDOM").attr("checked", (Config.ProcDOM == "S"));
            $("#txtConfigCotacaoSEG").attr("checked", (Config.ProcSEG == "S"));
            $("#txtConfigCotacaoTER").attr("checked", (Config.ProcTER == "S"));
            $("#txtConfigCotacaoQUA").attr("checked", (Config.ProcQUA == "S"));
            $("#txtConfigCotacaoQUI").attr("checked", (Config.ProcQUI == "S"));
            $("#txtConfigCotacaoSEX").attr("checked", (Config.ProcSEX == "S"));
            $("#txtConfigCotacaoSAB").attr("checked", (Config.ProcSAB == "S"));
            $("#txtConfigCotacaoLogErr").attr("checked", (Config.RegLogErr == "S"));
            $("#txtConfigCotacaoArqv").attr("checked", (Config.CriarArqv == "S"));
            $("#txtConfigCotacaoHrInicio").val(Config.HrInicio);
            $("#txtConfigCotacaoHrFim").val(Config.HrFim);
            $("#txtConfigCotacaoHrIntervalo").val(Config.HrIntervalo);
            $("#txtConfigCotacaoTpLista").val(Config.TpLista);
          } else {
            //fCriarAlerta("AreaAlertaPrincConfigCotacao", TP_ALERTA_ERRO, mensagem);
          }
        } else {
          fCriarAlerta("AreaAlertaPrincConfigCotacao", TP_ALERTA_ERRO, mensagem);
        }
      },
      error: function (data) {
        fCriarAlerta("AreaAlertaPrincConfigCotacao", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      }
    });

  } catch (e) {
    fCriarAlerta("AreaAlertaPrincConfigCotacao", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
  }
}

function fSalvarConfigCotacao( urlPadrao ) {
  try {

    fLimparAreaAlerta("AreaAlertaPrincConfigCotacao");

    iniciarAnimacaoSalvar();

    var Proc        = $("#txtConfigCotacaoProc").is(":checked") ? "S" : "N";
    var ProcDOM     = $("#txtConfigCotacaoDOM").is(":checked") ? "S" : "N";
    var ProcSEG     = $("#txtConfigCotacaoSEG").is(":checked") ? "S" : "N";
    var ProcTER     = $("#txtConfigCotacaoTER").is(":checked") ? "S" : "N";
    var ProcQUA     = $("#txtConfigCotacaoQUA").is(":checked") ? "S" : "N";
    var ProcQUI     = $("#txtConfigCotacaoQUI").is(":checked") ? "S" : "N";
    var ProcSEX     = $("#txtConfigCotacaoSEX").is(":checked") ? "S" : "N";
    var ProcSAB     = $("#txtConfigCotacaoSAB").is(":checked") ? "S" : "N";
    var RegLogErr   = $("#txtConfigCotacaoLogErr").is(":checked") ? "S" : "N";
    var CriarArqv   = $("#txtConfigCotacaoArqv").is(":checked") ? "S" : "N";
    var HrInicio    = $("#txtConfigCotacaoHrInicio").val();
    var HrFim       = $("#txtConfigCotacaoHrFim").val();
    var HrIntervalo = $("#txtConfigCotacaoHrIntervalo").val();
    var TpLista     = $("#txtConfigCotacaoTpLista").val();

    HrInicio    = tirarFormacataoData( HrInicio );
    HrFim       = tirarFormacataoData( HrFim );
    HrIntervalo = tirarFormacataoData( HrIntervalo );

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "config/salvar",
      data: {
        Tipo        : "Cotacao",
        Proc        : Proc,
        ProcDOM     : ProcDOM,
        ProcSEG     : ProcSEG,
        ProcTER     : ProcTER,
        ProcQUA     : ProcQUA,
        ProcQUI     : ProcQUI,
        ProcSEX     : ProcSEX,
        ProcSAB     : ProcSAB,
        RegLogErr   : RegLogErr,
        CriarArqv   : CriarArqv,
        HrInicio    : HrInicio,
        HrFim       : HrFim,
        HrIntervalo : HrIntervalo,
        TpLista     : TpLista
      },
      success: function (result) {

        finalizarAnimacaoSalvar();

        var resultado = result.data.Resultado;
        var mensagem  = result.data.Mensagem;

        if (resultado == "NSESSAO") {
          $(location).attr('href', urlPadrao + '/login');
          return false;
        } else if (resultado == "NOK") {
          fCriarAlerta("AreaAlertaPrincConfigCotacao", TP_ALERTA_AVISO, mensagem);
          return;
        } else if (resultado == "FALHA") {
          fCriarAlerta("AreaAlertaPrincConfigCotacao", TP_ALERTA_ERRO, mensagem);
          return;
        } else if (resultado == "OK") {
          fCriarAlerta("AreaAlertaPrincConfigCotacao", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
        } else {
          fCriarAlerta("AreaAlertaPrincConfigCotacao", TP_ALERTA_ERRO, mensagem);
          return;
        }

      },
      error: function (data) {
        finalizarAnimacaoSalvar();
        fCriarAlerta("AreaAlertaPrincConfigCotacao", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
        return;
      }
    });

  } catch (e) {
    finalizarAnimacaoSalvar();
    fCriarAlerta("AreaAlertaPrincConfigCotacao", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
  }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fCarregarConfigIndicador(urlPadrao) {
  try {

    fLimparAreaAlerta("AreaAlertaPrincConfigIndicador");

    $("#txtConfigIndicProc").attr("checked", false);
    $("#txtConfigIndicLogErr").attr("checked", false);
    $("#txtConfigIndicArqv").attr("checked", false);
    $("#txtConfigIndicDOM").attr("checked", false);
    $("#txtConfigIndicSEG").attr("checked", false);
    $("#txtConfigIndicTER").attr("checked", false);
    $("#txtConfigIndicQUA").attr("checked", false);
    $("#txtConfigIndicQUI").attr("checked", false);
    $("#txtConfigIndicSEX").attr("checked", false);
    $("#txtConfigIndicSAB").attr("checked", false);
    $("#txtConfigIndicHrInicio").val("00:00:00");
    $("#txtConfigIndicHrFim").val("00:00:00");
    $("#txtConfigIndicHrIntervalo").val("00:00:00");

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "config/carregar",
      data: { Tipo: "Indicador" },
      success: function (result) {

        var resultado = result.data.Resultado;
        var mensagem = result.data.Mensagem;
        var Config = result.data.Dados;

        if (resultado == "NSESSAO") {
          $(location).attr('href', urlPadrao + '/login');
          return false;
        } else if (resultado == "NOK") {
          fCriarAlerta("AreaAlertaPrincConfigIndicador", TP_ALERTA_AVISO, mensagem);
        } else if (resultado == "FALHA") {
          fCriarAlerta("AreaAlertaPrincConfigIndicador", TP_ALERTA_ERRO, mensagem);
        } else if (resultado == "OK") {
          if (Config.HrInicio) {
            $("#txtConfigIndicProc").attr("checked", (Config.Proc == "S"));
            $("#txtConfigIndicDOM").attr("checked", (Config.ProcDOM == "S"));
            $("#txtConfigIndicSEG").attr("checked", (Config.ProcSEG == "S"));
            $("#txtConfigIndicTER").attr("checked", (Config.ProcTER == "S"));
            $("#txtConfigIndicQUA").attr("checked", (Config.ProcQUA == "S"));
            $("#txtConfigIndicQUI").attr("checked", (Config.ProcQUI == "S"));
            $("#txtConfigIndicSEX").attr("checked", (Config.ProcSEX == "S"));
            $("#txtConfigIndicSAB").attr("checked", (Config.ProcSAB == "S"));
            $("#txtConfigIndicLogErr").attr("checked", (Config.RegLogErr == "S"));
            $("#txtConfigIndicArqv").attr("checked", (Config.CriarArqv == "S"));
            $("#txtConfigIndicHrInicio").val(Config.HrInicio);
            $("#txtConfigIndicHrFim").val(Config.HrFim);
            $("#txtConfigIndicHrIntervalo").val(Config.HrIntervalo);
          } else {
            // fCriarAlerta("AreaAlertaPrincConfigIndicador", TP_ALERTA_ERRO, mensagem);
          }
        } else {
          fCriarAlerta("AreaAlertaPrincConfigIndicador", TP_ALERTA_ERRO, mensagem);
        }
      },
      error: function (data) {
        fCriarAlerta("AreaAlertaPrincConfigIndicador", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      }
    });

  } catch (e) {
    fCriarAlerta("AreaAlertaPrincConfigIndicador", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
  }
}


function fSalvarConfigIndicador(urlPadrao) {
  try {

    fLimparAreaAlerta("AreaAlertaPrincConfigIndicador");

    iniciarAnimacaoSalvar();

    var Proc        = $("#txtConfigIndicProc").is(":checked") ? "S" : "N";
    var ProcDOM     = $("#txtConfigIndicDOM").is(":checked") ? "S" : "N";
    var ProcSEG     = $("#txtConfigIndicSEG").is(":checked") ? "S" : "N";
    var ProcTER     = $("#txtConfigIndicTER").is(":checked") ? "S" : "N";
    var ProcQUA     = $("#txtConfigIndicQUA").is(":checked") ? "S" : "N";
    var ProcQUI     = $("#txtConfigIndicQUI").is(":checked") ? "S" : "N";
    var ProcSEX     = $("#txtConfigIndicSEX").is(":checked") ? "S" : "N";
    var ProcSAB     = $("#txtConfigIndicSAB").is(":checked") ? "S" : "N";
    var RegLogErr   = $("#txtConfigIndicLogErr").is(":checked") ? "S" : "N";
    var CriarArqv   = $("#txtConfigIndicArqv").is(":checked") ? "S" : "N";
    var HrInicio    = $("#txtConfigIndicHrInicio").val();
    var HrFim       = $("#txtConfigIndicHrFim").val();
    var HrIntervalo = $("#txtConfigIndicHrIntervalo").val();

    HrInicio    = tirarFormacataoData( HrInicio    );
    HrFim       = tirarFormacataoData( HrFim       );
    HrIntervalo = tirarFormacataoData( HrIntervalo );

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "config/salvar",
      data: {
        Tipo        : "Indicador",
        Proc        : Proc,
        ProcDOM     : ProcDOM,
        ProcSEG     : ProcSEG,
        ProcTER     : ProcTER,
        ProcQUA     : ProcQUA,
        ProcQUI     : ProcQUI,
        ProcSEX     : ProcSEX,
        ProcSAB     : ProcSAB,
        RegLogErr   : RegLogErr,
        CriarArqv   : CriarArqv,
        HrInicio    : HrInicio,
        HrFim       : HrFim,
        HrIntervalo : HrIntervalo
      },
      success: function (result) {

        finalizarAnimacaoSalvar();

        var resultado = result.data.Resultado;
        var mensagem  = result.data.Mensagem;

        if (resultado == "NSESSAO") {
          $(location).attr('href', urlPadrao + '/login');
          return false;
        } else if (resultado == "NOK") {
          fCriarAlerta("AreaAlertaPrincConfigIndicador", TP_ALERTA_AVISO, mensagem);
          return;
        } else if (resultado == "FALHA") {
          fCriarAlerta("AreaAlertaPrincConfigIndicador", TP_ALERTA_ERRO, mensagem);
          return;
        } else if (resultado == "OK") {
          fCriarAlerta("AreaAlertaPrincConfigIndicador", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
        } else {
          fCriarAlerta("AreaAlertaPrincConfigIndicador", TP_ALERTA_ERRO, mensagem);
          return;
        }

      },
      error: function (data) {
        finalizarAnimacaoSalvar();
        fCriarAlerta("AreaAlertaPrincConfigIndicador", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
        return;
      }
    });

  } catch (e) {
    finalizarAnimacaoSalvar();
    fCriarAlerta("AreaAlertaPrincConfigIndicador", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
  }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fCarregarConfigEmail(urlPadrao) {
  try {

    fLimparAreaAlerta("AreaAlertaPrincConfigEmail");

    $("#txtConfigEmailProc").attr("checked", false);
    $("#txtConfigEmailLogErr").attr("checked", false);
    $("#txtConfigEmailArqv").attr("checked", false);
    $("#txtConfigEmailDOM").attr("checked", false);
    $("#txtConfigEmailSEG").attr("checked", false);
    $("#txtConfigEmailTER").attr("checked", false);
    $("#txtConfigEmailQUA").attr("checked", false);
    $("#txtConfigEmailQUI").attr("checked", false);
    $("#txtConfigEmailSEX").attr("checked", false);
    $("#txtConfigEmailSAB").attr("checked", false);
    $("#txtConfigEmailHrInicio").val("00:00:00");
    $("#txtConfigEmailHrFim").val("00:00:00");
    $("#txtConfigEmailHrIntervalo").val("00:00:00");
    $("#txtConfigEmailServHost").val("");
    $("#txtConfigEmailServPort").val("");
    $("#txtConfigEmailServUser").val("");
    $("#txtConfigEmailServPass").val("");
    $("#txtConfigEmailServDstPrinc").val("");
    $("#txtConfigEmailServDstCopia").val("");

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "config/carregar",
      data: { Tipo: "Email" },
      success: function (result) {

        var resultado = result.data.Resultado;
        var mensagem = result.data.Mensagem;
        var Config = result.data.Dados;

        if (resultado == "NSESSAO") {
          $(location).attr('href', urlPadrao + '/login');
          return false;
        } else if (resultado == "NOK") {
          fCriarAlerta("AreaAlertaPrincConfigEmail", TP_ALERTA_AVISO, mensagem);
        } else if (resultado == "FALHA") {
          fCriarAlerta("AreaAlertaPrincConfigEmail", TP_ALERTA_ERRO, mensagem);
        } else if (resultado == "OK") {
          if (Config.HrInicio) {
            $("#txtConfigEmailProc").attr("checked", (Config.Proc == "S"));
            $("#txtConfigEmailDOM").attr("checked", (Config.ProcDOM == "S"));
            $("#txtConfigEmailSEG").attr("checked", (Config.ProcSEG == "S"));
            $("#txtConfigEmailTER").attr("checked", (Config.ProcTER == "S"));
            $("#txtConfigEmailQUA").attr("checked", (Config.ProcQUA == "S"));
            $("#txtConfigEmailQUI").attr("checked", (Config.ProcQUI == "S"));
            $("#txtConfigEmailSEX").attr("checked", (Config.ProcSEX == "S"));
            $("#txtConfigEmailSAB").attr("checked", (Config.ProcSAB == "S"));
            $("#txtConfigEmailLogErr").attr("checked", (Config.RegLogErr == "S"));
            $("#txtConfigEmailArqv").attr("checked", (Config.CriarArqv == "S"));
            $("#txtConfigEmailHrInicio").val(Config.HrInicio);
            $("#txtConfigEmailHrFim").val(Config.HrFim);
            $("#txtConfigEmailHrIntervalo").val(Config.HrIntervalo);
            $("#txtConfigEmailServHost").val(Config.ServHost);
            $("#txtConfigEmailServPort").val(Config.ServPort);
            $("#txtConfigEmailServUser").val(Config.ServUser);
            $("#txtConfigEmailServPass").val(Config.ServPass);
            $("#txtConfigEmailServDstPrinc").val(Config.ServDstPrinc);
            $("#txtConfigEmailServDstCopia").val(Config.ServDstCopia);
          } else {
            //fCriarAlerta("AreaAlertaPrincConfigEmail", TP_ALERTA_ERRO, mensagem);
          }
        } else {
          fCriarAlerta("AreaAlertaPrincConfigEmail", TP_ALERTA_ERRO, mensagem);
        }
      },
      error: function (data) {
        fCriarAlerta("AreaAlertaPrincConfigEmail", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      }
    });

  } catch (e) {
    fCriarAlerta("AreaAlertaPrincConfigEmail", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
  }
}


function fSalvarConfigEmail(urlPadrao) {
  try {

    fLimparAreaAlerta("AreaAlertaPrincConfigEmail");

    iniciarAnimacaoSalvar();

    var Proc         = $("#txtConfigEmailProc").is(":checked") ? "S" : "N";
    var ProcDOM      = $("#txtConfigEmailDOM").is(":checked") ? "S" : "N";
    var ProcSEG      = $("#txtConfigEmailSEG").is(":checked") ? "S" : "N";
    var ProcTER      = $("#txtConfigEmailTER").is(":checked") ? "S" : "N";
    var ProcQUA      = $("#txtConfigEmailQUA").is(":checked") ? "S" : "N";
    var ProcQUI      = $("#txtConfigEmailQUI").is(":checked") ? "S" : "N";
    var ProcSEX      = $("#txtConfigEmailSEX").is(":checked") ? "S" : "N";
    var ProcSAB      = $("#txtConfigEmailSAB").is(":checked") ? "S" : "N";
    var RegLogErr    = $("#txtConfigEmailLogErr").is(":checked") ? "S" : "N";
    var CriarArqv    = $("#txtConfigEmailArqv").is(":checked") ? "S" : "N";
    var HrInicio     = $("#txtConfigEmailHrInicio").val();
    var HrFim        = $("#txtConfigEmailHrFim").val();
    var HrIntervalo  = $("#txtConfigEmailHrIntervalo").val();    
    var ServHost     = $("#txtConfigEmailServHost").val();
    var ServPort     = $("#txtConfigEmailServPort").val();
    var ServUser     = $("#txtConfigEmailServUser").val();
    var ServPass     = $("#txtConfigEmailServPass").val();
    var ServDstPrinc = $("#txtConfigEmailServDstPrinc").val();
    var ServDstCopia = $("#txtConfigEmailServDstCopia").val();

    HrInicio    = tirarFormacataoData( HrInicio    );
    HrFim       = tirarFormacataoData( HrFim       );
    HrIntervalo = tirarFormacataoData( HrIntervalo );

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "config/salvar",
      data: {
        Tipo         : "Email",
        Proc         : Proc,
        ProcDOM      : ProcDOM,
        ProcSEG      : ProcSEG,
        ProcTER      : ProcTER,
        ProcQUA      : ProcQUA,
        ProcQUI      : ProcQUI,
        ProcSEX      : ProcSEX,
        ProcSAB      : ProcSAB,
        RegLogErr    : RegLogErr,
        CriarArqv    : CriarArqv,
        HrInicio     : HrInicio,
        HrFim        : HrFim,
        HrIntervalo  : HrIntervalo,
        ServHost     : ServHost,
        ServPort     : ServPort,
        ServUser     : ServUser,
        ServPass     : ServPass,
        ServDstPrinc : ServDstPrinc,
        ServDstCopia : ServDstCopia
      },
      success: function (result) {

        finalizarAnimacaoSalvar();

        var resultado = result.data.Resultado;
        var mensagem  = result.data.Mensagem;

        if (resultado == "NSESSAO") {
          $(location).attr('href', urlPadrao + '/login');
          return false;
        } else if (resultado == "NOK") {
          fCriarAlerta("AreaAlertaPrincConfigEmail", TP_ALERTA_AVISO, mensagem);
          return;
        } else if (resultado == "FALHA") {
          fCriarAlerta("AreaAlertaPrincConfigEmail", TP_ALERTA_ERRO, mensagem);
          return;
        } else if (resultado == "OK") {
          fCriarAlerta("AreaAlertaPrincConfigEmail", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
        } else {
          fCriarAlerta("AreaAlertaPrincConfigEmail", TP_ALERTA_ERRO, mensagem);
          return;
        }

      },
      error: function (data) {
        finalizarAnimacaoSalvar();
        fCriarAlerta("AreaAlertaPrincConfigEmail", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
        return;
      }
    });

  } catch (e) {
    finalizarAnimacaoSalvar();
    fCriarAlerta("AreaAlertaPrincConfigEmail", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
  }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fCarregarConfigLimpeza(urlPadrao) {
  try {

    fLimparAreaAlerta("AreaAlertaPrincConfigLimpeza");

    $("#txtConfigLimpzProc").attr("checked", false);
    $("#txtConfigLimpzLogErr").attr("checked", false);
    $("#txtConfigLimpzArqv").attr("checked", false);
    $("#txtConfigLimpzDOM").attr("checked", false);
    $("#txtConfigLimpzSEG").attr("checked", false);
    $("#txtConfigLimpzTER").attr("checked", false);
    $("#txtConfigLimpzQUA").attr("checked", false);
    $("#txtConfigLimpzQUI").attr("checked", false);
    $("#txtConfigLimpzSEX").attr("checked", false);
    $("#txtConfigLimpzSAB").attr("checked", false);
    $("#txtConfigLimpzHrInicio").val("00:00:00");
    $("#txtConfigLimpzHrFim").val("00:00:00");
    $("#txtConfigLimpzHrIntervalo").val("00:00:00");
    $("#txtConfigLimpzDiasRetencao").val("");

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "config/carregar",
      data: { Tipo: "Limpeza" },
      success: function (result) {

        var resultado = result.data.Resultado;
        var mensagem = result.data.Mensagem;
        var Config = result.data.Dados;

        if (resultado == "NSESSAO") {
          $(location).attr('href', urlPadrao + '/login');
          return false;
        } else if (resultado == "NOK") {
          fCriarAlerta("AreaAlertaPrincConfigLimpeza", TP_ALERTA_AVISO, mensagem);
        } else if (resultado == "FALHA") {
          fCriarAlerta("AreaAlertaPrincConfigLimpeza", TP_ALERTA_ERRO, mensagem);
        } else if (resultado == "OK") {
          if (Config.HrInicio) {
            $("#txtConfigLimpzProc").attr("checked", (Config.Proc == "S"));
            $("#txtConfigLimpzDOM").attr("checked", (Config.ProcDOM == "S"));
            $("#txtConfigLimpzSEG").attr("checked", (Config.ProcSEG == "S"));
            $("#txtConfigLimpzTER").attr("checked", (Config.ProcTER == "S"));
            $("#txtConfigLimpzQUA").attr("checked", (Config.ProcQUA == "S"));
            $("#txtConfigLimpzQUI").attr("checked", (Config.ProcQUI == "S"));
            $("#txtConfigLimpzSEX").attr("checked", (Config.ProcSEX == "S"));
            $("#txtConfigLimpzSAB").attr("checked", (Config.ProcSAB == "S"));
            $("#txtConfigLimpzLogErr").attr("checked", (Config.RegLogErr == "S"));
            $("#txtConfigLimpzArqv").attr("checked", (Config.CriarArqv == "S"));
            $("#txtConfigLimpzHrInicio").val(Config.HrInicio);
            $("#txtConfigLimpzHrFim").val(Config.HrFim);
            $("#txtConfigLimpzHrIntervalo").val(Config.HrIntervalo);
            $("#txtConfigLimpzDiasRetencao").val(Config.DiasRetencao);
          } else {
            //fCriarAlerta("AreaAlertaPrincConfigLimpeza", TP_ALERTA_ERRO, mensagem);
          }
        } else {
          fCriarAlerta("AreaAlertaPrincConfigLimpeza", TP_ALERTA_ERRO, mensagem);
        }
      },
      error: function (data) {
        fCriarAlerta("AreaAlertaPrincConfigLimpeza", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
      }
    });

  } catch (e) {
    fCriarAlerta("AreaAlertaPrincConfigLimpeza", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
  }
}

function fSalvarConfigLimpeza(urlPadrao) {
  try {

    fLimparAreaAlerta("AreaAlertaPrincConfigLimpeza");

    iniciarAnimacaoSalvar();

    var Proc         = $("#txtConfigLimpzProc").is(":checked") ? "S" : "N";
    var ProcDOM      = $("#txtConfigLimpzDOM").is(":checked") ? "S" : "N";
    var ProcSEG      = $("#txtConfigLimpzSEG").is(":checked") ? "S" : "N";
    var ProcTER      = $("#txtConfigLimpzTER").is(":checked") ? "S" : "N";
    var ProcQUA      = $("#txtConfigLimpzQUA").is(":checked") ? "S" : "N";
    var ProcQUI      = $("#txtConfigLimpzQUI").is(":checked") ? "S" : "N";
    var ProcSEX      = $("#txtConfigLimpzSEX").is(":checked") ? "S" : "N";
    var ProcSAB      = $("#txtConfigLimpzSAB").is(":checked") ? "S" : "N";
    var RegLogErr    = $("#txtConfigLimpzLogErr").is(":checked") ? "S" : "N";
    var CriarArqv    = $("#txtConfigLimpzArqv").is(":checked") ? "S" : "N";
    var HrInicio     = $("#txtConfigLimpzHrInicio").val();
    var HrFim        = $("#txtConfigLimpzHrFim").val();
    var HrIntervalo  = $("#txtConfigLimpzHrIntervalo").val();
    var DiasRetencao = $("#txtConfigLimpzDiasRetencao").val();

    HrInicio    = tirarFormacataoData( HrInicio    );
    HrFim       = tirarFormacataoData( HrFim       );
    HrIntervalo = tirarFormacataoData( HrIntervalo );

    $.ajax({
      cache: "false",
      dataType: "json",
      async: true,
      type: "POST",
      url: urlPadrao + "config/salvar",
      data: {
        Tipo         : "Limpeza",
        Proc         : Proc,
        ProcDOM      : ProcDOM,
        ProcSEG      : ProcSEG,
        ProcTER      : ProcTER,
        ProcQUA      : ProcQUA,
        ProcQUI      : ProcQUI,
        ProcSEX      : ProcSEX,
        ProcSAB      : ProcSAB,
        RegLogErr    : RegLogErr,
        CriarArqv    : CriarArqv,
        HrInicio     : HrInicio,
        HrFim        : HrFim,
        HrIntervalo  : HrIntervalo,
        DiasRetencao : DiasRetencao
      },
      success: function (result) {

        finalizarAnimacaoSalvar();

        var resultado = result.data.Resultado;
        var mensagem  = result.data.Mensagem;

        if (resultado == "NSESSAO") {
          $(location).attr('href', urlPadrao + '/login');
          return false;
        } else if (resultado == "NOK") {
          fCriarAlerta("AreaAlertaPrincConfigLimpeza", TP_ALERTA_AVISO, mensagem);
          return;
        } else if (resultado == "FALHA") {
          fCriarAlerta("AreaAlertaPrincConfigLimpeza", TP_ALERTA_ERRO, mensagem);
          return;
        } else if (resultado == "OK") {
          fCriarAlerta("AreaAlertaPrincConfigLimpeza", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
        } else {
          fCriarAlerta("AreaAlertaPrincConfigLimpeza", TP_ALERTA_ERRO, mensagem);
          return;
        }

      },
      error: function (data) {
        finalizarAnimacaoSalvar();
        fCriarAlerta("AreaAlertaPrincConfigLimpeza", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
        return;
      }
    });

  } catch (e) {
    finalizarAnimacaoSalvar();
    fCriarAlerta("AreaAlertaPrincConfigLimpeza", TP_ALERTA_ERRO, MSG_ALERTA_ERRO);
  }
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------
