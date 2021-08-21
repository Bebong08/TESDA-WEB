from django.contrib.auth.models import User
import django_filters
from centers.models import Qualifications

class CentersFilter(django_filters.FilterSet):

    class Meta:
        model = Qualifications
        fields = '__all__'

