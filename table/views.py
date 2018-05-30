from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.db import connection
from table.models import Table, Column
from misc.views_tool import *
import json


def tables(request):
    tables = Table.objects.all()
    tables = [map_table(table) for table in tables]
    return render(request, 'tables.html', {'tables': tables})


def columns(request, tab_name):
    columns = Column.objects.filter(tab_name=tab_name)
    columns = [map_column(column) for column in columns]
    return render(request, 'columns.html', {'columns': columns})


def update_table(request):
    # 获取一个cursor
    cursor = connection.cursor()
    data = json.loads(request.body)
    tab_name = data['tab_name']
    tab_buzz = map_tab_buzz_value2key(data['tab_buzz'])
    tab_type = map_tab_type_value2key(data['tab_type'])
    tab_status = map_tab_status_value2key(data['tab_status'])
    tab_comment = data['tab_comment']
    # 执行SQL
    try:
        sql = 'UPDATE ehr_tables SET tab_ver=tab_ver+1, tab_buzz=%s, tab_type=%s, tab_status=%s, tab_comment=%s WHERE tab_name=%s'
        cursor.execute(sql, (tab_buzz, tab_type, tab_status, tab_comment, tab_name))
        connection.commit()
    except:
        return HttpResponseServerError(HttpResponse(json.dumps({'msg': 'error'})))
    return HttpResponse(json.dumps({'msg': '更新成功'}))
