import requests

url = "https://api.frankfurter.app/latest"
params = {"from": "USD", "to": "TND"}

response = requests.get(url, params=params, timeout=5)

print(response.status_code)
print(response.json())