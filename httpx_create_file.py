import httpx
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

authentification_payload = {
  "email": create_payload['email'],
  "password": create_payload['password']
}
response_authentification = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=authentification_payload)
response_authentification_data = response_authentification.json()
print(response_authentification.status_code)

create_file_headers = {
    "Authorization" : f"Bearer {response_authentification_data['token']['accessToken']}"
}
create_file_response = httpx.post(
    "http://127.0.0.1:8000/api/v1/files",
    data={"filename": "image.png", "directory": "courses"},
    files={"upload_file": open('./testdata/files/image.png', 'rb')},
    headers=create_file_headers
)
create_file_response_data = create_file_response.json()
print(create_file_response_data)