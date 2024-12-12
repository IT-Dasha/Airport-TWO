"""
URL configuration for airport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
        path('', views.home, name='home'),
    path('home_employee', views.home_employee, name='home_employee'),
        path('all_plane', views.all_plane, name='all_plane'),
        path('all_employee', views.all_employee, name='all_employee'),
        path('all_equipage', views.all_equipage, name='all_equipage'),
        path('all_technical_staff', views.all_technical_staff, name='all_technical_staff'),
        path('all_race', views.all_race, name='all_race'),
        path('all_shift', views.all_shift, name='all_shift'),
        path('all_takeofflane', views.all_takeofflane, name='all_takeofflane'),
        path('all_flight_history', views.all_flight_history, name='all_flight_history'),
    # Добавление
    path('add_plane', views.add_plane, name='add_plane'),
    path('add_equipage', views.add_equipage, name='add_equipage'),
    path('add_takeoff_lane', views.add_takeoff_lane, name='add_takeoff_lane'),
    path('add_race', views.add_race, name='add_race'),
    #  path('add_shift', views.add_race, name='add_shift'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('add_technical_staff', views.add_technical_staff, name='add_technical_staff'),
    path('add_flight_history', views.add_flight_history, name='add_flight_history'),
]
