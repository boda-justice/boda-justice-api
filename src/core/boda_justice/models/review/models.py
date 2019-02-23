from django.db import models
from django.utils.translation import gettext_lazy as _
from boda_justice.models.lawyer.models import Lawyers
from boda_justice.models.case.models import Case


class Reviews(models.Model):
    comments = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
    # A case ensures only people who were served to comment on it
    case = models.ForeignKey(
        Lawyers, on_delete=models.SET_NULL, null=True, blank=True)
