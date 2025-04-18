import uuid
from django.db import models

class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    years_of_experience = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"