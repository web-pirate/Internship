# Generated by Django 4.0.4 on 2022-07-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0004_job_posts_aboutcompany_alter_job_posts_jobtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_posts',
            name='jobtype',
            field=models.CharField(choices=[('part-time', 'part-time'), ('full-time', 'full-time')], default=None, max_length=20, null=True),
        ),
    ]
