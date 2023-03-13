"""allocation URL Configuration

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
from django.urls import path,include
from django.http import HttpResponse
# from allocation_engine.views import Testing
from allocation_engine.views import Employeeviewset


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('testing/', Testing),
    # path('allocation_engine/api/',include('allocation_engine.urls')),

    path('create/', Employeeviewset.as_view({'post':'create'})),
    path('update/', Employeeviewset.as_view({'put':'update'})),
    path('delete/<id>', Employeeviewset.as_view({'delete':'delete'})),
    path('retrivingAll/', Employeeviewset.as_view({'get':'retrivingAll'})),
    path('retriv/', Employeeviewset.as_view({'post':'retriv'})),
    # path('user/<int:pk>/', Employeeviewset.as_view(), empname='user-detail'), 






]
