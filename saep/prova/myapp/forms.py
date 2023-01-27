from django.forms import ModelForm
from django import forms
from myapp.models import Usuario, Agendamento, Servicos

class LoginForm(ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'id': 'usuario'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'id':'senha'}))
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha']

# Create the form class.
class UsersForm(ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)', 'id': 'username' }))
    nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)', 'id':'name'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'maxlength': '14', 'id':'password'}))
    confirmar_senha = forms.CharField(widget=forms.PasswordInput(attrs={'maxlength': '14', 'id':'password-confirmation'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_cel(event)', 'maxlength': '30', 'id':'email'}))
    data_nasc = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'id':'data'}))
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'nome', 'senha', 'confirmar_senha', 'email', 'data_nasc']



TIME_CHOICES = [
    ("", ""),
    ("08:00 às 09:00", "08:00 às 09:00"),
    ("09:00 às 10:00", "09:00 às 10:00"),
    ("10:00 às 11:00", "10:00 às 11:00"),
    ("11:00 às 12:00", "11:00 às 12:00"),
    ("13:00 às 14:00", "13:00 às 14:00"),
    ("14:00 às 15:00", "14:00 às 15:00"),
    ("15:00 às 16:00", "15:00 às 16:00"),
    ("16:00 às 17:00", "16:00 às 17:00"),
    ("17:00 às 18:00", "17:00 às 18:00"),
    ("18:00 às 19:00", "18:00 às 19:00"),
]

FUNCIONARIO_CHOICES = [
    ("gregorio","gregorio"),
    ("jose", "jose"),
    ("gabriela", "gabriela"),
    ("laura", "laura"),
]

SERVICO_CHOICES = [
    ("1 cabelo", "1 cabelo"),
    ("2 maquiagem", "2 maquiagem"),
    ("3 estetica", "3 estetica"),
    ("4 manicure", "4 manicure"),
]

class AgendamentoForm(ModelForm):
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    horario = forms.ChoiceField(choices = TIME_CHOICES,)
    nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    endereco = forms.EmailField(widget=forms.TextInput())
    funcionario = forms.ChoiceField(choices = FUNCIONARIO_CHOICES)
    Servico = forms.ChoiceField(choices = SERVICO_CHOICES)


    class Meta:
        model = Agendamento

        fields = [ 
            'nome',  
            'endereco', 
            'funcionario', 
            'servico',
            'data',
            'horario'
            ]

class ServicosForm(ModelForm):
    servico = forms.CharField() 
    valor = forms.IntegerField()
    class Meta:
        model = Servicos
        fields = ['servico', 'valor']