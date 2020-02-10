from django.contrib.auth.views import LoginView
from ..models import CustomUser
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
#https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.views.LoginView

class CustomLoginView(LoginView):
    template_name = 'users/Login.html' #--> DEFINIR LOGIN_URL NO SETTINGS --> https://stackoverflow.com/questions/56057801/how-to-set-custom-admin-login-url-in-django-admin-on-session-timeout
    #authentication_form --> IF I WANT TO OVERRIDE CUSTOM AUTHENTICATION_FORM --> I DECLARE NEW FORM HERE

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,  {"form" : self.form_class})

    def post(self, request, *args, **kwargs):

        try:
            if self.form_valid():
                formRetrieved = self.form_class(request.POST, instance=CustomUser.CustomUser)

                username = formRetrieved.cleaned_data.get('username')
                password = formRetrieved.cleaned_data.get('password')

                #CHECK AUTENTHICATION
                auth = authenticate(username=username, password=password)
                if auth is not None:
                    login(username, password)
                    return HttpResponse("Signed in")
                else:
                    return HttpResponse("Problem in authentication")
        except:
            raise

    def form_valid(self, form):
        return True

    #DEPOIS VER LOGIN_REDIRECT_URL --> https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-LOGIN_REDIRECT_URL

    def form_invalid(self, form):
        return self.render_to_response()
