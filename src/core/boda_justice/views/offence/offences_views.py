from boda_justice.serializers.offence.serializers import OffencesSerializer
from rest_framework import generics
from boda_justice.models.offence.models import Offence
from rest_framework.permissions import IsAdminUser


class OffencesView(generics.ListAPIView):
    """
    List all offences in the application
    """
    queryset = Offence.objects.all()
    serializer_class = OffencesSerializer


class OffencesDetailView(generics.RetrieveAPIView):
    """
    Retrieve, update or delete an offence.
    """
    queryset = Offence.objects.all()
    serializer_class = OffencesSerializer
