from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = auth.authenticate(username=username, password=password, email=email)
        if User is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('signup')

    return render(request, "signup.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['retype password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email is already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=email,
                                                password=password)
                user.save();
                return redirect('signup')
        else:
            messages.info(request, "email is already taken")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
# Create your views here.
