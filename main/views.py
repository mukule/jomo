from django.shortcuts import render
from service.models import *

# Create your views here.


def index(request):
    # Retrieve all service categories from the database
    service_categories = Service_category.objects.all()

    # Pass service_categories to the template context
    context = {
        'categories': service_categories
    }

    # Render the index.html template with the context
    return render(request, 'main/index.html', context)
