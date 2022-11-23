from django.shortcuts import render
# Create your views here. def home(request):

def login(request):
    return render(request,'login.html')

