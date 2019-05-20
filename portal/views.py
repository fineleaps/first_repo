from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


# @login_required
def home(request):
    if request.user.is_superuser:
        return redirect('crm_admin:home')
    else:
        return render(request, 'portal/home.html')


@login_required
def profile(request):

    abcd = {}

    return render(request, 'portal/profile.html', abcd)

