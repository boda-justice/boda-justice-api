from django.db import models
from django.utils.translation import gettext_lazy as _
from boda_justice.models.complainant.models import Complainants
from boda_justice.models.lawyer.models import Lawyers
from django.utils import timezone


class Offence(models.Model):
    fine = models.DecimalField(max_digits=6, decimal_places=0)
    creation_date = models.DateTimeField(_('date_created'),
                                         default=timezone.now)
    modification_date = models.DateTimeField(_('date_modified'),
                                             auto_now_add=True)
    description = models.TextField(_('offence_description'))
