from django.views.generic.list import ListView
from ..models import CNNModel
from django.contrib.auth.mixins import LoginRequiredMixin
from expDjango import settings

class ListOfModels(ListView, LoginRequiredMixin):
    model = CNNModel.CNNModel
    paginate_by = 6
    login_url = settings.LOGOUT_REDIRECT_URL

    def get_queryset(self):
        CNNModel.CNNModel.objects.all().values('id', 'name', 'normalize_std', 'normalize_mean', 'output_dict',
                                               'dataset_id__name', 'user_id')\
                                                .order_by('name')

    def get_context_data(self,**kwargs):
        context = super(ListOfModels, self).get_context_data(**kwargs)
        context["user_id"] = self.request.user.id
        return context