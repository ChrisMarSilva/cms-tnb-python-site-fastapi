import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import sqlalchemy.ext.declarative as _declarative
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
#import databases


# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/storedb"
# SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:Chrs8723@localhost:3306/tamonabo_BDCMSTamoNaBolsa'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:Chrs8723@localhost:3306/tamonabo_BDCMSTamoNaBolsa'
# SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://tamonabo_rootcms:Chrs8723@localhost:3306/tamonabo_BDCMSTamoNaBolsa'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://tamonabo_rootcms:Chrs8723@nspro44.hostgator.com.br:3306/tamonabo_BDCMSTamoNaBolsa'

SQLALCHEMY_DATABASE_URL = "sqlite:///./webapp.db"
engine = _sql.create_engine(url=SQLALCHEMY_DATABASE_URL, echo=False, pool_pre_ping=True, connect_args={"check_same_thread": False})
SessionLocal = _orm.sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False, class_=_orm.Session)
Base = _declarative.declarative_base()

SQLALCHEMY_DATABASE_URL_ASYNC = "sqlite+aiosqlite:///./webapp.db"
#database = databases.Database(url=SQLALCHEMY_DATABASE_URL_ASYNC)
engine_async = create_async_engine(url=SQLALCHEMY_DATABASE_URL_ASYNC, future=True, echo=False, pool_pre_ping=True, connect_args={"check_same_thread": False})
SessionAsync = _orm.sessionmaker(bind=engine_async, autoflush=False, autocommit=False, expire_on_commit=False, class_=AsyncSession)
