from django.contrib import admin
# from home.models.models import *
from home.models import *

#! Register your models here.

# admin.site.register(Test)
admin.site.register(User)
admin.site.register(user_type)
admin.site.register(ADMIN)
admin.site.register(CUSTOMER)
admin.site.register(DOCTOR)

admin.site.register(SymptomRecord)


#! *===== Admin Account =====*

# email: admin@gmail.com
# user: admin
# pass: 123

#! *===== User Account =====*

# email: test@gmail.com
# user: test
# pass: 123
