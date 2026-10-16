from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from jogos.models import Equipe, Modalidade


# Create your views here.
def index(request):
    context = {
        "modalidades": Modalidade.objects.all(),
        "equipes": Equipe.objects.all()
    }
    return render(request, "index.html", context)

def equipe(request, id):
    context = {
        "equipe": get_object_or_404(Equipe, pk=id)
    }
    return render(request, "equipe.html", context)

def modalidade(request, id):
    context = {
        "modalidade": get_object_or_404(Modalidade, pk=id)
    }
    return render(request, "modalidade.html", context)
