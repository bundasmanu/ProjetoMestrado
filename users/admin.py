from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms.CustomUserForm import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser.CustomUser

#REGISTO DO CUSTOM USER COMO OVERRIDE
admin.site.register(CustomUser.CustomUser, CustomUserAdmin)