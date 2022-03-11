from rest_framework import serializers

from transaction.models import Conta, Transacao

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id', 'titular', 'saldo', 'data_abertura']


class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = '__all__'

class ListContaTransacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = '__all__'