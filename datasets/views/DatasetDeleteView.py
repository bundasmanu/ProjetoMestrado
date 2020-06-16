from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from ..models import Dataset
import json
from expDjango import settings
from django.contrib import messages
import shutil

class DatasetDeleteView(DeleteView, LoginRequiredMixin):
    model = Dataset.Dataset
    login_url = settings.LOGOUT_REDIRECT_URL
    template_name = 'dataset/deleteDatasetForm.html'

    def get_queryset(self):
        queryset = super(DatasetDeleteView, self).get_queryset()
        id_dataset_to_delete = self.kwargs["pk"]
        return queryset.filter(id=id_dataset_to_delete)

    def delete(self, request, *args, **kwargs):
        try:

            # before delete dataset, i need to drop all .h5 models that have been saved on his model_path folder
            try:
                shutil.rmtree(self.get_object().dataset_path, ignore_errors=True)
            except:
                pass

            # delete dataset - cascade option delete all models and history of user, i don't need to do anything
            self.get_object().delete()
            delete_sucess = {'sucess' : 'ok'}
            messages.success(request, "Dataset eliminado com sucesso") # add success message to listDataset page, after success delete of dataset
            return HttpResponse(json.dumps(delete_sucess), content_type='application/json')
        except:
            messages.success(request, "Erro ao eliminar o dataset")
            delete_insucess = {'sucess': 'error'}
            return HttpResponse(json.dumps(delete_insucess), content_type='application/json')