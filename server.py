"""Главный файл по запуску приложения FastAPI"""
import atexit
from fastapi import FastAPI

from src.db.db import on_shutdown, on_startapp
from src.quiz.router import router as quiz_router

app  = FastAPI()


def main():
    """Главная функция при запуске приложения"""
    startapp()
    atexit.register(shutdown)


def startapp():
    """Функция старта приложения"""

    #included diferent routers from modules
    app.include_router(quiz_router)

    #startapp sqlite
    on_startapp()
    print("\n\n----------------\n\nstart application\n\n----------------\n\n")


def shutdown():
    """Функция завершения работы приложения"""
    #shutdown sqlite
    on_shutdown()
    print("\n\n----------------\n\nstop application\n\n----------------\n\n")

if __name__ == "server":
    main()
