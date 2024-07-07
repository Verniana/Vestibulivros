from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz, name="quiz"),
path('quiz/resposta/', views.resposta, name='resposta'),
]