from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone

# Create your models here.
class Universidade(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    sinopse = RichTextField(null=True, blank=True)
    ano_publicacao = models.PositiveIntegerField()
    editora = models.CharField(max_length=200)
    capa = models.ImageField(null=True, blank=True, upload_to='static/blog/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='livros')
    link_spotify = models.URLField(null=True, blank=True)
    link_amazon = models.URLField(null=True, blank=True)
    link_pdf = models.URLField(null=True, blank=True)
    resenha = RichTextField(null=True, blank=True)
    paginas = models.CharField(max_length=5, default=30)

    def __str__(self):
        return self.titulo

class Vestibular(models.Model):
    nome = models.CharField(max_length=200)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE, related_name='vestibulares')
    data = models.DateField()
    livros = models.ManyToManyField(Livro)

    class Meta:
        unique_together = ('nome', 'universidade')

    def __str__(self):
        return self.nome