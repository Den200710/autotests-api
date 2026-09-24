import httpx

login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(login_response.status_code)
print(login_response.json())

refresh_payload = {
  "refreshToken": login_response_data['token']['refreshToken']
}
refresh_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/refresh", json=refresh_payload)

print(refresh_response.status_code)
print(refresh_response.json())