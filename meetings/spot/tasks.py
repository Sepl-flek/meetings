from celery import shared_task
from django.db import transaction


@shared_task
def update_current_players(event_id):
    from spot.models import Event
    with transaction.atomic():
        event = Event.objects.get(id=event_id)

        event.current_players = event.current_players + 1
        event.save(update_fields=['current_players'])


@shared_task
def create_event(profile_id, event_id):
    from spot.models import Participation
    Participation.objects.create(profile_id=profile_id, event_id=event_id)
