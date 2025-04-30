from fastapi import FastAPI # type: ignore
from app.weather_service import get_weather_forecast

app = FastAPI()

@app.get("/weather")
def weather(lat: float, lng: float, start_date: str, end_date: str):
    return get_weather_forecast(lat, lng, start_date, end_date)