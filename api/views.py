from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

from country.models import Country
from country.services import CountryService


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    # permission_classes = )[permissions.AllowAny]

    from rest_framework import viewsets
    from country.models import Country
    from country.services import CountryService


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = None

    def list(self, request):
        service = CountryService()
        countries = service.find_all()
        return Response([{'id': c.id, 'name': c.name} for c in countries])

    def create(self, request):
        service = CountryService()
        country_name = request.data.get('name')
        if country_name in [choice.name for choice in Country.CountryNames]:
            country = service.save(country_name)
            return Response({'id': country.id, 'name': country.name}, status=201)
        return Response({'error': 'Invalid country name'}, status=400)