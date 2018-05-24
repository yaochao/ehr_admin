from django.shortcuts import render
from django.http import HttpResponse
from table.models import Table


def tables(request):
    tables = Table.objects.all()
    return render(request, 'tables.html', {'tables': tables})
