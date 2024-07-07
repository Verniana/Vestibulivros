from django.http import HttpResponse
from django.shortcuts import render

from quiz.models import Pergunta


# Create your views here.

#### FUNÇÃO ACESSA AS PERGUNTAS DO QUIZ DE FORMA ALEATÓRIA ####
def quiz(request):
    pergunta = Pergunta.objects.order_by("?").first()
    context = {
        'pergunta': pergunta
    }
    return render(request, 'quiz/quiz.html', context)


#### FUNÇÃO QUE RETORNA O FEEDBACK DA RESPOSTA DADA PELO USUÁRIO ####
def resposta(request):

    resposta = request.POST.get('resposta')

    if resposta == 'True':
        return HttpResponse("<p style='color:green'> Resposta Correta! </p>")
    elif resposta == 'False':
        return HttpResponse("<p style='color:red'> Resposta Incorreta. </p>")
    else:
        return HttpResponse("<p style='color:orange'> Selecione uma alternativa. </p>")