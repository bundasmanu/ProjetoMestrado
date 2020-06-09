from django.urls import path
from .views import ListOfModels, ModelCreateView
from django.views.decorators.csrf import csrf_exempt

app_name = 'modelos'

urlpatterns = [
    path('list', ListOfModels.ListOfModels.as_view(), name='listaModels'),
    path('create', ModelCreateView.ModelCreateView.as_view(), name='criaModelo'),
]