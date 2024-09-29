from django.db import models

# Patient model
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    diagnosis = models.CharField(max_length=200)
    image = models.URLField(max_length=200, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

# Doctor model
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField()
    image = models.URLField(max_length=200, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
