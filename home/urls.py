from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('livros/<int:livro_id>/book_detail', views.book_detail, name="book_detail"),
    path('vestibulares/<int:vestibular_id>/vestibular', views.vestibular, name="vestibular"),
    path('induce-error/', views.induce_error),
]