from rest_framework import serializers
from .models import Itinerary, Day, TransportOption, HotelOption

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Day
        fields = ['date', 'summary', 'slots']

class TransportOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TransportOption
        fields = [
            'mode', 'origin', 'destination',
            'departure', 'arrival',
            'duration', 'price', 'booking_url'
        ]

class HotelOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = HotelOption
        fields = [
            'name', 'location',
            'check_in', 'check_out',
            'price_per_night', 'rating',
            'type', 'platform'
        ]

class ItinerarySerializer(serializers.ModelSerializer):
    days       = DaySerializer(many=True, read_only=True)
    transports = TransportOptionSerializer(many=True, read_only=True)
    hotels     = HotelOptionSerializer(many=True, read_only=True)

    class Meta:
        model  = Itinerary
        fields = [
            'id', 'destination', 'start_date', 'end_date', 'budget',
            'generated', 'created_at',
            'days', 'transports', 'hotels',
        ]
        read_only_fields = [
            'id', 'generated', 'created_at',
            'days', 'transports', 'hotels'
        ]
