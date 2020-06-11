from django.urls import path
from datasets.views import DatasetCreateView, ListOfDatasets, ListSpecificDataset, PredictView, DatasetDeleteView, DatasetChangeView
from datasets.views.ajax import LoadModelsForDataset
from django.views.decorators.csrf import csrf_exempt

app_name = 'datasets'

urlpatterns = [
    path('create', DatasetCreateView.DatasetCreateView.as_view(), name='criaDataset'),
    path('list', ListOfDatasets.ListOfDatasets.as_view(), name='listaDatasets'),
    path('list/<int:pk>', ListSpecificDataset.ListSpecificDataset.as_view(), name="ListaDatasetByID"),
    path('delete/<int:pk>', csrf_exempt(DatasetDeleteView.DatasetDeleteView.as_view()), name="deleteDatasetByID"),
    path('change/<int:pk>', DatasetChangeView.DatasetChangeView.as_view(), name="changeDatasetByID"),
    path('predict', PredictView.PredictView.as_view(), name='predict'),
    path('ajax/loadmodel', LoadModelsForDataset.LoadModelsForDataset.as_view(), name="ajaxModelsLoad"),
]