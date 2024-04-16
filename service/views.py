from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404


def create_service_category(request):
    if request.method == 'POST':
        form = ServiceCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another view
            return redirect('service:services')
    else:
        form = ServiceCategoryForm()
    return render(request, 'service/create_service_category.html', {'form': form})


def services(request):
    categories = Service_category.objects.all()
    return render(request, 'service/services.html', {'categories': categories})


def service_detail(request, category_id):
    category = Service_category.objects.get(id=category_id)
    # Retrieve services associated with the category
    services = category.service_set.all()
    return render(request, 'service/service_detail.html', {'category': category, 'services': services})


def create_service(request, category_id):
    # Retrieve the Service_category instance based on the category_id
    category = get_object_or_404(Service_category, id=category_id)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new Service object but don't save it yet
            service = form.save(commit=False)
            # Set the category of the service
            service.category = category
            # Save the service
            service.save()
            # Redirect back to the service detail page for the same category
            return redirect('service:service_detail', category_id=category_id)
    else:
        # Prepopulate the form with the category
        form = ServiceForm(initial={'category': category})

    return render(request, 'service/create_service.html', {'form': form})
