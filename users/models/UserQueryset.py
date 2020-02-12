from django.db import models

#REFS: https://stackoverflow.com/questions/45957142/django-model-manager-or-django-queryset
#https://groups.google.com/forum/#!topic/django-users/loVv-yYH2qg
#A MAIS IMPORTANTE: https://simpleisbetterthancomplex.com/tips/2016/08/16/django-tip-11-custom-manager-with-chainable-querysets.html

class UserQueryset(models.query.QuerySet):

    def dataScientist(self):
        return self.filter(userType='D')

    def admin(self):
        return self.filter(userType='A')

    def healthCare(self):
        return self.filter(userType='H')

    def getUserByName(self, username):
        try:
            user = self.get(username=username)
            return user
        except:
            raise

    def checkExists(self, username, email):
        try:
            usernameCount = self.filter().count(username=username)
            emailCount = self.filter().count(email=email)
            if usernameCount > 0 or emailCount > 0:
                return True
            return False
        except:
            raise