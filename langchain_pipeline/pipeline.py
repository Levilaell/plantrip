# pipeline.py

from langchain_pipeline.agents.flight_agent import fetch_flights
from langchain_pipeline.agents.hotel_agent  import fetch_hotels
from langchain_pipeline.agents.poi_agent    import fetch_pois
from langchain_pipeline.agents.events_agent import fetch_events
from langchain_pipeline.agents.weather_agent import fetch_weather
from langchain_pipeline.agents.currency_agent import fetch_currency

from langchain_pipeline.chains.overview_chain import generate_overview
from langchain_pipeline.chains.day_chain      import generate_day_by_day


def start_pipeline(itinerary_id):

    flights = fetch_flights("GRU", "CDG", "2025-05-10")
    hotels = fetch_hotels("Paris", "2025-05-10", "2025-05-12")
    pois = fetch_pois("Paris")
    events = fetch_events("Paris", "2025-05-10", "2025-05-12")
    weather = fetch_weather(48.8566, 2.3522, "2025-05-10", "2025-05-12")
    currency = fetch_currency("EUR", "BRL")

    overview = generate_overview("Paris", "10/05–12/05", pois)
    days = generate_day_by_day(pois, events, weather)

    return {
        "overview": overview,
        "days": days,
        "flights": flights,
        "hotels": hotels,
        "events": events,
        "weather": weather,
        "currency": currency
    }
