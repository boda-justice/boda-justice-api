"""Urls for the app"""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from boda_justice.views.offence import offences_views
from boda_justice.views.root.root import api_root

urlpatterns = [
    url(r'^$', api_root),
    url(r'^offences/$', offences_views.OffencesView.as_view(),
        name='offences'),
    url(r'^offences/(?P<pk>[0-9]+)/$',
        offences_views.OffencesDetailView.as_view(), name='offences'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
