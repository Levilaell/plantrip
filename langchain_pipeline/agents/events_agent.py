import requests

def fetch_events(dest, start_date, end_date):
    url = f"http://events-service:5003/events?dest={dest}&start_date={start_date}&end_date={end_date}"
    response = requests.get(url)
    return response.json()
