from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from spot.models import Spot, Event
from spot.serializers import SpotSerializer, EventSerializer


# Create your views here.

class SpotViewSet(ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all().prefetch_related('place')
