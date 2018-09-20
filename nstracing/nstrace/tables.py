import django_tables2 as tables
from .models import nstracing
import django_filters
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django_tables2 import RequestConfig
from django.views.generic import TemplateView, ListView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


class NSTable(tables.Table):
    table = nstracing.objects.all()
    RequestConfig(request).configure(table)
    return render(request, 'home.html', {'table':table}

    class Meta:
        model = nstracing
        template_name = 'django_tables2/bootstrap.html'

"""class NST_FilterView(django_filters.FilterSet):
	Request_Type = django_filters.ModelChoiceFilter(label='Request_Type', queryset=models.nstracing.objects.all())
 	Path = django_filters.ModelChoiceFilter(label='Path', queryset=models.nstracing.objects.all())
    Pin = django_filters.ModelChoiceFilter(label='Pin', queryset=models.nstracing.objects.all())
    Prog = django_filters.ModelChoiceFilter(label='Prog', queryset=models.nstracing.objects.all())
    Open_Id = django_filters.ModelChoiceFilter(label='Open_Id', queryset=models.nstracing.objects.all())
    ZYQ_FileName = django_filters.ModelChoiceFilter(label='ZYQ_FileName', queryset=models.nstracing.objects.all())
 		 
 	class Meta:
 	model = models.nstracing
 	fields = ['Request_Type', 'Path', 'Pin', 'Prog','Open_Id','ZYQ_FileName']

class NST_Tableview():
    #model = nstracing
    table_class = NSTable
    filterset_class = NST_FilterView"""
