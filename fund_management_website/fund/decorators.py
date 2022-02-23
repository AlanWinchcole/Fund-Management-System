"""Module to assign different groups of users"""
from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles):
    """Allowed_users"""
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Not authorized')
        return wrapper_func
    return decorator

def admin_only(view_func):
    """Admin_only"""
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Applicant':
            return redirect('fund:dashboard')

        if group == 'LAG':
            return redirect('fund:dashboard')
            
        if group == 'Admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func
