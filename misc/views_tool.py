#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/24
map_tab_buzz = {
    '0': '字典类',
    '1': '居民健康档案',
    '2': '慢病',
    '3': '老年人',
    '4': '妇幼、儿童',
    '5': '家庭医生签约',
    '9': '其他',
}

map_tab_type = {
    'table': '表',
    'view': '视图',
}

map_tab_status = {
    '1': '启用',
    '0': '停用',
}

map_is_nullable = {
    '1': '可为空',
    '0': '不可为空',
}

map_column_status = {
    '1': '启用',
    '0': '停用',
}

def map_table(table):
    table.tab_buzz = map_tab_buzz[str(table.tab_buzz)] if table.tab_buzz else ''
    table.tab_type = map_tab_type[table.tab_type] if table.tab_type else ''
    table.tab_status = map_tab_status[str(table.tab_status)] if table.tab_status else ''
    return table

def map_column(column):
    column.is_nullable = map_is_nullable[str(column.is_nullable)] if column.is_nullable else ''
    column.col_status = map_column_status[str(column.col_status)] if column.col_status else ''
    return column