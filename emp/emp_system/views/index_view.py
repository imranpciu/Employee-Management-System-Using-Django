from django.shortcuts import render
from emp_system.models import Employee
def index(request):
    all_emp = Employee.objects.all()
    return render(request, "index.html", {
        'all_emp':all_emp,
    })
