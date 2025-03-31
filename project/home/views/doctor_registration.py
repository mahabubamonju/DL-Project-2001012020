from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

def DOCTOR_REGISTRATION(request):

    return render(request, 'login_registration/doctor_registration.html')
