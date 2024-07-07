from django.contrib import admin

from quiz.models import Alternativas, Pergunta


# Register your models here.

class Alternativa_(admin.TabularInline):
    model = Alternativas

class QuestaoAdm(admin.ModelAdmin):
    inlines = [
        Alternativa_
    ]
    class Meta:
        model = Pergunta

admin.site.register(Pergunta, QuestaoAdm)
admin.site.register(Alternativas)