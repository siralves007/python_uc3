from django.shortcuts import render, redirect
from .models import Cliente


def lista_clientes(request):
    try:
        clientes = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes})
    except:
        return render(request, 'clientes.html', {'clientes': []})


def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')

        Cliente.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            endereco=endereco
        )
    return redirect('lista_clientes')