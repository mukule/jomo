from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'service'
urlpatterns = [
    path('services/', views.services, name='services'),
    path('create_service_category/', views.create_service_category,
         name='create_service_category'),
    path('create/<int:category_id>/', views.create_service, name='create_service'),
    path('services/<int:category_id>/',
         views.service_detail, name='service_detail'),
]
