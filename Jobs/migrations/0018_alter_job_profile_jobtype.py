# Generated by Django 4.0.4 on 2022-07-15 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0017_job_profile_requirements_job_profile_benefits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_profile',
            name='jobtype',
            field=models.CharField(choices=[('full-time', 'full-time'), ('part-time', 'part-time')], default=None, max_length=20, null=True),
        ),
    ]
