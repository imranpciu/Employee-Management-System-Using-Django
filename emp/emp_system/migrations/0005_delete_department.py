# Generated by Django 4.1.7 on 2023-03-29 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_system', '0004_alter_employee_department'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Department',
        ),
    ]