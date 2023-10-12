"""Импорт для создания датаклассов"""
from dataclasses import dataclass
from environs import Env
from sqlalchemy.orm import Session

@dataclass
class DbData:
    """Класс с данными для базы данных"""
    database: str
    user: str
    password: str
    port: int
    debug: bool
    session: Session = None


@dataclass
class Config:
    """Общий класс конфига содержащий все остальные"""

    db: DbData
    app_container_name: str
    db_container_name: str


def load_config(path: str = None):
    """Загрузка переменных окружения в класс для удобства использования"""

    env = Env()
    env.read_env(path)

    config = Config(
        db=DbData(
            debug=env.bool("DEBUG"),
            database=env.str("POSTGRES_DB"),
            user=env.str("POSTGRES_USER"),
            password=env.str("POSTGRES_PASSWORD"),
            port=env.str("POSTGRES_PORT"),
        ),
        app_container_name=env.str("APP_CONTAINER_NAME"),
        db_container_name=env.str("DB_CONTAINER_NAME"),
    )
    return config

config = load_config("./.env")
