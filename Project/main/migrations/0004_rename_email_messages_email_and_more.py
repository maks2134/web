# Generated by Django 4.2.4 on 2023-09-03 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_messages_sur_name_alter_messages_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='messages',
            old_name='First_name',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='messages',
            old_name='Last_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='Message',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='Sur_name',
        ),
    ]
