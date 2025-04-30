def get_exchange_rate(base, target):
    # Simulação — depois podemos usar ExchangeRatesAPI ou Fixer
    return {
        "base": base,
        "target": target,
        "rate": 5.35 if base == "EUR" and target == "BRL" else 1.0
    }

def convert_amount(amount, rate):
    return {
        "original": amount,
        "converted": round(amount * rate, 2)
    }