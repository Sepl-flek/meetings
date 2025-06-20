# Generated by Django 5.2.2 on 2025-06-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0002_rename_user_participation_profile_alter_event_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spot',
            old_name='sport_types',
            new_name='sport_type',
        ),
        migrations.AlterField(
            model_name='event',
            name='current_players',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
