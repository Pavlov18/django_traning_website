# Generated by Django 4.2.3 on 2023-08-09 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telebot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telesettings',
            old_name='message',
            new_name='tg_message',
        ),
    ]
