from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
import expDjango.settings as settings
from ..forms import PredictForm
from django.contrib import messages
from expDjango import config
from modelos.models import CNNModel
from history.models import History
from tensorflow.keras.models import load_model
from django.core.files.storage import default_storage
import cv2
import numpy as np
from collections import OrderedDict
import ast
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

class PredictView(LoginRequiredMixin, FormView):

    template_name = 'dataset/predict.html'
    login_url = settings.LOGOUT_REDIRECT_URL
    form_class = PredictForm.PredictForm

    def get_context_data(self, **kwargs):
        context = super(PredictView, self).get_context_data(**kwargs)
        context["have_results"] = "false" # if user makes a predict this key is overrided
        return context

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
            raise

    # this function is used to retrieve keras .h5 file, of selected model
    def get_model_object(self, model_id) -> CNNModel.CNNModel:

        '''
        This function is used to retrieve selected model object
        :param model_id: integer: id of model
        :return: CNNModel Object --> None if a problem occur
        '''

        try:

            queryset = CNNModel.CNNModel.objects.all().filter(id=model_id)
            model_object = queryset.get()

            return model_object
        except:
            return None

    def resize_and_transform_to_array(self, image, model: CNNModel.CNNModel):

        '''
        This function is used to apply pre-process technique to sample image, in concordance with normalized values passed on model creation and with keras file
        :param image: png, jpeg file
        :param model: CNNModel
        :return: image pre-processed
        '''

        try:

            # get input_shape of object
            input_shape = tuple(map(int, model.input_shape.split(', ')))

            # read image
            image_read = cv2.imread(image)

            # apply resize of image
            x = cv2.resize(image_read, (input_shape[0], input_shape[1])) #input_shape[0] represents height and input_shape[1] represents width

            return np.array(x)
        except:
            return None

    def normalize_data(self, sample_array, model: CNNModel.CNNModel):

        '''
        This function is used to apply standardization technique to sample array, using training std and mean values of training data
        :param sample_array: numpy array: sample numpy array with shape (1, height, width, channels)
        :param model: CNNModel object: selected model
        :return: numpy array with each pixel standardized
        '''

        try:

            # convert strings normalized tuples to numpy array with dtype float32
            normalized_mean = np.array(model.normalize_mean.split(', '))
            normalized_std = np.array(model.normalize_std.split(', '))
            normalized_mean = np.asarray(normalized_mean, dtype=np.float64)
            normalized_std = np.asarray(normalized_std, dtype=np.float64)

            # apply normalization to all pixels of sample array
            sample_array = (sample_array - normalized_mean)/(normalized_std+1e-7)

            return sample_array

        except:
            return None

    def interpreting_results(self, prediction, dictionary_model):

        '''
        This function is used to define a dictionary with results per class (dictionary defined when the model was submitted by the user)
        :param prediction: numpy array, with shape (classes, ) --> predict value for each class
        :param dictionary_model: dictionary with classes names order
        :return: dictionary with predict value for each class
        '''

        try:

            # if values are not integers, i need convert them, and sort by values
            sorted_classes = OrderedDict(sorted(dictionary_model.items(), key=lambda t: int(t[1])))

            preds_by_class = dict()
            if len(sorted_classes) == prediction.shape[1]:  # needs to have same size, e.g, the number of declared classes on dictionary needs to be equal to number of predictions
                # i need to define new dictionary that for each key, put prediction value on them
                counter = 0
                for key, value in sorted_classes.items():
                    preds_by_class[key] = str(round(prediction[0][counter] * 100, 2))+"%" # round to "Hundredths" (centésimas)
                    counter = counter + 1

                return preds_by_class
        except:
            pass

    def form_valid(self, form):

        try:

            # collect form data
            if form.cleaned_data['dataset_dropdown'] == 'Selecciona um dataset' or form.cleaned_data['models_dropdown'] == 'Selecciona um modelo':
                raise NotImplementedError
            dataset_id = int(form.cleaned_data['dataset_dropdown'])
            model_id = int(form.cleaned_data['models_dropdown'])
            image = form.cleaned_data['image_upload'] # raises automatically

            # check if image is a temporary file, if it is i need to save image, otherwise image is loaded to memory, and i could use variable image directly
            url_image = None
            image_name = None
            if image.size > config.SIZE_GREATER_TEMPORARY: # if file is greater than 2.5MB, i need to store is url
                url_image = image.file.name
            else: # if it's a temporary file, i need to save them, in order to convert image to numpy array using cv2
                # ref: https://twigstechtips.blogspot.com/2012/04/django-how-to-save-inmemoryuploadedfile.html
                image_name = default_storage.save(image.name, image)

            # open image file
            image_file = None
            if image_name != None:
                image_file = default_storage.open(image_name)

            # process predict considering dataset and model --> i need to create a queryset that by model_id get's model file
            selected_model = self.get_model_object(model_id)

            # get File instance
            path_of_model = selected_model.model_path

            # first i need to transform image into numpy array, and if image is larger than input dimensions of model, i need to resize
            sample_data = None
            if url_image != None:
                sample_data = self.resize_and_transform_to_array(url_image, selected_model)
            else:
                sample_data = self.resize_and_transform_to_array(image_file.name, selected_model)

            if np.any(sample_data) == None: # if return value of resize_and_transform_to_array is None, then i can't continue the sample prediction process
                messages.error(self.request, "Definiu incorretamente o input_shape do modelo, ou o modelo não é condizente com o input_shape, altere o modelo")
                return self.render_to_response(self.get_context_data(form=PredictForm.PredictForm))

            # reshape sample_data from 3D to 4D --> e.g (50, 50, 3) to (1, 50, 50, 3)
            sample_data = sample_data.reshape(1, sample_data.shape[0], sample_data.shape[1], sample_data.shape[2])

            # apply pre-process technique in sample array, considering normalize_std and normalize_mean of training data, using in data definition (pre-processing)
            sample_data = self.normalize_data(sample_data, selected_model)

            if np.any(sample_data) == None:
                messages.error(self.request, "Definiu incorretamente o valor std e mean training do modelo, altere o modelo")
                return self.render_to_response(self.get_context_data(form=PredictForm.PredictForm))

            # predict value of sample
            load_file = load_model(path_of_model)

            # make prediction
            prediction = load_file.predict(sample_data)

            # convert output dict of model from string to dict
            dict_with_model_classes = ast.literal_eval(selected_model.output_dict)

            # get predictions by class
            preds_by_class = self.interpreting_results(prediction, dict_with_model_classes)

            # if file is temporary (saved in disk >2.5MB) --> i need to delete them, in order to avoid memory problems
            if url_image is not None:
                image.close()
                safe_delete = self.delete_image(url_image)
                if safe_delete == False:
                    pass
            else: # if it's a temporary file i need to remove them
                image_file.close()
                if os.path.exists(image_file.name):
                    os.remove(image_file.name)

            # add user action (sample predict -> to history table)
            History.History.objects.create(user_id=self.request.user, dataset_id_id=dataset_id,
                                           model_id=selected_model) # i already have user and model object, i just don't have dataset, then i need to pass dataset id (and create gets respectively object)

            # render to response to same page, but send to template preds_by_class dictionary with results --> form is resetted
            form = PredictForm.PredictForm() # reset form
            context = self.get_context_data(form=form)
            context["preds_by_classes"] = preds_by_class
            context["haveResults"] = "true"

            return self.render_to_response(context)
        except ValueError:
            messages.error(self.request,"Definiu incorretamente o input_shape do modelo, ou as dimensões iniciais do modelo, não coincidem com o input_shape, altere o modelo")
            return self.render_to_response(self.get_context_data(form=PredictForm.PredictForm()))
        except IOError:
            messages.error(self.request, "Erro no loading do modelo, confirme o ficheiro submetido")
            return self.render_to_response(self.get_context_data(form=PredictForm.PredictForm()))
        except NotImplementedError:
            if form.cleaned_data['dataset_dropdown'] == 'Selecciona um dataset':
                messages.error(self.request, "Seleccione um dataset")
            else:
                messages.error(self.request, "Seleccione um modelo")
            return self.render_to_response(self.get_context_data(form=PredictForm.PredictForm()))
        except:
            messages.error(self.request, "Erro na previsão do modelo")
            return self.render_to_response(self.get_context_data(form=PredictForm.PredictForm()))

    def form_invalid(self, form):

        storage = messages.get_messages(self.request)
        storage.used = True
        errors_dict = dict(form.errors)
        if "image_upload" in errors_dict:
            if errors_dict.get('image_upload').data[0].message == "Upload a valid image. The file you uploaded was either not an image or a corrupted image.":
                first_error = errors_dict.get('image_upload').data[0].message
                messages.error(self.request, first_error)
            else: # required message error
                messages.error(self.request, "Please choose an image")
        form = PredictForm.PredictForm() # reset form
        return super(PredictView, self).form_invalid(form)