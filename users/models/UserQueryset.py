from django.db import models

class UserQueryset(models.QuerySet):

    def dataScientist(self):
        return self.filter(userType='D')

    def admin(self):
        return self.filter(userType='A')

    def healthCare(self):
        return self.filter(userType='H')