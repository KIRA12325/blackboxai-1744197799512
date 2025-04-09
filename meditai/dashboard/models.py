from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    schedule = models.CharField(max_length=100)  # e.g. "8:00 AM, 2:00 PM, 8:00 PM"
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.dosage})"

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    reminder_hours = models.PositiveIntegerField(
        default=24,
        validators=[MinValueValidator(1), MaxValueValidator(72)]
    )

    def __str__(self):
        return f"Appointment with {self.doctor_name} on {self.date.strftime('%Y-%m-%d %H:%M')}"

class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.relationship})"
