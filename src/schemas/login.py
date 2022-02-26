from typing import Optional
import pydantic as _pydantic


class _LoginBase(_pydantic.BaseModel):
    ...


class LoginIn(_LoginBase):
    txtEmail: Optional[str] = None
    txtSenha: Optional[str] = None

    class Config:
        orm_mode = True
        schema_extra = {"example": {"txtEmail": "chris.mar.silva@gmail.com", "txtSenha": "#Chrs2387"}}


class LoginOut(_LoginBase):
    token_type: Optional[str] = None
    access_token: Optional[str] = None
    Id: Optional[str] = None
    Tipo: Optional[str] = None
    Nome: Optional[str] = None
    Foto: Optional[str] = None
    Email: Optional[str] = None

