# Generated by Django 3.2.18 on 2023-04-18 12:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]