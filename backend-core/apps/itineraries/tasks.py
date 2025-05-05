# apps/itineraries/tasks.py

from celery import shared_task
from django.apps import apps
from langchain_pipeline.pipeline import start_pipeline
from django.utils.dateparse import parse_datetime
from datetime import timedelta
from decimal import Decimal

@shared_task
def run_pipeline_task(itin_id):
    Itin   = apps.get_model('itineraries', 'Itinerary')
    Day    = apps.get_model('itineraries', 'Day')
    Flight = apps.get_model('itineraries', 'TransportOption')
    Hotel  = apps.get_model('itineraries', 'HotelOption')

    result = start_pipeline(itin_id)
    itin   = Itin.objects.get(pk=itin_id)

    # marca como gerado
    itin.generated = True
    itin.save()

    # dias
    Day.objects.filter(itinerary=itin).delete()
    for d in result.get('days', []):
        date       = d.pop('day')
        slots_data = d
        Day.objects.create(
            itinerary=itin,
            date=date,
            summary='',       # ou combine texto aqui
            slots=slots_data
        )

    # voos → TransportOption
    Flight.objects.filter(itinerary=itin).delete()
    for f in result.get('flights', []):
        # 1) converte departure_time para datetime
        dep = parse_datetime(f['departure_time'])
        # 2) extrai horas e minutos da string
        parts = f['duration'].split()
        hours = int(parts[0].rstrip('h'))
        mins  = int(parts[1].rstrip('min'))
        dur   = timedelta(hours=hours, minutes=mins)
        # 3) calcula arrival
        arr = dep + dur
        # 4) cria o registro
        Flight.objects.create(
            itinerary  = itin,
            mode       = 'flight',
            origin     = f['origin'],
            destination= f['destination'],
            departure  = dep,
            arrival    = arr,
            duration   = dur,
            price      = Decimal(str(f['price'])),
            booking_url= f.get('booking_url', None)
        )

    # hotéis → HotelOption
    Hotel.objects.filter(itinerary=itin).delete()
    for h in result.get('hotels', []):
        Hotel.objects.create(
            itinerary=itin,
            name            = h['name'],
            location        = h['location'],
            check_in        = h['check_in'],
            check_out       = h['check_out'],
            price_per_night = h['price_per_night'],
            rating          = h['rating'],
            type            = h['type'],
            platform        = h['platform']
        )

    return True
