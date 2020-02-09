from django.views.generic.list import ListView
from users.models import CustomUser

class ListAllUsers(ListView):
    model = CustomUser.CustomUser
    template_name = ''
    paginate_by = 10 #ADD PAGINATION TO CONTEXT

    def get_queryset(self):
        allUsers = self.model.objects.all() #RETRIEEVE ALL USERS --> PENSO QUE POR DEFEITO JA ME DAVA TODOS OS USERS, MAS ... --> https://medium.com/@hassanraza/when-to-use-get-get-queryset-get-context-data-in-django-952df6be036a
        return allUsers

    #NAO NECESSITO DE UM GET CONTEXT DATA --> PORQUE NAO PRECISO DE ADICIONAR MAIS CONTEUDO DO QUE O RETORNADO PELO QUERYSET
    #REF: https://medium.com/@hassanraza/when-to-use-get-get-queryset-get-context-data-in-django-952df6be036a

    #LINKS TO EXPLORE PAGINATION ON TEMPLATE CREATION:
    #https://docs.djangoproject.com/en/3.0/topics/pagination/
    #https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html