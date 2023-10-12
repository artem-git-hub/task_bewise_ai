"""Для логирования происходящего с базой данных"""
import logging

import sqlite3
from sqlalchemy import create_engine, Column, DateTime, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import config

logger = logging.getLogger(__name__)

# Create a base class for declarative models
Base = declarative_base()

class TimedModel(Base):
    """Класс для сохранения времени создания и обновления записи"""
    __abstract__ = True

    created_at = Column(DateTime(True), server_default=func.now())
    updated_at = Column(
        DateTime(True),
        default=func.now(),
        onupdate=func.now(),
        server_default=func.now(),
    )


def request(func):
    """Декоратор для функций взаимодействия с базой данных"""
    def good_interaction(*args, **kwargs):
        try:
            # Начало явной транзакции
            config.db.session.begin()

            # Операции с базой данных
            result = func(session=config.db.session, *args, **kwargs)

            # Закрыть сессию
            config.db.session.close()


            return result

        except Exception as e:
            # Откат транзакции в случае ошибки
            config.db.session.rollback()
            logger.error("Transaction error: %s", e)
            raise
    return good_interaction



def on_startapp():
    """Функция по запуску базы данных"""
    try:
        db_url = f"postgresql://{config.db.user}:{config.db.password}@{config.db_container_name}/{config.db.database}"
        engine = create_engine(db_url, echo=True)


        # Session = sessionmaker(bind=engine)
        Session = sessionmaker(autoflush=True, bind=engine)

        Base.metadata.create_all(engine, checkfirst=True)

        config.db.session = Session()

        logger.info("Successful connection to SQLite")
    except sqlite3.OperationalError as e:
        logger.error("Failed to establish connection with SQLite.")
        logger.error(str(e))
        exit(1)


    if config.db.debug:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)


def on_shutdown():
    """Функция для завершения работы базы данных"""
    config.db.session.close()
    