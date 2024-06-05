import secrets

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DetailView

from config.settings import DEFAULT_FROM_EMAIL
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("mailing:home")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.token = secrets.token_hex(7)
        user.save()

        host = self.request.get_host()
        url = f"http://{host}/users/confirm-register/{user.token}/"

        send_mail(
            subject="Hi! You need to confirm your registrations",
            message=f"Click here if it was you: {url}",
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )

        return super().form_valid(form)


class PasswortResetView(FormView):
    model = User
    template_name = "passwort_reset_view.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        email_form = form.cleaned_data("email")
        user = User.objects.get(email=email_form)

        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()
        send_mail(
            subject="New password",
            message=f"Here: {new_password}",
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class UserListView(UserPassesTestMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    success_url = reverse_lazy("users:user_list")

    def test_func(self):
        return self.request.user.is_superuser


class UserDetailView(UserPassesTestMixin, DetailView):
    model = User
    success_url = reverse_lazy("users:user_detail")

    def test_func(self):
        return self.request.user.is_superuser