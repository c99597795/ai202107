# Generated by Django 3.2.5 on 2021-07-13 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]