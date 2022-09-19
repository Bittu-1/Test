from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Customer, Employee

# Create your views here.


def view_home(request):
    resp = render(request, 'cms/home.html')
    return resp


def view_show(request):
    resp = render(request, 'cms/show.html')
    return resp


def view_dtl(request):
    d1 = {'a': 110, 'b': 200}
    resp = render(request, 'cms/dtl.html', context=d1)
    return resp


def cms_view(request):
    if request.method == "GET":
        resp = render(request, "cms/harsit.html")
        return resp
    elif request.method == "POST":
        if 'btnadd' in request.POST:
            cus = Customer()
            cus.name = request.POST.get('btntxt', 'NA')
            cus.address = request.POST.get('btnaddress', 'NA')
            cus.age = int(request.POST.get('btnage', 0))
            cus.mobileno = request.POST.get('btnmob', 'Na')
            cus.save()
            resp = HttpResponse(
                "<h1>Customer Added Successfully!!" + str(cus.id)+"</h1 >")
            return resp
        elif 'btnsearch' in request.POST:
            cusid = int(request.POST.get('btnid', 0))
            cus = Customer.objects.get(id=cusid)
            d1 = {'cus': cus}
            resp = render(request, 'cms/harsit.html', context=d1)
            return resp
        elif 'btnupdate' in request.POST:
            cus = Customer()
            cus.id = int(request.POST.get('btnid', 0))
            if Customer.objects.filter(id=cus.id).exists():
                cus.name = request.POST.get('btntxt', 'NA')
                cus.address = request.POST.get('btnaddress', 'NA')
                cus.age = int(request.POST.get('btnage', 0))
                cus.mobileno = request.POST.get('btnmob', 'Na')
                cus.save()
                resp = HttpResponse(
                    "<h1>Customer Updated Successfully!!" + str(cus.id)+"</h1>")
                return resp
        elif 'btndelete' in request.POST:
            cus = Customer()
            cus.id = int(request.POST.get('btnid', 0))
            Customer.objects.filter(id=cus.id).delete()
            resp = HttpResponse(
                "<h1>Customer deleted Successfully!!" + str(cus.id)+"</h1>")
            return resp
        elif 'btnshow' in request.POST:
            allcus = Customer.objects.all()
            d1 = {'allcus': allcus}
            resp = render(request, 'cms/harsit.html', context=d1)
            return resp


def view_Emp(request):
    if request.method == 'GET':
        resp = render(request, 'cms/prince.html')
        return resp
    elif request.method == "POST":
        if 'btnadd' in request.POST:
            emp = Employee()
            emp.name = request.POST.get('btntxt', 'NA')
            emp.address = request.POST.get('btnaddress', 'NA')
            emp.age = int(request.POST.get('btnage', 0))
            emp.city = request.POST.get('btncity', 'Na')
            emp.salary = int(request.POST.get('btnsalary', 0))
            emp.designation = request.POST.get('btndsg', 'NA')
            emp.save()
            resp = HttpResponse(
                "<h1>Employee Added Successfully!!" + str(emp.id)+"</h1 >")
            return resp
        elif 'btnsearch' in request.POST:
            empid = int(request.POST.get('btnid', 0))
            emp = Employee.objects.get(id=empid)
            d1 = {'emp': emp}
            resp = render(request, 'cms/prince.html', context=d1)
            return resp
        elif 'btnupdate' in request.POST:
            emp = Employee()
            emp.id = int(request.POST.get('btnid', 0))
            if Employee.objects.filter(id=emp.id).exists():
                emp.name = request.POST.get('btntxt', 'NA')
                emp.address = request.POST.get('btnaddress', 'NA')
                emp.age = int(request.POST.get('btnage', 0))
                emp.city = request.POST.get('btncity', 'Na')
                emp.salary = int(request.POST.get('btnsalary', 0))
                emp.designation = request.POST.get('btndsg', 'NA')
                emp.save()
                resp = HttpResponse(
                    "<h1>Employee Updated Successfully!!" + str(emp.id)+"</h1>")
                return resp
        elif 'btndelete' in request.POST:
            emp = Employee()
            emp.id = int(request.POST.get('btnid', 0))
            Employee.objects.filter(id=emp.id).delete()
            resp = HttpResponse(
                "<h1>Employee deleted Successfully!!" + str(emp.id)+"</h1>")
            return resp
        elif 'btnshow' in request.POST:
            allemp = Employee.objects.all()
            d1 = {'allemp': allemp}
            resp = render(request, 'cms/prince.html', context=d1)
            return resp
