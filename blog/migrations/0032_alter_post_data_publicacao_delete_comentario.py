# Generated by Django 5.0.6 on 2024-07-07 03:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 7, 7, 3, 42, 24, 889899, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
