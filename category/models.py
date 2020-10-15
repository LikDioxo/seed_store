from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=50
    )
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.id}: {self.title}"

