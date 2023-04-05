from django.shortcuts import render,redirect
from emp_system.models import Employee
def emp_update(request, id):
    emp = Employee.objects.get(id = id)
    return render(request, "update_emp.html",{"emp": emp})

def emp_do_update(request, id):
    # fetch data
    if request.method == "POST":
        full_name = request.POST.get("emp_name")
        emp_email = request.POST.get("emp_email")
        emp_phone = request.POST.get("emp_phone")
        emp_id = request.POST.get("emp_id")
        emp_department = request.POST.get("emp_department")

    empu = Employee.objects.get(id = id)
    #Creating model object and set 
    empu.full_name = full_name
    empu.email = emp_email
    empu.phone_number = emp_phone
    empu.emp_id = emp_id
    empu.department = emp_department

    # seve data to database
    empu.save()
    
    return redirect("/emp/index")
