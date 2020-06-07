from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from ..models import Dataset
import json
from expDjango import settings
from django.contrib import messages

class DatasetDeleteView(DeleteView, LoginRequiredMixin):
    model = Dataset.Dataset
    login_url = settings.LOGOUT_REDIRECT_URL
    template_name = 'dataset/deleteDatasetForm.html'

    def get_queryset(self):
        queryset = super(DatasetDeleteView, self).get_queryset()
        id_user_to_delete = self.kwargs["pk"]
        return queryset.filter(id=id_user_to_delete)

    def delete(self, request, *args, **kwargs):
        try:
            self.get_object().delete()
            delete_sucess = {'sucess' : 'ok'}
            messages.success(request, "Dataset eliminado com sucesso") # add success message to listDataset page, after success delete of dataset
            return HttpResponse(json.dumps(delete_sucess), content_type='application/json')
        except:
            messages.error(request, "Erro ao eliminar o dataset")