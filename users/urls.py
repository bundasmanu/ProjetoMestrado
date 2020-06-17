from django.urls import path
from .views import DetailUserInfoView, ListAllUsers, CreateUserView, CustomLoginView, LogoutCustomView, ChangeUserPasswordView, AboutRedirectView, EntryPage
from django.views.generic.base import TemplateView

app_name = 'userUrls'

urlpatterns = [
    path('', TemplateView.as_view(template_name='users/Home.html'), name='home'),
    path('about/', AboutRedirectView.AboutRedirectView.as_view(), name='about'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutCustomView.as_view(), name='logout'),
    path('info/', DetailUserInfoView.as_view(), name='info'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('entry', EntryPage.EntryPage.as_view(), name='entry'),
    path('changePass/<int:pk>', ChangeUserPasswordView.ChangeUserPasswordView.as_view(), name="changePass")
]