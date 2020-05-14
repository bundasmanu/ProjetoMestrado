from django.urls import path
from datasets.views import DatasetCreateView

app_name = 'datasets'

urlpatterns = [
    path('create', DatasetCreateView.DatasetCreateView.as_view(), name='criaDataset'),
]