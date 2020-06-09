from django.forms import ModelForm, ModelChoiceField
from ..models import CNNModel

class DatasetOptionsChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.name

class ModelChangeForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CNNModel.CNNModel
        exclude = ('id', 'creation_date', 'model_path', 'user_id', 'dataset_id')