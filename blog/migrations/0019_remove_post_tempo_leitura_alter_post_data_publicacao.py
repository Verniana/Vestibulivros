# Generated by Django 5.0.6 on 2024-06-30 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tempo_leitura',
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 30, 22, 44, 32, 458139, tzinfo=datetime.timezone.utc)),
        ),
    ]
