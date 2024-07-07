from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.contas, name="contas"),
    path('htmx_valida_username', views.htmx_valida_username, name="htmx_valida_username"),
    path('htmx_valida_senha', views.htmx_valida_senha, name="htmx_valida_senha"),
    path('htmx_valida_email', views.htmx_valida_email, name="htmx_valida_email"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

