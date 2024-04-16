from django.urls import path
from . import views


app_name = 'office'
urlpatterns = [
    path('', views.index, name='index'),
    path('jomotech/staffs', views.staffs, name='staffs'),
    path("create_staff", views.create_staff, name="create_staff"),
    path('edit-staff/<int:staff_id>/', views.edit_staff, name='edit_staff'),
    path('services/<int:category_id>/',
         views.service_detail, name='service_detail'),
    path("create_about", views.create_about, name="create_about"),
    path('about/<int:about_id>/edit/', views.edit_about, name='edit_about'),
    path("about", views.about, name="about"),
    path("create_school", views.create_school, name="create_school"),
    path("school", views.school, name="school"),
    path("courses", views.courses, name="courses"),
    path("create_course", views.create_course, name="create_course"),
    path("product_category", views.product_category, name="product_category"),
    path("create_product_category", views.create_product_category,
         name="create_product_category"),
    path('product_categories/<int:category_id>/',
         views.product_category_detail, name='product_category_detail'),

    path('create_product/<int:category_id>/',
         views.create_product, name='create_product'),
]
