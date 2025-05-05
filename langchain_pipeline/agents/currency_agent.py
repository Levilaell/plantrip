import requests

def fetch_currency(base, target):
    url = f"http://currency-service:5005/rate?base={base}&target={target}"
    response = requests.get(url)
    return response.json()
