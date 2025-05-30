import requests

url = "http://localhost:8000/suggest/"

payload = {
    "user_id": "user_1"
}

response = requests.post(url, json=payload)
print("Response JSON:", response.json())