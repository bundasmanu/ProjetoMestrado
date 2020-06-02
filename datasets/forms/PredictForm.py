# from django import forms
# from ..models import Dataset
# from django.db.models import Count
# from expDjango import config, settings
#
# class PredictForm(forms.Form):
#
#     # get only dataset's with models associated
#     datasets_with_models = Dataset.Dataset.objects.all().annotate(numbermodels=Count('cnnmodel'))
#     datasets_with_models = datasets_with_models.exclude(numbermodels=0)
#
#     # choices of dropdown's
#     dataset_choices = [(x.id, x.name) for x in datasets_with_models]
#     dataset_choices.insert(0, ('', 'Selecciona Dataset'))
#     models_choices = []
#     models_choices.insert(0, ('', 'Selecciona Modelo'))
#
#     # fields of form
#     dataset_dropdown = forms.CharField(label="Dataset",
#                                         widget=forms.Select(choices=dataset_choices), required=True)
#     models_dropdown = forms.CharField(label="Model",
#                                       widget=forms.Select(choices=models_choices), required=True)
#     image_upload = forms.ImageField(max_length=config.MAX_IMAGE_SIZE, required=True, label='Seleccione uma imagem',
#                                     help_text='Tamanho máximo 20MB', allow_empty_file=False)