def search_hotels(dest, check_in, check_out):
    # Simulação: depois substituímos por chamadas reais a Booking.com ou Expedia
    
    return [
        {
            "name": "Hotel Le Meurice",
            "location": dest,
            "check_in": check_in,
            "check_out": check_out,
            "price_per_night": 550.00,
            "rating": 9.2,
            "type": "Hotel",
            "platform": "Booking.com"
        },
        {
            "name": "Studio Montmartre",
            "location": dest,
            "check_in": check_in,
            "check_out": check_out,
            "price_per_night": 120.00,
            "rating": 4.9,
            "type": "Airbnb",
            "platform": "Airbnb"
        }
    ]