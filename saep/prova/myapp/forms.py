from django.forms import ModelForm
from django import forms
from myapp.models import Usuario

class UsersForm(ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Usuario',
        'maxlength':'30'
        }))

    nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'nome',
        'maxlength':'30'
        }))

    senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Senha',
        'maxlength':'30'
        }))

    confirmar_senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'confirmar_senha',
        'maxlength':'30'
        }))

    sobrenome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'sobrenome',
        'maxlength':'30'
        }))

    telefone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'telefone',
        'maxlength':'30'
        }))

    class Meta:
        model =  Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha', 'nome', 'sobrenome', 'telefone', 'confirmar_senha']

class LoginForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha']
