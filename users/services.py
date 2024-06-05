from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from users.models import User


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True

    group, created = Group.objects.get_or_create(name="ourusers")
    user.groups.add(group)
    user.save()
    return redirect(reverse("users:login"))


def toggle_activity(request, pk):
    user = User.objects.get(pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True

    user.save()
    return redirect("users:user_list")