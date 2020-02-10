from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.shortcuts import redirect
from django.urls import reverse

class HomeRedirectView(TemplateView):
    template_name = 'users/Home.html'

#LINK MUITO INTERESSANTE PARA DIFERENTES REDIRECTS CONSOANTE O TIPO DE UTILIZADOR --> https://stackoverflow.com/questions/32259242/can-i-set-different-template-names-inside-of-django-templateview