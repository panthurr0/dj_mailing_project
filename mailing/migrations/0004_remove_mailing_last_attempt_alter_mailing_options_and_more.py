# Generated by Django 5.0.6 on 2024-06-03 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_remove_mailing_client_mailing_clients'),
        ('users', '0002_company_remove_user_phone_number_user_token_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='last_attempt',
        ),
        migrations.AlterModelOptions(
            name='mailing',
            options={'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='first_attempt',
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='periodicity',
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='status',
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='theme',
        ),
        migrations.AddField(
            model_name='client',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.company', verbose_name='компания'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='answer',
            field=models.BooleanField(default=True, verbose_name='Статус попытки'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.company', verbose_name='компания'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время конца рассылки'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='frequency',
            field=models.CharField(choices=[('раз в день', 'Ежедневно'), ('раз в неделю', 'Еженедельно'), ('раз в месяц', 'Ежемесячно')], default='раз в месяц', max_length=150, verbose_name='Частота отправки'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='is_active',
            field=models.CharField(choices=[('Создана', 'Создана'), ('В работе', 'Запущена'), ('Завершена', 'Завершена'), ('Ошибка отправки', 'Ошибка отправки')], default='Создана', verbose_name='Состояние рассылки'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='mail',
            field=models.ManyToManyField(to='mailing.mailingtext', verbose_name='Сообщение для отправки'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время старта рассылки'),
        ),
        migrations.AddField(
            model_name='mailingtext',
            name='clients',
            field=models.ManyToManyField(blank=True, to='mailing.client', verbose_name='Клиенты для рассылки'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, unique=True, verbose_name='Контактный email'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='clients',
            field=models.ManyToManyField(to='mailing.client', verbose_name='Клиенты'),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата и время первой рассылки')),
                ('status', models.BooleanField(blank=True, max_length=75, null=True, verbose_name='Статус последней попытки')),
                ('server_response', models.CharField(blank=True, null=True, verbose_name='Ответ')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.client', verbose_name='Клиент')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.company', verbose_name='компания')),
                ('mailing_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='Рассылки')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.mailingtext', verbose_name='Письмо')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письмо',
            },
        ),
        migrations.DeleteModel(
            name='MailingAttempt',
        ),
    ]
