import uuid
from django.db import models
from model_utils.models import TimeStampedModel


class Product(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
