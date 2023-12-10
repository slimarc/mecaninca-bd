"""projeto_bd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from mecanica import views
from mecanica.views import ClienteViewSet, VeiculoViewSet, ServicoViewSet, MecanicoViewSet, AgendamentoServicoViewSet, \
    OrdemDeServicoViewSet

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet, basename='clientes')
router.register('veiculos', VeiculoViewSet, basename='veiculos')
router.register('servicos', ServicoViewSet, basename='servicos')
router.register('mecanicos', MecanicoViewSet, basename='mecanicos')
router.register('agendamentos', AgendamentoServicoViewSet, basename='agendamentos')
router.register('ordens', OrdemDeServicoViewSet, basename='ordens')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('veiculos/<str:cpf>/', views.veiculos_por_cliente, name='veiculos_por_cliente'),
    path('ordens/<str:placa>/', views.historico_do_veiculo, name='historico_do_veiculo'),
    path('', include(router.urls))
]
