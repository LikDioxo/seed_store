from django.db import models

from character.models import Character
from customer.models import Customer


class BredingOrder(models.Model):
    ordered_characters = models.OneToOneField(
        Character,
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
