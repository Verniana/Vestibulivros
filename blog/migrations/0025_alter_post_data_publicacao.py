# Generated by Django 5.0.6 on 2024-07-02 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_post_tempo_leitura_alter_post_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 7, 2, 5, 36, 51, 57280, tzinfo=datetime.timezone.utc)),
        ),
    ]
