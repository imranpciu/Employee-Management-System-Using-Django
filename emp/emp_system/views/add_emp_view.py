from django.shortcuts import render, redirect
from emp_system.models import Employee
from django.shortcuts import HttpResponse
# Create your views here.
def add_emp(request):
    if request.method == "POST":
        # fetch data
        full_name = request.POST.get("emp_name")
        emp_email = request.POST.get("emp_email")
        emp_phone = request.POST.get("emp_phone")
        emp_id = request.POST.get("emp_id")
        emp_department = request.POST.get("emp_department")

        #Creating model object and set 
        emps = Employee()
        emps.full_name = full_name
        emps.email = emp_email
        emps.phone_number = emp_phone
        emps.emp_id = emp_id
        emps.department = emp_department

        # seve data to database
        emps.save()


        return redirect('/emp/')
    return render(request, "add_emp.html", {})


