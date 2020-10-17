from django.db import models

from customer.models import Customer
from grades.models import Grade


class CartProduct(models.Model):
    product = models.OneToOneField(
        Grade,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"CartProduct: {self.product}, {self.quantity}, {self.price}"


class Cart(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE
    )
    products = models.ForeignKey(
        CartProduct,
        on_delete=models.CASCADE
    )

    total_price = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )

    def __str__(self):
        return f"Cart: {self.customer}, {self.products}, {self.total_price}"
