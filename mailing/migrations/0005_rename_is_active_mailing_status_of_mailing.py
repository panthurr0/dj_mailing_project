# Generated by Django 5.0.6 on 2024-06-03 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_remove_mailing_last_attempt_alter_mailing_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailing',
            old_name='is_active',
            new_name='status_of_mailing',
        ),
    ]