from django.urls import path
from rest_framework.routers import SimpleRouter

from spot.views import SpotViewSet, EventViewSet

router = SimpleRouter()
router.register(r'api/spots', SpotViewSet, basename='spots')
router.register(r'api/events', EventViewSet, basename='events')

urlpatterns = []
urlpatterns += router.urls