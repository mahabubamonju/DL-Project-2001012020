from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

from django.contrib.auth.decorators import login_required
from home.decorators import allowed_users


@login_required(login_url="accounts/login/")
@allowed_users(allowed_roles=['doctor'])
def DOCTOR_HOME(request):

    return render(request, 'doctor/main/index.html')
