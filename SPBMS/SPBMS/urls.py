"""
URL configuration for SPBMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('login/', logIn, name='signin'),
    path('logout/',logOut, name='logout'),
    path('register/', register, name='register'),
    path('dashboard/',dashboard, name = 'dashboard'),
    path('checkunique/', checkUsername, name='checkunique'),
    path('createbudget/',budget, name='budget'),
    path('savebudget/',saveBudget, name='savebudget'), # type: ignore
    path('savecategory/',saveCategory, name='savecategory'), # type: ignore
    path('spending/',spendings,name='spendings'),
    path('report/',reports,name='report'),
    
]