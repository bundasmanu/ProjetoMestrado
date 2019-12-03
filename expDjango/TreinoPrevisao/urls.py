from django.urls import path
from .views import predictResponse

urlpatterns = [
    path('', predictResponse.uploadTrainPredict, name = 'index'),
]
