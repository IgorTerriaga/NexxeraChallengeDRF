from django.contrib import admin

from transaction.models import Conta, Transacao


class Contas(admin.ModelAdmin):
    list_display = ('id', 'titular', 'saldo', 'data_abertura')
    list_display_links = ('id', 'titular')
    search_fields=('titular', )
    list_per_page = 20

admin.site.register(Conta, Contas)



class Transacoes(admin.ModelAdmin):
    list_display = ('id', 'discriminacao', 'valor','data','status','saldo_inicial','saldo_final','status','tipo', 'conta')
    list_display_links=('id', 'discriminacao')
    search_fields=('id',)

admin.site.register(Transacao, Transacoes)
