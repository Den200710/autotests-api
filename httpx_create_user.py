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

user_id = user_data['user']['id']

authentification_payload = {
  "email": create_payload['email'],
  "password": create_payload['password']
}
response_authentification = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=authentification_payload)
response_authentification_data = response_authentification.json()
print(response_authentification.status_code)
print(response_authentification.json())
print(response_authentification.url)

token = response_authentification_data['token']['accessToken']
headers = {"Authorization": f"Bearer {token}"}

response_get_user = httpx.get(f"http://127.0.0.1:8000/api/v1/users/{user_id}", headers=headers)
print(response_get_user.json())
print(response_get_user.url)

patch_payload = {
  "lastName": "Test",
  "firstName": "Test21",
  "middleName": "Test21"
}
response_patch_user = httpx.patch(f"http://127.0.0.1:8000/api/v1/users/{user_id}", json=patch_payload, headers=headers)
print(response_patch_user.status_code)
print(response_patch_user.json())
print(response_patch_user.url)

response_delete_user = httpx.delete(f"http://127.0.0.1:8000/api/v1/users/{user_id}", headers=headers)
print(response_delete_user.status_code)
print(response_delete_user.url)

response_authentification = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=authentification_payload)
response_authentification_data = response_authentification.json()
print(response_authentification.status_code)
print(response_authentification.json())
print(response_authentification.url)
