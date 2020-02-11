from django.views.generic.detail import DetailView
from ..models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
import expDjango.settings as settings

class DetailUserInfoView(LoginRequiredMixin, DetailView):
    model = CustomUser.CustomUser
    template_name = 'users/InfoUser.html'
    login_url = settings.LOGOUT_REDIRECT_URL
    context_object_name = 'user'

    def get_object(self):
        self.model = self.request.user
        return self.model

    # def get_context_data(self, **kwargs): #GET OBJECT ACTS AFTER THAN GET_OBJECT --> EXAMPLE OF GET_CONTEXT_DATA, I DIDN'T NEED THIS
    #     context = super().get_context_data(**kwargs)
    #     context['custom'] = self.model
    #     return context