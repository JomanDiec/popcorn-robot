# Generated by Django 3.1.5 on 2021-11-19 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0055_nbateam_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='nbateam',
            name='ticket_sales',
            field=models.IntegerField(default=3000),
            preserve_default=False,
        ),
    ]
