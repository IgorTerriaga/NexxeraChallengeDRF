from django.db import models


class Conta(models.Model):
    titular = models.CharField(max_length=43)
    saldo = models.FloatField(default=0, null=False)
    data_abertura = models.DateField("%d-%m-%Y", null=False)

    def __str__(self):
        return self.titular

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo
        # print("qewwwwwwwwww", saldo)
        self.save()

    def get_data_abertura(self, obj):
        return obj.data_abertura.strftime("%d-%m-%Y")


class Transacao(models.Model):
    TIPO = ("C", "Credito"), ("D", "Debito")
    discriminacao = models.CharField(max_length=100, null=False, blank=False)
    valor = models.FloatField(null=False)
    saldo_inicial = models.FloatField()
    saldo_final = models.FloatField()
    data = models.DateField(format("%d-%m-%Y"), null=False, blank=False)
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False, null=False)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)

   

    def get_valor_final(self):
        return self.saldo_final


    # def save(self, *args, **kwargs):
    #     print(args)
    #     # self.saldo_final = 0
    #     # self.saldo_inicial = 0
    #     super(Transacao, self).save(*args, **kwargs)

    def set_saldo_final(self, saldo_final):
        self.saldo_final = saldo_final
        # print("qewwwwwwwwww", saldo)
        self.save()

    def __str__(self):
        return self.discriminacao

    def get_data(self, obj):
        return obj.data.strftime("%d-%m-%Y")
