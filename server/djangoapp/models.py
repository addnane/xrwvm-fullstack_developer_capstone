from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime



class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(
        "CarMake", on_delete=models.CASCADE, related_name="models"
    )  # Many-to-One relationship

    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
        ("TRUCK", "Truck"),
        ("SPORTS", "Sports Car"),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default="SUV")

    year = models.IntegerField(
        default=datetime.date.today().year,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(datetime.date.today().year),
        ],
    )

    # Other fields as needed

    def __str__(self):
     return f"{self.car_make.name} {self.name} ({self.year})"