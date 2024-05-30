from django.contrib import admin

from mailing.models import Client, MailingAttempt, Mailing, MailingText


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)


@admin.register(MailingText)
class MailingTextAdmin(admin.ModelAdmin):
    list_display = ('theme',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'theme', 'status',)


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'last_attempt', 'status',)
