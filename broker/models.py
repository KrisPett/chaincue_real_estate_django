import uuid
from django.db import models


class Broker(models.Model):
    id = models.CharField(primary_key=True, max_length=36,
                          default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name if self.name else self.email

    class Meta:
        db_table = 'brokers'
