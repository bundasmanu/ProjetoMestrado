from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from ..models import Dataset
import json
from expDjango import settings

class DatasetDeleteView(DeleteView, LoginRequiredMixin):
    model = Dataset.Dataset
    login_url = settings.LOGOUT_REDIRECT_URL
    template_name = 'dataset/deleteDatasetForm.html'

    def get_queryset(self):
        queryset = super(DatasetDeleteView, self).get_queryset()
        id_user_to_delete = self.kwargs["pk"]
        return queryset.filter(id=id_user_to_delete)

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        delete_sucess = {'sucess' : 'ok'}
        return HttpResponse(json.dumps(delete_sucess), content_type='application/json')