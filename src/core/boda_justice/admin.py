from django.contrib import admin
from boda_justice.models.lawyer.models import Lawyers
from boda_justice.models.common.common_user import User
from boda_justice.models.complainant.models import Complainants
from boda_justice.models.case.models import Case
from boda_justice.models.complaint.models import Complaints
from boda_justice.models.offence.models import Offence
from boda_justice.models.police_station.models import PoliceStation
from boda_justice.models.review.models import Reviews

# Register your models here.
admin.site.register(Lawyers)
admin.site.register(User)
admin.site.register(Complainants)
admin.site.register(Case)
admin.site.register(Complaints)
admin.site.register(Offence)
admin.site.register(PoliceStation)
admin.site.register(Reviews)
