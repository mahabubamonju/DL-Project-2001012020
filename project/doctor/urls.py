from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views.home import HOME
from .views.chatbot import CHATBOT
from .views.madical_chekup import MADICAL_CHEKUP
from .views.print import PRINT

#! Login Page
from .views.login_page import *

#! Multiple -> ( Login , Logout, Registration )
from .views.accounts import LOGIN
from .views.logout import LOGOUT
from .views.accounts import REGISTRATION
from .views.accounts import MULTIPLE_REGISTRATION
from .views.admin_registration import ADMIN_REGISTRATION
from .views.customer_registration import CUSTOMER_REGISTRATION
from .views.doctor_registration import DOCTOR_REGISTRATION

urlpatterns = [
    #! Customer Page
    path('', HOME, name='home'),
    path('chatbot', CHATBOT, name='chatbot'),
    path('madical_chekup', MADICAL_CHEKUP, name='madical_chekup'),
    path('prescription', PRINT, name='print'),

    #! Login Page Admin
    path('admin_dashbord', ADMIN, name='admin'),

    #! Login Page Doctor
    path('doctor_dashbord', DOCTOR, name='doctor'),

    #! Login Page Home
    path('customer', CUSTOMER, name='customer'),

    #! Multiple -> ( Login , Logout, Registration )
    path('accounts/login/', LOGIN, name='login'),
    path('logout', LOGOUT, name='logout'),
    path('registration', REGISTRATION, name='registration'),
    path('multiple_registration', MULTIPLE_REGISTRATION, name='multiple-registration'),
    path('admin_registration', ADMIN_REGISTRATION, name='admin-registration'),
    path('customer_registration', CUSTOMER_REGISTRATION, name='customer-registration'),
    path('doctor_registration', DOCTOR_REGISTRATION, name='doctor-registration'),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)