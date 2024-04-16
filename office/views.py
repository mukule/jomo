from django.shortcuts import render, get_object_or_404
from users.forms import *
from users.decorators import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from users.models import *
from service.forms import *
from service.models import *
from about.forms import *
from about.models import *
from school.models import *
from school.forms import *
from products.models import *
from products.forms import *

# Create your views here.


@login_required
@staffs
def index(request):
    return render(request, 'office/index.html')


@managers
def create_staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active = True
            user.save()
            return redirect('users:login')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = StaffForm()

    return render(request, "office/create_staff.html",
                  context={"form": form}
                  )


def edit_staff(request, staff_id):
    # Get the staff member object or return a 404 error if not found
    staff = get_object_or_404(CustomUser, id=staff_id)

    if request.method == "POST":
        # Populate the form with the POST data and the instance of the staff member
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            # Save the form and redirect to a success page
            form.save()
            # Change 'success_url' to the appropriate URL
            return redirect('success_url')
    else:
        # Populate the form with the instance of the staff member
        form = StaffForm(instance=staff)

    return render(request, "office/edit_staff.html", {"form": form})


@login_required
@staffs
def staffs(request):
    staffs = CustomUser.objects.filter(access_level__in=[1, 2, 3])

    return render(request, 'office/staffs.html', {'staffs': staffs})


def not_allowed(request):
    return render(request, 'users/not_allowed.html')


@login_required
def service_detail(request, category_id):
    category = Service_category.objects.get(id=category_id)
    # Retrieve services associated with the category
    services = category.service_set.all()
    return render(request, 'office/service_detail.html', {'category': category, 'services': services})


@login_required
def create_about(request):
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('office:about')
    else:
        form = AboutForm()
    return render(request, 'office/create_about.html', {'form': form})


@login_required
def edit_about(request, about_id):
    about_instance = get_object_or_404(About, id=about_id)

    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about_instance)
        if form.is_valid():
            form.save()
            return redirect('office:about')
    else:
        form = AboutForm(instance=about_instance)

    return render(request, 'office/edit_about.html', {'form': form, 'about_instance': about_instance})


@login_required
def about(request):
    # Retrieve the first About instance
    about_instance = About.objects.first()
    return render(request, 'office/about.html', {'about': about_instance})


@login_required
def create_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('office:school')
    else:
        form = SchoolForm()
    return render(request, 'office/create_school.html', {'form': form})


@login_required
def school(request):
    first_school = School.objects.first()
    return render(request, 'office/school.html', {'school': first_school})


@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('office:courses')  # Redirect to a success page
    else:
        form = CourseForm()
    return render(request, 'office/create_course.html', {'form': form})


@login_required
def courses(request):
    courses = Course.objects.all()
    return render(request, 'office/courses.html', {'courses': courses})


@login_required
def create_product_category(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page
            return redirect('office:product_category')
    else:
        form = ProductCategoryForm()
    return render(request, 'office/create_product_category.html', {'form': form})


@login_required
def product_category(request):
    categories = ProductCategory.objects.all()
    return render(request, 'office/product_category.html', {'categories': categories})


@login_required
def product_category_detail(request, category_id):
    # Retrieve the product category object
    category = get_object_or_404(ProductCategory, id=category_id)

    # Retrieve all products belonging to the category
    products = Product.objects.filter(category=category)

    # Render the template with the category object and its related products
    return render(request, 'office/product_category_detail.html', {'category': category, 'products': products})


@login_required
def create_product(request, category_id):
    category = ProductCategory.objects.get(id=category_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the product but don't commit to database yet
            product = form.save(commit=False)
            product.category = category  # Set the product category
            product.save()  # Now save the product with category

            # Redirect to the product category detail page
            return redirect('office:product_category_detail', category_id=category_id)
    else:
        # Set the initial category for the form
        initial_data = {'category': category}
        form = ProductForm(initial=initial_data)

    return render(request, 'office/create_product.html', {'form': form})
