# Generated by Django 5.0.6 on 2024-06-30 04:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 30, 4, 1, 58, 292322, tzinfo=datetime.timezone.utc)),
        ),
    ]