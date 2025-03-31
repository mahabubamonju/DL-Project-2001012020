from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required

from home.decorators import allowed_users


@login_required(login_url="accounts/login/")
@allowed_users(allowed_roles=['admin'])
def ADMIN(request):

    return render(request, 'main/admin.html')

@login_required(login_url="accounts/login/")
@allowed_users(allowed_roles=['customer'])
def CUSTOMER(request):

    return render(request, 'main/customer.html')

# @login_required(login_url="accounts/login/")
# @allowed_users(allowed_roles=['doctor'])
# def DOCTOR(request):

#     return render(request, 'main/doctor.html')

