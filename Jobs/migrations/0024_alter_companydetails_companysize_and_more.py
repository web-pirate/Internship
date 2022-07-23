# Generated by Django 4.0.4 on 2022-07-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0023_rename_requirements_job_profile_requirements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetails',
            name='companysize',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job_profile',
            name='benefits',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job_profile',
            name='jobdescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job_profile',
            name='jobtype',
            field=models.CharField(choices=[('part-time', 'part-time'), ('full-time', 'full-time')], default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='job_profile',
            name='requirements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job_profile',
            name='responsibilities',
            field=models.TextField(blank=True, null=True),
        ),
    ]
