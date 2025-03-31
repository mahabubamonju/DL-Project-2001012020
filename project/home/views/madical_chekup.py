from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required

@login_required
def MADICAL_CHEKUP(request):
    
    return render(request, 'main/madical_chekup.html')
        



