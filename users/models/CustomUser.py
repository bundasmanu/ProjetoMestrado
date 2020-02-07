from django.contrib.auth.models import AbstractUser
from django.db import models
import expDjango.config as config
from .BaseUserManager import BaseUserManager
from .UserQueryset import UserQueryset

#DEFINICAO DO MANAGER PARA O USER, EXISTEM DUAS FORMAS POSSÍVEIS, OPTEI PELA MAIS SIMPLES --> https://groups.google.com/forum/#!topic/django-users/loVv-yYH2qg
UserManager = BaseUserManager.from_queryset(UserQueryset)

class CustomUser(AbstractUser):

    userType = models.CharField(max_length=50, choices=
                        (('D' , config.DATASCIENTIST),
                         ('A', config.ADMIN),
                        ('H' , config.HEALTHCARE)))
    username = models.CharField(unique=True, max_length=50)

    #MANAGER COM DEPENDENCIA DIRETA PARA O QUERYSET, RESPEITANDO AS NORMAS DE PROGRAMACAO DRY --> https://stackoverflow.com/questions/45957142/django-model-manager-or-django-queryset
    users = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password'] #EMAIL AND PASSWORD ARE REQUIRED BY DEFAULT --> É AQUI QUE SE COLOCAM OS ATRIBUTOS QUE SAO UTILIZADOS NA CRIACAO DE UM UTILIZADOR

    def __str__(self):
        return self.username
