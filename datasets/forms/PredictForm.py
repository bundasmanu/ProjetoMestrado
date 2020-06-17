from django import forms
from ..models import Dataset
from django.db.models import Count
from expDjango import config
from .. import validators

class PredictForm(forms.Form):

    # fields of form
    dataset_dropdown = forms.CharField(label="Dataset", empty_value='Selecciona um dataset',
                                        widget=forms.Select(choices=[('', '')]), required=True)
    models_dropdown = forms.CharField(label="Model", empty_value='Selecciona um modelo',
                                      widget=forms.Select(choices=[('', '')]), required=True)
    image_upload = forms.ImageField(max_length=config.MAX_IMAGE_SIZE, required=True, label='Seleccione uma imagem',
                                    help_text='Tamanho máximo 20MB', allow_empty_file=False, validators=[validators.validate_image_file_extension])

    def __init__(self, *args, **kwargs): # need to populate dropdown's in init because this form applies queryset's and db logic, and interferes in migrations, for new environment, in this way, i don't have problems
        super(PredictForm, self).__init__(*args, **kwargs)

        # get only dataset's with models associated
        datasets_with_models = Dataset.Dataset.objects.all().annotate(numbermodels=Count('cnnmodel'))
        datasets_with_models = datasets_with_models.exclude(numbermodels=0)

        # choices of dropdown's
        dataset_choices = [(x.id, x.name) for x in datasets_with_models]
        dataset_choices.insert(0, ('', 'Selecciona um dataset'))
        models_choices = []
        models_choices.insert(0, ('', 'Selecciona um modelo'))

        self.fields["dataset_dropdown"].widget.choices = dataset_choices
        self.fields["models_dropdown"].widget.choices = models_choices
