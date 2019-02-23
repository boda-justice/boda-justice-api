from django.db import models
from django.utils.translation import gettext_lazy as _
from boda_justice.models.complainant.models import Complainants
from django.utils import timezone


class Complaints(models.Model):
    complainant = models.ForeignKey(Complainants, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    description = models.TextField(_('complaint_description'))
    creation_date = models.DateTimeField(_('date_created'),
                                         default=timezone.now)
    modification_date = models.DateTimeField(_('date_modified'),
                                             auto_now_add=True)

    def __str__(self):
        return str(self.complainant) + self.description
