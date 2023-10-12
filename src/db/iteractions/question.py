"""Описание всех взаимодействий с базой данных конкретного класса"""
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import desc

from src.db.db import request
from src.db.models.question import Question

@request
def select_process_by_id(question_id: int, session: Session = None) -> Question:
    """Select question by id"""
    question = session.query(Question).where(Question.id == question_id).first()
    return question

@request
def select_all_questiones(session: Session = None) -> List[Question]:
    """all questions select"""
    questiones = session.query(Question).all()
    return questiones

@request
def select_last_question(session: Session = None) -> Question:
    """Select the last question from the database"""
    last_question = session.query(Question).order_by(desc(Question.created_at)).first()
    return last_question

@request
def add_question(
    question_id: int,
    question_text: str,
    answer_text: str,
    airdate: datetime,
    session: Session = None) -> bool:
    """Add new question"""
    new_question = Question(
        id=question_id,
        question_text=question_text,
        answer_text=answer_text,
        airdate=airdate
    )
    session.add(new_question)
    session.commit()

@request
def delete_question(question_id: int, session: Session = None) -> None:
    """Delete question by name"""
    question = session.query(Question).where(Question.id == question_id).first()
    session.delete(question)
    session.commit()
