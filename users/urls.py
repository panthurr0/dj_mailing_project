from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.urls import path

from config import settings
from users.apps import UsersConfig
from users.forms import UserRegisterForm
from users.services import email_verification, toggle_activity
from users.views import UserCreateView, PasswortResetView, UserListView, UserDetailView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("passwort_reset_view/",PasswortResetView.as_view(form_class=UserRegisterForm),name="passwort_reset"),
    path("confirm-register/<str:token>/", email_verification, name="confirm-register"),
    path("user_list/", UserListView.as_view(), name="user_list"),
    path("user_detail/<int:pk>", UserDetailView.as_view(), name="user_detail"),
    path("toggle_activity/<int:pk>", toggle_activity, name="toggle_activity"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
