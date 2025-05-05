# apps/itineraries/admin.py

from django.contrib import admin
from .models import Itinerary, Day, TransportOption, HotelOption

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display  = ('destination', 'start_date', 'end_date', 'user', 'budget', 'generated', 'created_at')
    list_filter   = ('generated', 'start_date', 'end_date')
    search_fields = ('destination', 'user__username')
    ordering      = ('-created_at',)

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display  = ('itinerary', 'date', 'summary')
    list_filter   = ('date',)
    search_fields = ('itinerary__destination',)

@admin.register(TransportOption)
class TransportOptionAdmin(admin.ModelAdmin):
    list_display  = ('itinerary', 'mode', 'origin', 'destination', 'departure', 'arrival', 'price')
    list_filter   = ('mode',)
    search_fields = ('origin', 'destination')

@admin.register(HotelOption)
class HotelOptionAdmin(admin.ModelAdmin):
    list_display  = ('itinerary', 'name', 'location', 'check_in', 'check_out', 'price_per_night', 'platform')
    list_filter   = ('platform', 'type')
    search_fields = ('name', 'location')
