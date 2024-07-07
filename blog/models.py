from ckeditor.fields import RichTextField
from django.db import models
from datetime import datetime
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

from contas.models import Perfil


# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    resumo = RichTextField(null=True, blank=True)
    conteudo = RichTextUploadingField(null=True, blank=True)
    imagem_post = models.ImageField(null=True, blank=True, upload_to='static/blog/')
    data_publicacao = models.DateTimeField(timezone.now())
    tempo_leitura = models.CharField(max_length=2, default=30)

    def __str__(self):
        return self.titulo

class Tag(models.Model):
    nome = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.nome


class Assunto(models.Model):
    nome = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.nome