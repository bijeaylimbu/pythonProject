# Generated by Django 3.1.5 on 2021-01-31 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_add', '0005_auto_20210131_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postadd_car',
            name='username',
        ),
    ]
