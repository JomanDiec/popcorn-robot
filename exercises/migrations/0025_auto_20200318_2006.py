# Generated by Django 2.2.1 on 2020-03-19 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0024_auto_20200318_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nbateam',
            name='worth',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
