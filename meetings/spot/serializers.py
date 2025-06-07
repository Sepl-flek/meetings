from rest_framework.serializers import ModelSerializer

from spot.models import Spot


class SpotSerializer(ModelSerializer):
    class Meta:
        model = Spot
        fields = ('name', 'description', 'address', 'sport_types', )