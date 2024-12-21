from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import CountrySerializer
from country.models import Country


class HousePage(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(detail=False, methods=['get'], url_path='page')
    def house_page(self, request, *args, **kwargs):
        print("house_page:", self.get_queryset())
        return Response("House Page")
