from django.urls import path
from rest_framework.routers import SimpleRouter

from spot.views import SpotViewSet, EventViewSet, SingleEventParticipationViewSet, SpotNearViewSet

router = SimpleRouter()
router.register(r'api/spots', SpotViewSet, basename='spots')
router.register(r'api/near', SpotNearViewSet, basename='spots-near')
router.register(r'api/events', EventViewSet, basename='events')
router.register(r'api/events/(?P<event_id>\d+)/information', SingleEventParticipationViewSet, basename='participation')

urlpatterns = []
urlpatterns += router.urls
