from django.contrib import admin
from mecanica.models import Cliente, Veiculo, Servico, Mecanico, AgendamentoServico, OrdemDeServico, Peca, \
    PecaQuantidade, OrdemDeCompra, Fornecedor


class ClientesAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'telefone', 'cep')
    list_display_links = ('cpf', 'nome')
    search_fields = ('cpf', 'nome')
    list_per_page = 20


class VeiculosAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'ano_veiculo', 'cliente')
    list_display_links = ('placa', 'cliente')
    search_fields = ('placa',)
    list_per_page = 20


class ServicosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'valor')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 20


class MecanicosAdmin(admin.ModelAdmin):
    list_display = ('identificacao', 'nome', 'especialidade','telefone')
    list_display_links = ('identificacao', 'nome')
    search_fields = ('especialidade', 'identificacao',)
    list_per_page = 20


class AgendamentosServicoAdmin(admin.ModelAdmin):
    list_display = ('numero_agendamento', 'veiculo', 'data_previsao_entrada', 'data_previsao_saida')
    list_display_links = ('numero_agendamento', 'veiculo')
    search_fields = ('numero_agendamento',)
    list_per_page = 20


class OrdensDeServicoAdmin(admin.ModelAdmin):
    list_display = ('numero_ordem', 'mecanico', 'servico_nome', 'veiculo_placa', 'data')
    list_display_links = ('numero_ordem', 'mecanico',)
    search_fields = ('numero_ordem', 'servico__nome', 'veiculo__placa', 'mecanico')
    list_per_page = 20

    def servico_nome(self, obj):
        return ', '.join([servico.nome for servico in obj.servico.all()])

    def veiculo_placa(self, obj):
        return obj.veiculo.placa if obj.veiculo else ''

    servico_nome.short_description = 'Serviço'
    veiculo_placa.short_description = 'Veículo'


class PecaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 20


class PecaQuantidadeAdmin(admin.ModelAdmin):
    list_display = ('peca', 'quantidade')
    list_display_links = ('peca',)
    search_fields = ('peca__nome',)
    list_per_page = 20


class OrdemDeCompraAdmin(admin.ModelAdmin):
    list_display = ('data_pedido', 'data_entrega', 'peca_quantidade_list')
    readonly_fields = ('peca_quantidade_list',)
    list_display_links = ('data_pedido', 'data_entrega')
    search_fields = ('peca_quantidade__peca__nome', 'fornecedor',)
    list_per_page = 20

    def peca_quantidade_list(self, obj):
        return ", ".join([str(pq) for pq in obj.peca_quantidade.all()])

    peca_quantidade_list.short_description = 'Pecas Quantidade'


class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'cep', 'telefone')
    list_display_links = ('nome', 'cnpj')
    search_fields = ('nome', 'cnpj',)
    list_per_page = 20


admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Veiculo, VeiculosAdmin)
admin.site.register(Servico, ServicosAdmin)
admin.site.register(Mecanico, MecanicosAdmin)
admin.site.register(AgendamentoServico, AgendamentosServicoAdmin)
admin.site.register(OrdemDeServico, OrdensDeServicoAdmin)
admin.site.register(Peca, PecaAdmin)
admin.site.register(PecaQuantidade, PecaQuantidadeAdmin)
admin.site.register(OrdemDeCompra, OrdemDeCompraAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)

