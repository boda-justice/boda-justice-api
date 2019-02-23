from django.db import models
from django.utils.translation import gettext_lazy as _


class PoliceStation(models.Model):
    name = models.CharField(_('police_station'), max_length=15)
    street_road = models.CharField(_('street_or_road'), max_length=15)
