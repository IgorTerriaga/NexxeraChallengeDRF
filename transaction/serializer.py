from rest_framework import serializers

from transaction.models import Conta, Transacao


class ContaSerializer(serializers.ModelSerializer):
    data_abertura = serializers.DateField(format("%d-%m-%Y"))

    class Meta:
        model = Conta
        fields = ["id", "titular", "saldo", "data_abertura"]


class TransacaoSerializer(serializers.ModelSerializer):
    data = serializers.DateField(format("%d-%m-%Y"))
    tipo = serializers.SerializerMethodField()
    class Meta:
        model = Transacao
        fields = [
            "id",
            "discriminacao",
            "valor",
            "data",
            "status",
            "saldo_inicial",
            "saldo_final",
            "conta",
            "tipo",
        ]
    def get_tipo(self, obj):
        return obj.get_tipo_display()



class ListContaTransacoesSerializer(serializers.ModelSerializer):
    tipo = serializers.SerializerMethodField()
    data = serializers.DateField(format("%d-%m-%Y"))

    class Meta:
        model = Transacao
        fields = [
            "id",
            "discriminacao",
            "valor",
            "data",
            "status",
            "saldo_inicial",
            "saldo_final",
            "conta",
            "tipo",
        ]

    def get_tipo(self, obj):
        return obj.get_tipo_display()
