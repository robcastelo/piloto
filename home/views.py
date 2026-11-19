from django.shortcuts import render, HttpResponse

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Pagina Principal!</h1>')
    
def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return HttpResponse('Essa é a página de contato!')

def ajuda(request):
    return HttpResponse('Essa é a página de ajuda!')