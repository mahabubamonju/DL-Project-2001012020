from django.db import models
from django.contrib.auth.models import AbstractUser

#! ========== Multiple User ==========
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class user_type(models.Model):
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.is_admin == True:
            return self.user.username + " - is_admin"
        elif self.is_customer == True:
            return self.user.username + " - is_customer"
        elif self.is_doctor == True:
            return self.user.username + " - is_doctor"

class ADMIN(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class CUSTOMER(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class DOCTOR(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
#! ========================================================================================

#! ========== SymptomRecord ==========
class SymptomRecord(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    date = models.DateField()
    symptoms = models.TextField()
    predicted_disease = models.CharField(max_length=100)
    dis_des = models.TextField()
    precautions = models.TextField()
    medications = models.TextField()
    rec_diet = models.TextField()
    workout = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.predicted_disease}"

#! ========================================================================================


