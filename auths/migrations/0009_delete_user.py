# Generated by Django 3.1.6 on 2021-02-18 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0008_user_full_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
