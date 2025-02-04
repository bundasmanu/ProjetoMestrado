from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import History
from django.db.models import Count
from expDjango import settings

class showHistoryDetails(LoginRequiredMixin, DetailView):
    model = History.History
    template_name = 'history/showHistoryDetails.html'
    login_url = settings.LOGOUT_REDIRECT_URL

    def get_object(self, queryset=None):
        pass # avoid need of pass a pk via get --> in ListView and CreateView i don't need this, but in a DetailView i need like in Update or Delete View

    def get_queryset(self):
        unique_dataset_filter = History.History.objects.all().filter(user_id_id=self.request.user.id).values('dataset_id').distinct('dataset_id')
        return History.History.objects.filter(dataset_id__in=unique_dataset_filter).values('dataset_id__name', 'dataset_id').annotate(number_datasets=Count('dataset_id')).\
        order_by('-number_datasets')[:3] # descending order

    def get_context_data(self, **kwargs):
        context = super(showHistoryDetails, self).get_context_data(**kwargs)
        # three most used datasets
        most_commom_datasets = History.History.objects.values('dataset_id__name', 'dataset_id').annotate(number_datasets=Count('dataset_id')).\
                                order_by('-number_datasets')[:3] # descending order
        context["commom_datasets"] = most_commom_datasets
        # three most used models
        most_commom_models = History.History.objects.values('model_id__name', 'model_id', 'dataset_id__name').\
                                annotate(number_models=Count('model_id')).order_by('-number_models')[:3] # descending order
        context["commom_models"] = most_commom_models
        # three most used datasets by user
        context["object_list"] = self.get_queryset()
        return context