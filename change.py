import requests

url = "https://api.frankfurter.dev/v1/latest" 
params = {"base": "USD", "symbols": "EUR"} #les information  

response = requests.get(url, params=params, timeout=5) # tipmeout ken me jewbch dans 5 s ttt3adda eurreur 
print(response.status_code)
print(response.json())