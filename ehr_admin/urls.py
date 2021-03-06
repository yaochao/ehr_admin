"""ehr_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from table.views import tables, columns, update_table, update_column, register

# TODO
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tables),
    path('table/<str:tab_name>/', columns),
    path('update_table/', update_table),
    path('update_column/', update_column),
    path('register/', register),
    path('users/', include('django.contrib.auth.urls'))
]
