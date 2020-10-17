from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=50
    )
    image = models.ImageField(blank=True, upload_to='category_images')

    def __str__(self):
        return f"{self.title}"

