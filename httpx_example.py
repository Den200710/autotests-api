from idlelib import query
from urllib import response
from wsgiref import headers

import httpx


# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
# print(response.status_code)
# print(response.json())
#
# data = {
#     'userId': 1988,
#     'title': 'new task',
#     'completed': False
# }
#
# request = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
# print(request.status_code)
# print(request.json())

# data = {"username": "tolik", "password": "123" }
# response = httpx.post("https://httpbin.org/post", data=data)
# print(response.status_code)
# print(response.json())

# headers = {"Chiki": "Piki"}
# response = httpx.get("https://httpbin.org/get", headers=headers)
# print(response.status_code)
# print(response.request.headers)
# print(response.json())

# params = {"userId": 1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params= params)
# print(response.url)
# print(response.json())

# files = {"file": ("examle.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
# print(response.json())

# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
# print(response1.json())
# print(response2.json())

# client = httpx.Client(headers={"Chiki": "Piki"})
# response = client.get("https://httpbin.org/get")
# print(response.json())

# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid")
#     response.raise_for_status()
# except httpx.HTTPStatusError as e:
#     print(f"Ошибка {e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
