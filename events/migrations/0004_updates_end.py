# Generated by Django 3.0.7 on 2020-07-01 07:02

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20200701_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates',
            name='end',
            field=models.DateTimeField(default=events.models.weekend),
        ),
    ]