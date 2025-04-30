def get_weather_forecast(lat, lng, start_date, end_date):
    # Simulação — depois vamos integrar com Google Weather API ou Open-Meteo
    return {
        "location": {"lat": lat, "lng": lng},
        "start_date": start_date,
        "end_date": end_date,
        "forecast": [
            {"date": start_date, "summary": "Parcialmente nublado", "temperature_c": 21},
            {"date": end_date, "summary": "Ensolarado", "temperature_c": 23}
        ]
    }