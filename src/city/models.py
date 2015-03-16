from utils.models import BaseModel
from django.db import models
from state.models import State


class City(BaseModel):
    state = models.ForeignKey(State)
    name = models.CharField(max_length = 200, null = False)

    def __str__(self):
        return self.name
