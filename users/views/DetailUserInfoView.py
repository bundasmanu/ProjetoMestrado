from django.views.generic.detail import DetailView
from ..models import CustomUser
from django.contrib.auth import get_user_model

class DetailUserInfoView(DetailView):
    model = CustomUser.CustomUser
    template_name = '/'

    def get_queryset(self): #OBTER APENAS OBJETO REFERENTE AO USER LOGADO
        return get_user_model()