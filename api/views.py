from rest_framework import viewsets, permissions
from api.models import FundoImobiliario
from api.serializers import FundoImobiliarioSerializer


class FundoImobiliarioViewSet(viewsets.ModelViewSet):
    queryset = FundoImobiliario.objects.all()
    serializer_class = FundoImobiliarioSerializer
    permission_classes = [permissions.IsAuthenticated]
