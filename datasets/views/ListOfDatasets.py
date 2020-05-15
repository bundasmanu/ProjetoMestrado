from django.views.generic.list import ListView
from ..models import Dataset
from django.db.models import Count

class ListOfDatasets(ListView):

    model = Dataset.Dataset
    paginate_by = 8
    template_name = 'dataset/listDatasets.html'

    # concatenate queryset's link: https://stackoverflow.com/questions/48872380/display-multiple-queryset-in-list-view
    def get_queryset(self):
        queryset = Dataset.Dataset.objects.annotate(numbermodels=Count('cnnmodel'))
        return queryset