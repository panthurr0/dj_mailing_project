from django.contrib.auth.forms import UserCreationForm

from mailing.forms import MixinForms
from users.models import User


class UserRegisterForm(MixinForms, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'company', 'password1', 'password2',)
