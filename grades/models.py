from django.db import models
from django.core.validators import ValidationError
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from kind.models import Kind
from character.models import Character
from utils.validators.grade_number_validator import grade_number_validator


class Image(models.Model):
    image = models.ImageField(upload_to="grade_images")


class Grade(models.Model):
    grade_number = models.CharField(
        max_length=12,
        validators=[grade_number_validator],
        primary_key=True
    )
    consignment = models.IntegerField(validators=[MinValueValidator(1)])
    name = models.CharField(
        max_length=50
    )
    kind = models.ForeignKey(
        Kind,
        on_delete=models.CASCADE
    )
    bred_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    characters = models.OneToOneField(
        Character,
        on_delete=models.CASCADE
    )
    planting_method = models.TextField()
    care = models.TextField()
    price = models.DecimalField(
        decimal_places=2,
        max_digits=9
    )
    images = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        blank=True
    )

    def __str__(self):
        return f"{self.id}: {self.grade_number}: {self.name}: {self.characters}"

    def clean(self):
        if self.bred_date > self.expiration_date:
            raise ValidationError(
                _("bred date can't be grater than expiration date!")
            )
