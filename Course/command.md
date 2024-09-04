Virtual env activation:
    `.\venv\Scripts\activate`

Server activation:
    `uvicorn api:app --port 8000 --reload`

curl Alias deletion on Windows:
    `Remove-Item alias:curl`

add todo with curl command:
    `curl -X POST 'http://127.0.0.1:8000/todo' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"id\": 1, \"item\": \"First Todo is to finish this book!\"}'`

add todo with curl command (including Todo Model):
    `curl -X POST 'http://127.0.0.1:8000/todo' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"id\": 1, \"item\": \"First Todo is to finish this book!\"}'`

update a todo with curl command:
    `curl -X PUT 'http://127.0.0.1:8000/todo/1' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"item\": \"Updated todo message!\"}'`

get a todo with curl command:
    `curl -X GET 'http://127.0.0.1:8000/todo/1' -H 'accept: application/json' -H 'Content-Type: application/json'`
    `curl -X GET 'http://127.0.0.1:8000/todo/1' -H 'accept: application/json'`