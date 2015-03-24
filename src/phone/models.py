import uuid
from django.db import models
from utils.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator


class Phone(BaseModel):

    phone =  PhoneNumberField()
    contact_type = models.CharField(max_length = 20, null = False)
    entity_object_id = models.UUIDField(default=uuid.uuid4, editable=False)
    entity_content_type = models.ForeignKey(ContentType)
    entity_object = GenericForeignKey('entity_content_type',
                                              'entity_object_id')
