from django.urls import path, re_path
from .import views

app_name = 'searches'

urlpatterns = [
    path('',views.search_list,name='list'),
    path('create', views.CreateView),
    
    
]