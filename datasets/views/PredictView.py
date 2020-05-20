from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
import expDjango.settings as settings
from django.views.defaults import page_not_found
from django.shortcuts import HttpResponseRedirect
from ..models import Dataset
from django.db.models import Count
from ..forms import PredictForm

class PredictView(LoginRequiredMixin, FormView):

    template_name = 'dataset/predict.html'
    login_url = settings.LOGOUT_REDIRECT_URL
    form_class = PredictForm.PredictForm

    def queysets(self):

        try:

            # get only dataset's with models associated
            datasets = Dataset.Dataset.objects.all().annotate(numbermodels=Count('cnnmodel'))
            datasets = datasets.exclude(numbermodels=0)
            return datasets
        except:
            return HttpResponseRedirect(page_not_found(self.request, "Database acess error"))

    def get_context_data(self, **kwargs):
        context = super(PredictView, self).get_context_data(**kwargs)
        x = self.queysets()
        return context