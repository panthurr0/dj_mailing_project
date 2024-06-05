from django.contrib import admin

from mailing.models import Client, MailingText, Mailing, Status


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "email",
        "name",
        "comment",
    )


@admin.register(MailingText)
class MailingTextAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "theme",
        "body",
    )


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "start_time",
        "end_time",
        "frequency",
        "answer",
        "status_of_mailing",
    )


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "status",
        "server_response",
        "last_attempt",
    )
