from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from expDjango import settings
from django.contrib import messages
from expDjango import config as config
from django.urls import reverse
from users.models import CustomUser
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist

#REFS:
#https://gist.github.com/bmispelon/1851113
#https://github.com/django/django/blob/2.0/django/contrib/auth/views.py#L566
#https://docs.djangoproject.com/en/3.0/topics/auth/default/
#https://stackoverflow.com/questions/36350317/django-authentication-issue-after-reseting-password

class ChangeUserPasswordView(LoginRequiredMixin, UpdateView):
    form_class = PasswordChangeForm
    login_url = settings.LOGOUT_REDIRECT_URL
    template_name = 'users/ChangePassword.html'
    model = CustomUser.CustomUser

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, *args ,**kwargs):
        self.form_class = self.form_class(user=self.request.user)#INITIALIZATION OF PasswordChangeForm, NEEDS user instance
        kwargs = {'form' : self.form_class, #PASS FORM TO TEMPLATE
                  'user' : self.request.user}
        context = super().get_context_data(**kwargs)
        return context

    def get_form_kwargs(self): #METHOD USED TO DEFINE ARGUMENTS TO INITIALIZE FORM
        kwargs = super(ChangeUserPasswordView, self).get_form_kwargs()
        kwargs['user'] = kwargs.pop('instance') #NEED TO PUT OBJECT INSTANCE ON KWARG USER, AND POP FUNCTION, DELETES INSTANCE KWARG --> https://stackoverflow.com/questions/49218302/python-difference-between-kwargs-pop-and-kwargs-get
        return kwargs #KWARGS['USER'] IS NEEDED, TO FORM KNOW WHAT TYPE OF MODEL IS USED ON FORM, IN OTHER FORMS IN META, THE MODELS ARE DEFINED, IN THIS CASE SUCH AS A GENERIC FORM, I NEED TO DEFINE THIS

    def form_valid(self, form):
        try:

            #I DON'T NEED TO MAKE VALIDATION BECAUSE THIS VALIDATIONS ARE USED IN FORM: AdminPasswordChangeForm
            #I ONLY NEED TO CALL SAVE METHOD ON PasswordChangeForm FORM
            user = form.save() #RETURNS THE USER IF NEW PASS

            #CASE OBJECT IS NULL --> PROBLEMS ON CLEANED_DATA
            if user == None:
                raise ObjectDoesNotExist

            update_session_auth_hash(self.request, user)#CHANGES AUTOMATICALLY THE PASSSWORD OF USER AND HIS SESSION, AND USER IS NOT LOGGED OUT

            return HttpResponseRedirect(self.get_success_url())
        except:
            raise

    def form_invalid(self, form):
        try:
            self.clean_messages()
            #ADD MESSAGE TO RENDERED TEMPLATE, THAT WAS BEEN SHOW AFTER THAT
            messages.add_message(self.request, messages.INFO, config.ERROR_FORM_UPDATE_USER)
            return self.render_to_response(self.get_context_data())
        except:
            raise

    def get_success_url(self):
        try:
            self.clean_messages()
            #ADD MESSAGE --> CORRECT UPDATED VALUES
            messages.add_message(self.request, messages.INFO, config.CORRECT_UPDATES_VALUES_USER)
            path = reverse("users:info")
            return path
        except:
            raise

    #THIS METHOD IS USED, IN ORDER TO PUT AND CLEAN MESSAGES THAT ARE RENDERED TO TEMPLATE
    def clean_messages(self):
        try:
            usedMessages = messages.get_messages(self.request)
            for message in usedMessages:
                pass
            usedMessages.used = True
        except:
            raise