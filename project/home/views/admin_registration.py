from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

def ADMIN_REGISTRATION(request):

    return render(request, 'login_registration/admin_registration.html')
