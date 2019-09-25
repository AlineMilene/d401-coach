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

        args = {
            'sucesso': 'Você conseguiu campeão! Grite: Alucinação'
        }
        return render(request, 'index.html', args) 
    return render(request, 'index.html') 
