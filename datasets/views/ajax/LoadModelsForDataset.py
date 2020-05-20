from django.views.generic.base import TemplateView
from ...models import CNNModel, Dataset

class LoadModelsForDataset(TemplateView):

    template_name = 'dataset/loadModelForDataset.html'

    def get_models(self, id_model):
        queryset = CNNModel.CNNModel.objects.filter(dataset_id__cnnmodel=id_model).order_by('dataset_id__cnnmodel')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LoadModelsForDataset, self).get_context_data(**kwargs)
        models_dataset = self.get_models(self.request.GET.get('id_model'))
        context['models'] = models_dataset
        return context