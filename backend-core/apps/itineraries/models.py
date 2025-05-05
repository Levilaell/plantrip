from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    destination = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    generated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)  

    def __str__(self):
        return f"{self.destination} ({self.start_date} → {self.end_date})"

class Day(models.Model):
    itinerary = models.ForeignKey(Itinerary, related_name='days', on_delete=models.CASCADE)
    date      = models.DateField()
    summary   = models.TextField(null=True, blank=True)
    slots     = models.JSONField(null=True, blank=True, help_text="morning/afternoon/weather/etc")

    def __str__(self):
        return f"{self.itinerary} – {self.date}"


class TransportOption(models.Model):
    itinerary = models.ForeignKey(Itinerary, related_name='transports', on_delete=models.CASCADE)
    mode = models.CharField(max_length=50)           # ex: 'flight', 'train'
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    duration = models.DurationField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    booking_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.mode.title()} {self.origin} → {self.destination}"


class HotelOption(models.Model):
    itinerary       = models.ForeignKey(Itinerary, related_name='hotels', on_delete=models.CASCADE)
    name            = models.CharField(max_length=255)
    location        = models.CharField(max_length=255)
    check_in        = models.DateField()
    check_out       = models.DateField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    rating          = models.FloatField()
    type            = models.CharField(max_length=100)
    platform        = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.location}) via {self.platform}"

