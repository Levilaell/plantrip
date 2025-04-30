from fastapi import FastAPI # type: ignore
from app.events_service import get_events

app = FastAPI()

@app.get("/events")
def events(dest: str, start_date: str, end_date: str):
    return get_events(dest, start_date, end_date)

