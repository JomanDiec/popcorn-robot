# Generated by Django 3.1.5 on 2021-11-20 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0059_auto_20211119_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='nbateam',
            name='city',
        ),
    ]