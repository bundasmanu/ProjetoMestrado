from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormMixin
from ..models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
import expDjango.settings as settings
from users.forms.CustomUserForm import CustomUserChangeForm
from django.core.exceptions import ObjectDoesNotExist
import expDjango.config as config
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, render

#REF, USE A FORM_VIEW INSIDE A DETAIL_VIEW --> https://stackoverflow.com/questions/45659986/django-implementing-a-form-within-a-generic-detailview

class DetailUserInfoView(LoginRequiredMixin, UpdateView):
    model = CustomUser.CustomUser
    template_name = 'users/InfoUser.html'
    login_url = settings.LOGOUT_REDIRECT_URL
    context_object_name = 'user'
    form_class = CustomUserChangeForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_initial(self):
        initial = super(DetailUserInfoView, self).get_initial()
        initial = initial.copy()
        initial[config.USERNAME] = self.request.user.username
        initial[config.FIRST_NAME] = self.request.user.first_name
        initial[config.LAST_NAME] = self.request.user.last_name
        return initial

    def get_context_data(self, **kwargs): #GET OBJECT ACTS AFTER THAN GET_OBJECT --> EXAMPLE OF GET_CONTEXT_DATA, I DIDN'T NEED THIS
        context = super(DetailUserInfoView, self).get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

    # def get(self, request, *args, **kwargs):
    #     form = super(DetailUserInfoView, self).get_form()
    #     initialBase = self.get_initial()
    #     form.initial = initialBase
    #     return render(request, self.template_name, {'form' : form, 'sp' : 'sp'})

    def form_valid(self, form):
        try:

            dataInForm = self.getContentOnForm(form)

            #CASE OBJECT IS NULL --> PROBLEMS ON CLEANED_DATA
            if dataInForm == None:
                raise ObjectDoesNotExist

            #NOW, IF USER MAKE CHANGES ON HIS DATA, I NEED TO MAKE A UPDATE QUERY TO SAVE HIS NEW VALUES
            dictValuesUpdatedData = { #https://stackoverflow.com/questions/49917796/update-django-object
                config.USERNAME : dataInForm.username,
                config.FIRST_NAME : dataInForm.first_name,
                config.LAST_NAME : dataInForm.last_name
            }
            self.model.objects.filter(pk=self.request.user.id).update(**dictValuesUpdatedData)

            #REDIRECT TO NEW PAGE
            return HttpResponseRedirect(self.get_success_url())
        except:
            raise

    def form_invalid(self, form):
        try:
            print(form.errors)
            self.clean_messages()
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

    def getContentOnForm(self, form):
        try:
            #CREATION OF NEW USER OBJECT, THAT AGGREGATES ALL DATA UPGRADED ON THE FORM
            dataUpdated = CustomUser.CustomUser

            dataUpdated.username = form.cleaned_data.get("username")
            dataUpdated.first_name = form.cleaned_data.get("first_name")
            dataUpdated.last_name = form.cleaned_data.get("last_name")

            return dataUpdated
        except:
            raise

    def clean_messages(self):
        try:
            usedMessages = messages.get_messages(self.request)
            for message in usedMessages:
                pass
            usedMessages.used = True
        except:
            raise

