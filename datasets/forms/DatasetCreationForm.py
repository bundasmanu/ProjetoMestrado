from django.forms import ModelForm
from ..models import Dataset
from expDjango import config
from django.contrib import messages

class DatasetCreationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(DatasetCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Dataset.Dataset
        exclude = ('id', ) # tuple

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