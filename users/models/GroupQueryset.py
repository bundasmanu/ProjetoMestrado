from django.contrib.auth.models import User, Group
from django.db import models
from .CustomUser import CustomUser

#REF --> https://www.re-cycledair.com/programmatically-adding-users-to-groups-in-django

class GroupQueryset(models.query.QuerySet):

    def getGroup(self, charGroup):
        try:
            group = Group.objects.get(name=charGroup)
            return group
        except Group.DoesNotExist:
            raise #RAISE THE EXCEPTION RETURNED BY GET FUNCTION
        except Group.MultipleObjectsReturned:
            raise

    def addUserToGroup(self, username, charGroup):
        try: #USER FOI INSERIDO NA BD --> ESTE METODO E CHAMADO AO MESMO TEMPO, QUE A SUA INSERCAO
            groupOfUser = self.getGroup(charGroup) #SE DER ERRO AS EXCECOES SAO TRATADAS NO METODO INVOCADO
            user = CustomUser.users.getUserByName(username)
            groupOfUser.user_set.add(user)
            return True
        except:
            return False