from django.urls import path
from rest_framework.routers import SimpleRouter

from spot.views import EventViewSet, SingleEventParticipationViewSet, SpotNearViewSet, VerifiedSpotViewSet, \
    ActualEventViewSet

router = SimpleRouter()
router.register(r'api/spots', VerifiedSpotViewSet, basename='spots')
router.register(r'api/near/spots', SpotNearViewSet, basename='spots-near')
router.register(r'api/all_events', EventViewSet, basename='events-all')
router.register(r'api/actual_events', ActualEventViewSet, basename='events-actual')
router.register(r'api/events/(?P<event_id>\d+)/information', SingleEventParticipationViewSet, basename='participation')

urlpatterns = []
urlpatterns += router.urls
