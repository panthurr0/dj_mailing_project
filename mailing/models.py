from django.db import models
from users.models import Company, User

NULLABLE = {'blank': True, 'null': True}

CREATE = "Создана"
IN_WORK = "В работе"
DONE = "Завершена"
ERROR = "Ошибка отправки"

DAILY = "раз в день"
WEEKLY = "раз в неделю"
MONTHLY = "раз в месяц"


class Client(models.Model):
    name = models.CharField(verbose_name='ФИО', **NULLABLE)
    email = models.EmailField(verbose_name='Контактный email', **NULLABLE, unique=True, max_length=50)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, verbose_name='компания', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('name',)
        permissions = [
            (
                "can_view_client_list",
                "Может просматривать пользователей сервиса",
            ),
        ]


class MailingText(models.Model):
    theme = models.CharField(verbose_name='Тема письма', max_length=150, **NULLABLE)
    body = models.TextField(verbose_name='Тело письма', **NULLABLE)
    clients = models.ManyToManyField(Client, verbose_name='Клиенты для рассылки', blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, verbose_name="Компания", null=True, blank=True)

    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        permissions = [
            (
                "can_change_mailingtext_list",
                "Может изменять текст для рассылок",
            ),
        ]


class Mailing(models.Model):
    FREQUENCY_CHOICES = [
        (DAILY, "Ежедневно"),
        (WEEKLY, "Еженедельно"),
        (MONTHLY, "Ежемесячно"),
    ]
    STATUS_OF_MAILING = [
        (CREATE, "Создана"),
        (IN_WORK, "В работе"),
        (DONE, "Завершена"),
        (ERROR, "Ошибка отправки"),
    ]

    start_time = models.DateTimeField(verbose_name='Время старта рассылки', **NULLABLE)
    end_time = models.DateTimeField(verbose_name='Время конца рассылки', **NULLABLE)
    frequency = models.CharField(verbose_name='Частота отправки', max_length=150, choices=FREQUENCY_CHOICES,
                                 default=MONTHLY)
    status_of_mailing = models.CharField(verbose_name='Состояние рассылки', choices=STATUS_OF_MAILING, default=CREATE)

    is_active = models.BooleanField(verbose_name='Статус попытки', default=True)
    clients = models.ManyToManyField(Client, verbose_name="Клиенты")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, verbose_name='компания', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)
    mail = models.ManyToManyField(MailingText, verbose_name="Сообщение для отправки")

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        permissions = [
            ("can_view_mailing", "Может видеть все рассылки"),
            ("can_disable_mailing", "Может отключать рассылки"),
            ("cannot_change_mailing", "Не может изменять рассылки"),
            ("cannot_delete_mailing", "Не может удалять рассылки"),
            ("cannot_create_mailing", "Не может создавать рассылки"),
        ]


class Status(models.Model):
    last_attempt = models.DateTimeField(verbose_name='Дата и время первой рассылки', auto_now=True, **NULLABLE)
    last_attempt_status = models.BooleanField(verbose_name='Статус последней попытки', max_length=75, **NULLABLE)

    theme = models.ForeignKey(MailingText, verbose_name='Письмо', on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE, **NULLABLE)
    mailing_list = models.ForeignKey(Mailing, verbose_name='Рассылки', on_delete=models.CASCADE, **NULLABLE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, verbose_name='компания', **NULLABLE)
    server_response = models.CharField(verbose_name='Ответ', **NULLABLE)

    def __str__(self):
        return f'Письмо {self.theme} для {self.client}'

    class Meta:
        verbose_name = 'Конфиг_письма'
        verbose_name_plural = 'Конфиг_письма'
