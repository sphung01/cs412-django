# Generated by Django 5.2.1 on 2025-06-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.TextField()),
                ('first_name', models.TextField()),
                ('street_number', models.TextField()),
                ('street_name', models.TextField()),
                ('apartment_number', models.TextField()),
                ('zip_code', models.CharField(max_length=5)),
                ('date_of_birth', models.DateField()),
                ('date_of_registration', models.DateField()),
                ('party_affiliation', models.CharField(max_length=2)),
                ('precinct_number', models.IntegerField()),
                ('v20state', models.BooleanField()),
                ('v21town', models.BooleanField()),
                ('v21primary', models.BooleanField()),
                ('v22general', models.BooleanField()),
                ('v23town', models.BooleanField()),
                ('voter_score', models.IntegerField()),
            ],
        ),
    ]
