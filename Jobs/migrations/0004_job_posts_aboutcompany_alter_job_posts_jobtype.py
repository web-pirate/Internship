# Generated by Django 4.0.4 on 2022-07-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0003_rename_companywebsite_job_posts_companymail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_posts',
            name='aboutcompany',
            field=models.TextField(default='dsdasdsd'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job_posts',
            name='jobtype',
            field=models.CharField(choices=[('full-time', 'full-time'), ('part-time', 'part-time')], default=None, max_length=20, null=True),
        ),
    ]
