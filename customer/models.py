from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"User: {self.firstname}, {self.lastname}, {self.email}"
