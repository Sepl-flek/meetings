from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from spot.models import Spot, Event, Participation
from spot.serializers import SpotSerializer, EventSerializer, ParticipationSerializer
from user.models import Profile


# Create your views here.

class SpotViewSet(ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all().prefetch_related('place')


class SingleEventParticipationViewSet(ModelViewSet):
    serializer_class = ParticipationSerializer

    def get_queryset(self):
        return Participation.objects.filter(event_id=self.kwargs.get('event_id')).select_related(
            'profile__user'
        )

