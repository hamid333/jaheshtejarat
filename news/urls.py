from django.urls import path
from . import views

urlpatterns = [
    path('list_news_transportation/', views.List_News, name='List_News'),
    path('Add_News/', views.news_transportation, name='news_transportation'),
    path('Add_News/Update/<int:id>/', views.news_transportation_update, name='news_transportation_update'),

]
