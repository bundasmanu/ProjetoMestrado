from django.urls import path
from .views import DetailUserInfoView, ListAllUsers, CreateUserView, CustomLoginView, LogoutCustomView, HomeRedirectView

app_name = 'userUrls'

urlpatterns = [
    path('home/', HomeRedirectView.HomeRedirectView.as_view() , name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutCustomView.as_view(), name='logout'),
    path('info/', DetailUserInfoView.as_view(), name='info'),
    path('create/', CreateUserView.as_view(), name='create')
]