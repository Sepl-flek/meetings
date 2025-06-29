from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from spot.models import Spot, Event, Participation


class SpotSerializer(ModelSerializer):
    class Meta:
        model = Spot
        fields = ('name', 'description', 'address', 'sport_type', 'verified')


class SpotWithDistanceSerializer(ModelSerializer):
    distance = serializers.FloatField()

    class Meta:
        model = Spot
        fields = ['id', 'name', 'description', 'address', 'sport_type', 'verified',
                  'latitude', 'longitude', 'distance']


class EventSerializer(ModelSerializer):
    place = SpotSerializer()

    class Meta:
        model = Event
        fields = ('place', 'scheduled_data_time', 'current_players', 'max_players', 'description')


class ParticipationSerializer(ModelSerializer):
    profile_name = serializers.CharField(source='profile.user.username')
    user_id = serializers.IntegerField(source='profile.user.id')

    class Meta:
        model = Participation
        fields = ('joined_at', 'profile_name', 'user_id')
