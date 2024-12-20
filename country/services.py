from abc import ABC, abstractmethod
from .models import Country


class CountryServiceI(ABC):
    @abstractmethod
    def save(self, country_name: Country.CountryNames) -> Country:
        pass

    @abstractmethod
    def find_all(self) -> list:
        pass


class CountryService(CountryServiceI):
    @staticmethod
    def save(country_name):
        country, created = Country.objects.get_or_create(name=country_name)
        return country

    def find_all(self) -> list:
        return self.country_repository.find_all()
