# Generated by Django 4.2.4 on 2023-09-03 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_email_messages_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='email',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='message',
        ),
    ]