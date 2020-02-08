from django.db import models

#REFS: https://stackoverflow.com/questions/45957142/django-model-manager-or-django-queryset
#https://groups.google.com/forum/#!topic/django-users/loVv-yYH2qg
#A MAIS IMPORTANTE: https://simpleisbetterthancomplex.com/tips/2016/08/16/django-tip-11-custom-manager-with-chainable-querysets.html

class UserQueryset(models.QuerySet):

    def dataScientist(self):
        return self.filter(userType='D')

    def admin(self):
        return self.filter(userType='A')

    def healthCare(self):
        return self.filter(userType='H')