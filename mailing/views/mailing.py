from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView,
                                  DetailView, )

from mailing.forms import MailingForm
from mailing.models import Mailing, CREATE, Client, MailingText
from mailing.services import send_mailing


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    permission_required = "mailing.can_view_all_mailings"
    success_url = reverse_lazy("mailing:mailing_list")

    def get_queryset(self):
        user = self.request.user
        company = user.company

        if user.has_perm("mailing.can_view_all_mailings") or user.is_superuser:
            return Mailing.objects.all()

        else:
            mailings = (
                Mailing.objects.filter(clients__company=company)
                .prefetch_related("clients__company", "mail")
                .distinct()
            )
            return mailings


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    context_object_name = "mailing"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        user = self.request.user
        if (
                user.is_superuser
                or (obj.clients.filter(company=user.company).exists())
                or user.is_staff
        ):
            return obj
        else:
            raise Http404("You do not have permission to view this mailing.")

    def get_success_url(self):
        return reverse("mailing:mailing_detail")


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm

    success_url = reverse_lazy("mailing:mailing_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        user = self.request.user
        company = user.company

        form.fields["clients"].queryset = Client.objects.filter(company=company)
        form.fields["mail"].queryset = MailingText.objects.filter(
            company=company
        )
        return form

    def form_valid(self, form):
        mailing = form.save(commit=False)

        selected_clients = form.cleaned_data.get("clients")
        selected_mails = form.cleaned_data.get("mail")
        selected_start_time = form.cleaned_data.get("start_time")

        mailing.status_of_mailing = CREATE
        mailing.start_time = selected_start_time

        mailing.save()

        mailing.clients.set(selected_clients)
        mailing.mail.set(selected_mails)

        send_mailing(mailing)

        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        user = self.request.user
        company = user.company

        form.fields["clients"].queryset = Client.objects.filter(company=company)
        form.fields["mail"].queryset = MailingText.objects.filter(
            company=company
        )
        return form

    def get_success_url(self):
        return reverse("mailing:mailing_list")

    def form_valid(self, form):
        mailing = form.save(commit=False)

        selected_clients = form.cleaned_data.get("clients")
        selected_messages = form.cleaned_data.get("mail")
        selected_start_time = form.cleaned_data.get("start_time")

        mailing.clients.clear()
        mailing.mail.clear()

        mailing.clients.set(selected_clients)
        mailing.mail.set(selected_messages)

        mailing.mailing = CREATE
        mailing.start_time = selected_start_time

        mailing.save()

        send_mailing(mailing)

        return super().form_valid(form)


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing

    def get_success_url(self):
        return reverse("mailing:mailing_list")
