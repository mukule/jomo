from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden


def user_not_authenticated(function=None, redirect_url='/'):
    """
    Decorator for views that checks that the user is NOT logged in, redirecting
    to the homepage if necessary by default.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator


def superuser(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser or request.user.access_level == 1:
            # Superuser or user with access_level 1 (Admin)
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden(render(request, 'users/not_allowed.html'))

    return _wrapped_view


def managers(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Admin or Manager
        if request.user.is_superuser or request.user.access_level in [1, 2]:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden(render(request, 'users/not_allowed.html'))

    return _wrapped_view


def staffs(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Admin, Manager, or Cashier
        if request.user.is_superuser or request.user.access_level in [1, 2, 3]:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden(render(request, 'users/not_allowed.html'))

    return _wrapped_view
