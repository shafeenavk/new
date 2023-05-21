from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from collegeapp.models import Department, Courses


# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User(username=username,password=password)
        user.save()


    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        user=User(username=username,password=password)
        user.save()
        return redirect("/login")
    return render(request,"register.html")
def new(request):
    department=Department.objects.all()
    courses=Courses.objects.all()
    return render(request,"new.html",{'department':department,'courses':courses})
def submit(request):
    return render(request,'submit.html')