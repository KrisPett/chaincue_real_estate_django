from abc import ABC, abstractmethod
from .models import Country, CountryNames

class CountryServiceI(ABC):
    @abstractmethod
    def save(self, country_name):
        pass

    @abstractmethod
    def find_all(self):
        pass

class CountryService(CountryServiceI):
    def save(self, country_name):
        country = Country.create(CountryNames[country_name])
        return country

    def find_all(self):
        return list(Country.objects.all())