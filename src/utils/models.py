import uuid
from django.db import models


class BaseModel(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   created_on = models.DateTimeField(auto_now_add=True,
                                     verbose_name=("Created on"))
   updated_on = models.DateTimeField(auto_now=True,
                                     verbose_name=("Updated on"))
   deleted_on = models.DateTimeField(blank=True,
                                     null=True,
                                     default=None,
                                     verbose_name=("Deleted on"))
   class Meta:
      abstract = True
