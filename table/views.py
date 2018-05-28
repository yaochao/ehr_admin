from django.shortcuts import render
from django.http import HttpResponse
from table.models import Table, Column
from misc.views_tool import map_table, map_column


def tables(request):
    tables = Table.objects.all()
    tables = [map_table(table) for table in tables]
    return render(request, 'tables.html', {'tables': tables})


def columns(request, tab_name):
    columns = Column.objects.filter(tab_name=tab_name)
    columns = [map_column(column) for column in columns]
    return render(request, 'columns.html', {'columns': columns})


def update_table(request):
    connect = None # TODO
    cursor = connect.cursor()
    if request.POST:
        a = request.POST['xxx']
        a2 = request.POST['xxx']
        a3 = request.POST['xxx']
        sql = 'UPDATE xxx SET aa=%s,bb=%s,cc=%s'
        cursor.execute(sql, (a, a2, a3))
    return HttpResponse('success')
