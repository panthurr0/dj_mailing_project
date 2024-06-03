from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterForm


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

    def get_default_redirect_url(self):
        if self.request.GET.get('next'):
            self.next_page = self.request.GET.get('next')
        return super().get_default_redirect_url()


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('mailing:list')
