# Generated by Django 2.2.1 on 2019-05-19 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]