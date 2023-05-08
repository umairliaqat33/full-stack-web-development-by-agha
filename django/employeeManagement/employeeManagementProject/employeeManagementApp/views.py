from django.shortcuts import render, HttpResponse
from .models import Employee, Roles, Department
from datetime import datetime
# Create your views here.


def index(request):
    return render(request, 'index.html')


def view_all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, "view_all_emp.html", context)


def add_emp(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        depat = request.POST['dept']
        role = request.POST['role']
        hire_date = request.POST['hire_date']
        new_emp = Employee(firstName=firstName, lastName=lastName, salary=salary,
                           bonus=bonus, phone=phone, dept=Department(), role=Roles(), hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("University Employee added Successfully")
    elif request.method == "GET":
        return render(request, "add_emp.html")
    else:
        return HttpResponse('An Exception Occured, Employee was not added')


def remove_emp(request):
    return render(request, "remove_emp.html")


def filter_emp(request):
    return render(request, "filter_emp.html")
