from django.shortcuts import render , redirect , HttpResponseRedirect
# from home.models.models import *
from home.models import *

def unauthenticated_user(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:

            user = request.user.id

            type_obj = user_type.objects.get(user=user)

            if type_obj.is_admin:
                return redirect('admin') #Go to Admin home
            elif type_obj.is_customer:
                # return redirect('customer') #Go to customer home
                return redirect('home') #Go to customer home
            elif type_obj.is_doctor:
                return redirect('doctor') #Go to editor home
                
        else:
            return views_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(views_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.is_authenticated:
                user = request.user.id

                type_obj = user_type.objects.get(user=user)

                if type_obj.is_admin:
                    group = 'admin' #Go to Admin home
                elif type_obj.is_customer:
                    group = 'customer' #Go to customer home
                elif type_obj.is_doctor:
                    group = 'doctor' #Go to doctor home

                if group in allowed_roles:
                    return views_func(request, *args, **kwargs)
                else:
                    return redirect('login')
                    # return HttpResponseRedirect('you are not see the page!')
            
        return wrapper_func
    return decorator

