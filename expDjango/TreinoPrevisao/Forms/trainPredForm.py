from django import forms
from expDjango.Dataset.Models import Dataset

allDataset = [(int(i.id), int(i.id)) for i in Dataset.Dataset.objects.all()]
dropdownDatasets = None #PARA NAO ACEDER, EM HARD CODE ÀS SUAS LABELS
gammaValue = None #PARA NAO ACEDER, EM HARD CODE ÀS SUAS LABELS

class TrainPredForm(forms.Form):
    dropDownDatasets = forms.IntegerField(label="Select one Dataset: ", widget=forms.Select(choices=allDataset))
    gammaValue = forms.FloatField(min_value=0, max_value=1, required=True, initial=0.01)


