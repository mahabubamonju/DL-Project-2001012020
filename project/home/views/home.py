from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

def HOME(request):

    return render(request, 'main/home.html')
