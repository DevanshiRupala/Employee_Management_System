"""EMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('adlogin', adlogin, name='adlogin'),
    path('emplogin', emplogin, name='emplogin'),
    path('option', option, name='option'),
    path('registration', registration, name='registration'),
    path('upload_payroll', upload_payroll, name='upload_payroll'),
    path('grant_leave', grant_leave, name='grant_leave'),
    path('view_payroll', view_payroll, name='view_payroll'),
    path('leaves', leaves, name='leaves'),
    path('profile', profile, name='profile'),
    path('Logout', Logout, name='Logout'),
]
