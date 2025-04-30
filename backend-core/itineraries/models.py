from django.db import models

# Create your models here.
class Itinerary(models.Model):
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="pending")
    generated_text = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    