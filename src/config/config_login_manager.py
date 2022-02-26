# -*- coding: utf-8 -*-
import sqlalchemy.orm as _orm
from fastapi_login import LoginManager
from src.database.session import SessionLocal
from src.repositories.usuario import UsuarioRepository


SECRET = 'b#=x&h)cms#lsr*4+jghmlsrpe^p3nyoamu$860gip$4h+00w'
ALGORITHM = "HS256"  # jwt.ALGORITHMS.HS256  # jwt.ALGORITHMS.HS512
manager = LoginManager(secret=SECRET, token_url='/login/entrar2', algorithm=ALGORITHM, use_cookie=True)
manager.cookie_name = "cms-tnb"


@manager.user_loader()
async def load_user(email: str, db: _orm.Session = None):
    if db is None:
        with SessionLocal() as db:
            return await UsuarioRepository.get_by_email_full(db=db, email=email)
    else:
        return await UsuarioRepository.get_by_email_full(db=db, email=email)


'''


- --- config_OAuth2.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import src.config.config_token as _token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/entrar2")


async def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    return _token.verify_token(data, credentials_exception)


from datetime import datetime, timedelta
from jose import JWTError, jwt
import src.schemas as _schemas


- --- config_token.py

SECRET_KEY = "070ca90e58cd94dd24405fef93dabc4026023b989c98e257f022e13b00c19c2c"
ALGORITHM = "HS256"  # jwt.ALGORITHMS.HS256  # jwt.ALGORITHMS.HS512
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str):
    str_decode_token = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
    return str_decode_token if str_decode_token["expires"] >= datetime.time else None


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not payload:
            raise credentials_exception
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        idd: str = payload.get("id")
        if idd is None:
            raise credentials_exception
        token_data = _schemas.TokenData(id=int(idd), username=email)
        return token_data
    except JWTError:
        raise credentials_exception



---- config_hashing.py

from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:

    @classmethod
    def bcrypt(cls, password: str):
        return pwd_cxt.hash(password)

    @classmethod
    def verify(cls, hashed_password: str, plain_password: str):
        return pwd_cxt.verify(secret=plain_password, hash=hashed_password)




'''