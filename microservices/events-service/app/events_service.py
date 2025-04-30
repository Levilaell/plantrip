def get_events(dest, start_date, end_date):
    # Simulação de eventos — depois usaremos Eventbrite ou Ticketmaster
    return [
        {
            "name": "Concerto de Jazz",
            "location": dest,
            "start_date": start_date,
            "end_date": end_date,
            "price": 30.00,
            "venue": "Le Duc des Lombards"
        },
        {
            "name": "Exposição de Arte Moderna",
            "location": dest,
            "start_date": start_date,
            "end_date": end_date,
            "price": 12.00,
            "venue": "Centre Pompidou"
        }
    ]