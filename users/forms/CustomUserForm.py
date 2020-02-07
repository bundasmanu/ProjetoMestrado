from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser

#I NEED TO OVERRIDE TWO CUSTOM CUSTOM USER FORMS TO NEW MODEL --> CUSTOM USER

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser.CustomUser
        fields = ('username', 'email', 'password')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser.CustomUser
        fields = ('email', 'password')