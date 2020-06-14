from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser

class EntryPage(LoginRequiredMixin, TemplateView):
    template_name = 'users/SlideShowEntryPage.html'

    def get_context_data(self, **kwargs):
        context = super(EntryPage, self).get_context_data(**kwargs)
        context["user_name"] = self.request.user.username
        return context