import requests

def fetch_pois(location):
    url = f"http://poi-service:5002/pois?location={location}"
    response = requests.get(url)
    return response.json()
