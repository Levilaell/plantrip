import requests

def fetch_hotels(dest, check_in, check_out):
    url = f"http://hotels-service:5001/hotels?dest={dest}&check_in={check_in}&check_out={check_out}"
    response = requests.get(url)
    return response.json()
