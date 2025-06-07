from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    STATUS_CHOICE = (
        ('beginner', 'Новичок'),
        ('active', 'Активный'),
        ('experienced', 'Опытный'),
        ('oldtimer', 'Ветеран'),
        ('legend', 'Легенда'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    information = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=15, choices=STATUS_CHOICE, default='beginner')
    feedbacks = models.ManyToManyField('self', through_fields=('user', 'author'),
                                       symmetrical=False, through='FeedBack')

    def __str__(self):
        return f"Профиль {self.user.username}"


class FeedBack(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='authored_feedbacks')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='feedbacks_received')
    feedback = models.CharField(max_length=255, null=True)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return f"Отзыв от {self.author} для {self.user}"

    class Meta:
        unique_together = ('author', 'user')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
