from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard'),
    path('Transportation/Air/', views.transportation_air, name='transportation_air'),
    path('Transportation/Road/', views.transportation_road, name='transportation_road'),
    path('Transportation/Maritime/', views.transportation_maritime, name='transportation_maritime'),
    path('Transportation/About/', views.transportation_about, name='transportation_about'),
    path('Transportation/Members/', views.transportation_members, name='transportation_members'),
    path('Transportation/Certificate/', views.transportation_certificate, name='transportation_certificate'),
    path('Transportation/Certificate/Update/<int:id>', views.transportation_certificate_update, name='transportation_certificate_update'),
]
