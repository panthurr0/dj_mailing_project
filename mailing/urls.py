from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from config import settings
from mailing.apps import MailingConfig
from mailing.views.client import ClientCreateView, ClientUpdateView, ClientDeleteView, ClientListView
from mailing.views.home import HomeView
from mailing.views.mailing import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, \
    MailingDeleteView
from mailing.views.mailingtext import MailingTextListView, MailingTextCreateView, MailingTextUpdateView, \
    MailingTextDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', cache_page(600)(HomeView.as_view()), name='home'),

    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_form/', ClientCreateView.as_view(), name='client_form'),
    path("<int:pk>/client_update", ClientUpdateView.as_view(), name="client_update"),
    path("<int:pk>/client_delete", ClientDeleteView.as_view(), name="client_delete"),

    path("mailing_list/", MailingListView.as_view(), name="mailing_list"),
    path("mailing_detail/<int:pk>", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailing_form/", MailingCreateView.as_view(), name="mailing_form"),
    path("<int:pk>/mailing_update", MailingUpdateView.as_view(), name="mailing_update"),
    path("<int:pk>/mailing_delete", MailingDeleteView.as_view(), name="mailing_delete"),

    path("mailingtext_list/", MailingTextListView.as_view(), name="mailingtext_list"),
    path("mailingtext_form/", MailingTextCreateView.as_view(), name="mailingtext_form"),
    path("<int:pk>/mailingtext_update", MailingTextUpdateView.as_view(), name="mailing_update"),
    path("<int:pk>/mailingtext_delete", MailingTextDeleteView.as_view(), name="mailing_delete"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
