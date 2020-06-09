from django.views.generic.edit import CreateView
from ..models import CNNModel
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import ModelCreateForm
from expDjango import settings
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage
import os
import time

class ModelCreateView(LoginRequiredMixin, CreateView):
    model = CNNModel.CNNModel
    form_class = ModelCreateForm.ModelCreateForm
    template_name = 'models/createModel.html'
    login_url = settings.LOGOUT_REDIRECT_URL

    def form_valid(self, form):

        # first i need to get data object from form, using save method --> commit = False, because i didn't fill all required fields
        self.object = form.save(commit=False)

        # association of all excluded files on ModelCreateForm
        # association of logged user to user that creates this model
        self.object.user_id = self.request.user

        # association of dataset_id with selected dataset object
        selected_dataset = form.cleaned_data["dataset_id_options"]
        self.object.dataset_id = selected_dataset

        # ref: default_storage (how save and get a file): https://stackoverflow.com/questions/26274021/simply-save-file-to-folder-in-django
        # add file to selected dataset folder
        dataset_path = os.path.join(settings.DATASET_PATH, selected_dataset.name)  # get string of dataset folder (that aggregates all it's models)
        uploaded_file_name = form.cleaned_data["file_upload"].name

        #define unique id to model path: /user_id/date_time_now/file.h5
        path_with_user_id = os.path.join(dataset_path, str(self.request.user.id))
        path_with_user_id_and_current_date = os.path.join(path_with_user_id, time.strftime("%Y%m%d-%H%M%S"))
        model_file_path = os.path.join(path_with_user_id_and_current_date, uploaded_file_name)  # add uploaded file to path

        # associate model path to table
        self.object.model_path = model_file_path

        # now i need to save file on respective folder (model path)
        default_storage.save(model_file_path, form.cleaned_data["file_upload"])

        # now i need to commit new model object
        self.object = form.save(commit=True)

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, "Insira um modelo Keras válido")
        form = ModelCreateForm.ModelCreateForm()
        return super(ModelCreateView, self).form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Modelo criado com sucesso")
        path = reverse('modelos:listaModels')
        return path