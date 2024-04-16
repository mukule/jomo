from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('product_categories/<int:category_id>/',
         views.product_category_detail, name='product_category_detail'),

    path('contact/', views.contact, name='contact'),
]
