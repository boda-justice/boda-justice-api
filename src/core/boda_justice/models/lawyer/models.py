from django.db import models
from django.utils.translation import gettext_lazy as _
from boda_justice.models.common.common_user import User


class Lawyers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True)
    status = models.BooleanField(
        _('active_status'), default=False, help_text=_(
            'Designates whether the user is available or not.'),)
    # The practise_number has letters and forward slashes e.g P.123/3456/89
    practise_number = models.CharField(_('pracitise_number'), max_length=15)
    building_address = models.CharField(_('building_address'), max_length=15)
    street_road = models.CharField(_('street_or_road'), max_length=15)
    building_floor = models.CharField(_('building_floor'), max_length=15)
