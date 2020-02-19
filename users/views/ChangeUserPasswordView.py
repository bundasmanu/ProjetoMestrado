from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from expDjango import settings
from django.contrib import messages
from expDjango import config as config
from django.urls import reverse
from users.models import CustomUser
from django.shortcuts import HttpResponseRedirect, get_object_or_404

class ChangeUserPasswordView(LoginRequiredMixin, UpdateView):
    form_class = PasswordChangeForm
    login_url = settings.LOGOUT_REDIRECT_URL
    template_name = 'users/ChangePassword.html'
    model = CustomUser.CustomUser
    #pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.request.user.id)

    def get_context_data(self, *args ,**kwargs):
        form =self.form_class(user=self.request.user)
        kwargs = {'form' : form}
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        try:

            #I DON'T NEED TO MAKE VALIDATION BECAUSE THIS VALIDATIONS ARE USED IN FORM: AdminPasswordChangeForm
            #I ONLY NEED TO CALL SAVE METHOD ON PasswordChangeForm FORM
            self.form_class.save()

            #self.model.objects.filter(pk=user.id).update(password=user.password)

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