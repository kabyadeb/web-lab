from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth.models import User,auth
# from django.contrib.auth import authenticate,login,logout

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            
            return render(request,'login.html',{'message':"Invalid credentials"})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(first_name)
        if password1==password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html',{'message':'username taken...'})
            
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "user created...")
                return redirect('login')
        else:
            return render(request, 'register.html',{'message':'password not matched...'})
        
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
