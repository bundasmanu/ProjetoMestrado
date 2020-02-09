from django.contrib.auth.views import LoginView

#https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.views.LoginView

class CustomLoginView(LoginView):
    template_name = ''
    #authentication_form --> IF I WANT TO OVERRIDE CUSTOM AUTHENTICATION_FORM --> I DECLARE NEW FORM HERE

    def get(self, request, *args, **kwargs):
        return None #I NEED TO OVERRIDE THIS

    def post(self, request, *args, **kwargs):
        return None #I NEED TO OVERRIDE THIS

    #DEPOIS VER LOGIN_REDIRECT_URL --> https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-LOGIN_REDIRECT_URL