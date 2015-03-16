from django.db import models
from utils.models import BaseModel
from category.models import Category


class Organization(BaseModel):
      category = models.ForeignKey(Category)
      name = models.CharField(max_length = 200, null = False)
      description = models.CharField(max_length = 200, null = False)

      def __str__(self):
            return self.name
