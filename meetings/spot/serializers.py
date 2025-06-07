from rest_framework.serializers import ModelSerializer

from spot.models import Spot, Event


class SpotSerializer(ModelSerializer):
    class Meta:
        model = Spot
        fields = ('name', 'description', 'address', 'sport_types',)


class EventSerializer(ModelSerializer):
    place = SpotSerializer()

    class Meta:
        model = Event
        fields = ('place', 'scheduled_data_time', 'current_players', 'max_players', 'description')
