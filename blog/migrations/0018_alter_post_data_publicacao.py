# Generated by Django 5.0.6 on 2024-06-30 22:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 30, 22, 43, 24, 840300, tzinfo=datetime.timezone.utc)),
        ),
    ]
