from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

def CUSTOMER_REGISTRATION(request):

    return render(request, 'login_registration/customer_registration.html')
