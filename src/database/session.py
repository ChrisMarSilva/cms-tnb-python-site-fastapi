import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import sqlalchemy.ext.declarative as _declarative


SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:Chrs8723@localhost:3306/tamonabo_BDCMSTamoNaBolsa'  # LOCALHOST
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://tamonabo_rootcms:Chrs8723@nspro44.hostgator.com.br:3306/tamonabo_BDCMSTamoNaBolsa'  # SERVIDOR HOSTGATOR
engine = _sql.create_engine(url=SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True)
SessionLocal = _orm.sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False, class_=_orm.Session)
Base = _declarative.declarative_base()
