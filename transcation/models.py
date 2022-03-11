from django.db import models


class Conta(models.Model):
    titular = models.CharField(max_length=43)
    saldo = models.FloatField(default=0)
    data_abertura = models.DateField()

    def __str__(self):
        return self.titular


class Transacao(models.Model):
    TIPO = ("C", "Credito"), ("D", "Debito")
    discriminacao = models.CharField(max_length=100)
    valor = models.FloatField()
    data = models.DateField()
    status = models.CharField(max_length=12)
    saldo_inicial = models.FloatField()
    saldo_final = models.FloatField()
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False, null=False)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)

    def __str__(self):
        return self.discriminacao
