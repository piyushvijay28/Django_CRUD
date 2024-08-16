from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Employee


def Index(request):
    emp = Employee.objects.all()
    context = {
        "emp":emp
    }
    return render(request, 'index.html', context)

def Add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        
        emp.save()
    return redirect('home')

def Edit(request):
    emp = Employee.objects.all()

    context = {
        "emp" : emp
    }

    return redirect(request, 'index.html', context)

def Update(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone,
        )
        
        emp.save()

        return redirect('home')
    return redirect(request,'index.html')

def Delete(request,id):
    emp = Employee.objects.filter(id = id)
    emp.delete()
    context = {
        'emp' : emp
    }
    return redirect('home')
    return render(request, 'index.html',context)