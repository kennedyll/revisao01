from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('cadastro/',views.cadastro, name='cadastro'),
    path('docad/',views.docad, name='docad'),
    path('login/',views.login,name='login'),
    path('dolog/',views.dolog, name='dolog'),
]