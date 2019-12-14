from django.urls import path
from treinoPrevisao.views import predictResponse, accuracyResponse

urlpatterns = [
    path('trainPreview', predictResponse.uploadTrainPredict, name = 'trPrev'),
    path('showAccuracy', accuracyResponse.showAccResponse, name = 'showAcc'),
]
