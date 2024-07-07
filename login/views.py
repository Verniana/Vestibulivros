from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.


#### Função responsável por autenticar e realizar o login ####
def processa_login(request, massages=None):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {
                'username': username,
                'password': password
            }
            messages.add_message(request=request, message="Nome do usuário ou senha incorretos!", level=messages.ERROR)
            return render(request, 'login/login.html', context)

    return render(request, 'login/login.html')


#### Função responsável pelo logout ####
def processa_logout(request):

    #### Remove mensagens ao fazer logout ####
    storage = messages.get_messages(request)

    for message in storage:
        pass

    logout(request)
    return redirect('login')


#### Função responsável por redirecionar o usuário para a home ####
def processa_redirect_home(request):
    return redirect('home')


