# Generated by Django 2.2.1 on 2019-08-20 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_food_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lol_Champs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champ_name', models.CharField(max_length=200)),
            ],
        ),
    ]
