# Generated by Django 5.0.6 on 2024-06-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_remove_mailingattempt_mailing_mailing_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='client',
        ),
        migrations.AddField(
            model_name='mailing',
            name='clients',
            field=models.ManyToManyField(related_name='mailings', to='mailing.client', verbose_name='Клиенты'),
        ),
    ]
