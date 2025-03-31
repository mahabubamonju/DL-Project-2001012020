from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from home.models import SymptomRecord

from django.contrib.auth.decorators import login_required

from home.decorators import allowed_users


@login_required(login_url="accounts/login/")
@allowed_users(allowed_roles=['doctor'])
def Patient_List(request):

    records = SymptomRecord.objects.all().order_by('-id')  # Fetch all records
    context = {
        'records': records
    }

    return render(request, 'doctor/main/patient_list.html',context)
