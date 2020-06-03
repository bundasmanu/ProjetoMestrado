from django.forms import ModelForm
from ..models import Dataset
from expDjango import config
from django.contrib import messages
from expDjango import settings
import os

class DatasetCreationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(DatasetCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Dataset.Dataset
        exclude = ('id', 'creation_date', 'dataset_path','user_id') # tuple

    def save(self, commit=True):

        try:
            dataset = super(DatasetCreationForm, self).save(commit=False)
            dataset.user_id = self.request.user
            str_path = os.path.join(settings.DATASET_PATH, dataset.name) # get path string
            os.mkdir(str_path) # create path --> no return, if can't create raises exception (no problem here, because clean_name checks name validation)
            dataset.dataset_path = str_path # associate dataset_path with created model path
            if commit == True:
                dataset.save()
            return dataset
        except:
            raise

    def clean_name(self):

        '''
        This function represents the logic of validation of form
        :return:
        '''

        try:
            name = self.cleaned_data['name']
            if Dataset.Dataset.objects.filter(name=name).exists():
                messages.add_message(self.request, messages.ERROR, config.DATASET_ALREADY_EXISTS)
                return
            return name
        except:
            raise