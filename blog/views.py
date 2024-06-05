from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from blog.forms import BlogForm
from blog.models import Blog


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        raise PermissionDenied("У вас нет доступа к этой странице!")


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")


class BlogCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        user = self.request.user
        blog = form.save(commit=False)
        blog.author = user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        user = self.request.user
        blog = form.save(commit=False)
        blog.author = user
        return super().form_valid(form)


class BlogDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        blog = super().get_object(queryset)
        blog.count_views += 1
        blog.save()
        return blog
