from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser

class Student(AbstractBaseUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'student'

    def __str__(self):
        return (self.name, " ", self.surname)
