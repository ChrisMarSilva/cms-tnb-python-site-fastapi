//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

$(document).ready(function() {
	//$(this).attr("title", ":: TnB - Comentarios ::");
	$("#MnPrincComentarios").addClass("active open");
	fLimparAreaAlerta("AreaAlertaPrinc");
});


//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fMostrarOcultarRespostas( IdComent ){
	var BtnToggleRespostas = $("#BtnToggleRespostas"+IdComent);
	var DivResposta        = $("#DivResposta"+IdComent);
	var qtde               = BtnToggleRespostas.data("qtde");
	if (  DivResposta.is(':visible') ){
		if( qtde > 1 ) BtnToggleRespostas.html('Ver todas as '+qtde+' respostas <i style="font-size: 12px;" class="fa fa-chevron-down"></i>')
		else           BtnToggleRespostas.html('Ver resposta <i style="font-size: 12px;" class="fa fa-chevron-down"></i>');
	}else{
		if( qtde > 1 ) BtnToggleRespostas.html('Ocultar respostas <i style="font-size: 12px;" class="fa fa-chevron-up"></i>')
		else           BtnToggleRespostas.html('Ocultar resposta <i style="font-size: 12px;" class="fa fa-chevron-up"></i>');
	}
	DivResposta.slideToggle("slow");  
}


function formatarTeste(str) {
    return str.replace(/<br>/g, '\n').replace(/(<br\/>)+/g, "\n")
}  

function formatarTeste0(str) {
    //return str.replace(/(?:\r\n|\r|\n)/g, '<br />');
    //var t = x.replace(/(^|\r\n|\n)([^*]|$)/g, "$1\r\n$2");
    ////String html = original.replaceAll("\\n\\r","&lt;br&gt;");
}  


function formatarTeste1 (str, is_xhtml) {
    var breakTag = (is_xhtml || typeof is_xhtml === 'undefined') ? '<br />' : '<br>';
    return (str + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + breakTag + '$2');
}  

function formatarTeste2 (str, is_xhtml) {
    if (typeof str === 'undefined' || str === null) {
        return '';
    }
    var breakTag = (is_xhtml || typeof is_xhtml === 'undefined') ? '<br />' : '<br>';
    return (str + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + breakTag + '$2');
}

function formatarTeste3 (str, is_xhtml) {
  // http://kevin.vanzonneveld.net
  // +   original by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
  // +   improved by: Philip Peterson
  // +   improved by: Onno Marsman
  // +   improved by: Atli Þór
  // +   bugfixed by: Onno Marsman
  // +      input by: Brett Zamir (http://brett-zamir.me)
  // +   bugfixed by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
  // +   improved by: Brett Zamir (http://brett-zamir.me)
  // +   improved by: Maximusya
  // *     example 1: nl2br('Kevin\nvan\nZonneveld');
  // *     returns 1: 'Kevin<br />\nvan<br />\nZonneveld'
  // *     example 2: nl2br("\nOne\nTwo\n\nThree\n", false);
  // *     returns 2: '<br>\nOne<br>\nTwo<br>\n<br>\nThree<br>\n'
  // *     example 3: nl2br("\nOne\nTwo\n\nThree\n", true);
  // *     returns 3: '<br />\nOne<br />\nTwo<br />\n<br />\nThree<br />\n'
  var breakTag = (is_xhtml || typeof is_xhtml === 'undefined') ? '<br ' + '/>' : '<br>'; // Adjust comment to avoid issue on phpjs.org display

  return (str + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + breakTag + '$2');
}


function fMontarDivComentario( urlPadrao, DadosComent ) {	
	try {

		var TxtHTML = '';
		
		TxtHTML += '<!-- DivComentario --> \n';
		TxtHTML += '<div class="border border-dark rounded mb-2" > \n';

		TxtHTML += '	<!-- row -->';
		TxtHTML += '	<div class="row clearfix"  style="margin: 0px; padding: 0px;"> \n';

		var DirFotoComent =  urlPadrao + ( ( DadosComent.Foto != "") ? DadosComent.Foto :'static/pages/img/pessoa-icon.png');

		TxtHTML += '		<!-- col-1 --> \n';
		TxtHTML += '		<div class="col-sm-1 col-md-1 col-lg-1 col-xl-1 text-center" style="margin: 0px; padding: 0px; padding-top: 10px;"> \n';
		TxtHTML += '			<img id="imgFotoPerfilComent'+DadosComent.Id+'" src="'+DirFotoComent+'" onerror="this.onerror=null;this.src=\'/static/pages/img/pessoa-icon.png\';"  alt="icone" width="60" height="60" class="img rounded-circle" alt="Foto Perfil" /> \n';
		TxtHTML += '		</div> \n';
		TxtHTML += '		<!-- col-1 --> \n';

		TxtHTML += '		<!-- col-11 --> \n';
		TxtHTML += '		<div class="col-sm-11 col-md-11 col-lg-11 col-xl-11" style="margin: 0px; padding: 0px;"> \n';

		TxtHTML += '			<!-- DivDadosUserComentario --> \n';
		TxtHTML += '			<div class="header" style="margin: 0px; padding: 0px; padding-top: 10px; padding-bottom: 10px;"> \n';              
		TxtHTML += '				<span class="font-weight-bold text-su ccess" style="font-size: 14px;">'+DadosComent.Nome+'</span>&nbsp; &nbsp;<small class="text-info" style="font-size: 11px;">( '+DadosComent.DtHr+' )</small> \n';         
		TxtHTML += '				<ul class="header-dropdown"> \n';
		TxtHTML += '					<li class="dropdown"> \n';
		TxtHTML += '						<a href="javascript:void(0);" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"> <i class="zmdi zmdi-more"></i> </a> \n';
		TxtHTML += '						<ul class="dropdown-menu dropdown-menu-right"> \n';
		if ( DadosComent.ExibeBtnDenu == "S" ) TxtHTML += '							<li><a href="javascript:void(0);" onclick="fMostrarModalDenunciar('+DadosComent.Id+');"                      > <i class="fa fa-warning"       aria-hidden="true"></i> &nbsp; Denunciar </a></li> \n';
		if ( DadosComent.ExibeBtnEdit == "S" ) TxtHTML += '							<li><a href="javascript:void(0);" onclick="fMostrarEditarComentario( '+DadosComent.Id+');"                   > <i class="fa fa-pencil fa-lg"  aria-hidden="true"></i> &nbsp; Editar    </a></li> \n';
		if ( DadosComent.ExibeBtnExcl == "S" ) TxtHTML += '							<li><a href="javascript:void(0);" onclick="fExcluirComentario( \''+urlPadrao +'\','+DadosComent.Id+',\'A\');"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> &nbsp; Excluir   </a></li> \n';
		TxtHTML += '						</ul> \n';
		TxtHTML += '					</li> \n';
		TxtHTML += '				</ul> \n';
		TxtHTML += '			</div> \n';
		TxtHTML += '			<!-- DivDadosUserComentario --> \n';

		TxtHTML += '			<!-- DivBody -->';
		TxtHTML += '			<div class="body" style="margin: 0px; padding: 0px;"> \n';

		TxtHTML += '				<!-- DivTextoComentario -->';
		TxtHTML += '			 	<div class="row clearfix" style="margin: 0px; padding: 0px;">';
		TxtHTML += '					<div class="col-sm-12 col-md-12 col-lg-12 col-xl-12" style="margin: 0px; padding: 0px; line-height: 1.3em; font-size: 10pt"> ';
		TxtHTML += '						<span id="DivTextoComentario'+DadosComent.Id+'" class="text-muted" style="font-size: 13px;">'+DadosComent.Texto+'</span>';
		TxtHTML += '						<span id="DivEditartTextoComentario'+DadosComent.Id+'" class="text-muted" style="display: none; font-size: 14px;">';
		TxtHTML += '							<textarea data-autoresize style="font-size:14px; resize:none; overflow:hidden; box-sizing:border-box;" class="form-control form-control-sm"  id="TxtTextoComentario'+DadosComent.Id+'" placeholder="Adicione uma Comentário...">'+ formatarTeste( DadosComent.Texto )+'</textarea>';
		// TxtHTML += '							<br/>';
		TxtHTML += '							<div class="text-right">';
		TxtHTML += '								<a style="font-size:12px; width: 120px; "  class="btn btn-sm btn-primary btn-round waves-effect" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fSalvarDadosComentario(\''+urlPadrao +'\','+DadosComent.Id+');"> <i class="fa fa-paper-plane" aria-hidden="true"></i> &nbsp; SALVAR </a>';
		TxtHTML += '								&nbsp;';
		TxtHTML += '								<a style="font-size:12px; width: 120px; "  class="btn btn-sm btn-light btn-simple btn-round waves-effect" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fEsconderEditarComentario('+DadosComent.Id+');"> <i class="fa fa-paper-plane" aria-hidden="true"></i> &nbsp; CANCELAR </a>';
		TxtHTML += '							</div>';
		TxtHTML += '							<br/>';
		TxtHTML += '						</span>';
		TxtHTML += '					</div>';
		TxtHTML += '				</div>';
		TxtHTML += '				<!-- DivTextoComentario -->';

		//TxtHTML += '			<br/>';

		TxtHTML += '			<!-- DivBotaoComentario -->';
		TxtHTML += '			<div class="row clearfix" style="margin: 0px; padding: 0px; padding-top: 10px; ">';
		TxtHTML += '				<div class="col-sm-8 col-md-8 col-lg-8 col-xl-8 text-left" style="margin: 0px; padding: 0px;">';		
		if ( DadosComent.MarcarGostei    == "S" ) TxtHTML += '					<a class="btn btn-sm btn-primary btn-simple btn-round waves-effect" href="javascript:void(0);" style="font-size: 10px; width: 90px; " role="button" aria-pressed="true" data-selc="'+DadosComent.MarcarGostei+'"    id="BtnGostei'+DadosComent.Id+'"    onclick="fSalvarDadosReacao(\''+urlPadrao +'\','+DadosComent.Id+',\'A\');"> <i id="iGostei'+DadosComent.Id+'"    style="font-size: 15px;" class="fa fa-thumbs-up">   </i> &nbsp; <span style="font-size: 12px;" class="text-primary" id="QtdeGostei'+DadosComent.Id+'"   >'+DadosComent.QtdeGostei+'   </span> </a>';
		if ( DadosComent.MarcarGostei    == "N" ) TxtHTML += '					<a class="btn btn-sm btn-light btn-simple btn-round waves-effect" href="javascript:void(0);" style="font-size: 10px; width: 90px; " role="button" aria-pressed="true" data-selc="'+DadosComent.MarcarGostei+'"    id="BtnGostei'+DadosComent.Id+'"    onclick="fSalvarDadosReacao(\''+urlPadrao +'\','+DadosComent.Id+',\'A\');"> <i id="iGostei'+DadosComent.Id+'"    style="font-size: 15px;" class="fa fa-thumbs-up">   </i> &nbsp; <span style="font-size: 12px;" class="text-muted"   id="QtdeGostei'+DadosComent.Id+'"   >'+DadosComent.QtdeGostei+'   </span> </a>';
		if ( DadosComent.MarcarNaoGostei == "S" ) TxtHTML += '					<a class="btn btn-sm btn-primary btn-simple btn-round waves-effect" href="javascript:void(0);" style="font-size: 10px; width: 90px; " role="button" aria-pressed="true" data-selc="'+DadosComent.MarcarNaoGostei+'" id="BtnNaoGostei'+DadosComent.Id+'" onclick="fSalvarDadosReacao(\''+urlPadrao +'\','+DadosComent.Id+',\'B\');"> <i id="iNaoGostei'+DadosComent.Id+'" style="font-size: 15px;" class="fa fa-thumbs-down"> </i> &nbsp; <span style="font-size: 12px;" class="text-primary" id="QtdeNaoGostei'+DadosComent.Id+'">'+DadosComent.QtdeNaoGostei+'</span> </a>';
		if ( DadosComent.MarcarNaoGostei == "N" ) TxtHTML += '					<a class="btn btn-sm btn-light btn-simple btn-round waves-effect" href="javascript:void(0);" style="font-size: 10px; width: 90px; " role="button" aria-pressed="true" data-selc="'+DadosComent.MarcarNaoGostei+'" id="BtnNaoGostei'+DadosComent.Id+'" onclick="fSalvarDadosReacao(\''+urlPadrao +'\','+DadosComent.Id+',\'B\');"> <i id="iNaoGostei'+DadosComent.Id+'" style="font-size: 15px;" class="fa fa-thumbs-down"> </i> &nbsp; <span style="font-size: 12px;" class="text-muted"   id="QtdeNaoGostei'+DadosComent.Id+'">'+DadosComent.QtdeNaoGostei+'</span> </a>';
		TxtHTML += '					<a class="btn btn-sm btn-primary btn-round waves-effect font-weight-bold" href="javascript:void(0);" style="font-size: 10px; width: 120px;" role="button" aria-pressed="true" id="BtnToggleResponder'+DadosComent.Id+'" onclick="fMostrarNovaResposta('+DadosComent.Id+');"> <i style="font-size: 15px;" class="fa fa-commenting"> </i>  &nbsp; RESPONDER  </a>';
		if ( DadosComent.ExibirDadosAdmin == "S" ) TxtHTML += '					<a class="btn btn-sm btn-warning btn-round waves-effect" href="javascript:void(0);" style="font-size: 10px; width: 120px;" title="Visualizar" role="button" aria-pressed="true" id="BtnVisualizarComentario'+DadosComent.Id+'" onclick="fVisualizarDadosAdmin(\''+urlPadrao +'\','+DadosComent.Id+');"> <i style="font-size: 15px;" class="fa fa-eye"> </i> &nbsp;VISUALIZAR</a>';
		TxtHTML += '				</div>';
		TxtHTML += '				<div class="col-sm-4 col-md-4 col-lg-4col-xl-4 text-right">';
		//if ( DadosComent.QtdeComent == 1 ) TxtHTML += '					<a class="text-muted font-weight-bold  btn btn-sm btn-light btn-simple" href="javascript:void(0);" role="button" aria-pressed="true" style="font-size: 12px;" id="BtnToggleRespostas'+DadosComent.Id+'" data-qtde="'+DadosComent.QtdeComent+'" onclick="fMostrarOcultarRespostas('+DadosComent.Id+');"> Ver resposta &nbsp;<i style="font-size: 12px;" class="fa fa-chevron-down"> </i> </a>';
		//if ( DadosComent.QtdeComent >  1 ) TxtHTML += '					<a class="text-muted font-weight-bold  btn btn-sm btn-light btn-simple" href="javascript:void(0);" role="button" aria-pressed="true" style="font-size: 12px;" id="BtnToggleRespostas'+DadosComent.Id+'" data-qtde="'+DadosComent.QtdeComent+'" onclick="fMostrarOcultarRespostas('+DadosComent.Id+');"> Ver todas as '+DadosComent.QtdeComent+' respostas &nbsp;<i style="font-size: 12px;" class="fa fa-chevron-down"> </i> </a>';
		TxtHTML += '				</div>';
		TxtHTML += '			</div>';
		TxtHTML += '			<!-- DivBotaoComentario -->';

		TxtHTML += '			<!-- DivResponder -->';
		TxtHTML += '			<div id="DivResponder'+DadosComent.Id+'" style="display: none; ">';
		TxtHTML += '				<br/>';
		TxtHTML += '				<div class="row clearfix">';
		TxtHTML += '					<div class="col-10">';
		TxtHTML += '						<textarea data-autoresize style="font-size:14px; wi dth: 100%; resize:none; overflow:hidden; box-sizing:border-box;" max length="2000" rows="2" class="form-control form-control-sm" id="TxtTextoResposta'+DadosComent.Id+'" placeholder="Adicione uma resposta..."></textarea>';
		TxtHTML += '					</div>';
		TxtHTML += '					<div class="col-2 text-right">';
		TxtHTML += '						<a style="font-size:14px; width: 150px;" class="btn btn-sm btn-primary btn-round waves-effect" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fSalvarDadosResposta(\''+urlPadrao +'\','+DadosComent.Id+', \'\');"> <i id="iSalvar"class="fa fa-paper-plane" aria-hidden="true"></i> &nbsp; ENVIAR </a>';
		TxtHTML += '					</div>';
		TxtHTML += '				</div>';
		TxtHTML += '			</div>';
		TxtHTML += '			<!-- DivResponder -->';		

		if ( DadosComent.ListaResp && DadosComent.ListaResp.length > 0 ){
			TxtHTML += '			<!-- DivResposta -->';
			TxtHTML += '			<div id="DivResposta'+DadosComent.Id+'" style="di splay: none; margin: 0px; padding: 0px;">';
			// TxtHTML += '				<hr class="border-muted" style="margin-bottom: 10px;!important; margin-top: 10px;!important; "/>';
			var fLenn = DadosComent.ListaResp.length;
			for (y = 0; y < fLenn; y++){
				
				TxtHTML += '				<hr class="border-muted" style="margin-bottom: 10px;!important; margin-top: 10px;!important; margin-right: 30px;"/>';

				TxtHTML += '				<!-- DivComentResposta -->';
				TxtHTML += '				<div class="row clearfix" style="margin: 0px; padding: 0px; margin-bottom: 5px;!important; ">';

				var DirFotoRespComent =  urlPadrao + ( ( DadosComent.ListaResp[y].Foto != "") ? DadosComent.ListaResp[y].Foto :'static/pages/img/pessoa-icon.png');

				TxtHTML += '					<!-- col-1 -->';
				TxtHTML += '					<div class="col-1 text-center" style="margin: 0px; padding: 0px; padding-top: 10px;" >';
				TxtHTML += '						<img id="imgFotoPerfilComent'+DadosComent.ListaResp[y].Id+'" src="'+DirFotoRespComent+'" onerror="this.onerror=null;this.src=\'/static/pages/img/pessoa-icon.png\';"  alt="icone" width="60" height="60" class="img rounded-circle" alt="Foto Perfil" /> \n';
				TxtHTML += '					</div>';
				TxtHTML += '					<!-- col-1 -->';

				TxtHTML += '					<!-- col-11 -->';
				TxtHTML += '					<div class="col-11">';

				TxtHTML += '			<!-- DivDadosUserComentarioResp --> \n';
				TxtHTML += '			<div class="header" style="margin: 0px; padding: 0px; padding-top: 10px; padding-bottom: 10px;"> \n';              
				TxtHTML += '				<span class="font-weight-bold text-su ccess" style="font-size: 14px;">'+DadosComent.ListaResp[y].Nome+'</span>&nbsp;&nbsp;<small class="text-info" style="font-size: 11px;">( '+DadosComent.ListaResp[y].DtHr+' )</small> \n';         
				TxtHTML += '				<ul class="header-dropdown"> \n';
				TxtHTML += '					<li class="dropdown"> \n';
				TxtHTML += '						<a href="javascript:void(0);" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"> <i class="zmdi zmdi-more"></i> </a> \n';
				TxtHTML += '						<ul class="dropdown-menu dropdown-menu-right"> \n';
				if ( DadosComent.ListaResp[y].ExibeBtnDenu == "S" ) TxtHTML += '							<li><a href="javascript:void(0);" onclick="fMostrarModalDenunciar('+DadosComent.ListaResp[y].Id+');"                     > <i class="fa fa-warning"       aria-hidden="true"></i> &nbsp; Denunciar </a></li> \n';
				if ( DadosComent.ListaResp[y].ExibeBtnEdit == "S" ) TxtHTML += '							<li><a href="javascript:void(0);" onclick="fMostrarEditarResposta( '+DadosComent.ListaResp[y].Id+');"                    > <i class="fa fa-pencil fa-lg"  aria-hidden="true"></i> &nbsp; Editar    </a></li> \n';
				if ( DadosComent.ListaResp[y].ExibeBtnExcl == "S" ) TxtHTML += '							<li><a href="javascript:void(0);" onclick="fExcluirComentario(\''+urlPadrao +'\','+DadosComent.ListaResp[y].Id+',\'B\');"> <i class="fa fa-trash-o fa-lg" aria-hidden="true"></i> &nbsp; Excluir   </a></li> \n';
				TxtHTML += '						</ul> \n';
				TxtHTML += '					</li> \n';
				TxtHTML += '				</ul> \n';
				TxtHTML += '			</div> \n';
				TxtHTML += '			<!-- DivDadosUserComentarioResp --> \n';
				
				TxtHTML += '			<!-- DivBody -->';
				TxtHTML += '			<div class="body" style="margin: 0px; padding: 0px;"> \n';
				
				TxtHTML += '						<!-- DivTextoComentarioResp -->';
				TxtHTML += '						<div class="row clearfix" style="margin: 0px; padding: 0px;">';
				TxtHTML += '							<div class="col-sm-12 col-md-12 col-lg-12 col-xl-12" style="margin: 0px; padding: 0px; line-height: 1.3em; font-size: 10pt"> ';
				TxtHTML += '								<span id="DivTextoComentarioResp'+DadosComent.ListaResp[y].Id+'" class="text-muted" style="font-size: 14px;">'+DadosComent.ListaResp[y].Texto+'</span>';
				TxtHTML += '								<span id="DivEditarTextoComentarioResp'+DadosComent.ListaResp[y].Id+'" class="text-muted" style="display: none; font-size: 14px;">';
				TxtHTML += '									<textarea data-autoresize style="font-size:14px; resize:none; overflow:hidden; box-sizing:border-box;" class="form-control form-control-sm" id="TxtTextoComentarioResp'+DadosComent.ListaResp[y].Id+'" placeholder="Adicione uma Comentário...">'+ formatarTeste( DadosComent.ListaResp[y].Texto )+'</textarea>';
				TxtHTML += '									<br/>';
				TxtHTML += '									<div class="text-right">';
				TxtHTML += '										<a style="font-size:12px; width: 120px;" class="btn btn-sm btn-primary btn-round waves-effect" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fSalvarDadosResposta(\''+urlPadrao +'\','+DadosComent.Id+','+DadosComent.ListaResp[y].Id+');"> <i class="fa fa-paper-plane" aria-hidden="true"></i> &nbsp; SALVAR </a>';
				TxtHTML += '										&nbsp;';
				TxtHTML += '										<a style="font-size:12px; width: 120px;" class="btn btn-sm btn-light btn-simple btn-round waves-effect" href="javascript:void(0);" role="button" aria-pressed="true" onclick="fEsconderEditarResposta('+DadosComent.ListaResp[y].Id+');"> <i class="fa fa-paper-plane" aria-hidden="true"></i> &nbsp; CANCELAR </a>';
				TxtHTML += '									</div>';
				TxtHTML += '									<br/>';
				TxtHTML += '								</span>';
				TxtHTML += '							</div>';
				TxtHTML += '						</div>';
				TxtHTML += '						<!-- DivTextoComentarioResp -->';
				
				//TxtHTML += '						<br/>';

				TxtHTML += '						<!-- DivBotaoComentarioResp -->';
				TxtHTML += '						<div class="row clearfix" style="margin: 0px; padding: 0px;  padding-top: 10px;">';
				TxtHTML += '							<div class="col-12 text-left" style="margin: 0px; padding: 0px;">';		
				if ( DadosComent.ListaResp[y].MarcarGostei     == "S" ) TxtHTML += '								<a class="btn btn-sm btn-primary btn-simple btn-round waves-effect" href="javascript:void(0);" style="font-size: 10px; width: 80px; " role="button" aria-pressed="true" data-selc="'+DadosComent.ListaResp[y].MarcarGostei+'"    id="BtnGostei'+DadosComent.ListaResp[y].Id+'"    onclick="fSalvarDadosReacao(\''+urlPadrao +'\','+DadosComent.ListaResp[y].Id+',\'A\');"   > <i id="iGostei'+DadosComent.ListaResp[y].Id+'"    style="font-size: 15px;" class="fa fa-thumbs-up">   </i> &nbsp; <span style="font-size: 12px;" class="text-primary" id="QtdeGostei'+DadosComent.ListaResp[y].Id+'"   >'+DadosComent.ListaResp[y].QtdeGostei+'   </span> </a>';
				if ( DadosComent.ListaResp[y].MarcarGostei     == "N" ) TxtHTML += '								<a class="btn btn-sm btn-light btn-simple btn-round waves-effect" href="javascript:void(0);" style="font-size: 10px; width: 80px; " role="button" aria-pressed="true" data-selc="'+DadosComent.ListaResp[y].MarcarGostei+'"    id="BtnGostei'+DadosComent.ListaResp[y].Id+'"    onclick="fSalvarDadosReacao(\''+urlPadrao +'\','+DadosComent.ListaResp[y].Id+',\'A\');"   > <i id="iGostei'+DadosComent.ListaResp[y].Id+'"    style="font-size: 15px;" class="fa fa-thumbs-up">   </i> &nbsp; <span style="font-size: 12px;" class="text-muted"   id="QtdeGostei'+DadosComent.ListaResp[y].Id+'"   >'+DadosComent.ListaResp[y].QtdeGostei+'   </span> </a>';
				if ( DadosComent.ListaResp[y].MarcarNaoGostei  == "S" ) TxtHTML += '								<a class="btn btn-sm btn-primary btn-simple btn-round waves-effect" href="javascript:void(0);" style="font-size: 10px; width: 80px; " role="button" aria-pressed="true" data-selc="'+DadosComent.ListaResp[y].MarcarNaoGostei+'" id="BtnNaoGostei'+DadosComent.ListaResp[y].Id+'" onclick="fSalvarDadosReacao(\''+urlPadrao +'\','+DadosComent.ListaResp[y].Id+',\'B\');"> <i id="iNaoGostei'+DadosComent.ListaResp[y].Id+'" style="font-size: 15px;" class="fa fa-thumbs-down"> </i> &nbsp; <span style="font-size: 12px;" class="text-primary" id="QtdeNaoGostei'+DadosComent.ListaResp[y].Id+'">'+DadosComent.ListaResp[y].QtdeNaoGostei+'</span> </a>';
				if ( DadosComent.ListaResp[y].MarcarNaoGostei  == "N" ) TxtHTML += '								<a class="btn btn-sm btn-light btn-simple btn-round waves-effect" href="javascript:void(0);" style="font-size: 10px; width: 80px; " role="button" aria-pressed="true" data-selc="'+DadosComent.ListaResp[y].MarcarNaoGostei+'" id="BtnNaoGostei'+DadosComent.ListaResp[y].Id+'" onclick="fSalvarDadosReacao(\''+urlPadrao +'\','+DadosComent.ListaResp[y].Id+',\'B\');"> <i id="iNaoGostei'+DadosComent.ListaResp[y].Id+'" style="font-size: 15px;" class="fa fa-thumbs-down"> </i> &nbsp; <span style="font-size: 12px;" class="text-muted"   id="QtdeNaoGostei'+DadosComent.ListaResp[y].Id+'">'+DadosComent.ListaResp[y].QtdeNaoGostei+'</span> </a>';
				if ( DadosComent.ListaResp[y].ExibirDadosAdmin == "S" ) TxtHTML += '					            <a class="btn btn-sm btn-warning btn-round waves-effect" href="javascript:void(0);" style="font-size: 10px; width: 120px;" title="Visualizar" role="button" aria-pressed="true" id="BtnVisualizarComentarioResp'+DadosComent.ListaResp[y].Id+'" onclick="fVisualizarDadosAdmin(\''+urlPadrao +'\','+DadosComent.ListaResp[y].Id+');"> <i style="font-size: 15px;" class="fa fa-eye"> </i> &nbsp;VISUALIZAR</a>';
				TxtHTML += '							</div>';
				TxtHTML += '						</div>';
				TxtHTML += '						<!-- DivBotaoComentarioResp -->';

				TxtHTML += '			</div> \n';
				TxtHTML += '			<!-- DivBody -->';

				TxtHTML += '					</div>';
				TxtHTML += '					<!-- col-11 -->';
				TxtHTML += '				</div>';
				TxtHTML += '				<!-- DivComentResposta -->';
				//TxtHTML += '				<hr class="border-muted" style="margin-bottom: 10px;!important; margin-top: 10px;!important; "/>';
			}
			TxtHTML += '			</div>';
			TxtHTML += '			<!-- DivResposta -->';
		}

		TxtHTML += '			</div> \n';
		TxtHTML += '			<!-- DivBody -->';

		TxtHTML += '		</div>';
		TxtHTML += '		<!-- col-11 -->';

		TxtHTML += '	</div>';
		TxtHTML += '	<!-- row -->';

		TxtHTML += '</div>';
		TxtHTML += '<!-- DivComentario -->';

		return TxtHTML;
	
	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	} 
}

function fCarregarListaComentarios( urlPadrao ) {	
	try {

		var DivListaComentarios = $("#DivListaComentarios");
		DivListaComentarios.html("");	
		
		var BtnPaginacao = $("#BtnPaginacao");
		BtnPaginacao.empty(); // $("#BtnPaginacao").html('');
		
		$.urlParam = function(name){
			var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
			return results[1] || 0;
		}

		var PagAtual = 1;
		try {
			PagAtual = $.urlParam('PagAtual');
		} catch (e) {
			var PagAtual = 1;
		} 

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "comentarios/lista",
			data    : { PagAtual: PagAtual },
			success: function(result) {  

				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				var lista     = result.data.Lista; 
				var PagAtual  = parseInt( result.data.PagAtual ); 
				var PagTotal  = parseInt( result.data.PagTotal ); 

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

					if ( lista.length > 0 ){
						for (i = 0; i < lista.length; i++)
							DivListaComentarios.append( fMontarDivComentario(urlPadrao, lista[i] ) );
					}

					if ( PagTotal )
						if ( PagTotal > 1 ){
							if ( PagAtual > 1 )                   BtnPaginacao.append('<li class="page-item">                                      <a class="page-link text-muted"                               href="'+urlPadrao+'comentarios?PagAtual='+(PagAtual-1)+'"                 title="Página Anterior" aria-label="Anterior">  <span>Anterior</span> </a> </li>');
							for (Num = 1; Num <= PagTotal; Num++) BtnPaginacao.append('<li class="page-item '+( Num==PagAtual ? "active" : "")+'"> <a class="page-link '+( Num==PagAtual ? "" : "text-muted")+'" href="'+( Num==PagAtual ? 'javascript:void(0);' : urlPadrao+'comentarios?PagAtual='+Num)+'" title="Página '+Num+'" >'+Num+'</a></li>');
							if ( PagAtual < PagTotal )            BtnPaginacao.append('<li class="page-item">                                      <a class="page-link text-muted"                               href="'+urlPadrao+'comentarios?PagAtual='+(PagAtual+1)+'"                 title="Próxima Página" aria-label="Next"> <span>Próxima</span> </a> </li>');
						}

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
	
	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
	} 
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fSalvarDadosReacao( urlPadrao, IdComent, Tipo ){
	try {

		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "comentarios/salvarReacao",
			data    : { IdComent: IdComent, Tipo: Tipo },
			success: function(result) {  
				
				var resultado   = result.data.Resultado; 
				var mensagem    = result.data.Mensagem; 
				var DadosComent = result.data.Dados;
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {

					var DivQtdeGostei    = $("#QtdeGostei"+IdComent);
					var DivQtdeNaoGostei = $("#QtdeNaoGostei"+IdComent);

					if ( Tipo == "A") fMarcarGostei(    IdComent );
					if ( Tipo == "B") fMarcarNaoGostei( IdComent );

					if ( DadosComent.QtdeGostei    ) DivQtdeGostei.html(    DadosComent.QtdeGostei    );
					if ( DadosComent.QtdeNaoGostei ) DivQtdeNaoGostei.html( DadosComent.QtdeNaoGostei );

				} else {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				}
			},
			error: function(data) {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});
	
	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

function fMarcarGostei( IdComent ){
	try {

		fLimparAreaAlerta("AreaAlertaPrinc");

		var BtnGostei     = $("#BtnGostei"+IdComent);
		var iGostei       = $("#iGostei"+IdComent);
		var DivQtdeGostei = $("#QtdeGostei"+IdComent);
		var qtde          = parseInt( DivQtdeGostei.text() );
		if ( BtnGostei.data("selc") == "N" ) {
			BtnGostei.data('selc', "S");  
			if( qtde ) DivQtdeGostei.html( qtde + 1 )
			else       DivQtdeGostei.html(1);
			iGostei.removeClass("text-muted");
			iGostei.addClass("text-primary");
			DivQtdeGostei.removeClass("text-muted");
			DivQtdeGostei.addClass("text-primary");
		}else{
			BtnGostei.data('selc', "N"); 
			if( qtde ) DivQtdeGostei.html( qtde - 1 )
			else       DivQtdeGostei.html(0);
			iGostei.addClass("text-muted");
			iGostei.removeClass("text-primary");
			DivQtdeGostei.addClass("text-muted");
			DivQtdeGostei.removeClass("text-primary");
		}
		
		var BtnNaoGostei     = $("#BtnNaoGostei"+IdComent);
		var iNaoGostei       = $("#iNaoGostei"+IdComent);
		var DivQtdeNaoGostei = $("#QtdeNaoGostei"+IdComent);
		if ( BtnNaoGostei.data("selc") == "S" ) {
			var qtde = parseInt( DivQtdeNaoGostei.text() );
			if( qtde ) DivQtdeNaoGostei.html( qtde - 1 )
			else       DivQtdeNaoGostei.html(1);
		}else{
			var qtde = parseInt( DivQtdeNaoGostei.text() );
			DivQtdeNaoGostei.html( qtde );
		}
		BtnNaoGostei.data('selc', "N");
		iNaoGostei.removeClass("text-primary");
		iNaoGostei.addClass("text-muted");
		DivQtdeNaoGostei.removeClass("text-primary");
		DivQtdeNaoGostei.addClass("text-muted");

	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 	
}

function fMarcarNaoGostei( IdComent ){
	try {

		fLimparAreaAlerta("AreaAlertaPrinc");
		
		var BtnGostei     = $("#BtnGostei"+IdComent);
		var iGostei       = $("#iGostei"+IdComent);
		var DivQtdeGostei = $("#QtdeGostei"+IdComent);
		if ( BtnGostei.data("selc") == "S" ) {
			var qtde = parseInt( DivQtdeGostei.text() );
			if( qtde ) DivQtdeGostei.html( qtde - 1 )
			else       DivQtdeGostei.html(1);
		}else{
			var qtde = parseInt( DivQtdeGostei.text() );
			DivQtdeGostei.html( qtde );
		}
		BtnGostei.data('selc', "N");  
		iGostei.addClass("text-muted");
		iGostei.removeClass("text-primary");
		DivQtdeGostei.addClass("text-muted");
		DivQtdeGostei.removeClass("text-primary");
		
		var BtnNaoGostei     = $("#BtnNaoGostei"+IdComent);
		var iNaoGostei       = $("#iNaoGostei"+IdComent);
		var DivQtdeNaoGostei = $("#QtdeNaoGostei"+IdComent);
		var qtde = parseInt( DivQtdeNaoGostei.text() );
		if ( BtnNaoGostei.data("selc") == "N" ) {
			if( qtde ) DivQtdeNaoGostei.html( qtde + 1 )
			else       DivQtdeNaoGostei.html(1);
			BtnNaoGostei.data('selc', "S");
			iNaoGostei.addClass("text-primary");
			iNaoGostei.removeClass("text-muted");
			DivQtdeNaoGostei.addClass("text-primary");
			DivQtdeNaoGostei.removeClass("text-muted");
		}else{
			BtnNaoGostei.data('selc', "N");
			if( qtde ) DivQtdeNaoGostei.html( qtde - 1 )
			else       DivQtdeNaoGostei.html(0);
			iNaoGostei.removeClass("text-primary");
			iNaoGostei.addClass("text-muted");
			DivQtdeNaoGostei.removeClass("text-primary");
			DivQtdeNaoGostei.addClass("text-muted");
		}

	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 	
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fMostrarNovoComentario(){

	var DivNovoComentario = $("#DivNovoComentario");
	var TxtTextoComentario = $("#TxtTextoComentario");
	TxtTextoComentario.val("");
	DivNovoComentario.toggle();

	jQuery.each(jQuery('textarea[data-autoresize]'), function() {
		var offset = this.offsetHeight - this.clientHeight;
		var resizeTextarea = function(el) {
			jQuery(el).css('height', 'auto').css('height', el.scrollHeight + offset);
		   
		};
		jQuery(this).on('keyup input', function() { resizeTextarea(this); }).removeAttr('data-autoresize');
	});

   TxtTextoComentario.focus(); 

}

function fEsconderNovoComentario(){
	var DivNovoComentario = $("#DivNovoComentario");
	DivNovoComentario.hide(); //DivNovoComentario.toggle();
}

function fMostrarEditarComentario( IdComent ){

	var DivTextoComentario        = $("#DivTextoComentario"+IdComent);
	var DivEditartTextoComentario = $("#DivEditartTextoComentario"+IdComent);
	var TxtTextoComentario        = $("#TxtTextoComentario"+IdComent);
	DivTextoComentario.toggle();
	DivEditartTextoComentario.toggle();

	TxtTextoComentario.focus(function(){
		var alturaScroll = this.scrollHeight;
		var alturaCaixa = $(this).height();
		if (alturaScroll > (alturaCaixa + 10)) {
			//if (alturaScroll > 5000) return;
			$(this).css('height', alturaScroll);
		}
	});

	jQuery.each(jQuery('textarea[data-autoresize]'), function() {
		var offset = this.offsetHeight - this.clientHeight;
		var resizeTextarea = function(el) {
			jQuery(el).css('height', 'auto').css('height', el.scrollHeight + offset);		   
		};
		jQuery(this).on('keyup input', function() { resizeTextarea(this); }).removeAttr('data-autoresize');
	});

	val = TxtTextoComentario.val();
	TxtTextoComentario.focus().val("").val(val);

}

function fEsconderEditarComentario( IdComent ){
	var DivTextoComentario        = $("#DivTextoComentario"+IdComent);
	var DivEditartTextoComentario = $("#DivEditartTextoComentario"+IdComent);
	DivTextoComentario.toggle();
	DivEditartTextoComentario.toggle();
}

function iniciarAnimacaoSalvarComent() {
    $("#iSalvarNovoComentario").removeClass("fa-check-square-o");
    $("#iSalvarNovoComentario").addClass("fa-spinner");
    $("#iSalvarNovoComentario").addClass("fa-pulse");
}

function finalizarAnimacaoSalvarComent() {
   $("#iSalvarNovoComentario").removeClass("fa-spinner");
   $("#iSalvarNovoComentario").removeClass("fa-pulse");
   $("#iSalvarNovoComentario").addClass("fa-check-square-o");
}

function fSalvarDadosComentario( urlPadrao, Id ){
	try {
		
		fLimparAreaAlerta("AreaAlertaPrinc");
		finalizarAnimacaoSalvarComent();

		var Texto = "";
		
		if ( typeof($("#TxtTextoComentario")) !== "undefined") 
			Texto = $("#TxtTextoComentario").val();

		if( Texto == "" &&  typeof($("#TxtTextoComentario"+Id)) !== "undefined" ) 
			Texto = $("#TxtTextoComentario"+Id).val();

		if( Texto == "" ){
			fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, "Por favor, informe o Comentário");
			return false;
		}		

		iniciarAnimacaoSalvarComent();
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "comentarios/salvarComentario",
			data    : { Id: Id, Texto: Texto },
			success: function(result) {  
			
				finalizarAnimacaoSalvarComent();
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					fEsconderNovoComentario();
					// fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					fCarregarListaComentarios( urlPadrao );
				} else {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				}
			},
			error: function(data) {
				finalizarAnimacaoSalvarComent();
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});
	
	} catch (e) {
		finalizarAnimacaoSalvarComent();
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fMostrarNovaResposta( IdComent ){
	var DivResponder     = $("#DivResponder"+IdComent);
	var TxtIdResposta    = null; //$("#TxtIdResposta"+IdComent).val().trim();
	var TxtTextoResposta = $("#TxtTextoResposta"+IdComent);
	//TxtIdResposta.val("");
	TxtTextoResposta.val("");
	DivResponder.toggle();

	jQuery.each(jQuery('textarea[data-autoresize]'), function() {
		var offset = this.offsetHeight - this.clientHeight;
		var resizeTextarea = function(el) {
			jQuery(el).css('height', 'auto').css('height', el.scrollHeight + offset);
		   
		};
		jQuery(this).on('keyup input', function() { resizeTextarea(this); }).removeAttr('data-autoresize');
	});	
	
	TxtTextoResposta.focus();

}

function fMostrarEditarResposta( IdComent ){
	var DivTextoComentarioResp       = $("#DivTextoComentarioResp"+IdComent);
	var DivEditarTextoComentarioResp = $("#DivEditarTextoComentarioResp"+IdComent);
	var TxtTextoComentarioResp       = $("#TxtTextoComentarioResp"+IdComent);
	DivTextoComentarioResp.toggle();
	DivEditarTextoComentarioResp.toggle();


	TxtTextoComentarioResp.focus(function(){
		var alturaScroll = this.scrollHeight;
		var alturaCaixa = $(this).height();
		if (alturaScroll > (alturaCaixa + 10)) {
			//if (alturaScroll > 5000) return;
			$(this).css('height', alturaScroll);
		}
	});

	jQuery.each(jQuery('textarea[data-autoresize]'), function() {
		var offset = this.offsetHeight - this.clientHeight;
		var resizeTextarea = function(el) {
			jQuery(el).css('height', 'auto').css('height', el.scrollHeight + offset);		   
		};
		jQuery(this).on('keyup input', function() { resizeTextarea(this); }).removeAttr('data-autoresize');
	});

	val = TxtTextoComentarioResp.val();
	TxtTextoComentarioResp.focus().val("").val(val);

}

function fEsconderEditarResposta( IdComent ){
	var DivTextoComentarioResp       = $("#DivTextoComentarioResp"+IdComent);
	var DivEditarTextoComentarioResp = $("#DivEditarTextoComentarioResp"+IdComent);
	DivTextoComentarioResp.toggle();
	DivEditarTextoComentarioResp.toggle();
}

function fSalvarDadosResposta( urlPadrao, IdComent, Id ){
	try {
		
		fLimparAreaAlerta("AreaAlertaPrinc");

		var Texto = ""; 
		
		if ( typeof($("#TxtTextoResposta"+IdComent)) !== "undefined") 
			Texto = $("#TxtTextoResposta"+IdComent).val(); 

		if( Texto == "" &&  typeof($("#TxtTextoComentarioResp"+Id)) !== "undefined" ) 
			Texto = $("#TxtTextoComentarioResp"+Id).val();

		if( Texto == "" ){
			fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, "Por favor, informe a Resposta do Comentário ");
			return false;
		}		
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "comentarios/salvarResposta",
			data    : { IdComent: IdComent, Id: Id, Texto: Texto },
			success: function(result) {  
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					// fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					fCarregarListaComentarios( urlPadrao );
				} else {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				}
			},
			error: function(data) {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});
	
	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fExcluirComentario( urlPadrao, IdComent, Tipo ){
	try {
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "comentarios/excluir",
			data    : { IdComent: IdComent, Tipo: Tipo },
			success: function(result) {  
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					// fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					fCarregarListaComentarios( urlPadrao );
				} else {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				}
			},
			error: function(data) {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});
	
	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fMostrarModalDenunciar( IdComent ){
	$("#TxtIdComentarioDenuncia").val( IdComent );
	$('#TxtTpDenuncia1').attr({"checked":false}).prop({"checked":false});
	$('#TxtTpDenuncia2').attr({"checked":false}).prop({"checked":false});
	$('#TxtTpDenuncia3').attr({"checked":false}).prop({"checked":false});
	$('#TxtTpDenuncia4').attr({"checked":false}).prop({"checked":false});
	$('#TxtTpDenuncia5').attr({"checked":false}).prop({"checked":false});
	$('#TxtTpDenuncia6').attr({"checked":false}).prop({"checked":false});
	$('#TxtTpDenuncia7').attr({"checked":false}).prop({"checked":false});
	//$('input[name=TxtTpDenuncia1]').attr({"checked":false}).prop({"checked":false});
	$('#PopModalDenuncia').modal({backdrop: 'static'});
}

function fDenunciarComentario( urlPadrao ){
	try {
		
		var IdComent = $("#TxtIdComentarioDenuncia").val().trim();
		if( IdComent == "" ){
			fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, "Por favor, informe o Id. Comentário ");
			return false;
		}	
	
		var TxtTipo = $('input[name=TxtTpDenuncia1]:checked').val();
		if( TxtTipo == undefined || TxtTipo == "" ){
			fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, "Por favor, informe o Tipo da Denúncia ");
			return false;
		}	
		
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "comentarios/denunciar",
			data    : { IdComent: IdComent, Tipo: TxtTipo },
			success: function(result) {  
				
				var resultado = result.data.Resultado; 
				var mensagem  = result.data.Mensagem; 
				
				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					// fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					$("#PopModalDenuncia").modal("hide");
					fCarregarListaComentarios( urlPadrao );
				} else {
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				}
			},
			error: function(data) {
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
				return;
			}
		});
	
	} catch (e) {
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); 
		return;
	} 
}

//------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------

function fVisualizarDadosAdmin( urlPadrao, IdComent ){
	try {

		//$("#PopModalVisualizou").modal("hide");

		$("#DivComentarioVisualizou").html("");

		if( IdComent == "" ){
			fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, "Por favor, informe o Id. Comentário ");
			return false;
		}	
	
		$.ajax({
			cache   : "false",
			dataType: "json",
			async   : true,
			type    : "POST",
			url     : urlPadrao + "comentarios/visualizar",
			data    : { IdComent: IdComent },
			success: function(result) {  
				
				var resultado   = result.data.Resultado; 
				var mensagem    = result.data.Mensagem; 
				var DadosComent = result.data.Dados;

				if (resultado == "NSESSAO") {
					$(location).attr('href', urlPadrao + '/login');
					return false;
				} else if (resultado == "NOK") {
					$("#PopModalVisualizou").modal("hide");
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_AVISO, mensagem); 
					return;
				} else if (resultado == "FALHA") {
					$("#PopModalVisualizou").modal("hide");
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				} else if (resultado == "OK") {
					// fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_SUCESSO, 'Dados salvo com sucesso!');
					
					var content = "";
					
					if ( DadosComent.ListaGostei != "" ){
						content += "<h6 class='text-dark font-weight-bold'>Lista de Gostei:</h6>";
						content += "<span class='text-muted' style='font-size: 12px;''>"+DadosComent.ListaGostei+"</span>";
						content += '<br><br>';
					}

					if ( DadosComent.ListaNaoGostei != "" ){
						content += "<h6 class='text-dark font-weight-bold'>Lista de Não Gostei:</h6>";
						content += "<span class='text-muted' style='font-size: 12px;''>"+DadosComent.ListaNaoGostei+"</span>";
						content += '<br><br>';
					}

					if ( DadosComent.ListaVisualizou != "" ){
						content += "<h6 class='text-dark font-weight-bold'>Lista de Visualização:</h6>";
						content += "<span class='text-muted' style='font-size: 12px;''>"+DadosComent.ListaVisualizou+"</span>";
						content += '<br><br>';
					}
					
					$("#DivComentarioVisualizou").html(content);
					$("#PopModalVisualizou").modal({backdrop: "static"});
					return;

				} else {
					$("#PopModalVisualizou").modal("hide");
					fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, mensagem); 
					return;
				}
			},
			error: function (request, status, error) { // error: function(data) {  // error: function (request, status, error) {
				$("#PopModalVisualizou").modal("hide");
				fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); // request.responseText //MSG_ALERTA_ERRO
				return;
			}
		});
		
	} catch (e) {
		$("#PopModalVisualizou").modal("hide");
		fCriarAlerta("AreaAlertaPrinc", TP_ALERTA_ERRO, MSG_ALERTA_ERRO); // MSG_ALERTA_ERRO // e.message
		return;
	} 
}
