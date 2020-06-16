from django.forms import ModelForm, FileField
from ..models import CNNModel
from ..validators import validate_model_file_extension, check_output_dict
from . import DatasetOptionsChoiceField
from datasets.models import Dataset
from expDjango import config
from django.core.exceptions import ValidationError
import ast

class ModelCreateForm(ModelForm):

    dataset_id_options = DatasetOptionsChoiceField.DatasetOptionsChoiceField(queryset=Dataset.Dataset.objects.all(), required=True) # the queryset needs to be always objects.all(), i can't put values --> "because it's going to save the relationships, so django have to use complete model objects, not certain values of model objects."
    file_upload = FileField(required=True, help_text='Supported extension file: .h5, max_size: 100MB', max_length=config.MAX_SIZE_OF_UPLOADED_MODEL,
                   error_messages={'required': 'Please pass a Keras model'}, validators=[validate_model_file_extension])

    class Meta:
        model = CNNModel.CNNModel
        fields = "__all__"
        exclude = ('id', 'creation_date', 'model_path', 'user_id', 'dataset_id')

    def clean(self):
        cleaned_data = super(ModelCreateForm, self).clean()

        # first, call validator to check if user puts a correct dictionary
        check_output_dict(cleaned_data.get("output_dict"))

        # if it's a dictionary, check if the number of keys is equal to number of classes of selected dataset
        output_dict = ast.literal_eval(cleaned_data.get("output_dict")) # already checked on validator
        number_keys = len(output_dict.keys())
        if cleaned_data.get("dataset_id_options").n_classes != number_keys:
            raise ValidationError(
                "Incorrect number of classes on dictionary, dataset have: {} classes, and you pass {} classes on dict".format(
                    cleaned_data.get("dataset_id_options").n_classes, number_keys))