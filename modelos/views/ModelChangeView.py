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
import time
import shutil

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
        kwargs["input_shape"] = self.object.input_shape

        return kwargs

    def form_valid(self, form):

        # get all form content, and don't commit the object, in order to change the other elements, not implicitly referenced in the form
        self.object = form.save(commit=False)

        # get selected dataset
        old_dataset_id = self.object.dataset_id
        self.object.dataset_id = form.cleaned_data["dataset_id_options"]

        # get uploaded file --> if not exists, and i don't need to make anything,
        # if exists i need to check if it's equal to the current model, and if it is i don't need to make anything,
        # but if uploaded model is different from current model, i need to change model path, and delete current model and save new model
        uploaded_file = form.cleaned_data["file_upload"]
        if old_dataset_id == self.object.dataset_id:  # no changes in selected dataset
            if uploaded_file != None: # if user uploaded a model
                if uploaded_file.name != self.get_file_name(): # if uploaded file is different from current file, then i need to change model path, and delete and save respectively old and new model

                    old_path = self.object.model_path # full directory where is file: C:/../../file.h5

                    # loop to parent directories --> C:/Breast_Histopathology/2/2020-06-10/file.h5 to C:/Breast_Histopathology/2
                    parent_path = old_path
                    for i in range(2):
                        parent_path = os.path.abspath(os.path.join(parent_path, os.pardir)) # get parent directory folder: C:/../Breast_Histopathology

                    # create new date time folder with the date of file update
                    new_folder_of_file = os.path.join(parent_path, time.strftime("%Y%m%d-%H%M%S"))

                    # delete parent path
                    shutil.rmtree(os.path.abspath(os.path.join(old_path, os.pardir)), ignore_errors=True)

                    # put file on new folder
                    new_path_with_file = os.path.join(new_folder_of_file, uploaded_file.name) # new path to save file: C:/../Breast_Histopathology/new_file.h5

                    # save file
                    default_storage.save(new_path_with_file, uploaded_file) # save file in directory (new_path)

                    # change model path of object
                    self.object.model_path = new_path_with_file

        else: # selected dataset is different from old dataset, then i need to delete current path's, and put in new path folder (dataset folder)

            old_path = self.object.model_path # get current path

            # save file (if user doesn't pass a new file)
            model_file = default_storage.open(old_path) # i need to open file in order to save this file in new directory, witn user doesn't provide a new model

            #definition of path to save model
            dataset_path = os.path.join(settings.DATASET_PATH, self.object.dataset_id.name) # path in concordance to selected dataset, e.g, C:/../Breast_Histopathology
            path_with_user_id = os.path.join(dataset_path, str(self.request.user.id))
            path_with_date_of_creation = os.path.join(path_with_user_id, time.strftime("%Y%m%d-%H%M%S"))

            # save file
            if uploaded_file == None: # if the user passed a model
                path_with_filename = os.path.join(path_with_date_of_creation, os.path.basename(model_file.name))
                default_storage.save(path_with_filename, model_file)
            else: # if the user did not pass a model
                path_with_filename = os.path.join(path_with_date_of_creation, uploaded_file.name)
                default_storage.save(path_with_filename, uploaded_file)

            # get user path with file: /../2/2020-06-10/file.h5 --> get /2020-06-10
            model_file.close() # close the file in order to delete folder, otherwise it generates an exception, saying that the file is in use
            shutil.rmtree(os.path.abspath(os.path.join(old_path, os.pardir)), ignore_errors=True) # delete directory associative to user and file

            # define new model path
            self.object.model_path = path_with_filename

        # commit object
        form.save(commit=True)

        # redirect to new page
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        # if form is invalid, i reset form with initial values
        errors_dict = dict(form.errors)
        if "input_shape" in errors_dict: # only appears one error at each time --> logic if elif
            first_error = errors_dict.get('input_shape').data[0].message
            messages.error(self.request, first_error)
        elif "output_dict" in errors_dict:
            first_error = errors_dict.get('output_dict').data[0].message
            messages.error(self.request, first_error)
        elif "file_upload" in errors_dict:
            first_error = errors_dict.get('file_upload').data[0].message
            messages.error(self.request, first_error)
        kwargs = self.get_form_kwargs()
        form = ModelChangeForm.ModelChangeForm(**kwargs) # reset form with initial values
        return super(ModelChangeView, self).form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Modelo atualizado com sucesso")
        path = reverse('models:listaModels')
        return path