# Generated by Django 3.0.7 on 2020-07-01 06:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_updates_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
