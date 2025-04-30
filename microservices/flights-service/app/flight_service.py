def get_flight_offers(origin, destination, date):
    # Em produção, aqui consultaria APIs reais como Amadeus ou Skyscanner
    return [
        {
            "origin": origin,
            "destination": destination,
            "date": date,
            "price": 350.00,
            "airline": "Air France",
            "duration": "10h 40min",
            "departure_time": "2025-05-10T23:50:00"
        }
    ]