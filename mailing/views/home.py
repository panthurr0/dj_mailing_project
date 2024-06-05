from random import shuffle

from django.views.generic import ListView

from blog.models import Blog
from mailing.models import Mailing, DONE, IN_WORK


class HomeView(ListView):
    model = Mailing
    template_name = "mailing/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset = self.get_queryset()
        mailings = queryset.filter()

        mailings_done_count = mailings.filter(status_of_mailing=DONE).count()
        mailings_active = mailings.filter(status_of_mailing=IN_WORK).count()
        unique_clients = (
            mailings.prefetch_related("clients").distinct().count()
        )

        context["mailings_done_count"] = mailings_done_count
        context["mailings_active"] = mailings_active
        context["unique_clients"] = unique_clients

        blog_pks = list(Blog.objects.values_list("pk", flat=True))
        shuffle(blog_pks)
        selected_blog_pks = blog_pks[:3]
        blogs_list = Blog.objects.filter(pk__in=selected_blog_pks)

        context["blogs_list"] = blogs_list

        return context
