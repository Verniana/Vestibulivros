from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',
         views.processa_login,
         name="login"),

    path('processa_logout',
         views.processa_logout,
         name="logout"),

    path('processa_redirect_home',
         views.processa_redirect_home,
         name="ir_home"),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name="login/password_reset_form.html"),
         name="password_reset"),

    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="login/password_reset_confirm.html"),
         name="password_reset_confirm"),

    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name="login/password_reset_done.html"),
         name="password_reset_done"),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="login/password_reset_complete.html"),
         name="password_reset_complete")
]

#<uidb64> é a codificação do ID do usuário usando a base 64