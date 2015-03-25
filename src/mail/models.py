from utils.models import BaseModel
from country.models import Country
from organization.models import Organization
from django.db import models
from office.models import Office


class Email(BaseModel):
    email = models.EmailField()
    description = models.CharField(max_length = 200, null = False)
    country = models.ForeignKey(Country)
    organization = models.ForeignKey(Organization)

    def __str__(self):
        return "%s %s" %(self.email, self.description)
