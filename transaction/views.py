from rest_framework import viewsets, generics
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


class TransacaoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as transacoes"""

    queryset = Transacao.objects.all()

    serializer_class = TransacaoSerializer


class ListContaTransacoes(generics.ListAPIView):
    """Listando todas as transacoes de uma conta"""

    def get_queryset(self):
        queryset = Transacao.objects.filter(conta_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListContaTransacoesSerializer
