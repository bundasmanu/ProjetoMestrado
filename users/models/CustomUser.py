from django.contrib.auth.models import AbstractUser
from django.db import models
import expDjango.config as config

class CustomUser(AbstractUser):

    userType = models.CharField(max_length=50, choices=
                        (('D' , config.DATASCIENTIST),
                         ('A', config.ADMIN),
                        ('H' , config.HEALTHCARE)))
    username = models.CharField(unique=True, max_length=50)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password'] #EMAIL AND PASSWORD ARE REQUIRED BY DEFAULT

    def __str__(self):
        return self.username

    def isHealthCare(self):
        return self.is_healthCare

    def isDataScientist(self):
        return self.is_dataScientist
