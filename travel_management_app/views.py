# views.py
from django.contrib.auth import authenticate,login as auth_login
from django.shortcuts import render,redirect
from.forms import Loginform,Signupform



def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('n1')
        password = request.POST.get('p1')
        user = authenticate(username = username,password = password)
        if user is not None:
            auth_login(request,user)
            return redirect('/travel_management_app/success/')
    return render(request,"login.html")

def signup(request):
    if request.method=='POST':
        form=Signupform(request.POST)
        if form.is_valid ():
            form.save()
            return redirect('/travel_management_app/success/')
    else:
        form=Signupform()
    return render(request,'signup.html',{'forms':form})



def success(request):
    return render(request,"success.html")