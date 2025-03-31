from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required

@login_required
def CHATBOT(request):
    
    return render(request, 'main/chatbot.html')
        
