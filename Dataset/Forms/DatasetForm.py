from django import forms
from Dataset.models import Dataset


class DatasetTemp(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = '__all__'