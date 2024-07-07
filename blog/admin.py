from django.contrib import admin
from . import models
# Register your models here.

class TagInline(admin.TabularInline):
    model = models.Tag.posts.through
    extra = 1

class AssuntoInline(admin.TabularInline):
    model = models.Assunto.posts.through
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
        AssuntoInline,
    ]
    class Meta:
        model = models.Post

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Assunto)
