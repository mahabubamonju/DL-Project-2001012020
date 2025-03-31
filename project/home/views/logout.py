from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

from django.contrib import messages
# from home.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout

def LOGOUT(request):

    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('home')

    return HttpResponse('home')
