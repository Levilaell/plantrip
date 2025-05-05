import requests

def fetch_flights(origin, destination, date):
    url = f"http://flights-service:5000/offers?origin={origin}&destination={destination}&date={date}"
    response = requests.get(url)
    return response.json()
