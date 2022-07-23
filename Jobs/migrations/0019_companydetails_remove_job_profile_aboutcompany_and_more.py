# Generated by Django 4.0.4 on 2022-07-15 15:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0018_alter_job_profile_jobtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='companydetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('logo', models.ImageField(default='', upload_to='companylogos')),
                ('companyname', models.CharField(max_length=200)),
                ('companysize', models.IntegerField()),
                ('companyaddress', models.CharField(max_length=50)),
                ('companyphone', models.CharField(max_length=50)),
                ('companyemail', models.EmailField(max_length=50)),
                ('companywebsite', models.URLField()),
                ('aboutcompany', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='job_profile',
            name='aboutcompany',
        ),
        migrations.RemoveField(
            model_name='job_profile',
            name='companymail',
        ),
        migrations.AlterField(
            model_name='job_profile',
            name='jobtype',
            field=models.CharField(choices=[('part-time', 'part-time'), ('full-time', 'full-time')], default=None, max_length=20, null=True),
        ),
    ]