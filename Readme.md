# Для запуска:

1. Установить Docker и docker-compose
2. Склонировать этот репозиторий в необходимую директорию и зайти в склонированный проект
3. Запустить команду `sudo docker-compose up --build`
4. Для тестирования можно выполнить такой запрос:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 5}' http://localhost:8000/get_questions/
```
где `'{"questions_num": 5}'` - это данные которые вы передаете в запросе, 5 - кол-во вопросов которые сохранятся в БД

p.s.: ТЗ: https://docs.google.com/document/d/1MPStlOFfvF9YWEx-0I1EwvWE9paKkhvFWyq7tRvcdc0