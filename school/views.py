from django.shortcuts import render, redirect, get_object_or_404
from .forms import SchoolForm
from school .models import *


def create_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('school:school')
    else:
        form = SchoolForm()
    return render(request, 'office/create_school.html', {'form': form})


def school(request):
    first_school = School.objects.first()
    return render(request, 'office/school.html', {'school': first_school})
