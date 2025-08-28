from django.shortcuts import render,redirect
from django .contrib.auth.models import User
from django .contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'todoapp/todo.html',{})
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if len(password)<3:
            messages.error(request,'Password must be at least 3 characters long.')
            return redirect('register')
        get_all_users=User.objects.filter(username=username)
        if get_all_users:
            messages.error(request,'Username already exists. Please choose a different username.')
            return redirect('register')
        new_user=User.objects.create_user(username,email,password)
        new_user.save()
        messages.success(request,'User registered successfully. Please log in.')
        return redirect('login')
    
      
    return render(request,'todoapp/register.html',{})
def login(request):
    if request.method==" POST":
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        validate_user=authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('homepage')
        else:
            messages.error(request,'Invalid credentials. Please try again.')
            return redirect('login')

    return render(request,'todoapp/login.html',{})