from django.urls import path

from . import views

urlpatterns = [
    path('singup/', views.SingUpView.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout_view'),
]
