from django.shortcuts import render, redirect
from emp_system.models import Employee
def emp_delete(request, id):
    emp = Employee.objects.get(id = id) #we can use pk = emp_id
    emp.delete()
    return redirect("/emp/index")