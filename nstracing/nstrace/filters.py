from django import forms
import django_filters
from .models import nstracing

class NSTFilter(django_filters.FilterSet):
    Request_Type = django_filters.CharFilter(lookup_expr = 'icontains')
    Path = django_filters.CharFilter(lookup_expr = 'icontains')
    Pin = django_filters.CharFilter(lookup_expr = 'icontains')
    Prog = django_filters.CharFilter(lookup_expr = 'icontains')
    #Request_Type = django_filters.ModelMultipleChoiceFilter(queryset=nstracing.objects.all(),
        #widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = nstracing
        fields = ['Request_Type','Path','Pin','Prog',]
