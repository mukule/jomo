from service.models import Service_category
from products.models import *


def service_categories(request):
    # Retrieve all service categories
    categories = Service_category.objects.all()
    # Return a dictionary with the categories to be available in templates
    return {'service_cat': categories}


def product_categories(request):
    # Retrieve all service categories
    categories = ProductCategory.objects.all()
    # Return a dictionary with the categories to be available in templates
    return {'categories': categories}
