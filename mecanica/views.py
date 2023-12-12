from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, status
from django.contrib import messages
from rest_framework.response import Response
from .models import Cliente, Veiculo, Servico, Mecanico, AgendamentoServico, OrdemDeServico, Peca, PecaQuantidade, \
    OrdemDeCompra, Fornecedor
from .serializers import ClienteSerializer, VeiculoSerializer, ServicoSerializer, MecanicoSerializer, \
    AgendamentoServicoSerializer, OrdemDeServicoSerializer, PecaSerializer, PecaQuantidadeSerializer, \
    OrdemDeCompraSerializer, FornecedorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['cpf', 'nome']
    filterset_fields = ['cpf']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def veiculos_por_cliente(self, cpf):
        cliente = get_object_or_404(Cliente, cpf=cpf)
        veiculos = Veiculo.objects.filter(cliente=cliente)
        veiculos_json = [{
            'placa': veiculo.placa if veiculo.placa else None,
            'modelo': veiculo.modelo if veiculo.modelo else None,
            'ano_veiculo': veiculo.ano_veiculo if veiculo.ano_veiculo else None
        }
            for veiculo in veiculos]
        return JsonResponse({'cliente': cliente.nome, 'veiculos': veiculos_json})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"detail": f"Cliente {instance} foi deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['placa']
    filterset_fields = ['ano_veiculo', 'modelo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"detail": f"Veículo {instance} foi deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"detail": f"Serviço {instance} foi deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)


class MecanicoViewSet(viewsets.ModelViewSet):
    queryset = Mecanico.objects.all()
    serializer_class = MecanicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['identificacao']
    filterset_fields = ['especialidade']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"detail": f"Mecânico {instance} foi deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)

class AgendamentoServicoViewSet(viewsets.ModelViewSet):
    queryset = AgendamentoServico.objects.all()
    serializer_class = AgendamentoServicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['numero_agendamento']
    filterset_fields = ['veiculo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"detail": f"Agendamento {instance} foi deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)

class OrdemDeServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemDeServico.objects.all()
    serializer_class = OrdemDeServicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['numero_ordem', 'mecanico']
    filterset_fields = ['veiculo', 'mecanico']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"detail": f"Ordem de serviço {instance} foi deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)

def historico_do_veiculo(request, placa):
    veiculo = get_object_or_404(Veiculo, placa=placa)
    ordens = OrdemDeServico.objects.filter(veiculo=veiculo)
    ordens_json = [{
                    'numero_ordem': ordem.numero_ordem if ordem.numero_ordem else None,
                    'data': ordem.data if ordem.data else None,
                    'veiculo': ordem.veiculo.placa if ordem.veiculo else None,
                    'mecanico': ordem.mecanico.nome if ordem.mecanico else None,
                    "servico": [
                        {
                            'nome': servico.nome if servico.nome else None,
                            'descricao': servico.descricao if servico.descricao else None,
                            'valor': float(servico.valor) if servico.valor else None
                        } for servico in ordem.servico.all()
                    ]
                   } for ordem in ordens]
    return JsonResponse({'veiculo': veiculo.placa, 'ordens': ordens_json})


class PecaViewSet(viewsets.ModelViewSet):
    queryset = Peca.objects.all()
    serializer_class = PecaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    filterset_fields = ['preco', 'estoque']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"detail": f"Peça {instance} foi deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)

class PecaQuantidadeViewSet(viewsets.ModelViewSet):
    queryset = PecaQuantidade.objects.all()
    serializer_class = PecaQuantidadeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['peca']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"detail": f" Quantidade de peças {instance} deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)

class OrdemDeCompraViewSet(viewsets.ModelViewSet):
    queryset = OrdemDeCompra.objects.all()
    serializer_class = OrdemDeCompraSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['fornecedor']
    filterset_fields = ['data_pedido', 'data_entrega']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"detail": f"Ordem de compra {instance} foi deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome', 'cnpj']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"detail": f"Fornecedor {instance} foi deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)