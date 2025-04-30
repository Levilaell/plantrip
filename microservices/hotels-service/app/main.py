from fastapi import FastAPI # type: ignore
from app.hotels_service import search_hotels

app = FastAPI()

@app.get("/hotels")
def hotels(dest: str, check_in: str, check_out: str):
    return search_hotels(dest, check_in, check_out)