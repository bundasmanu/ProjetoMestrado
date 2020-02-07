from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    is_dataScientist = models.BooleanField(default=False)
    is_healthCare = models.BooleanField(default=False)
    username = models.CharField(unique=True, max_length=50)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password'] #EMAIL AND PASSWORD ARE REQUIRED BY DEFAULT

    def __str__(self):
        return self.username

    def isHealthCare(self):
        return self.is_healthCare

    def isDataScientist(self):
        return self.is_dataScientist
