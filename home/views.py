
from django.http import HttpResponse

menu = """
<nav>
    <a href="/">Principal</a> |
    <a href="/sobre/">Sobre</a> |
    <a href="/contato/">Contato</a> |
    <a href="/ajuda/">Ajuda</a>
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

def perfil(request, usuario):
    return HttpResponse(f"Perfil do usuário: {usuario}")

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