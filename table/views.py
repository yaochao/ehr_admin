from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseServerError
from django.db import connection
from table.models import Table, Column
from misc.views_tool import *
from .forms import RegisterForm
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


def update_column(request):
    # 获取一个cursor
    cursor = connection.cursor()
    data = json.loads(request.body)
    col_name = data['col_name']
    tab_name = data['tab_name']
    data_type = data['data_type']
    is_nullable = map_is_nullable_value2key(data['is_nullable'])
    col_status = map_col_status_value2key(data['col_status'])
    col_comment = data['col_comment']
    # 执行SQL
    try:
        sql = 'UPDATE ehr_columns SET data_type=%s ,col_ver=col_ver+1, is_nullable=%s, col_status=%s, col_comment=%s WHERE tab_name=%s AND col_name=%s'
        cursor.execute(sql, (data_type, is_nullable, col_status, col_comment, tab_name, col_name))
        connection.commit()
    except:
        print('error')
        return HttpResponseServerError(HttpResponse(json.dumps({'msg': 'error'})))
    return HttpResponse(json.dumps({'msg': '更新成功'}))


def register(request):
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # 请求为 POST，利用用户提交的数据构造一个绑定了数据的表单
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的save方法将用户数据保存到数据库
            form.save()
            # 注册成功，跳转回首页
            return redirect('/')
    else:
        # 如果method不是post，表名用户正在访问注册页面，展示一个注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 1.如果不是 POST 请求，则渲染的是一个空的表单 else里面的form
    # 2.如果用户通过表单提交数据，但是数据验证不合法，则渲染的是一个带有错误信息的表单 if里面的form
    return render(request, 'register.html', context={'form': form})

