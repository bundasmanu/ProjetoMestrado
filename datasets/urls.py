from django.urls import path
from datasets.views import DatasetCreateView, ListOfDatasets

app_name = 'datasets'

urlpatterns = [
    path('create', DatasetCreateView.DatasetCreateView.as_view(), name='criaDataset'),
    path('list', ListOfDatasets.ListOfDatasets.as_view(), name='listaDatasets'),
]