# Generated by Django 4.1.7 on 2023-03-28 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='is_working',
        ),
    ]