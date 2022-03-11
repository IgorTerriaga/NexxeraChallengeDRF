from django.contrib import admin
from django.urls import path, include
from transcation.views import  ContaViewSet, TransacaoViewSet, ListContaTransacoes
from rest_framework import routers

router = routers.DefaultRouter()
router.register('contas', ContaViewSet, basename="Contas")
router.register('transacoes', TransacaoViewSet, basename="Transacoes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('transacoes/conta/<int:pk>', ListContaTransacoes.as_view())
]
