from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from mailing.models import MailingText


class MailingTextListView(LoginRequiredMixin, ListView):
    model = MailingText

    def get_queryset(self):
        user = self.request.user

        return MailingText.objects.filter(company=user.user_company)


class MailingTextCreateView(LoginRequiredMixin, CreateView):
    model = MailingText
    fields = (
        "theme",
        "body",
    )
    success_url = reverse_lazy("schedule:client_list")

    def form_valid(self, form):
        user = self.request.user
        form.save(commit=False)
        form.instance.company = user.user_company

        return super().form_valid(form)


class MailingTextUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingText
    fields = (
        "theme",
        "body",
    )

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not (user.user_company == self.get_object().company or user.is_superuser):
            return HttpResponseForbidden("Go out!")
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("schedule:mailingtext_list")


class MailingTextDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingText

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not (user.user_company == self.get_object().company or user.is_superuser):
            return HttpResponseForbidden("Go out!")
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("schedule:mailingtext_list")