import requests

url = "http://localhost:8000/suggest/"

payload = {
    "user_id": "user_1",
    "question": None
}

response = requests.post(url, json=payload)
print("Assistant:", response.json()['suggestion'])
