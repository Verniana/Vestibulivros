from django.shortcuts import render
from .models import Livro
# Create your views here.

#### FUNÇÃO PARA ACESSAR A ENTIDADE LIVRO DE ACORDO COM O ID ####
def livros(request):
    livros = Livro.objects.order_by('-id')

    context = {
        'livros': livros,
    }

    return render(request, 'livros/livros.html', context)