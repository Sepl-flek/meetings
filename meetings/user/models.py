from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Clients(models.Model):
    STATUS_CHOICE = (
        ('beginner', 'Новичок'),
        ('active', 'Активный'),
        ('experienced', 'Опытный'),
        ('oldtimer', 'Ветеран'),
        ('legend', 'Легенда'),
    )

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    information = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=STATUS_CHOICE, default='beginner')
