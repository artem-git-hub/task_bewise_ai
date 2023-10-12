# Для запуска:

1. Установить Docker и docker-compose
2. Склонировать этот репозиторий в необходимую директорию: `git clone git@github.com:artem-git-hub/task_bewise_ai.git`
3. Зайти в склонированный проект
4. Запустить команду `sudo docker-compose up --build`
5. Для тестирования можно выполнить такой запрос в новом окне терминала:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 5}' http://localhost:8000/get_questions/
```
где `'{"questions_num": 5}'` - это данные которые вы передаете в запросе, 5 - кол-во вопросов которые сохранятся в БД

p.s.: ТЗ: https://docs.google.com/document/d/1MPStlOFfvF9YWEx-0I1EwvWE9paKkhvFWyq7tRvcdc0