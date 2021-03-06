# Generated by Django 4.0.4 on 2022-07-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job_posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=50)),
                ('jobcategory', models.CharField(max_length=50)),
                ('companyname', models.CharField(max_length=50)),
                ('companywebsite', models.EmailField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('jobtype', models.CharField(choices=[('full-time', 'full-time'), ('part-time', 'part-time')], default=None, max_length=20, null=True)),
                ('jobtags', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('experience', models.CharField(max_length=50)),
                ('jobdescription', models.TextField()),
            ],
        ),
    ]
