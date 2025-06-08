from django.shortcuts import render

def employee(request):
    return render(request, 'home.html',{})

def dashboard(request):
    return render(request,'emp/dashboard.html',{})