# Generated by Django 3.1.5 on 2021-12-18 19:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0062_pinboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='pinboard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pinboard',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
