from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'service'
urlpatterns = [
    path('services/', views.services, name='services'),
    path('create_service_category/', views.create_service_category,
         name='create_service_category'),
]
