from boda_justice.models.offence.models import Offence
from rest_framework import serializers


class OffencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offence
        fields = ('fine', 'description')
