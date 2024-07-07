from django.shortcuts import render
from home.models import Livro, Vestibular


# Create your views here.

#### FUNÇÃO PARA ACESSAR AS ENTIDADES LIVRO E VESTIBULAR DE ACORDO COM O ID ####
def home(request):
    livros = Livro.objects.order_by('-id')[:5]
    vestibulares = Vestibular.objects.order_by('id')

    context = {
        'livros': livros,
        'vestibulares': vestibulares
    }

    return render(request, 'home/home.html', context)


#### FUNÇÃO PARA CONSULTAR A TABELA LIVRO DE ACORDO COM O ID ####
def book_detail(request, livro_id):
    livro = Livro.objects.get(pk=livro_id)

    context = {
        'livro': livro
    }

    return render(request, 'home/book_detail.html', context)


#### FUNÇÃO PARA CONSULTAR A TABELA VESTIBULAR DE ACORDO COM O ID ####
def vestibular(request, vestibular_id):
    vestibular = Vestibular.objects.get(pk=vestibular_id)

    context = {
        'vestibular': vestibular
    }

    return render(request, 'home/vestibular.html', context)


#### FUNÇÃO DE ACESSO A PÁGINA DE ERRO 404 ####
def handler404(request, exception):
    return render(request, 'error/404.html', status=404)


#### FUNÇÃO DE ACESSO A PÁGINA DE ERRO 500 ####
def handler500(request):
    return render(request, 'error/500.html', status=500)


#### FUNÇÃO PAR INDUZIR O ERRO 500 ####
def induce_error(request):
    raise Exception("Erro interno do servidor simulado!")
