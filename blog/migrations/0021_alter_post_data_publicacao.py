# Generated by Django 5.0.6 on 2024-06-30 22:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_remove_comentario_perfil_remove_comentario_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 30, 22, 47, 14, 575417, tzinfo=datetime.timezone.utc)),
        ),
    ]