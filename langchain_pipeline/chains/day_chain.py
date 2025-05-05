def generate_day_by_day(pois, events, weather):
    return [
        {
            "day": "2025-05-10",
            "morning": pois[0]["name"] if pois else "Passeio livre",
            "afternoon": events[0]["name"] if events else "Evento não disponível",
            "weather": weather["forecast"][0] if "forecast" in weather else {}
        },
        {
            "day": "2025-05-11",
            "morning": pois[1]["name"] if len(pois) > 1 else "Passeio livre",
            "afternoon": events[1]["name"] if len(events) > 1 else "Evento não disponível",
            "weather": weather["forecast"][1] if "forecast" in weather and len(weather["forecast"]) > 1 else {}
        }
    ]
