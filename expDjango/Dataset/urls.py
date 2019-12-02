from django.urls import path
from .views import DatasetCRUD

urlpatterns = [
    path('', DatasetCRUD.listAllDatasets , name = 'index'),
]
