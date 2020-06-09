from django.forms import ModelForm, ModelChoiceField
from ..models import CNNModel

class ModelCreateForm(ModelForm):

    dataset_id_options = ModelChoiceField(queryset=CNNModel.CNNModel.objects.all().values('dataset_id__name'))

    class Meta:
        model = CNNModel.CNNModel
        fields = '__all__'
        exclude = ('id', 'creation_date', 'model_path', 'user_id')