from django.forms import ModelForm
from ..models import Dataset
from django.contrib import messages
from expDjango import config

class DatasetChangeForm(ModelForm):

    # https://stackoverflow.com/questions/50041919/django-testform-object-has-no-attribute-fields
    def __init__(self, *args, **kwargs):

        # get kwargs values and eliminate them, in order to not pass them to ModelForm constructor
        self.request = kwargs.pop("request", None)
        initial_name = kwargs.pop("name", None) # if not exists return None
        initial_nClasses = kwargs.pop("n_classes", None) # if not exists return None
        initial_nSamples = kwargs.pop("n_samples", None) # if not exists return None
        initial_linkInfo = None
        if "link_info" in kwargs:
            initial_linkInfo = kwargs.pop("link_info", None)

        # i need to construct ModelForm first, to change initial fields values
        super(DatasetChangeForm, self).__init__(*args, **kwargs)

        # set fields
        self.fields["name"].initial = initial_name
        self.fields["n_classes"].initial = initial_nClasses
        self.fields["n_samples"].initial = initial_nSamples
        if initial_linkInfo != None:
            self.fields["link_info"].initial = initial_linkInfo

    class Meta:
        model = Dataset.Dataset
        exclude = ('id', 'user_id', 'creation_date', 'dataset_path')  # tuple
    
    def save(self, commit=True):
        return super(DatasetChangeForm, self).save(commit)
    
    def clean_name(self):

        '''
        This function represents the logic of validation of form
        :return:
        '''

        try:
            name = self.cleaned_data['name']
            if Dataset.Dataset.objects.filter(name=name).exists() and name != self.fields["name"].initial:
                messages.add_message(self.request, messages.ERROR, config.DATASET_ALREADY_EXISTS)
                return
            return name
        except:
            raise