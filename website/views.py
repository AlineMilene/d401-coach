from django.shortcuts import render
from website.models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        data = Coach()
        data.nome = request.POST['nome']
        data.frase = request.POST['frase']
        data.inspirador = request.POST['inspirador']
        data.save()

        args = { ## argumento que você quer passar se o post der certo
            'sucesso': 'Você conseguiu campeão! Grite: Alucinação'
        }
        return render(request, 'index.html', args) # chamar index e depois o args
    return render(request, 'index.html') 

def listar_coachs(request):
    listar_coachs = Coach.objects.all()
    args = {
        'listar_coachs': listar_coachs
    }
    return render(request, 'listar_coachs.html', args)