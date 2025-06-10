from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp

# Create your views here.
def manage(request):

    emps= Emp.objects.all()

    return render(request, 'emp/home.html',{'emps':emps})

def add_emp(request): 
    if(request.method=="POST"):
        # data feth
        emp_name= request.POST.get("emp_name")
        emp_id= request.POST.get("emp_id")
        emp_phone= request.POST.get("emp_phone")
        emp_address= request.POST.get("emp_address")
        emp_working= request.POST.get("emp_working")
        emp_department= request.POST.get("emp_department")

        #create models obj
        e=Emp()
        e.name=emp_name
        e.email_id =emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department

        if emp_working is None:
            e.working =False
        else:
            e.working=True
        
        # save korbo
        e.save()


        return redirect('/emp/manage')

    return render(request, 'emp/add_emp.html',{})


def about(request):
    return render(request,'emp/about.html',{})

def delete_emp(request, emp_id):
    print(emp_id)
    emp =Emp.objects.get(pk=emp_id)
    emp.delete()

    return redirect('/emp/manage')

def update_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    return render(request, 'emp/update_emp.html',{
        'emp':emp
    })

from django.shortcuts import redirect, get_object_or_404
from .models import Emp

def do_update(request, emp_id):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        emp = get_object_or_404(Emp, pk=emp_id)  # safely fetch existing record

        emp.name = emp_name
        emp.phone = emp_phone
        emp.address = emp_address
        emp.department = emp_department
        emp.working = emp_working is not None  # checkbox handling

        emp.save()

        return redirect('/emp/manage/')
    else:
        return HttpResponseNotAllowed(['POST'])
