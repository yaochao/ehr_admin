from django.shortcuts import render
from django.http import HttpResponse
from table.models import Table


def home(request):
    tables = Table.objects.all()
    return HttpResponse('hello world! this is my home.')
