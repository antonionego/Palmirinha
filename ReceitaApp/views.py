from django.shortcuts import render
from ReceitaApp.models import Receita

# Create your views here.
def index(request):
    #ações da minha view

    return render(request, 'index.html')

def receitas(request):
    lista_receitas = Receita.objects.all()
    context = {
        'receitas': lista_receitas,
        
    }
    return render(request, 'receitas.html', context)

def detalhes_receita(request, id):
    #busca a receita pelo id informado
    receita = Receita.objects.get(id=id)

    context = {
        'receita': receita
    }
    return render(request, 'receita.html', context)
    
