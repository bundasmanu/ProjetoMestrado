from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser.CustomUser
        fields = ('username', 'email', 'password1', 'password2' ,'first_name', 'last_name', 'userType')

class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs): #INITIAL VALUES OF FORM
        username_initial = kwargs.pop('username_initial', None)
        fName_initial = kwargs.pop('fName_initial', None)
        lName_initial = kwargs.pop('lName_initial', None)
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = username_initial
        self.fields['first_name'].initial = fName_initial
        self.fields['last_name'].initial = lName_initial

    class Meta(UserChangeForm.Meta):
        model = CustomUser.CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')#USERTYPE IS NOT CHANGEABLE --> EMAIL ALSO IS DON'T, BE USERCHANGEFORM MAKE THIS VALIDATION, AND DOES NOT RESULT IN FORM INVALID
