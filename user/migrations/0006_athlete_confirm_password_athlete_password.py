# Generated by Django 4.2.5 on 2023-09-20 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_athlete_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='confirm_password',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='athlete',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
