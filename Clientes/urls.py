from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('novo/', views.formulario_cliente, name='novo_cliente'),
    path('criar/', views.cadastrar_cliente, name='cadastrar_cliente'),
]