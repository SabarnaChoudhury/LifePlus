from django.db import models

# Create your models here.

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

