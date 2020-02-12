from django.views.generic.edit import CreateView
from users.models import CustomUser
from users.forms.CustomUserForm import CustomUserCreationForm
from datetime import datetime
from django.contrib.auth import authenticate, login
from ..models import GroupQueryset
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
import expDjango.utils as utils

class CreateUserView(CreateView):

    #REF: https://stackoverflow.com/questions/4051873/django-creating-object-from-post
    #EXPLANATION OF CORRECT OVERRIDE OF POST AND GET --> https://stackoverflow.com/questions/15622354/django-listview-with-post-method

    form_class = CustomUserCreationForm
    model = CustomUser.CustomUser
    template_name = 'users/CreateUser.html' #NECESSITO DE COLOCAR AQUI O TEMPLATE

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name,  {"form" : self.form_class})

    def form_valid(self, form):

        try:
            self.clean_messages()
            # GET DATA ON THE FORM'S --> I PASS THE CONTENT ON FORM TO MY MODEL
            self.get_content_form(form)

            # FORM IS_VALID() ALREADY CHECKS IF AN USER IS VALID (NOR EXISTS), AND I ONLY NEED TO ADD USER
            actual_hour = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # ADD USER TO GROUP
            self.model.objects.create_user(first_name=self.model.first_name, last_name=self.model.last_name,
                                           username=self.model.username,
                                           email=self.model.email, password=self.model.password,
                                           is_superuser=False, is_staff=True, date_joined=actual_hour,
                                           is_active=True, userType=self.model.userType, last_login=actual_hour)
            credentials = {'username': self.model.username, 'password': self.model.password}
            groupName = utils.getNameGroup(self.model.userType)
            x = GroupQueryset.GroupQueryset().as_manager()
            x.addUserToGroup(username=credentials.get('username'),
                             charGroup=groupName)  # GERA EXCECAO NAO E NECESSARIO VERIFICAR
            # AUTHENTICATE USER AND LOGIN WITH HIS CREDENTIALS, ACCESS DIRECTLY TO WEBSITE
            credentials = {'username': self.model.username, 'password': self.model.password}
            user = authenticate(**credentials)
            login(self.request, user)

            return HttpResponseRedirect(self.get_success_url())
        except:
            raise

    def get_content_form(self, form):
        try:
            self.model.username = form.cleaned_data.get("username")
            self.model.email = form.cleaned_data.get("email")
            self.model.password = form.cleaned_data.get("password1")
            self.model.first_name = form.cleaned_data.get("first_name")
            self.model.last_name = form.cleaned_data.get("last_name")
            self.model.userType = form.cleaned_data.get("userType")
        except:
            raise

    def form_invalid(self, form):
        try:
            print(form.errors)
            messages.add_message(self.request, messages.INFO, form.error_messages)
            #kwargs = {"form" : form}
            #context = self.get_context_data(**kwargs)
            return self.render_to_response(self.get_context_data()) #https://books.google.pt/books?id=8sU7DwAAQBAJ&pg=PA424&lpg=PA424&dq=how+can+i+pass+form+on+form_invalid()+django&source=bl&ots=RNfTHOcCCo&sig=ACfU3U30nGH3-dwZM1BuQK-Dfx-HpqfTdw&hl=pt-PT&sa=X&ved=2ahUKEwikwKfM5MrnAhVQx4UKHf5-DRYQ6AEwB3oECAoQAQ#v=onepage&q=how%20can%20i%20pass%20form%20on%20form_invalid()%20django&f=false
        except:
            raise

    def get_success_url(self):
        try:
            self.clean_messages()
            path = reverse('users:info')
            return path
        except:
            raise

    def clean_messages(self):
        try:
            usedMessages = messages.get_messages(self.request)
            for message in usedMessages:
                pass
            usedMessages.used = True
        except:
            raise


