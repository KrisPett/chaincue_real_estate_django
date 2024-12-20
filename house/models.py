from django.db import models
import uuid
from django.utils import timezone

from broker.models import Broker
import house


class HouseImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url
    
    class Meta:
        db_table = 'house_images'

    @staticmethod
    def create(url):
        return HouseImage.objects.create(
            url=url
        )


class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    number_rooms = models.IntegerField()
    beds = models.IntegerField()
    price = models.CharField(max_length=255)
    src = models.CharField(max_length=255)
    sold = models.BooleanField(default=False)
    house_types = models.CharField(max_length=50)
    images = models.ManyToManyField(HouseImage, related_name='houses', blank=True)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'houses'
        
    class HouseTypes(models.TextChoices):
        CONDOMINIUM = 'CONDOMINIUM', 'Condominium'
        VILLA = 'VILLA', 'Villa'
        TOWNHOUSE = 'TOWNHOUSE', 'Townhouse'
        VACATION_HOME = 'VACATION_HOME', 'Vacation Home'
        ESTATES_AND_FARMS = 'ESTATES_AND_FARMS', 'Estates and Farms'
        LAND = 'LAND', 'Land'
        OTHER_HOUSES = 'OTHER_HOUSES', 'Other Houses'

    @staticmethod
    def create(house_type, src):
        return House.objects.create(
            title='',
            description='',
            location='',
            number_rooms=0,
            beds=0,
            price='',
            src=src,
            sold=False,
            house_types=house_type,
            timestamp=timezone.now()
        )
