from django.forms import ModelForm
from ..models import Dataset

class DatasetChangeForm(ModelForm):

    class Meta:
        model = Dataset.Dataset
        exclude = ('id',)  # tuple