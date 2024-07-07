from django.contrib import admin

from home import models

# Register your models here.

class VestibularInline(admin.TabularInline):
    model = models.Vestibular.livros.through
    extra = 1

class LivroAdmin(admin.ModelAdmin):
    inlines = [
        VestibularInline,
    ]
    class Meta:
        model = models.Livro

admin.site.register(models.Universidade)
admin.site.register(models.Vestibular)
admin.site.register(models.Categoria)
admin.site.register(models.Livro, LivroAdmin)
