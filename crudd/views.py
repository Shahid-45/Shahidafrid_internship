from email.headerregistry import Address
from email.mime import image
from pickle import FALSE
import profile
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
    imgVal = request.FILES.get('profile')
    nameVal = request.POST.get('name')
    emailVal = request.POST.get('email')
    addressVal = request.POST.get('address')
    phoneVal = request.POST.get('phone')
    employee(profile = imgVal,Name=nameVal, Email = emailVal, Address = addressVal, Phone = phoneVal).save()
    return redirect('/crud')

def editEmployee(request,id):
    nameVal = request.POST.get('name')
    emailVal = request.POST.get('email')
    addressVal = request.POST.get('address')
    phoneVal = request.POST.get('phone')
    if 'profile' in request.FILES:
        imgVal = request.FILES.get('profile')
        employee(id=id,profile = imgVal,Name=nameVal, Email = emailVal, Address = addressVal, Phone = phoneVal).save()
    else:
        img = employee.objects.filter(id=id)[0]
        image = img.profile
        employee(id=id,profile=image,Name=nameVal, Email = emailVal, Address = addressVal, Phone = phoneVal).save()

    
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

def cap(request):
    return render(request,"captcha.html")