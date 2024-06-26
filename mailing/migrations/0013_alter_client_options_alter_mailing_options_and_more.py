# Generated by Django 5.0.6 on 2024-06-05 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0012_alter_client_options_client_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('name',), 'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='mailing',
            options={'permissions': [('can_view_all_newsletter', 'Может видеть все рассылки'), ('can_disable_newsletter', 'Может отключать рассылки'), ('cannot_change_newsletter', 'Не может изменять рассылки'), ('cannot_delete_newsletter', 'Не может удалять рассылки'), ('cannot_create_newsletter', 'Не может создавать рассылки')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
        migrations.AlterModelOptions(
            name='mailingtext',
            options={'permissions': [('cann_change_textfornewsletter_list', 'Может изменять текст для рассылок')], 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
    ]
