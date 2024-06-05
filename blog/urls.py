from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import (
    BlogListView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogDetailView,
)

app_name = BlogConfig.name


urlpatterns = [
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_form/", BlogCreateView.as_view(), name="blog_form"),
    path("<int:pk>/blog_update/", BlogUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/blog_delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("<int:pk>/blog_detail/", BlogDetailView.as_view(), name="blog_detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
