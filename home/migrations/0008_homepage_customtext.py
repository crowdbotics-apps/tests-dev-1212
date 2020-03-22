# Generated by Django 2.2.9 on 2020-03-22 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homepage_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='customText',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homepage_customText', to='home.CustomText'),
        ),
    ]
