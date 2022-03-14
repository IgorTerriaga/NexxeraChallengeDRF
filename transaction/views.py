from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from transaction.models import Conta, Transacao
from transaction.serializer import (
    ContaSerializer,
    TransacaoSerializer,
    ListContaTransacoesSerializer,
)

from rest_framework.response import Response
from rest_framework import status
from django_filters import FilterSet, AllValuesFilter
from django_filters import DateTimeFilter, NumberFilter


class ContaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as contas"""

    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    OrderingFilter = ["titular"]
    search_fields = ["tiular", "data_abertura"]
    filterset_fields = {"data_abertura": ["gte", "lte", "exact"]}

    def destroy(self, request, *args, **kwargs):
        test = Conta.objects.count()
        if test == 1:
            return Response(
                "Impossível apagar! Precisamos de ao menos uma conta!!",
                status=status.HTTP_400_BAD_REQUEST,
            )

        instance = self.get_object()
        self.perform_destroy(instance)
        context = {
            "status": status.HTTP_204_NO_CONTENT,
            "errors": False,
        }
        return Response(context)


class TransacaoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as transacoes"""

    queryset = Transacao.objects.all()

    serializer_class = TransacaoSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    OrderingFilter = ["data"]
    search_fields = ["tipo", "data"]
    filterset_fields = {"data": ["gte", "lte", "exact"]}

    def create(self, request, *args, **kwargs):

        # faz com que request.data (ordereddict) seja mutavel
        setattr(request.data, "_mutable", True)

        if not request.data:
            return Response("Sem dados", status=status.HTTP_400_BAD_REQUEST)
        if not request.data["discriminacao"]:
            return Response(
                "Por favor, informe a discriminação", status=status.HTTP_400_BAD_REQUEST
            )
        if not request.data["valor"]:
            return Response(
                "Por favor, informe  o valor", status=status.HTTP_400_BAD_REQUEST
            )
        if not request.data["data"]:
            return Response(
                "Por favor, informe a data", status=status.HTTP_400_BAD_REQUEST
            )

        # pega o saldo da conta e atribui a saldo_inicial
        id_conta = request.data["conta"]
        saldo = Conta.objects.get(id=id_conta).get_saldo()

        request.data["saldo_inicial"] = saldo
        if request.data["tipo"] == "D":
            request.data["saldo_final"] = saldo - float(request.data["valor"])
        else:
            request.data["saldo_final"] = saldo + float(request.data["valor"])

        serializer = self.get_serializer(data=request.data)

        Conta.objects.get(id=id_conta).set_saldo(request.data["saldo_final"])
       

        if serializer.is_valid():
            self.perform_create(serializer)
            serializer.save()
        context = {
            "status": status.HTTP_201_CREATED,
            "errors": serializer.errors,
            "data": serializer.data,
        }
        return Response(context)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        context = {
            "status": status.HTTP_204_NO_CONTENT,
            "errors": False,
        }
        return Response(context)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(
            queryset, context={"request": request}, many=True
        )
        data = serializer.data
        context = {
            "message": "Listed Successfully",
            "count": queryset.count(),
            "errors": False,
            "data": data,
        }
        return Response(context, status=status.HTTP_200_OK)


class ListContaTransacoes(generics.ListAPIView):
    """Listando todas as transacoes de uma conta"""

    def get_queryset(self):
        queryset = Transacao.objects.filter(conta_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListContaTransacoesSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    OrderingFilter = ["data"]
    search_fields = ["tipo", "data"]
    filterset_fields = {"data": ["gte", "lte", "exact"]}
