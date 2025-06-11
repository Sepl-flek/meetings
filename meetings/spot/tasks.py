from math import radians, sin, atan2, sqrt, cos

import httpx
from celery import shared_task
from django.db import transaction

from meetings.settings import YANDEX_API_KEY


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


@shared_task
def geocode_address(address: str):
    url = f'https://geocode-maps.yandex.ru/v1/'
    params = {
        "apikey": YANDEX_API_KEY,
        "geocode": address,
        "format": "json"
    }
    try:
        response = httpx.get(url, params=params, timeout=10)
        data = response.json()
        pos = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        lon, lat = map(float, pos.split())
        return {'latitude': lat, 'longitude': lon}

    except Exception as e:
        return {"Error": str(e)}


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # радиус Земли в км

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c
