# Generated by Django 3.0.7 on 2020-07-01 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nask', '0006_task_headline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='headline',
            field=models.CharField(default='', max_length=100),
        ),
    ]