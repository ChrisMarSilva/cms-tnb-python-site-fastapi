
function buscarDataHora() {
  try {
    var data = new Date();
    $("#divDtHr").html("&Uacute;ltima Atualiza&ccedil;&atilde;o: " +data.toLocaleDateString("pt-BR") +" as " +fHoraAtual() );
  } catch (e) {
	  fCriarAlertaPrinc(TP_ALERTA_ERRO, "Falha(buscarDataHora): " + e.message); 
  }
}

function fHoraAtual() {
  try {
    var data = new Date();
    return data.toLocaleTimeString("pt-BR");
  } catch (e) {
	  fCriarAlertaPrinc(TP_ALERTA_ERRO, "Falha(fHoraAtual): " + e.message);
  }
}

function fDataAtual(){	
	var data = new Date();
	var dia  = ("0" + data.getDate()).substr(-2);
	var mes  = ("0" + (data.getMonth() + 1)).substr(-2) ;
	var ano  = data.getFullYear();
	return  [ ano, mes, dia].join('-');		
}

function fDataPrimeira(){	
	var data            = new Date();
	var DataPrimeiroDia = new Date(data.getFullYear(), data.getMonth(), 1);
	var dia             = ("0" + DataPrimeiroDia.getDate()).substr(-2);
	var mes             = ("0" + (DataPrimeiroDia.getMonth() + 1)).substr(-2) ;
	var ano             = DataPrimeiroDia.getFullYear();
	return [ ano, mes, dia].join('-');	
}

function fDataUltima(){	
	var data            = new Date();
	var DataUltimoDia   = new Date(data.getFullYear(), data.getMonth() + 1, 0);
	var dia             = ("0" + DataUltimoDia.getDate()).substr(-2);
	var mes             = ("0" + (DataUltimoDia.getMonth() + 1)).substr(-2) ;
	var ano             = DataUltimoDia.getFullYear();
	return [ ano, mes, dia].join('-');		
}

function fDataAnoPrimeira(){	
	var data = new Date();
	var dia  = "01";
	var mes  = "01";
	var ano  = data.getFullYear();
	return  [ ano, mes, dia].join('-');		
}

function fDataAnoUltima(){	
	var data = new Date();
	var dia  = "31";
	var mes  = "12";
	var ano  = data.getFullYear();
	return  [ ano, mes, dia].join('-');		
}


