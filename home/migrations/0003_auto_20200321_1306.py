# Generated by Django 2.2.9 on 2020-03-21 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_auto_20200320_2049"),
    ]

    operations = [
        migrations.RemoveField(model_name="customtext", name="test",),
        migrations.RemoveField(model_name="customtext", name="user_test",),
    ]
