# apps/itineraries/views.py
from rest_framework import viewsets
from .models import Itinerary
from .serializers import ItinerarySerializer
from .tasks import run_pipeline_task
from rest_framework.permissions import IsAuthenticated


class ItineraryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer

    def perform_create(self, serializer):
        # vai criar só com campos existentes + user
        itin = serializer.save(user=self.request.user)
        run_pipeline_task.delay(itin.id)