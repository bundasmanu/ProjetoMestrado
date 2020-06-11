from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
import expDjango.settings as settings
from ..forms import PredictForm
from django.contrib import messages
from expDjango import config
from modelos.models import CNNModel
from django.core.files.storage import default_storage
import os

class PredictView(LoginRequiredMixin, FormView):

    template_name = 'dataset/predict.html'
    login_url = settings.LOGOUT_REDIRECT_URL
    form_class = PredictForm.PredictForm

    def delete_image(self, image_url):

        '''
        This function is used to delete temporary images that are saved (images > 2.5MB)
        :param image_url: url of image
        :return: bool --> if True delete works well, if False problems occured in process
        '''

        try:
            if os.path.exists(image_url):
                os.remove(image_url) # os.remove doesn't have return, i.e. if it goes wrong it generates exception
                return True
        except:
            return False

    # this function is used to retrieve keras .h5 file, of selected model
    def get_model_object(self, model_id) -> CNNModel.CNNModel:

        '''
        This function is used to retrieve selected model object
        :param model_id: integer: id of model
        :return: CNNModel Object --> None if a problem occur
        '''

        try:

            model_object = CNNModel.CNNModel.objects.objects.all.filter(id=model_id)

            return model_object
        except:
            return None

    def pre_process_image(self, image, model: CNNModel.CNNModel):

        '''
        This function is used to apply pre-process technique to sample image, in concordance with normalized values passed on model creation and with keras file
        :param image: png, jpeg file
        :param model: CNNModel
        :return: image pre-processed
        '''

        try:



            return image
        except:
            return None


    def get_context_data(self, **kwargs):
        context = super(PredictView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):

        try:

            # collect form data
            dataset_id = form.cleaned_data['dataset_dropdown']
            model_id = form.cleaned_data['models_dropdown']
            image = form.cleaned_data['image_upload']

            # check if image is a temporary file, if it is i need to save image, otherwise image is loaded to memory, and i could use variable image directly
            url_image = None
            if image.size > config.SIZE_GREATER_TEMPORARY: # if file is greater than 2.5MB, i need to store is url
                url_image = image.file.name

            # process predict considering dataset and model --> i need to create a queryset that by model_id get's model file
            selected_model = self.get_model_object(model_id)

            # get File instance
            keras_file = default_storage.open(selected_model.model_path)

            # apply pre-process to image, using normalize_std and normalize_mean of selected model


            # close File instance
            keras_file.close()

            # if file is temporary (saved in disk >2.5MB) --> i need to delete them, in order to avoid memory problems
            if url_image is not None:
                safe_delete = self.delete_image(url_image)
                if safe_delete == False:
                    pass

            return
        except:
            storage = messages.get_messages(self.request)
            storage.used = True
            messages.add_message(self.request, messages.ERROR, config.ERROR_ON_PREDICT)

    def form_invalid(self, form):

        storage = messages.get_messages(self.request)
        storage.used = True
        messages.add_message(self.request, messages.ERROR, config.PLEASE_FILL_FORM_CORRECTLY)
        return super(PredictView, self).form_invalid(form)
