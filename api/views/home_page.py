from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import CountrySerializer
from country.models import Country
from country.services import CountryService


class HomePage(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(detail=False, methods=['get'], url_path='page')
    def home_page(self, request, *args, **kwargs):
        print("Queryset:", self.get_queryset())
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create-country')
    def createCountry(self, request, *args, **kwargs):
        print("Creating a new country")
        country = CountryService().save(Country.CountryNames.SPAIN)
        serializer = self.get_serializer(country)
        return Response({"success": f"Country {country.name} saved successfully!", "data": serializer.data})
