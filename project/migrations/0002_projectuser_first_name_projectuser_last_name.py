# Generated by Django 5.2.1 on 2025-06-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectuser',
            name='first_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='projectuser',
            name='last_name',
            field=models.TextField(null=True),
        ),
    ]
