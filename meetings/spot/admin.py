from django.contrib import admin

from spot.models import Spot, Event, Participation

# Register your models here.

admin.site.register(Spot)
admin.site.register(Event)
admin.site.register(Participation)
