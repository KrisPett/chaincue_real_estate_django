from abc import ABC, abstractmethod

from utilities.aws_s3_urls import AwsS3Urls
from .models import House, HouseImage
from django.core.exceptions import ObjectDoesNotExist

class HouseImageServiceI(ABC):
    @abstractmethod
    def save(self, url: str) -> HouseImage:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> HouseImage:
        pass

    @abstractmethod
    def find_all(self) -> list:
        pass


class HouseImageService(HouseImageServiceI):
    @staticmethod
    def save(url: str) -> HouseImage:
        house_image = HouseImage.create(url)
        house_image.save()
        return house_image

    @staticmethod
    def find_by_id(id: str) -> HouseImage:
        try:
            return HouseImage.objects.get(id=id)
        except ObjectDoesNotExist:
            return {"error": f"HouseImage with id {id} not found"}

    @staticmethod
    def find_all() -> list:
        return list(HouseImage.objects.all())
        
        
class HouseServiceI(ABC):
    @abstractmethod
    def save(self, house_types: str) -> House:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> House:
        pass

    @abstractmethod
    def find_all(self) -> list:
        pass


class HouseService(HouseServiceI):
    @staticmethod
    def save(house_types: str) -> House:
        house = House.create(house_types, AwsS3Urls.URLFrontImage1)
        house.save()
        return house

    @staticmethod
    def find_by_id(id: str) -> House:
        try:
            return House.objects.get(id=id)
        except ObjectDoesNotExist:
            return {"error": f"House with id {id} not found"}

    @staticmethod
    def find_all() -> list:
        return list(House.objects.all())
