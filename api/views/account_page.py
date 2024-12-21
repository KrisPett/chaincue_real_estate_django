from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import CountrySerializer
from country.models import Country
from country.services import CountryService


class AccountPage(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(detail=False, methods=['get'], url_path='page')
    def account_page(self, request, *args, **kwargs):
        print("account_page:", self.get_queryset())
        return Response("Account Page")
