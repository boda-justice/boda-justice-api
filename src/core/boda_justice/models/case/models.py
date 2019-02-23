from django.db import models
from django.utils.translation import gettext_lazy as _
from boda_justice.models.police_station.models import PoliceStation
from boda_justice.models.complaint.models import Complaints
from boda_justice.models.lawyer.models import Lawyers
from boda_justice.models.offence.models import Offence


class Case(models.Model):
    complaint = models.ForeignKey(
        Complaints, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(
        Lawyers, on_delete=models.SET_NULL, null=True, blank=True)
    # Offences are not yet more than one.
    offence = models.ForeignKey(
        Offence, on_delete=models.SET_NULL, null=True, blank=True)
    police_station = models.ForeignKey(
        PoliceStation, on_delete=models.SET_NULL, null=True, blank=True)
    # A greater designation of a case will require either a choice field or a
    # separate model Case Status'
    status = models.BooleanField(_('case_status'), default=False, help_text=_(
        'Designates whether the case is open or closed.'),)
