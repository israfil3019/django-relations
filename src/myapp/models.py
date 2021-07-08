from django.db import models
from django.core.exceptions import ValidationError


def validate_number(value):
    if value > 5000:
        raise ValidationError("please enter a valid number less then 5000")


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.IntegerField(
        validators=[validate_number], blank=True, null=True)

    def __str__(self):
        return self.first_name
