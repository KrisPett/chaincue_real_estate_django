from django.db.models.signals import post_migrate
from django.dispatch import receiver
from house.models import House, HouseImage
from broker.models import Broker
from country.models import Country
from utilities.aws_s3_urls import AwsS3Urls

@receiver(post_migrate)
def populate_default_data(sender, **kwargs):
    if sender.name == 'api':
        # Clear existing data
        House.objects.all().delete()
        HouseImage.objects.all().delete()
        Broker.objects.all().delete()
        Country.objects.all().delete()

        # Create default houses
        houses = [
            House.create(House.HouseTypes.VILLA, AwsS3Urls.URLFrontImage1),
            House.create(House.HouseTypes.VILLA, AwsS3Urls.URLFrontImage2),
            House.create(House.HouseTypes.VILLA, AwsS3Urls.URLFrontImage3),
            House.create(House.HouseTypes.VILLA, AwsS3Urls.URLFrontImage4),
            House.create(House.HouseTypes.VILLA, AwsS3Urls.URLFrontImage5),
            House.create(House.HouseTypes.VILLA, AwsS3Urls.URLFrontImage6),
        ]

        for house in houses:
            house.location = "Spain, Málaga"
            house.number_rooms = 3
            house.beds = 2
            house.price = "$969 384"
            house.save()

        # Create default broker
        broker = Broker.objects.create(email="broker@example.com")
        broker.save()

        # Create default countries
        countries = [
            Country.objects.create(name=Country.CountryNames.SWEDEN),
            Country.objects.create(name=Country.CountryNames.SPAIN),
        ]
        for country in countries:
            country.save()