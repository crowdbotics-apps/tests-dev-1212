# Generated by Django 2.2.9 on 2020-03-21 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200321_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_test', to='home.HomePage'),
        ),
    ]