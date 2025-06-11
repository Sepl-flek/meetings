from django.db.models import F
from django.db.models.functions import ACos, Radians, Cos, Sin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from spot.models import Spot, Event, Participation
from spot.serializers import SpotSerializer, EventSerializer, ParticipationSerializer, SpotWithDistanceSerializer
from spot.tasks import geocode_address


# Create your views here.

class SpotViewSet(ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sport_type']


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all().prefetch_related('place')


class SingleEventParticipationViewSet(ModelViewSet):
    serializer_class = ParticipationSerializer

    def get_queryset(self):
        return Participation.objects.filter(event_id=self.kwargs.get('event_id')).select_related(
            'profile__user'
        )


class SpotNearViewSet(ModelViewSet):
    serializer_class = SpotWithDistanceSerializer

    def get_queryset(self):
        queryset = Spot.objects.all()
        address = self.request.query_params.get('address')
        limit = self.request.query_params.get('limit')

        try:
            limit = int(limit) if limit else None
        except ValueError:
            limit = None

        if address:
            coord = geocode_address(address)
            if not coord or 'latitude' not in coord or 'longitude' not in coord:
                return queryset.none()

            user_lat = coord['latitude']
            user_lon = coord['longitude']

            self.user_lat = user_lat
            self.user_lon = user_lon

            R = 6371

            queryset = queryset.annotate(
                distance=R * ACos(
                    Cos(Radians(user_lat)) * Cos(Radians(F('latitude'))) *
                    Cos(Radians(F('longitude')) - Radians(user_lon)) +
                    Sin(Radians(user_lat)) * Sin(Radians(F('latitude')))
                )
            ).order_by('distance')

            if limit:
                queryset = queryset[:limit]

        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user_lat'] = getattr(self, 'user_lat', None)
        context['user_lon'] = getattr(self, 'user_lon', None)
        return context
