# import sqlalchemy.orm as _orm
# import inspect
# import logging
# import fastapi as _fastapi
# import src.schemas as _schemas
# import src.services as _services
# import src.config.config_trace as _tracer
# import src.config.config_logging as _logger
# from src.repositories.AAUserRepository import UserRepository
# from src.models.AAUserModel import UserModel
#
#
# class UserService(_services.BaseService):
#     logger: logging.Logger = _logger.get_logger()
#
#     def __init__(self) -> None:
#         super().__init__()
#
#     @classmethod
#     async def get_users(cls, db: _orm.Session, skip: int = 0, limit: int = 100):  # -> Iterator[_schemas.User]:  # _orm.Session
#         cls.logger.info(msg="get_users")
#         with _tracer.tracer.start_as_current_span(f"{cls.__name__}.{inspect.stack()[0][3]}") as span:
#             span.set_attribute("parametro_skip", skip)
#             span.set_attribute("parametro_limit", limit)
#             try:
#
#                 # rows = await _repositories.UserRepository.get_all(db=db, skip=skip, limit=limit)
#                 # # users = []
#                 # # for row in rows:
#                 # #     user = _schemas.User(id=int(row["id"]), email=str(row["email"]), is_active=True if row["is_active"] else False)
#                 # #     users.append(user)
#                 # users = [_schemas.User(id=int(row["id"]), email=str(row["email"]), is_active=True if row["is_active"] else False) for row in rows]
#
#                 users = await UserRepository.get_all(db=db, skip=skip, limit=limit)
#
#                 return users
#
#             except Exception as e:
#                 span.record_exception(e)
#                 raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
#
#     @classmethod
#     async def get_user(cls, db: _orm.Session, user_id: int) -> UserModel:
#         with _tracer.tracer.start_as_current_span(f"{cls.__name__}.{inspect.stack()[0][3]}") as span:
#             span.set_attribute("parametro_user_id", user_id)
#             try:
#                 db_user = await UserRepository.get_by_id(db, user_id)
#                 if db_user is None:
#                     raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_404_NOT_FOUND, detail="sorry this user does not exist")
#                 return db_user
#             except Exception as e:
#                 span.record_exception(e)
#                 raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
#
#     @classmethod
#     async def get_user_by_email(cls, db: _orm.Session, email: str) -> UserModel:
#         with _tracer.tracer.start_as_current_span(f"{cls.__name__}.{inspect.stack()[0][3]}") as span:
#             span.set_attribute("parametro_email", email)
#             try:
#                 return await UserRepository.get_by_email(db, email)
#             except Exception as e:
#                 span.record_exception(e)
#                 raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
#
#     @classmethod
#     async def create_user(cls, db: _orm.Session, user: _schemas.UserCreate) -> UserModel:
#         with _tracer.tracer.start_as_current_span(f"{cls.__name__}.{inspect.stack()[0][3]}") as span:
#             span.set_attribute("parametro_user", user)
#             try:
#                 db_user = await _services.UserService.get_user_by_email(db=db, email=user.email)
#                 if db_user:
#                     raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_404_NOT_FOUND, detail="woops the email is in use")
#                 new_user = UserModel(email=user.email, hashed_password=user.password)
#                 return await UserRepository.create(db, new_user)
#             except Exception as e:
#                 span.record_exception(e)
#                 raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
#
#     @classmethod
#     async def update_user(cls, db: _orm.Session, user: _schemas.UserCreate, user_id: int) -> UserModel:
#         with _tracer.tracer.start_as_current_span(f"{cls.__name__}.{inspect.stack()[0][3]}") as span:
#             span.set_attribute("parametro_user_id", user_id)
#             span.set_attribute("parametro_user", user)
#             try:
#                 db_user = await UserRepository.get_by_id(db, user_id)
#                 if user.email:
#                     db_user.email = user.email
#                 if user.password:
#                     db_user.hashed_password = user.password
#                 return await UserRepository.update(db, db_user)
#             except Exception as e:
#                 span.record_exception(e)
#                 raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
#
#     @classmethod
#     async def delete_user(cls, db: _orm.Session, user_id: int):  # -> dict[str, str]:
#         with _tracer.tracer.start_as_current_span(f"{cls.__name__}.{inspect.stack()[0][3]}") as span:
#             span.set_attribute("parametro_user_id", user_id)
#             try:
#                 db_user = await UserRepository.get_by_id(db, user_id)
#                 if db_user is None:
#                     raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_404_NOT_FOUND, detail="Resource Not Found")
#                 await UserRepository.delete_by_id(db, db_user)
#                 # return {"message": f"successfully deleted user with id: {user_id}"}
#                 return _schemas.StandardOutput(message=f"successfully deleted user with id: {user_id}")
#             except Exception as e:
#                 span.record_exception(e)
#                 raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
