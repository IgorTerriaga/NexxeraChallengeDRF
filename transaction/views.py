from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from transaction.models import Conta, Transacao
from transaction.serializer import (
    ContaSerializer,
    TransacaoSerializer,
    ListContaTransacoesSerializer,
)


class ContaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as contas"""

    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    OrderingFilter=['titular']
    search_fields = ['tiular', 'data_abertura']


class TransacaoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as transacoes"""

    queryset = Transacao.objects.all()

    serializer_class = TransacaoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    OrderingFilter=['data']
    search_fields = ['tipo', 'data']
    filterset_fields=['data']
    


class ListContaTransacoes(generics.ListAPIView):
    """Listando todas as transacoes de uma conta"""

    def get_queryset(self):
        queryset = Transacao.objects.filter(conta_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListContaTransacoesSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    OrderingFilter=['data']
    search_fields = ['tipo', 'data']
