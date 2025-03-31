from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from home.models import SymptomRecord

from django.contrib.auth.decorators import login_required

from home.decorators import allowed_users


@login_required(login_url="accounts/login/")
@allowed_users(allowed_roles=['doctor'])
def Patient_View(request,id):
    records = SymptomRecord.objects.get(id=id)

    context = {
        'result': records
    }

    return render(request, 'doctor/main/patient_view.html',context)
