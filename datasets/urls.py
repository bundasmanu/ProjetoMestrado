from django.urls import path
from datasets.views import DatasetCreateView, ListOfDatasets, ListSpecificDataset, PredictView, DatasetDeleteView
from datasets.views.ajax import LoadModelsForDataset

app_name = 'datasets'

urlpatterns = [
    path('create', DatasetCreateView.DatasetCreateView.as_view(), name='criaDataset'),
    path('list', ListOfDatasets.ListOfDatasets.as_view(), name='listaDatasets'),
    path('list/<int:pk>', ListSpecificDataset.ListSpecificDataset.as_view(), name="ListaDatasetByID"),
    path('delete/<int:pk>', DatasetDeleteView.DatasetDeleteView.as_view(), name="deleteDatasetByID"),
    #path('predict', PredictView.PredictView.as_view(), name='predict'),
    path('ajax/loadmodel', LoadModelsForDataset.LoadModelsForDataset.as_view(), name="ajaxModelsLoad"),
]