from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, country_name):
        return cls.objects.create(
            name=country_name.value
        )

class CountryNames(models.TextChoices):
    SWEDEN = 'SWEDEN', _('Sweden')
    SPAIN = 'SPAIN', _('Spain')

