from django.views.generic.base import TemplateView
from ...models import CNNModel

class LoadModelsForDataset(TemplateView):

    template_name = 'dataset/loadModelForDataset.html'

    def get_models(self, id_model):
        return CNNModel.CNNModel.objects.filter(dataset_id=id_model).order_by('dataset_id__cnnmodel')

    def get_context_data(self, **kwargs):
        context = super(LoadModelsForDataset, self).get_context_data(**kwargs)
        models_dataset = self.get_models(self.request.GET.get('id_model'))
        context['models'] = models_dataset
        return context