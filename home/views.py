
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from django.http import JsonResponse

menu = """
<nav>
    <a href="/">Principal</a> |
    <a href="/sobre/">Sobre</a> |
    <a href="/contato/">Contato</a> |
    <a href="/ajuda/">Ajuda</a> |
    <a href="/perfil/">Perfil</a> |
    <a href="/dia_semana/">Dia da semana</a>
</nav>
"""

def index(request):
    return HttpResponse(menu + "<h1>Página Principal</h1>")

def sobre(request):
    return HttpResponse(menu + "<h1>Sobre</h1><p>Informações sobre o nosso sistema.</p>")

def contato(request):
    return HttpResponse(menu + "<h1>Contato</h1><p>Esta é a página de contato.</p>")

def ajuda(request):
    return HttpResponse(menu + "<h1>Ajuda</h1><p>Esta é a página de ajuda.</p>")

@require_GET
def perfil(request, usuario):
    # Simulando dados de um banco de dados
    dados_perfil = {
        "usuario": usuario,        
    }
    return JsonResponse(dados_perfil)

def dia_semana(request, numero):
    # Dicionário mapeando o número para o dia da semana
    dias = {
        1: "Segunda-feira",
        2: "Terça-feira",
        3: "Quarta-feira",
        4: "Quinta-feira",
        5: "Sexta-feira",
        6: "Sábado",
        7: "Domingo"
    }
    
    # Validação do parâmetro
    if numero not in dias:
        raise Http404("Número inválido. Use um inteiro de 1 a 7.")
        
    return HttpResponse(f"{dias[numero]}")