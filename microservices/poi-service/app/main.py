from fastapi import FastAPI # type: ignore
from app.poi_service import search_pois

app = FastAPI()

@app.get("/pois")
def pois(location: str):
    return search_pois(location)