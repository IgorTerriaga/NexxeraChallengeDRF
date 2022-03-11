from rest_framework import serializers

from transaction.models import Conta, Transacao


class ContaSerializer(serializers.ModelSerializer):
    data_abertura = serializers.DateField(format("%d-%m-%Y"))

    class Meta:
        model = Conta
        fields = ["id", "titular", "saldo", "data_abertura"]


class TransacaoSerializer(serializers.ModelSerializer):
    data = serializers.DateField(format("%d-%m-%Y"))
    # tipo = serializers.SerializerMethodField()
    # saldo_final = serializers.FloatField(read_only=True)
    # saldo_inicial = serializers.FloatField(read_only=True)
    # conta_saldo  = serializers.FloatField(source='conta.saldo')

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
        read_only_fields = ["saldo_inicial", "saldo_final"]

    def get_tipo(self, obj):
        return obj.get_tipo_display()

    def validate(self, data):
        """Check data"""
        # print(saldo)
        # aqui precisa testar se for maior que o valor em conta tbm
        if data["tipo"] == "D" and data["valor"] < 0:
            raise serializers.ValidationError(
                {
                    "messagem": "Não é possível debitar um valor superior ao que a conta possui."
                }
            )
        if data["tipo"] == "D":
            # aqui eu pego o valor da transacao e subtraio do valor da conta
            pass
        elif data["tipo"] == "C":
            # aqui eu pego o valor da transacao e adicione ao valor da conta
            pass
        return data


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
