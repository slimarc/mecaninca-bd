from django.contrib import admin
from mecanica.models import Cliente, Veiculo, Servico, Mecanico, AgendamentoServico, OrdemDeServico, HistoricoManutencao

class Clientes(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'telefone', 'cep')
    list_display_links = ('cpf', 'nome')
    search_fields = ('cpf',)
    list_per_page = 20

class Veiculos(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'ano_veiculo', 'cliente')
    list_display_links = ('placa', 'cliente')
    search_fields = ('placa',)
    list_per_page = 20

class Servicos(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'valor')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 20

class Mecanicos(admin.ModelAdmin):
    list_display = ('identificacao', 'nome', 'especialidade','telefone')
    list_display_links = ('identificacao', 'nome')
    search_fields = ('especialidade',)
    list_per_page = 20

class AgendamentosServico(admin.ModelAdmin):
    list_display = ('numero_agendamento', 'veiculo', 'data_agendamento', 'data_previsao')
    list_display_links = ('numero_agendamento', 'veiculo')
    search_fields = ('numero_agendamento',)
    list_per_page = 20

class OrdensDeServico(admin.ModelAdmin):
    list_display = ('numero_ordem', 'mecanico', 'servico_nome', 'veiculo_placa', 'data')
    list_display_links = ('numero_ordem','mecanico',)
    search_fields = ('numero_ordem', 'servico__nome', 'veiculo__placa','mecanico')
    list_per_page = 20

    def servico_nome(self, obj):
        return ', '.join([servico.nome for servico in obj.servico.all()])

    def veiculo_placa(self, obj):
        return obj.veiculo.placa if obj.veiculo else ''

    servico_nome.short_description = 'Serviço'
    veiculo_placa.short_description = 'Veículo'

class HistoricosManutencao(admin.ModelAdmin):
    list_display = ('id', 'veiculo_placa', 'ordem_de_servico_numero')
    search_fields = ('veiculo__placa',)  
    list_per_page = 20

    def veiculo_placa(self, obj):
        return obj.veiculo.placa if obj.veiculo else ''

    def ordem_de_servico_numero(self, obj):
        return obj.ordem_de_servico.numero if obj.ordem_de_servico else ''

    veiculo_placa.short_description = 'Veículo' 
    ordem_de_servico_numero.short_description = 'Ordem de Serviço'  

admin.site.register(Cliente, Clientes)
admin.site.register(Veiculo, Veiculos)
admin.site.register(Servico, Servicos)
admin.site.register(Mecanico, Mecanicos)
admin.site.register(AgendamentoServico, AgendamentosServico)
admin.site.register(OrdemDeServico, OrdensDeServico)
admin.site.register(HistoricoManutencao, HistoricosManutencao)

