from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import CNNModel
from expDjango import settings
from ..forms import ModelChangeForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import default_storage
import os

class ModelChangeView(LoginRequiredMixin, UpdateView):
    model = CNNModel.CNNModel
    template_name = 'models/changeModel.html'
    login_url = settings.LOGOUT_REDIRECT_URL
    form_class = ModelChangeForm.ModelChangeForm

    def get_file_name(self):
        file_path = self.object.model_path
        return os.path.basename(file_path) # only filename without directories

    def get_queryset(self):
        queryset = super(ModelChangeView, self).get_queryset()
        model_id = self.kwargs["pk"]
        return queryset.filter(id=model_id)
    
    def get_context_data(self, **kwargs):
        context = super(ModelChangeView, self).get_context_data(**kwargs)
        context["actual_file"] = self.get_file_name()
        return context
    
    def get_form_kwargs(self):
        kwargs = super(ModelChangeView, self).get_form_kwargs()

        # i need to send initial model values to form, to put initial data on fields
        kwargs["name"] = self.object.name
        kwargs["normalize_std"] = self.object.normalize_std
        kwargs["normalize_mean"] = self.object.normalize_mean
        kwargs["output_dict"] = self.object.output_dict
        kwargs["dataset_id"] = self.object.dataset_id

        return kwargs

    def form_valid(self, form):

        # get all form content, and don't commit the object, in order to change the other elements, not implicitly referenced in the form
        self.object = form.save(commit=False)

        # get selected dataset
        self.object.dataset_id = form.cleaned_data["dataset_id_options"]

        # get uploaded file --> if not exists, and i don't need to make anything,
        # if exists i need to check if it's equal to the current model, and if it is i don't need to make anything,
        # but if uploaded model is different from current model, i need to change model path, and delete current model and save new model
        uploaded_file = form.cleaned_data["file_upload"]
        if uploaded_file != None: # if user uploaded a model
            if uploaded_file.name != self.get_file_name(): # if uploaded file is different from current file, then i need to change model path, and delete and save respectively old and new model
                old_path = self.object.model_path # full directory where is file: C:/../../file.h5
                parent_path = os.path.abspath(os.path.join(old_path, os.pardir)) # get parent directory folder: C:/../Breast_Histopathology
                default_storage.delete(old_path) # delete old file
                new_path = os.path.join(parent_path, uploaded_file.name) # new path to save file: C:/../Breast_Histopathology/new_file.h5
                default_storage.save(new_path, uploaded_file) # save file in directory (new_path)
                self.object.model_path = new_path # change model path to new path

        # commit object
        form.save(commit=True)

        # redirect to new page
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        # if form is invalid, i reset form with initial values
        print(form.errors)
        messages.error(self.request, "Erro ao atualizar o modelo") # send error message to template
        kwargs = self.get_form_kwargs()
        form = ModelChangeForm.ModelChangeForm(**kwargs) # reset form with initial values
        return super(ModelChangeView, self).form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Modelo atualizado com sucesso")
        path = reverse('modelos:listaModels')
        return path