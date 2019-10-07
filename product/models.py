import uuid
from django.db import models
from model_utils.models import TimeStampedModel
from model_utils import Choices


class Product(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(TimeStampedModel):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Unit(TimeStampedModel):
    CHOICES = Choices(('IN_STOCK', 'In Stock'), ('DELIVERED', 'Delivered'))
    uuid = models.UUIDField(default=uuid.uuid4)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    status = models.CharField(max_length=255,
                              choices=CHOICES,
                              default=CHOICES.IN_STOCK)

    def __str__(self):
        return f'{self.uuid}'
