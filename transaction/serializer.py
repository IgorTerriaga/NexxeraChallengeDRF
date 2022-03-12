import pprint
from rest_framework import serializers
from transaction.validators import validate_transaction

from transaction.models import Conta, Transacao


class ContaSerializer(serializers.ModelSerializer):
    data_abertura = serializers.DateField(
        format("%d/%m/%Y"), input_formats=["%d/%m/%Y", "iso-8601"]
    )

    class Meta:
        model = Conta
        fields = ["id", "titular", "saldo", "data_abertura"]


class TransacaoSerializer(serializers.ModelSerializer):

    data = serializers.DateField(
        format("%d/%m/%Y"), input_formats=["%d/%m/%Y", "iso-8601"]
    )
    saldo_em_conta = serializers.SerializerMethodField(source="conta.saldo")
    titular = serializers.ReadOnlyField(source="conta.titular")
    print("----------------------", saldo_em_conta)

    # titular = serializers.ReadOnlyField(source="contas.titular")
    # print(saldo_em_conta)
    class Meta:
        model = Transacao
        fields = [
            "id",
            "discriminacao",
            "valor",
            "data",
            "conta",
            "titular",
            "saldo_em_conta",
            "tipo",
        ]

        read_only_fields = ["saldo_inicial", "saldo_final"]

    def get_tipo(self, obj):
        return obj.get_tipo_display()
    saldo_em_conta = serializers.ReadOnlyField(source="conta.saldo")
    print("dddddddddddddddddddddddddddd", saldo_em_conta)
    def validate(self, data):
        return validate_transaction(data)


class ListContaTransacoesSerializer(serializers.ModelSerializer):
    tipo = serializers.SerializerMethodField()
    data = serializers.DateField(
        format("%d/%m/%Y"), input_formats=["%d/%m/%Y", "iso-8601"]
    )

    class Meta:
        model = Transacao
        fields = [
            "id",
            "discriminacao",
            "valor",
            "data",
            "conta",
            "tipo",
        ]

    def get_tipo(self, obj):
        return obj.get_tipo_display()
