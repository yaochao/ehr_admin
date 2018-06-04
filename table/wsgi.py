#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/6/1


from django.core.wsgi import get_wsgi_application
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'ehr_admin.settings'
application = get_wsgi_application()