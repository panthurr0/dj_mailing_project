from datetime import datetime

from django.db import models

from users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Содержимое статьи")
    image = models.ImageField(upload_to="blog/", verbose_name="Картинка статьи", blank=True, null=True)
    count_views = models.PositiveIntegerField(verbose_name="Количество просмотров", default=0)
    created_at = models.DateTimeField(default=datetime.now, verbose_name="Дата содания")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Автор", blank=True, null=True)

    def __str__(self):
        return self.title, self.count_views, self.created_at

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        