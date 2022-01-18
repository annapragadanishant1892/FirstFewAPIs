import django_filters

from myapi.models import *

class BirthFilter(django_filters.FilterSet):



    class Meta:
        model= Person
        fields= {'birth': ['gt'],
                 'name': ['exact', 'contains']
                 }

