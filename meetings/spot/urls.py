from django.urls import path
from rest_framework.routers import SimpleRouter

from spot.views import SpotViewSet

router = SimpleRouter()
router.register(r'api/spots', SpotViewSet, basename='spots')

urlpatterns = []
urlpatterns += router.urls