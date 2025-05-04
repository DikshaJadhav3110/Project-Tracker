from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

@login_required
def dashboard(request):
    user = request.user

    if user.groups.filter(name='Student').exists():
        return render(request, 'student.html')

    elif user.groups.filter(name='Faculty').exists():
        return render(request, 'faculty.html')

    else:
        return render(request, 'unknown_role.html')  # fallback
