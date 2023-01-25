from django.shortcuts import render,redirect
from . models import Portfolio
from . forms import FormContact,FormBilling
from django.contrib.auth import authenticate
from django.contrib import auth,messages
from django.contrib.auth.models import User
import razorpay


def Home(request):
    form = FormContact(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    data = Portfolio.objects.all()
    
    return render(request, 'index.html', {'data':data, 'form':form})

def Subscribe(request):
    forms = FormBilling(request.POST)
    if forms.is_valid():
        forms.save()
        return redirect('success')
    return render(request, 'subscribe.html', {'forms':forms})

def Successview(request):
    return render(request, 'success.html')

def Profile(request):
    data = Portfolio.objects.all()
    return render(request, 'profile.html', {'data':data})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def Join(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, "User Already Exists")
                return redirect('join')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
        else:
            messages.info(request, "Password Mismatch")
            return redirect('join')
        return redirect('login')
    return render(request, 'join.html')

def Workview(request):
    return render(request, 'works.html')