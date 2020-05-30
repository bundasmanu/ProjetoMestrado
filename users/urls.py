from django.urls import path
from .views import DetailUserInfoView, ListAllUsers, CreateUserView, CustomLoginView, LogoutCustomView, ChangeUserPasswordView, AboutRedirectView
from django.views.generic.base import TemplateView

app_name = 'userUrls'

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='users/Home.html'), name='home'),
    path('about/', AboutRedirectView.AboutRedirectView.as_view(), name='about'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutCustomView.as_view(), name='logout'),
    path('info/', DetailUserInfoView.as_view(), name='info'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('changePass/<int:pk>', ChangeUserPasswordView.ChangeUserPasswordView.as_view(), name="changePass")
]