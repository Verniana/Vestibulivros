# Generated by Django 5.0.6 on 2024-06-30 21:09

import ckeditor_uploader.fields
import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 30, 21, 9, 3, 650998, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]
