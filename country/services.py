from abc import ABC, abstractmethod
from .models import Country

# class CountryServiceI(ABC):
#     @abstractmethod
#     def save(self, country_name):
#         pass
#
#     @abstractmethod
#     def find_all(self):
#         pass
#
# class CountryService(CountryServiceI):
#     def save(self, country_name):
#         country = Country.create(CountryNames[country_name])
#         return country
#
#     def find_all(self):
#         return list(Country.objects.all())



class CountryServiceI(ABC):
    @abstractmethod
    def save(self, country_name: Country.CountryNames) -> Country:
        pass

    @abstractmethod
    def find_all(self) -> list:
        pass

class CountryService(CountryServiceI):
    # def __init__(self, country_repository):
        # self.country_repository = country_repository

    @staticmethod
    def save(country_name):
        country, created = Country.objects.get_or_create(name=country_name)
        return country

    def find_all(self) -> list:
        return self.country_repository.find_all()