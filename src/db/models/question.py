"""Для создания модели"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from src.db.db import TimedModel

class Question(TimedModel):
    """Класс для хранения вопросов"""

    __tablename__ = "questions"
    id: int = Column(Integer, primary_key=True, index=True)
    question_text: str = Column(String)
    answer_text: str = Column(String)
    airdate: datetime = Column(DateTime(True))
