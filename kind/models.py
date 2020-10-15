from django.db import models
from category.models import Category


class Kind(models.Model):
    title = models.CharField(
        max_length=40
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.id}: {self.title}: {self.category.id}"
