"""Описание обработки эндпоинта"""
from datetime import datetime
import requests

from fastapi import APIRouter, HTTPException

from src.db.iteractions.question import add_question, select_process_by_id, select_last_question
# from src.db.models.question import Question
from .schemas import QuestionRequest
# from src.db.iteractions.question import add_question, select_process_by_id, select_last_question


router = APIRouter(prefix='', tags=['quiz'])

@router.post("/get_questions/")
async def get_questions(q: QuestionRequest) -> dict | str:
    """Метод для обработки запроса по получению вопроса"""

    num_of_unique_questions = 0
    while num_of_unique_questions < q.questions_num:
        try:
            response = requests.get(f"https://jservice.io/api/random?count={q.questions_num}", timeout=20)
        except requests.exceptions.ReadTimeout as e:
            return f"Error of jservice.io: {e}"

        if response.status_code == 200:
            data = response.json()
            if data and "question" in data[0] and "answer" in data[0]:
                question_id = data[0]["id"]
                question_text = data[0]["question"]
                answer_text = data[0]["answer"]
                airdate = data[0]["airdate"]
                datetime_airdate = datetime.strptime(airdate, '%Y-%m-%dT%H:%M:%S.%fZ')

                db_question = select_process_by_id(question_id=question_id)

                if not db_question:
                    db_question = add_question(question_id, question_text, answer_text, datetime_airdate)
                    num_of_unique_questions += 1
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch questions")
    
    last_question = select_last_question()


    return {"id": last_question.id, "question": last_question.question_text, "answer": last_question.answer_text, "airdate": last_question.airdate}
