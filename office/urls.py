from django.urls import path
from . import views


app_name = 'office'
urlpatterns = [
    path('', views.index, name='index'),
    path('jomotech/staffs', views.staffs, name='staffs'),
    path("create_staff", views.create_staff, name="create_staff"),

]
