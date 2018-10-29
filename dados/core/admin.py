from django.contrib import admin
from .models import Empreendimento, Cliente, Titulo, Unidade


class EmpreendimentoAdmin(admin.ModelAdmin):
    model = Empreendimento
    list_display = ('codigo', 'nome', 'cidade', 'categoria')
    ordering = ['codigo']
    search_fields = ['codigo', 'nome']


class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ('codigo', 'nome', 'cidade')
    ordering = ['codigo']
    search_fields = ['codigo', 'nome']


class UnidadeAdmin(admin.ModelAdmin):
    model = Unidade
    list_display = ('codigo', 'tipo_imovel', 'area')
    ordering = ['codigo']
    search_fields = ['codigo']


class TituloAdmin(admin.ModelAdmin):
    model = Titulo
    list_display = ('empreendimento', 'unidade', 'cliente', 'nro_titulo', 'parcela',
                    'valor_original', 'valor_liquido', 'data_distrato')
    ordering = ['empreendimento', 'unidade', 'nro_titulo', 'parcela']
    search_fields = ['empreendimento', 'cliente', 'nro_titulo']


admin.site.register(Empreendimento, EmpreendimentoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Titulo, TituloAdmin)
admin.site.register(Unidade, UnidadeAdmin)
