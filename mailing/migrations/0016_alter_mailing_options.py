# Generated by Django 5.0.6 on 2024-06-05 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0015_alter_client_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'permissions': [('can_view_mailing', 'Может видеть все рассылки'), ('can_disable_mailing', 'Может отключать рассылки'), ('cannot_change_mailing', 'Не может изменять рассылки'), ('cannot_delete_mailing', 'Не может удалять рассылки'), ('cannot_create_mailing', 'Не может создавать рассылки')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]
