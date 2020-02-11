from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from django import forms
import expDjango.config as config

#I NEED TO OVERRIDE TWO CUSTOM CUSTOM USER FORMS TO NEW MODEL --> CUSTOM USER
#ADD EXTRA FIELDS --> https://stackoverflow.com/questions/45708119/how-to-add-extra-fields-to-django-registration-form
userTypeChoices = [
    ('A', config.ADMIN),
    ('H', config.HEALTHCARE),
    ('D', config.DATASCIENTIST)
]

class CustomUserCreationForm(UserCreationForm):
    userTypesOptionsSelect = forms.ChoiceField(widget=forms.CheckboxInput ,choices=userTypeChoices) #https://stackoverflow.com/questions/15393134/django-how-can-i-create-a-multiple-select-form

    class Meta(UserCreationForm.Meta):
        model = CustomUser.CustomUser
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'userType')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser.CustomUser
        fields = ('email', 'password')