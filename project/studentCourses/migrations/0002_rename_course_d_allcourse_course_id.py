# Generated by Django 3.2.9 on 2021-11-20 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentCourses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allcourse',
            old_name='course_d',
            new_name='course_id',
        ),
    ]
