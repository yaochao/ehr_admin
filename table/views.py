from django.shortcuts import render
from django.http import HttpResponse
from table.models import Table, Column


def tables(request):
    tables = Table.objects.all()
    return render(request, 'tables.html', {'tables': tables})

def columns(request, tab_name):
    columns = Column.objects.filter(tab_name=tab_name)
    return render(request, 'columns.html', {'columns': columns})
