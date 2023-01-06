
from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,'Employee_Details\index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context= {
        'emps': emps
    }

    return render(request,'Employee_Details\complete_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        firstname=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['Department'])
        role=int(request.POST['role'])
        
        new_employe=Employee(first_name=firstname,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_employe.save()
        return HttpResponse("<center><h1>Employee added successfully</h1></center>")

    else:
        return render(request,'Employee_Details\employee_add.html')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_remove=Employee.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            return HttpResponse("<center><h1>Employee has removed successfully!</h1></center>")
        except:
            return HttpResponse("<center><h1>Please select properly!</h1></center>")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'Employee_Details\employee_removal.html',context)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role)
        context={
            'emps':emps
        }
        return render(request,'Employee_Details\complete_emp.html',context)


    return render(request,'Employee_Details\employee_filter.html')


