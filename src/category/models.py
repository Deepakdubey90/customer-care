from django.db import models
from utils.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length = 200, null = False)

    def __str__(self):
        return self.name
