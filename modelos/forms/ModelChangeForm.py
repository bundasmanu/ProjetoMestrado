from django.forms import ModelForm, FileField
from ..models import CNNModel
from . import DatasetOptionsChoiceField
from datasets.models import Dataset
from ..validators import validate_model_file_extension, check_output_dict
from django.core.exceptions import ValidationError
from expDjango import config
import ast

class ModelChangeForm(ModelForm):

    dataset_id_options = DatasetOptionsChoiceField.DatasetOptionsChoiceField(queryset=Dataset.Dataset.objects.all(), required=False) # the queryset needs to be always objects.all(), i can't put values --> "because it's going to save the relationships, so django have to use complete model objects, not certain values of model objects."
    file_upload = FileField(required=False, help_text='Supported extension file: .h5, max_size: 100MB',
                            max_length=config.MAX_SIZE_OF_UPLOADED_MODEL, validators=[validate_model_file_extension])

    def __init__(self, *args, **kwargs):

        # retrieve values from kwargs
        initial_name = kwargs.pop("name")
        initial_normalized_std = kwargs.pop("normalize_std")
        initial_normalized_mean = kwargs.pop("normalize_mean")
        initial_output_dict = kwargs.pop("output_dict")
        initial_dataset_id = kwargs.pop("dataset_id")
        initial_input_shape = kwargs.pop("input_shape")

        # call constructor, without kwargs values (pop drop his values)
        super(ModelChangeForm, self).__init__(*args, **kwargs)

        # declare initial fields with this values
        self.fields["name"].initial = initial_name
        self.fields["normalize_std"].initial = initial_normalized_std
        self.fields["normalize_mean"].initial = initial_normalized_mean
        self.fields["output_dict"].initial = initial_output_dict
        self.fields["dataset_id_options"].initial = initial_dataset_id
        self.fields["input_shape"].initial = initial_input_shape

    class Meta:
        model = CNNModel.CNNModel
        exclude = ('id', 'creation_date', 'model_path', 'user_id', 'dataset_id')
    
    def clean(self):
        cleaned_data = super(ModelChangeForm, self).clean()

        # first, call validator to check if user puts a correct dictionary
        check_output_dict(cleaned_data.get("output_dict"))

        # if it's a dictionary, check if the number of keys is equal to number of classes of selected dataset
        output_dict = ast.literal_eval(cleaned_data.get("output_dict")) # already checked on validator
        number_keys = len(output_dict.keys())
        if cleaned_data.get("dataset_id_options").n_classes != number_keys:
            raise ValidationError("Incorrect number of classes on dictionary, dataset have: {} classes, and you pass {} classes on dict".format(cleaned_data.get("dataset_id_options").n_classes, number_keys))