from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

def DOCTOR_PRINT(request):

    return render(request, 'doctor/main/print.html')