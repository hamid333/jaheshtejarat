from django.urls import path

from . import views

app_name = "transportation"

urlpatterns = [
    path('', views.transportation, name='transportation'),
    path('Maritime/', views.maritime, name='maritime'),
    path('Air/', views.air, name='air'),
    path('Road/', views.road, name='road'),
]

