# Generated by Django 3.1.5 on 2022-01-14 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask_it', '0003_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='question',
            new_name='parent',
        ),
    ]
