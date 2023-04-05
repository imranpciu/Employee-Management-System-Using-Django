from django.db import models

# Create your models here.
class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20)
    emp_id = models.CharField(max_length=50)
    department = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# class Department(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name