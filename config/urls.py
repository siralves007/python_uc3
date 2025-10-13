from django.contrib import admin
from django.urls import path, include
from app import views  # 👈 importa as views do app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_produtos, name='lista_produtos'),
    path('app/', include('app.urls')),
]