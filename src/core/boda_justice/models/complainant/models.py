from django.db import models
from django.utils.translation import gettext_lazy as _
from boda_justice.models.common.common_user import User


class Complainants(models.Model):
    OCCUPATION_CHOICES = (
        ('Uber Motorist', 'Uber Motorist'),
        ('Motor Cyclist', 'Motor Cyclist'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True)
    occupation = models.CharField(
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default='Uber Motorist',
    )
