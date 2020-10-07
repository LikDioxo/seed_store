from django.db import models


class Grade(models.Model):
    grade_number = models.IntegerField()
    name = models.CharField(max_length=50)
    bred_date = models.DateTimeField()
    characters = models.ForeignKey('Character', on_delete=models.CASCADE)
    planting_method = models.TextField()
    consignment = models.IntegerField()
    expiration_date = models.DateTimeField()
    image = models.ImageField()


class Character(models.Model):
    planting_depth = models.PositiveSmallIntegerField()  # Глубина посадки
    distance = models.PositiveSmallIntegerField()  # Растояние в радиусе от других растений и построек
    plant_height = models.PositiveSmallIntegerField()
    leaves_color = models.CharField(max_length=40)
    product_type = models.CharField(max_length=20)  # TODO: change with choice field
    soil_moisture = models.CharField(max_length=20)  # TODO: change with choice field
    watering_conditions = models.CharField(max_length=20)  # TODO: change with choice field
    fruit_size = models.PositiveSmallIntegerField()
    adaptation = models.BooleanField()
    frost_resistance = models.BooleanField()
    flowering_period_start = models.CharField(max_length=20)  # TODO: change with choice field
    flowering_period_end = models.CharField(max_length=20)  # TODO: change with choice field
