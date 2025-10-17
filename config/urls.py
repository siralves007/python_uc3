from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import lista_produtos, cadastrar_produto
from Clientes.views import lista_clientes, cadastrar_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # URLs diretas para produtos
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('produtos/novo/', TemplateView.as_view(template_name='produtos.html'), name='novo_produto'),
    path('produtos/criar/', cadastrar_produto, name='cadastrar_produto'),

    # URLs diretas para clientes
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/novo/', TemplateView.as_view(template_name='clientes.html'), name='novo_cliente'),
    path('clientes/criar/', cadastrar_cliente, name='cadastrar_cliente'),
]