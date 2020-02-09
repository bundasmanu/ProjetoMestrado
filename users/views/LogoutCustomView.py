from django.contrib.auth import logout
from django.views.generic import RedirectView

#https://gist.github.com/laozhu/8250910
#https://stackoverflow.com/questions/11444958/logout-then-login-in-django

class LogoutCustomView(RedirectView):
    pattern_name = 'home'
    permanent = False

    def get_redirect_url(self, *args, **kwargs):

        try:
            if self.request.user.is_authenticated():
                logout(self.request) #THEN I NEED TO PUT LOGOUT_URL ON SETTINGS --> IN ORDER TO REDIRECT TO HOME
        except:
            raise