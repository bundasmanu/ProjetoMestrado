from django.forms import ModelForm, FileField, ModelChoiceField
from ..models import CNNModel
from ..validators import validate_model_file_extension
from datasets.models import Dataset
from expDjango import config

class DatasetOptionsChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.name

class ModelCreateForm(ModelForm):

    dataset_id_options = DatasetOptionsChoiceField(queryset=Dataset.Dataset.objects.all(), required=True) # the queryset needs to be always objects.all(), i can't put values --> "because it's going to save the relationships, so django have to use complete model objects, not certain values of model objects."
    file_upload = FileField(required=True, help_text='Supported extension file: .h5, max_size: 100MB', max_length=config.MAX_SIZE_OF_UPLOADED_MODEL,
                   error_messages={'required': 'Please pass a Keras model'}, validators=[validate_model_file_extension])

    class Meta:
        model = CNNModel.CNNModel
        fields = "__all__"
        exclude = ('id', 'creation_date', 'model_path', 'user_id', 'dataset_id')