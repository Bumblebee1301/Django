from django.shortcuts import render
from django.http import HttpResponse
from .models import nstracing
from django.http import Http404
#from .tables import NSTable
from django_tables2 import RequestConfig
from django.views.generic import TemplateView, ListView
import django_tables2
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import NSTFilter

def home(request):
    #return HttpResponse('<p>home view</p>')
    #trace_obj= nstracing.objects.all()
    #return render(request, 'home.html', {'trace_obj':trace_obj})
    """table = NSTable(nstracing.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'home.html', {'table':table})"""
    """table = NST_Tableview()
    #RequestConfig(request).configure(table)
    return render(request, 'home.html', {'table':table})"""

    filter = NSTFilter(request.GET,queryset=nstracing.objects.all())
    return render(request, 'home.html', {'filter': filter})



def details(request, id):
    #return HttpResponse('<p>detail view of NS tracing with id {}</p>'.format(id))
    try:
        trace_with_id = nstracing.objects.get(id = id)
    except trace_with_id.DoesNotExist:
        raise Http404('Trace data not found')
    return render(request, 'details.html',{'trace_with_id': trace_with_id})
