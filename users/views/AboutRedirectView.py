from django.views.generic.base import TemplateView

class AboutRedirectView(TemplateView):

    template_name = 'general/About.html'
