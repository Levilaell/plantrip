from fastapi import FastAPI
from app.flight_service import get_flight_offers

app = FastAPI()

@app.get("/offers")
def offers(origin: str, destination: str, date: str):
    return get_flight_offers(origin, destination, date)