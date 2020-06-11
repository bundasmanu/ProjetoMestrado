from django.urls import path
from .views import ListOfModels, ModelCreateView, ModelChangeView, ModelDeleteView
from django.views.decorators.csrf import csrf_exempt

app_name = 'models'

urlpatterns = [
    path('list', ListOfModels.ListOfModels.as_view(), name='listaModels'),
    path('create', ModelCreateView.ModelCreateView.as_view(), name='criaModelo'),
    path('change/<int:pk>', ModelChangeView.ModelChangeView.as_view(), name='atualizaModelo'),
    path('delete/<int:pk>', csrf_exempt(ModelDeleteView.ModelDeleteView.as_view()), name='deleteModelByID'),
]