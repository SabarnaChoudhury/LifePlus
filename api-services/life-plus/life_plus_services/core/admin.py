from django.contrib import admin
from .models import Doctor, Patient  # Import your models

# Register the models
admin.site.register(Doctor)
admin.site.register(Patient)
