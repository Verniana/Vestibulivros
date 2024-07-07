from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django import forms
from contas.models import Perfil

class UserForm(ModelForm):

    #Código para tornar todos os campos do formulário obrigatórios
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['password'].required = True

    #Código para definir os nomes dos campos do formulário
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

        #Código para renomear os nomes no formulário
        labels = {
            'last_name' : 'Sobrenome',
            'username' : 'Nome de usuário'
        }

        #Código para a criação dos campos do formulário
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class PerfilForm(ModelForm):

    class Meta:
        model = Perfil
        fields = ['bio', 'foto']

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }