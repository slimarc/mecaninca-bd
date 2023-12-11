from django.contrib import admin
from mecanica.models import Cliente, Veiculo, Servico, Mecanico, AgendamentoServico, OrdemDeServico

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'telefone', 'cep')
    list_display_links = ('cpf', 'nome')
    search_fields = ('cpf',)
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
    search_fields = ('especialidade',)
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


admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Veiculo, VeiculosAdmin)
admin.site.register(Servico, ServicosAdmin)
admin.site.register(Mecanico, MecanicosAdmin)
admin.site.register(AgendamentoServico, AgendamentosServicoAdmin)
admin.site.register(OrdemDeServico, OrdensDeServicoAdmin)


