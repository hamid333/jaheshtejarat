from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard'),
    path('Transportation/Air/', views.transportation_air, name='transportation_air'),
    path('Transportation/Air/Update/<int:id>/', views.transportation_air_update, name='transportation_air_update'),
    path('Transportation/Air/Delete/<int:id>/', views.transportation_air_delete, name='transportation_air_delete'),

    path('Transportation/Road/', views.transportation_road, name='transportation_road'),
    path('Transportation/Road/Update/<int:id>/', views.transportation_road_update, name='transportation_road_update'),
    path('Transportation/Road/Delete/<int:id>/', views.transportation_road_delete, name='transportation_road_delete'),

    path('Transportation/Maritime/', views.transportation_maritime, name='transportation_maritime'),
    path('Transportation/Maritime/Update/<int:id>/', views.transportation_maritime_update, name='transportation_maritime_update'),
    path('Transportation/Maritime/Delete/<int:id>/', views.transportation_maritime_delete, name='transportation_maritime_delete'),

    path('Transportation/About/', views.transportation_about, name='transportation_about'),
    path('Transportation/Members/', views.transportation_members, name='transportation_members'),
    path('Transportation/Members/Update/<int:id>/', views.transportation_member_update,
         name='transportation_member_update'),
    path('Transportation/Certificate/', views.transportation_certificate, name='transportation_certificate'),
    path('Transportation/Certificate/Update/<int:id>/', views.transportation_certificate_update,
         name='transportation_certificate_update'),
]
