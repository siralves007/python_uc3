from django.shortcuts import render, redirect
from .models import Produto

def lista_produtos(request):
    try:
        produtos = Produto.objects.all()
        return render(request, 'produtos.html', {'produtos': produtos})
    except:
        return render(request, 'produtos.html', {'produtos': []})

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        Produto.objects.create(nome=nome, preco=preco)
    return redirect('lista_produtos')