from django.forms import ModelChoiceField

class DatasetOptionsChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.name