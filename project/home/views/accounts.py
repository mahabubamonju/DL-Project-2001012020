from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

from django.contrib import messages
from home.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout

from home.decorators import unauthenticated_user

# from home.models.models import *
from home.models import *


@unauthenticated_user
def LOGIN(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        #? user to email chanege (user ke email dara poriborton kora hoise)
        # --- start ---
        user = EmailBackEnd.authenticate(request, 
        username=email,
        password=password)

        #! All login
        if user is not None:
            login(request, user)

            if request.GET.get('next',None):
                return HttpResponseRedirect(request.GET['next'])

            type_obj = user_type.objects.get(user=user)
            if user.is_authenticated and type_obj.is_admin:
                return redirect('admin') #Go to customer home
            elif user.is_authenticated and type_obj.is_customer:
                # return redirect('customer') #Go to customer home
                return redirect('home') #Go to customer home
            elif user.is_authenticated and type_obj.is_doctor:
                return redirect('doctor') #Go to editor home

        else:
            # Invalid email or password. Handle as you wish
            messages.error(request, 'Email and Password Are Invalid !')
            return redirect('login')

    return render(request, 'login_registration/login.html')

@unauthenticated_user
def REGISTRATION(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cu = request.POST.get('customer')

        # Chek Email
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email are Already Exists !')
            # return redirect('registration')
            return redirect('customer-registration')

        # Check Username
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username are Already Exists !')
            # return redirect('registration')
            return redirect('customer-registration')

        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        #! Save one by one
        usero = None
        if cu:
            usero = CUSTOMER(user=user)

        usero.save()

        # #! Save All
        usert = None
        if cu:
            usert = user_type(user=user,is_customer=True)
        
        usert.save()

        #Successfully registered. Redirect to homepage
        return redirect('login')

    return render(request, 'login_registration/customer_registration.html')

#! ==========================================================

def MULTIPLE_REGISTRATION(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        ad = request.POST.get('admin')
        cu = request.POST.get('customer')
        dt = request.POST.get('doctor')

        # Chek Email
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email are Already Exists !')
            # return redirect('registration')
            return redirect('customer-registration')

        # Check Username
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username are Already Exists !')
            # return redirect('registration')
            return redirect('customer-registration')

        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        #! Save one by one
        usero = None
        if ad:
            usero = ADMIN(user=user)
        elif cu:
            usero = CUSTOMER(user=user)
        elif dt:
            usero = DOCTOR(user=user)

        usero.save()

        # #! Save All
        usert = None
        if ad:
            usert = user_type(user=user,is_admin=True)
        elif cu:
            usert = user_type(user=user,is_customer=True)
        elif dt:
            usert = user_type(user=user,is_doctor=True)
        
        usert.save()

        #Successfully registered. Redirect to homepage
        return redirect('login')

    return render(request, 'login_registration/admin_registration.html')

#! ==========================================================


