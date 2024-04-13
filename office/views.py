from django.shortcuts import render
from users.forms import *
from users.decorators import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from users.models import *

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


@login_required
@staffs
def staffs(request):
    staffs = CustomUser.objects.filter(access_level__in=[1, 2, 3])

    return render(request, 'office/staffs.html', {'staffs': staffs})


def not_allowed(request):
    return render(request, 'users/not_allowed.html')
