import requests

def fetch_weather(lat, lng, start_date, end_date):
    url = f"http://weather-service:5004/weather?lat={lat}&lng={lng}&start_date={start_date}&end_date={end_date}"
    response = requests.get(url)
    return response.json()
