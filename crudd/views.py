from email.headerregistry import Address
from unicodedata import name
from webbrowser import get
from django.shortcuts import render,redirect
from .models import employee
from qrcode import *
data=None

# Create your views here.
def index(request):
    emp = employee.objects.all()
    return render(request, 'index.html', {'emp':emp})

def addEmployee(request):
    nameVal = request.POST.get('name')
    emailVal = request.POST.get('email')
    addressVal = request.POST.get('address')
    phoneVal = request.POST.get('phone')
    employee(Name=nameVal, Email = emailVal, Address = addressVal, Phone = phoneVal).save()
    return redirect('/crud')

def editEmployee(request,id):
    nameVal = request.POST.get('name')
    emailVal = request.POST.get('email')
    addressVal = request.POST.get('address')
    phoneVal = request.POST.get('phone')
    employee(id=id,Name=nameVal, Email = emailVal, Address = addressVal, Phone = phoneVal).save()
    return redirect('/crud')

def deleteEmployee(request,id):
    # if request.method == 'POST':
    employee.objects.filter(id=id).delete()
    return redirect('/crud')

def homepage(request):
    return render(request,"Homepage.html")

def qr(request):
    global data
    if request.method=="POST":
        data=request.POST['data']
        img=make(data)
        img.save("static/image/test.png")
    else:
        pass
    return render(request,"qrcode.html",{'data':data})
