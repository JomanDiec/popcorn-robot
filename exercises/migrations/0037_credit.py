# Generated by Django 3.1.5 on 2021-09-19 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0036_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('card', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
