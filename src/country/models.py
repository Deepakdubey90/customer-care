from django.db import models
from utils.models import BaseModel


class Country(BaseModel):

    name = models.CharField(max_length = 200, null = False)
    code_2 = models.CharField(max_length = 2, null = True)
    code_3 = models.CharField(max_length = 3, null = True)

    def __str__(self):
        return self.name
