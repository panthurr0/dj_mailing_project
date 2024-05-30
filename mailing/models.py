from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    name = models.CharField(verbose_name='ФИО', **NULLABLE)
    email = models.EmailField(verbose_name='Контактный email', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('name',)


class MailingText(models.Model):
    theme = models.CharField(verbose_name='Тема письма', max_length=150, **NULLABLE)
    body = models.TextField(verbose_name='Тело письма', **NULLABLE)

    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('theme',)


class Mailing(models.Model):
    theme = models.ForeignKey(MailingText, on_delete=models.SET_NULL, null=True)
    first_attempt = models.DateTimeField(verbose_name='Дата и время первой рассылки', auto_now=True)
    periodicity = models.CharField(verbose_name='Периодичность', max_length=150, **NULLABLE)
    status = models.CharField(verbose_name='Статус', max_length=75, **NULLABLE)

    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ('theme',)


class MailingAttempt(models.Model):
    SUCCESS = 'success'
    FAILURE = 'failure'

    STATUS_CHOICES = [(SUCCESS, 'Успешно'), (FAILURE, 'Не успешно'),
                      ]

    mailing = models.ForeignKey(Mailing, on_delete=models.SET_NULL, null=True)
    last_attempt = models.DateTimeField(verbose_name='дата и время последней попытки', auto_now=True)
    status = models.BooleanField(verbose_name='Статус попытки', max_length=7, choices=STATUS_CHOICES, default=FAILURE)
    answer = models.CharField(verbose_name='Ответ почтового сервиса', **NULLABLE)

    def __str__(self):
        return f'Попытка {self.mailing}: {self.status}'

    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'
        ordering = ('mailing',)
