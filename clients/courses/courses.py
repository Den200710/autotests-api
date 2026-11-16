import httpx

from clients import courses
from tools.fakers import get_random_email


create_payload = {
  "email": get_random_email(),
  "password": "123",
  "lastName": "Test",
  "firstName": "Test19",
  "middleName": "Test19"
}

response_create_user = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_payload)
user_data = response_create_user.json()
print(user_data)

user_id = user_data['user']['id']

authentification_payload = {
  "email": create_payload['email'],
  "password": create_payload['password']
}
response_authentification = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=authentification_payload)
response_authentification_data = response_authentification.json()

token = response_authentification_data['token']['accessToken']
headers = {"Authorization": f"Bearer {token}"}

courses_payload = {
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "estimatedTime": "string",
    "previewFileId": "string",
    "createdByUserId": str(user_id)
}

create_courses = httpx.post(f"http://127.0.0.1:8000/api/v1/courses", headers=headers, json=courses_payload)
created_courses_data = create_courses.json()
print(created_courses_data)

response_course = httpx.get(f"http://127.0.0.1:8000/api/v1/courses/{user_id}", headers=headers )
print(response_course.json())