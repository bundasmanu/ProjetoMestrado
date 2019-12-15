from django import forms
from Dataset.models import Dataset

allDataset = [(i.id, i.name) for i in Dataset.objects.all()]
dropdownDatasets = None #PARA NAO ACEDER, EM HARD CODE ÀS SUAS LABELS
gammaValue = None #PARA NAO ACEDER, EM HARD CODE ÀS SUAS LABELS

class TrainPredForm(forms.Form): #FORM PORQUE ESTES DADOS SAO SÓ PARA SELECÇÃO E NAO ALTERACAO, CASO FOSSE ALTERACAO A OPCAO MODELSFORM ERA MELHOR OPCAO
    dropDownDatasets = forms.ChoiceField(label="Select one dataset", choices=allDataset)
    gammaValue = forms.FloatField(min_value=0, max_value=1, required=True, initial=0.01)


