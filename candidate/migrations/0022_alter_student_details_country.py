# Generated by Django 4.0.4 on 2022-07-14 13:53

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0021_student_details_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
