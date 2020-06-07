from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Dataset
from ..forms import DatasetChangeForm
from expDjango import settings
from django.urls import reverse
from django.contrib import messages

class DatasetChangeView(LoginRequiredMixin, UpdateView):
    model = Dataset.Dataset
    form_class = DatasetChangeForm.DatasetChangeForm
    login_url = settings.LOGOUT_REDIRECT_URL
    template_name = "dataset/changeDataset.html" # i need to change this after

    def get_queryset(self):
        queryset = super(DatasetChangeView, self).get_queryset()
        dataset_id = self.kwargs["pk"]
        return queryset.filter(id=dataset_id)

    def get_form_kwargs(self):
        kwargs = super(DatasetChangeView, self).get_form_kwargs()

        # pass request to form, in order to send messages
        kwargs["request"] = self.request

        # pass initial dataset values to form
        dataset = self.object #get object retieved in get_object ethod, that uses get_queryset
        kwargs["name"] = dataset.name
        kwargs["n_classes"] = dataset.n_classes
        kwargs["n_samples"] = dataset.n_samples
        if dataset.link_info != None:
            kwargs["link_info"] = dataset.link_info
        return kwargs

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data()) # i don't pass form in order to get initial form

    def get_success_url(self):
        messages.success(self.request, 'Dataset alterado com sucesso')
        kwargs = {'pk' : self.object.id}
        path = reverse('datasets:changeDatasetByID', kwargs=kwargs)
        return path