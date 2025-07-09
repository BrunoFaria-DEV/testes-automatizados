from django.shortcuts import render, redirect, get_object_or_404
from pessoas.models import Pessoa
from .forms import PessoaForm

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/lista.html', {'pessoas': pessoas})

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'pessoas/form.html', {'form': form})

def editar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'pessoas/form.html', {'form': form})

def excluir_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('lista_pessoas')
    return render(request, 'pessoas/confirmar_exclusao.html', {'pessoa': pessoa})
