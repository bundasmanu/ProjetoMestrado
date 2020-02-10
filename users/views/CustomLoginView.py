from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate
#https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.views.LoginView

class CustomLoginView(LoginView):
    template_name = 'users/Login.html' #--> DEFINIR LOGIN_URL NO SETTINGS --> https://stackoverflow.com/questions/56057801/how-to-set-custom-admin-login-url-in-django-admin-on-session-timeout
    #authentication_form --> IF I WANT TO OVERRIDE CUSTOM AUTHENTICATION_FORM --> I DECLARE NEW FORM HERE

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,  {"form" : self.form_class})

    #PODE VIR A SER NECESSÁRIO
    # def post(self, request, *args, **kwargs):
    #
    #     #CHECK AUTHENTICATION
    #     username = self.request.POST.get('username')
    #     password = self.request.POST.get('password')
    #     user = authenticate(username=username, password=password)
    #
    #     if user is None:
    #         return self.form_invalid(self.form_class)
    #
    #     return super(CustomLoginView, self).post(self.request)

    def form_invalid(self, form):
        try:
            self.clean_messages(self.request)
            messages.add_message(self.request, messages.INFO, 'ERROR ON FORM')
            return self.render_to_response(self.get_context_data()) #I NEED TO PASS CONTEXT DATA, IF I DON'T PASS IT, I CAN'T SEE FORM
        except:
            raise

    def get_success_url(self):
        try:
            self.clean_messages()
            path = reverse('users:home')
            return path
        except:
            raise

    #I NEED THIS METHOD TO OVERRIDE ALL MESSAGES CREATED ON USAGE BETWEEN TENTATIVES TO ACCESS TO APPLICATION --> https://stackoverflow.com/questions/42546006/deleting-clearing-django-contrib-messages
    def clean_messages(self):
        try:
            usedMessages = messages.get_messages(self.request)
            for message in usedMessages:
                pass
            usedMessages.used = True
        except:
            raise