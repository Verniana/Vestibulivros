from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Post


# Create your views here.

#### FUNÇÃO PARA CONSULTAR O BANCO DE DADOS DE ACORDO COM AS ÚLTIMAS INSERÇÕES ####
def blog(request):
    posts = Post.objects.order_by('-data_publicacao')[:5]

    context = {
        'posts': posts
    }

    return render(request, 'blog/blog.html', context)

#### FUNÇÃO PARA CONSULTAR O BANCO DE DADOS DE ACORDO COM O ID DOS POSTS ####
def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)

    context = {
        'post': post
    }

    return render(request, 'blog/post_detail.html', context)

#### FUNÇÃO PARA CONSULTAR O BANCO DE DADOS DE ACORDO COM AS ÚLTIMAS INSERÇÕES ####
def blog_posts(request):
    posts = Post.objects.order_by('-data_publicacao')[:4]

    context = {
        'posts': posts
    }

    return render(request, 'blog/blog_posts.html', context)
