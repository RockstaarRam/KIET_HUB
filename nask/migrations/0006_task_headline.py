# Generated by Django 3.0.7 on 2020-07-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nask', '0005_auto_20200629_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='headline',
            field=models.TextField(default=''),
        ),
    ]