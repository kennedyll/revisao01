from django.forms import ModelForm
from django import forms
from myapp.models import Usuario, Agendamento, Servicos

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

# Create the form class.
class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'maxlength': '14'}))
    celular = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_cel(event)', 'maxlength': '10'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    ultimo_nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha', 'nome', 'ultimo_nome', 'celular']



TIME_CHOICES = [
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
    ("1 people", "1 people"),
    ("2 people", "2 people"),
    ("3 people","3 people"),
    ("4 people", "4 people"),
]


# Create the form class.
class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'maxlength': '14'}))
    celular = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_cel(event)', 'maxlength': '10'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    ultimo_nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha', 'nome', 'ultimo_nome', 'celular']

class AgendamentoForm(ModelForm):
    data = forms.DateInput(attrs={'type': 'date'})
    hora = forms.ChoiceField(choices = TIME_CHOICES,)
    telefone = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_cel(event)', 'maxlength': '10'}))
    nome_completo = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    endereco = forms.EmailField(widget=forms.TextInput())
    funcionario = forms.ChoiceField(choices = FUNCIONARIO_CHOICES)
    Servico = forms.ChoiceField(choices = SERVICO_CHOICES)


    class Meta:
        model = Agendamento

        fields = [ 
            'nome_completo',  
            'numero_de_telefone', 
            'endereco', 
            'selecione_o_funcionario', 
            'selecione_o_sevico',
            'data_de_agendamento',
            'horario']

class ServicosForm(ModelForm):
    servico = forms.CharField() 
    valor = forms.IntegerField()
    class Meta:
        model = Servicos
        fields = ['servico', 'valor']