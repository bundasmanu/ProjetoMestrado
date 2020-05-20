from django import forms
from ..models import Dataset
from django.db.models import Count

def queysets():

    # get only dataset's with models associated
    number_models = Dataset.Dataset.objects.all().annotate(numbermodels=Count('cnnmodel'))
    number_models = number_models.exclude(numbermodels=0)

    return number_models

class PredictForm(forms.Form):

    # fields
    dataset_choices = [(x.id, x.name) for x in queysets()]
    dataset_choices.insert(0, ('', 'Selecciona Dataset'))
    models_choices = []
    models_choices.insert(0, ('', 'Selecciona Modelo'))

    dataset_dropdown = forms.CharField(label="Dataset",
                                        widget=forms.Select(choices=dataset_choices), required=True)
    models_dropdown = forms.CharField(label="Model",
                                      widget=forms.Select(choices=models_choices), required=True)