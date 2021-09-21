from django.urls import path
from . import views

urlpatterns = [
    path('', views.listproduct, name= 'home'), 
    path('category', views.category, name='category') 
]
