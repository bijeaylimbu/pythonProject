# Generated by Django 3.1.5 on 2021-02-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_add', '0043_auto_20210211_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadd_fashion',
            name='usedFor',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
