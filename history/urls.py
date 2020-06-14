from django.urls import path
from .views import showHistoryDetails

app_name = 'history'

urlpatterns = [
    path('details/', showHistoryDetails.showHistoryDetails.as_view(), name='showDetails'),
]