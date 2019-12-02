from django import forms
from expDjango.Dataset.Models import Dataset


class DatasetTemp(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = '__all__'

