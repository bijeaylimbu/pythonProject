# Generated by Django 3.1.5 on 2021-02-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_add', '0040_auto_20210211_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadd_bikes',
            name='usedFor',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
