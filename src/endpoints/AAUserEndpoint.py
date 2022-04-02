# -*- coding: utf-8 -*-
import sys
import os
import inspect
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import src.database as _database
import src.config.config_trace as _tracer
from src.config.config_login_manager import manager
from src.config.config_templates import templates as _templates
import src.schemas as _schemas
import src.services as _services


router = _fastapi.APIRouter(prefix="/users", tags=['users'])
# fastapi.responses.RedirectResponse(url=request.url_for(name='account')


# @router.post("/login", status_code=_fastapi.status.HTTP_200_OK)
# async def get_login(request: OAuth2PasswordRequestForm = _fastapi.Depends(), db: _orm.Session = _fastapi.Depends(_database.base.get_db)):
#     try:
#         db_user = await _services.UserService.get_user_by_email(db=db, email=request.username)
#         if not db_user:
#             raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
#         if not Hash.verify(db_user.hashed_password, request.password):
#             raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
#         access_token = _token.create_access_token(data={"sub": db_user.email, "id": db_user.id})
#         return {"access_token": access_token, "token_type": "bearer"}
#     except Exception as e:
#         raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
#
#
# @router.post("/logado", status_code=_fastapi.status.HTTP_200_OK)
# async def get_logado(current_user: _schemas.User = _fastapi.Depends(_oauth2.get_current_user)):
#     try:
#         return {"logado-id": current_user.id, "logado-email": current_user.username}
#     except Exception as e:
#         raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/", responses={_fastapi.status.HTTP_400_BAD_REQUEST: {'model': _schemas.ErrorOutput}})  # , response_model=List[_schemas.User]
async def read_users(skip: int = 0, limit: int = 10, db: _orm.Session = _fastapi.Depends(_database.base.get_db)):  # _orm.Session # _database.SessionAsync # AsyncSession
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        span.set_attribute("parametro_skip", skip)
        span.set_attribute("parametro_limit", limit)
        _rows = await _services.UserService.get_users(db=db, skip=skip, limit=limit)
        return _schemas.ResponseSchema(status="Ok", code="200", message="Success fetch all data", result=_rows).dict(exclude_none=True, exclude_unset=True, exclude_defaults=True)


@router.get("/{user_id}", response_model=_schemas.User)
async def read_user(user_id: int, db: _orm.Session = _fastapi.Depends(_database.base.get_db)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        span.set_attribute("parametro_user_id", user_id)
        return await _services.UserService.get_user(db=db, user_id=user_id)


@router.post("/", response_model=_schemas.User)
async def create_user(user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_database.base.get_db)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        span.set_attribute("parametro_user", user)
        return await _services.UserService.create_user(db=db, user=user)


@router.put("/{user_id}", response_model=_schemas.User)
async def update_user(user_id: int, user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_database.base.get_db)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        span.set_attribute("parametro_user", user)
        return await _services.UserService.update_user(db=db, user=user, user_id=user_id)


@router.delete("/{user_id}", status_code=_fastapi.status.HTTP_204_NO_CONTENT)
async def delete_post(user_id: int, db: _orm.Session = _fastapi.Depends(_database.base.get_db)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        span.set_attribute("parametro_user_id", user_id)
        return await _services.UserService.delete_user(db=db, user_id=user_id)
