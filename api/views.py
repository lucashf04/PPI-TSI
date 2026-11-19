from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, permissions
from api.models import FundoImobiliario
from api.serializers import FundoImobiliarioSerializer


class FundoImobiliarioViewSet(viewsets.ModelViewSet):
    queryset = FundoImobiliario.objects.all()
    serializer_class = FundoImobiliarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['codigo', 'setor']
    search_fields = ['codigo', 'setor']
