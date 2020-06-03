from django.views.generic.list import ListView
from ..models import Dataset
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
import expDjango.settings as settings

class ListOfDatasets(ListView, LoginRequiredMixin):

    model = Dataset.Dataset
    paginate_by = 6
    template_name = 'dataset/listDatasets.html'
    login_url = settings.LOGOUT_REDIRECT_URL

    # concatenate queryset's link: https://stackoverflow.com/questions/48872380/display-multiple-queryset-in-list-view
    def get_queryset(self):
        datasets = Dataset.Dataset.objects.all().values('name', 'n_classes', 'n_samples', 'creation_date', 'id')\
                                                                .order_by('id').distinct('id')

        return datasets

    def get_context_data(self, **kwargs):
        context = super(ListOfDatasets, self).get_context_data(**kwargs)
        models_per_dataset = Dataset.Dataset.objects.values('id', 'cnnmodel__name').order_by('id')
        context['models'] = models_per_dataset
        number_models = Dataset.Dataset.objects.annotate(numbermodels=Count('cnnmodel'))
        context['number_models'] = number_models
        return context
    #https://stackoverflow.com/questions/45242717/how-to-select-data-from-two-tables-in-django