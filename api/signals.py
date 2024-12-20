from django.db.models.signals import post_migrate
from django.dispatch import receiver
from house.models import House, HouseImage
from broker.models import Broker
from country.models import Country
from utilities.aws_s3_urls import AwsS3Urls

def populate_default_data():
    # Clear existing data
    House.objects.all().delete()
    HouseImage.objects.all().delete()
    Broker.objects.all().delete()
    Country.objects.all().delete()

    # Create default broker
    broker = Broker.objects.create(email="broker@example.com")
    broker.save()

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
        house.broker = broker
        house.save()

    # Create default countries
    countries = [
        Country.objects.create(name=Country.CountryNames.SWEDEN),
        Country.objects.create(name=Country.CountryNames.SPAIN),
    ]
    for country in countries:
        country.save()
        
    # Create house images and associate them with houses
    for house in houses:
        for _ in range(6):
            house_image1 = HouseImage.create(house.src)
            house_image2 = HouseImage.create(AwsS3Urls.URL1)
            house_image3 = HouseImage.create(AwsS3Urls.URL2)
            house_image4 = HouseImage.create(AwsS3Urls.URL3)
            house_image5 = HouseImage.create(AwsS3Urls.URL4)
            house_image6 = HouseImage.create(AwsS3Urls.URL5)
            house_image7 = HouseImage.create(AwsS3Urls.URL6)
            house.images.add(house_image1, house_image2, house_image3, house_image4, house_image5, house_image6, house_image7)
            house.save()

@receiver(post_migrate)
def post_migrate_handler(sender, **kwargs):
    if sender.name == 'api':
        populate_default_data()