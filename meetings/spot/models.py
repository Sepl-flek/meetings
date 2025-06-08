from django.db import models

from user.models import Profile


# later add geoDjango

class Spot(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    sport_types = models.CharField(max_length=30)
    verified = models.BooleanField(default=False)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name}: {self.address}"


class Event(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    place = models.ForeignKey(Spot, on_delete=models.CASCADE, related_name='event')
    scheduled_data_time = models.DateTimeField()
    max_players = models.PositiveIntegerField()
    current_players = models.PositiveIntegerField(default=1)
    description = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    created_data_time = models.DateTimeField(auto_now_add=True)
    edit_data_time = models.DateTimeField(auto_now=True)


class Participation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
