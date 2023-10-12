"""Описание класса для обработки приходящего запроса"""
from pydantic import BaseModel


class QuestionRequest(BaseModel):
    """Класс для принятия POST запросов"""
    questions_num: int
