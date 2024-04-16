from django.shortcuts import render, get_object_or_404
from service.models import *
from about.models import *
from datetime import datetime
from school.models import *
from products.models import *

# Create your views here.


def index(request):
    # Retrieve all service categories from the database
    service_categories = Service_category.objects.all()
    about_instance = About.objects.first()
    school = School.objects.first()
    courses = Course.objects.all()
    categories = ProductCategory.objects.all()

    # Calculate the difference between the current year and year_started
    current_year = datetime.now().year
    year_started_difference = current_year - about_instance.year_started
    heroes = Service_category.objects.all()[:3]

    context = {
        'categories': service_categories,
        'about': about_instance,
        'experience': year_started_difference,
        'heroes': heroes,
        'school': school,
        'courses': courses,
        'product_categories': categories
    }

    # Render the index.html template with the context
    return render(request, 'main/index.html', context)


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    first_school = School.objects.first()

    return render(request, 'main/course_detail.html', {'course': course, 'school': first_school})


def product_category_detail(request, category_id):
    # Retrieve the product category object
    category = get_object_or_404(ProductCategory, pk=category_id)

    # Retrieve all products belonging to this category
    products = Product.objects.filter(category=category)

    return render(request, 'main/product_category_detail.html', {'category': category, 'products': products})


def contact(request):
    first_school = School.objects.first()
    return render(request, 'main/contact.html', {'school': first_school})
