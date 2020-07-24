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

        # if it's a dictionary, check if the number of keys is equal to number of classes of selected dataset
        try:
            output_dict = ast.literal_eval(cleaned_data.get("output_dict"))  # already checked on validator
        except:
            raise ValidationError("Invalid Output dictionary")
        number_keys = len(output_dict.keys())
        if cleaned_data.get("dataset_id_options").n_classes != number_keys:
            raise ValidationError(
                "Incorrect number of classes on dictionary, dataset have: {} classes, and you pass {} classes on dict".format(
                    cleaned_data.get("dataset_id_options").n_classes, number_keys))

        # check if input shape corresponds with an grayscale or rgb image
        input_shape = cleaned_data.get("input_shape")
        res = tuple(map(int, input_shape.split(', ')))
        if len(res) == 3:
            if res[2] not in (1, 3):
                raise ValidationError(
                    "Please pass a correct tuple, last dimension need to be 1 (grayscale) or 3 (RGB) channels")
        else:
            raise ValidationError("Incorrect number of dimensions of tuple, please pass a tuple with three dimensions")

        # check if number of normalized values is coherent to input shape dimensions
        normalized_mean = cleaned_data.get("normalize_mean")
        normalized_std = cleaned_data.get("normalize_std")
        try:
            res_norm_mean = tuple(map(float, normalized_mean.split(', ')))
            res_norm_std = tuple(map(float, normalized_std.split(', ')))
        except:
            raise ValidationError("Invalid normalized values")
        if all(res[2] == x for x in (len(res_norm_mean), len(res_norm_std))) == False: # input shape channels, need to be equal to dimensions of normalize_mean and normalize_std
            raise ValidationError(
                "Mismatch between input shape dimensions, and normalized mean tuple and std tuple")