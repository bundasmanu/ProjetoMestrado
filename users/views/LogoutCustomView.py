from django.contrib.auth.views import LogoutView

#https://gist.github.com/laozhu/8250910
#https://stackoverflow.com/questions/11444958/logout-then-login-in-django

class LogoutCustomView(LogoutView):
    extra_context = {} #IF I WANT TO PASS EXTRA FIELDS TO TEMPLATE --> https://docs.djangoproject.com/en/3.0/topics/auth/default/

    #I DEFINE LOGOUT_REDIRECT_URL TO AVOID THE USAGE OF REDIRECT_VIEW, BECAUSE WITH REDIRECT_VIEW I NEED TO OVERRIDE GET_REDIRECT_URL