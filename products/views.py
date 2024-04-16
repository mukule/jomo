from django.shortcuts import render, redirect
from .forms import ProductCategoryForm


def create_product_category(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page
            return redirect('products:product_category')
    else:
        form = ProductCategoryForm()
    return render(request, 'office/category.html', {'form': form})


def product_category(request):
    return render(request, 'office:categories')
