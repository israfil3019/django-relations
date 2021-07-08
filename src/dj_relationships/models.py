from django import db
from django.db import models


class Creator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Language(models.Model):
    name = models.CharField(max_length=50)
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=50)
    framework = models.ManyToManyField(
        Framework, db_table="dd")  # the table between we use "dd"

    def __str__(self):
        return self.name
