import re

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from contas.models import Perfil
from contas.usuario_form import PerfilForm, UserForm


# Create your views here.

#### Função responsável pela validação do e-mail ####
def valida_email(email):
    regex = '^(\w+)@[a-z]+(\.[a-z]+){1,2}$'

    if (re.search(regex, email)):
        return True
    else:
        return False

#### Função para a criação de usuários ####
def contas(request):
    if request.method == 'POST':
        user = UserForm(request.POST)
        perfil = PerfilForm(request.POST, request.FILES)
        if perfil.is_valid() and user.is_valid():
            usr = User.objects.create_user(
                first_name=user.cleaned_data['first_name'],
                last_name=user.cleaned_data['last_name'],
                username=user.cleaned_data['username'],
                email=user.cleaned_data['email'],
                password=user.cleaned_data['password']
            )

            perl = Perfil(bio=perfil.cleaned_data['bio'],
                          foto=perfil.cleaned_data['foto'],
                          user=usr)
            perl.save()

            return redirect('login')
        else:
            return render(request, 'contas/contas.html', { 'form': user, 'form_perfil': perfil})
    else:
        return render(request, 'contas/contas.html', {'form': UserForm(), 'form_perfil': PerfilForm()})


#### Função para a validação do username ####
def htmx_valida_username(request):
    context = {'usr_val': 'Nome de usuário já cadastrado!', 'st_submit': 'disabled', 'cor': 'red'}
    usernameParam = request.POST.get('username')

    if not User.objects.filter(username=usernameParam):
        context['usr_val'] = 'Nome de usuário disponível!'
        context['st_submit'] = ''
        context['cor'] = 'green'

    str_template = render_to_string('contas/template_valida_email.html', context)
    return HttpResponse(str_template)

#### Função para a validação da confirmação de senha ####
def htmx_valida_senha(request):
    context = {'error_pwd': 'As senhas estão diferentes!', 'st_submit': 'disabled', 'cor': 'red'}
    pwd_confirm = request.POST.get('pwd_confirm')
    password = request.POST.get('password')

    if pwd_confirm == password:
        context['error_pwd'] = ''
        context['st_submit'] = ''
        context['cor'] = ''

    str_template = render_to_string('contas/template_valida_email.html', context)
    return HttpResponse(str_template)

#### Função para a verificação se o email já foi cadastrado ####
def htmx_valida_email(request):

    context = {'usr_email': 'E-mail inválido ou já cadastrado!', 'st_submit': 'disabled', 'cor': 'red'}
    email = request.POST.get('email')

    if valida_email(email) and not User.objects.filter(email=email):
        context['usr_email'] = 'E-mail válido!'
        context['st_submit'] = ''
        context['cor'] = 'green'

    str_template = render_to_string('contas/template_valida_email.html', context)
    return HttpResponse(str_template)