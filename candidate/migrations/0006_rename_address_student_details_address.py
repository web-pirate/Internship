# Generated by Django 4.0.4 on 2022-06-30 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_rename_phonenumber_student_details_pnumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_details',
            old_name='Address',
            new_name='address',
        ),
    ]