

var FMT_TEXTO=1,
    FMT_DATA=2,
    FMT_HORA=3,
    FMT_DATAHORA=4, 
    FMT_ANOMES=5,
    FMT_INTEIRO=6,
    FMT_DECIMAL=7,
    FMT_CPF=8,
    FMT_CNPJ=9,
    FMT_CNPJCPF=10,
    FMT_CNPJCPFBASE=11;
    FMT_FONECOMERCIAL=11;
    FMT_FONERESIDENCIAL=12;
    FMT_FONECELULAR=13;
    FMT_FONETODOS=14;
    
//////////////////////////////////////////////

function formataCampo(campoInput, formato){
  if ( ( (formato==FMT_CNPJCPF) || (formato==FMT_CPF) || (formato==FMT_CNPJ) ) && (campoInput.value.length > 0) ) {

    if ( ((campoInput.value.length <= 11) && (formato==FMT_CNPJCPF)) || (formato==FMT_CPF) ) {
      //CPF
      campoInput.value = PreencheCharEsquerda(campoInput.value, 11, '0');
      campoInput.value = campoInput.value.substr(0,3)+'.'+campoInput.value.substr(3,3)+'.'+campoInput.value.substr(6,3) +'-'+campoInput.value.substr(9,2);
    }
    else { 
      if ( ( (campoInput.value.length > 11) && (formato==FMT_CNPJCPF) ) || (formato==FMT_CNPJ) ) {
        campoInput.value = PreencheCharEsquerda(campoInput.value, 14, '0');
        campoInput.value = campoInput.value.substr(0,2)+'.'+campoInput.value.substr(2,3)+'.'+campoInput.value.substr(5,3) +'/'+campoInput.value.substr(8,4)+'-'+campoInput.value.substr(12,2);
      };
    };
  }
  else{
    campoInput.value = campoInput.value;
  };

  return;
};

function formataCampoNew(campoInput, formato)
{
  campoInput.value = removeCharNaoNumero(campoInput.value);
  if ( ( (formato==FMT_CNPJCPF) || (formato==FMT_CPF) || (formato==FMT_CNPJ) || (formato==FMT_CNPJCPFBASE) ) && (campoInput.value.length > 0) ) 
  {

    if ( ((campoInput.value.length <= 8) && (formato==FMT_CNPJCPFBASE)) ) 
    {
      //CNPJBASE
      campoInput.value = PreencheCharEsquerda(campoInput.value, 8, '0');
      //campoInput.value = campoInput.value.substr(0,2)+'.'+campoInput.value.substr(3,3)+'.'+campoInput.value.substr(6,3);
    } 
    else 
    { 
        if ( (campoInput.value.length <= 11) && ( ( formato==FMT_CNPJCPF) || (formato==FMT_CPF) || (formato==FMT_CNPJCPFBASE) ) )  
        {
          //CPF
          campoInput.value = PreencheCharEsquerda(campoInput.value, 11, '0');
          campoInput.value = campoInput.value.substr(0,3)+'.'+campoInput.value.substr(3,3)+'.'+campoInput.value.substr(6,3) +'-'+campoInput.value.substr(9,2);
        } 
        else 
        {
            if ( (campoInput.value.length <= 11) && ((formato==FMT_CNPJCPF) || (formato==FMT_CPF) || (formato==FMT_CNPJCPFBASE) ) ) 
            {
              //CPF
              campoInput.value = PreencheCharEsquerda(campoInput.value, 11, '0');
              campoInput.value = campoInput.value.substr(0,3)+'.'+campoInput.value.substr(3,3)+'.'+campoInput.value.substr(6,3) +'-'+campoInput.value.substr(9,2);
            }
            else 
            { 
              if ( (campoInput.value.length > 11) && ((formato==FMT_CNPJCPF) || (formato==FMT_CNPJ) || (formato==FMT_CNPJCPFBASE) ) ) 
              {
                campoInput.value = PreencheCharEsquerda(campoInput.value, 14, '0');
                campoInput.value = campoInput.value.substr(0,2)+'.'+campoInput.value.substr(2,3)+'.'+campoInput.value.substr(5,3) +'/'+campoInput.value.substr(8,4)+'-'+campoInput.value.substr(12,2);
              };
              
            };
        };
    };

    
  }
  else
  {
    campoInput.value = campoInput.value;
  };

  return;
};
//////////////////////////////////////////////
function desformataCampo(campoInput, formato){
  if((formato==FMT_CNPJCPF)||(formato==FMT_CNPJCPFBASE)||(formato==FMT_CPF)||(formato==FMT_CNPJ)||
     (formato==FMT_FONECOMERCIAL)||(formato==FMT_FONERESIDENCIAL)||(formato==FMT_FONECELULAR)){
    campoInput.value = removeSpcChars(campoInput.value);
    campoInput.value = removeLetra(campoInput.value, '.');
    campoInput.value = removeLetra(campoInput.value, '/');
    campoInput.value = removeLetra(campoInput.value, '-');  
    campoInput.value = removeLetra(campoInput.value, '('); 
    campoInput.value = removeLetra(campoInput.value, ')');  
    campoInput.value = removePrimeiraLetra(campoInput.value, '0');
  }
  else{
    if ((formato==FMT_INTEIRO)||(formato==FMT_DECIMAL))
    {
      campoInput.value = removePrimeiraLetra(campoInput.value, '0');
    };
    if (formato==FMT_HORA){
         campoInput.value = removeSpcChars(campoInput.value);
         campoInput.value = removeLetra(campoInput.value, ':');
    };
  };

  campoInput.select();
  return;
};
//////////////////////////////////////////////
function validaKey(campoInput, formato, CasasDecimais, Ocorrencia) {
  var nArg=validaKey.arguments.length,
    c = String(campoInput.value.charAt(campoInput.value.length -1));

  if ( (formato==FMT_CNPJCPF)||(formato==FMT_CNPJCPFBASE)||(formato==FMT_CNPJ)||(formato==FMT_CPF)||
       (formato==FMT_INTEIRO)||(formato==FMT_DECIMAL)||(formato==FMT_DATA)||
       (formato==FMT_HORA)||(formato==FMT_DATAHORA))
  {
    campoInput.value = removeCharNaoNumero(campoInput.value);
  };

  if (formato==FMT_INTEIRO)
  {
    campoInput.value = removePrimeiraLetra(campoInput.value, '0');
  };

  if (nArg>=3&&formato==FMT_DECIMAL &&(CasasDecimais>0)) {
    campoInput.value = removeLetra(campoInput.value, ',');
    campoInput.value = removeLetra(campoInput.value, '.');
    campoInput.value = removePrimeiraLetra(campoInput.value, '0');

    if ((campoInput.value == '') && (c == '0'))
    {
       campoInput.value = '000';
     };
     
    if (campoInput.value.length < (CasasDecimais +1)) {
      if (((nArg>=4)&&(Ocorrencia!='?'))||(campoInput.value!='')) {
        campoInput.value = PreencheCharEsquerda(campoInput.value, (CasasDecimais +1), '0');
      }
    };

    if (campoInput.value != '')
    {
      partInteira = campoInput.value.substr(0, (campoInput.value.length - CasasDecimais));
      partInteiraFmt = ""
      
     qtdNum = 0;         
     for( var i=partInteira.length;i>=0;i--){
         c=partInteira.charAt(i);
         if (qtdNum > 3) {
            partInteiraFmt = c + '.' + partInteiraFmt;
            qtdNum = 1;
         } else {
            partInteiraFmt = c + partInteiraFmt;
         };
         qtdNum = qtdNum + 1;
     };
     
      campoInput.value = partInteiraFmt +','+ campoInput.value.substr((campoInput.value.length - CasasDecimais), CasasDecimais);
    };
  };

  if ((formato==FMT_DATA)||(formato==FMT_DATAHORA)) {
    campoInput.value = removeLetra(campoInput.value, '/');
    campoInput.value = removeLetra(campoInput.value, ' ');
    campoInput.value = removeLetra(campoInput.value, ':');

    if (campoInput.value.length > 2)
    {
      campoInput.value = campoInput.value.substr(0, 2)+'/'+campoInput.value.substr(2,campoInput.value.length-2);
    };

    if (campoInput.value.length > 5)
    {
      campoInput.value = campoInput.value.substr(0, 5)+'/'+campoInput.value.substr(5,campoInput.value.length-5);
    };

    if (campoInput.value.length > 10)
    {
      campoInput.value = campoInput.value.substr(0, 10)+' '+campoInput.value.substr(10,campoInput.value.length-10);
    };

    if (campoInput.value.length > 13)
    {
      campoInput.value = campoInput.value.substr(0, 13)+':'+campoInput.value.substr(13,campoInput.value.length-13);
    };

    if (campoInput.value.length > 16)
    {
      campoInput.value = campoInput.value.substr(0, 16)+':'+campoInput.value.substr(16,campoInput.value.length-16);
    };
  };

  if (formato==FMT_HORA) {
    campoInput.value = removeLetra(campoInput.value, ' ');
    campoInput.value = removeLetra(campoInput.value, ':');

    if (campoInput.value.length > 2)
    {
      campoInput.value = campoInput.value.substr(0, 2)+':'+campoInput.value.substr(2,campoInput.value.length-2);
    };

    if (campoInput.value.length > 5)
    {
      campoInput.value = campoInput.value.substr(0, 5)+':'+campoInput.value.substr(5,campoInput.value.length-5);
    };
  };

  if (formato==FMT_ANOMES) {
    campoInput.value = removeLetra(campoInput.value, '/');

    if (campoInput.value.length > 2)
    {
      campoInput.value = campoInput.value.substr(0, 2)+'/'+campoInput.value.substr(2,campoInput.value.length-2);
    };
  };
};
//////////////////////////////////////////////
function removeCharNaoNumero(Texto){
  var ret = "",
      s = String(Texto),
      c = "";
  
  for( var i=0;i<s.length;i++){
      c=s.charAt(i);
    if ((c>='0') && (c<='9')) {
      ret += c;
    }
  };

  return ret;
};
//////////////////////////////////////////////
function removeSpcChars(Texto,type){
var nArg=removeSpcChars.arguments.length,
  ret="",
  re=/197|198|208|215|216|222|223|229|230|240|247|248/,
  c=0,
  s=String(Texto);
  for(var i=0;i<s.length;i++){
      c=s.charCodeAt(i);
      if( (c>31&&c<253&&
        ( c<127||c>191)&&
          !re.test(c) ) ||
      (nArg==2&&type=="textarea"&& (c==9||c==13||c==10)))
      ret+=s.charAt(i);
  }
return ret;
};
//////////////////////////////////////////////
function removePrimeiraLetra(Texto,Letra){
  var ret="",
      c="",
      bResto=false,
      s=String(Texto);
  for(var i=0;i<s.length;i++){
    c=s.charAt(i);
    if ( c != Letra )
    {
      bResto = true;
    }

    if (bResto)
    {
      ret += c;
    }
  }

  return ret;
};
//////////////////////////////////////////////
function removeLetra(Texto,Letra){
var ret="",
  c="",
  s=String(Texto);
  for(var i=0;i<s.length;i++){
      c=s.charAt(i);
      if( c != Letra)
      ret+=s.charAt(i);
  }
  return ret;
};
//////////////////////////////////////////////
function PreencheCharDireita(Texto, Tamanho, Letra){
  var ret="",
      s=String(Texto),
      l=String(Letra);

  ret = s;
  while (ret.length < Tamanho)
  {
    ret+=Letra;
  };
  
  ret = ret.substr(0,Tamanho);

  return ret;
};
//////////////////////////////////////////////
function PreencheCharEsquerda(Texto, Tamanho, Letra){
  var ret="",
      s=String(Texto),
      l=String(Letra);

  ret = s;
  while (ret.length < Tamanho) {
    ret=Letra+ret;
  };
  
  ret = ret.substr(0,Tamanho);

  return ret;
};
//////////////////////////////////////////////
function StrofChar(Letra, Quantidade) {
var ret="";

  for(var i=0;i<Quantidade;i++){
    ret+=Letra;
  };

  return ret;
};
//////////////////////////////////////////////
function CasasDecimais(Valor, Digitos) {
  var sNumero="",
      fNumero=Valor,
      iVlrArred = Math.pow(10, Digitos);
      c="",
      posic=-1,
      sValor='';

  fNumero = fNumero * iVlrArred;
  fNumero = Math.round(fNumero);
  fNumero = fNumero / iVlrArred;
  sNumero = String(fNumero);

  for(var i=0;i<sNumero.length;i++){
      c=sNumero.charAt(i);
      if(c == '.' || c == ',') {
      posic=i;
      break;
    };
  };
  
  if (posic==-1) {
    sValor = sNumero + '.' + StrofChar('0', Digitos);
  }
  else {
    posic += 1;
    posic += Digitos;
    sNumero += StrofChar('0', Digitos);
    sValor = sNumero.substr(0, posic);
  };

  return sValor;
};
//////////////////////////////////////////////
function TruncDecimais(Valor, Digitos) {
  var sNumero="",
      fNumero=Valor,
      iVlrArred = Math.pow(10, Digitos);
      c="",
      posic=-1,
      sValor='';

  fNumero = fNumero * iVlrArred;
  fNumero = parseInt(fNumero);
  fNumero = fNumero / iVlrArred;
  sNumero = String(fNumero);

  for(var i=0;i<sNumero.length;i++){
      c=sNumero.charAt(i);
      if(c == '.' || c == ',') {
      posic=i;
      break;
    };
  };
  
  if (posic==-1) {
    sValor = sNumero + '.' + StrofChar('0', Digitos);
  }
  else {
    posic += 1;
    posic += Digitos;
    sNumero += StrofChar('0', Digitos);
    sValor = sNumero.substr(0, posic);
  };

  return sValor;
};
//////////////////////////////////////////////
function ObjMultiplica(Fator1, Fator2, Produto, Digitos) {
  var nFator1 =  0.0,
      nFator2 =  0.0,
      nProduto = 0.0;

  nFator1 = Fator1.value;
  nFator2 = Fator2.value;
  nProduto = nFator1 * nFator2;

  Produto.value = CasasDecimais(nProduto, Digitos);

  return;
};


//////////////////////////////////////////////
function ValidarCPFCNPJ(campoInput)
{

    desformataCampo(campoInput, FMT_CNPJCPF);
    
  if (campoInput.value.length > 11)  
    {   
    formataCampo(campoInput, FMT_CNPJCPF);
        return ValidarCNPJ(campoInput, FMT_CNPJ);//CNPJ 
        }
    else 
    {           
    formataCampo(campoInput, FMT_CNPJCPF);
        return ValidarCPF(campoInput, FMT_CPF);//CPF    
    }
    

}
//////////////////////////////////////////////
function ValidarCPF(campoInput, formato)
{

    var cpf = campoInput.value;
    cpf = cpf.replace(/[^\d]+/g,'');

    if(cpf == '') return false;

    // Elimina CPFs invalidos conhecidos
    if (cpf.length != 11)
        return false;
    
    // Valida 1o digito
    add = 0;
    for (i=0; i < 9; i ++)
        add += parseInt(cpf.charAt(i)) * (10 - i);
    rev = 11 - (add % 11);
    if (rev == 10 || rev == 11)
        rev = 0;
    if (rev != parseInt(cpf.charAt(9)))
        return false;
    
    // Valida 2o digito
    add = 0;
    for (i = 0; i < 10; i ++)
        add += parseInt(cpf.charAt(i)) * (11 - i);
    rev = 11 - (add % 11);
    if (rev == 10 || rev == 11)
        rev = 0;
    if (rev != parseInt(cpf.charAt(10)))
        return false;
        
    return true;            
}
//////////////////////////////////////////////
function ValidarCNPJ(campoInput, formato)
{
    var cnpj = removeCharNaoNumero(campoInput.value);
    cnpj = tirarFormacataoCPFCNPJ(cnpj);
    cnpj = PreencheCharEsquerda(cnpj, 14, '0');
    var valida = new Array(6,5,4,3,2,9,8,7,6,5,4,3,2);
    var dig1= new Number;
    var dig2= new Number;
    
    if (cnpj.length > 0)
    {
        exp = /\.|\-|\//g
        cnpj = cnpj.toString().replace( exp, "" ); 
        var digito = new Number(eval(cnpj.charAt(12)+cnpj.charAt(13)));
            
        for(i = 0; i<valida.length; i++)
        {
            dig1 += (i>0? (cnpj.charAt(i-1)*valida[i]):0);  
            dig2 += cnpj.charAt(i)*valida[i];   
        }
        dig1 = (((dig1%11)<2)? 0:(11-(dig1%11)));
        dig2 = (((dig2%11)<2)? 0:(11-(dig2%11)));
        
        if(((dig1*10)+dig2) != digito)
        {   
            //alert('CNPJ Invalido!');      
            //campoInput.focus();
            return false;
        }               
        else
        {
         formataCampo(campoInput, formato)
        }
    }
}
//////////////////////////////////////////////

function ValidarCPFCNPJRadio(Radio, campoInput, formato)
{
   var chkTpPessoa = Radio;
   
   if (chkTpPessoa[0].checked)
   {
        ValidarCPF(campoInput, formato);//CPF
        return 0;
   }
   if (chkTpPessoa[1].checked)
   {
        ValidarCNPJ(campoInput, formato);//CPF
        return 0;
   }
   if (chkTpPessoa[2].checked)
   {
        campoInput.value = PreencheCharEsquerda(campoInput.value, 8, '0'); //CNPJBase
        campoInput.value = campoInput.value.substr(0,2)+'.'+campoInput.value.substr(2,3)+'.'+campoInput.value.substr(5,3);
        return 0;
   }   
}
//////////////////////////////////////////////
function FormataTelefone(campoInput, formato)
{
  campoInput.value = removeCharNaoNumero(campoInput.value);
  if (campoInput.value.length > 0)
  {
        
     if ((formato==FMT_FONECOMERCIAL) || (formato==FMT_FONERESIDENCIAL))
       campoInput.value = '(' + campoInput.value.substr(0,2) + ')' + campoInput.value.substr(2,4) + '-' + campoInput.value.substr(6,4)
       else
        if (campoInput.value.length == 10)
          campoInput.value = '(' + campoInput.value.substr(0,2) + ')' + campoInput.value.substr(2,4) + '-' + campoInput.value.substr(6,4)
          else
           if (campoInput.value.length >= 11)
           { 
              campoInput.value = '(' + campoInput.value.substr(0,2) + ')' + campoInput.value.substr(2,5) + '-' + campoInput.value.substr(7,4);
           }
  }
}

function ValidaTelefone(campoInput){
    if ((removeCharNaoNumero(campoInput.value).length < 10) || (removeCharNaoNumero(campoInput.value).length > 11) )
      return false;
    else
      return true;
}
//////////////////////////////////////////////
function FormataCEP(campoInput)
{
  if (campoInput.value.length > 0)
  {   
    if (campoInput.value.length == 8)
    {
       campoInput.value = campoInput.value.substr(0,5) + '-' + campoInput.value.substr(5,4);
    }
    else
    {
        //alert("Favor inserir um CEP válido!");
        //campoInput.value = '';
        campoInput.focus();
        return false;
    }
    
  }
  
}
//////////////////////////////////////////////
function ValidaEmail(campoInput)
{ 
    
    if (campoInput.value.length > 0)
    {
        var x= campoInput.value;
        var atpos=x.indexOf("@");
        var dotpos=x.lastIndexOf(".");
        if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length)
            return false;
        else
            return true;
    }
} 

//////////////////////////////////////////////
function VerificaTamanhoMin(campoInput, tamMin, NomeCampo)
{
    if (campoInput.value.length > 0)
    {
        if (campoInput.value.length < tamMin)
        {
          return false;
        }
        else
          return true;
    }
}
/////////////////////////////////////////////
function EhDataValida(Data)
{
    var patternValidaData = /^(((0[1-9]|[12][0-9]|3[01])([-.\/])(0[13578]|10|12)([-.\/])(\d{4}))|(([0][1-9]|[12][0-9]|30)([-.\/])(0[469]|11)([-.\/])(\d{4}))|((0[1-9]|1[0-9]|2[0-8])([-.\/])(02)([-.\/])(\d{4}))|((29)(\.|-|\/)(02)([-.\/])([02468][048]00))|((29)([-.\/])(02)([-.\/])([13579][26]00))|((29)([-.\/])(02)([-.\/])([0-9][0-9][0][48]))|((29)([-.\/])(02)([-.\/])([0-9][0-9][2468][048]))|((29)([-.\/])(02)([-.\/])([0-9][0-9][13579][26])))$/;  
    
    if (!patternValidaData.test(Data))
        return false;
    else
        return true;
}
///////////////////////////////////////////
function ConfigMaskCPFCNPJ(campoInput, campoCPFCNPJ)
{
    campoCPFCNPJ.value = '';

    if (campoInput.selectedIndex != 0)
    {
        if (campoInput.selectedIndex == 1)
        {
            jQuery(function($){
                   $(campoCPFCNPJ).mask("9?99.999.999-99");
            });         
            
        }
        else
        if (campoInput.selectedIndex == 2)
        {
            jQuery(function($){
                   $(campoCPFCNPJ).mask("9?9.999.999/9999-99");
            }); 
        }
        else
        if (campoInput.selectedIndex == 3)
        {
            jQuery(function($){
                   $(campoCPFCNPJ).mask("9?9.999.999");
            }); 
        }
    }
}

function onLoadConfigMaskCPFCNPJ(campoInput, campoCPFCNPJ)
{
    if (campoInput.selectedIndex != 0)
    {
        if (campoInput.selectedIndex == 1)
        {
            jQuery(function($){
                   $(campoCPFCNPJ).mask("9?99.999.999-99");
            });         
            
        }
        else
        if (campoInput.selectedIndex == 2)
        {
            jQuery(function($){
                   $(campoCPFCNPJ).mask("9?9.999.999/9999-99");
            }); 
        }
        else
        if (campoInput.selectedIndex == 3)
        {
            jQuery(function($){
                   $(campoCPFCNPJ).mask("9?9.999.999");
            }); 
        }
    }
}
//////////////////////////////////////////
function ValidarCPFCNPJPadrao(campoInput, campoParametro, formato)
{
    var desc = 'Tipo Pessoa';
    
    if (campoParametro.selectedIndex != 0)
    {
        campoInput.value = removeCharNaoNumero(campoInput.value);
        
        var CPFCNPJ = parseInt(campoInput.value);
        if (CPFCNPJ == 0)
            return false
        else
        if (campoParametro.selectedIndex == 1)
        {           
            formataCampoPadrao(campoInput, campoParametro);
            return ValidarCPF(campoInput, formato);//CPF            
        }
        else 
        if (campoParametro.selectedIndex == 2)
        {           
            formataCampoPadrao(campoInput, campoParametro);
            return ValidarCNPJ(campoInput, formato);//CNPJ
        }
        else
        if (campoParametro.selectedIndex == 3)
        {
            formataCampoPadrao(campoInput, campoParametro);
            campoInput.value = campoInput.value.substr(0,2)+'.'+campoInput.value.substr(2,3)+'.'+campoInput.value.substr(5,3);
        }
    }
}

//////////////////////////////////////////

function formataCampoPadrao(campoInput, campoParametro){
  campoInput.value = removeCharNaoNumero(campoInput.value);
  if (campoParametro.selectedIndex != 0)
  {

    if (campoParametro.selectedIndex == 3)
    {
      //CNPJBASE
      campoInput.value = PreencheCharEsquerda(campoInput.value, 8, '0');
      //campoInput.value = campoInput.value.substr(0,2)+'.'+campoInput.value.substr(3,3)+'.'+campoInput.value.substr(6,3);
    } 
    else 
    {
        if (campoParametro.selectedIndex == 1)
        {
          //CPF
          campoInput.value = PreencheCharEsquerda(campoInput.value, 11, '0');
          campoInput.value = campoInput.value.substr(0,3)+'.'+campoInput.value.substr(3,3)+'.'+campoInput.value.substr(6,3) +'-'+campoInput.value.substr(9,2);
        }
        else 
        { 
          if (campoParametro.selectedIndex == 2)
          {
            campoInput.value = PreencheCharEsquerda(campoInput.value, 14, '0');
            campoInput.value = campoInput.value.substr(0,2)+'.'+campoInput.value.substr(2,3)+'.'+campoInput.value.substr(5,3) +'/'+campoInput.value.substr(8,4)+'-'+campoInput.value.substr(12,2);
          };
        };
    };
    
  }
  else
  {
    
    if(campoInput.value != '')
    {
        //campoInput.value = campoInput.value;
        jAlert('Informe o Tipo Pessoa', TITULO_ALERTA);
        campoInput.value = '';
        campoParametro.focus();
        return 0;
    }
  };

  return;
};

function ValidaCampoValor(campoInput, qtdMax)
{
    conteudo = campoInput.value;    
    conteudo = conteudo.replace(/[.]/gi, "");
    conteudo = conteudo.replace(",", ".");      

    if ((conteudo.length - 1) > qtdMax) //conteudo.length - 1 por causa do "." que não considera
        campoInput.value = '';
    
    if (!jQuery.isNumeric(conteudo))
        campoInput.value = '';  
        
    return 0;
}

function ValidaCaracteresEspeciais(campoInput) {
   //se não desejar números é só remover da regex abaixo
   var regex = '[^a-zA-Z0-9]+';
   if(campoInput.match(regex)) {
        //encontrou então não passa na validação
    return false;
   }
   else {
        //não encontrou caracteres especiais
    return true;
   }
}

function MascaraCPFCNPJ(o,f){
    v_obj=o
    v_fun=f
    setTimeout('ExecMascara()',1)
}
 
function ExecMascara(){
    v_obj.value=v_fun(v_obj.value)
}
 
function CPFCnpj( v ){
 
    v=v.replace(/\D/g,""); //Remove tudo o que não é dígito
 
    if (v.length <= 14) { //CPF
        v=v.replace(/\D/g,""); //Remove tudo o que não é dígito
        v=v.replace(/(\d{3})(\d)/,"$1.$2"); //Coloca um ponto entre o terceiro e o quarto dígitos
        v=v.replace(/(\d{3})(\d)/,"$1.$2"); //Coloca um ponto entre o terceiro e o quarto dígitos
        //de novo (para o segundo bloco de números)
        v=v.replace(/(\d{3})(\d{1,2})$/,"$1-$2"); //Coloca um hífen entre o terceiro e o quarto dígitos
    } else { //CNPJ
        v=v.replace(/\D/g,""); //Remove tudo o que não é dígito
        v=v.replace(/^(\d{2})(\d)/,"$1.$2"); //Coloca ponto entre o segundo e o terceiro dígitos
        v=v.replace(/^(\d{2})\.(\d{3})(\d)/,"$1.$2.$3"); //Coloca ponto entre o quinto e o sexto dígitos
        v=v.replace(/\.(\d{3})(\d)/,".$1/$2"); //Coloca uma barra entre o oitavo e o nono dígitos
        v=v.replace(/(\d{4})(\d)/,"$1-$2"); //Coloca um hífen depois do bloco de quatro dígitos
    }
 
    return v;

}

function FormatarCPFCNPJ( v ){

    v = tirarFormacataoCPFCNPJ(v);

    if(v == '') return v;

    if ( v.length <= 11) { //CPF
      v = PreencheCharEsquerda(v, 11, '0');
      v = v.substr(0,3)+'.'+v.substr(3,3)+'.'+v.substr(6,3) +'-'+v.substr(9,2);

    } else { //CNPJ
      v = PreencheCharEsquerda(v, 14, '0');
      v = v.substr(0,2)+'.'+v.substr(2,3)+'.'+v.substr(5,3) +'/'+v.substr(8,4)+'-'+v.substr(12,2);
    }
    return v;

}

function ValidarCPFCNPJ(campoInput){

  desformataCampo(campoInput, FMT_CNPJCPF);
    
  if (campoInput.value.length > 11)  
    {   
        formataCampo(campoInput, FMT_CNPJCPF);
        return ValidarCNPJ(campoInput, FMT_CNPJ);//CNPJ 
        }
    else 
    {           
        formataCampo(campoInput, FMT_CNPJCPF);
        return ValidarCPF(campoInput, FMT_CPF);//CPF    
    }

}

function tirarFormacataoCPFCNPJ(valor){
    valor = removeLetra(valor, '.');
    valor = removeLetra(valor, '/');
    valor = removeLetra(valor, '-');  
    return valor;
}

function tirarFormacataoData(valor){
    valor = removeLetra(valor, '/');
    valor = removeLetra(valor, '-');  
    valor = removeLetra(valor, ' ');  
    valor = removeLetra(valor, ':');  
    return valor;
}

function colcarFormacataoData(valor){
    valor = tirarFormacataoData(valor); // valor = 20180119 == 19/01/2018
    if ( valor != "" ){
      valor = valor.substring(6,8) + "/"+valor.substring(4,6)+ "/" + valor.substring(0,4);
    }
    return valor;
}

function colcarFormacataoDataXML(valor){
  valor = tirarFormacataoData(valor); // valor = 20180119 == 2019-02-01
  if ( valor != "" ){
    valor = valor.substring(0,4) + "-"+valor.substring(4,6)+ "-" + valor.substring(6,8);
  }
  return valor;
}

function colcarFormacataoDataXMLPadrao(valor){
  valor = tirarFormacataoData(valor); // valor = 01/02/2019 == 2019-02-01
  if ( valor != "" ){
    valor = valor.substring(4,8)+ "-"+valor.substring(2,4)+ "-" + valor.substring(0,2) ;
  }
  return valor;
}

function tirarFormacataoHora(valor){
    // valor = 105959
    valor = tirarFormacataoData(valor);

    if ( valor != "" ){
      valor = valor.substring(0,2) + ":"+valor.substring(2,4)+ ":" + valor.substring(4,6);
    }

     return valor;

}

function colcarFormacataoDataHora(valor){
    // valor = 20180119100000

    if ( valor == "" || valor == "0" ){
      return "";
    }
    
    valor = tirarFormacataoData(valor);
    
    if ( valor == "" || valor == "0" ){
      return "";
    }

    data = valor.substring(0, 8);
    hora = valor.substring(8,14);
    valor = colcarFormacataoData( data ) + " " + tirarFormacataoHora( hora );

    return valor;
}

function colcarFormacataoInteiro(nr) {
  return String(nr).split('').reverse().join('').split(/(\d{3})/).filter(Boolean).join('.').split('').reverse().join('');
}

function isNumber(n) {
    return !isNaN( parseFloat(n)) && isFinite(n);
}

function GetValorInteiro( Valor ){	
	try {
		
		//if( !isNumber(Valor) )
		//	return 0;
		//return parseInt( Valor.replace(/\./g, '') ) || 0;	
		
		var Resultado = 0;
		Resultado = parseInt( Valor.replace(/\./g, '') ) || 0;	
		if( !isNumber(Resultado) )
			return 0;
		return Resultado;	
		
	} catch (e) {
		return 0;
	}
}

function GetValorDecimal( Valor ){	
	try {
		
		//Valor = Valor.replace(/\./g, '').replace(',', '.');
		//if( !isNumber(Valor) )
		//	return 0;			
		//return parseFloat( Valor.replace(/\./g, '').replace(',', '.') ).toFixed(2) || 0;
		//return parseFloat( Valor ).toFixed(2) || 0;
		
		var Resultado = 0;
		//Resultado = parseFloat( Valor ).toFixed(2) || 0;
		Resultado = parseFloat( Valor.replace(/\./g, '').replace(',', '.') ).toFixed(2) || 0;
		if( !isNumber(Resultado) )
			return 0;	
		return Resultado;	
		
	} catch (e) {
		return 0;
	} 
}

function GetValorDecimalMaior( Valor ){	
	try {
		
		var Resultado = 0;
		Resultado = parseFloat( Valor.replace(/\./g, '').replace(',', '.') ) || 0;
		if( !isNumber(Resultado) )
			return 0;	
		return Resultado;	
		
	} catch (e) {
		return 0;
	} 
}

function fTrucarValorFixed(Valor, TamanhoCasasDecimais = 2) {
  TamanhoCasasDecimais = TamanhoCasasDecimais || 0;
  TamanhoCasasDecimais = Math.pow(10, TamanhoCasasDecimais);
  return Math.floor(Valor * TamanhoCasasDecimais) / TamanhoCasasDecimais;
}

function fTrucarValor( Valor ){
    //return Math.trunc(Valor * Math.pow(10, 2)) / Math.pow(10, 2);
	//return Valor - Math.pow(10, -2) / 2;
	
	Valor = Valor - Math.pow(10, -2) / 2;
	var valores = Valor.toString().split(".");
	var resultado = "0.00";
	if( valores[1].length == 1)
		resultado = valores[0]+"."+valores[1]+"0"
	else	
		resultado = valores[0]+"."+valores[1].substring(0,2);
	return parseFloat(resultado);
}

function fMascaraValor( valor ) {
    return valor.toFixed(2).replace('.', ',').replace(/(\d)(?=(\d{3})+\,)/g, "$1.");
    // return valor.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});
    // return Intl.NumberFormat('pt-br', {style: 'currency', currency: 'BRL'}).format(valor)
}

function fMascaraValorMaior( valor ) {
	return valor.toFixed(10).replace('.', ',').replace(/(\d)(?=(\d{3})+\,)/g, "$1.");
}

function fMascaraValorSemLimite( valor ) {
    return valor.toLocaleString('pt-br', {minimumFractionDigits: 2, maximumFractionDigits: 10}).replace(',00', '');
}

function fCalcularJuros(Valor, Taxa){
	//return (Valor * Taxa) / 100;
	
	var Total = 0;
	Total = (Valor  * Taxa );
	//Total = Total.toFixed(2);
	
	Total = (Total / 100 );
	//Total = Total.toFixed(2);
	
	return parseFloat(Total.toFixed(2));
}