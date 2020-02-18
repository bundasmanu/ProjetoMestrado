from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser.CustomUser
        fields = ('username', 'email', 'password1', 'password2' ,'first_name', 'last_name', 'userType')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser.CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')#USERTYPE IS NOT CHANGEABLE --> EMAIL ALSO IS DON'T, BE USERCHANGEFORM MAKE THIS VALIDATION, AND DOES NOT RESULT IN FORM INVALID