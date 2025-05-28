from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp

# Create your views here.
def manage(request):
    return render(request, 'emp/home.html',{})

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