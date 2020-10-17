from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    return render(request, 'student/home.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'student/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'student/signup.html', {'error': 'Passwords must match'})
    else:
        # wants to enter info
        return render(request, 'student/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            return render(request, 'student/login.html', {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'student/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def profile(request):
    return render(request, 'student/profile.html')

def dashboard(request):
    return render(request, 'student/dashboard.html')

def payment(request):
    return render(request, 'student/payment.html')

def stats(request):
    return render(request, 'student/stats.html')

def schedule(request):
    return render(request, 'student/schedule.html')

