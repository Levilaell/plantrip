from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.itineraries.views import ItineraryViewSet

router = routers.DefaultRouter()
router.register(r'itineraries', ItineraryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]