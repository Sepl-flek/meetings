from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from spot.models import Spot
from spot.serializers import SpotSerializer


# Create your views here.

class SpotViewSet(ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
    