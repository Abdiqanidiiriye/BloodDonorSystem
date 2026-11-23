from django.db import models

# Create your models here.

class BloodDonor(models.Model):

    BLOOD_GROUPS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    name = models.CharField(max_length=100)

    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUPS
    )

    phone = models.CharField(max_length=20)

    email = models.EmailField(blank=True)

    city = models.CharField(max_length=100)

    available = models.BooleanField(default=True)

    registered_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name