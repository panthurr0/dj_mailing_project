from random import shuffle

from django.views.generic import ListView

from mailing.models import Mailing, DONE, IN_WORK


class HomeView(ListView):
    model = Mailing
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset = self.get_queryset()
        mailings = queryset.filter()

        mailing_done_count = mailings.filter(status_of_newsletter=DONE).count()
        mailing_active = mailings.filter(status_of_newsletter=IN_WORK).count()
        unique_clients = (
            mailings.prefetch_related("clients").all().distinct().count()
        )

        context["mailing_done_count"] = mailing_done_count
        context["mailing_active"] = mailing_active
        context["unique_clients"] = unique_clients

        # blog_pks = list(Blog.objects.values_list("pk", flat=True))
        # shuffle(blog_pks)
        # selected_blog_pks = blog_pks[:3]
        # blogs_list = Blog.objects.filter(pk__in=selected_blog_pks)

        # context["blogs_list"] = blogs_list

        return context
