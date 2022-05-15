import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import sqlalchemy.ext.declarative as _declarative


SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:senha@localhost:3306/banco'
engine = _sql.create_engine(url=SQLALCHEMY_DATABASE_URL, echo=False, pool_pre_ping=True)
SessionLocal = _orm.sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False, class_=_orm.Session)
Base = _declarative.declarative_base()
