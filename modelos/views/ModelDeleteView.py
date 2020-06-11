from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from ..models import CNNModel
from expDjango import settings
from django.contrib import messages
import json
import shutil
import os

class ModelDeleteView(LoginRequiredMixin, DeleteView):
    model = CNNModel.CNNModel
    template_name = 'models/deleteModelForm.html'
    login_url = settings.LOGOUT_REDIRECT_URL

    def delete(self, request, *args, **kwargs):

        try:
            # get object, i can also use get_object method
            self.object = self.get_object()

            # first, i need to drop object from database, if a problem occur in delete file already exists, and if a problem occurs on delete directory with file the objects already doesn't exists, and there are no problems (even if it is not possible to delete the file from the local system, because the object no longer exists in bd)
            self.object.delete()

            # before deleting the object from the database, you must delete the model_path created with the .h5 file
            model_path = self.object.model_path # path where the file is located

            # get parent directory where file is located, e.g, directory with model creation (unique identifier of model)
            path_to_drop = os.path.abspath(os.path.join(model_path, os.pardir))

            # drop directory
            shutil.rmtree(path_to_drop, ignore_errors=True)

            # add success message to listModels page
            messages.success(request, "Dataset eliminado com sucesso")
            delete_sucess = {'sucess': 'ok'}

            return HttpResponse(json.dumps(delete_sucess), content_type='application/json')

        except:
            messages.success(request, "Erro ao eliminar o dataset")
            delete_insucess = {'sucess': 'error'}
            return HttpResponse(json.dumps(delete_insucess), content_type='application/json')