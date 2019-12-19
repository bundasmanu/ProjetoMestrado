from django.urls import path, re_path
from treinoPrevisao.views import predictResponse, accuracyResponse

app_name = 'treinoPrev'

urlpatterns = [
    path('trainPreview', predictResponse.uploadTrainPredict, name = 'trPrev'),
    path('showAccuracy/<str:arrayConf>/<str:acc>/<str:prec>/<str:rec>/<str:f1>', accuracyResponse.showAccResponse, name = 'showAcc'),
]

#r'^showAccuracy/(?P<arrayConf>\w+)/(?P<acc>\w+)/(?P<prec>\w+)/(?P<rec>\w+)/(?P<f1>\w+)/$