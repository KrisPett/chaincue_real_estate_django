from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'countries'

    class CountryNames(models.TextChoices):
        SWEDEN = 'SWEDEN', _('Sweden')
        SPAIN = 'SPAIN', _('Spain')
