# Generated by Django 3.1.5 on 2021-11-19 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0050_nbateam_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nbateam',
            name='worth',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]