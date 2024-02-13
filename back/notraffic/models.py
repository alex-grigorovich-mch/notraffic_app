from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from common.models import BaseModel


class Street(BaseModel):
    name = models.CharField(max_length=128, primary_key=True)

    def __str__(self):
        return self.name


class Intersection(BaseModel):
    name = models.CharField(max_length=128, null=False, blank=False, unique=True)

    latitude = models.DecimalField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
        max_digits=9,
        decimal_places=6,
        null=False,
        blank=False,
    )

    longitude = models.DecimalField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
        max_digits=9,
        decimal_places=6,
        null=False,
        blank=False,
    )

    first_street = models.ForeignKey(Street, on_delete=models.RESTRICT, related_name="+")

    second_street = models.ForeignKey(Street, on_delete=models.RESTRICT, related_name="+")

    def __str__(self):
        return self.name
