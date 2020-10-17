from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
        ('Сентябрь', 'Сентябрь'),
        ('Октябрь', 'Октябрь'),
        ('Ноябрь', 'Ноябрь'),
        ('Декабрь', 'Декабрь'),
    ]

    watering_conditions_choices = [
        ('Поверхностное орошение', 'Поверхностное орошение'),
        ('Капельное орошение', 'Капельное орошение'),
        ('Дождевание', 'Дождевание'),
        ('Подпочвенное орошение', 'Подпочвенное орошение'),
    ]

    product_type_choices = [
        ('Семена', 'Семена'),
        ('Саженец', 'Саженец'),
        ('Луковица', 'Луковица'),
        ('Споры', 'Споры'),
    ]

    planting_depth = models.PositiveSmallIntegerField()
    distance = models.PositiveSmallIntegerField()
    plant_height = models.PositiveSmallIntegerField()
    leaves_color = models.CharField(max_length=40)
    product_type = models.CharField(max_length=8, choices=product_type_choices)
    soil_moisture = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    watering_conditions = models.CharField(max_length=22, choices=watering_conditions_choices)
    fruit_size = models.PositiveSmallIntegerField()
    adaptation = models.BooleanField()
    frost_resistance = models.BooleanField()
    flowering_period_start = models.CharField(max_length=9, choices=months)
    flowering_period_end = models.CharField(max_length=9, choices=months)

    def __str__(self):
        return f"{self.id}: {self.planting_depth}: {self.distance}: {self.plant_height}: {self.leaves_color}"
