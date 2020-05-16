from django.views.generic.edit import CreateView
from datasets.forms import DatasetCreationForm
from datasets.models import Dataset
from django.urls import reverse
from django.contrib import messages
from expDjango import config

class DatasetCreateView(CreateView):

    form_class = DatasetCreationForm.DatasetCreationForm
    model = Dataset.Dataset
    template_name = 'dataset/createDataset.html' # need to complement

    def get_form_kwargs(self, *args, **kwargs):
        form_args = super(DatasetCreateView, self).get_form_kwargs(*args, **kwargs)
        form_args['request'] = self.request # add request to creation form --> and to put message error
        return form_args

    def form_valid(self, form):

        '''
        This function overrides logic of form validation
        :param form: user form output after submit (post)
        :return: raise or HTTP Response Redirect
        '''

        try:
            return super(DatasetCreateView, self).form_valid(form)
        except:
            raise

    def form_invalid(self, form):
        form = DatasetCreationForm.DatasetCreationForm(request=self.request) # reset form --> reset errors to only appear once
        return super(DatasetCreateView, self).form_invalid(form)

    def get_success_url(self):

        '''
        This function defines the success path after form validation
        :return: reverse of a path
        '''

        try:
            storage = messages.get_messages(request=self.request)
            storage.used = True # clean old messages
            messages.add_message(self.request, messages.INFO, config.SUCCESS_DATASET_CREATION) # add message

            #pass kwargs with pk to ListSpecificDataset --> important need to kwargs because, get queryset method gets pk via kwargs, but i also can send via args, passing a tuple
            kwargs = {"pk" : self.object.id}
            path = reverse("datasets:ListaDatasetByID", kwargs=kwargs)
            return path
        except:
            raise
