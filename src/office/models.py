from django.db import models
from utils.models import BaseModel
from city.models import City
from organization.models import Organization


class Office(BaseModel):
    city = models.ForeignKey(City)
    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length = 200, null = False)
    description = models.CharField(max_length = 200, null = False)
    line1 = models.CharField(max_length = 200, null = False)
    line2 = models.CharField(max_length = 200, null = True, blank = True)
    zipcode = models.CharField(max_length =10, null = True, blank = True)
    def __str__(self):
        return self.name
