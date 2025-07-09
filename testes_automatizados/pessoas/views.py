from django.shortcuts import render
from .forms import PessoaForm

def lista_pessoas(request):
    return render(request, 'pessoas/lista.html', {'pessoas': []})

def criar_pessoa(request):
    form = PessoaForm()
    return render(request, 'pessoas/form.html', {'form': form})

def editar_pessoa(request, id):
    form = PessoaForm()
    return render(request, 'pessoas/form.html', {'form': form})

def excluir_pessoa(request, id):
    return render(request, 'pessoas/confirmar_exclusao.html', {})
