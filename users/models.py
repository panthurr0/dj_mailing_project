from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Company(models.Model):
    company_name = models.CharField(max_length=150, verbose_name="Название компании")

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, verbose_name='компания', **NULLABLE)

    token = models.CharField(verbose_name="Token", max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    avatar = models.ImageField(verbose_name='аватар', upload_to='users/', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
