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

    # saldo_final = serializers.SerializerMethodField("_get_saldo_final")
    data = serializers.DateField(
        format("%d/%m/%Y"), input_formats=["%d/%m/%Y", "iso-8601"]
    )
    titular = serializers.ReadOnlyField(source="conta.titular")

    # saldo_inicial = serializers.HiddenField(default=0) 
    # saldo_final = serializers.HiddenField(default=0) 
    class Meta:
        model = Transacao
        fields = [
            "id",
            "discriminacao",
            "valor",
            "data",
            "conta",
            "saldo_inicial",
            "saldo_final",
            "titular",
            # "saldo_em_conta",
            "tipo",
        ]

        #read_only_fields = ('saldo_inicial', 'saldo_final',)
        #read_only_fields = ["saldo_inicial"]
        #extra_kwargs = {"saldo_final": {"write_only": True} }
        # extra_kwargs = {"saldo_inicial": {"write_only": True}}

    def get_tipo(self, obj):
        return obj.get_tipo_display()

    # def validate(self, data):
    #     return validate_transaction(data)


class ListContaTransacoesSerializer(serializers.ModelSerializer):
    tipo = serializers.SerializerMethodField()
    data = serializers.DateField(
        format("%d/%m/%Y"), input_formats=["%d/%m/%Y", "iso-8601"]
    )
    saldo_em_conta = serializers.ReadOnlyField(source="conta.saldo")
    titular = serializers.ReadOnlyField(source="conta.titular")
    saldo_inicial = serializers.ReadOnlyField(source="conta.saldo")

    class Meta:
        model = Transacao
        fields = [
            "id",
            "discriminacao",
            "valor",
            "saldo_inicial",
            "saldo_final",
            "data",
            "conta",
            "saldo_em_conta",
            "titular",
            "tipo",
        ]

    def get_tipo(self, obj):
        return obj.get_tipo_display()
