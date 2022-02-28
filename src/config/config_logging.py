import logging


def get_logger() -> logging.Logger:
    #FORMAT = "[%(levelname)s  %(name)s %(module)s:%(lineno)s - %(funcName)s() - %(asctime)s]\t %(message)s \n"
    FORMAT = "[%(asctime)s] | %(levelname)7s | %(module)10s | %(funcName)11s | %(lineno)4d | %(message)s"
    TIME_FORMAT = "%Y.%m.%d %I:%M:%S %p"
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)  # datefmt=TIME_FORMAT,  FILENAME = 'example/path/log.log'
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(FORMAT))
    logger.addHandler(handler)
    return logger




# from fastapi.logger import logger as fastapi_logger
# from logging.handlers import RotatingFileHandler
# import logging
#
# formatter = logging.Formatter("[%(asctime)s.%(msecs)03d] %(levelname)s [%(thread)d] - %(message)s", "%Y-%m-%d %H:%M:%S")
# handler = RotatingFileHandler('logfile.log', backupCount=0)
# logging.getLogger("fastapi")
# fastapi_logger.addHandler(handler)
# handler.setFormatter(formatter)
# fastapi_logger.info('****************** Starting Server *****************')
#
# #logging.basicConfig(filename='mylog.log', encoding='utf-8', level=logging.DEBUG)


'''


config.setup_logging()
logger = config.get_logger()
   logger.debug("Added new actor %s", name)
     logger.warn(str(e))
     logger.error(str(e))
      logger.critical(str(e))
      logger.info("Created sqlite table schemas")


import os
import sys
from logging import Logger, getLogger
from logging.config import dictConfig

import yaml

DEFAULT_DB_PATH = "./db"

################################################################################
# config functions


def get_db_path() -> str:
    """Returns the movie DB path."""

    return os.getenv("MM_DB_PATH", DEFAULT_DB_PATH)


def get_log_config() -> str:
    """Returns the logging config path."""

    path_override = os.getenv("MM_LOG_CONFIG_PATH")

    if path_override is not None:
        path = path_override
    else:
        path = f"{get_db_path()}/logging.yaml"

    return path


def get_logger() -> Logger:
    """Returns the application logger."""

    return getLogger("moviemanager")


def get_sqlite_path() -> str:
    """Returns path to the sqlite DB file."""

    path_override = os.getenv("MM_SQLITE_PATH")

    if path_override is not None:
        return path_override

    return f"{get_db_path()}/sqlite.db"


def setup_logging() -> None:
    """Configures logging for the application using the yaml config file."""

    path = get_log_config()

    try:
        with open(path, "r") as f:
            data = yaml.safe_load(f)
    except:
        logger = getLogger()
        logger.critical("Failed to read the logging config file %s", path)

        sys.exit(1)

    dictConfig(data)
    
    



import logging
import sys
import typing as t

from werkzeug.local import LocalProxy

from .globals import request

if t.TYPE_CHECKING:
    from .app import Flask


@LocalProxy
def wsgi_errors_stream() -> t.TextIO:
    return request.environ["wsgi.errors"] if request else sys.stderr


def has_level_handler(logger: logging.Logger) -> bool:
    level = logger.getEffectiveLevel()
    current = logger
    while current:
        if any(handler.level <= level for handler in current.handlers):
            return True
        if not current.propagate:
            break
        current = current.parent  # type: ignore
    return False

default_handler = logging.StreamHandler(wsgi_errors_stream)  # type: ignore
default_handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s"))

def create_logger(app: "Flask") -> logging.Logger:.logging.wsgi_errors_stream` with a basic format.
    """
    logger = logging.getLogger(app.name)

    if app.debug and not logger.level:
        logger.setLevel(logging.DEBUG)

    if not has_level_handler(logger):
        logger.addHandler(default_handler)

    return logger

    
'''