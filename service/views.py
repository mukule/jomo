from django.shortcuts import render, redirect
from .forms import ServiceCategoryForm
from .models import *


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
