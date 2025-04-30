def search_pois(location):
    # Simulação de POIs — depois vamos integrar com Google Places / TripAdvisor
    
    return [
        {
            "name": "Torre Eiffel",
            "category": "landmark",
            "rating": 4.8,
            "price_level": "€€",
            "location": location
        },
        {
            "name": "Museu do Louvre",
            "category": "museum",
            "rating": 4.7,
            "price_level": "€€",
            "location": location
        },
        {
            "name": "Montmartre",
            "category": "neighborhood",
            "rating": 4.6,
            "price_level": "€",
            "location": location
        }
    ]