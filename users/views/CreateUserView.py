from django.views.generic.edit import CreateView
from users.models import CustomUser
from users.forms.CustomUserForm import CustomUserCreationForm
from django.core.exceptions import MultipleObjectsReturned
from datetime import datetime
from django.contrib.auth import authenticate, login
from ..models import GroupQueryset

class CreateUserView(CreateView):

    #REF: https://stackoverflow.com/questions/4051873/django-creating-object-from-post

    form_class = CustomUserCreationForm
    model = CustomUser.CustomUser
    template_name = '' #NECESSITO DE COLOCAR AQUI O TEMPLATE

    def post(self, request, *args, **kwargs):

        try:

            formRetrieved = self.form_class(request.POST, instance=CustomUser.CustomUser)

            if formRetrieved.is_valid():
                #GET ALL DATA ON THE FIELDS --> THE FIELDS ARE: fields = ('username', 'email', 'password', 'first_name', 'last_name')
                username = formRetrieved.cleaned_data.get('username')
                email = formRetrieved.cleaned_data.get('email')
                password = formRetrieved.cleaned_data.get('password')
                first_name = formRetrieved.cleaned_data.get('first_name')
                last_name = formRetrieved.cleaned_data.get('last_name')

                #CHECK IF USER ALREADY EXISTS --> USING MANAGER APPROACH
                exists = self.model.users.checkExists(username)
                if exists == True:
                    raise MultipleObjectsReturned

                #IF USER DOESN'T EXISTS THEN I WILL CREATE USER
                actual_hour= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.model.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=password,
                                          is_superuser=False, is_staff=False, date_joined=actual_hour, is_active=True, userType='D', last_login=actual_hour)
                #ADD USER TO GROUP
                GroupQueryset.GroupQueryset.addUserToGroup(username=username, charGroup='D') #GERA EXCECAO NAO E NECESSARIO VERIFICAR
                #AUTHENTICATE USER AND LOGIN WITH HIS CREDENTIALS, ACCESS DIRECTLY TO WEBSITE
                credentials ={'username' : username, 'password' : password}
                user = authenticate(**credentials)
                login(request, user)

                #REDIRECT TO A PAGE THAT IS NOT LOGIN PAGE
                #return HttpResponseRedirect('/some/page/which/is/not/logginpage')#cause user is already logged in

            #LOGIN PAGE RENDER --> ACHO QUE NAO PRECISO O GET FAZ POR MIM
            #return render(request, 'treinoPrevisao/trainPreview.html', {'form': form})  # ALTERAR DPS O NOME DA FORM
        except:
            raise