# Generated by Django 3.1.5 on 2021-11-19 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0052_auto_20211119_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='nbateam',
            name='city',
            field=models.CharField(default='las vegas', max_length=255),
        ),
    ]