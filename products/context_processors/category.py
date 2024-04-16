from service.models import Service_category
from products.models import *


def product_categories(request):
    # Retrieve all service categories
    categories = ProductCategory.objects.all()
    # Return a dictionary with the categories to be available in templates
    return {'product_categories': categories}
