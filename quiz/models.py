from django.db import models

# Create your models here.

class Pergunta(models.Model):
    enunciado = models.TextField(max_length=300, null=False, blank=False, default='')
    figura = models.ImageField(null=False, blank=False, default='')

    def __str__ (self):
        return self.enunciado

class Alternativas(models.Model):
    texto = models.TextField(max_length=300, null=False, blank=False, default='')
    correta = models.BooleanField(default=False, null=True, blank=True)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto