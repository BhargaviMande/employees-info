from django.shortcuts import render,HttpResponse
from .models import employee,role,department
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')
def all_emp(request):
    emps=employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus =int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        role =int(request.POST['role'])
        department =int(request.POST['department'])
        hire_date = request.POST['hire_date']
        location = request.POST['location']
        s1=employee(first_name=first_name, last_name=last_name,salary=salary,bonus=bonus,phone=phone, role_id=role,department_id=department,hire_date=hire_date,location=location)
        s1.save()
        return HttpResponse('employee added successfully')
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse('exception occured')
def delete_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_be_removed = employee.objects.get(id=emp_id)
            emp_be_removed.delete()
            return HttpResponse('employe removed successfully')
        except:
            return HttpResponse('please enter a valid employee id')


    emps = employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'delete_emp.html',context)
def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        department = request.POST['department']
        role = request.POST['role']
        emps=employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name)) | Q(last_name__icontains=name)
        if department:
            emps = emps.filter(deparment__name__icontains=department)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('an exception occured')



