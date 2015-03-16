from django.db import models
from utils.models import BaseModel
from country.models import Country


class State(BaseModel):
    country = models.ForeignKey(Country)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
