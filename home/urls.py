from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    path('dia-semana/<int:numero>/', views.dia_semana, name='dia_semana'),
]
