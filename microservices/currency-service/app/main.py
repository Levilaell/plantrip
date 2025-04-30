from fastapi import FastAPI # type: ignore
from app.currency_service import get_exchange_rate, convert_amount

app = FastAPI()

@app.get("/rate")
def rate(base: str, target: str):
    return get_exchange_rate(base, target)

@app.get("/convert")
def convert(amount: float, rate: float):
    return convert_amount(amount, rate)