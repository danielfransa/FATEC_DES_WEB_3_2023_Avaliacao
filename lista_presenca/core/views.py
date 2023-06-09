from django.http import HttpResponse
from django.shortcuts import render

from core.models import ListaPresenca
from .forms import ListaPresencaForm

def cadastro(request):
    if request.method == 'POST':
        form = ListaPresencaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Formulário enviado com sucesso!')
    else:
        form = ListaPresencaForm()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)

def listar(request):
    presencas = ListaPresenca.objects.all()
    return render(request, 'lista.html', {'presencas': presencas})