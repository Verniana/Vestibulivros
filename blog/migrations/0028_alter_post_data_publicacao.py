# Generated by Django 5.0.6 on 2024-07-03 05:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 7, 3, 5, 18, 4, 572699, tzinfo=datetime.timezone.utc)),
        ),
    ]
