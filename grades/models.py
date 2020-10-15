from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from kind.models import Kind


class Grade(models.Model):
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    grade_number = models.IntegerField()
    name = models.CharField(max_length=50)
    bred_date = models.DateTimeField()
    characters = models.OneToOneField('Character', on_delete=models.CASCADE)
    planting_method = models.TextField()
    care = models.TextField()
    consignment = models.IntegerField()
    expiration_date = models.DateTimeField()
    image = models.ImageField()

    def __str__(self):
        return f"{self.id}: {self.grade_number}: {self.name}: {self.characters}"


class Character(models.Model):
    months = [
        ('Январь', 'Январь'),
        ('Февраль', 'Февраль'),
        ('Март', 'Март'),
        ('Апрель', 'Апрель'),
        ('Май', 'Май'),
        ('Июнь', 'Июнь'),
        ('Июль', 'Июль'),
        ('Август', 'Август'),
        ('Сеньтябрь', 'Сеньтябрь'),
        ('Октабрь', 'Октабрь'),
        ('Ноябрь', 'Ноябрь'),
        ('Декабрь', 'Декабрь'),
    ]

    watering_conditions_choices = [
        ('поверхносное орошение', 'поверхносное орошение'),
        ('капельное орошение', 'капельное орошение'),
        ('дождевание', 'дождевание'),
        ('подпочвенное орошение', 'подпочвенное орошение')
    ]

    product_type_choices = [
        ()
    ]

    planting_depth = models.PositiveSmallIntegerField()  # Глубина посадки
    distance = models.PositiveSmallIntegerField()  # Растояние в радиусе от других растений и построек
    plant_height = models.PositiveSmallIntegerField()
    leaves_color = models.CharField(max_length=40)
    product_type = models.CharField(max_length=20)  # TODO: change with choice field
    soil_moisture = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    watering_conditions = models.TextField(choices=watering_conditions_choices)
    fruit_size = models.PositiveSmallIntegerField()
    adaptation = models.BooleanField()
    frost_resistance = models.BooleanField()
    flowering_period_start = models.CharField(max_length=20, choices=months)
    flowering_period_end = models.CharField(max_length=20, choices=months)

    def __str__(self):
        return f"{self.id}: {self.planting_depth}: {self.distance}: {self.plant_height}: {self.leaves_color}"
