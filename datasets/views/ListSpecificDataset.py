from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
import expDjango.settings as settings
from ..models import Dataset
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.defaults import page_not_found

class ListSpecificDataset(LoginRequiredMixin, DetailView):

    template_name = 'dataset/listSingleDataset.html'
    model = Dataset.Dataset
    login_url = settings.LOGOUT_REDIRECT_URL

    # https://stackoverflow.com/questions/25699416/how-to-use-value-from-url-and-request-in-django-detailview
    def get_queryset(self):
        dataset_id = self.kwargs['pk'] # get url primary key of dataset
        queryset = Dataset.Dataset.objects.filter(id=dataset_id)
        if queryset == None:
            return HttpResponseRedirect(page_not_found(self.request, "Dataset Does not exist"))
        return queryset

    #https://stackoverflow.com/questions/30869642/django-blog-not-linking-to-detail-view --> Implementation of slug url to link ListView to DetailView